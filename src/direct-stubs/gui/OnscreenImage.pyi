__all__ = ['OnscreenImage']

from _typeshed import Self
from typing import Any

from direct._typing import Unused, Vec3OrTuple, Vec4OrTuple
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, TransformState

class OnscreenImage(DirectObject, NodePath):
    def __init__(
        self,
        image: NodePath | str | None = ...,
        pos: Vec3OrTuple | None = ...,
        hpr: Vec3OrTuple | None = ...,
        scale: Vec3OrTuple | float | None = ...,
        color: Vec4OrTuple | None = ...,
        parent: NodePath | None = ...,
        sort: int = ...,
    ) -> None: ...
    def setImage(
        self, image: NodePath | str | None, parent: NodePath = ..., transform: TransformState | None = ..., sort: int = ...
    ) -> None: ...
    def getImage(self: Self) -> Self: ...
    def configure(self, option: Unused = ..., **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
    cget = __getitem__
    def destroy(self) -> None: ...
