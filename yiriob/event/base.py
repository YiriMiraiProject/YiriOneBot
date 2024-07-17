from abc import ABC
from typing import Literal

from pydantic import BaseModel


class EventBase(BaseModel, ABC):
    """事件类

    Attributes:
        time: 事件发生时间
        self_id: 收到事件的机器人 id
        post_type: 事件类型
    """

    time: int
    self_id: int
    post_type: Literal["message", "notice", "request", "meta_event"] | str


__all__ = ["EventBase"]
