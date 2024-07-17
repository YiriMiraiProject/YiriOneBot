from pydantic import BaseModel, model_serializer
from .message_components import MessageComponent
from typing import Any


class MessageChain(BaseModel):
    components: list[MessageComponent]

    def __init__(self, components: list[MessageComponent]) -> None:
        super().__init__(components=components)

    @model_serializer
    def model_ser(self) -> list[dict[str, Any]]:
        return [x.model_dump(mode="json") for x in self.components]

    def to_cqcode(self) -> str:
        """转换成 CQ 码。不保证完全正确，谨慎使用。如有问题，请提 Issue。

        Returns:
            CQ 码
        """
        return "".join([x.to_cqcode() for x in self.components])


__all__ = ["MessageChain"]
