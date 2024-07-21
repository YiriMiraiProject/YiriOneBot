import asyncio
from typing import Any, Optional

import pydantic

from yiriob.adapters.base import Adapter
from yiriob.event.base import (EventBase, events_list, get_key_from_dict,
                               get_key_from_event)
from yiriob.interface.message import (SendGroupMessageInterface,
                                      SendGroupMessageParams,
                                      SendGroupMessageResponse,
                                      SendPrivateMessageInterface,
                                      SendPrivateMessageParams,
                                      SendPrivateMessageResponse)
from yiriob.message.message_chain import MessageChain
from yiriob.utils import logger


class Bot:
    def __init__(self, adapter: Adapter, self_id: int) -> None:
        """机器人类。

        Args:
            adapter: 适配器，用于跟 OneBot 实现通讯
            self_id: 机器人 id，避免接收到其它机器人的事件

        你可以像这样初始化一个机器人：

        ```python
        bus = EventBus()
        bot = Bot(
            adapter=ReverseWebsocketAdapter(
                host="127.0.0.1", port=8080, access_token="...", bus=bus
            ),
            self_id=...,
        )
        ```

        然后像这样监听事件并处理事件（还有调用 API）：

        ```python
        @bus.on(GroupMessageEvent)
        async def on_group_message(event: GroupMessageEvent) -> None:
            resp = await bot.adapter.call_api(
                SendGroupMessageInterface,
                SendGroupMessageParams(
                    group_id=event.group_id, message=MessageChain([Text("Hello World!")])
                ),
            )
        ```

        一些常见的 API 有简化形式，例如发送消息：

        ```python
        await bot.send_group_message(group_id=..., message=...)
        await bot.send_private_message(user_id=..., message=...)
        ```
        """
        self.adapter = adapter
        self.id = self_id
        self.bus = adapter.bus

        self.bus.subscribe("onebot_event", self._onebot_event_handler)

    async def _onebot_event_handler(self, data: dict[str, Any]) -> None:
        """将原始的onebot事件解析为事件类并触发事件总线。

        Args:
            data: 原始事件
        """
        validated_model: Optional[EventBase] = next(
            (
                x(**data)
                for x in events_list
                if get_key_from_event(x) == get_key_from_dict(data)
            ),
            None,
        )

        if validated_model is None:
            logger.debug("主匹配方法失败，使用 Fallback 匹配方法")
            # 此为 fallback 匹配方法（有些 OB Impl 的自定义事件不兼容上面的匹配方法）
            for event in events_list:
                try:
                    validated_model = event.model_validate(data)
                    break
                except pydantic.ValidationError:
                    continue

        if validated_model is None:
            logger.debug(f"事件 {data} 没有被任何一个注册的事件类匹配到！")
            return

        if validated_model.self_id != self.id:
            logger.debug(f"事件 {data} 与当前机器人不匹配！")
            return

        logger.debug(f"匹配到事件：{type(validated_model)}")
        self.bus.emit(type(validated_model), validated_model)

    async def send_group_message(
        self,
        group_id: int,
        message: MessageChain | str,
        auto_escape: bool = True,
    ) -> SendGroupMessageResponse:
        """发送群消息。

        Args:
            group_id: 群号
            message: 消息
            auto_escape: 是否自动转义
        """
        return await self.adapter.call_api(
            SendGroupMessageInterface,
            SendGroupMessageParams(
                group_id=group_id, message=message, auto_escape=auto_escape
            ),
        )

    async def send_private_message(
        self, user_id: int, message: MessageChain | str, auto_escape: bool = True
    ) -> SendPrivateMessageResponse:
        """发送私聊消息。

        Args:
            user_id: 用户 id
            message: 消息
            auto_escape: 是否自动转义
        """
        return await self.adapter.call_api(
            SendPrivateMessageInterface,
            SendPrivateMessageParams(
                user_id=user_id, message=message, auto_escape=auto_escape
            ),
        )

    def run(self) -> None:
        """启动机器人。该方法将会开启适配器，并且阻塞。"""
        self.adapter.start()
        asyncio.get_event_loop().run_forever()
