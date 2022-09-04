from typing_extensions import Final, Literal

from panda3d.core import NodePath, Texture
from ..task.Task import Task
from .FilterManager import FilterManager

CARTOON_BODY: Final[str]
SSAO_BODY: Final[str]

class FilterConfig:
    separation: int
    color: tuple[float, float, float, float]
    caster = ...
    numsamples: int
    density: float
    decay: float
    exposure: float
    source: str

class CommonFilters:
    manager: FilterManager
    configuration: dict[str, FilterConfig]
    task: Task | None
    textures: dict[str, Texture]
    finalQuad: NodePath | None
    bloom: list[NodePath]
    blur: list[NodePath]
    ssao: list[NodePath]
    def __init__(self, win, cam) -> None: ...
    def cleanup(self) -> None: ...
    def reconfigure(self, fullrebuild: bool, changed: str) -> bool | None: ...
    def update(self, task: Task | None = None) -> Literal[1] | None: ...
    def set_cartoon_ink(self, separation: int = 1, color: tuple[float, float, float, float] = ...) -> bool | None: ...
    def del_cartoon_ink(self) -> bool | None: ...
    def set_bloom(
        self,
        blend: tuple[float, float, float, float] = ...,
        mintrigger: float = 0.6,
        maxtrigger: float | None = 1,
        desat: float = 0.6,
        intensity: float = 1,
        size: str | int = 'medium',
    ) -> bool | None: ...
    def del_bloom(self) -> bool | None: ...
    def set_half_pixel_shift(self) -> bool | None: ...
    def del_half_pixel_shift(self) -> bool | None: ...
    def set_view_glow(self) -> bool | None: ...
    def del_view_glow(self) -> bool | None: ...
    def set_inverted(self) -> bool | None: ...
    def del_inverted(self) -> bool | None: ...
    def set_volumetric_lighting(
        self,
        caster,
        numsamples: int = 32,
        density: float = 5,
        decay: float = 0.1,
        exposure: float = 0.1,
        source: str = 'color',
    ) -> bool | None: ...
    def del_volumetric_lighting(self) -> bool | None: ...
    def set_blur_sharpen(self, amount: float = 0) -> bool | None: ...
    def del_blur_sharpen(self) -> bool | None: ...
    def set_ambient_occlusion(
        self,
        numsamples: int = 16,
        radius: float = 0.05,
        amount: float = 2,
        strength: float = 0.01,
        falloff: float = 0.000002,
    ) -> bool | None: ...
    def del_ambient_occlusion(self) -> bool | None: ...
    def set_gamma_adjust(self, gamma) -> bool | None: ...
    def del_gamma_adjust(self) -> bool | None: ...
    def set_srgb_encode(self, force: bool = False) -> bool | None: ...
    def del_srgb_encode(self) -> bool | None: ...
    def set_high_dynamic_range(self) -> bool | None: ...
    def del_high_dynamic_range(self) -> bool | None: ...
    def set_exposure_adjust(self, stops) -> bool | None: ...
    def del_exposure_adjust(self) -> bool | None: ...
    setCartoonInt = set_cartoon_ink
    delCartoonInt = del_cartoon_ink
    setBloom = set_bloom
    delBloom = del_bloom
    setHalfPixelShift = set_half_pixel_shift
    delHalfPixelShift = del_half_pixel_shift
    setViewGlow = set_view_glow
    delViewGlow = del_view_glow
    setInverted = set_inverted
    delInverted = del_inverted
    setVolumetricLighting = set_volumetric_lighting
    delVolumetricLighting = del_volumetric_lighting
    setBlurSharpen = set_blur_sharpen
    delBlurSharpen = del_blur_sharpen
    setAmbientOcclusion = set_ambient_occlusion
    delAmbientOcclusion = del_ambient_occlusion
    setGammaAdjust = set_gamma_adjust
    delGammaAdjust = del_gamma_adjust
    setSrgbEncode = set_srgb_encode
    delSrgbEncode = del_srgb_encode
    setHighDynamicRange = set_high_dynamic_range
    delHighDynamicRange = del_high_dynamic_range
    setExposureAdjust = set_exposure_adjust
    delExposureAdjust = del_exposure_adjust
