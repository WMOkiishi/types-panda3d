__all__ = ['FilterManager']

from collections.abc import Mapping, Sequence
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from panda3d._typing import Vec4f
from panda3d.core import (
    Camera,
    DisplayRegion,
    DrawableRegion,
    FrameBufferProperties,
    GraphicsEngine,
    GraphicsOutput,
    LVecBase4f,
    NodePath,
    RenderState,
    Texture,
)
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

_Unused: TypeAlias = object

class FilterManager(DirectObject):
    notify: ClassVar[Notifier | None]
    win: GraphicsOutput
    forcex: int
    forcey: int
    engine: GraphicsEngine
    region: DisplayRegion
    wclears: list[tuple[bool, LVecBase4f]]
    rclears: list[tuple[bool, LVecBase4f]]
    camera: NodePath[Camera]
    caminit: RenderState
    camstate: RenderState
    buffers: list
    sizes: list[tuple[float, float, float]]
    nextsort: int
    basex: int
    basey: int
    def __init__(self, win: GraphicsOutput, cam: NodePath[Camera], forcex: int = ..., forcey: int = ...) -> None: ...
    def get_clears(self, region: DrawableRegion) -> list[tuple[bool, LVecBase4f]]: ...
    def set_clears(self, region: DrawableRegion, clears: Sequence[tuple[bool, Vec4f]]) -> None: ...
    def set_stacked_clears(
        self,
        region: DrawableRegion,
        clears0: Sequence[tuple[bool, Vec4f]],
        clears1: Sequence[tuple[bool, Vec4f]],
    ) -> list[Any]: ...
    def is_fullscreen(self) -> bool: ...
    def get_scaled_size(self, mul: float, div: float, align: float) -> tuple[int, int]: ...
    def render_scene_into(
        self,
        depthtex: Texture | None = None,
        colortex: Texture | None = None,
        auxtex: Texture | None = None,
        auxbits: int = ...,
        textures: Mapping[str, Texture] | None = None,
        fbprops: FrameBufferProperties | None = None,
        clamping: bool | None = None,
    ) -> NodePath | None: ...
    def render_quad_into(
        self,
        name: str = ...,
        mul: float = ...,
        div: float = ...,
        align: float = ...,
        depthtex: Texture | None = None,
        colortex: Texture | None = None,
        auxtex0: Texture | None = None,
        auxtex1: Texture | None = None,
        fbprops: FrameBufferProperties | None = None,
    ) -> NodePath | None: ...
    def create_buffer(
        self,
        name: str,
        xsize: int,
        ysize: int,
        texgroup: tuple[Texture, Texture, Texture, Texture],
        depthbits: bool = True,
        fbprops: FrameBufferProperties | None = None,
    ) -> GraphicsOutput: ...
    def window_event(self, win: _Unused) -> None: ...
    def resize_buffers(self) -> None: ...
    def cleanup(self) -> None: ...
    getClears = get_clears
    setClears = set_clears
    setStackedClears = set_stacked_clears
    isFullscreen = is_fullscreen
    getScaledSize = get_scaled_size
    renderSceneInto = render_scene_into
    renderQuadInto = render_quad_into
    createBuffer = create_buffer
    windowEvent = window_event
    resizeBuffers = resize_buffers
