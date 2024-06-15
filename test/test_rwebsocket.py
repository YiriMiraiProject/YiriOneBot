import asyncio
import json
import time
import uuid

import pytest
import websockets

from mirai_onebot.adapters import ReverseWebsocketAdapter
from mirai_onebot.event.bus import EventBus


@pytest.mark.asyncio
async def test_old_onebot():

    await asyncio.sleep(0.2)

    await websockets.connect('ws://127.0.0.1:4561', extra_headers={
        'Sec-WebSocket-Protocol': '11.test'
    })


@pytest.mark.asyncio
async def test_new_onebot():

    await asyncio.sleep(0.2)

    await websockets.connect('ws://127.0.0.1:4562', extra_headers={
        'Sec-WebSocket-Protocol': '13.test'
    })


@pytest.mark.asyncio
@pytest.mark.filterwarnings
async def test_normal():
    adapter = ReverseWebsocketAdapter('hello', '0.0.0.0', 4563, 1)

    await asyncio.sleep(0.2)

    bus = EventBus()
    adapter.register_event_bus(bus)

    ws_client = await websockets.connect('ws://127.0.0.1:4563', extra_headers={
        'Sec-WebSocket-Protocol': '12.test',
        'Authorization': 'Bearer hello'
    })

    # 正常事件
    id = uuid.uuid4().__str__()
    await ws_client.send(json.dumps({
        "id": id,
        "time": time.time(),
        "type": "meta",
        "detail_type": "connect",
        "sub_type": "",
        "version": {
            "impl": "test",
            "version": "0.0.1",
            "onebot_version": "12"
        }
    }))

    @bus.on('onebot_event')
    async def subscribe(data: dict):
        assert data['id'] == id

    # 错误事件
    await ws_client.send('hello?')

    # 调用api
    asyncio.create_task(adapter.call_api('hello', test='test'))

    # 发送响应
    echo = json.loads(await ws_client.recv())['echo']
    await ws_client.send(json.dumps({'echo': echo, 'resp': 'test'}))

    # 调用api超时
    await adapter.call_api('hello', test='test')
    await asyncio.sleep(1.5)

    # 关闭连接
    await ws_client.close()

    # 再次调用handler函数，引发错误
    await adapter.handler(adapter.ws_connections[0], '/')
