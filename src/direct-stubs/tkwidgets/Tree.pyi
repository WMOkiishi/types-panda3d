__all__ = ['TreeItem', 'TreeNode']

import tkinter
from abc import ABCMeta, abstractmethod
from collections.abc import Mapping
from typing import Any, Final

ICONDIR: Final[str]

class TreeNode:
    canvas: tkinter.Canvas
    parent: TreeNode
    item: TreeItem
    state: str
    selected: bool
    children: dict
    kidKeys: list
    x: int | None
    y: int | None
    iconimages: dict[str, tkinter.PhotoImage]
    menuList: list
    menuVar: Any
    fSortChildren: bool
    fModeChildrenTag: bool
    childrenTag: Mapping[str, bool]
    setAsTarget: bool
    def __init__(self, canvas: tkinter.Canvas, parent, item, menuList: list = []) -> None: ...
    def setFSortChildren(self, fSortChildren: bool) -> None: ...
    def setChildrenTag(self, tag: Mapping[str, bool], fModeChildrenTag: bool) -> None: ...
    def destroy(self) -> None: ...
    def geticonimage(self, name: str) -> tkinter.PhotoImage: ...
    def select(self, event=None) -> None: ...
    def deselect(self, event=None) -> None: ...
    def deselectall(self) -> None: ...
    def deselecttree(self) -> None: ...
    def flip(self, event=None) -> str: ...
    def createPopupMenu(self) -> None: ...
    def popupMenu(self, event=None) -> str | None: ...
    def popupMenuCommand(self) -> None: ...
    def expand(self, event=None) -> None: ...
    def collapse(self, event=None) -> None: ...
    def view(self) -> None: ...
    def reveal(self) -> None: ...
    def lastvisiblechild(self): ...
    def updateAll(self, fMode: bool, depth: int = 0, fUseCachedChildren: bool = ...) -> None: ...
    def update(self, fUseCachedChildren: bool = ..., fExpandMode: bool = ...) -> None: ...
    def draw(self, x: int, y: int, fUseCachedChildren: bool = ...) -> int: ...
    def drawicon(self) -> None: ...
    def drawtext(self) -> None: ...
    def select_or_edit(self, event=None) -> None: ...
    def edit(self, event=None) -> None: ...
    def edit_finish(self, event=None) -> None: ...
    def edit_cancel(self, event=None) -> None: ...
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
