# 本例提供 Reverse Websocket Adapter 的直接调用效果
# 非专业人员请通过 Bot 类调用 API
import asyncio
from typing import Any

from yiriob.adapters import ReverseWebsocketAdapter
from yiriob.event import EventBus
from yiriob.interface import Interface, InterfaceParams, InterfaceResponse

bus = EventBus()
adapter = ReverseWebsocketAdapter(
    host="127.0.0.1", port=8080, access_token="helloworld", bus=bus
)


class SendGroupMsgParams(InterfaceParams):
    group_id: int
    message: dict[str, Any] | str


class SendGroupMsgResponse(InterfaceResponse):
    message_id: int


class SendGroupMsg(Interface[SendGroupMsgParams, SendGroupMsgResponse]):
    action: str = "send_group_msg"
    params_type: type[SendGroupMsgParams] = SendGroupMsgParams
    response_type: type[SendGroupMsgResponse] = SendGroupMsgResponse


@bus.on("onebot_event")
async def onebot_event(data: dict[Any, str]):
    # 收到事件就调用一次 API（包括心跳）
    await adapter.call_api(
        SendGroupMsg(),
        SendGroupMsgParams(group_id=825435724, message="Hello World"),
    )


adapter.start()
asyncio.get_event_loop().run_forever()
