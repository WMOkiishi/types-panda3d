__all__ = ['ThreeUpShow']

from direct._typing import Unused
from panda3d.core import Camera, GraphicsOutput, NodePath

from .ShowBase import ShowBase

class ThreeUpShow(ShowBase):
    def __init__(self) -> None: ...
    def makeCamera(  # type: ignore[override]
        self,
        win: GraphicsOutput,
        sort: Unused = ...,
        scene: Unused = ...,
        displayRegion: Unused = ...,
        stereo: Unused = ...,
        aspectRatio: Unused = ...,
        clearDepth: Unused = ...,
        clearColor: Unused = ...,
        lens: Unused = ...,
        camName: Unused = ...,
        mask: Unused = ...,
        useCamera: Unused = ...,
    ) -> NodePath[Camera]: ...
