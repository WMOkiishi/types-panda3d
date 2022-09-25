from typing import ClassVar
from typing_extensions import Literal

from panda3d.core import ClockObject
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

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
        bits: int = 16,
        ticksPerSec: float = 100,
    ) -> float: ...
    def localToNetworkTime(self, localTime: float, bits: int = 16, ticksPerSec: float = 100) -> int: ...
    def getRealNetworkTime(self, bits: int = 16, ticksPerSec: float = 100) -> int: ...
    def getFrameNetworkTime(self, bits: int = 16, ticksPerSec: float = 100) -> int: ...
    def localElapsedTime(self, networkTime, bits: int = 16, ticksPerSec: float = 100) -> float: ...

globalClockDelta: ClockDelta
