import asyncio
import json
import uuid
from typing import List, Literal, Union
from urllib.parse import parse_qs, urlparse

import websockets

from mirai_onebot.adapters.base import Adapter
from mirai_onebot.utils import logging

logger = logging.getLogger(__name__)


class ReverseWebsocketAdapter(Adapter):
    """反向Websocket适配器。

    Args:
        access_token: 访问令牌
        host: WS服务器监听IP
        port: WS服务器监听端口
        timeout: 发送、接收OneBot实现消息的超时时间
    """

    def __init__(self, access_token: str, host: str, port: int, timeout: float) -> None:
        super().__init__(access_token)
        self.host = host
        self.port = port
        self.timeout = timeout
        self.ws_connections: List[websockets.WebSocketServerProtocol] = []

        asyncio.create_task(self.start_server())

    async def start_server(self):
        await websockets.serve(self.handler, self.host, self.port)

    async def handler(self, websocket: websockets.WebSocketServerProtocol, path: str):
        # 检测OneBot标准版本
        protocol = websocket.request_headers.get(
            'Sec-WebSocket-Protocol').split('.')
        if int(protocol[0]) > 12:
            logger.warning('不支持版本12以上的OneBot实现，可能出现兼容性问题。')
        elif int(protocol[0]) < 12:
            logger.warning(
                f'不支持版本12以下的OneBot实现，可能出现兼容性问题，请在调用api前查询对应OneBot {protocol[0]} 的接口定义。')

        # 检测Access Token
        query = parse_qs(urlparse(websocket.path).query)
        if websocket.request_headers.get('Authorization', '').endswith(self.access_token) or query.get('access_token', '') == self.access_token:
            logger.info('一个OneBot实现建立了连接。')
            self.ws_connections.append(websocket)
            while True:
                try:
                    await self.recv(websocket)
                except (ConnectionResetError, websockets.exceptions.ConnectionClosedError):
                    await websocket.wait_closed()
                    logger.info('一个OneBot实现断开了连接。')
                    self.ws_connections.remove(websocket)
                    break
        else:
            logger.warning('一个OneBot实现在建立的过程中未正确传递 access_token，请检查设置。')
            await websocket.close(401, 'Unauthorized')

    async def recv(self, websocket: websockets.WebSocketServerProtocol):
        """监听WS客户端消息"""
        if websocket.closed:
            raise ConnectionResetError("连接已关闭")

        # 解析错误
        try:
            data = await websocket.recv()
            data: dict = json.loads(data)
        except json.JSONDecodeError:
            logger.warning(
                f'无法解析 OneBot 实现 {websocket.remote_address[0]} 的消息 {data}。')
            return None

        # 解析是事件还是响应
        if data.get('detail_type', None) is None and data.get('sub_type', None) is None:  # 是响应或其他
            await self._internal_event_bus.emit('onebot_resp', data=data)
        else:  # 是事件
            # 触发事件
            await self.emit('onebot_event', data)

    async def call_api(self, api: str, **params):
        """调用API

        Returns: 一个数组，包含每个OneBot实现的返回值。
        """
        data = {
            'action': api,
            'params': params
        }

        async def call_server(ws_connection: websockets.WebSocketServerProtocol):
            echo = uuid.uuid4().__str__()

            try:
                await asyncio.wait_for(ws_connection.send(json.dumps({
                    **data,
                    'echo': echo
                })), timeout=self.timeout)

                # 注：不能同时调用两个recv函数，这里使用内部事件总线进行监听
                # return await asyncio.wait_for(ws_connection.recv(), timeout=self.timeout)
                tmp = None
                recived_event = asyncio.Event()

                @self._internal_event_bus.on('onebot_resp')
                async def subscriber(data: dict):
                    if data['echo'] == echo:
                        nonlocal tmp, recived_event
                        tmp = data
                        recived_event.set()
                        self._internal_event_bus.unsubscribe(
                            'onebot_resp', subscriber)

                # 直到收到消息
                await asyncio.wait_for(recived_event.wait(), timeout=self.timeout)

                return tmp
            except (asyncio.CancelledError, asyncio.TimeoutError):
                logger.error(f'发送、接收OneBot实现消息时超时。')
                return -1

        tasks = [call_server(ws_connection)
                 for ws_connection in self.ws_connections]
        return await asyncio.gather(*tasks)
