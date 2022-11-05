from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from typing import Any, TypeVar

import wx  # type: ignore[import]
from direct._typing import Unused
from .LevelEditor import LevelEditor

_T = TypeVar('_T')

class ProtoDropTarget(wx.PyDropTarget):
    ui = ...
    do: wx.DataObjectComposite
    filedo: wx.FileDataObject
    textdo: wx.TextDataObject
    bmpdo: wx.BitmapDataObject
    def __init__(self, ui) -> None: ...
    def OnData(self, x: Unused, y: Unused, d: _T) -> _T: ...

class ProtoObjsUI(wx.Panel, metaclass=ABCMeta):
    editor: LevelEditor
    protoObjs = ...
    supportedExts: Iterable[str]
    llist: wx.ListCtrl
    opDelete: str
    menuItems: list[str]
    popupmenu: wx.Menu
    def __init__(self, parent: Any, editor: LevelEditor, protoObjs, supportedExts: Iterable[str]) -> None: ...
    def populate(self) -> None: ...
    @abstractmethod
    def addObj(self, filename) -> None: ...
    def onPopupItemSelected(self, event) -> None: ...
    def onShowPopup(self, event) -> None: ...
    def findLabel(self, text) -> bool: ...
    def removeItem(self, index: int) -> None: ...
    def remove(self) -> None: ...
    def add(self, filename: str | bytes) -> None: ...
    def addNewItem(self, result) -> None: ...
    def AquireFile(self, filename: str) -> None: ...
