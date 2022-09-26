__all__ = ['FourStateAI']

from collections.abc import Sequence
from typing import ClassVar
from typing_extensions import Literal, TypeAlias
from _typeshed import SupportsGetItem

from direct.directnotify.Notifier import Notifier
from panda3d.core import AsyncTask
from .ClassicFSM import ClassicFSM
from .State import State

_StateIndex: TypeAlias = Literal[0, 1, 2, 3, 4]
_Unused: TypeAlias = object

class FourStateAI:
    notify: ClassVar[Notifier]
    stateIndex: _StateIndex
    nextStateIndex: _StateIndex
    doLaterTask: AsyncTask | None
    names: SupportsGetItem[_StateIndex, str]
    durations: SupportsGetItem[_StateIndex, float | None]
    states: dict[_StateIndex, State]
    fsm: ClassicFSM
    def __init__(self, names: Sequence[str], durations: SupportsGetItem[_StateIndex, float | None] = ...) -> None: ...
    def delete(self) -> None: ...
    def getState(self) -> list[int]: ...
    def sendState(self) -> None: ...
    def setIsOn(self, isOn: bool) -> None: ...
    def isOn(self) -> bool: ...
    def changedOnState(self, isOn: bool) -> None: ...
    def switchToNextStateTask(self, task: _Unused) -> Literal[0]: ...
    def distributeStateChange(self) -> None: ...
    def enterStateN(self, stateIndex: _StateIndex, nextStateIndex: _StateIndex) -> None: ...
    def exitStateN(self) -> None: ...
    def enterState0(self) -> None: ...
    def exitState0(self) -> None: ...
    def enterState1(self) -> None: ...
    def exitState1(self) -> None: ...
    def enterState2(self) -> None: ...
    def exitState2(self) -> None: ...
    def enterState3(self) -> None: ...
    def exitState3(self) -> None: ...
    def enterState4(self) -> None: ...
    def exitState4(self) -> None: ...
