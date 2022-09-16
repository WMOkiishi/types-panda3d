__all__ = ['Viewport', 'ViewportManager']

from typing import Any, ClassVar
from typing_extensions import Final, Literal

from panda3d.core import ButtonThrower, Camera, CollisionNode, LPoint3f, Lens, NodePath
from ..directtools.DirectGrid import DirectGrid
from ..showbase.DirectObject import DirectObject
from .WxPandaWindow import WxPandaWindow

HORIZONTAL: Final[Any]
VERTICAL: Final[Any]
CREATENEW: Final[Literal[99]]
VPLEFT: Final[Literal[10]]
VPFRONT: Final[Literal[11]]
VPTOP: Final[Literal[12]]
VPPERSPECTIVE: Final[Literal[13]]

class ViewportManager:
    viewports: list
    gsg: Any
    @staticmethod
    def initializeAll(*args, **kwargs) -> None: ...
    @staticmethod
    def updateAll(*args, **kwargs) -> None: ...
    @staticmethod
    def layoutAll(*args, **kwargs) -> None: ...

class Viewport(WxPandaWindow, DirectObject):
    CREATENEW: ClassVar[Literal[99]]
    VPLEFT: ClassVar[Literal[10]]
    VPFRONT: ClassVar[Literal[11]]
    VPTOP: ClassVar[Literal[12]]
    VPPERSPECTIVE: ClassVar[Literal[13]]
    name: str
    camera: NodePath | None
    lens: Lens | None
    camPos: LPoint3f | None
    camLookAt: LPoint3f | None
    initialized: bool
    grid: DirectGrid | None
    collPlane: CollisionNode | None
    cam2d: NodePath[Camera]
    cam: NodePath[Camera]
    camNode: Camera
    bt: NodePath[ButtonThrower]
    camLens: Lens
    def __init__(self, name: str, *args, **kwargs) -> None: ...
    def initialize(self) -> None: ...
    def Close(self) -> None: ...
    def onRightDown(self, evt=None) -> None: ...
    def zoomOut(self) -> None: ...
    def zoomIn(self) -> None: ...
    @staticmethod
    def make(parent, vpType: Viewport | Literal[99, 10, 11, 12, 13, None] = None) -> Viewport: ...
    @staticmethod
    def makeOrthographic(parent, name: str, campos: LPoint3f) -> Viewport: ...
    @staticmethod
    def makePerspective(parent) -> Viewport: ...
    @staticmethod
    def makeLeft(parent) -> Viewport: ...
    @staticmethod
    def makeFront(parent) -> Viewport: ...
    @staticmethod
    def makeTop(parent) -> Viewport: ...