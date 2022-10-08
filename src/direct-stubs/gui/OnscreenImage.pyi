__all__ = ['OnscreenImage']

from _typeshed import Self
from typing import Any, Union
from typing_extensions import TypeAlias

from direct._typing import Unused
from direct.showbase.DirectObject import DirectObject
from panda3d.core import LColor, LVecBase3f, NodePath, TransformState

_Color: TypeAlias = Union[LColor, tuple[float, float, float, float]]
_Point: TypeAlias = Union[LVecBase3f, tuple[float, float, float]]

class OnscreenImage(DirectObject, NodePath):
    def __init__(
        self,
        image: NodePath | str | None = ...,
        pos: _Point | None = ...,
        hpr: _Point | None = ...,
        scale: _Point | float | None = ...,
        color: _Color | None = ...,
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
