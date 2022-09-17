from collections.abc import Sequence
from typing import Union
from typing_extensions import Literal, TypeAlias

from panda3d.core import ConfigVariableBool, LPoint3f, LVecBase3f, LVecBase4f, NodePath, NurbsCurveEvaluator, RopeNode

_Order: TypeAlias = Literal[1, 2, 3, 4]
_Vert: TypeAlias = Union[LVecBase3f, LVecBase4f, tuple[float, float, float], tuple[float, float, float, float]]

class Rope(NodePath):
    showRope: bool | ConfigVariableBool
    ropeNode: RopeNode
    curve: NurbsCurveEvaluator
    order: _Order
    verts: Sequence[_Vert]
    knots: Sequence[float] | None
    def __init__(self, name: str = 'Rope') -> None: ...
    def setup(self, order: _Order, verts: Sequence[_Vert], knots: Sequence[float] | None = None) -> None: ...
    def recompute(self) -> None: ...
    def getPoints(self, len: int) -> list[LPoint3f]: ...
