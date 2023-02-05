from collections.abc import Callable, Iterable
from typing import Any

import wx  # type: ignore[import]
import wx.sipblib as sip  # type: ignore[import]
from direct._typing import Incomplete, Unused
from direct.wxwidgets.WxSlider import WxSlider
from wx.lib.agw.cubecolourdialog import CubeColourDialog  # type: ignore[import]
from wx.lib.embeddedimage import PyEmbeddedImage  # type: ignore[import]
from wx.lib.scrolledpanel import ScrolledPanel  # type: ignore[import]

from .LevelEditor import LevelEditor

Key: PyEmbeddedImage

class AnimFileDrop(wx.FileDropTarget, metaclass=sip.wrapper):
    editor: LevelEditor
    def __init__(self, editor: LevelEditor) -> None: ...
    def OnDropFiles(self, x: Unused, y: Unused, filenames: Iterable[str]) -> None: ...

class ObjectPropUI(wx.Panel, metaclass=sip.wrapper):
    parent: Any
    labelPane: wx.Panel
    label: wx.StaticText
    labelSizer: wx.BoxSizer
    setKeyButton: wx.BitmapButton
    uiPane: wx.Panel
    def __init__(self, parent: Any, label) -> None: ...
    def onKey(self, evt) -> None: ...
    def setValue(self, value) -> None: ...
    def getValue(self): ...
    def bindFunc(self, inFunc, outFunc, valFunc=None) -> None: ...

class ObjectPropUIEntry(ObjectPropUI, metaclass=sip.wrapper):
    ui: wx.TextCtrl
    eventType = ...
    def __init__(self, parent, label) -> None: ...
    def setValue(self, value: object) -> None: ...

class ObjectPropUISlider(ObjectPropUI, metaclass=sip.wrapper):
    ui: WxSlider
    def __init__(self, parent: Any, label, value, minValue: float, maxValue: float) -> None: ...

class ObjectPropUISpinner(ObjectPropUI, metaclass=sip.wrapper):
    ui: wx.SpinCtrl
    eventType = ...
    def __init__(self, parent: Any, label, value, minValue, maxValue) -> None: ...

class ObjectPropUICheck(ObjectPropUI, metaclass=sip.wrapper):
    ui: wx.CheckBox
    eventType = ...
    def __init__(self, parent: Any, label, value) -> None: ...

class ObjectPropUIRadio(ObjectPropUI, metaclass=sip.wrapper):
    ui: wx.RadioBox
    eventType = ...
    def __init__(self, parent: Any, label, value, valueList) -> None: ...
    def setValue(self, value) -> None: ...
    def getValue(self): ...

class ObjectPropUICombo(ObjectPropUI, metaclass=sip.wrapper):
    ui: wx.Choice
    eventType = ...
    def __init__(
        self,
        parent: Any,
        label,
        value,
        valueList,
        obj=None,
        callBack: Callable[[Incomplete, Incomplete, Incomplete], object] | None = None,
    ) -> None: ...
    def setItems(self, valueList) -> None: ...

class ObjectPropUITime(wx.Panel, metaclass=sip.wrapper):
    parent: Any
    labelPane: wx.Panel
    label: wx.StaticText
    labelSizer: wx.BoxSizer
    uiPane: wx.Panel
    uiAmPm: wx.Choice
    uiHour: wx.Choice
    uiMin: wx.Choice
    eventType = ...
    def __init__(self, parent: Any, label, value) -> None: ...
    def setValue(self, value: float) -> None: ...
    def getValue(self) -> float: ...
    def bindFunc(self, inFunc, outFunc, valFunc=None) -> None: ...

class ColorPicker(CubeColourDialog, metaclass=sip.wrapper):
    updateCB = ...
    def __init__(self, parent: Any, colourData=None, style=1, alpha: int = 255, updateCB=None, exitCB=None) -> None: ...
    def SetPanelColours(self) -> None: ...

class ObjectPropertyUI(ScrolledPanel, metaclass=sip.wrapper):
    editor: LevelEditor
    colorPicker: ColorPicker | None
    lastColorPickerPos: wx.Point | None
    lastPropTab: str | None
    propPane: wx.Panel
    nb: wx.Notebook
    transformPane: wx.Panel
    propX: ObjectPropUIEntry
    propY: ObjectPropUIEntry
    propZ: ObjectPropUIEntry
    propH: ObjectPropUISlider
    propP: ObjectPropUISlider
    propR: ObjectPropUISlider
    propSX: ObjectPropUIEntry
    propSY: ObjectPropUIEntry
    propSZ: ObjectPropUIEntry
    lookPane: wx.Panel
    propCR: ObjectPropUISlider
    propCG: ObjectPropUISlider
    propCB: ObjectPropUISlider
    propCA: ObjectPropUISlider
    propsPane: wx.Panel
    def __init__(self, parent: Any, editor: LevelEditor) -> None: ...
    def clearPropUI(self) -> None: ...
    def colorPickerExitCB(self, evt: Unused = None) -> None: ...
    def colorPickerUpdateCB(self, rr: float, gg: float, bb: float, aa: float) -> None: ...
    def onColorSlider(self, evt) -> None: ...
    def openColorPicker(self, evt, colourData, alpha: int) -> None: ...
    def updateProps(self, obj, movable: bool = True) -> None: ...
