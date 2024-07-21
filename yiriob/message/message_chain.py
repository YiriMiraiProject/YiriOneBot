from typing import Annotated, Any, Iterable

from pydantic import GetCoreSchemaHandler, WrapSerializer
from pydantic_core import CoreSchema, core_schema

from .message_components import MessageComponent, Text


class MessageChain(list[MessageComponent]):
    def __init__(self, iterable: Iterable[MessageComponent | str], /) -> None:
        self.extend([Text(x) if isinstance(x, str) else x for x in iterable])

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler(list[MessageComponent])
        )

    def to_dict(self) -> list[dict[str, Any]]:
        return [x.to_dict() for x in self]

    def to_cqcode(self) -> str:
        """转换成 CQ 码。不保证完全正确，谨慎使用。如有问题，请提 Issue。

        Returns:
            CQ 码
        """
        return "".join([x.to_cqcode() for x in self])

    def has(self, obj: MessageComponent | str | object) -> bool:
        if isinstance(obj, str):
            return obj in self.to_cqcode()
        return obj in self

    def __contains__(self, obj: MessageComponent | str | object) -> bool:
        return self.has(obj)


__all__ = ["MessageChain"]
