from collections.abc import Callable
from typing import Any

import wx  # type: ignore[import]
import wx.siplib as sip  # type: ignore[import]

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
        style=...,
        validator=...,
        name: str = ...,
        textSize: tuple[int, int] = ...,
    ) -> None: ...
    def GetValue(self) -> float: ...
    def SetValue(self, value: float) -> None: ...
    def onChange(self, event) -> None: ...
    def onEnter(self, event) -> None: ...
    def bindFunc(self, updateCB) -> None: ...
    def Disable(self) -> None: ...
    def Enable(self) -> None: ...
