import asyncio
import json
from secrets import token_hex
from typing import Any, Optional

import websockets
from websockets.frames import CloseCode

from yiriob.event import EventBus
from yiriob.utils import logger

from .base import Adapter


class ReverseWebsocketAdapter(Adapter):
    def __init__(self, host: str, port: int, access_token: str, bus: EventBus) -> None:
        super().__init__(access_token, bus)

        self.host = host
        self.port = port

        self.stop_signal: asyncio.Future = asyncio.Future()
        self.wsprotocol: Optional[websockets.WebSocketServerProtocol] = (
            None  # 只和最后一个连接的客户端打交道
        )
        self.response_callbacks: dict[
            str, asyncio.Future[dict[str, Any]]
        ] = {}  # 收到响应后用 echo 作为 key，把 future 的 result 设置成 response 就行

    def _check_access_token(self, token: str) -> bool:
        return token == self.access_token

    async def _handler(self, websocket: websockets.WebSocketServerProtocol):
        # 校验 access_token
        if not self._check_access_token(
            websocket.request_headers.get("Authorization", "")
            .replace("Bearer ", "")
            .strip()
        ):
            await websocket.close(code=3001, reason="Unauthorized")
            return

        # 要求是 Universal 客户端
        if websocket.request_headers.get("X-Client-Role") != "Universal":
            logger.warning(
                "WebSocket 客户端（OneBot 实现）不是一个 Universal 客户端，如果是一个 API 客户端，则无法接收事件；如果是一个 Event 客户端，则无法调用 API！"
            )

        self.wsprotocol = websocket

        # 接收消息
        while True:
            message = await websocket.recv()
            # 数据类型错误（收到 byte 了）
            if not isinstance(message, str):
                logger.warning("WebSocket 客户端（OneBot 实现）发送了一个错误的消息！")
                await websocket.close(code=CloseCode.UNSUPPORTED_DATA)
                return

            data = json.loads(message)

            # 收到事件
            if data.get("post_type", None) is not None:
                self.emit_onebot_event(data)
            # 收到响应
            elif data.get("status", None) is not None:
                echo = data.get("echo", None)

                # 没有 echo
                if echo is None:
                    logger.warning(
                        "WebSocket 客户端（OneBot 实现）发送了一个错误的响应消息："
                    )
                    logger.warning("响应缺少 echo 字段，无法辨别其所属请求。")
                    continue

                callback = self.response_callbacks.get(echo, None)

                # echo 找不着
                if callback is None:
                    logger.warning(
                        "WebSocket 客户端（OneBot 实现）发送了一个错误的响应消息："
                    )
                    logger.warning(f"收到的响应 echo {echo} 没有所属请求。")
                    continue

                callback.set_result(data)
            # 消息不符合 onebot 11 标准
            else:
                await websocket.close(code=CloseCode.UNSUPPORTED_DATA)
                return

    async def _call_api(
        self, action: str, params: dict[str, Any], timeout: int = 20
    ) -> dict[str, Any]:
        if self.wsprotocol is None:
            logger.warning("WebSocket 客户端未连接，无法调用 API。")
            logger.debug("由于上述原因，_call_api 方法返回一个假请求。")
            return {
                "status": "failed",
                "retcode": -1,
                "data": None,
                "echo": token_hex(16),
            }

        echo = token_hex(16)

        await self.wsprotocol.send(
            json.dumps({"action": action, "params": params, "echo": echo})
        )

        callback = asyncio.Future[dict[str, Any]]()
        self.response_callbacks[echo] = callback
        try:
            return await asyncio.wait_for(callback, timeout=timeout)
        except asyncio.TimeoutError:
            raise TimeoutError("调用 API 超时")

    def start(self):
        """启动 Websocket 服务器"""

        async def _server():
            server = await websockets.serve(
                self._handler, host=self.host, port=self.port
            )
            await self.stop_signal
            server.close()

        self.stop_signal = asyncio.Future()  # 重建一个新的，防止之前的已经被取消
        asyncio.get_event_loop().create_task(_server())

    def stop(self):
        """关闭 Websocket 服务器"""
        self.stop_signal.set_result(None)


__all__ = ["ReverseWebsocketAdapter"]
