from abc import ABC
from typing import Any, Dict, Optional


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

    def __repr__(self) -> str:
        return f'{self.message_type}: {self.data}'

    def __eq__(self, __value: object) -> bool:
        try:
            return self.message_type == __value.message_type and self.data == __value.data
        except AttributeError:  # 未实例化的__value
            return self.message_type == __value.message_type


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

        if isinstance(__value, Text):
            return self.text == __value.text


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

    message_type: str = 'image'
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


__all__ = [
    'Text', 'Mention', 'MentionAll', 'Image',
    'Voice', 'Audio', 'Video', 'File',
    'Location', 'Reply'
]
