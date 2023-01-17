from typing import ClassVar
from typing_extensions import Final

from direct.showbase.DirectObject import DirectObject
from panda3d.core import AnalogNode, ButtonNode, ClientBase, DialNode, NodePath, TrackerNode
from panda3d.vrpn import VrpnClient

ANALOG_MIN: Final = -0.95
ANALOG_MAX: Final = 0.95
ANALOG_DEADBAND: Final = 0.125
ANALOG_CENTER: Final = 0.0

class DirectDeviceManager(VrpnClient, DirectObject):
    server: str
    def __init__(self, server: str | None = ...) -> None: ...
    def createButtons(self, device: str) -> DirectButtons: ...
    def createAnalogs(self, device: str) -> DirectAnalogs: ...
    def createTracker(self, device: str) -> DirectTracker: ...
    def createDials(self, device: str) -> DirectDials: ...
    def createTimecodeReader(self, device: str) -> DirectTimecodeReader: ...

class DirectButtons(ButtonNode, DirectObject):
    buttonCount: ClassVar[int]
    nodePath: NodePath[DirectButtons]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def __getitem__(self, index: int) -> bool: ...
    def __len__(self) -> int: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...  # type: ignore[override]
    def getNodePath(self) -> NodePath[DirectButtons]: ...

class DirectAnalogs(AnalogNode, DirectObject):
    analogCount: ClassVar[int]
    nodePath: NodePath[DirectAnalogs]
    analogDeadband: float
    analogMin: float
    analogCenter: float
    analogRange: float
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def __getitem__(self, index: int) -> float: ...
    def __len__(self) -> int: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def normalizeWithoutCentering(self, val: float, minVal: float = ..., maxVal: float = ...) -> float: ...
    def normalize(self, rawValue: float, minVal: float = ..., maxVal: float = ..., sf: float = ...) -> float: ...
    def normalizeChannel(self, chan: int, minVal: float = ..., maxVal: float = ..., sf: float = ...) -> float: ...
    def getName(self) -> str: ...  # type: ignore[override]
    def getNodePath(self) -> NodePath[DirectAnalogs]: ...

class DirectTracker(TrackerNode, DirectObject):
    trackerCount: ClassVar[int]
    nodePath: NodePath[DirectTracker]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...  # type: ignore[override]
    def getNodePath(self) -> NodePath[DirectTracker]: ...

class DirectDials(DialNode, DirectObject):
    dialCount: ClassVar[int]
    nodePath: NodePath[DirectDials]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def __getitem__(self, index: int) -> float: ...
    def __len__(self) -> int: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...  # type: ignore[override]
    def getNodePath(self) -> NodePath[DirectDials]: ...

class DirectTimecodeReader(AnalogNode, DirectObject):
    timecodeReaderCount: ClassVar[int]
    frames: int
    seconds: int
    minutes: int
    hours: int
    nodePath: NodePath[DirectTimecodeReader]
    def __init__(self, vrpnClient: ClientBase, device: str) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def getName(self) -> str: ...  # type: ignore[override]
    def getNodePath(self) -> NodePath[DirectTimecodeReader]: ...
    def getTime(self) -> tuple[int, int, int, int, float]: ...
