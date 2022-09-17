__all__ = ['OnscreenImage']

from typing import Any, Union
from typing_extensions import Self, TypeAlias

from panda3d.core import LVecBase3f, LVecBase4f, NodePath, TransformState
from ..showbase.DirectObject import DirectObject

_Color: TypeAlias = Union[LVecBase4f, tuple[float, float, float, float]]
_Point: TypeAlias = Union[LVecBase3f, tuple[float, float, float]]

class OnscreenImage(DirectObject, NodePath):
    def __init__(
        self,
        image = None,
        pos: _Point | None = None,
        hpr: _Point | None = None,
        scale: _Point | float | None = None,
        color: _Color | None = None,
        parent: NodePath | None = None,
        sort: int = 0,
    ) -> None: ...
    def setImage(
        self,
        image: NodePath | str | None,
        parent: NodePath = ...,
        transform: TransformState | None = None,
        sort: int = 0,
        color: _Color | None = None,
    ) -> None: ...
    def getImage(self) -> Self: ...
    def configure(self, option: object = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
    cget = __getitem__
    def destroy(self) -> None: ...
