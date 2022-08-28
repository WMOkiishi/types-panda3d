__all__ = ['TestInterval']

from typing import ClassVar

from panda3d.core import NodePath
from ..particles.ParticleEffect import ParticleEffect
from .Interval import Interval

class TestInterval(Interval):
    particleNum: ClassVar[int]
    def __init__(
        self,
        particleEffect: ParticleEffect,
        duration: float = 0,
        parent: NodePath | None = None,
        renderParent: NodePath | None = None,
        name: str | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...
