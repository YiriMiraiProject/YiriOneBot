from mirai_onebot.message import (Audio, File, Image, Location, Mention,
                                  MentionAll, MessageChain, Reply, Text, Video,
                                  Voice)


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

    print(message_chain.to_message_chain())
