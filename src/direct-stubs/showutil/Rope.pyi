from collections.abc import Sequence
from typing_extensions import Literal, TypeAlias

from direct._typing import Vec3OrTuple, Vec4OrTuple
from panda3d.core import ConfigVariableBool, LPoint3f, NodePath, NurbsCurveEvaluator, RopeNode

_Order: TypeAlias = Literal[1, 2, 3, 4]
_Vert: TypeAlias = Vec3OrTuple | Vec4OrTuple

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
