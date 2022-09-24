__all__ = ['WidgetPropertiesDialog']

from collections.abc import Iterable
from tkinter import Misc, Toplevel
from typing import Any, TypeVar

from typing_extensions import TypeAlias

_Self = TypeVar('_Self')

Pmw: Any

_PropertyDict: TypeAlias = dict[str, tuple[Any, Any, Any, bool]]

class WidgetPropertiesDialog(Toplevel):
    propertyDict: _PropertyDict
    propertyList: Iterable[str]
    parent: Misc | None
    modifiedDict: _PropertyDict
    initial_focus: WidgetPropertiesDialog
    def __init__(
        self,
        propertyDict: _PropertyDict,
        propertyList: Iterable[str] | None = None,
        parent: Misc | None = None,
        title: str = 'Widget Properties',
    ) -> None: ...
    def body(self: _Self, master: Misc | None) -> Pmw.EntryField | _Self: ...
    def modified(self, widget, entry, property: str, type, fNone: bool) -> None: ...
    def buttonbox(self) -> None: ...
    def realOrNone(self, val: str): ...
    def intOrNone(self, val: str): ...
    def ok(self, event=None) -> None: ...
    def cancel(self, event=None) -> None: ...
    def validateChanges(self) -> None: ...
    def apply(self) -> None: ...
