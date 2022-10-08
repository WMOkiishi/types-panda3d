__all__ = ['TreeItem', 'TreeNode']

from abc import ABCMeta, abstractmethod
from tkinter import PhotoImage
from typing import Any
from typing_extensions import Final, Literal

ICONDIR: Final[str]

class TreeNode:
    canvas = ...
    parent = ...
    item = ...
    state: str
    selected: bool
    children: dict
    kidKeys: list
    x: int | None
    y: int | None
    iconimages: dict[str, PhotoImage]
    menuList: list
    menuVar: Any
    fSortChildren: bool
    fModeChildrenTag: bool
    childrenTag = ...
    setAsTarget: bool
    def __init__(self, canvas, parent, item, menuList: list = ...) -> None: ...
    def setFSortChildren(self, fSortChildren: bool) -> None: ...
    def setChildrenTag(self, tag, fModeChildrenTag: bool) -> None: ...
    def destroy(self) -> None: ...
    def geticonimage(self, name: str) -> PhotoImage: ...
    def select(self, event=...) -> None: ...
    def deselect(self, event=...) -> None: ...
    def deselectall(self) -> None: ...
    def deselecttree(self) -> None: ...
    def flip(self, event=...) -> Literal['break']: ...
    def createPopupMenu(self) -> None: ...
    def popupMenu(self, event=...) -> Literal['break'] | None: ...
    def popupMenuCommand(self) -> None: ...
    def expand(self, event=...) -> None: ...
    def collapse(self, event=...) -> None: ...
    def view(self) -> None: ...
    def reveal(self) -> None: ...
    def lastvisiblechild(self): ...
    def updateAll(self, fMode: bool, depth: int = ..., fUseCachedChildren: bool = ...) -> None: ...
    def update(self, fUseCachedChildren: bool = ..., fExpandMode: bool = ...) -> None: ...
    def draw(self, x, y, fUseCachedChildren: bool = ...) -> int: ...
    def drawicon(self) -> None: ...
    def drawtext(self) -> None: ...
    def select_or_edit(self, event=...) -> None: ...
    def edit(self, event=...) -> None: ...
    def edit_finish(self, event=...) -> None: ...
    def edit_cancel(self, event=...) -> None: ...
    def find(self, searchKey) -> TreeNode | None: ...

class TreeItem(metaclass=ABCMeta):
    @abstractmethod
    def GetText(self) -> str: ...
    def GetTextFg(self) -> str: ...
    def GetTextBg(self) -> str: ...
    def GetLabelText(self) -> None: ...
    def IsExpandable(self) -> bool: ...
    @abstractmethod
    def IsEditable(self) -> bool: ...
    def SetText(self, text: str) -> None: ...
    @abstractmethod
    def GetIconName(self) -> str: ...
    def GetSelectedIconName(self) -> str | None: ...
    @abstractmethod
    def GetSubList(self): ...
    def OnDoubleClick(self) -> None: ...
    def OnSelect(self) -> None: ...
