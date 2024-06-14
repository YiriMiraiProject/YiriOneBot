# %%
import sys

sys.path.append('..')
from mirai_onebot.adapters import ReverseWebsocketAdapter
from mirai_onebot.event import EventBus

bus = EventBus()

adapter = ReverseWebsocketAdapter('test', '0.0.0.0', 8120, 10)
adapter.register_event_bus(bus)

# %% [markdown]
# 此时使用任意一个OneBot实现（例如我用的是matcha这样的模拟环境）连接，即可在下方收到事件。

# %%


@bus.on('onebot_event')
async def onebot_event(data: dict):
    print(data)
