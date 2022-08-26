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

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

class ThreeUpShow(ShowBase):
    def __init__(self) -> None: ...
    def makeCamera(
        self,
        win: GraphicsOutput,
        sort: int = 0,
        scene: NodePath | None = None,
        displayRegion: _Vec4f | tuple[float, float, float, float] = ...,
        stereo: bool | None = None,
        aspectRatio: float | None = None,
        clearDepth: bool = False,
        clearColor: _Vec4f | None = None,
        lens: Lens | None = None,
        camName: str = 'cam',
        mask=None,
        useCamera: NodePath[Camera] | None = None,
    ) -> NodePath[Camera]: ...
