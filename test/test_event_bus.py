import pytest

from mirai_onebot.event import EventBus, MessageGroupEvent
from mirai_onebot.event.event_base import EventBase
from mirai_onebot.event.group_event import (NoticeGroupMemberDecreaseEvent,
                                            NoticeGroupMemberIncreaseEvent,
                                            NoticeGroupMessageDeleteEvent)
from mirai_onebot.event.private_direct_event import (
    MessagePrivateEvent, NoticeFriendDecreaseEvent, NoticeFriendIncreaseEvent,
    NoticePrivateMessageDelete)

bus = EventBus()


@pytest.mark.asyncio
async def test_subscribe():
    run1 = False
    run2 = False

    async def handle_print_message(message: str):
        nonlocal run1
        print(message)
        run1 = True

    @bus.on(MessageGroupEvent)
    async def handle_message_group_event():
        nonlocal run2
        run2 = True

    bus.subscribe('print_message', handle_print_message)

    await bus.emit(MessageGroupEvent)
    await bus.emit('print_message', 'hello')

    assert run1 == True
    assert run2 == True


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


def test_events():
    event = MessageGroupEvent()
    assert str(event) == event.name

    for event, data in {
        MessageGroupEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "message",
            "detail_type": "group",
            "sub_type": "",
            "message_id": "6283",
            "message": [
                {
            "type": "text",
            "data": {
                "text": "OneBot is not a bot"
            }
                    },
                {
            "type": "image",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
                    }
            ],
            "alt_message": "OneBot is not a bot[图片]",
            "group_id": "12345",
            "user_id": "123456788"
        },
        NoticeGroupMemberIncreaseEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "notice",
            "detail_type": "group_member_increase",
            "sub_type": "join",
            "user_id": "123456788",
            "group_id": "87654321",
            "operator_id": "1234567"
        },
        NoticeGroupMemberDecreaseEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "notice",
            "detail_type": "group_member_decrease",
            "sub_type": "leave",
            "user_id": "123456788",
            "group_id": "87654321",
            "operator_id": "1234567"
        },
        NoticeGroupMessageDeleteEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "notice",
            "detail_type": "group_message_delete",
            "sub_type": "recall",
            "group_id": "87654321",
            "message_id": "2847",
            "user_id": "123456788",
            "operator_id": "1234567"
        },
        MessagePrivateEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "message",
            "detail_type": "private",
            "sub_type": "",
            "message_id": "6283",
            "message": [
                {
            "type": "text",
            "data": {
                "text": "OneBot is not a bot"
            }
                    },
                {
            "type": "image",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
                    }
            ],
            "alt_message": "OneBot is not a bot[图片]",
            "user_id": "123456788"
        },
        NoticeFriendIncreaseEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "notice",
            "detail_type": "friend_increase",
            "sub_type": "",
            "user_id": "123456788"
        },
        NoticeFriendDecreaseEvent: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "notice",
            "detail_type": "friend_decrease",
            "sub_type": "",
            "user_id": "123456788"
        },
        NoticePrivateMessageDelete: {
            "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
            "self": {
                "platform": "qq",
                "user_id": "123234"
            },
            "time": 1632847927.599013,
            "type": "notice",
            "detail_type": "private_message_delete",
            "sub_type": "",
            "message_id": "2847",
            "user_id": "123456788"
        }
    }.items():
        e = event().load_from_dict(data)
