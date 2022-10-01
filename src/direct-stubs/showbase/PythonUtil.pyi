from _typeshed import Self, SupportsWrite
from collections.abc import Callable, Collection, Container, Generator, Iterable, Mapping, MutableSequence, Sequence
from typing import Any, ClassVar, Generic, TypeVar, overload
from typing_extensions import Never, TypeAlias

from direct._typing import AnyReal, SimpleCallback
from direct.tkwidgets.Valuator import ValuatorGroupPanel
from panda3d.core import PStatCollector

_T = TypeVar('_T')
_S = TypeVar('_S')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_C = TypeVar('_C', bound=SimpleCallback)

_RNG: TypeAlias = Callable[[], float]

class Functor(Generic[_T]):
    def __init__(self, function: Callable[..., _T], *args: Any, **kargs: Any) -> None: ...
    def destroy(self) -> None: ...
    def __call__(self, *args: Any, **kargs: Any) -> _T: ...

class Stack(Generic[_T]):
    def __init__(self) -> None: ...
    def push(self, item: _T) -> None: ...
    def top(self) -> _T: ...
    def pop(self) -> _T: ...
    def clear(self) -> None: ...
    def isEmpty(self) -> bool: ...
    def __len__(self) -> int: ...

class Queue(Generic[_T]):
    def __init__(self) -> None: ...
    def push(self, item: _T) -> None: ...
    def top(self) -> _T: ...
    def front(self) -> _T: ...
    def back(self) -> _T: ...
    def pop(self) -> _T: ...
    def clear(self) -> None: ...
    def isEmpty(self) -> bool: ...
    def __len__(self) -> int: ...

def indent(stream: SupportsWrite[str], numIndents: int, str: str) -> None: ...
def doc(obj: object) -> None: ...
def adjust(command: Callable[..., Any] | None = None, dim: Any = ..., parent: Any = None, **kw: Any) -> ValuatorGroupPanel: ...
def difference(a: Collection[_T], b: Collection[_T]) -> list[_T]: ...
def intersection(a: Collection[_T], b: Collection[_T]) -> list[_T]: ...
def union(a: Collection[_T], b: Collection[_T]) -> list[_T]: ...
def sameElements(a: Collection[_T], b: Collection[_T]) -> bool: ...
@overload
def makeList(x: list[_T] | tuple[_T, ...]) -> list[_T]: ...
@overload
def makeList(x: _T) -> list[_T]: ...
@overload
def makeTuple(x: list[_T] | tuple[_T, ...]) -> tuple[_T, ...]: ...  # type: ignore[misc]
@overload
def makeTuple(x: _T) -> tuple[_T]: ...
def list2dict(L: Iterable[_KT], value: _VT = None) -> dict[_KT, _VT]: ...
def listToIndex2item(L: Iterable[_VT]) -> dict[int, _VT]: ...
def listToItem2index(L: Iterable[_KT]) -> dict[_KT, int]: ...
def invertDict(D: Mapping[_KT, _VT], lossy: bool = False) -> dict[_VT, _KT]: ...
def invertDictLossless(D: Mapping[_KT, _VT]) -> dict[_VT, list[_KT]]: ...
def uniqueElements(L: Collection[object]) -> bool: ...
def disjoint(L1: Iterable[object], L2: Iterable[object]) -> bool: ...
def contains(whole: Container[object], sub: Iterable[object]) -> bool: ...
def replace(list: MutableSequence[_T], old: _T, new: _T, all: bool = False) -> int: ...

rad90: float
rad180: float
rad270: float
rad360: float

def reduceAngle(deg: float) -> float: ...
def fitSrcAngle2Dest(src: float, dest: float) -> float: ...
def fitDestAngle2Src(src: float, dest: float) -> float: ...
def closestDestAngle2(src: float, dest: float) -> float: ...
def closestDestAngle(src: float, dest: float) -> float: ...

class StdoutCapture:
    def __init__(self) -> None: ...
    def destroy(self) -> None: ...
    def getString(self) -> str: ...
    def write(self, string: str) -> None: ...

class StdoutPassthrough(StdoutCapture): ...

def getSetterName(valueName: str, prefix: str = ...) -> str: ...
def getSetter(targetObj: Any, valueName: str, prefix: str = ...) -> Any: ...
def mostDerivedLast(classList: list[type]) -> None: ...
def bound(value: AnyReal, bound1: AnyReal, bound2: AnyReal) -> AnyReal: ...
clamp = bound
def lerp(v0: AnyReal, v1: AnyReal, t: AnyReal) -> AnyReal: ...
def getShortestRotation(start: AnyReal, end: AnyReal) -> tuple[AnyReal, AnyReal]: ...
def average(*args: float) -> float: ...

class Averager:
    def __init__(self, name: object) -> None: ...
    def reset(self) -> None: ...
    def addValue(self, value: float) -> None: ...
    def getAverage(self) -> float: ...
    def getCount(self) -> int: ...

