from typing import ClassVar
from typing_extensions import Final, Literal, Protocol

from panda3d.core import ConfigVariableBool, LVector3f
from .CartesianGridBase import CartesianGridBase
from .DistributedNode import DistributedNode
from .GridParent import GridParent

class _HasGridParent(Protocol):
    gridParent: GridParent | None

GRID_Z_OFFSET: Final[float]

class DistributedCartesianGrid(DistributedNode, CartesianGridBase):
    VisualizeGrid: ClassVar[ConfigVariableBool]
    RuleSeparator: ClassVar[str]
    visAvatar = ...
    gridVisContext = ...
    cellWidth: float
    style = ...
    startingZone: int
    gridSize: int
    viewingRadius: int
    centerPos: LVector3f
    def isGridParent(self) -> Literal[True]: ...
    def setCellWidth(self, width: float) -> None: ...
    def setParentingRules(self, style, rule) -> None: ...
    def getCenterPos(self) -> LVector3f: ...
    def handleChildArrive(self, child: _HasGridParent, zoneId: int) -> None: ...
    def handleChildArriveZone(self, child: _HasGridParent, zoneId: int) -> None: ...
    def handleChildLeave(self, child: _HasGridParent, zoneId: int) -> None: ...
    def startProcessVisibility(self, avatar) -> None: ...
    def stopProcessVisibility(self, clearAll: bool = False, event: str | None = None) -> None: ...
    def processVisibility(self, task: object) -> Literal[1]: ...
    def addObjectToGrid(self, av) -> None: ...
    def removeObjectFromGrid(self, av) -> None: ...
    def handleAvatarZoneChange(self, av, zoneId: int) -> None: ...
    def turnOff(self) -> None: ...
    def turnOn(self, av=None) -> None: ...
    def setWorldContext(self, worldContext: object) -> None: ...
    def clearWorldContext(self, event: object = None) -> None: ...
