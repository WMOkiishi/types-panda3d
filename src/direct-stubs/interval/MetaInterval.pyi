__all__ = ['MetaInterval', 'Parallel', 'ParallelEndTogether', 'Sequence', 'Track']

from _typeshed import Self
from collections.abc import Iterable
from typing import ClassVar
from typing_extensions import Final, Literal, SupportsIndex, TypeAlias, TypeGuard

from direct.directnotify.Notifier import Notifier
from panda3d.core import PStatCollector, ostream
from panda3d.direct import CInterval, CMetaInterval

from .Interval import Interval

_Interval: TypeAlias = Interval | CInterval
_RelativeStart: TypeAlias = Literal[0, 1, 2]

PREVIOUS_END: Final = 0
PREVIOUS_START: Final = 1
TRACK_START: Final = 2

class MetaInterval(CMetaInterval):
    notify: ClassVar[Notifier]
    SequenceNum: ClassVar[int]
    phonyDuration: int
    ivals: tuple[_Interval, ...] | list[_Interval]
    pstats: PStatCollector | None
    pythonIvals: list[_Interval]
    inPython: bool
    def __init__(
        self, *ivals: _Interval, name: str | None = ..., autoPause: bool = ..., autoFinish: bool = ..., duration: float = ...
    ) -> None: ...
    def append(self, ival: _Interval) -> None: ...
    def extend(self, ivals: MetaInterval | Iterable[_Interval]) -> None: ...
    def index(self, ival: _Interval) -> int: ...
    def count(self, ival: _Interval) -> int: ...
    def insert(self, index: SupportsIndex, ival: _Interval) -> None: ...
    def pop(self, index: SupportsIndex | None = None) -> _Interval: ...
    def remove(self, ival: _Interval) -> None: ...
    def reverse(self) -> None: ...
    def sort(self, cmpfunc: None = None) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: SupportsIndex) -> _Interval: ...
    def __setitem__(self, index: SupportsIndex, value: _Interval) -> None: ...
    def __delitem__(self, index: SupportsIndex) -> None: ...
    def __getslice__(self: Self, i: SupportsIndex, j: SupportsIndex) -> Self: ...
    def __setslice__(self, i: SupportsIndex, j: SupportsIndex, s: Iterable[_Interval]) -> None: ...
    def __delslice__(self, i: SupportsIndex, j: SupportsIndex) -> None: ...
    def __iadd__(self: Self, other: MetaInterval | Iterable[_Interval]) -> Self: ...
    def __add__(self: Self, other: MetaInterval | Iterable[_Interval]) -> Self: ...
    def add_sequence(
        self, list: Iterable[_Interval], name: str, relTime: float, relTo: _RelativeStart, duration: float
    ) -> None: ...
    def add_parallel(
        self, list: Iterable[_Interval], name: str, relTime: float, relTo: _RelativeStart, duration: float
    ) -> None: ...
    def add_parallel_end_together(
        self, list: Iterable[_Interval], name: str, relTime: float, relTo: _RelativeStart, duration: float
    ) -> None: ...
    def add_track(
        self,
        trackList: Iterable[tuple[_Interval, ...] | list[_Interval]],
        name: str,
        relTime: float,
        relTo: _RelativeStart,
        duration: float,
    ) -> None: ...
    def add_interval(self, ival: _Interval, relTime: float, relTo: _RelativeStart) -> None: ...
    def start(self, startT: float = 0.0, endT: float = -1.0, playRate: float = 1.0) -> None: ...
    def loop(self, startT: float = 0.0, endT: float = -1.0, playRate: float = 1.0) -> None: ...
    def resume(self, startT: float | None = None) -> None: ...
    def resume_until(self, endT: float) -> None: ...
    def validateComponent(self, component: object) -> TypeGuard[_Interval]: ...
    def validateComponents(self, components: Iterable[object]) -> TypeGuard[Iterable[_Interval]]: ...
    def applyIvals(self, meta: MetaInterval, relTime: float, relTo: _RelativeStart) -> None: ...
    def set_play_rate(self, playRate: float) -> None: ...
    def priv_post_event(self) -> None: ...
    @property
    def duration(self) -> float: ...
    def timeline(self, out: ostream | None = None) -> None: ...
    addSequence = add_sequence
    addParallel = add_parallel
    addParallelEndTogether = add_parallel_end_together
    addTrack = add_track
    addInterval = add_interval
    resumeUntil = resume_until  # type: ignore[assignment]
    setPlayRate = set_play_rate  # type: ignore[assignment]
    privPostEvent = priv_post_event

class Sequence(MetaInterval): ...
class Parallel(MetaInterval): ...
class ParallelEndTogether(MetaInterval): ...

class Track(MetaInterval):
    def validateComponent(self, tupleObj: object) -> TypeGuard[_Interval]: ...
