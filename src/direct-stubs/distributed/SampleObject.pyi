from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .ClientRepository import ClientRepository
from .DistributedObject import DistributedObject

class SampleObject(DistributedObject):
    notify: ClassVar[Notifier]
    cr: ClientRepository
    def __init__(self, cr: ClientRepository) -> None: ...
    def setColor(self, red: int = 0, green: int = 0, blue: int = 0) -> None: ...
    def getColor(self) -> tuple[int, int, int]: ...
