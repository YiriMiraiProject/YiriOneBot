import secrets
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


class BotSelf(BaseModel):
    platform: str
    user_id: str


class RequestParams(BaseModel):
    pass


class ResponseData(BaseModel):
    pass


class Request(BaseModel):
    action: str
    params: RequestParams
    echo: Optional[str] = Field(default_factory=lambda: secrets.token_hex(8))
    self: Optional[BotSelf] = None


class Response(BaseModel):
    status: Literal['ok', 'failed']
    retcode: int
    data: Any
    message: str
    echo: Optional[str]


__all__ = ["BotSelf", "Request", "Response", "RequestParams", "ResponseData"]
