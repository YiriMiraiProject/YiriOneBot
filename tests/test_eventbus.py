from yiriob.event import EventBus
import asyncio
from pytest import mark


@mark.asyncio
async def test_eventbus():
    flagA = False
    flagB = False

    bus = EventBus()

    @bus.on("a")
    async def handlerA():
        nonlocal flagA
        flagA = True

    @bus.on("b")
    async def handlerB():
        nonlocal flagB
        flagB = True

    assert flagA is False
    assert flagB is False

    bus.emit("a")
    bus.emit("b")

    await asyncio.sleep(0.5)

    assert flagA is True
    assert flagB is True

    flagA = False
    flagB = False

    bus.unsubscribe("a", handlerA)

    bus.emit("a")
    bus.emit("b")

    await asyncio.sleep(0.5)

    assert flagA is False
    assert flagB is True

    bus.unsubscribe("b", None)
    bus.unsubscribe("c", None)

    flagB = False
    bus.emit("b")

    await asyncio.sleep(0.5)

    assert flagB is False
