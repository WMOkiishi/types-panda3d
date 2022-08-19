__all__ = ['OnscreenGeom']

from typing import Any
from typing_extensions import Self, TypeAlias

from panda3d.core import LVecBase3f, LVecBase4f, NodePath, TransformState
from ..showbase.DirectObject import DirectObject

_Color: TypeAlias = LVecBase4f | tuple[float, float, float, float]
_Point: TypeAlias = LVecBase3f | tuple[float, float, float]

class OnscreenGeom(DirectObject, NodePath):
    def __init__(
        self,
        geom: NodePath | str | None = None,
        pos: _Point | None = None,
        hpr: _Point | None = None,
        scale: _Point | float | None = None,
        color: _Color | None = None,
        parent: NodePath | None = None,
        sort: int = 0,
    ) -> None: ...
    def setGeom(
        self,
        geom: NodePath | str | None,
        parent: NodePath = ...,
        transform: TransformState | None = None,
        sort: int = 0,
        color: _Color | None = None,
    ) -> None: ...
    def getGeom(self) -> Self: ...
    def configure(self, option: object = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    cget = __getitem__
    def __getitem__(self, option: str) -> Any: ...
    def destroy(self) -> None: ...
