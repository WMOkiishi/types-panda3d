__all__ = ['SceneGraphExplorer', 'SceneGraphExplorerItem', 'explore']

from collections.abc import Mapping
from typing import Final

import Pmw  # type: ignore[import-untyped]
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath

from .Tree import TreeItem

DEFAULT_MENU_ITEMS: Final[list[str]]

class SceneGraphExplorer(Pmw.MegaWidget, DirectObject):
    nodePath: NodePath
    def __init__(self, parent=None, nodePath: NodePath | None = None, isItemEditable: bool = True, **kw) -> None: ...
    def setChildrenTag(self, tag: Mapping[str, bool], fModeChildrenTag: bool) -> None: ...
    def setFSortChildren(self, fSortChildren: bool) -> None: ...
    def update(self, fUseCachedChildren: bool = ...) -> None: ...
    def mouse2Down(self, event) -> None: ...
    def mouse2Motion(self, event) -> None: ...
    def onDestroy(self, event) -> None: ...
    def updateSelection(self, searchKey) -> None: ...

class SceneGraphExplorerItem(TreeItem):
    nodePath: NodePath
    isItemEditable: bool
    def __init__(self, nodePath: NodePath, isItemEditable: bool = True) -> None: ...
    def GetText(self) -> str: ...
    def GetKey(self) -> int: ...
    def IsEditable(self) -> bool: ...
    def SetText(self, text: str) -> None: ...
    def GetIconName(self) -> str: ...
    def IsExpandable(self) -> bool: ...
    def GetSubList(self) -> list[SceneGraphExplorerItem]: ...
    def OnSelect(self) -> None: ...
    def MenuCommand(self, command: str) -> None: ...

def explore(nodePath: NodePath | None = None) -> SceneGraphExplorer: ...
