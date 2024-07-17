from pydantic import BaseModel, model_serializer
from .message_components import MessageComponent
from typing import TYPE_CHECKING, Any, Generator, SupportsIndex, Literal


class MessageChain(BaseModel):
    components: list[MessageComponent]

    def __init__(self, components: list[MessageComponent]) -> None:
        super().__init__(components=components)

    def to_dict(self) -> list[dict[str, Any]]:
        return [x.to_dict() for x in self.components]

    def to_cqcode(self) -> str:
        """转换成 CQ 码。不保证完全正确，谨慎使用。如有问题，请提 Issue。

        Returns:
            CQ 码
        """
        return "".join([x.to_cqcode() for x in self.components])

    def has(self, obj: MessageComponent | str | object) -> bool:
        if isinstance(obj, str):
            return obj in self.to_cqcode()
        return obj in self.components

    def __contains__(self, obj: MessageComponent | str | object) -> bool:
        return self.has(obj)

    def __iter__(self) -> Generator[MessageComponent, None, None]:  # type: ignore
        return (x for x in self.components)

    def __len__(self) -> int:
        return len(self.components)

    def __add__(self, obj: MessageComponent) -> "MessageChain":
        self.components.append(obj)
        return self

    def __sub__(self, obj: MessageComponent) -> "MessageChain":
        self.components.remove(obj)
        return self

    def __getitem__(self, index: SupportsIndex):
        return self.components.__getitem__(index)


__all__ = ["MessageChain"]
