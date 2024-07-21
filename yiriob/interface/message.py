from typing import Type

from yiriob.interface.base import Interface, InterfaceParams, InterfaceResponse
from yiriob.message import MessageChain


class SendPrivateMessageParams(InterfaceParams):
    user_id: int
    message: MessageChain | str
    auto_escape: bool = False


class SendPrivateMessageResponse(InterfaceResponse):
    message_id: int


class SendPrivateMessageInterface(
    Interface[SendPrivateMessageParams, SendPrivateMessageResponse]
):
    action: str = "send_private_msg"
    params_type: Type[SendPrivateMessageParams] = SendPrivateMessageParams
    response_type: Type[SendPrivateMessageResponse] = SendPrivateMessageResponse


class SendGroupMessageParams(InterfaceParams):
    group_id: int
    message: MessageChain | str
    auto_escape: bool = False


class SendGroupMessageResponse(InterfaceResponse):
    message_id: int


class SendGroupMessageInterface(
    Interface[SendGroupMessageParams, SendGroupMessageResponse]
):
    action: str = "send_group_msg"
    params_type: Type[SendGroupMessageParams] = SendGroupMessageParams
    response_type: Type[SendGroupMessageResponse] = SendGroupMessageResponse


__all__ = [
    "SendPrivateMessageParams",
    "SendPrivateMessageResponse",
    "SendPrivateMessageInterface",
    "SendGroupMessageParams",
    "SendGroupMessageResponse",
    "SendGroupMessageInterface",
]
