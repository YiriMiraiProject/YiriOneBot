import asyncio
import json
import uuid
from typing import List, Union
from urllib.parse import parse_qs, urlparse

import websockets
from utils import logging

from mirai_onebot.adapters.base import Adapter

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
        self.ws_servers: List[websockets.WebSocketServerProtocol] = []

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
            self.ws_servers.append(websocket)
            while True:
                try:
                    await self.recv(websocket)
                except (ConnectionResetError, websockets.exceptions.ConnectionClosedError):
                    await websocket.wait_closed()
                    logger.info('一个OneBot实现断开了连接。')
                    self.ws_servers.remove(websocket)
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
            data = json.loads(await websocket.recv())
        except json.JSONDecodeError:
            logger.error(
                f'无法解析 OneBot 实现 {websocket.remote_address[0]} 的消息 {data}。')
            return None

        # 触发事件
        await self.emit('onebot_event', data)

    async def call_api(self, api: str, **params):
        data = json.dumps({
            'action': api,
            'params': params
        })

        async def call_server(ws_server: websockets.WebSocketServerProtocol):
            echo = uuid.uuid4().__str__()

            try:
                await asyncio.wait_for(ws_server.send({
                    **data,
                    'echo': echo
                }), timeout=self.timeout)

                await asyncio.wait_for(ws_server.recv(), timeout=self.timeout)
            except asyncio.CancelledError:
                logger.error(f'发送、接收OneBot实现消息时超时。')

        tasks = [asyncio.create_task(call_server(ws_server))
                 for ws_server in self.ws_servers]
        await asyncio.wait(tasks)

    async def emit(self, event: str, *args, **kwargs) -> None:
        """向事件总线发送事件

        Args:
            event (str): 事件
        """
        tasks = [asyncio.create_task(
            bus.emit(event, *args, **kwargs)) for bus in self.buses]
        await asyncio.gather(*tasks)
