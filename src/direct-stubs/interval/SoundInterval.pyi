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
        loop: bool = False,
        duration: float = ...,
        name: str | None = None,
        volume: float = ...,
        startTime: float = ...,
        node: NodePath | None = None,
        seamlessLoop: bool = True,
        listenerNode: NodePath | None = None,
        cutOff: float | None = None,
    ) -> None: ...
    def loop(self, startT: float = ..., endT: float = ..., playRate: float = ..., stagger: bool = False) -> None: ...
