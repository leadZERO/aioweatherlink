from __future__ import annotations

from typing import (
    Any,
    Dict,
    Protocol,
    Type
)


class FromJson(Protocol):
    @classmethod
    def FromJson(cls: Type[FromJson], obj: Dict[str, Any]) -> FromJson:
        ...