from typing import SupportsFloat
from typing_extensions import Literal, SupportsIndex, TypeAlias

from panda3d.core import Geom, GeomNode, LVecBase4f, NodePath

GEO_ID: int

_RealNumber: TypeAlias = SupportsFloat | SupportsIndex

def circleX(angle: _RealNumber, radius: float, centerX: float, centerY: float) -> float: ...
def circleY(angle: _RealNumber, radius: float, centerX: float, centerY: float) -> float: ...
def getCirclePoints(
    segCount: int,
    centerX: float,
    centerY: float,
    radius: float,
    wideX: float = 1,
    wideY: float = 1,
) -> list[tuple[float, float, Literal[1]]]: ...
def addCircle(
    attachNode: GeomNode,
    vertexCount: int,
    radius: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    centerColor: LVecBase4f | tuple[float, float, float, float] | None = None,
    layer: object = 0,
) -> Geom: ...
def addCircleGeom(
    rootNode: NodePath,
    vertexCount: int,
    radius: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    centerColor: LVecBase4f | tuple[float, float, float, float] | None = None,
    layer: object = 0,
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addSquare(
    attachNode: GeomNode,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: object = 0,
) -> Geom: ...
def addSquareGeom(
    rootNode: NodePath,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: object = 0,
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
    layer: object = 0,
) -> Geom: ...
def addArrowGeom(
    rootNode: NodePath,
    sizeX: float,
    sizeY: float,
    color: LVecBase4f | tuple[float, float, float, float] = ...,
    layer: object = 0,
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
