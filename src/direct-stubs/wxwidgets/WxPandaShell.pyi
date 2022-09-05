from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal

from ..showbase.ShowBase import ShowBase
from ..task.Task import Task
from .WxAppShell import WxAppShell
from .ViewPort import Viewport

wx: Any

base: ShowBase
ID_FOUR_VIEW: Final[Literal[401]]
ID_TOP_VIEW: Final[Literal[402]]
ID_FRONT_VIEW: Final[Literal[403]]
ID_LEFT_VIEW: Final[Literal[404]]
ID_PERSP_VIEW: Final[Literal[405]]

class WxPandaShell(WxAppShell):
    MENU_TEXTS: ClassVar[dict[Literal[401, 402, 403, 404, 405], tuple[str, None]]]
    fStartDirect: bool
    wxApp: wx.App
    menuView: wx.Menu
    perspViewMenuItem = ...
    mainFrame: wx.SplitterWindow
    leftFrame: wx.SplitterWindow
    baseFrame: wx.SplitterWindow
    viewFrame = ...
    rightFrame: Any
    topView: Viewport
    frontView: Viewport
    leftView: Viewport
    perspView: Viewport
    leftBarUpPane: wx.Panel
    leftBarDownPane: wx.Panel
    rightBarUpPane: wx.Panel
    rightBarDownPane: wx.Panel
    evtLoop: wx.EventLoop
    oldLoop = ...
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
