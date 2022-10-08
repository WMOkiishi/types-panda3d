__all__ = ['TestInterval']

from typing import ClassVar

from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import NodePath
from .Interval import Interval

class TestInterval(Interval):
    particleNum: ClassVar[int]
    def __init__(
        self,
        particleEffect: ParticleEffect,
        duration: float = ...,
        parent: NodePath | None = ...,
        renderParent: NodePath | None = ...,
        name: str | None = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
