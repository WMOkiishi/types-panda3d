from direct.showbase.DirectObject import DirectObject
from panda3d._typing import Vec3Like
from panda3d.core import LPoint3f, NodePath

from .DirectGeometry import LineNodePath

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
    gridSize: float
    gridSpacing: float
    snapAngle: float
    fEnabled: bool
    def __init__(
        self,
        gridSize: float = ...,
        gridSpacing: float = ...,
        planeColor: tuple[float, float, float] | tuple[float, float, float, float] = ...,
        parent: NodePath | None = ...,
    ) -> None: ...
    def enable(self, parent: NodePath | None = ...) -> None: ...
    def disable(self) -> None: ...
    def toggleGrid(self, parent: NodePath | None = ...) -> None: ...
    def isEnabled(self) -> bool: ...
    def updateGrid(self) -> None: ...
    def setXyzSnap(self, fSnap: bool) -> None: ...
    def getXyzSnap(self) -> bool: ...
    def setHprSnap(self, fSnap: bool) -> None: ...
    def getHprSnap(self) -> bool: ...
    def computeSnapPoint(self, point: Vec3Like) -> LPoint3f: ...
    def computeSnapAngle(self, angle: float) -> float: ...
    def setSnapAngle(self, angle: float) -> None: ...
    def getSnapAngle(self) -> float: ...
    def setGridSpacing(self, spacing: int) -> None: ...
    def getGridSpacing(self) -> int: ...
    def setGridSize(self, size: int) -> None: ...
    def getGridSize(self) -> int: ...
