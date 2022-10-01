from collections.abc import Callable
from typing import TypeVar
from typing_extensions import TypeAlias

AnyReal = TypeVar('AnyReal', int, float)  # noqa: Y001

SimpleCallback: TypeAlias = Callable[[], object]
Unused: TypeAlias = object
