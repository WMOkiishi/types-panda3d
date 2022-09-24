from typing_extensions import TypeAlias

from panda3d.core import LMatrix3f, LPoint3f, LVector3f, NodePath
from ..showbase.DirectObject import DirectObject
from .DirectGeometry import LineNodePath

_Vec3f: TypeAlias = LVector3f | LMatrix3f.Row | LMatrix3f.CRow

class DirectGrid(NodePath, DirectObject):
    gridBack: NodePath
    lines: NodePath
    minorLines: LineNodePath
    majorLines: LineNodePath
    centerLines: LineNodePath
    snapMarker: NodePath
    snapPos: LPoint3f
    fXyzSnap: bool
    fHprSnap: bool
    gridSize: int
    gridSpacing: int
    snapAngle: float
    fEnabled: bool
    def __init__(
        self,
        gridSize: int = ...,
        gridSpacing: int = ...,
        planeColor: tuple[float, float, float] | tuple[float, float, float, float] = ...,
        parent: NodePath | None = None,
    ) -> None: ...
    def enable(self, parent: NodePath | None = None) -> None: ...
    def disable(self) -> None: ...
    def toggleGrid(self, parent: NodePath | None = None) -> None: ...
    def isEnabled(self) -> bool: ...
    def updateGrid(self) -> None: ...
    def setXyzSnap(self, fSnap: bool) -> None: ...
    def getXyzSnap(self) -> bool: ...
    def setHprSnap(self, fSnap: bool) -> None: ...
    def getHprSnap(self) -> bool: ...
    def computeSnapPoint(self, point: _Vec3f) -> LPoint3f: ...
    def computeSnapAngle(self, angle: float) -> float: ...
    def setSnapAngle(self, angle: float) -> None: ...
    def getSnapAngle(self) -> float: ...
    def setGridSpacing(self, spacing: int) -> None: ...
    def getGridSpacing(self) -> int: ...
    def setGridSize(self, size: int) -> None: ...
    def getGridSize(self) -> int: ...