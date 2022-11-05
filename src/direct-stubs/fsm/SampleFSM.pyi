# undocumented

__all__ = ['ClassicStyle', 'NewStyle', 'ToonEyes']

from typing import overload
from typing_extensions import Literal, TypeVarTuple, Unpack

from direct._typing import Unused

from .FSM import FSM

_T = TypeVarTuple('_T')  # type: ignore[misc]

class ClassicStyle(FSM):
    def enterRed(self) -> None: ...
    def exitRed(self) -> None: ...
    def enterYellow(self) -> None: ...
    def exitYellow(self) -> None: ...
    def enterGreen(self) -> None: ...
    def exitGreen(self) -> None: ...

class NewStyle(FSM):
    def enterRed(self) -> None: ...
    @overload
    def filterRed(self, request: Literal['advance'], args: Unused) -> Literal['Green']: ...  # type: ignore[misc]
    @overload
    def filterRed(self, request: str, args: tuple[Unpack[_T]]) -> tuple[str, Unpack[_T]] | None: ...  # type: ignore[misc]
    def exitRed(self) -> None: ...
    def enterYellow(self) -> None: ...
    @overload
    def filterYellow(self, request: Literal['advance'], args: Unused) -> Literal['Red']: ...  # type: ignore[misc]
    @overload
    def filterYellow(self, request: str, args: tuple[Unpack[_T]]) -> tuple[str, Unpack[_T]] | None: ...  # type: ignore[misc]
    def exitYellow(self) -> None: ...
    def enterGreen(self) -> None: ...
    @overload
    def filterGreen(self, request: Literal['advance'], args: Unused) -> Literal['Yellow']: ...  # type: ignore[misc]
    @overload
    def filterGreen(self, request: str, args: tuple[Unpack[_T]]) -> tuple[str, Unpack[_T]] | None: ...  # type: ignore[misc]
    def exitGreen(self) -> None: ...

class ToonEyes(FSM):
    def __init__(self) -> None: ...
    def defaultFilter(self, request: str, args: Unused) -> str | None: ...  # type: ignore[override]
    def enterOpen(self) -> None: ...
    def filterOpen(self, request: str, args: Unused) -> str | None: ...
    def enterClosed(self) -> None: ...
    def filterClosed(self, request: str, args: Unused) -> str | None: ...
    def enterSurprised(self) -> None: ...
    def enterOff(self) -> None: ...
