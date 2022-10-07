__all__ = ['AppShell']

from collections.abc import MutableMapping
from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Radiobutton, Toplevel, Widget
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

_W = TypeVar('_W', bound=Widget)
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
    parent: Toplevel
    id: str
    widgetDict: dict[str, Any]
    variableDict: dict[str, Any]
    menuFrame: Frame
    menuBar: Pmw.MenuBar
    dateArea: Frame
    about: Pmw.AboutDialog
    toggleBalloonVar: IntVar
    def __init__(self, parent: Toplevel | None = None, **kw) -> None: ...
    def toggleBalloon(self) -> None: ...
    def showAbout(self) -> None: ...
    def quit(self) -> None: ...
    def appInit(self) -> None: ...
    def createInterface(self) -> None: ...
    def onDestroy(self, event) -> None: ...
    def createMenuBar(self) -> None: ...
    def interior(self) -> Frame: ...
    def balloon(self) -> Pmw.Balloon: ...
    def buttonBox(self) -> Pmw.ButtonBox: ...
    def messageBar(self) -> Pmw.MessageBar: ...
    def buttonAdd(self, buttonName, helpMessage=None, statusMessage=None, **kw): ...
    def alignbuttons(self) -> None: ...
    def bind(self, child, balloonHelpMsg, statusHelpMsg=None) -> None: ...
    def updateProgress(self, newValue=..., newMax=...) -> None: ...
    def addWidget(self, category: str, text: str, widget) -> None: ...
    def getWidget(self, category: str, text: str) -> Any | None: ...
    def addVariable(self, category: str, text: str, variable) -> None: ...
    def getVariable(self, category: str, text: str) -> Any | None: ...
    def createWidget(
        self,
        parent,
        category: str,
        text: str,
        widgetClass: type[_W],
        help: str,
        command,
        side: _TkSide,
        fill: _TkFill,
        expand: int,
        kw: MutableMapping[str, Any],
    ) -> _W: ...
    def newCreateLabeledEntry(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        value: str = ...,
        width: int = ...,
        relief: _TkRelief = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
    ) -> Entry: ...
    def newCreateButton(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Button: ...
    def newCreateCheckbutton(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        initialState: bool = False,
        anchor: _TkAnchor = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Checkbutton: ...
    def newCreateRadiobutton(
        self,
        parent,
        category: str,
        text: str,
        variable,
        value,
        command=None,
        help: str = ...,
        anchor: _TkAnchor = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Radiobutton: ...
    def newCreateFloater(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Floater: ...
    def newCreateDial(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Dial: ...
    def newCreateSider(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Slider: ...
    def newCreateEntryScale(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> EntryScale: ...
    def newCreateVector2Entry(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Vector2Entry: ...
    def newCreateVector3Entry(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Vector3Entry: ...
    def newCreateColorEntry(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> ColorEntry: ...
    def newCreateOptionMenu(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        items: list[str] = ...,
        labelpos=...,
        label_anchor: _TkAnchor = ...,
        label_width: int = ...,
        menu_tearoff: int = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Pmw.OptionMenu: ...
    def newCreateComboBox(
        self,
        parent,
        category: str,
        text: str,
        help: str = ...,
        command=None,
        items=...,
        state: _TkState = ...,
        history: Unused = ...,
        labelpos=...,
        label_anchor: _TkAnchor = ...,
        label_width: int = ...,
        entry_width: int = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw: Any,
    ) -> Pmw.ComboBox: ...
    def transformRGB(self, rgb: tuple[int, int, int], max: float = ...) -> str: ...

class TestAppShell(AppShell):
    def createButtons(self) -> None: ...
    def createMain(self) -> None: ...
