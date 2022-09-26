from abc import ABCMeta, abstractmethod
from typing import Any

wx: Any

class ProtoDropTarget(wx.PyDropTarget):
    ui = ...
    do: wx.DataObjectComposite
    filedo: wx.FileDataObject
    textdo: wx.TextDataObject
    bmpdo: wx.BitmapDataObject
    def __init__(self, ui) -> None: ...
    def OnData(self, x, y, d): ...

class ProtoObjsUI(wx.Panel, metaclass=ABCMeta):
    editor = ...
    protoObjs = ...
    supportedExts = ...
    llist: wx.ListCtrl
    opDelete: str
    menuItems: list[str]
    popupmenu: wx.Menu
    def __init__(self, parent, editor, protoObjs, supportedExts) -> None: ...
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