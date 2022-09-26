__all__ = ['OnscreenGeom']

from typing import Any, TypeVar, Union

from panda3d.core import LVecBase3f, LVecBase4f, NodePath, TransformState
from typing_extensions import TypeAlias

from direct.showbase.DirectObject import DirectObject

_Self = TypeVar('_Self')
_Color: TypeAlias = Union[LVecBase4f, tuple[float, float, float, float]]
_Point: TypeAlias = Union[LVecBase3f, tuple[float, float, float]]
_Unused: TypeAlias = object

class OnscreenGeom(DirectObject, NodePath):
    def __init__(
        self,
        geom: NodePath | str | None = None,
        pos: _Point | None = None,
        hpr: _Point | None = None,
        scale: _Point | float | None = None,
        color: _Color | None = None,
        parent: NodePath | None = None,
        sort: int = ...,
    ) -> None: ...
    def setGeom(
        self,
        geom: NodePath | str | None,
        parent: NodePath = ...,
        transform: TransformState | None = None,
        sort: int = ...,
        color: _Color | None = None,
    ) -> None: ...
    def getGeom(self: _Self) -> _Self: ...
    def configure(self, option: _Unused = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
    cget = __getitem__
    def destroy(self) -> None: ...
