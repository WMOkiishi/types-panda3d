from typing import ClassVar, Final, Literal, overload

import wx  # type: ignore
import wx.siplib as sip  # type: ignore
from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task
from wx.lib.agw.fourwaysplitter import FourWaySplitter  # type: ignore

from .ViewPort import Viewport
from .WxAppShell import WxAppShell

base: ShowBase
ID_FOUR_VIEW: Final = 401
ID_TOP_VIEW: Final = 402
ID_FRONT_VIEW: Final = 403
ID_LEFT_VIEW: Final = 404
ID_PERSP_VIEW: Final = 405

class WxPandaShell(WxAppShell, metaclass=sip.wrapper):
    MENU_TEXTS: ClassVar[dict[int, tuple[str, str | None]]]
    fStartDirect: bool
    wxApp: wx.App
    menuView: wx.Menu
    perspViewMenuItem: wx.MenuItem
    mainFrame: wx.SplitterWindow
    leftFrame: wx.SplitterWindow
    baseFrame: wx.SplitterWindow
    viewFrame: FourWaySplitter
    rightFrame: wx.SplitterWindow
    topView: Viewport
    frontView: Viewport
    leftView: Viewport
    perspView: Viewport
    leftBarUpPane: wx.Panel
    leftBarDownPane: wx.Panel
    rightBarUpPane: wx.Panel
    rightBarDownPane: wx.Panel
    evtLoop: wx.EventLoop
    oldLoop: wx.EventLoopBase
    currentView: Viewport | None
    def __init__(self, fStartDirect: bool = False) -> None: ...
    def createMenu(self) -> None: ...
    def initialize(self) -> None: ...
    @overload
    def wxStep(self, task: Task) -> Literal[1]: ...
    @overload
    def wxStep(self, task: None = None) -> None: ...
    def onViewChange(self, evt, viewIdx: int) -> None: ...
    def getCurrentView(self) -> Viewport | None: ...
