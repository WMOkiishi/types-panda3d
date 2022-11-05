__all__ = ['ProjectileInterval']

from typing import Any, ClassVar

from panda3d._typing import Vec3Like
from panda3d.core import CollisionNode, LParabolaf, NodePath
from .Interval import Interval

class ProjectileInterval(Interval):
    projectileIntervalNum: ClassVar[int]
    gravity: ClassVar[float]
    node: NodePath
    collNode: CollisionNode | None
    implicitStartPos: bool
    trajectoryArgs: tuple[Any, ...]
    startPos: Vec3Like
    zAcc: float
    endPos: Vec3Like | None
    startVel: Vec3Like
    parabola: LParabolaf
    def __init__(
        self,
        node: NodePath,
        startPos: Vec3Like | None = ...,
        endPos: Vec3Like | None = ...,
        duration: float | None = ...,
        startVel: Vec3Like | None = ...,
        endZ: float | None = ...,
        wayPoint: Vec3Like | None = ...,
        timeToWayPoint: float | None = ...,
        gravityMult: float | None = ...,
        name: str | None = ...,
        collNode: CollisionNode | NodePath[CollisionNode] | None = ...,
    ) -> None: ...
    def testTrajectory(self) -> bool: ...
