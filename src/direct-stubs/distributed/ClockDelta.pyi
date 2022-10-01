from typing import ClassVar
from typing_extensions import Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import ClockObject

NetworkTimeBits: Literal[16]
NetworkTimePrecision: float
NetworkTimeMask: Literal[65535]
NetworkTimeSignedMask: Literal[32767]
NetworkTimeTopBits: Literal[16]
MaxTimeDelta: float
ClockDriftPerHour: float
ClockDriftPerSecond: float
P2PResyncDelay: float

class ClockDelta(DirectObject):
    notify: ClassVar[Notifier]
    globalClock: ClockObject
    delta: float
    uncertainty: float | None
    lastResync: float
    def getDelta(self) -> float: ...
    def getUncertainty(self) -> float | None: ...
    def getLastResync(self) -> float: ...
    def clear(self) -> None: ...
    def resynchronize(self, localTime: float, networkTime: float, newUncertainty: float, trustNew: bool = True) -> None: ...
    def peerToPeerResync(self, avId: object, timestamp: int, serverTime: float, uncertainty: float) -> int: ...
    def newDelta(self, localTime: float, newDelta: float, newUncertainty: float, trustNew: bool = True) -> bool: ...
    def networkToLocalTime(
        self,
        networkTime: int,
        now: float | None = None,
        bits: int = ...,
        ticksPerSec: float = ...,
    ) -> float: ...
    def localToNetworkTime(self, localTime: float, bits: int = ..., ticksPerSec: float = ...) -> int: ...
    def getRealNetworkTime(self, bits: int = ..., ticksPerSec: float = ...) -> int: ...
    def getFrameNetworkTime(self, bits: int = ..., ticksPerSec: float = ...) -> int: ...
    def localElapsedTime(self, networkTime, bits: int = ..., ticksPerSec: float = ...) -> float: ...

globalClockDelta: ClockDelta
