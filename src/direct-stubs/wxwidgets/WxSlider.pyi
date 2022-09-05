from typing import Any

wx: Any

class WxSlider(wx.Slider):
    maxValue: float
    minValue: float
    textValue: wx.TextCtrl | None
    updateCB = ...
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
        name: str = 'slider',
        textSize: tuple[int, int] = ...,
    ) -> None: ...
    def GetValue(self) -> float: ...
    def SetValue(self, value: float) -> None: ...
    def onChange(self, event) -> None: ...
    def onEnter(self, event) -> None: ...
    def bindFunc(self, updateCB) -> None: ...
    def Disable(self) -> None: ...
    def Enable(self) -> None: ...
