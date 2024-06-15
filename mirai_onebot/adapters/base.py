import asyncio
from typing import Set

from mirai_onebot.api import ApiProvider
from mirai_onebot.event import EventBus


class Adapter(ApiProvider):
    """用于兼容OneBot的各种通讯协议。收到OneBot响应时，在内部事件总线触发onebot_resp事件。收到OneBot事件时，触发onebot_event。"""

    access_token: str
    buses: Set[EventBus] = set()
    _internal_event_bus = EventBus()  # 用于适配器内部通信使用

    def __init__(self, access_token: str) -> None:
        super().__init__()
        self.access_token = access_token

    def start(self):
        """启动适配器，不阻塞"""

    def stop(self):
        """停止适配器"""

    def register_event_bus(self, bus: EventBus):
        self.buses.add(bus)

    async def emit(self, event: str, *args, **kwargs) -> None:
        """向事件总线发送事件

        Args:
            event (str): 事件
        """
        [asyncio.create_task(
            bus.emit(event, *args, **kwargs)) for bus in self.buses]
        # await asyncio.gather(*tasks)
