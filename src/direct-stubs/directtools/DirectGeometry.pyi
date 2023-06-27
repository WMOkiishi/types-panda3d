from collections.abc import Iterable, Sequence
from typing import overload

from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import GeomNode, LColor, LineSegs, LPoint3f, LQuaternionf, LVecBase2f, LVecBase3f, LVector3f, NodePath

class LineNodePath(NodePath[GeomNode]):
    lineNode: GeomNode
    lineSegs: LineSegs
    def __init__(
        self, parent: NodePath | None = None, name: str | None = None, thickness: float = 1.0, colorVec: Vec4Like = ...
    ) -> None: ...
    @overload
    def moveTo(self, v: Vec3Like, /) -> None: ...
    @overload
    def moveTo(self, x: float, y: float, z: float, /) -> None: ...
    @overload
    def drawTo(self, v: Vec3Like, /) -> None: ...
    @overload
    def drawTo(self, x: float, y: float, z: float, /) -> None: ...
    def create(self, frameAccurate: bool = ...) -> None: ...
    def reset(self) -> None: ...
    def isEmpty(self) -> bool: ...  # type: ignore[override]
    def setThickness(self, thickness: float) -> None: ...
    @overload  # type: ignore[override]
    def setColor(self, color: Vec4Like, /) -> None: ...
    @overload
    def setColor(self, r: float, g: float, b: float, a: float, /) -> None: ...
    @overload
    def setVertex(self, n: int, vert: Vec3Like, /) -> None: ...
    @overload
    def setVertex(self, vertex: int, x: float, y: float, z: float, /) -> None: ...
    @overload
    def setVertexColor(self, vertex: int, c: Vec4Like, /) -> None: ...
    @overload
    def setVertexColor(self, vertex: int, r: float, g: float, b: float, a: float = ..., /) -> None: ...
    def getCurrentPosition(self) -> LPoint3f: ...
    def getNumVertices(self) -> int: ...
    def getVertex(self, index: int) -> LPoint3f: ...
    def getVertexColor(self) -> LColor: ...
    def drawArrow(self, sv: Vec3Like, ev: Vec3Like, arrowAngle: float, arrowLength: float) -> None: ...
    def drawArrow2d(self, sv: Vec3Like, ev: Vec3Like, arrowAngle: float, arrowLength: float) -> None: ...
    def drawLines(self, lineList: Iterable[Sequence[Vec3Like]]) -> None: ...

def planeIntersect(lineOrigin: Vec3Like, lineDir: LVecBase3f, planeOrigin: LVecBase3f, normal: Vec3Like) -> LVecBase3f: ...
def getNearProjectionPoint(nodePath: NodePath) -> LPoint3f: ...
def getScreenXY(nodePath: NodePath) -> LVector3f: ...
def getCrankAngle(center: LVecBase2f) -> float: ...
def relHpr(nodePath: NodePath, base: NodePath, h: float, p: float, r: float) -> None: ...
def qSlerp(startQuat: Vec4Like, endQuat: LQuaternionf, t: float) -> LQuaternionf: ...
