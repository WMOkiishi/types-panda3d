__all__ = ['SfxPlayer']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import AudioSound, NodePath

_OldBool: TypeAlias = Literal[0, 1]

class SfxPlayer:
    UseInverseSquare: ClassVar[bool | _OldBool]
    cutoffVolume: float
    cutoffDistance: float
    distanceScale: float
    def __init__(self) -> None: ...
    def setCutoffDistance(self, d: float) -> None: ...
    def getCutoffDistance(self) -> float: ...
    def getLocalizedVolume(self, node: NodePath, listenerNode: NodePath | None = None, cutoff: float | None = None) -> float: ...
    def playSfx(
            self,
            sfx: AudioSound,
            looping: bool = False,
            interrupt: bool = True,
            volume: float | None = None,
            time: float = 0,
            node: NodePath | None = None,
            listenerNode: NodePath | None = None,
            cutoff: float | None = None,
    ) -> None: ...
    def setFinalVolume(
            self,
            sfx: AudioSound,
            node: NodePath | None,
            volume: float | None,
            listenerNode: NodePath | None,
            cutoff: float | None = None,
    ) -> None: ...
