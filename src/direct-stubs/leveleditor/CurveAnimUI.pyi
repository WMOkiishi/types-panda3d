from typing import Any

import wx  # type: ignore[import]
from direct._typing import Obj, Unused
from direct.interval import MetaInterval
from panda3d.core import NodePath
from .LevelEditor import LevelEditor
from .ObjectPaletteBase import ObjectCurve

class CurveAnimUI(wx.Dialog):
    editor: LevelEditor
    nodePath: NodePath
    curve: Obj[NodePath, ObjectCurve] | None
    mainPanel: wx.Panel
    chooseNode: wx.StaticText
    chooseNodeTxt: wx.TextCtrl
    chooseNodeButton: wx.Button
    chooseCurve: wx.StaticText
    chooseCurveTxt: wx.TextCtrl
    chooseCurveButton: wx.Button
    duritionTime: wx.StaticText
    duritionTimeSpin: wx.SpinCtrl
    createAnimButton: wx.Button
    saveAnimButton: wx.Button
    time: int
    curveSequence: MetaInterval.Sequence
    def __init__(self, parent: Any, editor: LevelEditor) -> None: ...
    def SetProperties(self) -> None: ...
    def DoLayout(self) -> None: ...
    def OnChooseNode(self, evt: Unused) -> None: ...
    def OnChooseCurve(self, evt: Unused) -> None: ...
    def OnCreateAnim(self, evt: Unused) -> None: ...
    def OnSaveAnim(self, evt: Unused) -> None: ...
    def OnExit(self, evt: Unused) -> None: ...
