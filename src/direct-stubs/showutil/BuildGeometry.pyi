from typing import SupportsFloat
from typing_extensions import Literal, SupportsIndex, TypeAlias

from panda3d.core import Geom, GeomNode, LVecBase4f, NodePath

_RealNumber: TypeAlias = SupportsFloat | SupportsIndex
_Unused: TypeAlias = object

GEO_ID: int

def circleX(angle: _RealNumber, radius: float, centerX: float, centerY: float) -> float: ...
def circleY(angle: _RealNumber, radius: float, centerX: float, centerY: float) -> float: ...
def getCirclePoints(
    segCount: int,
    centerX: float,
    centerY: float,
    radius: float,
    wideX: float = ...,
    wideY: float = ...,
) -> list[tuple[float, float, Literal[1]]]: ...
def addCircle(
    attachNode: GeomNode,
    vertexCount: int,
    radius: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    centerColor: LVecBase4f | tuple[float, float, float, float] | None = None,
    layer: _Unused = ...,
) -> Geom: ...
def addCircleGeom(
    rootNode: NodePath,
    vertexCount: int,
    radius: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    centerColor: LVecBase4f | tuple[float, float, float, float] | None = None,
    layer: _Unused = ...,
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addSquare(
    attachNode: GeomNode,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: _Unused = ...,
) -> Geom: ...
def addSquareGeom(
    rootNode: NodePath,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: _Unused = ...,
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addBox(
    attachNode: GeomNode,
    sizeX: float,
    sizeY: float,
    sizeZ: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    darken: bool = False,
) -> Geom: ...
def addBoxGeom(
    rootNode: NodePath,
    sizeX: float,
    sizeY: float,
    sizeZ: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    darken: bool = False,
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addArrow(
    attachNode: GeomNode,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: _Unused = ...,
) -> Geom: ...
def addArrowGeom(
    rootNode: NodePath,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: _Unused = ...,
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
