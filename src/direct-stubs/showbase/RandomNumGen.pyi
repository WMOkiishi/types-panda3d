__all__ = ['RandomNumGen', 'randHash']

from collections.abc import MutableSequence, Sequence
from typing import ClassVar, SupportsInt, TypeVar
from typing_extensions import SupportsIndex

from ..directnotify.Notifier import Notifier

_T = TypeVar('_T')

def randHash(num: SupportsInt | RandomNumGen) -> int: ...

class RandomNumGen:
    notify: ClassVar[Notifier]
    def __init__(self, seed: SupportsInt | RandomNumGen) -> None: ...
    def choice(self, seq: Sequence[_T]) -> _T: ...
    def shuffle(self, x: MutableSequence) -> None: ...
    def randrange(self, start: SupportsIndex, stop: SupportsIndex | None = None, step: SupportsIndex = ...) -> int: ...
    def randint(self, a: int, b: int) -> int: ...
    def random(self) -> float: ...
