import sys
from typing import ClassVar

import wx  # type: ignore[import]
import wx.glcanvas as wxgl  # type: ignore[import]
from panda3d.core import ConfigVariableBool, GraphicsWindow, InputDevice

class EmbeddedPandaWindow(wx.Window):
    win: GraphicsWindow
    def __init__(self, *args, **kw) -> None: ...
    def cleanup(self) -> None: ...
    def onSize(self, event) -> None: ...

class OpenGLPandaWindow(wxgl.GLCanvas):
    removeCallbackWindow: ClassVar[ConfigVariableBool]
    Keymap: ClassVar[dict]
    visible: bool
    win: GraphicsWindow
    hasCapture: bool
    inputDevice: InputDevice | None
    def __init__(self, *args, **kw): ...
    def cleanup(self) -> None: ...
    def onSize(self, event) -> None: ...
    def onPaint(self, event) -> None: ...
    def onIdle(self, event) -> None: ...

if sys.platform == 'darwin' or sys.platform == 'linux':
    WxPandaWindow = OpenGLPandaWindow
else:
    WxPandaWindow = EmbeddedPandaWindow
