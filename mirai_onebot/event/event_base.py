from __future__ import annotations

from abc import ABC, abstractmethod


class EventBase(ABC):
    """基本事件类"""
    name: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    def load_from_dict(data: dict) -> EventBase:
        """从字典加载为事件类

        Args:
            data (dict): 字典

        Returns:
            EventBase: 事件类
        """

    def __str__(self) -> str:
        return self.name
