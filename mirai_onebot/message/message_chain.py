from typing import List, Union

from mirai_onebot.message.message_components import (Audio, File, Image,
                                                     Location, Mention,
                                                     MentionAll,
                                                     MessageComponent, Reply,
                                                     Text, Video, Voice)
from mirai_onebot.utils import logging

logger = logging.getLogger(__name__)

__all__ = [
    'MessageChain'
]


class MessageChain(object):
    """消息链"""

    def __init__(self, components: List[Union[Audio, File, Image, Location, Mention, MentionAll, Reply, Text, Video, Voice, str]]) -> None:
        # str 自动转为 Text
        for index, comp in enumerate(components):
            if isinstance(comp, str):
                components[index] = Text(comp)

        self.components = components

        self._idx = 0

    def append(self, comp: Union[Audio, File, Image, Location, Mention, MentionAll, Reply, Text, Video, Voice]):
        self.components.append(comp)

    def extend(self, comp: Union[Audio, File, Image, Location, Mention, MentionAll, Reply, Text, Video, Voice]):
        self.components.extend(comp)

    def to_message_chain(self):
        return [x.to_dict() for x in self.components]

    def has(self, comp: Union[Audio, File, Image, Location, Mention, MentionAll, Reply, Text, Video, Voice]) -> bool:
        """检测是否有某一组件/某一组件类型。

        Args:
            comp (Union[Audio, File, Image, Location, Mention, MentionAll, Reply, Text, Video, Voice]): 可传入如Text或Text('Hello')等形式

        Returns:
            bool: 结果
        """
        result = False
        # 未实例化
        if isinstance(comp, type):
            for x in self.components:
                if type(x) == comp:
                    result = True

        # 实例化
        if isinstance(comp, MessageComponent):
            for x in self.components:
                if x == comp:
                    result = True

        return result

    def __getitem__(self, idx: int):
        return self.components[idx]

    def __contains__(self, comp:  Union[Audio, File, Image, Location, Mention, MentionAll, Reply, Text, Video, Voice]) -> bool:
        return self.has(comp)

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        try:
            result = self.components[self._idx]
        except:
            raise StopIteration

        self._idx += 1
        return result
