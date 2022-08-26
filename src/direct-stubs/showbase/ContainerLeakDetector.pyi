from collections.abc import Callable, Generator
from typing import Any, ClassVar, TypeAlias, overload

from ..directnotify.Notifier import Notifier
from .Job import Job

_Callback: TypeAlias = Callable[[], object]

class NoDictKey: ...

class Indirection:
    evalStr = ...
    dictKey = ...
    def __init__(self, evalStr: str | None = None, dictKey=...) -> None: ...
    def destroy(self) -> None: ...
    def acquite(self) -> None: ...
    def release(self) -> None: ...
    def isDictKey(self) -> bool: ...
    def dereferenceDictKey(self, parentDict): ...
    def getString(self, prevIndirection=None, nextIndirection=None) -> str: ...

class ObjectRef:
    notify: ClassVar[Notifier]
    def __init__(self, indirection, objId, other: ObjectRef | None = None) -> None: ...
    def destroy(self) -> None: ...
    def getNumIndirections(self) -> int: ...
    @overload
    def goesThroughGen(self, obj: object) -> Generator[bool | None, None, None]: ...
    @overload
    def goesThroughGen(self, *, objId: int) -> Generator[bool | None, None, None]: ...
    @overload
    def goesThrough(self, obj: object) -> bool: ...
    @overload
    def goesThrough(self, *, objId: int) -> bool: ...
    def getContainerGen(self, getInstance: bool = False) -> Generator[Any | None, None, None]: ...
    def getEvalStrGen(self, getInstance: bool = False) -> Generator[str | None, None, None]: ...
    def getFinalIndirectionStr(self) -> str: ...

class FindContainers(Job):
    def __init__(self, name: str, leakDetector): ...
    def destroy(self) -> None: ...
    def getPriority(self) -> int: ...
    @staticmethod
    def getStartObjAffinity(startObj: object) -> int: ...
    def run(self) -> Generator[Any | None, None, None]: ...

class CheckContainers(Job):
    ReprItems: ClassVar[int]
    notify: Notifier
    def __init__(self, name: str, leakDetector, index: int) -> None: ...
    def destroy(self) -> None: ...
    def getPriority(self) -> int: ...
    def run(self) -> Generator[Any | None, None, None]: ...

class FPTObjsOfType(Job):
    notify: Notifier
    def __init__(
        self,
        name: str,
        leakDetector: ContainerLeakDetector,
        otn: str,
        doneCallback: _Callback | None = None,
    ) -> None: ...
    def destroy(self) -> None: ...
    def getPriority(self) -> int: ...
    def run(self) -> Generator[Any | None, None, None]: ...
    def finished(self) -> None: ...

class FPTObjsNamed(Job):
    notify: Notifier
    def __init__(
        self,
        name: str,
        leakDetector: ContainerLeakDetector,
        on: str,
        doneCallback: _Callback | None = None,
    ) -> None: ...
    def destroy(self) -> None: ...
    def getPriority(self) -> int: ...
    def run(self) -> Generator[Any | None, None, None]: ...
    def finished(self) -> None: ...

class PruneObjectRefs(Job):
    notify: Notifier
    def __init__(self, name: str, leakDetector: ContainerLeakDetector) -> None: ...
    def destroy(self) -> None: ...
    def getPriority(self) -> int: ...
    def run(self) -> Generator[Any | None, None, None]: ...

class ContainerLeakDetector(Job):
    notify: ClassVar[Notifier]
    PrivateIds: ClassVar[set[int]]
    def __init__(self, name: str, firstCheckDelay: float | None = None) -> None: ...
    def destroy(self) -> None: ...
    @classmethod
    def addPrivateObj(cls, obj: object) -> None: ...
    @classmethod
    def removePrivateObj(cls, obj: object) -> None: ...
    def getContainerIds(self) -> list[int]: ...
    def getContainerByIdGen(self, id: int, **kwArgs): ...
    def getContainerById(self, id: int): ...
    def getContainerNameByIdGen(self, id: int, **kwArgs): ...
    def getContainerNameById(self, id: int) -> str: ...
    def removeContainerById(self, id: int) -> None: ...
    def run(self) -> Generator[Any, None, None]: ...
    def getPathsToContainers(self, name: str, ot: str, doneCallback: _Callback | None = None) -> FPTObjsOfType: ...
    def getPathsToContainersNamed(self, name: str, on: str, doneCallback: _Callback | None = None) -> FPTObjsNamed: ...