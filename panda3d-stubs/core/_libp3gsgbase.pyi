from typing import Any, ClassVar

class GraphicsOutputBase(TypedWritableReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_sort(self, sort: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setSort = set_sort
    getClassType = get_class_type

class GraphicsStateGuardianBase(TypedWritableReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_incomplete_render(self) -> bool: ...
    def get_effective_incomplete_render(self) -> bool: ...
    def prefers_triangle_strips(self) -> bool: ...
    def get_max_vertices_per_array(self) -> int: ...
    def get_max_vertices_per_primitive(self) -> int: ...
    def get_max_texture_dimension(self) -> int: ...
    def get_supports_compressed_texture_format(self, compression_mode: int) -> bool: ...
    def get_supports_multisample(self) -> bool: ...
    def get_supported_geom_rendering(self) -> int: ...
    def get_supports_shadow_filter(self) -> bool: ...
    def get_supports_texture_srgb(self) -> bool: ...
    def get_supports_hlsl(self) -> bool: ...
    @staticmethod
    def get_default_gsg() -> GraphicsStateGuardianBase: ...
    @staticmethod
    def set_default_gsg(default_gsg: GraphicsStateGuardianBase) -> None: ...
    @staticmethod
    def get_num_gsgs() -> int: ...
    @staticmethod
    def get_gsg(n: int) -> GraphicsStateGuardianBase: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_gsgs(self) -> tuple[GraphicsStateGuardianBase, ...]: ...
    getIncompleteRender = get_incomplete_render
    getEffectiveIncompleteRender = get_effective_incomplete_render
    prefersTriangleStrips = prefers_triangle_strips
    getMaxVerticesPerArray = get_max_vertices_per_array
    getMaxVerticesPerPrimitive = get_max_vertices_per_primitive
    getMaxTextureDimension = get_max_texture_dimension
    getSupportsCompressedTextureFormat = get_supports_compressed_texture_format
    getSupportsMultisample = get_supports_multisample
    getSupportedGeomRendering = get_supported_geom_rendering
    getSupportsShadowFilter = get_supports_shadow_filter
    getSupportsTextureSrgb = get_supports_texture_srgb
    getSupportsHlsl = get_supports_hlsl
    getDefaultGsg = get_default_gsg
    setDefaultGsg = set_default_gsg
    getNumGsgs = get_num_gsgs
    getGsg = get_gsg
    getClassType = get_class_type
    getGsgs = get_gsgs
