class GridChild:
    def __init__(self) -> None: ...
    def delete(self) -> None: ...
    def setGridCell(self, grid, zoneId: int) -> None: ...
    def updateGridInterest(self, grid, zoneId: int) -> None: ...
    def enableGridInterest(self, enabled: bool = True) -> None: ...
    def isOnAGrid(self) -> bool: ...
    def getGrid(self): ...
    def getGridZone(self): ...
    def getGridInterestIds(self) -> list: ...
    def getGridInterestZoneId(self, gridDoId: int): ...

class SmoothGridChild(GridChild):
    def transformTelemetry(self, x, y, z, h, p, r, e: int): ...