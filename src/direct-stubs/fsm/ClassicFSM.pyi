__all__ = ['ClassicFSM']

from collections.abc import Iterable
from typing import ClassVar
from typing_extensions import Literal

from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject
from .State import State

class ClassicFSM(DirectObject):
    notify: ClassVar[Notifier]
    ALLOW: ClassVar[Literal[0]]
    DISALLOW: ClassVar[Literal[1]]
    DISALLOW_VERBOSE: ClassVar[Literal[2]]
    ERROR: ClassVar[Literal[3]]
    onUndefTransition: Literal[0, 1, 2, 3]
    inspecting: bool
    def __init__(
        self,
        name: str,
        states: Iterable[State] = ...,
        initialStateName: str | None = None,
        finalStateName: str | None = None,
        onUndefTransition: Literal[0, 1, 2, 3] = DISALLOW_VERBOSE,
    ) -> None: ...
    def enterInitialState(self, argList=...) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def getStates(self) -> list[str]: ...
    def setStates(self, states: Iterable[State]) -> None: ...
    def addState(self, state: State) -> None: ...
    def getInitialState(self): ...
    def setInitialState(self, initialStateName: str) -> None: ...
    def getFinalState(self): ...
    def setFinalState(self, finalStateName: str) -> None: ...
    def requestFinalState(self) -> None: ...
    def getCurrentState(self): ...
    def getStateNamed(self, stateName: str): ...
    def hasStateNamed(self, stateName: str) -> bool: ...
    def request(self, aStateName: str, enterArgList=..., exitArgList=..., force: bool = False) -> bool: ...
    def forceTransition(self, aStateName: str, enterArgList=..., exitArgList=...) -> None: ...
    def conditional_request(self, aStateName: str, enterArgList=..., exitArgList=...) -> bool: ...
    def view(self) -> None: ...
    def isInternalStateInFlux(self) -> bool: ...
