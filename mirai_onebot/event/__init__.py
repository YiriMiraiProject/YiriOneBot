from typing import Dict, Type

from mirai_onebot.event.bus import EventBus
from mirai_onebot.event.event_base import EventBase
from mirai_onebot.event.group_event import (MessageGroupEvent,
                                            NoticeGroupMemberDecreaseEvent,
                                            NoticeGroupMemberIncreaseEvent,
                                            NoticeGroupMessageDeleteEvent)
from mirai_onebot.event.private_direct_event import (
    MessagePrivateEvent, NoticeFriendDecreaseEvent, NoticeFriendIncreaseEvent,
    NoticePrivateMessageDelete)

__all__ = [
    'EventBus',
    'MessageGroupEvent',
    'NoticeGroupMemberDecreaseEvent',
    'NoticeGroupMemberIncreaseEvent',
    'NoticeGroupMessageDeleteEvent',
    'MessagePrivateEvent',
    'NoticeFriendDecreaseEvent',
    'NoticeFriendIncreaseEvent',
    'SLUG_TO_EVENT',
    'NoticePrivateMessageDelete'
]

# 从 slug 到类的映射
SLUG_TO_EVENT: Dict[str, Dict[str, Type[EventBase]]] = {
    'message': {
        'group': MessageGroupEvent,
        'private': MessagePrivateEvent
    },
    'notice': {
        'group_member_increase': NoticeGroupMemberIncreaseEvent,
        'group_member_decrease': NoticeGroupMemberDecreaseEvent,
        'group_message_delete': NoticeGroupMessageDeleteEvent,
        'friend_increase': NoticeFriendIncreaseEvent,
        'friend_decrease': NoticeFriendDecreaseEvent,
        'private_message_delete': NoticePrivateMessageDelete
    }
}
