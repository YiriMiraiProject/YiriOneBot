import pytest

from mirai_onebot.message import (Audio, File, Image, Location, Mention,
                                  MentionAll, MessageChain, Reply, Text, Video,
                                  Voice)
from mirai_onebot.message.message_components import MessageComponent


def test_comps():
    assert Audio('test').file_id == 'test'
    assert File('test').file_id == 'test'
    assert Image('test').file_id == 'test'

    location = Location(0, 0, 'hello', 'originpoint')
    assert location.latitude == 0
    assert location.longitude == 0
    assert location.title == 'hello'
    assert location.content == 'originpoint'

    assert Mention('test').user_id == 'test'
    assert MentionAll().message_type == 'mention_all'
    assert Reply('test msgid', 'test userid').message_id == 'test msgid'
    assert Reply('test msgid', 'test userid').user_id == 'test userid'

    assert Text('test').text == 'test'
    assert Text('test').to_dict() == {'type': 'text', 'data': {'text': 'test'}}
    assert Text('test').__repr__() == "text: {'text': 'test'}"
    assert Text('test') == 'test'
    assert Text('test') == Text('test')

    assert Video('test').file_id == 'test'
    assert Voice('test').file_id == 'test'
    assert Voice('test') == Voice

    for comp in [
        {
            "type": "text",
            "data": {
                "text": "OneBot is not a bot"
            }
        },
        {
            "type": "mention",
            "data": {
                "user_id": "1234567"
            }
        },
        {
            "type": "mention_all",
            "data": {}
        },
        {
            "type": "image",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
        },
        {
            "type": "voice",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
        },
        {
            "type": "audio",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
        },
        {
            "type": "video",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
        },
        {
            "type": "file",
            "data": {
                "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
            }
        },
        {
            "type": "location",
            "data": {
                "latitude": 31.032315,
                "longitude": 121.447127,
                "title": "上海交通大学闵行校区",
                "content": "中国上海市闵行区东川路800号"
            }
        },
        {
            "type": "reply",
            "data": {
                "message_id": "6283",
                "user_id": "1234567"
            }
        }
    ]:
        msgComp = MessageComponent.load_from_dict(comp)
        assert msgComp.message_type == comp['type']
        assert msgComp.data == comp['data']

    with pytest.raises(ValueError):
        MessageComponent.load_from_dict({'type': 'fake'})


def test_message_chain():
    message_chain = MessageChain([
        'hello',
        Text('hello text')
    ])

    assert message_chain[0] == Text('hello')
    assert message_chain[1] == Text('hello text')

    message_chain.append(MentionAll())

    assert message_chain[2] == MentionAll()

    message_chain.extend([File('test1'), File('test2')])

    assert message_chain[3] == File('test1')
    assert message_chain[4] == File('test2')
    assert File in message_chain
    assert not File('test3') in message_chain
    assert File('test2') in message_chain

    # 迭代器测试
    comp = []
    for item in message_chain:
        comp.append(item)

    assert len(comp) == len(message_chain.components)
    assert message_chain.to_dict().__len__() == len(message_chain.components)

    message_chain = MessageChain.load_from_dict({
        'message': [
            {
                'type': 'text',
                'data': {
                    'text': 'OneBot is not a bot'
                }
            }
        ]
    })

    assert message_chain[0].message_type == 'text'
    assert message_chain[0].data == {'text': 'OneBot is not a bot'}
    assert message_chain[0].text == 'OneBot is not a bot'
