import sys
from typing import ClassVar

import wx  # type: ignore[import]
import wx.glcanvas as wxgl  # type: ignore[import]
import wx.siplib as sip  # type: ignore[import]
from panda3d.core import ButtonHandle, ConfigVariableBool, GraphicsWindow, InputDevice

class EmbeddedPandaWindow(wx.Window, metaclass=sip.wrapper):
    win: GraphicsWindow
    def __init__(self, *args, **kw) -> None: ...
    def cleanup(self) -> None: ...
    def onSize(self, event) -> None: ...

class OpenGLPandaWindow(wxgl.GLCanvas, metaclass=sip.wrapper):
    removeCallbackWindow: ClassVar[ConfigVariableBool]
    Keymap: ClassVar[dict[int, ButtonHandle]]
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