def addListsByValue(a: Iterable[AnyReal], b: Iterable[AnyReal]) -> list[AnyReal]: ...
def boolEqual(a: _S, b: _T) -> _S | _T | bool: ...
def lineupPos(i: int, num: int, spacing: float) -> float: ...
def formatElapsedSeconds(seconds: float) -> str: ...
def solveQuadratic(a: float, b: float, c: float) -> tuple[float, float] | float | None: ...
def findPythonModule(module: str) -> str | None: ...
def clampScalar(value: AnyReal, a: AnyReal, b: AnyReal) -> AnyReal: ...
def weightedChoice(choiceList: Iterable[tuple[float, _T]], rng: _RNG = ..., sum: float | None = None) -> _T: ...
def randFloat(a: float, b: float = ..., rng: _RNG = ...) -> float: ...
def normalDistrib(a: float, b: float, gauss: Callable[[float, float], float] = ...) -> float: ...
def weightedRand(valDict: Mapping[_KT, float], rng: _RNG = ...) -> _KT: ...
def randUint31(rng: _RNG = ...) -> int: ...
def randInt32(rng: _RNG = ...) -> int: ...

class SerialNumGen:
    def __init__(self, start: int | None = None) -> None: ...
    def __next__(self) -> int: ...
    next = __next__

class SerialMaskedGen(SerialNumGen):
    def __init__(self, mask: int, start: int | None = None) -> None: ...

def serialNum() -> int: ...
def uniqueName(name: object) -> str: ...

class EnumIter:
    def __init__(self, enum: Enum) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> int: ...
    next = __next__

class Enum:
    def __init__(self, items: str | Iterable[str], start: int = ...) -> None: ...
    def __iter__(self) -> EnumIter: ...
    def hasString(self, string: str) -> bool: ...
    def fromString(self, string: str) -> int: ...
    def getString(self, value: int) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __len__(self) -> int: ...
    def copyTo(self, obj: Enum) -> None: ...

class Singleton(type):
    def __init__(cls, name: str, bases: tuple[type, ...], dic: dict[str, Any]) -> None: ...

class SingletonError(ValueError): ...

def printListEnumGen(l: Sequence[object]) -> Generator[None, None, None]: ...
def printListEnum(l: Sequence[object]) -> None: ...

dtoolSuperBase: Any | None
safeReprNotify: Any | None

def safeRepr(obj: object) -> str: ...
def safeReprTypeOnFail(obj: object) -> str: ...
def fastRepr(obj: object, maxLen: int = ..., strFactor: int = ..., _visitedIds: set[int] | None = None) -> str: ...
def convertTree(objTree: Mapping[_KT, Any], idList: Mapping[_KT, object]) -> dict: ...
def r_convertTree(oldTree: Mapping[_KT, Any], newTree: Mapping[str, Any], idList: Mapping[_KT, object]) -> None: ...
def pretty_print(tree: Mapping[str, object]) -> None: ...
def r_pretty_print(tree: Mapping[str, Any], num: int) -> None: ...
def isDefaultValue(x: object) -> bool: ...
def appendStr(obj: _T, st: str) -> _T: ...

class ScratchPad(Generic[_T]):
    def __init__(self, **kArgs: str) -> None: ...
    def __getattr__(self, name: str) -> _T: ...
    def __setattr__(self, name: str, value: _T) -> None: ...
    def add(self, **kArgs: _T) -> None: ...
    def destroy(self) -> None: ...
    def __getitem__(self, itemName: str) -> Any: ...
    @overload
    def get(self, itemName: str) -> _T | None: ...
    @overload
    def get(self, itemName: str, default: _S) -> _T | _S: ...
    def __contains__(self, itemName: object) -> bool: ...

class Sync:
    def __init__(self, name: str, other: Sync | None = None) -> None: ...
    def invalidate(self) -> None: ...
    def change(self) -> None: ...
    def sync(self, other: Sync) -> bool: ...
    def isSynced(self, other: Sync) -> bool: ...

def itype(obj: object) -> type | str: ...
def deeptype(obj: object, maxLen: int = ..., _visitedIds: set[int] | None = None) -> str: ...
def getNumberedTypedString(items: Sequence[object], maxLen: int = ..., numPrefix: str = ...) -> str: ...
def getNumberedTypedSortedString(items: Sequence[object], maxLen: int = ..., numPrefix: str = ...) -> str: ...
def printNumberedTyped(items: Sequence[object], maxLen: int = ...) -> None: ...
def printNumberedTypesGen(items: Sequence[object], maxLen: int = ...) -> Generator[None, None, None]: ...
def printNumberedTypes(items: Sequence[object], maxLen: int = ...) -> Generator[None, None, None]: ...

