# isort: off
# autopep8: off
import sys
import pathlib

sys.path.insert(0, pathlib.Path('.').parent.absolute().__str__())
# isort: on
# autopep8: on

from mirai_onebot import Bot  # noqa: E402
from mirai_onebot.adapters.reverse_websocket_adapter import \
    ReverseWebsocketAdapter  # noqa: E402
from mirai_onebot.api.interfaces.message import \
    SendMessageResponse  # noqa: E402
from mirai_onebot.api.interfaces.message import (  # noqa: E402
    SendMessageRequest, SendMessageRequestParams)
from mirai_onebot.event.group_event import MessageGroupEvent  # noqa: E402
from mirai_onebot.event.private_direct_event import \
    MessagePrivateEvent  # noqa: E402
from mirai_onebot.message.message_chain import MessageChain  # noqa: E402
from mirai_onebot.message.message_components import Text  # noqa: E402

bot = Bot(
    adapter=ReverseWebsocketAdapter(
        access_token='test',
        host='0.0.0.0',
        port=8120,
        timeout=10
    )
)


@bot.on(MessageGroupEvent)
async def handle_message_group(event: MessageGroupEvent):
    await bot.call(SendMessageRequest(
        params=SendMessageRequestParams(
            detail_type="group",
            group_id=event.group_id,
            message=MessageChain([
                Text('你好')
            ]).to_dict()
        )
    ), SendMessageResponse)


@bot.on(MessagePrivateEvent)
async def handle_message_private(event: MessagePrivateEvent):
    await bot.call(SendMessageRequest(
        params=SendMessageRequestParams(
            detail_type="private",
            user_id=event.user_id,
            message=MessageChain([
                Text('你好')
            ]).to_dict()
        )
    ), SendMessageResponse)

bot.run()
