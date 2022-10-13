import wx  # type: ignore[import]
from wx.lib.embeddedimage import PyEmbeddedImage  # type: ignore[import]
from .LevelEditor import LevelEditor

FirstFrame: PyEmbeddedImage
PreFrame: PyEmbeddedImage
PreKeyFrame: PyEmbeddedImage
PrePlay: PyEmbeddedImage
Play: PyEmbeddedImage
NextKeyFrame: PyEmbeddedImage
NextFrame: PyEmbeddedImage
LastFrame: PyEmbeddedImage
Key: PyEmbeddedImage
Stop: PyEmbeddedImage
DeleteKey: PyEmbeddedImage

class TimeSlider(wx.Window):
    points: list
    numbers: list
    curFrame: int
    sliderStartFrame: int
    sliderEndFrame: int
    frameNum: int
    buffer: wx.Bitmap
    unitWidth: float
    def __init__(self, parent, slidersize, sliderStartFrame: int, sliderEndFrame: int, curFrame: int) -> None: ...
    def InitBuffer(self) -> None: ...
    def SetTimeSliderData(self, sliderStartFrame: int = ..., sliderEndFrame: int = ..., curFrame: int = ...) -> None: ...
    def OnPaint(self, evt) -> None: ...
    def DrawTimeSlider(self, dc) -> None: ...
    def DrawNumber(self, dc) -> None: ...
    def DrawFrame(self, dc) -> None: ...
    def DrawKeys(self, dc) -> None: ...
    def OnSize(self, evt) -> None: ...
    def OnLeftDown(self, evt) -> None: ...
    def OnLeftUp(self, evt) -> None: ...
    def OnMotion(self, evt) -> None: ...

class TimeRange(wx.Window):
    startFrame: int
    endFrame: int
    sliderStartFrame: int
    sliderEndFrame: int
    frameNum: int
    w = ...
    h = ...
    buffer: wx.Bitmap
    unitWidth: float
    rangePosX: float
    rangePosY: float
    rangeWidth: float
    rangeHeight: float
    curRect: wx.Rect
    def __init__(self, parent, rangesize, startFrame: int, endFrame: int, sliderStartFrame: int, sliderEndFrame: int) -> None: ...
    def InitBuffer(self) -> None: ...
    def SetTimeRangeData(
        self, startFrame: int = ..., endFrame: int = ..., sliderStartFrame: int = ..., sliderEndFrame: int = ...
    ) -> None: ...
    def OnPaint(self, evt) -> None: ...
    def DrawTimeRange(self, dc) -> None: ...
    def OnSize(self, evt) -> None: ...
    def OnLeftDown(self, evt) -> None: ...
    def OnLeftUp(self, evt) -> None: ...
    def OnMotion(self, evt) -> None: ...
    def MainPanelUpdate(self) -> None: ...

class AnimControlUI(wx.Dialog):
    editor: LevelEditor
    parallel: list
    keys = ...
    prePlay: bool
    play: bool
    stop: bool
    curFrame: int
    startFrame: int
    sliderStartFrame: int
    endFrame: int
    sliderEndFrame: int
    mainPanel1: wx.Panel
    timeSlider: TimeSlider
    curFrameSpin: wx.SpinCtrl
    bmpPrePlay = ...
    bmpPlay = ...
    bmpStop = ...
    buttonFirstFrame: wx.BitmapButton
    buttonPreFrame: wx.BitmapButton
    buttonPreKeyFrame: wx.BitmapButton
    buttonPrePlay: wx.BitmapButton
    buttonPlay: wx.BitmapButton
    buttonNextKeyFrame: wx.BitmapButton
    buttonNextFrame: wx.BitmapButton
    buttonLastFrame: wx.BitmapButton
    mainPanel2: wx.Panel
    timeStartSpin: wx.SpinCtrl
    timeSliderStartSpin: wx.SpinCtrl
    timeRange: TimeRange
    timeSliderEndSpin: wx.SpinCtrl
    timeEndSpin: wx.SpinCtrl
    buttonDeleteKey: wx.BitmapButton
    timeUnit: float
    timer: wx.Timer
    dialogSizer: wx.BoxSizer
    def __init__(self, parent, editor: LevelEditor) -> None: ...
    def SetProperties(self) -> None: ...
    def DoLayout(self) -> None: ...
    def OnCurrentTime(self, evt) -> None: ...
    def OnControl(self) -> None: ...
    def OnFirstFrame(self, evt) -> None: ...
    def OnPreFrame(self, evt) -> None: ...
    def sortKey(self) -> None: ...
    def OnPreKeyFrame(self, evt) -> None: ...
    def OnTimer(self, evt) -> None: ...
    def OnPrePlay(self, evt) -> None: ...
    def OnPlay(self, evt) -> None: ...
    def OnNextKeyFrame(self, evt) -> None: ...
    def OnNextFrame(self, evt) -> None: ...
    def OnLastFrame(self, evt) -> None: ...
    def OnTime(self) -> None: ...
    def OnTimeStartSpin(self, evt) -> None: ...
    def OnTimeSliderStartSpin(self, evt) -> None: ...
    def OnTimeSliderEndSpin(self, evt) -> None: ...
    def OnTimeEndSpin(self, evt) -> None: ...
    def OnDeleteKey(self, evt) -> None: ...
    def OnPropKey(self) -> None: ...
    def OnAnimation(self, curFrame: int) -> None: ...
    def OnExit(self, evt) -> None: ...
