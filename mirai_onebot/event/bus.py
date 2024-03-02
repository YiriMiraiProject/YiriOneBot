import asyncio
from typing import Callable, Dict, List, Set, Union

from mirai_onebot.event.event_base import EventBase
from mirai_onebot.utils import logging

logger = logging.getLogger(__name__)


class EventBus(object):
    def __init__(self) -> None:
        self._subscribers: Dict[Union[EventBase, str], Set[Callable]] = {}

    def subscribe(self, event: Union[EventBase, str], func: Callable) -> None:
        """注册事件处理器

        Args:
            event (str | EventBase): 事件
            func (Callable): 事件处理器
        """
        if event not in self._subscribers.keys():
            self._subscribers[event] = {func}
        else:
            self._subscribers[event].add(func)

    def unsubscribe(self, event: Union[EventBase, str], func: Callable) -> None:
        """移除事件处理器

        Args:
            event (str | EventBase): 事件
            func (Callable): 事件处理器
        """
        try:
            self._subscribers[event].remove(func)
        except KeyError:
            logger.warning(f'试图移除事件 `{event}` 的一个不存在的事件处理器 `{func}`。')

    def on(self, event: Union[EventBase, str]) -> Callable:
        """以装饰器方式注册事件处理器。

        Args:
            event (str | EventBase): 事件
        """
        def decorator(func: Callable) -> Callable:
            self.subscribe(event, func)
            return func

        return decorator

    async def emit(self, event: Union[EventBase, str], *args, **kwargs) -> None:
        """触发事件

        Args:
            event (str | EventBase): 事件
            args/kwargs: 传递给事件处理器的参数
        """
        if event in self._subscribers.keys():
            tasks = [asyncio.create_task(subscriber(*args, **kwargs))
                     for subscriber in self._subscribers[event]]
            await asyncio.wait(tasks)
