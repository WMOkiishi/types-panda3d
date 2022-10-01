from collections.abc import Sequence
from typing import Any, SupportsFloat, Union
from typing_extensions import TypeAlias

from panda3d.core import LVecBase2f

wx: Any
PyEmbeddedImage: TypeAlias = wx.lib.embeddedimage.PyEmbeddedImage

_Vec2f: TypeAlias = Union[LVecBase2f, tuple[float, float]]

property: PyEmbeddedImage
ZoomIn: PyEmbeddedImage
ZoomOut: PyEmbeddedImage
OneTangent: PyEmbeddedImage
TwoTangents: PyEmbeddedImage

class GraphEditorWindow(wx.Window):
    w = ...
    h = ...
    zoom: float
    object = ...
    curFrame = ...
    property = ...
    zeroPos: tuple[float, float]
    zero: int
    unitWidth: float
    unitHeight: float
    X: list
    Y: list
    Z: list
    buffer: wx.EmptyBitmap
    def __init__(
        self,
        parent,
        windowSize,
        property,
        xRange: SupportsFloat,
        yRange: SupportsFloat,
        curFrame: int,
        object,
    ) -> None: ...
    def refresh(self) -> None: ...
    def generateInfo(self) -> None: ...
    def generateHandler(self, item): ...
    def InitBuffer(self) -> None: ...
    def SetGraphEditorData(self, property, curFrame: int = ...) -> None: ...
    def OnPaint(self, evt) -> None: ...
    def DrawXCoord(self, dc) -> None: ...
    def DrawYCoord(self, dc) -> None: ...
    def drawXNumber(self, dc, st, pos: float) -> None: ...
    def drawYNumber(self, dc, st, pos: float) -> None: ...
    def DrawFrame(self, dc) -> None: ...
    def drawX(self, dc) -> None: ...
    def drawY(self, dc) -> None: ...
    def drawZ(self, dc) -> None: ...
    def DrawCurve(self, dc) -> None: ...
    def drawSingleCurve(self, list: Sequence, dc) -> None: ...
    def drawKeys(self, list: Sequence, dc) -> None: ...
    def drawHandler(self, list: Sequence, dc) -> None: ...
    def DrawSelectRec(self, dc) -> None: ...
    def OnSize(self, evt) -> None: ...
    def OnLeftDown(self, evt) -> None: ...
    def OnLeftUp(self, evt) -> None: ...
    def OnMiddleDown(self, evt) -> None: ...
    def OnMiddleUp(self, evt) -> None: ...
    def OnMotion(self, evt) -> None: ...
    def setExistKey(self, list: Sequence) -> bool: ...
    def setNewKey(self, list: Sequence) -> None: ...
    def setSelection(self) -> None: ...
    def setSelectionBase(self, list: Sequence) -> None: ...
    def inside(self, point0: _Vec2f, point1: _Vec2f, point: _Vec2f) -> bool: ...
    def recalculateSlope(self) -> None: ...
    def recalculateSlopeBase(self, list: Sequence) -> None: ...
    def selectHandler(self) -> None: ...
    def onAnimation(self) -> None: ...

class GraphEditorUI(wx.Dialog):
    editor = ...
    object = ...
    xRange: int
    yRange: int
    curFrame: int
    mainPanel1: wx.Panel
    buttonZoomIn: wx.BitmapButton
    buttonZoomOut: wx.BitmapButton
    buttonOneTangent: wx.BitmapButton
    buttonTwoTangents: wx.BitmapButton
    mainPanel2: wx.Panel
    tree: wx.TreeCtrl
    namestr: str
    root = ...
    str: str
    graphEditorWindow: GraphEditorWindow
    dialogSizer: wx.BoxSizer
    def __init__(self, parent, editor, object) -> None: ...
    def SetProperties(self) -> None: ...
    def DoLayout(self) -> None: ...
    def AddTreeNodes(self, parentItem, items) -> None: ...
    def OnSelChanged(self, evt) -> None: ...
    def OnZoomIn(self, evt) -> None: ...
    def OnZoomOut(self, evt) -> None: ...
    def OnOneTangent(self, evt) -> None: ...
    def OnTwoTangents(self, evt) -> None: ...
    def curFrameChange(self) -> None: ...
    def OnExit(self, evt) -> None: ...
