from .ClientRepository import ClientRepository
from .DistributedObject import DistributedObject

class DistributedObjectGlobal(DistributedObject):
    def __init__(self, cr: ClientRepository) -> None: ...
