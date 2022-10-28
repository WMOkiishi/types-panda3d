__all__ = ['EntryScale', 'EntryScaleGroup']

import tkinter
from collections.abc import Callable
from typing import Any

import Pmw  # type: ignore[import]
from panda3d.core import NodePath

class EntryScale(Pmw.MegaWidget):
    value: float
    entryFormat: str
    fScaleCommand: bool
    labelFrame: tkinter.Frame
    entryValue: tkinter.StringVar
    entry: Pmw.EntryField
    label: tkinter.Label
    minMaxFrame: tkinter.Frame
    minLabel: tkinter.Label
    scale: tkinter.Scale
    maxLabel: tkinter.Label
    def __init__(self, parent=..., **kw) -> None: ...
    def askForLabel(self, event=...) -> None: ...
    def askForMin(self, event=...) -> None: ...
    def setMin(self, newMin: float) -> None: ...
    def askForMax(self, event=...) -> None: ...
    def setMax(self, newMax: float) -> None: ...
    def askForResolution(self, event=...) -> None: ...
    def setResolution(self, newResolution: float) -> None: ...
    def get(self) -> float: ...
    def set(self, newVal: float, fCommand: bool = ...) -> None: ...
    def onReturn(self, *args) -> None: ...
    def onReturnRelease(self, *args) -> None: ...
    def onPress(self, *args) -> None: ...
    def onRelease(self, *args) -> None: ...

class EntryScaleGroup(Pmw.MegaToplevel):
    balloon: Pmw.Balloon
    toggleBalloonVar: tkinter.IntVar
    entryScaleList: list
    def __init__(self, parent=..., **kw): ...
    def toggleBalloon(self) -> None: ...
    def get(self) -> list: ...
    def getAt(self, index: int): ...
    def set(self, value, fCommand: bool = ...) -> None: ...
    def setAt(self, index: int, value) -> None: ...
    def reset(self) -> None: ...
    def onReturn(self, *args) -> None: ...
    def onReturnRelease(self, *args) -> None: ...
    def onPress(self, *args) -> None: ...
    def onRelease(self, *args) -> None: ...

def rgbPanel(nodePath: NodePath, callback: Callable[[Any], object] | None = ...) -> EntryScaleGroup: ...
