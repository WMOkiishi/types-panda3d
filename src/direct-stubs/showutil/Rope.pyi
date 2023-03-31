from collections.abc import Sequence
from typing_extensions import TypeAlias

from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import ConfigVariableBool, LPoint3f, NodePath, NurbsCurveEvaluator, RopeNode

_Vert: TypeAlias = Vec3Like | Vec4Like

class Rope(NodePath):
    showRope: bool | ConfigVariableBool
    ropeNode: RopeNode
    curve: NurbsCurveEvaluator
    order: int
    verts: Sequence[_Vert]
    knots: Sequence[float] | None
    def __init__(self, name: str = 'Rope') -> None: ...
    def setup(self, order: int, verts: Sequence[_Vert], knots: Sequence[float] | None = None) -> None: ...
    def recompute(self) -> None: ...
    def getPoints(self, len: int) -> list[LPoint3f]: ...
