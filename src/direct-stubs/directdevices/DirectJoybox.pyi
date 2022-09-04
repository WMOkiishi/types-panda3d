from collections.abc import Callable
from typing import ClassVar
from typing_extensions import Final, Literal

from panda3d.core import ButtonRegistry, NodePath
from ..gui.OnscreenText import OnscreenText
from ..showbase.DirectObject import DirectObject
from .DirectDeviceManager import DirectAnalogs, DirectButtons

L_STICK: Final[Literal[0]]
L_UPPER: Final[Literal[1]]
L_LOWER: Final[Literal[2]]
R_STICK: Final[Literal[3]]
R_UPPER: Final[Literal[4]]
R_LOWER: Final[Literal[5]]
NULL_AXIS: Final[Literal[-1]]
L_LEFT_RIGHT: Final[Literal[0]]
L_FWD_BACK: Final[Literal[1]]
L_TWIST: Final[Literal[2]]
L_SLIDE: Final[Literal[3]]
R_LEFT_RIGHT: Final[Literal[4]]
R_FWD_BACK: Final[Literal[5]]
R_TWIST: Final[Literal[6]]
R_SLIDE: Final[Literal[7]]
JOYBOX_MIN: Final[float]
JOYBOX_MAX: Final[float]
JOYBOX_RANGE: Final[float]
JOYBOX_TREAD_SEPERATION: Final[float]

class DirectJoybox(DirectObject):
    joyboxCount: ClassVar[int]
    xyzMultiplier: ClassVar[float]
    hprMultiplier: ClassVar[float]
    name: str
    devie: str
    analogs: DirectAnalogs
    buttons: DirectButtons
    aList: list[float]
    bList: list[bool]
    mapping: list[int]
    modifier: list[Literal[-1, 0, 1]]
    lastTime: float
    nodePath: NodePath
    headingNP: NodePath
    useHeadingNP: bool
    rotateInPlace: bool
    refCS = ...
    tempCS: NodePath
    readout: OnscreenText
    modeList: list[Callable[[], object]]
    updateFunc: Callable[[], object]
    modeName: str
    auxData: list
    breg: ButtonRegistry
    def __init__(self, device: str = 'CerealBox', nodePath: NodePath = ..., headingNP: NodePath = ...) -> None: ...
    def setHeadingNodePath(self, np: NodePath) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def addButtonEvents(self) -> None: ...
    def setNodePath(self, nodePath: NodePath) -> None: ...
    def getNodePath(self) -> NodePath: ...
    def setRefCS(self, refCS) -> None: ...
    def getEventName(self, index: object) -> str: ...
    def setXyzMultiplier(self, multiplier: float) -> None: ...
    def getXyzMultiplier(self) -> float: ...
    def setHprMultiplier(self, multiplier: float) -> None: ...
    def getHprMultiplier(self) -> float: ...
    def updateTask(self, state: object) -> Literal[1]: ...
    def updateVals(self) -> None: ...
    def updateValsUnrolled(self) -> None: ...
    def acceptSwitchModeEvent(self, button: int = 4) -> None: ...
    def ignoreSwitchModeEvent(self, button: int = 4) -> None: ...
    def switchMode(self) -> None: ...
    def showMode(self, modeText: str) -> None: ...
    def acceptUprightCameraEvent(self, button: int = 1) -> None: ...
    def ignoreUprightCameraEvent(self, button: int = 1) -> None: ...
    def setMode(self, func: Callable[[], object], name: str) -> None: ...
    def setUseHeadingNP(self, enabled: bool) -> None: ...
    def setRotateInPlace(self, enabled: bool) -> None: ...
    def joyboxFly(self) -> None: ...
    def joeMode(self) -> None: ...
    def fpsMode(self) -> None: ...
    def tankMode(self) -> None: ...
    def nullMode(self) -> None: ...
    def lucMode(self) -> None: ...
    def driveMode(self) -> None: ...
    def lookAtMode(self) -> None: ...
    def lookAroundMode(self) -> None: ...
    def demoMode(self) -> None: ...
    def hprXyzMode(self) -> None: ...
    def mopathMode(self) -> None: ...
    def walkthruMode(self) -> None: ...
    def spaceMode(self) -> None: ...
    def nullFly(self) -> None: ...
    def tankFly(self) -> None: ...
    def spaceFly(self) -> None: ...
    def planetMode(self, auxData: list= ...) -> None: ...
    def planetFly(self) -> None: ...
    def orbitMode(self) -> None: ...
    def orbitFly(self) -> None: ...
    def orbitNode(self, h: float, p: float, r: float) -> None: ...
    def normalizeChannel(self, chan: int, minVal: float = -1, maxVal: float = 1) -> float: ...
