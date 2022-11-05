# undocumented
from panda3d.core import NodePath, PandaNode

from .ParticleEffect import ParticleEffect
from .Particles import Particles

class ParticleFloorTest(NodePath[PandaNode]):
    f: ParticleEffect
    p0: Particles
    def __init__(self) -> None: ...
    def start(self) -> None: ...
