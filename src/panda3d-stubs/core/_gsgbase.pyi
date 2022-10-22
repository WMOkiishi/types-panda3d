from panda3d.core._putil import TypedWritableReferenceCount

class GraphicsOutputBase(TypedWritableReferenceCount):
    """An abstract base class for GraphicsOutput, for all the usual reasons."""

    def set_sort(self, sort: int) -> None: ...
    setSort = set_sort

class GraphicsStateGuardianBase(TypedWritableReferenceCount):
    """This is a base class for the GraphicsStateGuardian class, which is itself a
    base class for the various GSG's for different platforms.  This class
    contains all the function prototypes to support the double-dispatch of GSG
    to geoms, transitions, etc.  It lives in a separate class in its own
    package so we can avoid circular build dependency problems.

    GraphicsStateGuardians are not actually writable to bam files, of course,
    but they may be passed as event parameters, so they inherit from
    TypedWritableReferenceCount instead of TypedReferenceCount for that
    convenience.
    """

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
    def get_default_gsg() -> GraphicsStateGuardianBase:
        """Returns a pointer to the "default" GSG.  This is typically the first GSG
        created in an application; in a single-window application, it will be the
        only GSG. This GSG is used to determine default optimization choices for
        loaded geometry.

        The return value may be NULL if a GSG has not been created.
        """
    @staticmethod
    def set_default_gsg(default_gsg: GraphicsStateGuardianBase) -> None:
        """Specifies a particular GSG to use as the "default" GSG.  See
        get_default_gsg().
        """
    @staticmethod
    def get_num_gsgs() -> int:
        """Returns the total number of GSG's in the universe."""
    @staticmethod
    def get_gsg(n: int) -> GraphicsStateGuardianBase:
        """Returns the nth GSG in the universe.  GSG's automatically add themselves
        and remove themselves from this list as they are created and destroyed.
        """
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
    getGsgs = get_gsgs
