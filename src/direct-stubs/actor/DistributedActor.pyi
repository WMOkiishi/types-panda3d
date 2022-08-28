__all__ = ['DistributedActor']

from typing_extensions import Literal

from ..distributed.DistributedNode import DistributedNode
from ..distributed.ClientRepository import ClientRepository
from .Actor import Actor

class DistributedActor(DistributedNode, Actor):
    DistributedActor_initialized: Literal[1]
    def __init__(self, cr: ClientRepository) -> None: ...
    def disable(self) -> None: ...
    def delete(self) -> None: ...
    def loop(
        self,
        animName: str,
        restart: bool = True,
        partName: str | None = None,
        fromFrame: float | None = None,
        toFrame: float | None = None,
    ) -> None: ...
