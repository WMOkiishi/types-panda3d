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
        duration: float = 0.0,
        name: str | None = None,
        volume: float = 1.0,
        startTime: float = 0.0,
        node: NodePath | None = None,
        seamlessLoop: bool = True,
        listenerNode: NodePath | None = None,
        cutOff: float | None = None,
    ) -> None: ...
    def loop(self, startT: float = 0.0, endT: float = -1.0, playRate: float = 1.0, stagger: bool = False) -> None: ...
