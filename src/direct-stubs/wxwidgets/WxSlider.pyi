from collections.abc import Callable
from typing import Any

import wx  # type: ignore
import wx.siplib as sip  # type: ignore

class WxSlider(wx.Slider, metaclass=sip.wrapper):
    maxValue: float
    minValue: float
    textValue: wx.TextCtrl | None
    updateCB: Callable[[Any], object] | None
    def __init__(
        self,
        parent,
        id,
        value: float,
        minValue: float,
        maxValue: float,
        pos=...,
        size=...,
        style=4,
        validator=...,
        name: str = 'slider',
        textSize: tuple[int, int] = (40, 20),
    ) -> None: ...
    def GetValue(self) -> float: ...
    def SetValue(self, value: float) -> None: ...
    def onChange(self, event) -> None: ...
    def onEnter(self, event) -> None: ...
    def bindFunc(self, updateCB) -> None: ...
    def Disable(self) -> None: ...
    def Enable(self) -> None: ...
