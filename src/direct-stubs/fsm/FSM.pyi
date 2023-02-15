__all__ = ['FSM', 'FSMException']

from collections.abc import Callable, Collection, Mapping, Sequence
from typing import Any, ClassVar
from typing_extensions import TypeVarTuple, Unpack

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from direct.stdpy.threading import RLock

_T = TypeVarTuple('_T')

class FSMException(Exception): ...
class AlreadyInTransition(FSMException): ...
class RequestDenied(FSMException): ...

class FSM(DirectObject):
    notify: ClassVar[Notifier]
    SerialNum: ClassVar[int]
    fsmLock: RLock
    stateArray: Sequence[str]
    state: str | None
    oldState: str | None
    newState: str
    defaultTransitions: Mapping[str, Collection[str]] | None
    def __init__(self, name: str) -> None: ...
    def cleanup(self) -> None: ...
    def setBroadcastStateChanges(self, doBroadcast: bool) -> None: ...
    def getStateChangeEvent(self) -> str: ...
    def getCurrentFilter(self) -> Callable[..., Any]: ...
    def getCurrentOrNextState(self) -> str: ...
    def getCurrentStateOrTransition(self) -> str: ...
    def isInTransition(self) -> bool: ...
    def forceTransition(self, request: str, *args: Any) -> None: ...
    def demand(self, request: str, *args: Any) -> None: ...
    def request(self, request: str, *args: Any) -> Any: ...
    def defaultEnter(self, *args: object) -> None: ...
    def defaultExit(self) -> None: ...
    def defaultFilter(self, request: str, args: tuple[Unpack[_T]]) -> tuple[str, Unpack[_T]] | None: ...
    def filterOff(self, request: str, args: tuple[Unpack[_T]]) -> tuple[str, Unpack[_T]] | None: ...
    def setStateArray(self, stateArray: Sequence[str]) -> None: ...
    def requestNext(self, *args: Any) -> None: ...
    def requestPrev(self, *args: Any) -> None: ...
