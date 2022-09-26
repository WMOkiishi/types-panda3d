from typing import Any, ClassVar

wx: Any

class WxAppShell(wx.Frame):
    appversion: ClassVar[str]
    appname: ClassVar[str]
    copyright: ClassVar[str]
    contactname: ClassVar[str]
    contactemail: ClassVar[str]
    frameWidth: ClassVar[int]
    frameHeight: ClassVar[int]
    padx: ClassVar[int]
    pady: ClassVar[int]
    usecommandarea: ClassVar[int]
    usestatusarea: ClassVar[int]
    balloonState: ClassVar[str]
    panelCount: ClassVar[int]
    menuFile: wx.Menu
    menuHelp: wx.Menu
    def __init__(self, *args, **kw) -> None: ...
    def showAbout(self, event) -> None: ...
    def quit(self, event=None) -> None: ...
    def appInit(self) -> None: ...
    def createInterface(self) -> None: ...
    def onDestroy(self, event) -> None: ...
    def createMenuBar(self) -> None: ...
