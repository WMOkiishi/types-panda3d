from .DistributedCamera import Fixture
from .DistributedObjectAI import DistributedObjectAI

class DistributedCameraAI(DistributedObjectAI):
    parent: int
    fixtures: list[Fixture]
    def getCamParent(self) -> int: ...
    def getFixtures(self) -> list[Fixture]: ...
