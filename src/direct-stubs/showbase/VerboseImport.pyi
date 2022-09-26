__all__: list[str] = []

from collections.abc import Mapping, Sequence
from typing import Any

indentLevel: int

def newimport(
    name: str,
    globals: Mapping[str, Any] | None = None,
    locals: Mapping[str, Any] | None = None,
    fromlist: Sequence[str] = (),
    level: int = ...,
) -> Any: ...
