from abc import ABC
from typing import Generic, Type, TypeVar

from pydantic import BaseModel


class InterfaceParams(BaseModel, ABC):
    pass


class InterfaceResponse(BaseModel, ABC):
    pass


InterfaceParamsType = TypeVar("InterfaceParamsType", bound=InterfaceParams)
InterfaceResponseType = TypeVar("InterfaceResponseType", bound=InterfaceResponse)


class Interface(BaseModel, ABC, Generic[InterfaceParamsType, InterfaceResponseType]):
    action: str
    params_type: Type[InterfaceParamsType]
    response_type: Type[InterfaceResponseType]

    def get_ratelimited_interface(self) -> "Interface":
        """获取限速调用的 API，避免因为调用速度过快被封。详情请见 OneBot 11 标准 -> API -> API 概述 -> 限速调用。

        Returns:
            一个限速调用版本的 API，action 字段有 _rate_limited 后缀。
        """
        return Interface(
            action=self.action + "_rate_limited",
            params_type=self.params_type,
            response_type=self.response_type,
        )


__all__ = [
    "Interface",
    "InterfaceParams",
    "InterfaceResponse",
    "InterfaceParamsType",
    "InterfaceResponseType",
]
