__all__ = ['IntervalManager', 'ivalMgr']

from typing_extensions import TypeAlias

from direct.showbase.EventManager import EventManager
from panda3d.core import EventQueue
from panda3d.direct import CInterval, CIntervalManager
from .Interval import Interval

_Interval: TypeAlias = Interval | CInterval

class IntervalManager(CIntervalManager):
    eventQueue: EventQueue
    MyEventmanager: EventManager
    ivals: list[_Interval | None]
    def __init__(self, globalPtr: bool = False) -> None: ...
    def addInterval(self, interval: CInterval) -> None: ...
    def removeInterval(self, interval: _Interval) -> bool: ...
    def getInterval(self, name: str) -> _Interval | None: ...
    def getIntervalsMatching(self, pattern: str) -> list[_Interval]: ...
    def finishIntervalsMatching(self, pattern: str) -> int: ...
    def pauseIntervalsMatching(self, pattern: str) -> int: ...

ivalMgr: IntervalManager
