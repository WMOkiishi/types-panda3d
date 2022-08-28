from .ClientRepository import ClientRepository
from .DistributedCamera import Fixture
from .DistributedObjectAI import DistributedObjectAI

class DistributedCameraAI(DistributedObjectAI):
    parent: int
    fixtures: list[Fixture]
    def __init__(self, air: ClientRepository) -> None: ...
    def getCamParent(self) -> int: ...
    def getFixtures(self) -> list[Fixture]: ...
