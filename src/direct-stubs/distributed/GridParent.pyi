from typing import ClassVar

from panda3d.core import NodePath

class GridParent:
    GridZone2CellOrigin: ClassVar[dict[tuple[NodePath, int], NodePath]]
    GridZone2count: ClassVar[dict[tuple[NodePath, int], int]]
    av: NodePath
    grid: NodePath | None
    ownCellOrigin: NodePath
    cellOrigin: NodePath
    zoneId: int
    @staticmethod
    def getCellOrigin(grid: NodePath, zoneId: int) -> NodePath: ...
    @staticmethod
    def releaseCellOrigin(grid: NodePath, zoneId: int) -> None: ...
    def __init__(self, av: NodePath) -> None: ...
    def delete(self) -> None: ...
    def setGridParent(self, grid: NodePath, zoneId: int, teleport: bool = False) -> None: ...
