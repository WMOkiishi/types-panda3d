from collections.abc import Sequence
from typing_extensions import Literal, TypeAlias

from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import ConfigVariableBool, LPoint3f, NodePath, NurbsCurveEvaluator, RopeNode

_Order: TypeAlias = Literal[1, 2, 3, 4]
_Vert: TypeAlias = Vec3Like | Vec4Like

class Rope(NodePath):
    showRope: bool | ConfigVariableBool
    ropeNode: RopeNode
    curve: NurbsCurveEvaluator
    order: _Order
    verts: Sequence[_Vert]
    knots: Sequence[float] | None
    def __init__(self, name: str = ...) -> None: ...
    def setup(self, order: _Order, verts: Sequence[_Vert], knots: Sequence[float] | None = ...) -> None: ...
    def recompute(self) -> None: ...
    def getPoints(self, len: int) -> list[LPoint3f]: ...
