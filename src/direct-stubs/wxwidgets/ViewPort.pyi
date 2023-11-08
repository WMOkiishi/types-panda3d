__all__ = ['Viewport', 'ViewportManager']

from typing import Any, ClassVar
from typing_extensions import Final, Literal

import wx.siplib as sip  # type: ignore[import-untyped]
from direct.directtools.DirectGrid import DirectGrid
from direct.showbase.DirectObject import DirectObject
from panda3d.core import ButtonThrower, Camera, CollisionNode, Lens, LPoint3f, NodePath

from .WxPandaWindow import WxPandaWindow

HORIZONTAL: Final = 1
VERTICAL: Final = 2
CREATENEW: Final = 99
VPLEFT: Final = 10
VPFRONT: Final = 11
VPTOP: Final = 12
VPPERSPECTIVE: Final = 13

class ViewportManager:
    viewports: ClassVar[list[Viewport]]
    gsg: ClassVar[Any]
    @staticmethod
    def initializeAll(*args, **kwargs) -> None: ...
    @staticmethod
    def updateAll(*args, **kwargs) -> None: ...
    @staticmethod
    def layoutAll(*args, **kwargs) -> None: ...

class Viewport(WxPandaWindow, DirectObject, metaclass=sip.wrapper):
    CREATENEW: Final = 99
    VPLEFT: Final = 10
    VPFRONT: Final = 11
    VPTOP: Final = 12
    VPPERSPECTIVE: Final = 13
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
    def onSize(self, evt) -> None: ...
    def onRightDown(self, evt=None) -> None: ...
    def zoomOut(self) -> None: ...
    def zoomIn(self) -> None: ...
    @staticmethod
    def make(parent, vpType: Viewport | Literal[99, 10, 11, 12, 13] | None = None) -> Viewport: ...
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
