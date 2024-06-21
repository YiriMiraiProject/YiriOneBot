import asyncio
import logging
from typing import Callable, List, Optional, Type, TypeVar, Union

from mirai_onebot.adapters.base import Adapter
from mirai_onebot.api.interfaces.base import BotSelf, Request, Response
from mirai_onebot.api.interfaces.message import (SendMessageRequest,
                                                 SendMessageRequestParams,
                                                 SendMessageResponse)
from mirai_onebot.event import SLUG_TO_EVENT
from mirai_onebot.event.bus import EventBus
from mirai_onebot.event.event_base import EventBase
from mirai_onebot.message.message_chain import MessageChain
from mirai_onebot.message.message_components import (MessageComponent,
                                                     MessageComponentsType,
                                                     Text)

logger = logging.getLogger(__name__)
ResponseT = TypeVar('ResponseT', bound=Response)


class Bot(object):
    def __init__(
        self,
        adapter: Adapter,
        bus: Optional[EventBus] = None,
        bot_platform: Optional[str] = None,
        bot_user_id: Optional[str] = None
    ) -> None:
        """MiraiOneBot 高级类，用于处理事件、发送消息。用户应该直接基于该类进行开发

        Args:
            adapter (Adapter): 适配器
            bus (Optional[EventBus], optional): 事件总线，不填自动创建一个事件总线
            bot_platform (Optional[str], optional): 机器人平台，不填自动接收所有 OneBot 实现发来的事件
            bot_user_id (Optional[str], optional): 机器人id，不填自动接收所有 OneBot 实现发来的事件
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
            if data['self']['platform'] != self.bot_platform:
                return

        if self.bot_user_id is not None and 'self' in data.keys():
            if data['self']['user_id'] != self.bot_platform:
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

    async def call(self, request: Request, response_type: Type[ResponseT], auto_set_self=True) -> ResponseT:
        """调用API

        Args:
            request (Request): 请求
            response_type (Type[Response]): 返回类型
            auto_set_self (bool, optional): 自动设置请求中的 self，要求 bot_user_id 和 bot_platform 不为 None. Defaults to True.

        Returns:
            Response: 调用返回值
        """
        if auto_set_self and self.bot_platform is not None and self.bot_user_id is not None:
            request.self = BotSelf(platform=self.bot_platform, user_id=self.bot_user_id)

        return await self.adapter.call(request, response_type)

    # 简化 API
    async def send_group_message(self, group_id: str, message: Union[MessageChain, str, List[str], List[MessageComponentsType]]):
        """发送私聊消息

        Args:
            group_id (str): 群 id
            message (Union[MessageChain, str, List[str], List[MessageComponentsType]]): 消息

        Returns:
            SendMessageResponseData: 返回值
        """
        if isinstance(message, str):
            message_chain = MessageChain([Text(message)])
        elif isinstance(message, list):
            message_chain = MessageChain([
                x if isinstance(x, MessageComponent) else Text(x)
                for x in message
            ])

        return (await self.call(
            request=SendMessageRequest(
                params=SendMessageRequestParams(
                    detail_type='group',
                    group_id=group_id,
                    message=message_chain.to_dict()
                )
            ),
            response_type=SendMessageResponse
        )).data

    async def send_private_message(self, user_id: str, message: Union[MessageChain, str, List[str], List[MessageComponentsType]]):
        """发送私聊消息

        Args:
            user_id (str): 用户 id
            message (Union[MessageChain, str, List[str], List[MessageComponentsType]]): 消息

        Returns:
            SendMessageResponseData: 返回值
        """
        if isinstance(message, str):
            message_chain = MessageChain([Text(message)])
        elif isinstance(message, list):
            message_chain = MessageChain([
                x if isinstance(x, MessageComponent) else Text(x)
                for x in message
            ])

        return await self.call(
            request=SendMessageRequest(
                params=SendMessageRequestParams(
                    detail_type='private',
                    user_id=user_id,
                    message=message_chain.to_dict()
                )
            ),
            response_type=SendMessageResponse
        )
