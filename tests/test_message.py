from yiriob.message import MessageChain, Text, Face


def test_messagechain():
    chain = MessageChain(
        [
            Text("hello"),
            Face(1),
        ]
    )

    assert chain.to_cqcode() == "hello[CQ:face,id=1]"
