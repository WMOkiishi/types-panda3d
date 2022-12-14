__all__ = ['WidgetPropertiesDialog']

import tkinter
from _typeshed import Self
from collections.abc import Iterable
from typing import Any
from typing_extensions import TypeAlias

import Pmw  # type: ignore[import]

_PropertyDict: TypeAlias = dict[str, tuple[Any, Any, Any, bool]]

class WidgetPropertiesDialog(tkinter.Toplevel):
    propertyDict: _PropertyDict
    propertyList: Iterable[str]
    parent: tkinter.Misc | None
    modifiedDict: _PropertyDict
    initial_focus: WidgetPropertiesDialog
    def __init__(
        self,
        propertyDict: _PropertyDict,
        propertyList: Iterable[str] | None = ...,
        parent: tkinter.Misc | None = ...,
        title: str = ...,
    ) -> None: ...
    def body(self: Self, master: tkinter.Misc | None) -> Pmw.EntryField | Self: ...
    def modified(self, widget, entry, property: str, type, fNone: bool) -> None: ...
    def buttonbox(self) -> None: ...
    def realOrNone(self, val: str): ...
    def intOrNone(self, val: str): ...
    def ok(self, event=...) -> None: ...
    def cancel(self, event=...) -> None: ...
    def validateChanges(self) -> None: ...
    def apply(self) -> None: ...
