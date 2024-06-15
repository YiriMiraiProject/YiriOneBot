from __future__ import annotations

from typing import Literal

from mirai_onebot.event.event_base import EventBase
from mirai_onebot.message import MessageChain

__all__ = [
    'MessageGroupEvent',
    'NoticeGroupMemberIncreaseEvent',
    'NoticeGroupMemberDecreaseEvent',
    'NoticeGroupMessageDeleteEvent'
]


class MessageGroupEvent(EventBase):
    """群消息"""
    name = 'message.group'
    message_id: str
    message: MessageChain
    alt_message: str = ''
    group_id: str
    user_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> MessageGroupEvent:
        event = MessageGroupEvent()
        event.message_id = data['message_id']
        event.message = MessageChain.load_from_dict(data['message'])
        event.alt_message = data.get('alt_message', '')
        event.group_id = data['group_id']
        event.user_id = data['user_id']
        return event


class NoticeGroupMemberIncreaseEvent(EventBase):
    """群成员增加"""
    name = 'notice.group_member_increase'
    sub_type: Literal['join', 'invite', ''] = ''
    group_id: str
    user_id: str
    operator_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> NoticeGroupMemberIncreaseEvent:
        event = NoticeGroupMemberIncreaseEvent()
        event.group_id = data['group_id']
        event.user_id = data['user_id']
        event.operator_id = data.get('operator_id', '')
        event.sub_type = data.get('sub_type', '')
        return event


class NoticeGroupMemberDecreaseEvent(EventBase):
    """群成员减少"""
    name = 'notice.group_member_decrease'
    sub_type: Literal['leave', 'kick', ''] = ''
    group_id: str
    user_id: str
    operator_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> NoticeGroupMemberDecreaseEvent:
        event = NoticeGroupMemberDecreaseEvent()
        event.group_id = data['group_id']
        event.user_id = data['user_id']
        event.operator_id = data.get('operator_id', '')
        event.sub_type = data.get('sub_type', '')
        return event


class NoticeGroupMessageDeleteEvent(EventBase):
    """群消息删除"""
    name = 'notice.group_message_delete'
    sub_type: Literal['recall', 'delete', ''] = ''
    group_id: str
    message_id: str
    user_id: str
    operator_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> NoticeGroupMessageDeleteEvent:
        event = NoticeGroupMessageDeleteEvent()
        event.group_id = data['group_id']
        event.message_id = data['message_id']
        event.user_id = data['user_id']
        event.operator_id = data.get('operator_id', '')
        event.sub_type = data.get('sub_type', '')
        return event
