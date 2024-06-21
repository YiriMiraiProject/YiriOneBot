from typing import Any, Dict, List, Literal, Optional

from mirai_onebot.api.interfaces.base import (Request, RequestParams, Response,
                                              ResponseData)

__all__ = [
    'SendMessageRequest', 'SendMessageResponse', 'SendMessageRequestParams', 'SendMessageResponseData', 'DeleteMessageRequest', 'DeleteMessageResponse', 'DeleteMessageRequestParams'
]

# ========= SendMessage =========


class SendMessageRequestParams(RequestParams):
    detail_type: Literal['private', 'group', 'channel']
    group_id: Optional[str] = None  # 用于群组消息
    user_id: Optional[str] = None   # 用于私聊消息
    guild_id: Optional[str] = None  # 用于频道消息
    channel_id: Optional[str] = None  # 用于频道消息
    message: List[Dict[str, Any]]


class SendMessageResponseData(ResponseData):
    message_id: str
    time: float


class SendMessageRequest(Request):
    action: str = 'send_message'
    params: SendMessageRequestParams


class SendMessageResponse(Response):
    data: SendMessageResponseData

# ========= DeleteMessage =========


class DeleteMessageRequestParams(RequestParams):
    message_id: str


class DeleteMessageRequest(Request):
    action: str = 'delete_message'
    params: DeleteMessageRequestParams

# 撤回消息的响应数据为空


class DeleteMessageResponse(Response):
    pass
