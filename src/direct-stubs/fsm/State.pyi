__all__ = ['State']

import typing
from collections.abc import Callable, Iterable
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject
from .ClassicFSM import ClassicFSM

_ANY: TypeAlias = Literal['ANY']
_Callback: TypeAlias = Callable[..., object] | None

class State(DirectObject):
    notify: ClassVar[Notifier]
    Any: ClassVar[_ANY]
    def __init__(
        self,
        name: str,
        enterFunc: _Callback = None,
        exitFunc: _Callback = None,
        transitions: list[str] | _ANY = State.Any,
        inspectorPos=...,
    ) -> None: ...
    def getName(self) -> str: ...
    def setName(self, stateName: str) -> None: ...
    def getEnterFunc(self) -> _Callback: ...
    def setEnterFunc(self, stateEnterFunc: _Callback) -> None: ...
    def getExitFunc(self) -> _Callback: ...
    def setExitFunc(self, stateExitFunc: _Callback) -> None: ...
    def transitionsToAny(self) -> bool: ...
    def getTransitions(self) -> list[str]: ...
    def isTransitionDefined(self, otherState: str | State) -> bool | Literal[1]: ...
    def setTransitions(self, stateTransitions: list[str] | _ANY) -> None: ...
    def addTransition(self, transition: str) -> None: ...
    def getChildren(self) -> list[ClassicFSM]: ...
    def setChildren(self, FSMList: list[ClassicFSM]) -> None: ...
    def addChild(self, ClassicFSM: ClassicFSM) -> None: ...
    def removeChild(self, ClassicFSM: ClassicFSM) -> None: ...
    def hasChildren(self) -> bool: ...
    def enter(self, argList: Iterable[typing.Any] = ...) -> None: ...
    def exit(self, argList: Iterable[typing.Any] = ...) -> None: ...
