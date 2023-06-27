__all__ = ['DistributedActor']

from typing import Literal

from direct.distributed.ClientRepository import ClientRepository
from direct.distributed.DistributedNode import DistributedNode

from .Actor import Actor

class DistributedActor(DistributedNode, Actor):
    DistributedActor_initialized: Literal[1]
    def __init__(self, cr: ClientRepository) -> None: ...
