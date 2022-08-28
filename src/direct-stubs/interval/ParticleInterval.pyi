__all__ = ['ParticleInterval']

from typing import ClassVar

from panda3d.core import NodePath
from ..particles.ParticleEffect import ParticleEffect
from .Interval import Interval

class ParticleInterval(Interval):
    particleNum: ClassVar[int]
    particleEffect: ParticleEffect
    cleanup: bool
    softStopT: float
    def __init__(
        self,
        particleEffect: ParticleEffect,
        parent: NodePath,
        worldRelative: bool = True,
        renderParent: NodePath | None = None,
        duration: float = 0,
        softStopT: float = 0,
        cleanup: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privInitialize(self, t: float) -> None: ...
    def privInstant(self) -> None: ...
    def privStep(self, t: float) -> None: ...
    def privFinalize(self) -> None: ...
