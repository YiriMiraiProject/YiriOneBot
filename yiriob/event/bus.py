import asyncio
from collections.abc import Callable, Coroutine

from yiriob.utils import logger

from .base import EventBase

Event = str | type[EventBase]
EventHandler = Callable[..., Coroutine[None, None, None]]


class EventBus:
    """事件总线

    Attributes:
        handlers: 事件-响应器集合 的映射
    """

    def __init__(self) -> None:
        self.handlers: dict[Event, set[EventHandler]] = {}

    def subscribe(self, event: Event, handler: EventHandler) -> None:
        """订阅事件

        Args:
            event: 事件
            handler: 事件响应器
        """
        if event not in self.handlers.keys():
            self.handlers[event] = set()
        self.handlers[event].add(handler)

    def unsubscribe(self, event: Event, handler: EventHandler | None) -> None:
        """取消订阅事件

        Args:
            event: 事件
            handler: 事件响应器，传入 None 表示取消所有
        """
        try:
            if handler is None:
                del self.handlers[event]
            else:
                self.handlers[event].remove(handler)
        except KeyError:
            pass

    def on(self, event: Event):
        """订阅事件，装饰器版本

        Args:
            event: 事件
        """

        def decorator(func: EventHandler) -> EventHandler:
            self.subscribe(event, func)
            return func

        return decorator

    def emit(self, event: Event, *args, **kwargs) -> bool:
        """触发事件

        Args:
            event: 事件
            *args: 传递给 handler 的位置参数
            **kwargs: 传递给 handler 的 keyword 参数

        Returns:
            False: 事件未注册导致调用失败
            True: 调用成功
        """
        if self.handlers.get(event, None) is None:
            logger.debug(f"找不到事件 {event} 的响应器")
            return False

        for h in self.handlers[event]:
            asyncio.create_task(h(*args, **kwargs))

        return True


__all__ = ["EventBus"]
