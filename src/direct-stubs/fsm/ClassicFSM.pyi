__all__ = ['ClassicFSM']

from collections.abc import Iterable
from typing import Any, ClassVar
from typing_extensions import Final, Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject

from .State import State

class ClassicFSM(DirectObject):
    notify: ClassVar[Notifier]
    ALLOW: Final = 0
    DISALLOW: Final = 1
    DISALLOW_VERBOSE: Final = 2
    ERROR: Final = 3
    onUndefTransition: Literal[0, 1, 2, 3]
    inspecting: bool
    def __init__(
        self,
        name: str,
        states: Iterable[State] = ...,
        initialStateName: str | None = ...,
        finalStateName: str | None = ...,
        onUndefTransition: Literal[0, 1, 2, 3] = ...,
    ) -> None: ...
    def enterInitialState(self, argList: Iterable[Any] = ...) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def getStates(self) -> list[str]: ...
    def setStates(self, states: Iterable[State]) -> None: ...
    def addState(self, state: State) -> None: ...
    def getInitialState(self) -> State: ...
    def setInitialState(self, initialStateName: str) -> None: ...
    def getFinalState(self) -> State: ...
    def setFinalState(self, finalStateName: str) -> None: ...
    def requestFinalState(self) -> None: ...
    def getCurrentState(self) -> State: ...
    def getStateNamed(self, stateName: str) -> State: ...
    def hasStateNamed(self, stateName: str) -> bool: ...
    def request(
        self, aStateName: str, enterArgList: Iterable[Any] = ..., exitArgList: Iterable[Any] = ..., force: bool = ...
    ) -> bool: ...
    def forceTransition(self, aStateName: str, enterArgList: Iterable[Any] = ..., exitArgList: Iterable[Any] = ...) -> None: ...
    def conditional_request(
        self, aStateName: str, enterArgList: Iterable[Any] = ..., exitArgList: Iterable[Any] = ...
    ) -> bool: ...
    def view(self) -> None: ...
    def isInternalStateInFlux(self) -> bool: ...
