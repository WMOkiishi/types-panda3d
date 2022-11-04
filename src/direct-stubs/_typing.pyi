from collections.abc import Callable
from typing import Any, TypeVar
from typing_extensions import TypeAlias

AnyReal = TypeVar('AnyReal', int, float)  # noqa: Y001

Incomplete: TypeAlias = Any
SimpleCallback: TypeAlias = Callable[[], object]
Unused: TypeAlias = object
