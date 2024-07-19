from yiriob.message import (At, Face, Forward, Json, MessageChain, Reply, Text,
                            Xml)


def test_messagechain():
    comps = [
        Text("hello"),
        Face(1),
    ]
    chain = MessageChain(comps)

    assert chain.to_cqcode() == "hello[CQ:face,id=1]"
    assert Text("hello").to_cqcode() in chain
    assert Text("hello") in chain
    assert Text("world") not in chain
    assert "hello" in chain
    assert "world" not in chain
    assert "[CQ:face,id=1]" in chain
    assert "[CQ:face,id=2]" not in chain

    assert list(chain) == comps
    assert chain.to_dict() == [
        {"type": "text", "data": {"text": "hello"}},
        {"type": "face", "data": {"id": "1"}},
    ]

    chain += Text("world")
    assert chain.to_cqcode() == "hello[CQ:face,id=1]world"

    chain -= Text("hello")
    assert chain.to_cqcode() == "[CQ:face,id=1]world"

    assert chain[0] == Face(1)
    assert chain[1] == "world"
    assert chain[1] != {}

    assert repr(chain[0]) == "[CQ:face,id=1]"

    assert At("111").to_cqcode() == "[CQ:at,qq=111]"
    assert Reply("111").to_cqcode() == "[CQ:reply,id=111]"
    assert Forward("111").to_cqcode() == "[CQ:forward,id=111]"
    assert Xml("<a/>").to_cqcode() == "[CQ:xml,data=<a/>]"
    assert Json("{}").to_cqcode() == "[CQ:json,data={}]"
