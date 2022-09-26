__all__ = ['FakeObject', 'GarbageLogger', 'GarbageReport', '_createGarbage']

from collections.abc import Callable, Generator
from typing import Any, ClassVar

from ..directnotify.Notifier import Notifier
from .Job import Job

GarbageCycleCountAnnounceEvent: str

class FakeObject: ...

class FakeDelObject:
    def __del__(self) -> None: ...

def _createGarbage(num: int = ...) -> None: ...

class GarbageReport(Job):
    notify: ClassVar[Notifier]
    numGarbageInstances: int
    garbageInstanceIds: set[int]
    garbage: list[object]
    numGarbage: int
    referrersByReference: dict[int, list[int]]
    referrersByNumber: dict[int, list[object]]
    cycles: list[int]
    cyclesBySyntax: list[str]
    uniqueCycleSets: set[tuple[int, ...]]
    cycleIds: set[int]
    def __init__(
        self,
        name: str,
        log: bool = True,
        verbose: bool = False,
        fullReport: bool = False,
        findCycles: bool = True,
        threaded: bool = False,
        doneCallback: Callable[[GarbageReport], object] | None = None,
        autoDestroy: bool = False,
        priority: int | None = None,
        safeMode: bool = False,
        delOnly: bool = False,
        collect: bool = True,
    ) -> None: ...
    def run(self) -> Generator[Any | None, None, None]: ...
    def getNumCycles(self) -> int: ...
    def getDesc2numDict(self) -> dict: ...
    def getGarbage(self) -> list[object]: ...
    def getReport(self) -> str: ...

class GarbageLogger(GarbageReport): ...
def checkForGarbageLeaks() -> int: ...
def b_checkForGarbageLeaks(wantReply: bool = False) -> int: ...
