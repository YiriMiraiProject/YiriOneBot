from abc import ABC, abstractmethod
from typing import Any

from yiriob.event import EventBus
from yiriob.exceptions.api import InterfaceCallFailed
from yiriob.interface import (Interface, InterfaceParamsType,
                              InterfaceResponseType)


class Adapter(ABC):
    """适配器基类

    Attributes:
        access_token: 用于鉴权的 access_token，必填
    """

    def __init__(self, access_token: str, bus: EventBus) -> None:
        self.access_token = access_token
        self.bus = bus

    @abstractmethod
    def start(self):
        """启动适配器"""

    @abstractmethod
    def stop(self):
        """停止适配器"""

    @abstractmethod
    async def _call_api(
        self, action: str, params: dict[str, Any], timeout: int = 20
    ) -> dict[str, Any]:
        """内部接口，用于直接调用 API，不带类型验证等

        Args:
            action: 动作，见 OneBot 术语表
            params: API 参数
            timeout: 调用超时时间

        Returns:
            API 调用结果

        Raises:
            TimeoutError: 调用超时
        """

    async def call_api(
        self,
        interface: Interface[InterfaceParamsType, InterfaceResponseType],
        params: InterfaceParamsType,
    ) -> InterfaceResponseType:
        """公开接口，用于调用 API，有静态类型推导和验证

        Args:
            interface: 要调用的 API
            params: 调用参数，类型根据 interface 自动推导

        Returns:
            调用结果，类型根据 interface 自动推导

        Raises:
            TimeoutError: 调用超时
        """
        resp = await self._call_api(interface.action, params.model_dump(mode="json"))
        if resp.get("status", None) == "failed":
            raise InterfaceCallFailed(
                action=interface.action,
                params=params.model_dump(),
                retcode=resp["retcode"],
            )

        return interface.response_type.model_validate(resp["data"])

    def emit_onebot_event(self, data: dict[str, Any]):
        self.bus.emit("onebot_event", data)
