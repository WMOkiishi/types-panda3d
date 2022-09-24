__all__ = ['ThreeUpShow']

from typing_extensions import TypeAlias

from panda3d.core import (
    Camera,
    ConfigVariableColor,
    GraphicsOutput,
    Lens,
    LMatrix4f,
    LVecBase4f,
    NodePath,
    UnalignedLVecBase4f,
)
from .ShowBase import ShowBase

_Unused: TypeAlias = object
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

class ThreeUpShow(ShowBase):
    def __init__(self) -> None: ...
    def makeCamera(  # type: ignore[override]
        self,
        win: GraphicsOutput,
        sort: _Unused = ...,
        scene: _Unused = ...,
        displayRegion: _Unused = ...,
        stereo: _Unused = ...,
        aspectRatio: _Unused = ...,
        clearDepth: _Unused = ...,
        clearColor: _Unused = ...,
        lens: _Unused = ...,
        camName: _Unused = ...,
        mask: _Unused = ...,
        useCamera: _Unused = ...,
    ) -> NodePath[Camera]: ...
