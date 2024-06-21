from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Optional, Union


class MessageComponent(ABC):
    message_type: str
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    data: Dict[str, Any]
    """消息参数"""

    def __init__(self) -> None:
        super().__init__()
        self.data = {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self.message_type,
            'data': self.data
        }

    @staticmethod
    def load_from_dict(data: dict) -> MessageComponentsType:
        """从字典加载为消息组件

        Examples:
            load_from_dict({
                "type": "text",
                "data": {
                    "text": "OneBot is not a bot"
                }
            })

        Args:
            data (dict): 字典

        Raises:
            KeyError: 未提供正确的数据
            ValueError: 未传入正确的message_type

        Returns:
            MessageComponent: 加载后的消息组件
        """

        message_type = data.get('type')
        if message_type == 'text':
            return Text(data['data']['text'])
        elif message_type == 'mention':
            return Mention(data['data']['user_id'])
        elif message_type == 'mention_all':
            return MentionAll()
        elif message_type == 'image':
            return Image(data['data']['file_id'])
        elif message_type == 'voice':
            return Voice(data['data']['file_id'])
        elif message_type == 'audio':
            return Audio(data['data']['file_id'])
        elif message_type == 'video':
            return Video(data['data']['file_id'])
        elif message_type == 'file':
            return File(data['data']['file_id'])
        elif message_type == 'location':
            return Location(data['data']['latitude'], data['data']['longitude'], data['data']['title'], data['data']['content'])
        elif message_type == 'reply':
            return Reply(data['data']['message_id'], data['data'].get('user_id', None))
        else:
            raise ValueError(f"Unknown message type: {message_type}")

    def __repr__(self) -> str:
        return f'{self.message_type}: {self.data}'

    def __eq__(self, __value: MessageComponent) -> bool:  # type: ignore
        if isinstance(__value, MessageComponent):  # 实例化的
            return self.message_type == __value.message_type and self.data == __value.data
        elif isinstance(__value, type):  # 未实例化
            return isinstance(self, __value)
        else:
            raise ValueError("Can't compare MessageComponent with non-MessageComponent object")


class Text(MessageComponent):
    """纯文本"""

    message_type: str = 'text'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    text: str
    """纯文本内容"""

    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text
        self.data['text'] = self.text

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, str):
            return self.text == __value
        elif isinstance(__value, Text):
            return self.text == __value.text
        else:
            return False


class Mention(MessageComponent):
    """提及"""

    message_type: str = 'mention'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    user_id: str
    """提及的用户 ID"""

    def __init__(self, user_id: str) -> None:
        super().__init__()
        self.user_id = user_id
        self.data['user_id'] = self.user_id


class MentionAll(MessageComponent):
    """提及所有人"""

    message_type: str = 'mention_all'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""

    def __init__(self) -> None:
        super().__init__()


class Image(MessageComponent):
    """图片"""

    message_type: str = 'image'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    file_id: str
    """图片文件 ID"""

    def __init__(self, file_id: str) -> None:
        super().__init__()
        self.file_id = file_id
        self.data['file_id'] = self.file_id


class Voice(MessageComponent):
    """语音"""

    message_type: str = 'voice'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    file_id: str
    """语音文件 ID"""

    def __init__(self, file_id: str) -> None:
        super().__init__()
        self.file_id = file_id
        self.data['file_id'] = self.file_id


class Audio(MessageComponent):
    """音频

    提示：音频消息段和语音消息段的区别是：语音消息段在聊天软件中表现为用户当场录制的声音，而音频消息段可能是直接发送的一个音乐文件，在消息列表中显示为可播放。
    """

    message_type: str = 'audio'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    file_id: str
    """音频文件 ID"""

    def __init__(self, file_id: str) -> None:
        super().__init__()
        self.file_id = file_id
        self.data['file_id'] = self.file_id


class Video(MessageComponent):
    """视频"""

    message_type: str = 'video'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    file_id: str
    """视频文件 ID"""

    def __init__(self, file_id: str) -> None:
        super().__init__()
        self.file_id = file_id
        self.data['file_id'] = self.file_id


class File(MessageComponent):
    """文件"""

    message_type: str = 'file'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    file_id: str
    """文件 ID"""

    def __init__(self, file_id: str) -> None:
        super().__init__()
        self.file_id = file_id
        self.data['file_id'] = self.file_id


class Location(MessageComponent):
    """位置"""

    message_type: str = 'location'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    latitude: float
    """纬度"""
    longitude: float
    """经度"""
    title: str
    """标题"""
    content: str
    """地址内容"""

    def __init__(self, latitude: float, longitude: float, title: str, content: str) -> None:
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.content = content
        self.data = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'title': self.title,
            'content': self.content
        }


class Reply(MessageComponent):
    """回复"""

    message_type: str = 'reply'
    """消息类型（为避免与built-in函数type冲突，命名为message_type）"""
    message_id: str
    """回复的消息 ID"""
    user_id: Optional[str]
    """回复的消息发送者 ID，发送时可以不传入"""

    def __init__(self, message_id: str, user_id: Optional[str] = None) -> None:
        super().__init__()
        self.message_id = message_id
        self.user_id = user_id
        self.data['message_id'] = self.message_id
        self.data['user_id'] = self.user_id


MessageComponentsType = Union[Text, Mention, MentionAll, Image, Voice, Audio, Video, File, Location, Reply]

__all__ = [
    'Text', 'Mention', 'MentionAll', 'Image',
    'Voice', 'Audio', 'Video', 'File',
    'Location', 'Reply',
    'MessageComponentsType'
]
