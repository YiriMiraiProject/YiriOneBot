from typing import List

from pydantic import BaseModel

from mirai_onebot.api.interfaces.base import (BotSelf, Request, Response,
                                              ResponseData)


# ========== GetStatus ==========
class BotStatus(BaseModel):
    self: BotSelf
    online: bool


class GetStatusResponseData(ResponseData):
    good: bool
    bots: List[BotStatus]


class GetStatusRequest(Request):
    action: str = 'get_status'
    params: dict = {}


class GetStatusResponse(Response):
    data: GetStatusResponseData
