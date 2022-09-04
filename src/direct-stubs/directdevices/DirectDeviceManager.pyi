from typing import ClassVar
from typing_extensions import Final, Self

from panda3d.core import AnalogNode, ButtonNode, ClientBase, DialNode, NodePath, TrackerNode
from panda3d.vrpn import VrpnClient
from ..showbase.DirectObject import DirectObject

ANALOG_MIN: Final[float]
ANALOG_MAX: Final[float]
ANALOG_DEADBAND: Final[float]
ANALOG_CENTER: Final[float]

class DirectDeviceManager(VrpnClient, DirectObject):
    server: str
    def __init__(self, server: str | None = None) -> None: ...
    def createButtons(self, device) -> DirectButtons: ...
    def createAnalogs(self, device) -> DirectAnalogs: ...
    def createTracker(self, device) -> DirectTracker: ...
    def createDials(self, device) -> DirectDials: ...
    def createTimecodeReader(self, device) -> DirectTimecodeReader: ...

class DirectButtons(ButtonNode, DirectObject):
    buttonCount: ClassVar[int]
    nodePath: NodePath[Self]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def __getitem__(self, index: int) -> bool: ...
    def __len__(self) -> int: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...
    def getNodePath(self) -> NodePath[Self]: ...

class DirectAnalogs(AnalogNode, DirectObject):
    analogCount: ClassVar[int]
    nodePath: NodePath[Self]
    analogDeadband: float
    analogMin: float
    analogCenter: float
    analogRange: float
    def __init__(self, vrpnCLient: ClientBase, device: str) -> None: ...
    def __getitem__(self, index: int) -> float: ...
    def __len__(self) -> int: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def normalizeWithoutCentering(self, val: float, minVal: float = -1, maxVal: float = 1) -> float: ...
    def normalize(self, rawValue: float, minVal: float = -1, maxVal: float = 1, sf: float = 1) -> float: ...
    def normalizeChannel(self, chan: int, minVal: float = -1, maxVal: float = 1, sf: float = 1) -> float: ...
    def getName(self) -> str: ...
    def getNodePath(self) -> NodePath[Self]: ...

class DirectTracker(TrackerNode, DirectObject):
    trackerCount: ClassVar[int]
    nodePath: NodePath[Self]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...
    def getNodePath(self) -> NodePath[Self]: ...

class DirectDials(DialNode, DirectObject):
    dialCount: ClassVar[int]
    nodePath: NodePath[Self]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def __getitem__(self, index: int) -> float: ...
    def __len__(self) -> int: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...
    def getNodePath(self) -> NodePath[Self]: ...

class DirectTimecodeReader(AnalogNode, DirectObject):
    timecodeReaderCount: ClassVar[int]
    frames: int
    seconds: int
    minutes: int
    hours: int
    ndoePath: NodePath[Self]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...
    def getNodePath(self) -> NodePath[Self]: ...
    def getTime(self) -> tuple[int, int, int, int, float]: ...
