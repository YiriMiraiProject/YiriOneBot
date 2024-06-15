import asyncio
import json
import secrets
from typing import Any, Dict, List, Optional, Union
from urllib.parse import parse_qs, urlparse

import websockets
import websockets.frames
import websockets.legacy
import websockets.legacy.server

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
        self.server: Optional[websockets.legacy.server.Serve] = None
        self.ws_connections: List[websockets.WebSocketServerProtocol] = []

    def start(self):
        async def start_server():
            self.server = await websockets.serve(self.handler, self.host, self.port)

        asyncio.get_event_loop().create_task(start_server())

    def stop(self):
        if self.server is None:
            return

        tasks: List[asyncio.Task] = []
        for ws in self.ws_connections:
            tasks.append(asyncio.create_task(ws.close()))
        asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

    async def handler(self, websocket: websockets.WebSocketServerProtocol, path: str):
        # 检测OneBot标准版本
        protocol_str = websocket.request_headers.get(
            'Sec-WebSocket-Protocol')

        if protocol_str is None:
            logger.warning('未提供Sec-WebSocket-Protocol，可能出现兼容性问题。')
            logger.warning('自动将 protocol 指定为 11.undefined。')
            protocol_str = '11.undefined'

        protocol = protocol_str.split('.')

        if int(protocol[0]) > 12:
            logger.warning('不支持版本12以上的OneBot实现，可能出现兼容性问题。')
        elif int(protocol[0]) < 11:
            logger.warning(
                f'不支持版本11以下的OneBot实现，可能出现兼容性问题，请在调用api前查询对应OneBot {protocol[0]} 的接口定义。')
        elif int(protocol[0]) == 11:
            logger.warning('OneBot 11 的实现暂处于开发阶段，可能存在兼容性问题。')

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
            await websocket.close(websockets.frames.CloseCode.NORMAL_CLOSURE, 'Unauthorized')

    async def recv(self, websocket: websockets.WebSocketServerProtocol):
        """监听WS客户端消息。

        响应类消息在 interal_event_bus 触发 onebot_resp 事件。

        事件类消息在 外部事件总线 触发 onebot_event 事件。
        """
        if websocket.closed:
            raise ConnectionResetError("连接已关闭")

        # 解析错误
        try:
            try:
                data = json.loads(await websocket.recv())
            except websockets.exceptions.ConnectionClosedOK:
                raise ConnectionResetError("连接已关闭")
            if not isinstance(data, dict):
                logger.warning(f'OneBot 实现 {websocket.remote_address[0]} 发送了非字典数据 {data}。')
                return None
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

    async def _call_api(self, action: str, params: dict, echo: str = secrets.token_hex(8)) -> Union[Dict[str, Any], None]:
        """内部接口。直接调用API。本接口只发送给第一个连接的客户端。

        Args:
            action (str): 参见父类
            params (dict): 参见父类
            echo (str, optional): 参见父类. Defaults to secrets.token_hex(8).
        """

        if len(self.ws_connections) == 0:
            return None

        flag = asyncio.Event()
        response: Optional[Dict[str, Any]] = None

        @self._internal_event_bus.on('onebot_resp')
        async def _on_resp(data: dict):
            nonlocal response, flag

            if data.get('echo', None) == echo:
                self._internal_event_bus.unsubscribe('onebot_resp', _on_resp)
                response = data
                flag.set()

        await self.ws_connections[0].send(json.dumps({
            "action": action,
            "params": params,
            "echo": echo
        }))

        await flag.wait()

        return response
