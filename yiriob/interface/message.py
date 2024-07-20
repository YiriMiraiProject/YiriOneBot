from yiriob.interface.base import InterfaceParams, InterfaceResponse, Interface
from yiriob.message import MessageChain


class SendPrivateMessageParams(InterfaceParams):
    user_id: int
    message: MessageChain
    auto_escape: bool = False


class SendPrivateMessageResponse(InterfaceResponse):
    message_id: int


class SendPrivateMessageInterface(
    Interface[SendPrivateMessageParams, SendPrivateMessageResponse]
):
    action = "send_private_msg"
    params_type = SendPrivateMessageParams
    response_type = SendPrivateMessageResponse


class SendGroupMessageParams(InterfaceParams):
    group_id: int
    message: MessageChain
    auto_escape: bool = False


class SendGroupMessageResponse(InterfaceResponse):
    message_id: int


class SendGroupMessageInterface(
    Interface[SendGroupMessageParams, SendGroupMessageResponse]
):
    action = "send_group_msg"
    params_type = SendGroupMessageParams
    response_type = SendGroupMessageResponse


__all__ = [
    "SendPrivateMessageParams",
    "SendPrivateMessageResponse",
    "SendPrivateMessageInterface",
    "SendGroupMessageParams",
    "SendGroupMessageResponse",
    "SendGroupMessageInterface",
]
