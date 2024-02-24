from typing import Set

from mirai_onebot.api import ApiProvider
from mirai_onebot.event import EventBus


class Adapter(ApiProvider):
    """用于兼容OneBot的各种通讯协议。"""

    access_token: str
    buses: Set[EventBus] = set()

    def __init__(self, access_token: str) -> None:
        super().__init__()
        self.access_token = access_token

    def register_event_bus(self, bus: EventBus):
        self.buses.add(bus)
