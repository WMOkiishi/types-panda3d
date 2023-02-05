from typing import Any, SupportsFloat
from typing_extensions import Final

import wx  # type: ignore[import]
import wx.siplib as sip  # type: ignore[import]
from direct._typing import Unused
from direct.wxwidgets.ViewPort import Viewport
from direct.wxwidgets.WxPandaShell import WxPandaShell
from direct.wxwidgets.WxSlider import WxSlider

from .AnimControlUI import AnimControlUI
from .CurveAnimUI import CurveAnimUI
from .GraphEditorUI import GraphEditorUI
from .LevelEditor import LevelEditor

ID_NEW: Final = 101
ID_OPEN: Final = 102
ID_SAVE: Final = 103
ID_SAVE_AS: Final = 104
ID_EXPORT_TO_MAYA: Final = 105
ID_DUPLICATE: Final = 201
ID_MAKE_LIVE: Final = 202
ID_UNDO: Final = 203
ID_REDO: Final = 204
ID_SHOW_GRID: Final = 301
ID_GRID_SIZE: Final = 302
ID_GRID_SNAP: Final = 303
ID_SHOW_PANDA_OBJECT: Final = 304
ID_HOT_KEYS: Final = 305
ID_PARENT_TO_SELECTED: Final = 306
ID_CREATE_CURVE: Final = 601
ID_EDIT_CURVE: Final = 602
ID_CURVE_ANIM: Final = 603
ID_ANIM: Final = 701
ID_GRAPH: Final = 702

class PandaTextDropTarget(wx.TextDropTarget, metaclass=sip.wrapper):
    editor: LevelEditor
    view: Viewport
    def __init__(self, editor: LevelEditor, view: Viewport) -> None: ...
    def OnDropText(self, x: float, y: float, text: str) -> bool | None: ...

class LevelEditorUIBase(WxPandaShell, metaclass=sip.wrapper):
    editor: LevelEditor
    contextMenu: ViewportMenu
    menuEdit: wx.Menu
    menuOptions: wx.Menu
    showGridMenuItem: wx.MenuItem
    gridSizeMenuItem: wx.MenuItem
    gridSnapMenuItem: wx.MenuItem
    showPandaObjectsMenuItem: wx.MenuItem
    parentToSelectedMenuItem: wx.MenuItem
    hotKeysMenuItem: wx.MenuItem
    menuCurve: wx.Menu
    createCurveMenuItem: wx.MenuItem
    editCurveMenuItem: wx.MenuItem
    curveAnimMenuItem: wx.MenuItem
    menuAnim: wx.Menu
    editAnimMenuItem: wx.MenuItem
    graphEditorMenuItem: wx.MenuItem
    graphEditorUI: GraphEditorUI
    animUI: AnimControlUI
    curveAnimUI: CurveAnimUI
    def __init__(self, editor: LevelEditor) -> None: ...
    def bindKeyEvents(self, toBind: bool = True) -> None: ...
    def onGraphEditor(self, e: Unused) -> None: ...
    def onAnimation(self, e: Unused) -> None: ...
    def onCurveAnim(self, e: Unused) -> None: ...
    def onCreateCurve(self, e: Unused) -> None: ...
    def onEditCurve(self, e: Unused) -> None: ...
    def updateMenu(self) -> None: ...
    def onRightDown(self, evt=None) -> None: ...
    def onKeyDownEvent(self, evt) -> None: ...
    def onKeyUpEvent(self, evt) -> None: ...
    def onKeyEvent(self, evt) -> None: ...
    def reset(self) -> None: ...
    def onNew(self, evt: Unused = None) -> None: ...
    def onOpen(self, evt: Unused = None) -> None: ...
    def onSave(self, evt=None) -> bool | None: ...
    def onSaveAs(self, evt: Unused) -> bool: ...
    def onExportToMaya(self, evt: Unused) -> None: ...
    def onDuplicate(self, evt: Unused) -> None: ...
    def onMakeLive(self, evt: Unused) -> None: ...
    def toggleGrid(self, evt: Unused) -> None: ...
    def toggleGridSnap(self, evt: Unused) -> None: ...
    def onGridSize(self, evt: Unused) -> None: ...
    def onShowPandaObjects(self, evt: Unused) -> None: ...
    def onDestroy(self, evt: Unused) -> None: ...
    def updateGrids(self, newSize, newSpacing) -> None: ...
    def onHotKeys(self, evt: Unused) -> None: ...
    def buildContextMenu(self, nodePath: Unused): ...
    def replaceObject(self, evt, all: bool = False) -> None: ...

class GridSizeUI(wx.Dialog, metaclass=sip.wrapper):
    parent: Any
    gridSizeSlider: WxSlider
    gridSpacingSlider: WxSlider
    def __init__(self, parent: Any, id, title: str, gridSize: SupportsFloat, gridSpacing: SupportsFloat) -> None: ...
    def onApply(self, evt: Unused) -> None: ...

class ViewportMenu(wx.Menu, metaclass=sip.wrapper):
    def __init__(self) -> None: ...
    def addItem(self, name, parent: Any | None = None, call=None, id=None) -> None: ...
    def addMenu(self, name, parent: Any | None = None, id=None) -> wx.Menu: ...

class CurveDegreeUI(wx.Dialog, metaclass=sip.wrapper):
    parent: Any
    degree: wx.RadioBox
    def __init__(self, parent: Any, id, title: str) -> None: ...
    def onApply(self, evt) -> None: ...
