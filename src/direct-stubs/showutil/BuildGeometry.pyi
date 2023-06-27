from typing import Literal, SupportsFloat, SupportsIndex
from typing_extensions import TypeAlias

from direct._typing import Unused
from panda3d.core import Geom, GeomNode, LColor, NodePath

_RealNumber: TypeAlias = SupportsFloat | SupportsIndex

GEO_ID: int

def circleX(angle: _RealNumber, radius: float, centerX: float, centerY: float) -> float: ...
def circleY(angle: _RealNumber, radius: float, centerX: float, centerY: float) -> float: ...
def getCirclePoints(
    segCount: int, centerX: float, centerY: float, radius: float, wideX: float = 1.0, wideY: float = 1.0
) -> list[tuple[float, float, Literal[1]]]: ...
def addCircle(
    attachNode: GeomNode,
    vertexCount: int,
    radius: float,
    color: LColor = ...,
    centerColor: LColor | None = None,
    layer: Unused = 0,
) -> Geom: ...
def addCircleGeom(
    rootNode: NodePath, vertexCount: int, radius: float, color: LColor = ..., centerColor: LColor | None = None, layer: Unused = 0
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addSquare(attachNode: GeomNode, sizeX: float, sizeY: float, color: LColor = ..., layer: Unused = 0) -> Geom: ...
def addSquareGeom(
    rootNode: NodePath, sizeX: float, sizeY: float, color: LColor = ..., layer: Unused = 0
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addBox(attachNode: GeomNode, sizeX: float, sizeY: float, sizeZ: float, color: LColor = ..., darken: bool = ...) -> Geom: ...
def addBoxGeom(
    rootNode: NodePath, sizeX: float, sizeY: float, sizeZ: float, color: LColor = ..., darken: bool = ...
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
def addArrow(attachNode: GeomNode, sizeX: float, sizeY: float, color: LColor = ..., layer: Unused = 0) -> Geom: ...
def addArrowGeom(
    rootNode: NodePath, sizeX: float, sizeY: float, color: LColor = ..., layer: Unused = 0
) -> tuple[NodePath[GeomNode], GeomNode, Geom]: ...
