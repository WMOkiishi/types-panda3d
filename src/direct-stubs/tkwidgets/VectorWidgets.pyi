__all__ = ['ColorEntry', 'VectorEntry', 'Vector2Entry', 'Vector3Entry', 'Vector4Entry']

import tkinter

import Pmw  # type: ignore[import]

from .Valuator import ValuatorGroupPanel

class VectorEntry(Pmw.MegaWidget):
    entryFormat: str
    menu: tkinter.Menu
    variableList: list[tkinter.StringVar]
    entryList: list[Pmw.EntryField]
    entryBackground: str
    def __init__(self, parent=..., **kw): ...
    def label(self) -> tkinter.Menubutton: ...
    def entry(self, index: int) -> Pmw.EntryField: ...
    def floaters(self) -> ValuatorGroupPanel: ...
    def get(self) -> list: ...
    def getAt(self, index: int): ...
    def set(self, value, fCommand: bool = ...) -> None: ...
    def setAt(self, index: int, value, fCommand: bool = ...) -> None: ...
    def action(self, fCommand: bool = ...) -> None: ...
    def reset(self) -> None: ...
    def addMenuItem(self, label: str = ..., command=...) -> None: ...
    def popupSliders(self) -> None: ...

class Vector2Entry(VectorEntry): ...
class Vector3Entry(VectorEntry): ...
class Vector4Entry(VectorEntry): ...

class ColorEntry(VectorEntry):
    def popupColorPicker(self) -> None: ...
