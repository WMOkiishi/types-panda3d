from typing_extensions import Literal

from panda3d.core import NodePath
from .ClientRepository import ClientRepository
from .DistributedObject import DistributedObject
from .GridParent import GridParent

class DistributedNode(DistributedObject, NodePath):
    DistributedNode_initialized: Literal[1]
    DistributedNode_deleted: Literal[1]
    gotStringParentToken: bool
    gridParent: GridParent | None
    def __init__(self, cr: ClientRepository) -> None: ...
    def setLocation(self, parentId: int, zoneId: int, teleport: bool = ...) -> None: ...  # type: ignore[override]
    def __cmp__(self, other: object) -> Literal[0, 1]: ...
    def b_setParent(self, parentToken) -> None: ...
    def d_setParent(self, parentToken) -> None: ...
    def setParentStr(self, parentTokenStr: str) -> None: ...
    def setParent(self, parentToken) -> None: ...
    def do_setParent(self, parentToken: int) -> None: ...
    def d_setX(self, x: float) -> None: ...
    def d_setY(self, y: float) -> None: ...
    def d_setZ(self, z: float) -> None: ...
    def d_setH(self, h: float) -> None: ...
    def d_setP(self, p: float) -> None: ...
    def d_setR(self, r: float) -> None: ...
    def setXY(self, x: float, y: float) -> None: ...
    def d_setXY(self, x: float, y: float) -> None: ...
    def setXZ(self, x: float, z: float) -> None: ...
    def d_setXZ(self, x: float, z: float) -> None: ...
    def d_setPos(self, x: float, y: float, z: float) -> None: ...
    def d_setHpr(self, h: float, p: float, r: float) -> None: ...
    def setXYH(self, x: float, y: float, h: float) -> None: ...
    def d_setXYH(self, x: float, y: float, h: float) -> None: ...
    def setXYZH(self, x: float, y: float, z: float, h: float) -> None: ...
    def d_setXYZH(self, x: float, y: float, z: float, h: float) -> None: ...
    def d_setPosHpr(self, x: float, y: float, z: float, h: float, p: float, r: float) -> None: ...
