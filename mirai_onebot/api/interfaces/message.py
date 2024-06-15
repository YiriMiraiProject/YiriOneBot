from mirai_onebot.api.interfaces.base import (Request, RequestParams, Response,
                                              ResponseData)


# ========= SendMessage =========
class SendMessageRequestParams(RequestParams):
    detail_type: str
    group_id: str  # 用于群组消息
    message: list[dict]


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
