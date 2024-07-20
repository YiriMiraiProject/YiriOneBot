import asyncio
from typing import Any, Optional

import pydantic
from yiriob.adapters.base import Adapter
from yiriob.event.base import EventBase, events_list
from yiriob.event.message_events import GroupMessageEvent
from yiriob.utils import logger


class Bot:
    def __init__(self, adapter: Adapter, self_id: int) -> None:
        self.adapter = adapter
        self.id = self_id
        self.bus = adapter.bus

        self.bus.subscribe("onebot_event", self._onebot_event_handler)

    async def _onebot_event_handler(self, data: dict[str, Any]) -> None:
        validated_model: Optional[EventBase] = None

        for event in events_list:
            try:
                validated_model = event.model_validate(data)
            except pydantic.ValidationError:
                continue

        if validated_model is None:
            logger.debug(f"事件 {data} 没有被任何一个注册的事件类匹配到！")
            return

        if validated_model.self_id != self.id:
            logger.debug(f"事件 {data} 与当前机器人不匹配！")
            return

        self.bus.emit(type(validated_model), validated_model)

    def run(self) -> None:
        self.adapter.start()
        asyncio.get_event_loop().run_forever()
