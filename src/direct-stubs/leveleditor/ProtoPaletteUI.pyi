from typing import Any, TypeVar

import wx  # type: ignore[import-untyped]
import wx.siplib as sip  # type: ignore[import-untyped]
from direct._typing import Incomplete

from .LevelEditor import LevelEditor
from .PaletteTreeCtrl import PaletteTreeCtrl
from .ProtoPalette import ProtoPalette

_T = TypeVar('_T')

class UniversalDropTarget(wx.PyDropTarget, metaclass=sip.wrapper):
    editor: LevelEditor
    do: wx.DataObjectComposite
    filedo: wx.FileDataObject
    textdo: wx.TextDataObject
    bmpdo: wx.BitmapDataObject
    def __init__(self, editor: LevelEditor) -> None: ...
    def OnData(self, x, y, d: _T) -> _T: ...

class ProtoPaletteUI(wx.Panel, metaclass=sip.wrapper):
    editor: LevelEditor
    palette: ProtoPalette
    tree: PaletteTreeCtrl
    editorTxt: str
    opSortAlpha: str
    opSortOrig: str
    opSort: str
    opAdd: str
    opDelete: str
    menuItemsGen: list[str]
    menuItemsSel: list[str]
    popupmenu: wx.Menu
    def __init__(self, parent: Any, editor: LevelEditor) -> None: ...
    def populate(self) -> None: ...
    def OnBeginLabelEdit(self, event) -> None: ...
    def OnEndLabelEdit(self, event) -> None: ...
    def menuAppendGenItems(self) -> None: ...
    def menuAppendSelItems(self) -> None: ...
    def onShowPopup(self, event) -> None: ...
    def onPopupItemSelected(self, event) -> None: ...
    def AquireFile(self, filename: str) -> None: ...
    def addNewItem(self, result: tuple[str, Incomplete] | tuple[str, Incomplete, Incomplete]) -> None: ...
    def compareItems(self, item1, item2): ...
