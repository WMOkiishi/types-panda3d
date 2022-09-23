from collections.abc import Iterable, Sequence
from typing import TypeAlias, overload

from panda3d.core import (
    GeomNode,
    LineSegs,
    LMatrix3f,
    LMatrix4f,
    LPoint3f,
    LQuaternionf,
    LVecBase3f,
    LVecBase4f,
    LVector3f,
    NodePath,
    UnalignedLVecBase4f,
)

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow

class LineNodePath(NodePath[GeomNode]):
    lineNode: GeomNode
    lineSegs: LineSegs
    def __init__(
        self,
        parent: NodePath | None = None,
        name: str | None = None,
        thickness: float = ...,
        colorVec: _Vec4f = ...,
    ) -> None: ...
    @overload
    def moveTo(self, __v: _Vec3f) -> None: ...
    @overload
    def moveTo(self, __x: float, __y: float, __z: float) -> None: ...
    @overload
    def drawTo(self, __v: _Vec3f) -> None: ...
    @overload
    def drawTo(self, __x: float, __y: float, __z: float) -> None: ...
    def create(self, frameAccurate: bool = False) -> None: ...
    def reset(self) -> None: ...
    def isEmpty(self) -> bool: ...  # type: ignore[override]
    def setThickness(self, thickness: float) -> None: ...
    @overload  # type: ignore[override]
    def setColor(self, __color: _Vec4f) -> None: ...
    @overload
    def setColor(self, __r: float, __g: float, __b: float, __a: float) -> None: ...
    @overload
    def setVertex(self, __n: int, __vert: _Vec3f) -> None: ...
    @overload
    def setVertex(self, __vertex: int, __x: float, __y: float, __z: float) -> None: ...
    @overload
    def setVertexColor(self, __vertex: int, __c: _Vec4f) -> None: ...
    @overload
    def setVertexColor(self, __vertex: int, __r: float, __g: float, __b: float, __a: float = ...) -> None: ...
    def getCurrentPosition(self) -> LPoint3f: ...
    def getNumVertices(self) -> int: ...
    def getVertex(self, index: int) -> LPoint3f: ...
    def getVertexColor(self) -> LVecBase4f: ...
    def drawArrow(self, sv: _Vec3f, ev: _Vec3f, arrowAngle: float, arrowLength: float) -> None: ...
    def drawArrow2d(self, sv: _Vec3f, ev: _Vec3f, arrowAngle: float, arrowLength: float) -> None: ...
    def drawLines(self, lineList: Iterable[Sequence[_Vec3f]]) -> None: ...

def planeIntersect(lineOrigin: LVecBase3f, lineDir: LVecBase3f, planeOrigin: LVecBase3f, normal: _Vec3f) -> LVecBase3f: ...
def getNearProjectionPoint(nodePath: NodePath) -> LPoint3f: ...
def getScreenXY(nodePath: NodePath) -> LVector3f: ...
def getCrankAngle(center: Sequence[float]) -> float: ...
def relHpr(nodePath: NodePath, base: NodePath, h: float, p: float, r: float) -> None: ...
def qSlerp(startQuat: _Vec4f, endQuat: LQuaternionf, t: float) -> LQuaternionf: ...
