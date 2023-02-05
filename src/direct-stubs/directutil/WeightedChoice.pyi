from collections.abc import Iterable, Sequence
from typing import Protocol

class _RNG(Protocol):
    def randrange(self, __start: int) -> int: ...

class WeightedChoice:
    total: int
    listOfLists: Iterable[Sequence[int]]
    weightIndex: int
    def __init__(self, listOfLists: Iterable[Sequence[int]], weightIndex: int = 0) -> None: ...
    def choose(self, rng: _RNG = ...) -> Sequence[int]: ...
