__all__ = ['ParticleInterval']

from typing import ClassVar

from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import NodePath
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
        worldRelative: bool = ...,
        renderParent: NodePath | None = ...,
        duration: float = ...,
        softStopT: float = ...,
        cleanup: bool = ...,
        name: str | None = ...,
    ) -> None: ...
