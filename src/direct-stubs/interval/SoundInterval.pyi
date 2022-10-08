__all__ = ['SoundInterval']

from typing import ClassVar

from panda3d.core import AudioSound, NodePath
from .Interval import Interval

class SoundInterval(Interval):
    soundNum: ClassVar[int]
    sound: AudioSound
    soundDuration: float
    fLoop: bool
    volume: float
    startTime: float
    node: NodePath | None
    listenerNode: NodePath | None
    cutOff: float | None
    def __init__(
        self,
        sound: AudioSound,
        loop: bool = ...,
        duration: float = ...,
        name: str | None = ...,
        volume: float = ...,
        startTime: float = ...,
        node: NodePath | None = ...,
        seamlessLoop: bool = ...,
        listenerNode: NodePath | None = ...,
        cutOff: float | None = ...,
    ) -> None: ...
    def loop(self, startT: float = ..., endT: float = ..., playRate: float = ..., stagger: bool = ...) -> None: ...
