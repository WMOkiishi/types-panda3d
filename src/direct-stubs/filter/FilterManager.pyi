__all__ = ['FilterManager']

from collections.abc import Mapping, Sequence
from typing import Any, ClassVar

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d._typing import Vec4Like
from panda3d.core import (
    Camera,
    DisplayRegion,
    DrawableRegion,
    FrameBufferProperties,
    GraphicsEngine,
    GraphicsOutput,
    LColor,
    NodePath,
    RenderState,
    Texture,
)

class FilterManager(DirectObject):
    notify: ClassVar[Notifier | None]
    win: GraphicsOutput
    forcex: int
    forcey: int
    engine: GraphicsEngine
    region: DisplayRegion
    wclears: list[tuple[bool, LColor]]
    rclears: list[tuple[bool, LColor]]
    camera: NodePath[Camera]
    caminit: RenderState
    camstate: RenderState
    buffers: list[GraphicsOutput]
    sizes: list[tuple[float, float, float]]
    nextsort: int
    basex: int
    basey: int
    def __init__(self, win: GraphicsOutput, cam: NodePath[Camera], forcex: int = ..., forcey: int = ...) -> None: ...
    def get_clears(self, region: DrawableRegion) -> list[tuple[bool, LColor]]: ...
    def set_clears(self, region: DrawableRegion, clears: Sequence[tuple[bool, Vec4Like]]) -> None: ...
    def set_stacked_clears(
        self, region: DrawableRegion, clears0: Sequence[tuple[bool, Vec4Like]], clears1: Sequence[tuple[bool, Vec4Like]]
    ) -> list[Any]: ...
    def is_fullscreen(self) -> bool: ...
    def get_scaled_size(self, mul: float, div: float, align: float) -> tuple[int, int]: ...
    def render_scene_into(
        self,
        depthtex: Texture | None = ...,
        colortex: Texture | None = ...,
        auxtex: Texture | None = ...,
        auxbits: int = ...,
        textures: Mapping[str, Texture] | None = ...,
        fbprops: FrameBufferProperties | None = ...,
        clamping: bool | None = ...,
    ) -> NodePath | None: ...
    def render_quad_into(
        self,
        name: str = ...,
        mul: float = ...,
        div: float = ...,
        align: float = ...,
        depthtex: Texture | None = ...,
        colortex: Texture | None = ...,
        auxtex0: Texture | None = ...,
        auxtex1: Texture | None = ...,
        fbprops: FrameBufferProperties | None = ...,
    ) -> NodePath | None: ...
    def create_buffer(
        self,
        name: str,
        xsize: int,
        ysize: int,
        texgroup: tuple[Texture, Texture, Texture, Texture],
        depthbits: bool = ...,
        fbprops: FrameBufferProperties | None = ...,
    ) -> GraphicsOutput: ...
    def window_event(self, win: Unused) -> None: ...
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
