from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .ClientRepository import ClientRepository
from .DistributedObject import DistributedObject

class DistributedObjectGlobal(DistributedObject):
    notify: ClassVar[Notifier]
    neverDisable: bool
    def __init__(self, cr: ClientRepository) -> None: ...
