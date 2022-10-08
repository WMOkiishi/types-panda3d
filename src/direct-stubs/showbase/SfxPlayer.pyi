__all__ = ['SfxPlayer']

from typing import ClassVar

from panda3d.core import AudioSound, NodePath

class SfxPlayer:
    UseInverseSquare: ClassVar[bool]
    cutoffVolume: float
    cutoffDistance: float
    distanceScale: float
    def __init__(self) -> None: ...
    def setCutoffDistance(self, d: float) -> None: ...
    def getCutoffDistance(self) -> float: ...
    def getLocalizedVolume(self, node: NodePath, listenerNode: NodePath | None = ..., cutoff: float | None = ...) -> float: ...
    def playSfx(
        self,
        sfx: AudioSound,
        looping: bool = ...,
        interrupt: bool = ...,
        volume: float | None = ...,
        time: float = ...,
        node: NodePath | None = ...,
        listenerNode: NodePath | None = ...,
        cutoff: float | None = ...,
    ) -> None: ...
    def setFinalVolume(
        self,
        sfx: AudioSound,
        node: NodePath | None,
        volume: float | None,
        listenerNode: NodePath | None,
        cutoff: float | None = ...,
    ) -> None: ...
