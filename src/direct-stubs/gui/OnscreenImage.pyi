__all__ = ['OnscreenImage']

from _typeshed import Self
from typing import Any, Union
from typing_extensions import TypeAlias

from direct._typing import Unused
from direct.showbase.DirectObject import DirectObject
from panda3d.core import LVecBase3f, LVecBase4f, NodePath, TransformState

_Color: TypeAlias = Union[LVecBase4f, tuple[float, float, float, float]]
_Point: TypeAlias = Union[LVecBase3f, tuple[float, float, float]]

class OnscreenImage(DirectObject, NodePath):
    def __init__(
        self,
        image: NodePath | str | None = None,
        pos: _Point | None = None,
        hpr: _Point | None = None,
        scale: _Point | float | None = None,
        color: _Color | None = None,
        parent: NodePath | None = None,
        sort: int = ...,
    ) -> None: ...
    def setImage(
        self,
        image: NodePath | str | None,
        parent: NodePath = ...,
        transform: TransformState | None = None,
        sort: int = ...,
    ) -> None: ...
    def getImage(self: Self) -> Self: ...
    def configure(self, option: Unused = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
    cget = __getitem__
    def destroy(self) -> None: ...
