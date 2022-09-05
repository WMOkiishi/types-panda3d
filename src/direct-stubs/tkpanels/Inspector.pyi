__all__ = [
    'ClassInspector',
    'CodeInspector',
    'ComplexInspector',
    'DictionaryInspector',
    'FunctionInspector',
    'Inspector',
    'InspectorWindow',
    'InstanceInspector',
    'InstanceMethodInspector',
    'ModuleInspector',
    'SequenceInspector',
    'SliceInspector',
    'inspect',
    'inspectorFor',
]

from collections.abc import Callable, Iterable, Mapping, Sequence
from tkinter import Menu, Toplevel
from types import CodeType, ModuleType
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal, Protocol

_T = TypeVar('_T')
_T_co = TypeVar('_T_co')

class _FunctionLike(Protocol):
    @property
    def __name__(self) -> str: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class _MethodLike(_FunctionLike, Protocol):
    @property
    def __self__(self) -> object: ...

def inspect(anObject: _T) -> InspectorWindow[_T]: ...
def inspectorFor(anObject: _T) -> Inspector[_T]: ...
def initializeInspectorMap() -> None: ...

class Inspector(Generic[_T_co]):
    object: _T_co
    lastPartNumber: int
    def __init__(self, anObject: _T_co) -> None: ...
    def initializePartsList(self) -> None: ...
    def initializePartNames(self) -> None: ...
    def title(self) -> str: ...
    def getLastPartNumber(self) -> int: ...
    def selectedPart(self) -> Any: ...
    def namedParts(self) -> list[str]: ...
    def stringForPartNumber(self, partNumber: int) -> str: ...
    @overload
    def partNumber(self, partNumber: Literal[0]) -> _T_co: ...
    @overload
    def partNumber(self, partNumber: int) -> Any: ...
    def inspectorFor(self, part: _T) -> Inspector[_T]: ...
    def privatePartNumber(self, partNumber: int) -> str: ...
    def partNames(self) -> list[str]: ...
    def objectType(self) -> type[_T_co]: ...

class ModuleInspector(Inspector[ModuleType]): ...
class ClassInspector(Inspector[type]): ...
class InstanceInspector(Inspector[object]): ...
class FunctionInspector(Inspector[_FunctionLike]): ...
class InstanceMethodInspector(Inspector[_MethodLike]): ...
class CodeInspector(Inspector[CodeType]): ...
class ComplexInspector(Inspector[complex]): ...
class DictionaryInspector(Inspector[Mapping]): ...
class SequenceInspector(Inspector[Sequence]): ...
class SliceInspector(Inspector[slice]): ...

class InspectorWindow(Generic[_T_co]):
    inspectors: list[Inspector[_T_co]]
    top: Toplevel
    def __init__(self, inspector: Inspector[_T_co]) -> None: ...
    def topInspector(self) -> Inspector[_T_co]: ...
    def selectedPart(self) -> Any: ...
    def inspectedObject(self) -> _T_co: ...
    def open(self) -> None: ...
    def createViews(self) -> None: ...
    def setTitle(self) -> None: ...
    def createListWidget(self) -> None: ...
    def createTextWidgets(self) -> None: ...
    def createMenus(self) -> None: ...
    def fillList(self) -> None: ...
    def listSelectionChanged(self, event) -> None: ...
    def popOrDive(self, event) -> None: ...
    def evalCommand(self, event) -> None: ...
    def inspect(self) -> None: ...
    def pop(self) -> None: ...
    def dive(self) -> None: ...
    def update(self) -> None: ...
    def showHelp(self) -> None: ...
    def selectedIndex(self) -> int | None: ...
    def inspectorForSelectedPart(self) -> Inspector[Any] | None: ...
    def popupMenu(self, event) -> None: ...
    def createPopupMenu(self, part: _T, menuList: Iterable[tuple[str, Callable[[_T], Any | str]]]) -> Menu: ...
