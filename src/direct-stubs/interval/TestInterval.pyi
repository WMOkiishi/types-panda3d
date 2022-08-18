__all__ = ['TestInterval']

from typing import ClassVar

from panda3d.core import NodePath
from ..directnotify.Notifier import Notifier
from ..particles.ParticleEffect import ParticleEffect
from .Interval import Interval

class TestInterval(Interval):
    particleNum: ClassVar[int]
    notify: ClassVar[Notifier]
    def __init__(
        self,
        particleEffect: ParticleEffect,
        duration: float = 0,
        parent: NodePath | None = None,
        renderParent: NodePath | None = None,
        name: str | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...
    def start(self, startT: float = 0, endT: float = -1, playRate: float = 1) -> None: ...
    def privInitialize(self, t: float) -> None: ...
    def privStep(self, t: float) -> None: ...
    def privFinalize(self) -> None: ...
    def privInstant(self) -> None: ...
    def privInterrupt(self) -> None: ...
