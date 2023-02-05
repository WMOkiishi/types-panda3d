__all__ = ['OnscreenGeom']

from _typeshed import Self
from typing import Any

from direct._typing import Unused
from direct.showbase.DirectObject import DirectObject
from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import NodePath, TransformState

class OnscreenGeom(DirectObject, NodePath):
    def __init__(
        self,
        geom: NodePath | str | None = None,
        pos: Vec3Like | None = None,
        hpr: Vec3Like | None = None,
        scale: Vec3Like | float | None = None,
        color: Vec4Like | None = None,
        parent: NodePath | None = None,
        sort: int = 0,
    ) -> None: ...
    def setGeom(
        self,
        geom: NodePath | str | None,
        parent: NodePath = ...,
        transform: TransformState | None = None,
        sort: int = 0,
        color: Vec4Like | None = None,
    ) -> None: ...
    def getGeom(self: Self) -> Self: ...
    def configure(self, option: Unused = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
    cget = __getitem__
    def destroy(self) -> None: ...
