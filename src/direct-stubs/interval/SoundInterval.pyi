__all__ = ['SoundInterval']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import AudioSound, NodePath
from ..directnotify.Notifier import Notifier
from .Interval import Interval

_OldBool: TypeAlias = Literal[0, 1]

class SoundInterval(Interval):
    soundNum: ClassVar[int]
    notify: ClassVar[Notifier]
    sound: AudioSound
    soundDuration: float
    fLoop: bool | _OldBool
    volume: float
    startTime: float
    node: NodePath | None
    listenerNode: NodePath | None
    cutOff: float | None
    def __init__(
        self,
        sound: AudioSound,
        loop: bool = False,
        duration: float = 0,
        name: str | None = None,
        volume: float = 1,
        startTime: float = 0,
        node: NodePath | None = None,
        seamlessLoop: bool = True,
        listenerNode: NodePath | None = None,
        cutOff: float | None = None,
    ) -> None: ...
    def privInitialize(self, t: float) -> None: ...
    def privInstant(self) -> None: ...
    def privStep(self, t: float) -> None: ...
    def finish(self) -> None: ...
    def privFinalize(self) -> None: ...
    def privReverseInitialize(self, t: float) -> None: ...
    def privReverseInstant(self) -> None: ...
    def privReverseFinalize(self) -> None: ...
    def privInterrupt(self) -> None: ...
    def loop(self, startT: float = 0, endT: float = -1, playRate: float = 1, stagger: bool = False) -> None: ...
