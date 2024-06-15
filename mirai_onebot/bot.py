import asyncio
import logging
from typing import Callable, List, Optional, Type, Union

from mirai_onebot.adapters.base import Adapter
from mirai_onebot.event import SLUG_TO_EVENT
from mirai_onebot.event.bus import EventBus
from mirai_onebot.event.event_base import EventBase

logger = logging.getLogger(__name__)


class Bot(object):
    def __init__(
        self,
        adapter: Adapter,
        bus: Optional[EventBus] = None,
        bot_platform: Optional[List[str]] = None,
        bot_user_id: Optional[List[str]] = None
    ) -> None:
        """MiraiOneBot 高级类，用于处理事件、发送消息。用户应该直接基于该类进行开发

        Args:
            adapter (Adapter): 适配器
            bus (Optional[EventBus], optional): 事件总线，不填自动创建一个事件总线
            bot_platform (Optional[List[str]], optional): 机器人平台，不填自动接收所有 OneBot 实现发来的事件
            bot_user_id (Optional[List[str]], optional): 机器人id，不填自动接收所有 OneBot 实现发来的事件
        """

        self.adapter = adapter
        self.bot_platform = bot_platform
        self.bot_user_id = bot_user_id

        if bus is None:
            self.bus = EventBus()
        else:
            self.bus = bus

        self.adapter.register_event_bus(self.bus)
        self.bus.subscribe('onebot_event', self.unserialize_raw_event)

    async def unserialize_raw_event(self, data: dict):
        """反序列化原始事件

        Args:
            data (str): 事件
        """
        # 筛选自身事件
        if self.bot_platform is not None and 'self' in data.keys():
            if data['self']['platform'] not in self.bot_platform:
                return

        if self.bot_user_id is not None and 'self' in data.keys():
            if data['self']['user_id'] not in self.bot_user_id:
                return

        # 解析
        try:
            event = SLUG_TO_EVENT[data['type']][data['detail_type']]
        except KeyError:
            logger.debug(f'不支持的事件：{data}')
            await self.bus.emit(f'{data["type"]}.{data["detail_type"]}', data)
            return

        await self.bus.emit(event, event.load_from_dict(data))

    def run(self) -> None:
        """启动机器人，然后阻塞"""
        self.adapter.start()

        logger.info(f'{self.adapter} 适配器启动完成。')

        try:
            asyncio.get_event_loop().run_forever()
        except KeyboardInterrupt:
            self.adapter.stop()
            logger.info(f'{self.adapter} 适配器停止。')

    def subscribe(self, event: Union[Type[EventBase], str], func: Callable):
        """注册事件的回调函数

        Args:
            event (Union[Type[EventBase], str]): 事件
            func (Callable): 回调函数
        """
        self.bus.subscribe(event, func)

    def unsubscribe(self, event: Union[Type[EventBase], str], func: Callable):
        """注销事件的回调函数

        Args:
            event (Union[Type[EventBase], str]): 事件
            func (Callable): 回调函数
        """
        self.bus.unsubscribe(event, func)

    def on(self, event: Union[Type[EventBase], str]):
        """注册事件的回调函数，装饰器版本

        Args:
            event (Union[Type[EventBase], str]): 事件
        """
        return self.bus.on(event)
