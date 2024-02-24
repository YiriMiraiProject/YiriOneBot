import pytest

from mirai_onebot.event import EventBus

bus = EventBus()


def test_subscribe():
    async def handle_print_message(message: str):
        print(message)

    bus.subscribe('print_message', handle_print_message)

    @bus.on('print_message2')
    @bus.on('print_message2')
    async def handle_print_message2(message: str):
        print(message)


def test_unsubscribe():
    @bus.on('test1')
    async def test1():
        pass

    bus.unsubscribe('test1', test1)
    bus.unsubscribe('test2', test1)


run1 = False
run2 = False


@pytest.mark.asyncio
async def test_emit():
    @bus.on('test3')
    async def test3():
        global run1
        run1 = True

    @bus.on('test3')
    async def test31():
        global run2
        run2 = True

    await bus.emit('test3')

    assert run1 == True
    assert run2 == True
