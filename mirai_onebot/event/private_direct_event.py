from __future__ import annotations

from mirai_onebot.event.event_base import EventBase
from mirai_onebot.message import MessageChain

__all__ = ['MessagePrivateEvent', 'NoticeFriendIncreaseEvent',
           'NoticeFriendDecreaseEvent', 'NoticePrivateMessageDelete']


class MessagePrivateEvent(EventBase):
    """私聊消息"""
    name = 'message.private'
    message_id: str
    message: MessageChain
    alt_message: str = ''
    user_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> MessagePrivateEvent:
        event = MessagePrivateEvent()
        event.message_id = data['message_id']
        event.message = MessageChain.load_from_dict(data)
        event.alt_message = data.get('alt_message', '')
        event.user_id = data['user_id']
        return event


class NoticeFriendIncreaseEvent(EventBase):
    """好友增加"""
    name = 'notice.friend_increase'
    user_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> NoticeFriendIncreaseEvent:
        event = NoticeFriendIncreaseEvent()
        event.user_id = data['user_id']
        return event


class NoticeFriendDecreaseEvent(EventBase):
    """好友减少"""
    name = 'notice.friend_decrease'
    user_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> NoticeFriendDecreaseEvent:
        event = NoticeFriendDecreaseEvent()
        event.user_id = data['user_id']
        return event


class NoticePrivateMessageDelete(EventBase):
    """私聊消息删除"""
    name = 'notice.private_message_delete'
    message_id: str
    user_id: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def load_from_dict(data: dict) -> NoticePrivateMessageDelete:
        event = NoticePrivateMessageDelete()
        event.message_id = data['message_id']
        event.user_id = data['user_id']
        return event