class DelayedCall:
    def __init__(self, func: SimpleCallback, name: str | None = None, delay: float | None = None) -> None: ...
    def destroy(self) -> None: ...
    def finish(self) -> None: ...

class FrameDelayedCall:
    def __init__(
        self,
        name: str,
        callback: SimpleCallback,
        frames: int | None = None,
        cancelFunc: SimpleCallback | None = None,
    ) -> None: ...
    def destroy(self) -> None: ...
    def finish(self) -> None: ...

class DelayedFunctor:
    def __init__(self, functor: Callable[..., object], name: str | None = None, delay: float | None = None) -> None: ...
    def __call__(self, *args: Any, **kwArgs: Any) -> None: ...

class SubframeCall:
    def __init__(self, functor: SimpleCallback, taskPriority: int | None, name: str | None = None) -> None: ...
    def cleanup(self) -> None: ...

class PStatScope:
    collectors: ClassVar[dict[str, PStatCollector]]
    levels: list[str]
    def __init__(self, level: str | None = None) -> None: ...
    def copy(self, push: bool | None = None) -> PStatScope: ...
    def push(self, level: str) -> None: ...
    def pop(self) -> str: ...
    def start(self, push: bool | None = None) -> None: ...
    def stop(self, pop: bool = False) -> None: ...
    def getCollector(self) -> PStatCollector: ...

def pstatcollect(scope: PStatScope, level: str | None = None) -> Callable[[_T], _T]: ...
def report(
    types: Container[str] = ...,
    prefix: str = ...,
    xform: Callable[[Any], object] | None = None,
    notifyFunc: Callable[[str], object] | None = None,
    dConfigParam: str | list[str] | tuple[str, ...] = ...,
) -> Callable[[_T], _T]: ...

def getBase(): ...
def getRepository(): ...
exceptionLoggedNotify: Any | None

GoldenRatio: float
class GoldenRectangle:
    @staticmethod
    def getLongerEdge(shorter: float) -> float: ...
    @staticmethod
    def getShorterEdge(longer: float) -> float: ...

def nullGen() -> Generator[Never, None, None]: ...
def loopGen(l: Iterable[_T]) -> Generator[_T, None, None]: ...
@overload
def makeFlywheelGen(
    objects: Sequence[_T],
    countList: MutableSequence[int],
    countFunc: object = None,
    scale: float | None = None,
) -> Generator[Generator[_T, None, None] | None, None, None]: ...
@overload
def makeFlywheelGen(
    objects: Sequence[_T],
    countList: None = None,
    countFunc: Callable[[_T], int] = ...,
    scale: float | None = None,
) -> Generator[Generator[_T, None, None] | None, None, None]: ...
@overload
def flywheel(
    objects: Sequence[_T],
    countList: MutableSequence[int],
    countFunc: object = None,
    scale: float | None = None,
) -> Generator[_T, None, None]: ...
@overload
def flywheel(
    objects: Sequence[_T],
    countList: None = None,
    countFunc: Callable[[_T], int] = ...,
    scale: float | None = None,
) -> Generator[_T, None, None]: ...

def getTotalAnnounceTime() -> float: ...
def getAnnounceGenerateTime(stat) -> float: ...

class MiniLog:
    indent: int
    name: str
    lines: list[str]
    def __init__(self, name: str) -> None: ...
    def enterFunction(self, funcName: str, *args: object, **kw: object) -> str: ...
    def exitFunction(self) -> int: ...
    def appendFunctionCall(self, line: str) -> str: ...
    def appendLine(self, line: str) -> str: ...
    def flush(self) -> str: ...

class MiniLogSentry:
    def __init__(self, log: MiniLog | None, funcName: str, *args: object, **kw: object) -> None: ...
    def __del__(self) -> None: ...

def logBlock(id: int, msg: object) -> None: ...

class HierarchyException(Exception):
    JOSWILSO: ClassVar[int]
    owner: object
    description: object
    def __init__(self, owner: object, description: object) -> None: ...

def formatTimeCompact(seconds: float) -> str: ...
def formatTimeExact(seconds: float) -> str: ...

class AlphabetCounter:
    def __init__(self) -> None: ...
    def __next__(self) -> str: ...
    next = __next__

class Default: ...

superLogFile: Any | None
def startSuperLog(customFunction: object = None) -> None: ...
def endSuperLog() -> None: ...
def configIsToday(configName: str) -> bool: ...
def typeName(o: object) -> str: ...
def safeTypeName(o: object) -> str: ...
def histogramDict(l: Iterable[_T]) -> dict[_T, int]: ...
def unescapeHtmlString(s: str) -> str: ...

class PriorityCallbacks:
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def add(self, callback: _C, priority: int | None = None) -> tuple[int, _C]: ...
    def remove(self, item: tuple[int, SimpleCallback]) -> None: ...
    def __call__(self) -> None: ...
