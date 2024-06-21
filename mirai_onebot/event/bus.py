import asyncio
from typing import Callable, Dict, Set, Type, Union

from mirai_onebot.event.event_base import EventBase
from mirai_onebot.utils import logging

logger = logging.getLogger(__name__)


class EventBus(object):
    def __init__(self) -> None:
        self._subscribers: Dict[Union[Type[EventBase], str], Set[Callable]] = {}

    def subscribe(self, event: Union[Type[EventBase], str], func: Callable) -> None:
        """注册事件处理器

        Args:
            event (str | Type[EventBase]): 事件
            func (Callable): 事件处理器
        """
        if event not in self._subscribers.keys():
            self._subscribers[event] = {func}
        else:
            self._subscribers[event].add(func)

    def unsubscribe(self, event: Union[Type[EventBase], str], func: Callable) -> None:
        """移除事件处理器

        Args:
            event (str | Type[EventBase]): 事件
            func (Callable): 事件处理器
        """
        try:
            self._subscribers[event].remove(func)
        except KeyError:
            logger.warning(f'试图移除事件 `{event}` 的一个不存在的事件处理器 `{func}`。')

    def on(self, event: Union[Type[EventBase], str]) -> Callable:
        """以装饰器方式注册事件处理器。

        Args:
            event (str | Type[EventBase]): 事件
        """
        def decorator(func: Callable) -> Callable:
            self.subscribe(event, func)
            return func

        return decorator

    async def emit(self, event: Union[Type[EventBase], str], background=True, *args, **kwargs) -> None:
        """触发事件

        Args:
            event (str | Type[EventBase]): 事件
            background (bool, optional): 是否在后台触发事件，设置为False会等待事件完成. Defaults to True.
            args/kwargs: 传递给事件处理器的参数
        """
        if event in self._subscribers.keys():
            tasks = [asyncio.create_task(subscriber(*args, **kwargs))
                     for subscriber in self._subscribers[event]]
            if not background:
                await asyncio.wait(tasks)
