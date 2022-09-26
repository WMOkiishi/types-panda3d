from collections.abc import Callable
from typing import TypeVar
from typing_extensions import TypeAlias

AnyReal = TypeVar('AnyReal', int, float)

SimpleCallback: TypeAlias = Callable[[], object]
Unused: TypeAlias = object
