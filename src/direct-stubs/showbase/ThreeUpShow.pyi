__all__ = ['ThreeUpShow']

from direct._typing import Unused
from panda3d.core import Camera, GraphicsOutput, NodePath

from .ShowBase import ShowBase

class ThreeUpShow(ShowBase):
    def __init__(self) -> None: ...
    def makeCamera(  # type: ignore[override]
        self,
        win: GraphicsOutput,
        sort: Unused = 0,
        scene: Unused = None,
        displayRegion: Unused = (0, 1, 0, 1),
        stereo: Unused = None,
        aspectRatio: Unused = None,
        clearDepth: Unused = 0,
        clearColor: Unused = None,
        lens: Unused = None,
        camName: Unused = 'cam',
        mask: Unused = None,
        useCamera: Unused = None,
    ) -> NodePath[Camera]: ...
