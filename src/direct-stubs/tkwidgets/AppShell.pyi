__all__ = ['AppShell']

import tkinter
from collections.abc import MutableMapping
from typing import Any, ClassVar, TypeVar
from typing_extensions import Literal, TypeAlias

import Pmw  # type: ignore[import]
from direct._typing import Unused
from direct.showbase.DirectObject import DirectObject

from .Dial import Dial
from .EntryScale import EntryScale
from .Floater import Floater
from .Slider import Slider
from .VectorWidgets import ColorEntry, Vector2Entry, Vector3Entry

_WidgetT = TypeVar('_WidgetT', bound=tkinter.Widget)
_TkAnchor: TypeAlias = Literal['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se']
_TkFill: TypeAlias = Literal['none', 'x', 'y', 'both']
_TkRelief: TypeAlias = Literal['raised', 'sunken', 'flat', 'ridge', 'solid', 'groove']
_TkSide: TypeAlias = Literal['left', 'right', 'top', 'bottom']
_TkState: TypeAlias = Literal['normal', 'active', 'disabled']

def resetWidgetDict() -> None: ...
def resetVariableDict() -> None: ...

class AppShell(Pmw.MegaWidget, DirectObject):
    appversion: ClassVar[str]
    appname: ClassVar[str]
    copyright: ClassVar[str]
    contactname: ClassVar[str]
    contactphone: ClassVar[str]
    contactemail: ClassVar[str]
    frameWidth: ClassVar[int]
    frameHeight: ClassVar[int]
    padx: ClassVar[int]
    pady: ClassVar[int]
    usecommandarea: ClassVar[bool]
    usestatusarea: ClassVar[bool]
    balloonState: ClassVar[str]
    panelCount: ClassVar[int]
    parent: tkinter.Toplevel
    id: str
    widgetDict: dict[str, Any]
    variableDict: dict[str, Any]
    menuFrame: tkinter.Frame
    menuBar: Pmw.MenuBar
    dateArea: tkinter.Frame
    about: Pmw.AboutDialog
    toggleBalloonVar: tkinter.IntVar
    def __init__(self, parent: tkinter.Toplevel | None = None, **kw) -> None: ...
    def toggleBalloon(self) -> None: ...
    def showAbout(self) -> None: ...
    def quit(self) -> None: ...
    def appInit(self) -> None: ...
    def createInterface(self) -> None: ...
    def onDestroy(self, event) -> None: ...
    def createMenuBar(self) -> None: ...
    def interior(self) -> tkinter.Frame: ...
    def balloon(self) -> Pmw.Balloon: ...
    def buttonBox(self) -> Pmw.ButtonBox: ...
    def messageBar(self) -> Pmw.MessageBar: ...
    def buttonAdd(self, buttonName, helpMessage=None, statusMessage=None, **kw): ...
    def alignbuttons(self) -> None: ...
    def bind(self, child, balloonHelpMsg, statusHelpMsg=None) -> None: ...
    def updateProgress(self, newValue=0, newMax=0) -> None: ...
    def addWidget(self, category: str, text: str, widget) -> None: ...
    def getWidget(self, category: str, text: str) -> Any | None: ...
    def addVariable(self, category: str, text: str, variable) -> None: ...
    def getVariable(self, category: str, text: str) -> Any | None: ...
    def createWidget(
        self,
        parent,
        category: str,
        text: str,
        widgetClass: type[_WidgetT],
        help: str,
        command,
        side: _TkSide,
        fill: _TkFill,
        expand: int,
        kw: MutableMapping[str, Any],
    ) -> _WidgetT: ...
    def newCreateLabeledEntry(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        value: str = '',
        width: int = 12,
        relief: _TkRelief = 'sunken',
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
    ) -> tkinter.Entry: ...
    def newCreateButton(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> tkinter.Button: ...
    def newCreateCheckbutton(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        initialState: bool = ...,
        anchor: _TkAnchor = 'w',
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> tkinter.Checkbutton: ...
    def newCreateRadiobutton(
        self,
        parent,
        category: str,
        text: str,
        variable,
        value,
        command=None,
        help: str = '',
        anchor: _TkAnchor = 'w',
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> tkinter.Radiobutton: ...
    def newCreateFloater(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Floater: ...
    def newCreateDial(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Dial: ...
    def newCreateSider(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Slider: ...
    def newCreateEntryScale(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> EntryScale: ...
    def newCreateVector2Entry(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Vector2Entry: ...
    def newCreateVector3Entry(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Vector3Entry: ...
    def newCreateColorEntry(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> ColorEntry: ...
    def newCreateOptionMenu(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        items: list[str] = [],
        labelpos='w',
        label_anchor: _TkAnchor = 'w',
        label_width: int = 16,
        menu_tearoff: int = 1,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Pmw.OptionMenu: ...
    def newCreateComboBox(
        self,
        parent,
        category: str,
        text: str,
        help: str = '',
        command=None,
        items=[],
        state: _TkState = 'disabled',
        history: Unused = 0,
        labelpos='w',
        label_anchor: _TkAnchor = 'w',
        label_width: int = 16,
        entry_width: int = 16,
        side: _TkSide = 'left',
        fill: _TkFill = 'x',
        expand: int = 0,
        **kw: Any,
    ) -> Pmw.ComboBox: ...
    def transformRGB(self, rgb: tuple[int, int, int], max: float = 1.0) -> str: ...

class TestAppShell(AppShell):
    def createButtons(self) -> None: ...
    def createMain(self) -> None: ...
