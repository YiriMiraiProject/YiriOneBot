from typing import List

from pydantic import BaseModel

from mirai_onebot.api.interfaces.base import (BotSelf, Request, RequestParams,
                                              Response, ResponseData)

__all__ = [
    'GetStatusRequest', 'GetStatusResponse', 'GetStatusRequestParams', 'GetStatusResponseData', 'BotStatus'
]

# ========== GetStatus ==========


class BotStatus(BaseModel):
    self: BotSelf
    online: bool


class GetStatusResponseData(ResponseData):
    good: bool
    bots: List[BotStatus]


class GetStatusRequestParams(RequestParams):
    pass


class GetStatusRequest(Request):
    action: str = 'get_status'
    params: GetStatusRequestParams = GetStatusRequestParams()


class GetStatusResponse(Response):
    data: GetStatusResponseData
