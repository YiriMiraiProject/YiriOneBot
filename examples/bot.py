from yiriob.bot import Bot
from yiriob.event import EventBus
from yiriob.event.events import GroupMessageEvent, PrivateMessageEvent
from yiriob.adapters import ReverseWebsocketAdapter
from yiriob.interface.message import (
    SendGroupMessageInterface,
    SendGroupMessageParams,
    SendPrivateMessageInterface,
    SendPrivateMessageParams,
)
from yiriob.message.message_chain import MessageChain
from yiriob.message.message_components import Text

bus = EventBus()
bot = Bot(
    adapter=ReverseWebsocketAdapter(
        host="127.0.0.1", port=8080, access_token="helloworld", bus=bus
    ),
    self_id=3442852292,
)


@bus.on(GroupMessageEvent)
async def on_group_message(event: GroupMessageEvent) -> None:
    resp = await bot.adapter.call_api(
        SendGroupMessageInterface,
        SendGroupMessageParams(
            group_id=event.group_id, message=MessageChain([Text("Hello World!")])
        ),
    )


@bus.on(PrivateMessageEvent)
async def on_private_message(event: GroupMessageEvent) -> None:
    await bot.adapter.call_api(
        SendPrivateMessageInterface,
        SendPrivateMessageParams(
            user_id=event.user_id, message=MessageChain([Text("Hello World!")])
        ),
    )


bot.run()
