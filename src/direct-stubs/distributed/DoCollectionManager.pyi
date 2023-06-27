import re
from collections.abc import Callable
from typing import Final, TypeVar, overload
from typing_extensions import TypeAlias, TypeGuard

from panda3d.core import DatagramIterator

from .DistributedObject import DistributedObject

_D = TypeVar('_D', bound=DistributedObject)
_DOCallback: TypeAlias = Callable[[DistributedObject], object]

BAD_DO_ID: Final = 0
BAD_ZONE_ID: Final = 0
BAD_CHANNEL_ID: Final = 0

class DoCollectionManager:
    doId2do: dict[int, DistributedObject]
    doId2ownerView: dict[int, DistributedObject]
    GameGlobalsId: int
    def __init__(self) -> None: ...
    def getDo(self, doId: int) -> DistributedObject | None: ...
    def getGameDoId(self) -> int: ...
    def callbackWithDo(self, doId: int, callback: _DOCallback | None) -> None: ...
    def getOwnerView(self, doId: int) -> DistributedObject | None: ...
    def callbackWithOwnerView(self, doId: int, callback: _DOCallback | None) -> None: ...
    def getDoTable(self, ownerView: bool) -> dict[int, DistributedObject]: ...
    def doFind(self, str: str) -> DistributedObject: ...
    def doFindAll(self, str: str) -> list[DistributedObject]: ...
    def doFindAllMatching(self, str: str | re.Pattern[str]) -> list[DistributedObject]: ...
    def doFindAllOfType(self, query: str) -> tuple[list[DistributedObject], int]: ...
    def doFindAllInstances(self, cls: type[_D]) -> list[_D]: ...
    def dosByDistance(self) -> list[DistributedObject]: ...
    def doByDistance(self) -> None: ...
    def webPrintObjectCount(self) -> str: ...
    def printObjectCount(self) -> None: ...
    @overload
    def getDoList(self, parentId: int, zoneId: int | None, classType: type[_D]) -> list[_D]: ...
    @overload
    def getDoList(self, parentId: int, zoneId: int | None = None, classType: None = None) -> list[DistributedObject]: ...
    def getDoIdList(self, parentId: int, zoneId: int | None = None, classType: type | None = None) -> list[int]: ...
    def hasOwnerViewDoId(self, doId: int) -> bool: ...
    def getOwnerViewDoList(self, classType: type[_D]) -> list[_D]: ...
    def getOwnerViewDoIdList(self, classType: type) -> list[int]: ...
    def countObjects(self, classType: type) -> int: ...
    def getAllOfType(self, type: type[_D]) -> list[_D]: ...
    def findAnyOfType(self, type: type[_D]) -> _D | None: ...
    def deleteDistributedObjects(self) -> None: ...
    def handleObjectLocation(self, di: DatagramIterator) -> None: ...
    def handleSetLocation(self, di: DatagramIterator) -> None: ...
    def storeObjectLocation(self, object: DistributedObject, parentId: int | None, zoneId: int | None) -> None: ...
    def deleteObjectLocation(self, object: DistributedObject, parentId: int, zoneId: int) -> None: ...
    def addDOToTables(self, do: DistributedObject, location: tuple[int, int] | None = None, ownerView: bool = False) -> None: ...
    def isValidLocationTuple(self, location: tuple[int, int] | None) -> TypeGuard[tuple[int, int]]: ...
    def removeDOFromTables(self, do: DistributedObject) -> None: ...
    def getObjectsInZone(self, parentId: int, zoneId: int) -> dict[int, DistributedObject]: ...
    @overload
    def getObjectsOfClassInZone(self, parentId: int, zoneId: int, objClass: type[_D]) -> dict[int, _D]: ...
    @overload
    def getObjectsOfClassInZone(self, parentId: int, zoneId: int, objClass: None) -> dict[int, DistributedObject]: ...
