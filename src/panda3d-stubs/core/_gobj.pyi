from _typeshed import StrOrBytesPath
from collections.abc import Iterator, Mapping, MutableMapping, MutableSequence, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias, final

from panda3d._typing import (
    DoubleMat4Like,
    DoubleVec2Like,
    DoubleVec3Like,
    DoubleVec4Like,
    IntVec2Like,
    IntVec3Like,
    IntVec4Like,
    Mat4Like,
    Vec2Like,
    Vec3Like,
    Vec4Like,
)
from panda3d.core._dtoolbase import TypedObject, TypeHandle
from panda3d.core._dtoolutil import Filename, istream, ostream
from panda3d.core._event import AsyncFuture, AsyncTask
from panda3d.core._express import (
    CPTA_int,
    CPTA_uchar,
    Namable,
    PointerToArray_unsigned_char,
    PTA_int,
    PTA_uchar,
    ReferenceCount,
    TypedReferenceCount,
)
from panda3d.core._gsgbase import GraphicsStateGuardianBase
from panda3d.core._linmath import (
    LColor,
    LMatrix3,
    LMatrix3d,
    LMatrix3f,
    LMatrix4,
    LMatrix4d,
    LMatrix4f,
    LPoint3,
    LVecBase2,
    LVecBase2d,
    LVecBase2f,
    LVecBase2i,
    LVecBase3,
    LVecBase3d,
    LVecBase3f,
    LVecBase3i,
    LVecBase4,
    LVecBase4d,
    LVecBase4f,
    LVecBase4i,
    LVector2,
    LVector3,
)
from panda3d.core._mathutil import BoundingVolume
from panda3d.core._pipeline import Mutex, Thread
from panda3d.core._pnmimage import PfmFile, PNMImage
from panda3d.core._putil import (
    AnimInterface,
    BamCacheRecord,
    BitArray,
    CopyOnWriteObject,
    LoaderOptions,
    ParamValueBase,
    SparseArray,
    TypedWritableReferenceCount,
    UpdateSeq,
)

_GeomEnums_AnimationType: TypeAlias = Literal[0, 1, 2]
_GeomEnums_NumericType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
_GeomEnums_Contents: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_VertexDataPage_RamClass: TypeAlias = Literal[0, 1, 2, 3]
_GeomEnums_UsageHint: TypeAlias = Literal[0, 1, 2, 3, 4]
_GeomEnums_PrimitiveType: TypeAlias = Literal[0, 1, 2, 3, 4]
_GeomEnums_ShadeModel: TypeAlias = Literal[0, 1, 2, 3]
_TextureStage_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_TextureStage_CombineMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_TextureStage_CombineSource: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_TextureStage_CombineOperand: TypeAlias = Literal[0, 1, 2, 3, 4]
_BoundingVolume_BoundsType: TypeAlias = Literal[0, 1, 2, 3, 4]
_SamplerState_WrapMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_SamplerState_FilterType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_Texture_TextureType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_Texture_Format: TypeAlias = int
_Texture_ComponentType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_Texture_CompressionMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
_Texture_QualityLevel: TypeAlias = Literal[0, 1, 2, 3]
_AutoTextureScale: TypeAlias = Literal[0, 1, 2, 3, 4]
_Shader_ShaderLanguage: TypeAlias = Literal[0, 1, 2, 3, 4]
_Shader_ShaderType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_Lens_StereoChannel: TypeAlias = Literal[0, 1, 2, 3]
_TextureStagePool_Mode: TypeAlias = Literal[0, 1, 2]

class AdaptiveLru(Namable):
    """A basic LRU-type algorithm, except that it is adaptive and attempts to
    avoid evicting pages that have been used more frequently (even if less
    recently) than other pages.

    The interface is designed to be identical to that for SimpleLru, so that it
    may be used as a drop-in replacement.
    """

    def __init__(self, name: str, max_size: int) -> None: ...
    def get_total_size(self) -> int:
        """Returns the total size of all objects currently active on the LRU."""
    def get_max_size(self) -> int:
        """Returns the max size of all objects that are allowed to be active on the
        LRU.
        """
    def set_max_size(self, max_size: int) -> None:
        """Changes the max size of all objects that are allowed to be active on the
        LRU.

        If the size is (size_t)-1, there is no limit.
        """
    def count_active_size(self) -> int:
        """Returns the total size of the pages that were enqueued since the last call
        to begin_epoch().
        """
    def consider_evict(self) -> None:
        """Evicts a sequence of objects if the queue is full."""
    def evict_to(self, target_size: int) -> None:
        """Evicts a sequence of objects until the queue fits within the indicated
        target size, regardless of its normal max size.
        """
    def begin_epoch(self) -> None:
        """Marks the end of the previous epoch and the beginning of the next one.
        This will evict any objects that are pending eviction, and also update any
        internal bookkeeping.
        """
    def validate(self) -> bool:
        """Checks that the LRU is internally self-consistent.  Returns true if
        successful, false if there is some problem.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    def set_weight(self, weight: float) -> None:
        """The following methods are specific to AdaptiveLru, and do not exist in
        the SimpleLru implementation.  In most cases, the defaults will be
        sufficient, so you do not need to mess with them.
        """
    def get_weight(self) -> float:
        """Returns the weight value used to compute the exponential moving average."""
    def set_max_updates_per_frame(self, max_updates_per_frame: int) -> None:
        """Specifies the maximum number of pages the AdaptiveLru will update each
        frame.  This is a performance optimization: keeping this number low limits
        the impact of the AdaptiveLru's adaptive algorithm.
        """
    def get_max_updates_per_frame(self) -> int:
        """Returns the maximum number of pages the AdaptiveLru will update each frame."""
    getTotalSize = get_total_size
    getMaxSize = get_max_size
    setMaxSize = set_max_size
    countActiveSize = count_active_size
    considerEvict = consider_evict
    evictTo = evict_to
    beginEpoch = begin_epoch
    setWeight = set_weight
    getWeight = get_weight
    setMaxUpdatesPerFrame = set_max_updates_per_frame
    getMaxUpdatesPerFrame = get_max_updates_per_frame

class AdaptiveLruPage:
    """One atomic piece that may be managed by a AdaptiveLru chain.  To use this
    class, inherit from it and override evict_lru().

    This class multiply inherits from two classes which in turn both inherit
    from LinkedListNode.  This is just a sneaky C++ trick to allow this class
    to inherit from LinkedListNode twice, so that pages can be stored on two
    different linked lists simultaneously.  The AdaptiveLru class depends on
    this; it maintains its pages in two different lists, one grouped by
    priority, and one in order by next partial update needs.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: AdaptiveLruPage) -> None: ...
    @overload
    def __init__(self, lru_size: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_lru(self) -> AdaptiveLru:
        """Returns the LRU that manages this page, or NULL if it is not currently
        managed by any LRU.
        """
    def enqueue_lru(self, lru: AdaptiveLru) -> None:
        """Adds the page to the LRU for the first time, or marks it recently-accessed
        if it has already been added.

        If lru is NULL, it means to remove this page from its LRU.
        """
    def dequeue_lru(self) -> None:
        """Removes the page from its AdaptiveLru."""
    def mark_used_lru(self, lru: AdaptiveLru = ...) -> None:
        """`(self)`:
        To be called when the page is used; this will move it to the tail of the
        AdaptiveLru queue it is already on.

        This method is const because it's not technically modifying the contents of
        the page itself.

        `(self, lru: AdaptiveLru)`:
        To be called when the page is used; this will move it to the tail of the
        specified AdaptiveLru queue.
        """
    def get_lru_size(self) -> int:
        """Returns the size of this page as reported to the LRU, presumably in bytes."""
    def set_lru_size(self, lru_size: int) -> None:
        """Specifies the size of this page, presumably in bytes, although any unit is
        possible.
        """
    def evict_lru(self) -> None:
        """Evicts the page from the LRU.  Called internally when the LRU determines
        that it is full.  May also be called externally when necessary to
        explicitly evict the page.

        It is legal for this method to either evict the page as requested, do
        nothing (in which case the eviction will be requested again at the next
        epoch), or requeue itself on the tail of the queue (in which case the
        eviction will be requested again much later).
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def get_num_frames(self) -> int:
        """Returns the number of frames since the page was first added to its LRU.
        Returns 0 if it does not have an LRU.
        """
    def get_num_inactive_frames(self) -> int:
        """Returns the number of frames since the page was last accessed on its LRU.
        Returns 0 if it does not have an LRU.
        """
    getLru = get_lru
    enqueueLru = enqueue_lru
    dequeueLru = dequeue_lru
    markUsedLru = mark_used_lru
    getLruSize = get_lru_size
    setLruSize = set_lru_size
    evictLru = evict_lru
    getNumFrames = get_num_frames
    getNumInactiveFrames = get_num_inactive_frames

class GeomEnums:
    """This class exists just to provide scoping for the various enumerated types
    used by Geom, GeomVertexData, GeomVertexArrayData, GeomPrimitive, and other
    related classes.
    """

    UH_client: Final = 0
    UHClient: Final = 0
    UH_stream: Final = 1
    UHStream: Final = 1
    UH_dynamic: Final = 2
    UHDynamic: Final = 2
    UH_static: Final = 3
    UHStatic: Final = 3
    UH_unspecified: Final = 4
    UHUnspecified: Final = 4
    GR_indexed_point: Final = 1
    GRIndexedPoint: Final = 1
    GR_indexed_other: Final = 65536
    GRIndexedOther: Final = 65536
    GR_indexed_bits: Final = 65537
    GRIndexedBits: Final = 65537
    GR_point: Final = 2
    GRPoint: Final = 2
    GR_point_uniform_size: Final = 4
    GRPointUniformSize: Final = 4
    GR_per_point_size: Final = 8
    GRPerPointSize: Final = 8
    GR_point_perspective: Final = 16
    GRPointPerspective: Final = 16
    GR_point_aspect_ratio: Final = 32
    GRPointAspectRatio: Final = 32
    GR_point_scale: Final = 64
    GRPointScale: Final = 64
    GR_point_rotate: Final = 128
    GRPointRotate: Final = 128
    GR_point_sprite: Final = 256
    GRPointSprite: Final = 256
    GR_point_sprite_tex_matrix: Final = 512
    GRPointSpriteTexMatrix: Final = 512
    GR_point_bits: Final = 1022
    GRPointBits: Final = 1022
    GR_triangle_strip: Final = 1024
    GRTriangleStrip: Final = 1024
    GR_triangle_fan: Final = 2048
    GRTriangleFan: Final = 2048
    GR_line_strip: Final = 4096
    GRLineStrip: Final = 4096
    GR_composite_bits: Final = 7168
    GRCompositeBits: Final = 7168
    GR_strip_cut_index: Final = 131072
    GRStripCutIndex: Final = 131072
    GR_flat_first_vertex: Final = 8192
    GRFlatFirstVertex: Final = 8192
    GR_flat_last_vertex: Final = 16384
    GRFlatLastVertex: Final = 16384
    GR_shade_model_bits: Final = 24576
    GRShadeModelBits: Final = 24576
    GR_render_mode_wireframe: Final = 262144
    GRRenderModeWireframe: Final = 262144
    GR_render_mode_point: Final = 524288
    GRRenderModePoint: Final = 524288
    GR_adjacency: Final = 1048576
    GRAdjacency: Final = 1048576
    SM_uniform: Final = 0
    SMUniform: Final = 0
    SM_smooth: Final = 1
    SMSmooth: Final = 1
    SM_flat_first_vertex: Final = 2
    SMFlatFirstVertex: Final = 2
    SM_flat_last_vertex: Final = 3
    SMFlatLastVertex: Final = 3
    PT_none: Final = 0
    PTNone: Final = 0
    PT_polygons: Final = 1
    PTPolygons: Final = 1
    PT_lines: Final = 2
    PTLines: Final = 2
    PT_points: Final = 3
    PTPoints: Final = 3
    PT_patches: Final = 4
    PTPatches: Final = 4
    NT_uint8: Final = 0
    NTUint8: Final = 0
    NT_uint16: Final = 1
    NTUint16: Final = 1
    NT_uint32: Final = 2
    NTUint32: Final = 2
    NT_packed_dcba: Final = 3
    NTPackedDcba: Final = 3
    NT_packed_dabc: Final = 4
    NTPackedDabc: Final = 4
    NT_float32: Final = 5
    NTFloat32: Final = 5
    NT_float64: Final = 6
    NTFloat64: Final = 6
    NT_stdfloat: Final = 7
    NTStdfloat: Final = 7
    NT_int8: Final = 8
    NTInt8: Final = 8
    NT_int16: Final = 9
    NTInt16: Final = 9
    NT_int32: Final = 10
    NTInt32: Final = 10
    NT_packed_ufloat: Final = 11
    NTPackedUfloat: Final = 11
    C_other: Final = 0
    COther: Final = 0
    C_point: Final = 1
    CPoint: Final = 1
    C_clip_point: Final = 2
    CClipPoint: Final = 2
    C_vector: Final = 3
    CVector: Final = 3
    C_texcoord: Final = 4
    CTexcoord: Final = 4
    C_color: Final = 5
    CColor: Final = 5
    C_index: Final = 6
    CIndex: Final = 6
    C_morph_delta: Final = 7
    CMorphDelta: Final = 7
    C_matrix: Final = 8
    CMatrix: Final = 8
    C_normal: Final = 9
    CNormal: Final = 9
    AT_none: Final = 0
    ATNone: Final = 0
    AT_panda: Final = 1
    ATPanda: Final = 1
    AT_hardware: Final = 2
    ATHardware: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: GeomEnums = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class GeomVertexAnimationSpec(GeomEnums):
    """This object describes how the vertex animation, if any, represented in a
    GeomVertexData is encoded.

    Vertex animation includes soft-skinned skeleton animation and morphs (blend
    shapes), and might be performed on the CPU by Panda, or passed down to the
    graphics backed to be performed on the hardware (depending on the
    hardware's advertised capabilities).

    Changing this setting doesn't by itself change the way the animation is
    actually performed; this just specifies how the vertices are set up to be
    animated.
    """

    @property
    def animation_type(self) -> _GeomEnums_AnimationType: ...
    @property
    def num_transforms(self) -> int: ...
    @property
    def indexed_transforms(self) -> bool: ...
    def __init__(self, other: GeomVertexAnimationSpec = ...) -> None: ...
    def assign(self, other: Self) -> Self: ...
    def get_animation_type(self) -> _GeomEnums_AnimationType:
        """Returns the type of animation represented by this spec."""
    def get_num_transforms(self) -> int:
        """This is only meaningful for animation_type AT_hardware.  It specifies the
        maximum number of transforms that might be simultaneously applied to any
        one vertex by the data in this format.
        """
    def get_indexed_transforms(self) -> bool:
        """This is only meaningful for animation_type AT_hardware.  If true, it
        indicates that the format uses indexed animation tables.  It is false if
        each vertex will reference the first _num_transforms table entries only.
        """
    def set_none(self) -> None:
        """Specifies that no vertex animation is represented by this spec."""
    def set_panda(self) -> None:
        """Specifies that vertex animation is to be performed by Panda.  This is the
        most general setting and can handle any kind of vertex animation
        represented.
        """
    def set_hardware(self, num_transforms: int, indexed_transforms: bool) -> None:
        """Specifies that vertex animation is to be performed by the graphics hardware
        (or at least by the graphics backend API, which is actually still free to
        animate the vertices on the CPU).

        This is only legal if the graphics hardware can support the specified
        limits on number of transforms and/or indexed transforms.  Also, no current
        graphics API's support morphing.
        """
    def output(self, out: ostream) -> None: ...
    getAnimationType = get_animation_type
    getNumTransforms = get_num_transforms
    getIndexedTransforms = get_indexed_transforms
    setNone = set_none
    setPanda = set_panda
    setHardware = set_hardware

@final
class InternalName(TypedWritableReferenceCount):
    """Encodes a string name in a hash table, mapping it to a pointer.  This is
    used to tokenify names so they may be used efficiently in low-level Panda
    structures, for instance to differentiate the multiple sets of texture
    coordinates that might be stored on a Geom.

    InternalNames are hierarchical, with the '.' used by convention as a
    separator character.  You can construct a single InternalName as a
    composition of one or more other names, or by giving it a source string
    directly.
    """

    @property
    def parent(self) -> InternalName: ...
    @property
    def name(self) -> str: ...
    @property
    def basename(self) -> str: ...
    @overload
    @staticmethod
    def make(str: str) -> InternalName:
        """`(str)`:
        These versions are exposed to Python, which have additional logic to map
        from Python interned strings.

        `(name: str, index: int)`:
        Make using a string and an integer.  Concatenates the two.
        """
    @overload
    @staticmethod
    def make(name: str, index: int) -> InternalName: ...
    def append(self, basename: str) -> InternalName:
        """Constructs a new InternalName based on this name, with the indicated string
        following it.  This is a cheaper way to construct a hierarchical name than
        InternalName::make(parent->get_name() + ".basename").
        """
    def get_parent(self) -> InternalName:
        """Return the parent of this InternalName.  All names have a parent, except
        the root name.
        """
    def get_name(self) -> str:
        """Returns the complete name represented by the InternalName and all of its
        parents.
        """
    def join(self, sep: str) -> str:
        """Like get_name, but uses a custom separator instead of "."."""
    def get_basename(self) -> str:
        """Return the name represented by just this particular InternalName object,
        ignoring its parents names.  This is everything after the rightmost dot.
        """
    def find_ancestor(self, basename: str) -> int:
        """Returns the index of the ancestor with the indicated basename, or -1 if no
        ancestor has that basename.  Returns 0 if this name has the basename.

        This index value may be passed to get_ancestor() or get_net_basename() to
        retrieve more information about the indicated name.
        """
    def get_ancestor(self, n: int) -> InternalName:
        """Returns the ancestor with the indicated index number.  0 is this name
        itself, 1 is the name's parent, 2 is the parent's parent, and so on.  If
        there are not enough ancestors, returns the root InternalName.
        """
    def get_top(self) -> InternalName:
        """Returns the oldest ancestor in the InternalName's chain, not counting the
        root.  This will be the first name in the string, e.g.  "texcoord.foo.bar"
        will return the InternalName "texcoord".
        """
    def get_net_basename(self, n: int) -> str:
        """Returns the basename of this name prefixed by the indicated number of
        ancestors.  0 is this name's basename, 1 is parent.basename, 2 is
        grandparent.parent.basename, and so on.
        """
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_root() -> InternalName:
        """Returns the standard root InternalName.  This is the root of all other
        InternalNames.  It has no name itself, and it is the only InternalName with
        no parent.
        """
    @staticmethod
    def get_error() -> InternalName:
        """Returns the standard InternalName "error"."""
    @staticmethod
    def get_vertex() -> InternalName:
        """Returns the standard InternalName "vertex".  This is the column header for
        the 3-d or 4-d vertex position information for each vertex.
        """
    @staticmethod
    def get_normal() -> InternalName:
        """Returns the standard InternalName "normal".  This is the column header for
        the 3-d lighting normal for each vertex.
        """
    @staticmethod
    def get_tangent() -> InternalName:
        """Returns the standard InternalName "tangent".  This is the column header for
        the tangent vector associated with each vertex, which is a unit vector
        usually perpendicular to the normal and in the direction of the U texture
        coordinate change.  It is used for deriving bump maps.
        """
    @staticmethod
    def get_tangent_name(name: str) -> InternalName:
        """Returns the InternalName "tangent.name", where name is the supplied string.
        This is the column header for the tangent associated with the named texture
        coordinate set.
        """
    @staticmethod
    def get_binormal() -> InternalName:
        """Returns the standard InternalName "binormal".  This is the column header
        for the tangent vector associated with each vertex, which is a unit vector
        usually perpendicular to both the normal and the tangent, and in the
        direction of the V texture coordinate change.  It is used for deriving bump
        maps.
        """
    @staticmethod
    def get_binormal_name(name: str) -> InternalName:
        """Returns the InternalName "binormal.name", where name is the supplied
        string.  This is the column header for the binormal associated with the
        named texture coordinate set.
        """
    @staticmethod
    def get_texcoord() -> InternalName:
        """Returns the standard InternalName "texcoord".  This is the column header
        for the default texture coordinate set for each vertex.  It is also used
        for identifying the default texture coordinate set in a TextureStage.
        """
    @staticmethod
    def get_texcoord_name(name: str) -> InternalName:
        """Returns the InternalName "texcoord.name", where name is the supplied
        string.  This is the column header for the named texture coordinate set for
        each vertex.  It is also used for identifying the named texture coordinate
        set in a TextureStage.
        """
    @staticmethod
    def get_color() -> InternalName:
        """Returns the standard InternalName "color".  This is the column header for
        the 4-component color value for each vertex.
        """
    @staticmethod
    def get_rotate() -> InternalName:
        """Returns the standard InternalName "rotate".  This is the column header for
        the floating-point rotate value, which represents a number of degrees
        counter-clockwise to rotate each point or point sprite.
        """
    @staticmethod
    def get_size() -> InternalName:
        """Returns the standard InternalName "size".  This is the column header for
        the floating-point size value, which overrides the thickness parameter of
        the RenderModeAttrib on a per-vertex (e.g.  per-point) basis.
        """
    @staticmethod
    def get_aspect_ratio() -> InternalName:
        """Returns the standard InternalName "aspect_ratio". This is the column header
        for the floating-point aspect ratio value, which is used to define non-
        square points.  This number is the ratio x / y, where y is the point size
        (above).
        """
    @staticmethod
    def get_transform_blend() -> InternalName:
        """Returns the standard InternalName "transform_blend". This is the column
        header for the integer transform_blend index, which is used to define
        vertex animation on the CPU by indexing to a particular vertex weighting
        from the TransformBlendTable.
        """
    @staticmethod
    def get_transform_weight() -> InternalName:
        """Returns the standard InternalName "transform_weight". This is the column
        header for the n-component transform_weight value, which is used in
        conjuntion with "transform_index" to define vertex animation on the
        graphics card.  The transform_weight value specifies the weight of the nth
        transform.  By convention, there are 1 fewer weight values than transforms,
        since the weights are assumed to sum to 1 (and the last value is therefore
        implicit).
        """
    @staticmethod
    def get_transform_index() -> InternalName:
        """Returns the standard InternalName "transform_index". This is the column
        header for the n-component transform_index value, which is used in
        conjuntion with "transform_weight" to define vertex animation on the
        graphics card.  The transform_index value specifies the nth transform, by
        lookup in the TransformTable.  The transform_index column may be omitted,
        in which case the nth transform is the nth entry in the table.
        """
    @staticmethod
    def get_morph(column: InternalName | str, slider: str) -> InternalName:
        """Returns an InternalName derived from the given base column name and the
        given slider name, which is the column header for the offset vector that
        should be applied to the base column name when the named morph slider is
        engaged.

        Each morph slider requires a set of n morph columns, one for each base
        column it applies to.
        """
    @staticmethod
    def get_index() -> InternalName:
        """Returns the standard InternalName "index".  This is the column header for
        the integer vertex index.  It is not used in the vertex data itself, but is
        used in the GeomPrimitive structure to index into the vertex data.
        """
    @staticmethod
    def get_world() -> InternalName:
        """Returns the standard InternalName "world".  This is used as a keyword in
        the shader subsystem.
        """
    @staticmethod
    def get_camera() -> InternalName:
        """Returns the standard InternalName "camera".  This is used as a keyword in
        the shader subsystem.
        """
    @staticmethod
    def get_model() -> InternalName:
        """Returns the standard InternalName "model".  This is used as a keyword in
        the shader subsystem.
        """
    @staticmethod
    def get_view() -> InternalName:
        """Returns the standard InternalName "view".  This is used as a keyword in the
        shader subsystem.
        """
    getParent = get_parent
    getName = get_name
    getBasename = get_basename
    findAncestor = find_ancestor
    getAncestor = get_ancestor
    getTop = get_top
    getNetBasename = get_net_basename
    getRoot = get_root
    getError = get_error
    getVertex = get_vertex
    getNormal = get_normal
    getTangent = get_tangent
    getTangentName = get_tangent_name
    getBinormal = get_binormal
    getBinormalName = get_binormal_name
    getTexcoord = get_texcoord
    getTexcoordName = get_texcoord_name
    getColor = get_color
    getRotate = get_rotate
    getSize = get_size
    getAspectRatio = get_aspect_ratio
    getTransformBlend = get_transform_blend
    getTransformWeight = get_transform_weight
    getTransformIndex = get_transform_index
    getMorph = get_morph
    getIndex = get_index
    getWorld = get_world
    getCamera = get_camera
    getModel = get_model
    getView = get_view

class GeomVertexColumn(GeomEnums):
    """This defines how a single column is interleaved within a vertex array
    stored within a Geom.  The GeomVertexArrayFormat class maintains a list of
    these to completely define a particular array structure.
    """

    @overload
    def __init__(self, copy: GeomVertexColumn) -> None: ...
    @overload
    def __init__(
        self,
        name: InternalName | str,
        num_components: int,
        numeric_type: _GeomEnums_NumericType,
        contents: _GeomEnums_Contents,
        start: int,
        column_alignment: int = ...,
        num_elements: int = ...,
        element_stride: int = ...,
    ) -> None: ...
    def assign(self, copy: Self) -> Self: ...
    def get_name(self) -> InternalName:
        """Returns the name of this particular data field, e.g.  "vertex" or "normal".
        The name may be a user-defined string, or it may be one of the standard
        system-defined field types.  Only the system-defined field types are used
        for the actual rendering.
        """
    def get_num_components(self) -> int:
        """Returns the number of components of the column: the number of instances of
        the NumericType in each element.  This is usually, but not always, the same
        thing as get_num_values().
        """
    def get_num_values(self) -> int:
        """Returns the number of numeric values of the column: the number of distinct
        numeric values that go into each element.  This is usually, but not always,
        the same thing as get_num_components(); the difference is in the case of a
        composite numeric type like NT_packed_dcba, which has four numeric values
        per component.
        """
    def get_num_elements(self) -> int:
        """Returns the number of times this column is repeated.  This is usually 1,
        except for matrices.
        """
    def get_numeric_type(self) -> _GeomEnums_NumericType:
        """Returns the token representing the numeric type of the data storage."""
    def get_contents(self) -> _GeomEnums_Contents:
        """Returns the token representing the semantic meaning of the stored value."""
    def get_start(self) -> int:
        """Returns the byte within the array record at which this column starts.  This
        can be set to non-zero to implement interleaved arrays.
        """
    def get_column_alignment(self) -> int:
        """Returns the alignment requirements for this column.  If this is greater
        than 1, it restricts the column to appear only on memory addresses that are
        integer multiples of this value; this has implications for this column's
        start value, as well as the stride of the resulting array.
        """
    def get_element_stride(self) -> int:
        """This value is only relevant for matrix types.  Returns the number of bytes
        to add to access the next row of the matrix.
        """
    def get_component_bytes(self) -> int:
        """Returns the number of bytes used by each component (that is, by one element
        of the numeric type).
        """
    def get_total_bytes(self) -> int:
        """Returns the number of bytes used by each element of the column:
        component_bytes * num_components.
        """
    def has_homogeneous_coord(self) -> bool:
        """Returns true if this Contents type is one that includes a homogeneous
        coordinate in the fourth component, or false otherwise.  If this is true,
        correct operation on the vertex data may require scaling by the homogeneous
        coordinate from time to time (but in general this is handled automatically
        if you use the 3-component or smaller forms of get_data() and set_data()).
        """
    def overlaps_with(self, start_byte: int, num_bytes: int) -> bool:
        """Returns true if this column overlaps with any of the bytes in the indicated
        range, false if it does not.
        """
    def is_bytewise_equivalent(self, other: GeomVertexColumn) -> bool:
        """Returns true if the data store of this column is exactly the same as that
        of the other, irrespective of name or start position within the record.
        """
    def set_name(self, name: InternalName | str) -> None:
        """Replaces the name of an existing column.  This is only legal on an
        unregistered format (i.e.  when constructing the format initially).
        """
    def set_num_components(self, num_components: int) -> None:
        """Changes the number of components of an existing column.  This is only legal
        on an unregistered format (i.e.  when constructing the format initially).
        """
    def set_numeric_type(self, numeric_type: _GeomEnums_NumericType) -> None:
        """Changes the numeric type an existing column.  This is only legal on an
        unregistered format (i.e.  when constructing the format initially).
        """
    def set_contents(self, contents: _GeomEnums_Contents) -> None:
        """Changes the semantic meaning of an existing column.  This is only legal on
        an unregistered format (i.e.  when constructing the format initially).
        """
    def set_start(self, start: int) -> None:
        """Changes the start byte of an existing column.  This is only legal on an
        unregistered format (i.e.  when constructing the format initially).
        """
    def set_column_alignment(self, column_alignment: int) -> None:
        """Changes the column alignment of an existing column.  This is only legal on
        an unregistered format (i.e.  when constructing the format initially).
        """
    def output(self, out: ostream) -> None: ...
    getName = get_name
    getNumComponents = get_num_components
    getNumValues = get_num_values
    getNumElements = get_num_elements
    getNumericType = get_numeric_type
    getContents = get_contents
    getStart = get_start
    getColumnAlignment = get_column_alignment
    getElementStride = get_element_stride
    getComponentBytes = get_component_bytes
    getTotalBytes = get_total_bytes
    hasHomogeneousCoord = has_homogeneous_coord
    overlapsWith = overlaps_with
    isBytewiseEquivalent = is_bytewise_equivalent
    setName = set_name
    setNumComponents = set_num_components
    setNumericType = set_numeric_type
    setContents = set_contents
    setStart = set_start
    setColumnAlignment = set_column_alignment

@final
class GeomVertexArrayFormat(TypedWritableReferenceCount, GeomEnums):
    """This describes the structure of a single array within a Geom data.  See
    GeomVertexFormat for the parent class which collects together all of the
    individual GeomVertexArrayFormat objects.

    A particular array may include any number of standard or user-defined
    columns.  All columns consist of a sequence of one or more numeric values,
    packed in any of a variety of formats; the semantic meaning of each column
    is defined in general with its contents member, and in particular by its
    name.  The standard array types used most often are named "vertex",
    "normal", "texcoord", and "color"; other kinds of data may be piggybacked
    into the data record simply by choosing a unique name.
    """

    stride: int
    pad_to: int
    divisor: int
    @property
    def registered(self) -> bool: ...
    @property
    def total_bytes(self) -> int: ...
    @property
    def columns(self) -> Sequence[GeomVertexColumn]: ...
    @overload
    def __init__(self, copy: GeomVertexArrayFormat = ...) -> None: ...
    @overload
    def __init__(
        self,
        name0: InternalName | str,
        num_components0: int,
        numeric_type0: _GeomEnums_NumericType,
        contents0: _GeomEnums_Contents,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name0: InternalName | str,
        num_components0: int,
        numeric_type0: _GeomEnums_NumericType,
        contents0: _GeomEnums_Contents,
        name1: InternalName | str,
        num_components1: int,
        numeric_type1: _GeomEnums_NumericType,
        contents1: _GeomEnums_Contents,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name0: InternalName | str,
        num_components0: int,
        numeric_type0: _GeomEnums_NumericType,
        contents0: _GeomEnums_Contents,
        name1: InternalName | str,
        num_components1: int,
        numeric_type1: _GeomEnums_NumericType,
        contents1: _GeomEnums_Contents,
        name2: InternalName | str,
        num_components2: int,
        numeric_type2: _GeomEnums_NumericType,
        contents2: _GeomEnums_Contents,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name0: InternalName | str,
        num_components0: int,
        numeric_type0: _GeomEnums_NumericType,
        contents0: _GeomEnums_Contents,
        name1: InternalName | str,
        num_components1: int,
        numeric_type1: _GeomEnums_NumericType,
        contents1: _GeomEnums_Contents,
        name2: InternalName | str,
        num_components2: int,
        numeric_type2: _GeomEnums_NumericType,
        contents2: _GeomEnums_Contents,
        name3: InternalName | str,
        num_components3: int,
        numeric_type3: _GeomEnums_NumericType,
        contents3: _GeomEnums_Contents,
    ) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def assign(self, copy: Self) -> Self: ...
    def unref(self) -> bool:
        """This method overrides ReferenceCount::unref() to unregister the object when
        its reference count goes to zero.
        """
    def is_registered(self) -> bool:
        """Returns true if this format has been registered, false if it has not.  It
        may not be used for a Geom until it has been registered, but once
        registered, it may no longer be modified.
        """
    @staticmethod
    def register_format(format: GeomVertexArrayFormat) -> GeomVertexArrayFormat:
        """Adds the indicated format to the registry, if there is not an equivalent
        format already there; in either case, returns the pointer to the equivalent
        format now in the registry.

        This is similar to GeomVertexFormat::register_format(), except that you
        generally need not call it explicitly.  Calling
        GeomVertexFormat::register_format() automatically registers all of the
        nested array formats.
        """
    def get_stride(self) -> int:
        """Returns the total number of bytes reserved in the array for each vertex."""
    def set_stride(self, stride: int) -> None:
        """Changes the total number of bytes reserved in the array for each vertex.
        You may not reduce this below get_total_bytes(), but you may increase it
        arbitrarily.
        """
    def get_pad_to(self) -> int:
        """Returns the byte divisor to which the data record must be padded to meet
        hardware limitations.  For instance, if this is 4, the stride will be
        automatically rounded up to the next multiple of 4 bytes.  This value is
        automatically increased as needed to ensure the individual numeric
        components in the array are word-aligned.
        """
    def set_pad_to(self, pad_to: int) -> None:
        """Explicitly sets the byte divisor to which the data record must be padded to
        meet hardware limitations.  See get_pad_to().  Normally it is not necessary
        to call this unless you have some specific requirements for row-to-row data
        alignment.  Note that this value may be automatically increased at each
        subsequent call to add_column().
        """
    def get_divisor(self) -> int:
        """Returns the divisor attribute for the data in this array.  If 0, it
        contains per-vertex data.  If 1, it contains per-instance data.  If higher
        than 1, the read row is advanced for each n instances.
        """
    def set_divisor(self, divisor: int) -> None:
        """Set this to 0 to indicate that this array contains per-vertex data, or to 1
        to indicate that it contains per-instance data.  If higher than 1, the read
        row is advanced for each n instances.
        """
    def get_total_bytes(self) -> int:
        """Returns the total number of bytes used by the data types within the format,
        including gaps between elements.
        """
    @overload
    def add_column(self, column: GeomVertexColumn) -> int:
        """`(self, name: InternalName, num_components: int, numeric_type: _GeomEnums_NumericType, contents: _GeomEnums_Contents, start: int = ..., column_alignment: int = ...)`:
        Adds a new column to the specification.  This is a table of per-vertex
        floating-point numbers such as "vertex" or "normal"; you must specify where
        in each record the table starts, and how many components (dimensions) exist
        per vertex.

        The return value is the index number of the new data type.

        `(self, column: GeomVertexColumn)`:
        Adds a new column to the specification.  This is a table of per-vertex
        floating-point numbers such as "vertex" or "normal"; you must specify where
        in each record the table starts, and how many components (dimensions) exist
        per vertex.

        Adding a column with the same name as a previous type, or that overlaps
        with one or more previous types, quietly removes the previous type(s).

        The return value is the index number of the new data type.
        """
    @overload
    def add_column(
        self,
        name: InternalName | str,
        num_components: int,
        numeric_type: _GeomEnums_NumericType,
        contents: _GeomEnums_Contents,
        start: int = ...,
        column_alignment: int = ...,
    ) -> int: ...
    def remove_column(self, name: InternalName | str) -> None:
        """Removes the column with the indicated name, if any.  This leaves a gap in
        the byte structure.
        """
    def clear_columns(self) -> None:
        """Removes all columns previously added, sets the stride to zero, and prepares
        to start over.
        """
    def pack_columns(self) -> None:
        """Removes wasted space between columns."""
    def align_columns_for_animation(self) -> None:
        """Reprocesses the columns in the format to align the C_point and C_vector
        columns to 16-byte boundaries to allow for the more efficient SSE2
        operations (assuming SSE2 is enabled in the build).

        The caller is responsible for testing vertex_animation_align_16 to decide
        whether to call this method.
        """
    def get_num_columns(self) -> int:
        """Returns the number of different columns in the array."""
    @overload
    def get_column(self, name: InternalName | str) -> GeomVertexColumn:
        """`(self, name: InternalName)`:
        Returns the specification with the indicated name, or NULL if the name is
        not used.

        `(self, i: int)`:
        Returns the ith column of the array.

        `(self, start_byte: int, num_bytes: int)`:
        Returns the first specification that overlaps with any of the indicated
        bytes in the range, or NULL if none do.
        """
    @overload
    def get_column(self, i: int) -> GeomVertexColumn: ...
    @overload
    def get_column(self, start_byte: int, num_bytes: int) -> GeomVertexColumn: ...
    def has_column(self, name: InternalName | str) -> bool:
        """Returns true if the array has the named column, false otherwise."""
    def is_data_subset_of(self, other: GeomVertexArrayFormat) -> bool:
        """Returns true if all of the fields in this array format are also present and
        equivalent in the other array format, and in the same byte positions, and
        the stride is the same.  That is, true if this format can share the same
        data pointer as the other format (with possibly some unused gaps).
        """
    def count_unused_space(self) -> int:
        """Returns the number of bytes per row that are not assigned to any column."""
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_with_data(self, out: ostream, indent_level: int, array_data: GeomVertexArrayData) -> None: ...
    def get_format_string(self, pad: bool = ...) -> str:
        """Returns a string with format codes representing the exact memory layout of
        the columns in memory, as understood by Python's struct module.  If pad is
        true, extra padding bytes are added to the end as 'x' characters as needed.
        """
    def get_columns(self) -> tuple[GeomVertexColumn, ...]: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToGeomEnums = upcast_to_GeomEnums
    isRegistered = is_registered
    registerFormat = register_format
    getStride = get_stride
    setStride = set_stride
    getPadTo = get_pad_to
    setPadTo = set_pad_to
    getDivisor = get_divisor
    setDivisor = set_divisor
    getTotalBytes = get_total_bytes
    addColumn = add_column
    removeColumn = remove_column
    clearColumns = clear_columns
    packColumns = pack_columns
    alignColumnsForAnimation = align_columns_for_animation
    getNumColumns = get_num_columns
    getColumn = get_column
    hasColumn = has_column
    isDataSubsetOf = is_data_subset_of
    countUnusedSpace = count_unused_space
    writeWithData = write_with_data
    getFormatString = get_format_string
    getColumns = get_columns

@final
class GeomVertexFormat(TypedWritableReferenceCount, GeomEnums):
    """This class defines the physical layout of the vertex data stored within a
    Geom.  The layout consists of a list of named columns, each of which has a
    numeric type and a size.

    The columns are typically interleaved within a single array, but they may
    also be distributed among multiple different arrays; at the extreme, each
    column may be alone within its own array (which amounts to a parallel-array
    definition).

    Thus, a GeomVertexFormat is really a list of GeomVertexArrayFormats, each
    of which contains a list of columns.  However, a particular column name
    should not appear more than once in the format, even between different
    arrays.

    There are a handful of standard pre-defined GeomVertexFormat objects, or
    you may define your own as needed.  You may record any combination of
    standard and/or user-defined columns in your custom GeomVertexFormat
    constructions.
    """

    animation: GeomVertexAnimationSpec
    @property
    def registered(self) -> bool: ...
    @property
    def arrays(self) -> MutableSequence[GeomVertexArrayFormat]: ...
    @property
    def points(self) -> Sequence[InternalName]: ...
    @property
    def vectors(self) -> Sequence[InternalName]: ...
    @property
    def columns(self) -> Mapping[InternalName, GeomVertexColumn]:
        """We also define this as a mapping interface, for lookups by name."""
    @overload
    def __init__(self, array_format: GeomVertexArrayFormat = ...) -> None: ...
    @overload
    def __init__(self, copy: GeomVertexFormat) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def assign(self, copy: GeomVertexArrayFormat | GeomVertexFormat) -> Self: ...
    def unref(self) -> bool:
        """This method overrides ReferenceCount::unref() to unregister the object when
        its reference count goes to zero.
        """
    def is_registered(self) -> bool:
        """Returns true if this format has been registered, false if it has not.  It
        may not be used for a Geom until it has been registered, but once
        registered, it may no longer be modified.
        """
    @staticmethod
    def register_format(format: GeomVertexArrayFormat | GeomVertexFormat) -> GeomVertexFormat:
        """`(format: GeomVertexArrayFormat)`:
        This flavor of register_format() implicitly creates a one-array vertex
        format from the array definition.

        `(format: GeomVertexFormat)`:
        Adds the indicated format to the registry, if there is not an equivalent
        format already there; in either case, returns the pointer to the equivalent
        format now in the registry.

        This must be called before a format may be used in a Geom.  After this
        call, you should discard the original pointer you passed in (which may or
        may not now be invalid) and let its reference count decrement normally; you
        should use only the returned value from this point on.
        """
    def get_animation(self) -> GeomVertexAnimationSpec:
        """Returns the GeomVertexAnimationSpec that indicates how this format's
        vertices are set up for animation.
        """
    def set_animation(self, animation: GeomVertexAnimationSpec) -> None:
        """Resets the GeomVertexAnimationSpec that indicates how this format's
        vertices are set up for animation.  You should also, of course, change the
        columns in the tables accordingly.

        This may not be called once the format has been registered.
        """
    def get_post_animated_format(self) -> GeomVertexFormat:
        """Returns a suitable vertex format for sending the animated vertices to the
        graphics backend.  This is the same format as the source format, with the
        CPU-animation data elements removed.

        This may only be called after the format has been registered.  The return
        value will have been already registered.
        """
    def get_union_format(self, other: GeomVertexArrayFormat | GeomVertexFormat) -> GeomVertexFormat:
        """Returns a new GeomVertexFormat that includes all of the columns defined in
        either this GeomVertexFormat or the other one.  If any column is defined in
        both formats with different sizes (for instance, texcoord2 vs.  texcoord3),
        the new format will include the larger of the two definitions.

        This may only be called after both source formats have been registered.
        The return value will also have been already registered.
        """
    def get_num_arrays(self) -> int:
        """Returns the number of individual arrays required by the format.  If the
        array data is completely interleaved, this will be 1; if it is completely
        parallel, this will be the same as the number of data types.
        """
    def get_array(self, array: int) -> GeomVertexArrayFormat:
        """Returns the description of the nth array used by the format."""
    def modify_array(self, array: int) -> GeomVertexArrayFormat:
        """Returns a modifiable pointer to the indicated array.  This means
        duplicating it if it is shared or registered.

        This may not be called once the format has been registered.
        """
    def set_array(self, array: int, format: GeomVertexArrayFormat) -> None:
        """Replaces the definition of the indicated array.

        This may not be called once the format has been registered.
        """
    def remove_array(self, array: int) -> None:
        """Removes the nth array from the format.

        This may not be called once the format has been registered.
        """
    def add_array(self, array_format: GeomVertexArrayFormat) -> int:
        """Adds the indicated array definition to the list of arrays included within
        this vertex format definition.  The return value is the index number of the
        new array.

        This may not be called once the format has been registered.
        """
    def insert_array(self, array: int, array_format: GeomVertexArrayFormat) -> None:
        """Adds the indicated array definition to the list of arrays at the indicated
        position.  This works just like add_array(), except that you can specify
        which array index the new array should have.

        This may not be called once the format has been registered.
        """
    def clear_arrays(self) -> None:
        """Removes all of the array definitions from the format and starts over.

        This may not be called once the format has been registered.
        """
    def remove_empty_arrays(self) -> None:
        """Removes the arrays that define no columns.

        This may not be called once the format has been registered.
        """
    def get_num_columns(self) -> int:
        """Returns the total number of different columns in the specification, across
        all arrays.
        """
    @overload
    def get_array_with(self, name: InternalName | str) -> int:
        """`(self, name: InternalName)`:
        Returns the index number of the array with the indicated column, or -1 if
        no arrays contained that name.

        The return value can be passed to get_array_format() to get the format of
        the array.  It may also be passed to GeomVertexData::get_array_data() or
        get_data() or set_data() to manipulate the actual array data.

        This may only be called after the format has been registered.

        `(self, i: int)`:
        Returns the index number of the array with the ith column.

        The return value can be passed to get_array_format() to get the format of
        the array.  It may also be passed to GeomVertexData::get_array_data() or
        get_data() or set_data() to manipulate the actual array data.
        """
    @overload
    def get_array_with(self, i: int) -> int: ...
    @overload
    def get_column(self, name: InternalName | str) -> GeomVertexColumn:
        """`(self, name: InternalName)`:
        Returns the specification with the indicated name, or NULL if the name is
        not used.  Use get_array_with() to determine which array this column is
        associated with.

        `(self, i: int)`:
        Returns the ith column of the specification, across all arrays.
        """
    @overload
    def get_column(self, i: int) -> GeomVertexColumn: ...
    def has_column(self, name: InternalName | str) -> bool:
        """Returns true if the format has the named column, false otherwise."""
    def get_column_name(self, i: int) -> InternalName:
        """Returns the name of the ith column, across all arrays."""
    def remove_column(self, name: InternalName | str, keep_empty_array: bool = ...) -> None:
        """Removes the named column from the format, from whichever array it exists
        in.  If there are other columns remaining in the array, the array is left
        with a gap where the column used to be; if this was the only column in the
        array, the array is removed (unless keep_empty_array is true).

        This may not be called once the format has been registered.
        """
    def pack_columns(self) -> None:
        """Removes wasted space between columns."""
    def align_columns_for_animation(self) -> None:
        """Reprocesses the columns in the format to align the C_point and C_vector
        columns to 16-byte boundaries to allow for the more efficient SSE2
        operations (assuming SSE2 is enabled in the build).

        Also see maybe_align_columns_for_animation().
        """
    def maybe_align_columns_for_animation(self) -> None:
        """Calls align_columns_for_animation() if this format's AnimationSpec
        indicates that it contains animated vertices, and if vertex-animation-
        align-16 is true.
        """
    def get_num_points(self) -> int:
        """Returns the number of columns within the format that represent points in
        space.

        This may only be called after the format has been registered.
        """
    def get_point(self, n: int) -> InternalName:
        """Returns the name of the nth point column.  This represents a point in
        space, which should be transformed by any spatial transform matrix.

        This may only be called after the format has been registered.
        """
    def get_num_vectors(self) -> int:
        """Returns the number of columns within the format that represent directional
        vectors.

        This may only be called after the format has been registered.
        """
    def get_vector(self, n: int) -> InternalName:
        """Returns the name of the nth vector column.  This represents a directional
        vector, which should be transformed by any spatial transform matrix as a
        vector.

        This may only be called after the format has been registered.
        """
    def get_num_texcoords(self) -> int:
        """Returns the number of columns within the format that represent texture
        coordinates.

        This may only be called after the format has been registered.
        """
    def get_texcoord(self, n: int) -> InternalName:
        """Returns the name of the nth texcoord column.  This represents a texture
        coordinate.

        This may only be called after the format has been registered.
        """
    def get_num_morphs(self) -> int:
        """Returns the number of columns within the format that represent morph
        deltas.

        This may only be called after the format has been registered.
        """
    def get_morph_slider(self, n: int) -> InternalName:
        """Returns the slider name associated with the nth morph column.  This is the
        name of the slider that will control the morph, and should be defined
        within the SliderTable associated with the GeomVertexData.

        This may only be called after the format has been registered.
        """
    def get_morph_base(self, n: int) -> InternalName:
        """Returns the name of the base column that the nth morph modifies.  This
        column will also be defined within the format, and can be retrieved via
        get_array_with() and/or get_column().

        This may only be called after the format has been registered.
        """
    def get_morph_delta(self, n: int) -> InternalName:
        """Returns the name of the column that defines the nth morph.  This contains
        the delta offsets that are to be applied to the column defined by
        get_morph_base().  This column will be defined within the format, and can
        be retrieved via get_array_with() and/or get_column().

        This may only be called after the format has been registered.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def write_with_data(self, out: ostream, indent_level: int, data: GeomVertexData) -> None: ...
    @staticmethod
    def get_empty() -> GeomVertexFormat:
        """Returns a standard vertex format containing no arrays at all, useful for
        pull-style vertex rendering.
        """
    @staticmethod
    def get_v3() -> GeomVertexFormat:
        """Some standard vertex formats.  No particular requirement to use one of
        these, but the DirectX renderers can use these formats directly, whereas
        any other format will have to be converted first.
        """
    @staticmethod
    def get_v3n3() -> GeomVertexFormat:
        """Returns a standard vertex format with a 3-component normal and a
        3-component vertex position.
        """
    @staticmethod
    def get_v3t2() -> GeomVertexFormat:
        """Returns a standard vertex format with a 2-component texture coordinate pair
        and a 3-component vertex position.
        """
    @staticmethod
    def get_v3n3t2() -> GeomVertexFormat:
        """Returns a standard vertex format with a 2-component texture coordinate
        pair, a 3-component normal, and a 3-component vertex position.
        """
    @staticmethod
    def get_v3cp() -> GeomVertexFormat:
        """These formats, with the DirectX-style packed color, may not be supported
        directly by OpenGL.  If you use them and the driver does not support
        them, the GLGraphicsStateGuardian will automatically convert to native
        OpenGL form (with a small runtime overhead).
        """
    @staticmethod
    def get_v3cpt2() -> GeomVertexFormat:
        """Returns a standard vertex format with a 2-component texture coordinate
        pair, a packed color, and a 3-component vertex position.
        """
    @staticmethod
    def get_v3n3cp() -> GeomVertexFormat:
        """Returns a standard vertex format with a packed color, a 3-component normal,
        and a 3-component vertex position.
        """
    @staticmethod
    def get_v3n3cpt2() -> GeomVertexFormat:
        """Returns a standard vertex format with a 2-component texture coordinate
        pair, a packed color, a 3-component normal, and a 3-component vertex
        position.
        """
    @staticmethod
    def get_v3c4() -> GeomVertexFormat:
        """These formats, with an OpenGL-style four-byte color, are not supported
        directly by DirectX.  If you use them, the DXGraphicsStateGuardian will
        automatically convert to DirectX form (with a larger runtime overhead,
        since DirectX8, and old DirectX9 drivers, require everything to be
        interleaved together).
        """
    @staticmethod
    def get_v3c4t2() -> GeomVertexFormat:
        """Returns a standard vertex format with a 2-component texture coordinate
        pair, a 4-component color, and a 3-component vertex position.
        """
    @staticmethod
    def get_v3n3c4() -> GeomVertexFormat:
        """Returns a standard vertex format with a 4-component color, a 3-component
        normal, and a 3-component vertex position.
        """
    @staticmethod
    def get_v3n3c4t2() -> GeomVertexFormat:
        """Returns a standard vertex format with a 2-component texture coordinate
        pair, a 4-component color, a 3-component normal, and a 3-component vertex
        position.
        """
    def get_arrays(self) -> tuple[GeomVertexArrayFormat, ...]: ...
    def get_columns(self) -> tuple[GeomVertexColumn, ...]: ...
    def get_points(self) -> tuple[InternalName, ...]: ...
    def get_vectors(self) -> tuple[InternalName, ...]: ...
    def get_texcoords(self) -> tuple[InternalName, ...]: ...
    def get_morph_sliders(self) -> tuple[InternalName, ...]: ...
    def get_morph_bases(self) -> tuple[InternalName, ...]: ...
    def get_morph_deltas(self) -> tuple[InternalName, ...]: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToGeomEnums = upcast_to_GeomEnums
    isRegistered = is_registered
    registerFormat = register_format
    getAnimation = get_animation
    setAnimation = set_animation
    getPostAnimatedFormat = get_post_animated_format
    getUnionFormat = get_union_format
    getNumArrays = get_num_arrays
    getArray = get_array
    modifyArray = modify_array
    setArray = set_array
    removeArray = remove_array
    addArray = add_array
    insertArray = insert_array
    clearArrays = clear_arrays
    removeEmptyArrays = remove_empty_arrays
    getNumColumns = get_num_columns
    getArrayWith = get_array_with
    getColumn = get_column
    hasColumn = has_column
    getColumnName = get_column_name
    removeColumn = remove_column
    packColumns = pack_columns
    alignColumnsForAnimation = align_columns_for_animation
    maybeAlignColumnsForAnimation = maybe_align_columns_for_animation
    getNumPoints = get_num_points
    getPoint = get_point
    getNumVectors = get_num_vectors
    getVector = get_vector
    getNumTexcoords = get_num_texcoords
    getTexcoord = get_texcoord
    getNumMorphs = get_num_morphs
    getMorphSlider = get_morph_slider
    getMorphBase = get_morph_base
    getMorphDelta = get_morph_delta
    writeWithData = write_with_data
    getEmpty = get_empty
    getV3 = get_v3
    getV3n3 = get_v3n3
    getV3t2 = get_v3t2
    getV3n3t2 = get_v3n3t2
    getV3cp = get_v3cp
    getV3cpt2 = get_v3cpt2
    getV3n3cp = get_v3n3cp
    getV3n3cpt2 = get_v3n3cpt2
    getV3c4 = get_v3c4
    getV3c4t2 = get_v3c4t2
    getV3n3c4 = get_v3n3c4
    getV3n3c4t2 = get_v3n3c4t2
    getArrays = get_arrays
    getColumns = get_columns
    getPoints = get_points
    getVectors = get_vectors
    getTexcoords = get_texcoords
    getMorphSliders = get_morph_sliders
    getMorphBases = get_morph_bases
    getMorphDeltas = get_morph_deltas

class SimpleLru(Namable):
    """An implementation of a very simple LRU algorithm.  Also see AdaptiveLru."""

    def __init__(self, name: str, max_size: int) -> None: ...
    def upcast_to_Namable(self) -> Namable: ...
    def get_total_size(self) -> int:
        """Returns the total size of all objects currently active on the LRU."""
    def get_max_size(self) -> int:
        """Returns the max size of all objects that are allowed to be active on the
        LRU.
        """
    def set_max_size(self, max_size: int) -> None:
        """Changes the max size of all objects that are allowed to be active on the
        LRU.

        If the size is (size_t)-1, there is no limit.
        """
    def count_active_size(self) -> int:
        """Returns the total size of the pages that were enqueued since the last call
        to begin_epoch().
        """
    def consider_evict(self) -> None:
        """Evicts a sequence of objects if the queue is full."""
    def evict_to(self, target_size: int) -> None:
        """Evicts a sequence of objects until the queue fits within the indicated
        target size, regardless of its normal max size.
        """
    def begin_epoch(self) -> None:
        """Marks the end of the previous epoch and the beginning of the next one.
        This will evict any objects that are pending eviction, and also update any
        internal bookkeeping.
        """
    def validate(self) -> bool:
        """Checks that the LRU is internally self-consistent.  Returns true if
        successful, false if there is some problem.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    upcastToNamable = upcast_to_Namable
    getTotalSize = get_total_size
    getMaxSize = get_max_size
    setMaxSize = set_max_size
    countActiveSize = count_active_size
    considerEvict = consider_evict
    evictTo = evict_to
    beginEpoch = begin_epoch

class SimpleLruPage:
    """One atomic piece that may be managed by a SimpleLru chain.  To use this
    class, inherit from it and override evict_lru().
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: SimpleLruPage) -> None: ...
    @overload
    def __init__(self, lru_size: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_lru(self) -> SimpleLru:
        """Returns the LRU that manages this page, or NULL if it is not currently
        managed by any LRU.
        """
    def enqueue_lru(self, lru: SimpleLru) -> None:
        """Adds the page to the LRU for the first time, or marks it recently-accessed
        if it has already been added.

        If lru is NULL, it means to remove this page from its LRU.
        """
    def dequeue_lru(self) -> None:
        """Removes the page from its SimpleLru."""
    def mark_used_lru(self, lru: SimpleLru = ...) -> None:
        """`(self)`:
        To be called when the page is used; this will move it to the tail of the
        SimpleLru queue it is already on.

        This method is const because it's not technically modifying the contents of
        the page itself.

        `(self, lru: SimpleLru)`:
        To be called when the page is used; this will move it to the tail of the
        specified SimpleLru queue.
        """
    def get_lru_size(self) -> int:
        """Returns the size of this page as reported to the LRU, presumably in bytes."""
    def set_lru_size(self, lru_size: int) -> None:
        """Specifies the size of this page, presumably in bytes, although any unit is
        possible.
        """
    def evict_lru(self) -> None:
        """Evicts the page from the LRU.  Called internally when the LRU determines
        that it is full.  May also be called externally when necessary to
        explicitly evict the page.

        It is legal for this method to either evict the page as requested, do
        nothing (in which case the eviction will be requested again at the next
        epoch), or requeue itself on the tail of the queue (in which case the
        eviction will be requested again much later).
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    getLru = get_lru
    enqueueLru = enqueue_lru
    dequeueLru = dequeue_lru
    markUsedLru = mark_used_lru
    getLruSize = get_lru_size
    setLruSize = set_lru_size
    evictLru = evict_lru

class SimpleAllocator:
    """An implementation of a very simple block allocator.  This class can
    allocate ranges of nonnegative integers within a specified upper limit; it
    uses a simple first-fit algorithm to find the next available space.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, max_size: int, lock: Mutex) -> None: ...
    def alloc(self, size: int, alignment: int = ...) -> SimpleAllocatorBlock:
        """Allocates a new block.  Returns NULL if a block of the requested size
        cannot be allocated.

        To free the allocated block, call block->free(), or simply delete the block
        pointer.
        """
    def is_empty(self) -> bool:
        """Returns true if there are no blocks allocated on this page, or false if
        there is at least one.
        """
    def get_total_size(self) -> int:
        """Returns the total size of allocated objects."""
    def get_max_size(self) -> int:
        """Returns the available space for allocated objects."""
    def set_max_size(self, max_size: int) -> None:
        """Changes the available space for allocated objects.  This will not affect
        any already-allocated objects, but will have an effect on future calls to
        alloc().
        """
    def get_contiguous(self) -> int:
        """Returns an upper-bound estimate of the size of the largest contiguous block
        that may be allocated.  It is guaranteed that an attempt to allocate a
        block larger than this will fail, though it is not guaranteed that an
        attempt to allocate a block this size or smaller will succeed.
        """
    def get_first_block(self) -> SimpleAllocatorBlock:
        """Returns a pointer to the first allocated block, or NULL if there are no
        allocated blocks.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    isEmpty = is_empty
    getTotalSize = get_total_size
    getMaxSize = get_max_size
    setMaxSize = set_max_size
    getContiguous = get_contiguous
    getFirstBlock = get_first_block

class SimpleAllocatorBlock:
    """A single block as returned from SimpleAllocator::alloc()."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    def free(self) -> None:
        """Releases the allocated space."""
    def get_allocator(self) -> SimpleAllocator:
        """Returns the SimpleAllocator object that owns this block.  Returns NULL if
        the block has been freed.
        """
    def get_start(self) -> int:
        """Returns the starting point of this block.  It is an error to call this if
        the block has been freed.
        """
    def get_size(self) -> int:
        """Returns the size of this block.  It is an error to call this if the block
        has been freed.
        """
    def is_free(self) -> bool:
        """Returns true if the block has been freed, false if it is still valid."""
    def get_max_size(self) -> int:
        """Returns the maximum size this block can be reallocated to, as limited by
        the following block.
        """
    def realloc(self, size: int) -> bool:
        """Changes the size of this block to the specified size.  Returns true if the
        change is accepted, false if there was not enough room.
        """
    def get_next_block(self) -> SimpleAllocatorBlock:
        """Returns a pointer to the next allocated block in the chain, or NULL if
        there are no more allocated blocks.
        """
    def output(self, out: ostream) -> None: ...
    getAllocator = get_allocator
    getStart = get_start
    getSize = get_size
    isFree = is_free
    getMaxSize = get_max_size
    getNextBlock = get_next_block

class VertexDataSaveFile(SimpleAllocator):
    """A temporary file to hold the vertex data that has been evicted from memory
    and written to disk.  All vertex data arrays are written into one large
    flat file.
    """

    def is_valid(self) -> bool:
        """Returns true if the save file was successfully created and is ready for
        use, false if there was an error.
        """
    def get_total_file_size(self) -> int:
        """Returns the amount of space consumed by the save file, including unused
        portions.
        """
    def get_used_file_size(self) -> int:
        """Returns the amount of space within the save file that is currently in use."""
    isValid = is_valid
    getTotalFileSize = get_total_file_size
    getUsedFileSize = get_used_file_size

class VertexDataPage(SimpleAllocator, SimpleLruPage):
    """A block of bytes that holds one or more VertexDataBlocks.  The entire page
    may be paged out, in the form of in-memory compression or to an on-disk
    cache file, if necessary.
    """

    RC_resident: Final = 0
    RCResident: Final = 0
    RC_compressed: Final = 1
    RCCompressed: Final = 1
    RC_disk: Final = 2
    RCDisk: Final = 2
    RC_end_of_list: Final = 3
    RCEndOfList: Final = 3
    @property
    def save_file(self) -> VertexDataSaveFile: ...
    def upcast_to_SimpleAllocator(self) -> SimpleAllocator: ...
    def upcast_to_SimpleLruPage(self) -> SimpleLruPage: ...
    def get_ram_class(self) -> _VertexDataPage_RamClass:
        """Returns the current ram class of the array.  If this is other than
        RC_resident, the array data is not resident in memory.
        """
    def get_pending_ram_class(self) -> _VertexDataPage_RamClass:
        """Returns the pending ram class of the array.  If this is different from
        get_ram_class(), this page has been queued to be processed by the thread.
        Eventually the page will be set to this ram class.
        """
    def request_resident(self) -> None:
        """Ensures that the page will become resident soon.  Future calls to
        get_page_data() will eventually return non-NULL.
        """
    def alloc(self, size: int) -> VertexDataBlock:  # type: ignore[override]
        """Allocates a new block.  Returns NULL if a block of the requested size
        cannot be allocated.

        To free the allocated block, call block->free(), or simply delete the block
        pointer.
        """
    def get_first_block(self) -> VertexDataBlock:
        """Returns a pointer to the first allocated block, or NULL if there are no
        allocated blocks.
        """
    def get_book(self) -> VertexDataBook:
        """Returns a pointer to the book that owns this page."""
    @staticmethod
    def get_global_lru(rclass: _VertexDataPage_RamClass) -> SimpleLru:
        """Returns a pointer to the global LRU object that manages the
        VertexDataPage's with the indicated RamClass.
        """
    @staticmethod
    def get_pending_lru() -> SimpleLru:
        """Returns a pointer to the global LRU object that manages the
        VertexDataPage's that are pending processing by the thread.
        """
    @staticmethod
    def get_save_file() -> VertexDataSaveFile:
        """Returns the global VertexDataSaveFile that will be used to save vertex data
        buffers to disk when necessary.
        """
    def save_to_disk(self) -> bool:
        """Writes the page to disk, but does not evict it from memory or affect its
        LRU status.  If it gets evicted later without having been modified, it will
        not need to write itself to disk again.
        """
    @staticmethod
    def get_num_threads() -> int:
        """Returns the number of threads that have been spawned to service vertex
        paging requests, or 0 if no threads have been spawned (which may mean
        either that all paging requests will be handled by the main thread, or
        simply that no paging requests have yet been issued).
        """
    @staticmethod
    def get_num_pending_reads() -> int:
        """Returns the number of read requests that are waiting to be serviced by a
        thread.
        """
    @staticmethod
    def get_num_pending_writes() -> int:
        """Returns the number of write requests that are waiting to be serviced by a
        thread.
        """
    @staticmethod
    def stop_threads() -> None:
        """Call this to stop the paging threads, if they were started.  This may block
        until all of the pending tasks have been completed.
        """
    @staticmethod
    def flush_threads() -> None:
        """Waits for all of the pending thread tasks to finish before returning."""
    def write(self, out: ostream, indent_level: int) -> None: ...  # type: ignore[override]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    upcastToSimpleAllocator = upcast_to_SimpleAllocator
    upcastToSimpleLruPage = upcast_to_SimpleLruPage
    getRamClass = get_ram_class
    getPendingRamClass = get_pending_ram_class
    requestResident = request_resident
    getFirstBlock = get_first_block
    getBook = get_book
    getGlobalLru = get_global_lru
    getPendingLru = get_pending_lru
    getSaveFile = get_save_file
    saveToDisk = save_to_disk
    getNumThreads = get_num_threads
    getNumPendingReads = get_num_pending_reads
    getNumPendingWrites = get_num_pending_writes
    stopThreads = stop_threads
    flushThreads = flush_threads
    getClassType = get_class_type

class VertexDataBook:
    """A collection of VertexDataPages, which can be used to allocate new
    VertexDataBlock objects.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, block_size: int) -> None: ...
    def alloc(self, size: int) -> VertexDataBlock:
        """Allocates and returns a new VertexDataBuffer of the requested size."""
    def get_num_pages(self) -> int:
        """Returns the number of pages created for the book."""
    def count_total_page_size(self, ram_class: _VertexDataPage_RamClass = ...) -> int:
        """`(self)`:
        Returns the total size of all bytes owned by all pages owned by this book.

        `(self, ram_class: _VertexDataPage_RamClass)`:
        Returns the total size of all bytes owned by all pages owned by this book
        that have the indicated ram class.
        """
    def count_allocated_size(self, ram_class: _VertexDataPage_RamClass = ...) -> int:
        """`(self)`:
        Returns the total size of all bytes allocated within pages owned by this
        book.

        `(self, ram_class: _VertexDataPage_RamClass)`:
        Returns the total size of all bytes allocated within pages owned by this
        book that have the indicated ram class.
        """
    def save_to_disk(self) -> None:
        """Writes all pages to disk immediately, just in case they get evicted later.
        It makes sense to make this call just before taking down a loading screen,
        to minimize chugs from saving pages inadvertently later.
        """
    getNumPages = get_num_pages
    countTotalPageSize = count_total_page_size
    countAllocatedSize = count_allocated_size
    saveToDisk = save_to_disk

class VertexDataBlock(SimpleAllocatorBlock, ReferenceCount):
    """A block of bytes that stores the actual raw vertex data referenced by a
    GeomVertexArrayData object.
    """

    def upcast_to_SimpleAllocatorBlock(self) -> SimpleAllocatorBlock: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    def get_page(self) -> VertexDataPage:
        """Returns the page from which this buffer was allocated."""
    def get_next_block(self) -> VertexDataBlock:
        """Returns a pointer to the next allocated block in the chain, or NULL if
        there are no more allocated blocks.
        """
    upcastToSimpleAllocatorBlock = upcast_to_SimpleAllocatorBlock
    upcastToReferenceCount = upcast_to_ReferenceCount
    getPage = get_page
    getNextBlock = get_next_block

class GeomVertexArrayData(CopyOnWriteObject, SimpleLruPage, GeomEnums):  # type: ignore[misc]
    """This is the data for one array of a GeomVertexData structure.  Many
    GeomVertexData structures will only define one array, with all data
    elements interleaved (DirectX 8.0 and before insisted on this format); some
    will define multiple arrays.

    DirectX calls this concept of one array a "stream". It also closely
    correlates with the concept of a vertex buffer.

    This object is just a block of data.  In general, you should not be
    directly messing with this object from application code.  See
    GeomVertexData for the organizing structure, and see
    GeomVertexReader/Writer/Rewriter for high-level tools to manipulate the
    actual vertex data.
    """

    usage_hint: _GeomEnums_UsageHint
    @property
    def array_format(self) -> GeomVertexArrayFormat: ...
    @property
    def data_size_bytes(self) -> int: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @overload
    def __init__(self, copy: GeomVertexArrayData) -> None: ...
    @overload
    def __init__(self, array_format: GeomVertexArrayFormat, usage_hint: _GeomEnums_UsageHint) -> None: ...
    def upcast_to_CopyOnWriteObject(self) -> CopyOnWriteObject: ...
    def upcast_to_SimpleLruPage(self) -> SimpleLruPage: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def compare_to(self, other: GeomVertexArrayData) -> int:
        """Returns 0 if the two arrays are equivalent, even if they are not the same
        pointer.
        """
    def get_array_format(self) -> GeomVertexArrayFormat:
        """Returns the format object that describes this array."""
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the usage hint that describes to the rendering backend how often
        the vertex data will be modified and/or rendered.  See geomEnums.h.
        """
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None:
        """Changes the UsageHint hint for this array.  See get_usage_hint().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def has_column(self, name: InternalName | str) -> bool:
        """Returns true if the array has the named column, false otherwise.  This is
        really just a shortcut for asking the same thing from the format.
        """
    def get_num_rows(self) -> int:
        """Returns the number of rows stored in the array, based on the number of
        bytes and the stride.  This should be the same for all arrays within a
        given GeomVertexData object.
        """
    def set_num_rows(self, n: int) -> bool:
        """Sets the length of the array to n rows.

        Normally, you would not call this directly, since all of the arrays in a
        particular GeomVertexData must have the same number of rows; instead, call
        GeomVertexData::set_num_rows().

        The return value is true if the number of rows was changed, false if the
        object already contained n rows (or if there was some error).

        The new vertex data is initialized to 0, including the "color" column (but
        see GeomVertexData::set_num_rows()).

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def unclean_set_num_rows(self, n: int) -> bool:
        """This method behaves like set_num_rows(), except the new data is not
        initialized.  Furthermore, after this call, *any* of the data in the
        GeomVertexArrayData may be uninitialized, including the earlier rows.

        Normally, you would not call this directly, since all of the arrays in a
        particular GeomVertexData must have the same number of rows; instead, call
        GeomVertexData::unclean_set_num_rows().
        """
    def reserve_num_rows(self, n: int) -> bool:
        """This ensures that enough memory space for n rows is allocated, so that you
        may increase the number of rows to n without causing a new memory
        allocation.  This is a performance optimization only; it is especially
        useful when you know ahead of time that you will be adding n rows to the
        data.
        """
    def clear_rows(self) -> None:
        """Removes all of the rows in the array.  Functionally equivalent to
        set_num_rows(0).
        """
    def get_data_size_bytes(self) -> int:
        """Returns the number of bytes stored in the array."""
    def get_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the array vertex data is modified.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def request_resident(self, current_thread: Thread = ...) -> bool:
        """Returns true if the vertex data is currently resident in memory.  If this
        returns true, the next call to get_handle()->get_read_pointer() will
        probably not block.  If this returns false, the vertex data will be brought
        back into memory shortly; try again later.
        """
    def get_handle(self, current_thread: Thread = ...) -> GeomVertexArrayDataHandle:
        """Returns an object that can be used to read the actual data bytes stored in
        the array.  Calling this method locks the data, and will block any other
        threads attempting to read or write the data, until the returned object
        destructs.
        """
    def modify_handle(self, current_thread: Thread = ...) -> GeomVertexArrayDataHandle:
        """Returns an object that can be used to read or write the actual data bytes
        stored in the array.  Calling this method locks the data, and will block
        any other threads attempting to read or write the data, until the returned
        object destructs.
        """
    def prepare(self, prepared_objects: PreparedGraphicsObjects) -> None:
        """Indicates that the data should be enqueued to be prepared in the indicated
        prepared_objects at the beginning of the next frame.  This will ensure the
        data is already loaded into the GSG if it is expected to be rendered soon.

        Use this function instead of prepare_now() to preload datas from a user
        interface standpoint.
        """
    def is_prepared(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the data has already been prepared or enqueued for
        preparation on the indicated GSG, false otherwise.
        """
    def prepare_now(self, prepared_objects: PreparedGraphicsObjects, gsg: GraphicsStateGuardianBase) -> VertexBufferContext:
        """Creates a context for the data on the particular GSG, if it does not
        already exist.  Returns the new (or old) VertexBufferContext.  This assumes
        that the GraphicsStateGuardian is the currently active rendering context
        and that it is ready to accept new datas.  If this is not necessarily the
        case, you should use prepare() instead.

        Normally, this is not called directly except by the GraphicsStateGuardian;
        a data does not need to be explicitly prepared by the user before it may be
        rendered.
        """
    def release(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Frees the data context only on the indicated object, if it exists there.
        Returns true if it was released, false if it had not been prepared.
        """
    def release_all(self) -> int:
        """Frees the context allocated on all objects for which the data has been
        declared.  Returns the number of contexts which have been freed.
        """
    @staticmethod
    def get_independent_lru() -> SimpleLru:
        """Returns a pointer to the global LRU object that manages the
        GeomVertexArrayData's that have not (yet) been paged out.
        """
    @staticmethod
    def get_small_lru() -> SimpleLru:
        """Returns a pointer to the global LRU object that manages the
        GeomVertexArrayData's that are deemed too small to be paged out.
        """
    @staticmethod
    def lru_epoch() -> None:
        """Marks that an epoch has passed in each LRU.  Asks the LRU's to consider
        whether they should perform evictions.
        """
    @staticmethod
    def get_book() -> VertexDataBook:
        """Returns the global VertexDataBook that will be used to allocate vertex data
        buffers.
        """
    upcastToCopyOnWriteObject = upcast_to_CopyOnWriteObject
    upcastToSimpleLruPage = upcast_to_SimpleLruPage
    upcastToGeomEnums = upcast_to_GeomEnums
    compareTo = compare_to
    getArrayFormat = get_array_format
    getUsageHint = get_usage_hint
    setUsageHint = set_usage_hint
    hasColumn = has_column
    getNumRows = get_num_rows
    setNumRows = set_num_rows
    uncleanSetNumRows = unclean_set_num_rows
    reserveNumRows = reserve_num_rows
    clearRows = clear_rows
    getDataSizeBytes = get_data_size_bytes
    getModified = get_modified
    requestResident = request_resident
    getHandle = get_handle
    modifyHandle = modify_handle
    isPrepared = is_prepared
    prepareNow = prepare_now
    releaseAll = release_all
    getIndependentLru = get_independent_lru
    getSmallLru = get_small_lru
    lruEpoch = lru_epoch
    getBook = get_book

class GeomVertexArrayDataHandle(ReferenceCount, GeomEnums):
    """This data object is returned by GeomVertexArrayData::get_handle() or
    modify_handle(). As long as it exists, the data is locked; when the last of
    these destructs, the data is unlocked.

    Only one thread at a time may lock the data; other threads attempting to
    lock the data will block.  A given thread may simultaneously lock the data
    multiple times.

    This class serves in lieu of a pair of GeomVertexArrayDataPipelineReader
    and GeomVertexArrayDataPipelineWriter classes
    """

    @property
    def object(self) -> GeomVertexArrayData: ...
    @property
    def array_format(self) -> GeomVertexArrayFormat: ...
    @property
    def usage_hint(self) -> _GeomEnums_UsageHint: ...
    @property
    def data_size_bytes(self) -> int: ...
    @property
    def modified(self) -> UpdateSeq: ...
    def upcast_to_ReferenceCount(self) -> ReferenceCount: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def get_object(self) -> GeomVertexArrayData: ...
    def get_array_format(self) -> GeomVertexArrayFormat: ...
    def get_usage_hint(self) -> _GeomEnums_UsageHint: ...
    def get_num_rows(self) -> int: ...
    def set_num_rows(self, n: int) -> bool: ...
    def unclean_set_num_rows(self, n: int) -> bool: ...
    def reserve_num_rows(self, n: int) -> bool: ...
    def clear_rows(self) -> None: ...
    def get_data_size_bytes(self) -> int: ...
    def get_modified(self) -> UpdateSeq: ...
    def request_resident(self) -> bool:
        """Returns true if the vertex data is currently resident in memory.  If this
        returns true, the next call to get_handle()->get_read_pointer() will
        probably not block.  If this returns false, the vertex data will be brought
        back into memory shortly; try again later.
        """
    def prepare_now(self, prepared_objects: PreparedGraphicsObjects, gsg: GraphicsStateGuardianBase) -> VertexBufferContext:
        """Creates a context for the data on the particular GSG, if it does not
        already exist.  Returns the new (or old) VertexBufferContext.  This assumes
        that the GraphicsStateGuardian is the currently active rendering context
        and that it is ready to accept new datas.  If this is not necessarily the
        case, you should use prepare() instead.

        Normally, this is not called directly except by the GraphicsStateGuardian;
        a data does not need to be explicitly prepared by the user before it may be
        rendered.
        """
    @overload
    def copy_data_from(self, other: GeomVertexArrayDataHandle) -> None:
        """Copies the entire data array from the other object."""
    @overload
    def copy_data_from(self, buffer) -> None: ...
    @overload
    def copy_subdata_from(self, to_start: int, to_size: int, buffer) -> None:
        """Copies a portion of the data array from the other object into a portion of
        the data array of this object.  If to_size != from_size, the size of this
        data array is adjusted accordingly.
        """
    @overload
    def copy_subdata_from(
        self, to_start: int, to_size: int, other: GeomVertexArrayDataHandle, from_start: int, from_size: int
    ) -> None: ...
    @overload
    def copy_subdata_from(self, to_start: int, to_size: int, buffer, from_start: int, from_size: int) -> None: ...
    def get_data(self) -> bytes:
        """Returns the entire raw data of the GeomVertexArrayData object, formatted as
        a string.  This is primarily for the benefit of high-level languages such
        as Python.
        """
    def set_data(self, data: bytes) -> None:
        """Replaces the entire raw data array with the contents of the indicated
        string.  This is primarily for the benefit of high-level languages like
        Python.
        """
    def get_subdata(self, start: int, size: int) -> bytes:
        """Returns a subset of the raw data of the GeomVertexArrayData object,
        formatted as a string.  This is primarily for the benefit of high-level
        languages such as Python.
        """
    def set_subdata(self, start: int, size: int, data: bytes) -> None:
        """Replaces a portion of the data array from the indicated string.  If size !=
        data.size(), the size of this data array is adjusted accordingly.

        This is primarily for the benefit of high-level languages like Python.
        """
    def mark_used(self) -> None:
        """Marks the array data recently-used."""
    upcastToReferenceCount = upcast_to_ReferenceCount
    upcastToGeomEnums = upcast_to_GeomEnums
    getObject = get_object
    getArrayFormat = get_array_format
    getUsageHint = get_usage_hint
    getNumRows = get_num_rows
    setNumRows = set_num_rows
    uncleanSetNumRows = unclean_set_num_rows
    reserveNumRows = reserve_num_rows
    clearRows = clear_rows
    getDataSizeBytes = get_data_size_bytes
    getModified = get_modified
    requestResident = request_resident
    prepareNow = prepare_now
    copyDataFrom = copy_data_from
    copySubdataFrom = copy_subdata_from
    getData = get_data
    setData = set_data
    getSubdata = get_subdata
    setSubdata = set_subdata
    markUsed = mark_used

class GeomCacheManager:
    """This is used to keep track of, and limit the size of, the cache of munged
    vertices, which would otherwise be distributed through all of the
    GeomVertexData objects in the system.

    The actual data in the cache is not stored here, but rather it is
    distributed among the various GeomVertexData source objects.  This allows
    the cache data to propagate through the multiprocess pipeline.

    This structure actually caches any of a number of different types of
    pointers, and mixes them all up in the same LRU cache list.  Some of them
    (such as GeomMunger) are reference-counted here in the cache; most are not.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_max_size(self, max_size: int) -> None:
        """Specifies the maximum number of entries in the cache for storing pre-
        processed data for rendering vertices.  This limit is flexible, and may be
        temporarily exceeded if many different Geoms are pre-processed during the
        space of a single frame.

        This is not a limit on the actual vertex data, which is what it is; it is
        also not a limit on the amount of memory used by the video driver or the
        system graphics interface, which Panda has no control over.
        """
    def get_max_size(self) -> int:
        """Returns the maximum number of entries in the cache for storing pre-
        processed data for rendering vertices.  See set_max_size().
        """
    def get_total_size(self) -> int:
        """Returns the number of entries currently in the cache."""
    def flush(self) -> None:
        """Immediately empties all elements in the cache."""
    @staticmethod
    def get_global_ptr() -> GeomCacheManager:
        """Returns the global cache manager pointer."""
    setMaxSize = set_max_size
    getMaxSize = get_max_size
    getTotalSize = get_total_size
    getGlobalPtr = get_global_ptr

class VertexTransform(TypedWritableReferenceCount):
    """This is an abstract base class that holds a pointer to some transform,
    computed in some arbitrary way, that is to be applied to vertices during
    rendering.  This is used to implement soft-skinned and animated vertices.
    Derived classes will define how the transform is actually computed.
    """

    @property
    def modified(self) -> UpdateSeq: ...
    def get_matrix(self, matrix: Mat4Like) -> None: ...
    def mult_matrix(self, result: Mat4Like, previous: Mat4Like) -> None:
        """Premultiplies this transform's matrix with the indicated previous matrix,
        so that the result is the net composition of the given transform with this
        transform.  The result is stored in the parameter "result", which should
        not be the same matrix as previous.
        """
    def accumulate_matrix(self, accum: Mat4Like, weight: float) -> None:
        """Adds the value of this transform's matrix, modified by the indicated
        weight, into the indicated accumulation matrix.  This is used to compute
        the result of several blended transforms.
        """
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a sequence number that's guaranteed to change at least every time
        the value reported by get_matrix() changes.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_next_modified(current_thread: Thread) -> UpdateSeq:
        """Returns a monotonically increasing sequence.  Each time this is called, a
        new sequence number is returned, higher than the previous value.

        This is used to ensure that all VertexTransform::get_modified() calls
        return an increasing number in the same space, so that
        TransformBlend::get_modified() is easy to determine.  It is similar to
        Geom::get_modified(), but it is in a different space.
        """
    @staticmethod
    def get_global_modified(current_thread: Thread) -> UpdateSeq:
        """Returns the currently highest VertexTransform::get_modified() value in the
        world.  This can be used as a quick way to determine if any
        VertexTransforms have changed value recently.
        """
    getMatrix = get_matrix
    multMatrix = mult_matrix
    accumulateMatrix = accumulate_matrix
    getModified = get_modified
    getNextModified = get_next_modified
    getGlobalModified = get_global_modified

class TransformTable(TypedWritableReferenceCount):
    """Stores the total set of VertexTransforms that the vertices in a particular
    GeomVertexData object might depend on.

    This structure is used for a GeomVertexData set up to compute its dynamic
    vertices on the graphics card.  See TransformBlendTable for one set up to
    compute its dynamic vertices on the CPU.
    """

    @property
    def registered(self) -> bool: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @property
    def transforms(self) -> MutableSequence[VertexTransform]: ...
    def __init__(self, copy: TransformTable = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def is_registered(self) -> bool:
        """Returns true if this table has been registered.  Once it has been
        registered, the set of transforms in a TransformTable may not be further
        modified; but it must be registered before it can be assigned to a Geom.
        """
    @staticmethod
    def register_table(table: TransformTable) -> TransformTable:
        """Registers a TransformTable for use.  This is similar to
        GeomVertexFormat::register_format().  Once registered, a TransformTable may
        no longer be modified (although the individual VertexTransform objects may
        modify their reported transforms).

        This must be called before a table may be used in a Geom.  After this call,
        you should discard the original pointer you passed in (which may or may not
        now be invalid) and let its reference count decrement normally; you should
        use only the returned value from this point on.
        """
    def get_num_transforms(self) -> int:
        """Returns the number of transforms in the table."""
    def get_transform(self, n: int) -> VertexTransform:
        """Returns the nth transform in the table."""
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a sequence number that's guaranteed to change at least when any
        VertexTransforms in the table change.  (However, this is only true for a
        registered table.  An unregistered table may or may not reflect an update
        here when a VertexTransform changes.)
        """
    def set_transform(self, n: int, transform: VertexTransform) -> None:
        """Replaces the nth transform.  Only valid for unregistered tables."""
    def insert_transform(self, n: int, transform: VertexTransform) -> None:
        """Inserts a new transform to the table at the given index position.  If the
        index is beyond the end of the table, appends it to the end.  Only valid
        for unregistered tables.

        This does not automatically uniquify the pointer; if the transform is
        already present in the table, it will be added twice.
        """
    def remove_transform(self, n: int) -> None:
        """Removes the nth transform.  Only valid for unregistered tables."""
    def add_transform(self, transform: VertexTransform) -> int:
        """Adds a new transform to the table and returns the index number of the new
        transform.  Only valid for unregistered tables.

        This does not automatically uniquify the pointer; if the transform is
        already present in the table, it will be added twice.
        """
    def write(self, out: ostream) -> None: ...
    def get_transforms(self) -> tuple[VertexTransform, ...]: ...
    isRegistered = is_registered
    registerTable = register_table
    getNumTransforms = get_num_transforms
    getTransform = get_transform
    getModified = get_modified
    setTransform = set_transform
    insertTransform = insert_transform
    removeTransform = remove_transform
    addTransform = add_transform
    getTransforms = get_transforms

class TransformBlend:
    """This defines a single entry in a TransformBlendTable.  It represents a
    unique combination of VertexTransform pointers and blend amounts.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def transforms(self) -> MutableSequence[VertexTransform]: ...
    @property
    def weights(self) -> Mapping[VertexTransform, float]: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @overload
    def __init__(self, copy: TransformBlend = ...) -> None: ...
    @overload
    def __init__(self, transform0: VertexTransform, weight0: float) -> None: ...
    @overload
    def __init__(self, transform0: VertexTransform, weight0: float, transform1: VertexTransform, weight1: float) -> None: ...
    @overload
    def __init__(
        self,
        transform0: VertexTransform,
        weight0: float,
        transform1: VertexTransform,
        weight1: float,
        transform2: VertexTransform,
        weight2: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        transform0: VertexTransform,
        weight0: float,
        transform1: VertexTransform,
        weight1: float,
        transform2: VertexTransform,
        weight2: float,
        transform3: VertexTransform,
        weight3: float,
    ) -> None: ...
    def __lt__(self, other: TransformBlend) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def compare_to(self, other: TransformBlend) -> int:
        """Defines an arbitrary ordering for TransformBlend objects."""
    def add_transform(self, transform: VertexTransform, weight: float) -> None:
        """Adds a new transform to the blend.  If the transform already existed,
        increases its weight factor.
        """
    @overload
    def remove_transform(self, transform: VertexTransform) -> None:
        """`(self, transform: VertexTransform)`:
        Removes the indicated transform from the blend.

        `(self, n: int)`:
        Removes the nth transform stored in the blend object.
        """
    @overload
    def remove_transform(self, n: int) -> None: ...
    def limit_transforms(self, max_transforms: int) -> None:
        """If the total number of transforms in the blend exceeds max_transforms,
        removes the n least-important transforms as needed to reduce the number of
        transforms to max_transforms.
        """
    def normalize_weights(self) -> None:
        """Rescales all of the weights on the various transforms so that they sum to
        1.0.  It is generally a good idea to call this after adding or removing
        transforms from the blend.
        """
    def has_transform(self, transform: VertexTransform) -> bool:
        """Returns true if the blend has the indicated transform, false otherwise."""
    @overload
    def get_weight(self, transform: VertexTransform) -> float:
        """`(self, transform: VertexTransform)`:
        Returns the weight associated with the indicated transform, or 0 if there
        is no entry for the transform.

        `(self, n: int)`:
        Returns the weight associated with the nth transform stored in the blend
        object.
        """
    @overload
    def get_weight(self, n: int) -> float: ...
    def get_num_transforms(self) -> int:
        """Returns the number of transforms stored in the blend object."""
    def get_transform(self, n: int) -> VertexTransform:
        """Returns the nth transform stored in the blend object."""
    def set_transform(self, n: int, transform: VertexTransform) -> None:
        """Replaces the nth transform stored in the blend object."""
    def set_weight(self, n: int, weight: float) -> None:
        """Replaces the weight associated with the nth transform stored in the blend
        object.
        """
    def update_blend(self, current_thread: Thread) -> None:
        """Recomputes the internal representation of the blend value, if necessary.
        You should call this before calling get_blend() or transform_point().
        """
    def get_blend(self, result: Mat4Like, current_thread: Thread) -> None:
        """Returns the current value of the blend, based on the current value of all
        of the nested transform objects and their associated weights.

        You should call update_blend() to ensure that the cache is up-to-date
        before calling this.
        """
    def transform_point(self, point: DoubleVec3Like | DoubleVec4Like | Vec3Like | Vec4Like, current_thread: Thread) -> None:
        """Transforms the indicated point by the blend matrix.

        You should call update_blend() to ensure that the cache is up-to-date
        before calling this.
        """
    def transform_vector(self, point: DoubleVec3Like | Vec3Like, current_thread: Thread) -> None:
        """Transforms the indicated vector by the blend matrix.

        You should call update_blend() to ensure that the cache is up-to-date
        before calling this.
        """
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a counter which is guaranteed to increment at least as often as the
        result of get_blend() changes.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_transforms(self) -> tuple[VertexTransform, ...]: ...
    compareTo = compare_to
    addTransform = add_transform
    removeTransform = remove_transform
    limitTransforms = limit_transforms
    normalizeWeights = normalize_weights
    hasTransform = has_transform
    getWeight = get_weight
    getNumTransforms = get_num_transforms
    getTransform = get_transform
    setTransform = set_transform
    setWeight = set_weight
    updateBlend = update_blend
    getBlend = get_blend
    transformPoint = transform_point
    transformVector = transform_vector
    getModified = get_modified
    getClassType = get_class_type
    getTransforms = get_transforms

class TransformBlendTable(CopyOnWriteObject):
    """This structure collects together the different combinations of transforms
    and blend amounts used by a GeomVertexData, to facilitate computing dynamic
    vertices on the CPU at runtime.  Each vertex has a pointer to exactly one
    of the entries in this table, and each entry defines a number of
    transform/blend combinations.

    This structure is used for a GeomVertexData set up to compute its dynamic
    vertices on the CPU.  See TransformTable for one set up to compute its
    dynamic vertices on the graphics card.
    """

    rows: SparseArray
    @property
    def blends(self) -> MutableSequence[TransformBlend]: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @property
    def num_transforms(self) -> int: ...
    @property
    def max_simultaneous_transforms(self) -> int: ...
    def __init__(self, copy: TransformBlendTable = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_num_blends(self) -> int:
        """Returns the total number of different blend combinations in the table."""
    def get_blend(self, n: int) -> TransformBlend:
        """Returns the nth blend in the table."""
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a counter which is guaranteed to increment at least when any
        TransformBlends within the table have changed.
        """
    def set_blend(self, n: int, blend: TransformBlend) -> None:
        """Replaces the blend at the nth position with the indicated value."""
    def remove_blend(self, n: int) -> None:
        """Removes the blend at the nth position."""
    def add_blend(self, blend: TransformBlend) -> int:
        """Adds a new blend to the table, and returns its index number.  If there is
        already an identical blend in the table, simply returns that number
        instead.
        """
    def get_num_transforms(self) -> int:
        """Returns the number of unique VertexTransform objects represented in the
        table.  This will correspond to the size of the TransformTable object that
        would represent the same table.  This is also the same limit reflected by
        GraphicsStateGuardian::get_max_vertex_transform_indices().
        """
    def get_max_simultaneous_transforms(self) -> int:
        """Returns the maximum number of unique VertexTransform objects that are
        applied to any one vertex simultaneously.  This is the same limit reflected
        by GraphicsStateGuardian::get_max_vertex_transforms().
        """
    def set_rows(self, rows: BitArray | SparseArray) -> None:
        """Specifies the subset of rows (vertices) in the associated GeomVertexData
        that this TransformBlendTable actually affects.
        """
    def get_rows(self) -> SparseArray:
        """Returns the subset of rows (vertices) in the associated GeomVertexData that
        this TransformBlendTable actually affects.
        """
    def modify_rows(self) -> SparseArray:
        """Returns a modifiable reference to the SparseArray that specifies the subset
        of rows (vertices) in the associated GeomVertexData that this
        TransformBlendTable actually affects.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    def get_blends(self) -> tuple[TransformBlend, ...]: ...
    getNumBlends = get_num_blends
    getBlend = get_blend
    getModified = get_modified
    setBlend = set_blend
    removeBlend = remove_blend
    addBlend = add_blend
    getNumTransforms = get_num_transforms
    getMaxSimultaneousTransforms = get_max_simultaneous_transforms
    setRows = set_rows
    getRows = get_rows
    modifyRows = modify_rows
    getBlends = get_blends

class VertexSlider(TypedWritableReferenceCount):
    """This is an abstract base class that retains some slider value, which is a
    linear value that typically ranges from 0.0 to 1.0, and is used to control
    the animation of morphs (blend shapes).

    It is similar to VertexTransform, which keeps a full 4x4 transform matrix,
    but the VertexSlider only keeps a single float value.
    """

    @property
    def name(self) -> InternalName: ...
    @property
    def slider(self) -> float: ...
    @property
    def modified(self) -> UpdateSeq: ...
    def get_name(self) -> InternalName:
        """Returns the name of this particular slider.  Every unique blend shape
        within a particular Geom must be identified with a different name, which is
        shared by the slider that controls it.
        """
    def get_slider(self) -> float: ...
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a sequence number that's guaranteed to change at least every time
        the value reported by get_slider() changes.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    getName = get_name
    getSlider = get_slider
    getModified = get_modified

class SliderTable(TypedWritableReferenceCount):
    """Stores the total set of VertexSliders that the vertices in a particular
    GeomVertexData object might depend on.

    This is similar to a TransformTable, but it stores VertexSliders instead of
    VertexTransforms, and it stores them by name instead of by index number.
    Also, it is only used when animating vertices on the CPU, since GPU's don't
    support morphs at this point in time.
    """

    @property
    def modified(self) -> UpdateSeq: ...
    def __init__(self, copy: SliderTable = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def is_registered(self) -> bool:
        """Returns true if this table has been registered.  Once it has been
        registered, the set of sliders in a SliderTable may not be further
        modified; but it must be registered before it can be assigned to a Geom.
        """
    @staticmethod
    def register_table(table: SliderTable) -> SliderTable:
        """Registers a SliderTable for use.  This is similar to
        GeomVertexFormat::register_format().  Once registered, a SliderTable may no
        longer be modified (although the individual VertexSlider objects may modify
        their reported sliders).

        This must be called before a table may be used in a Geom.  After this call,
        you should discard the original pointer you passed in (which may or may not
        now be invalid) and let its reference count decrement normally; you should
        use only the returned value from this point on.
        """
    def get_num_sliders(self) -> int:
        """Returns the number of sliders in the table."""
    def get_slider(self, n: int) -> VertexSlider:
        """Returns the nth slider in the table."""
    def get_slider_rows(self, n: int) -> SparseArray:
        """Returns the set of rows (vertices) governed by the nth slider in the table."""
    def find_sliders(self, name: InternalName | str) -> SparseArray:
        """Returns a list of slider indices that represent the list of sliders with
        the indicated name, or an empty SparseArray if no slider in the table has
        that name.
        """
    def has_slider(self, name: InternalName | str) -> bool:
        """Returns true if the table has at least one slider by the indicated name,
        false otherwise.
        """
    def is_empty(self) -> bool:
        """Returns true if the table has no sliders, false if it has at least one."""
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a sequence number that's guaranteed to change at least when any
        VertexSliders in the table change.  (However, this is only true for a
        registered table.  An unregistered table may or may not reflect an update
        here when a VertexSlider changes.)
        """
    def set_slider(self, n: int, slider: VertexSlider) -> None:
        """Replaces the nth slider.  Only valid for unregistered tables."""
    def set_slider_rows(self, n: int, rows: BitArray | SparseArray) -> None:
        """Replaces the rows affected by the nth slider.  Only valid for unregistered
        tables.
        """
    def remove_slider(self, n: int) -> None:
        """Removes the nth slider.  Only valid for unregistered tables."""
    def add_slider(self, slider: VertexSlider, rows: BitArray | SparseArray) -> int:
        """Adds a new slider to the table, and returns the index number of the new
        slider.  Only valid for unregistered tables.
        """
    def write(self, out: ostream) -> None: ...
    def get_sliders(self) -> tuple[VertexSlider, ...]: ...
    isRegistered = is_registered
    registerTable = register_table
    getNumSliders = get_num_sliders
    getSlider = get_slider
    getSliderRows = get_slider_rows
    findSliders = find_sliders
    hasSlider = has_slider
    isEmpty = is_empty
    getModified = get_modified
    setSlider = set_slider
    setSliderRows = set_slider_rows
    removeSlider = remove_slider
    addSlider = add_slider
    getSliders = get_sliders

class GeomVertexData(CopyOnWriteObject, GeomEnums):
    """This defines the actual numeric vertex data stored in a Geom, in the
    structure defined by a particular GeomVertexFormat object.

    The data consists of one or more arrays, each of which in turn consists of
    a series of rows, one per vertex.  All arrays should have the same number
    of rows; each vertex is defined by the column data from a particular row
    across all arrays.

    Often, there will be only one array per Geom, and the various columns
    defined in the GeomVertexFormat will be interleaved within that array.
    However, it is also possible to have multiple different arrays, with a
    certain subset of the total columns defined in each array.

    However the data is distributed, the effect is of a single table of
    vertices, where each vertex is represented by one row of the table.

    In general, application code should not attempt to directly manipulate the
    vertex data through this structure; instead, use the GeomVertexReader,
    GeomVertexWriter, and GeomVertexRewriter objects to read and write vertex
    data at a high level.
    """

    name: str
    usage_hint: _GeomEnums_UsageHint
    format: GeomVertexFormat
    transform_table: TransformTable
    slider_table: SliderTable
    @property
    def arrays(self) -> MutableSequence[GeomVertexArrayData]: ...
    @property
    def num_bytes(self) -> int: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @overload
    def __init__(self, copy: GeomVertexData, format: GeomVertexArrayFormat | GeomVertexFormat = ...) -> None:
        """This constructor copies all of the basic properties of the source
        VertexData, like usage_hint and animation tables, but does not copy the
        actual data, and it allows you to specify a different format.
        """
    @overload
    def __init__(self, name: str, format: GeomVertexArrayFormat | GeomVertexFormat, usage_hint: _GeomEnums_UsageHint) -> None: ...
    def upcast_to_CopyOnWriteObject(self) -> CopyOnWriteObject: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def assign(self, copy: Self) -> Self: ...
    def compare_to(self, other: GeomVertexData) -> int:
        """Returns 0 if the two objects are equivalent, even if they are not the same
        pointer.
        """
    def get_name(self) -> str:
        """Returns the name passed to the constructor, if any.  This name is reported
        on the PStats graph for vertex computations.
        """
    def set_name(self, name: str) -> None:
        """Changes the name of the vertex data.  This name is reported on the PStats
        graph for vertex computations.
        """
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the usage hint that was passed to the constructor, and which will
        be passed to each array data object created initially, and arrays created
        as the result of a convert_to() operation.  See geomEnums.h.

        However, each individual array may be replaced with a different array
        object with an independent usage hint specified, so there is no guarantee
        that the individual arrays all have the same usage_hint.
        """
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None:
        """Changes the UsageHint hint for this vertex data, and for all of the arrays
        that share this data.  See get_usage_hint().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_format(self) -> GeomVertexFormat:
        """Returns a pointer to the GeomVertexFormat structure that defines this data."""
    def set_format(self, format: GeomVertexArrayFormat | GeomVertexFormat) -> None:
        """Changes the format of the vertex data.  If the data is not empty, this will
        implicitly change every row to match the new format.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def unclean_set_format(self, format: GeomVertexArrayFormat | GeomVertexFormat) -> None:
        """Changes the format of the vertex data, without reformatting the data to
        match.  The data is exactly the same after this operation, but will be
        reinterpreted according to the new format.  This assumes that the new
        format is fundamentally compatible with the old format; in particular, it
        must have the same number of arrays with the same stride in each one.  No
        checking is performed that the data remains sensible.
        """
    def has_column(self, name: InternalName | str) -> bool:
        """Returns true if the data has the named column, false otherwise.  This is
        really just a shortcut for asking the same thing from the format.
        """
    def get_num_rows(self) -> int:
        """Returns the number of rows stored within all the arrays.  All arrays store
        data for the same n rows.
        """
    def set_num_rows(self, n: int) -> bool:
        """Sets the length of the array to n rows in all of the various arrays
        (presumably by adding rows).

        The new vertex data is initialized to 0, except for the "color" column,
        which is initialized to (1, 1, 1, 1).

        The return value is true if the number of rows was changed, false if the
        object already contained n rows (or if there was some error).

        This can be used when you know exactly how many rows you will be needing.
        It is faster than reserve_num_rows().  Also see unclean_set_num_rows() if
        you are planning to fill in all the data yourself.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def unclean_set_num_rows(self, n: int) -> bool:
        """This method behaves like set_num_rows(), except the new data is not
        initialized.  Furthermore, after this call, *any* of the data in the
        GeomVertexData may be uninitialized, including the earlier rows.

        This is intended for applications that are about to completely fill the
        GeomVertexData with new data anyway; it provides a tiny performance boost
        over set_num_rows().

        This can be used when you know exactly how many rows you will be needing.
        It is faster than reserve_num_rows().
        """
    def reserve_num_rows(self, n: int) -> bool:
        """This ensures that enough memory space for n rows is allocated, so that you
        may increase the number of rows to n without causing a new memory
        allocation.  This is a performance optimization only; it is especially
        useful when you know ahead of time that you will be adding n rows to the
        data.

        If you know exactly how many rows you will be needing, it is significantly
        faster to use set_num_rows() or unclean_set_num_rows() instead.
        """
    def clear_rows(self) -> None:
        """Removes all of the rows from the arrays; functionally equivalent to
        set_num_rows(0) (but faster).

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_num_arrays(self) -> int:
        """Returns the number of individual arrays stored within the data.  This must
        match get_format()->get_num_arrays().
        """
    def get_array(self, i: int) -> GeomVertexArrayData:
        """Returns a const pointer to the vertex data for the indicated array, for
        application code to directly examine (but not modify) the underlying vertex
        data.
        """
    def get_array_handle(self, i: int) -> GeomVertexArrayDataHandle:
        """Equivalent to get_array(i).get_handle()."""
    def modify_array(self, i: int) -> GeomVertexArrayData:
        """Returns a modifiable pointer to the indicated vertex array, so that
        application code may directly manipulate the data.  You should avoid
        changing the length of this array, since all of the arrays should be kept
        in sync--use set_num_rows() instead.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def modify_array_handle(self, i: int) -> GeomVertexArrayDataHandle:
        """Equivalent to modify_array(i).modify_handle()."""
    def set_array(self, i: int, array: GeomVertexArrayData) -> None:
        """Replaces the indicated vertex data array with a completely new array.  You
        should be careful that the new array has the same length and format as the
        old one, unless you know what you are doing.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_transform_table(self) -> TransformTable:
        """Returns a const pointer to the TransformTable assigned to this data.
        Vertices within the table will index into this table to indicate their
        dynamic skinning information; this table is used when the vertex animation
        is to be performed by the graphics hardware (but also see
        get_transform_blend_table()).

        This will return NULL if the vertex data does not have a TransformTable
        assigned (which implies the vertices will not be animated by the graphics
        hardware).
        """
    def set_transform_table(self, table: TransformTable) -> None:
        """Replaces the TransformTable on this vertex data with the indicated table.
        The length of this table should be consistent with the maximum table index
        assigned to the vertices under the "transform_index" name.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def clear_transform_table(self) -> None:
        """Sets the TransformTable pointer to NULL, removing the table from the vertex
        data.  This disables hardware-driven vertex animation.
        """
    def get_transform_blend_table(self) -> TransformBlendTable:
        """Returns a const pointer to the TransformBlendTable assigned to this data.
        Vertices within the table will index into this table to indicate their
        dynamic skinning information; this table is used when the vertex animation
        is to be performed by the CPU (but also see get_transform_table()).

        This will return NULL if the vertex data does not have a
        TransformBlendTable assigned (which implies the vertices will not be
        animated by the CPU).
        """
    def modify_transform_blend_table(self) -> TransformBlendTable:
        """Returns a modifiable pointer to the current TransformBlendTable on this
        vertex data, if any, or NULL if there is not a TransformBlendTable.  See
        get_transform_blend_table().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def set_transform_blend_table(self, table: TransformBlendTable) -> None:
        """Replaces the TransformBlendTable on this vertex data with the indicated
        table.  The length of this table should be consistent with the maximum
        table index assigned to the vertices under the "transform_blend" name.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def clear_transform_blend_table(self) -> None:
        """Sets the TransformBlendTable pointer to NULL, removing the table from the
        vertex data.  This disables CPU-driven vertex animation.
        """
    def get_slider_table(self) -> SliderTable:
        """Returns a const pointer to the SliderTable assigned to this data.  Vertices
        within the vertex data will look up their morph offsets, if any, within
        this table.

        This will return NULL if the vertex data does not have a SliderTable
        assigned.
        """
    def set_slider_table(self, table: SliderTable) -> None:
        """Replaces the SliderTable on this vertex data with the indicated table.
        There should be an entry in this table for each kind of morph offset
        defined in the vertex data.

        The SliderTable object must have been registered prior to setting it on the
        GeomVertexData.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def clear_slider_table(self) -> None:
        """Sets the SliderTable pointer to NULL, removing the table from the vertex
        data.  This disables morph (blend shape) animation.
        """
    def get_num_bytes(self) -> int:
        """Returns the total number of bytes consumed by the different arrays of the
        vertex data.
        """
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the vertex data is modified.
        """
    def request_resident(self) -> bool:
        """Returns true if the vertex data is currently resident in memory.  If this
        returns false, the vertex data will be brought back into memory shortly;
        try again later.
        """
    def copy_from(self, source: GeomVertexData, keep_data_objects: bool, current_thread: Thread = ...) -> None:
        """Copies all the data from the other array into the corresponding data types
        in this array, by matching data types name-by-name.

        keep_data_objects specifies what to do when one or more of the arrays can
        be copied without the need to apply any conversion operation.  If it is
        true, the original GeomVertexArrayData objects in this object are retained,
        and their data arrays are copied byte-by-byte from the source; if it is
        false, then the GeomVertexArrayData objects are copied pointerwise from the
        source.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def copy_row_from(self, dest_row: int, source: GeomVertexData, source_row: int, current_thread: Thread) -> None:
        """Copies a single row of the data from the other array into the indicated row
        of this array.  In this case, the source format must exactly match the
        destination format.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def convert_to(self, new_format: GeomVertexArrayFormat | GeomVertexFormat) -> GeomVertexData:
        """Returns a new GeomVertexData that represents the same contents as this one,
        with all data types matched up name-by-name to the indicated new format.
        """
    @overload
    def scale_color(self, color_scale: Vec4Like) -> GeomVertexData:
        """`(self, color_scale: LVecBase4)`:
        Returns a new GeomVertexData object with the color table modified in-place
        to apply the indicated scale.

        If the vertex data does not include a color column, a new one will not be
        added.

        `(self, color_scale: LVecBase4, num_components: int, numeric_type: _GeomEnums_NumericType, contents: _GeomEnums_Contents)`:
        Returns a new GeomVertexData object with the color table replaced with a
        new color table that has been scaled by the indicated value.  The new color
        table will be added as a new array; if the old color table was interleaved
        with a previous array, the previous array will not be repacked.
        """
    @overload
    def scale_color(
        self, color_scale: Vec4Like, num_components: int, numeric_type: _GeomEnums_NumericType, contents: _GeomEnums_Contents
    ) -> GeomVertexData: ...
    @overload
    def set_color(self, color: Vec4Like) -> GeomVertexData:
        """`(self, color: LColor)`:
        Returns a new GeomVertexData object with the color data modified in-place
        with the new value.

        If the vertex data does not include a color column, a new one will not be
        added.

        `(self, color: LColor, num_components: int, numeric_type: _GeomEnums_NumericType, contents: _GeomEnums_Contents)`:
        Returns a new GeomVertexData object with the color table replaced with a
        new color table for which each vertex has the indicated value.  The new
        color table will be added as a new array; if the old color table was
        interleaved with a previous array, the previous array will not be repacked.
        """
    @overload
    def set_color(
        self, color: Vec4Like, num_components: int, numeric_type: _GeomEnums_NumericType, contents: _GeomEnums_Contents
    ) -> GeomVertexData: ...
    def reverse_normals(self) -> GeomVertexData:
        """Returns a new GeomVertexData object with the normal data modified in-place,
        so that each lighting normal is now facing in the opposite direction.

        If the vertex data does not include a normal column, this returns the
        original GeomVertexData object, unchanged.
        """
    def animate_vertices(self, force: bool, current_thread: Thread) -> GeomVertexData:
        """Returns a GeomVertexData that represents the results of computing the
        vertex animation on the CPU for this GeomVertexData.

        If there is no CPU-defined vertex animation on this object, this just
        returns the original object.

        If there is vertex animation, but the VertexTransform values have not
        changed since last time, this may return the same pointer it returned
        previously.  Even if the VertexTransform values have changed, it may still
        return the same pointer, but with its contents modified (this is preferred,
        since it allows the graphics backend to update vertex buffers optimally).

        If force is false, this method may return immediately with stale data, if
        the vertex data is not completely resident.  If force is true, this method
        will never return stale data, but may block until the data is available.
        """
    def clear_animated_vertices(self) -> None:
        """Removes the cache of animated vertices computed by a previous call to
        animate_vertices() within the same frame.  This will force the next call to
        animate_vertices() to recompute these values from scratch.  Normally it is
        not necessary to call this.
        """
    @overload
    def transform_vertices(self, mat: Mat4Like, rows: BitArray | SparseArray = ...) -> None:
        """`(self, mat: LMatrix4)`:
        Applies the indicated transform matrix to all of the vertices in the
        GeomVertexData.  The transform is applied to all "point" and "vector" type
        columns described in the format.

        `(self, mat: LMatrix4, rows: SparseArray)`:
        Applies the indicated transform matrix to all of the vertices mentioned in
        the sparse array.  The transform is applied to all "point" and "vector"
        type columns described in the format.

        `(self, mat: LMatrix4, begin_row: int, end_row: int)`:
        Applies the indicated transform matrix to all of the vertices from
        begin_row up to but not including end_row.  The transform is applied to all
        "point" and "vector" type columns described in the format.
        """
    @overload
    def transform_vertices(self, mat: Mat4Like, begin_row: int, end_row: int) -> None: ...
    def replace_column(
        self, name: InternalName | str, num_components: int, numeric_type: _GeomEnums_NumericType, contents: _GeomEnums_Contents
    ) -> GeomVertexData:
        """Returns a new GeomVertexData object, suitable for modification, with the
        indicated data type replaced with a new table filled with undefined values.
        The new table will be added as a new array; if the old table was
        interleaved with a previous array, the previous array will not be repacked.

        If num_components is 0, the indicated name is simply removed from the type,
        without replacing it with anything else.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def describe_vertex(self, out: ostream, row: int) -> None:
        """Writes a verbose, human-friendly description of the indicated vertex
        number.
        """
    def clear_cache(self) -> None:
        """Removes all of the previously-cached results of convert_to().

        This blows away the entire cache, upstream and downstream the pipeline.
        Use clear_cache_stage() instead if you only want to blow away the cache at
        the current stage and upstream.
        """
    def clear_cache_stage(self) -> None:
        """Removes all of the previously-cached results of convert_to(), at the
        current pipeline stage and upstream.  Does not affect the downstream cache.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_arrays(self) -> tuple[GeomVertexArrayData, ...]: ...
    upcastToCopyOnWriteObject = upcast_to_CopyOnWriteObject
    upcastToGeomEnums = upcast_to_GeomEnums
    compareTo = compare_to
    getName = get_name
    setName = set_name
    getUsageHint = get_usage_hint
    setUsageHint = set_usage_hint
    getFormat = get_format
    setFormat = set_format
    uncleanSetFormat = unclean_set_format
    hasColumn = has_column
    getNumRows = get_num_rows
    setNumRows = set_num_rows
    uncleanSetNumRows = unclean_set_num_rows
    reserveNumRows = reserve_num_rows
    clearRows = clear_rows
    getNumArrays = get_num_arrays
    getArray = get_array
    getArrayHandle = get_array_handle
    modifyArray = modify_array
    modifyArrayHandle = modify_array_handle
    setArray = set_array
    getTransformTable = get_transform_table
    setTransformTable = set_transform_table
    clearTransformTable = clear_transform_table
    getTransformBlendTable = get_transform_blend_table
    modifyTransformBlendTable = modify_transform_blend_table
    setTransformBlendTable = set_transform_blend_table
    clearTransformBlendTable = clear_transform_blend_table
    getSliderTable = get_slider_table
    setSliderTable = set_slider_table
    clearSliderTable = clear_slider_table
    getNumBytes = get_num_bytes
    getModified = get_modified
    requestResident = request_resident
    copyFrom = copy_from
    copyRowFrom = copy_row_from
    convertTo = convert_to
    scaleColor = scale_color
    setColor = set_color
    reverseNormals = reverse_normals
    animateVertices = animate_vertices
    clearAnimatedVertices = clear_animated_vertices
    transformVertices = transform_vertices
    replaceColumn = replace_column
    describeVertex = describe_vertex
    clearCache = clear_cache
    clearCacheStage = clear_cache_stage
    getArrays = get_arrays

class AnimateVerticesRequest(AsyncTask):
    """This class object manages a single asynchronous request to animate vertices
    on a GeomVertexData object.  animate_vertices will be called with
    force=true (i.e.  blocking) in a sub-thread (if threading is available).
    No result is stored or returned from this object.  It is expected that the
    result will be cached and available for immediate use later during
    rendering.  Thus it is important that the main thread block while these
    requests are being run (presumably on multiple CPUs/cores), to ensure that
    the data has been computed by the time it's needed.
    """

    @overload
    def __init__(self, __param0: AnimateVerticesRequest) -> None:
        """Create a new AnimateVerticesRequest."""
    @overload
    def __init__(self, geom_vertex_data: GeomVertexData) -> None: ...
    def is_ready(self) -> bool:
        """Returns true if this request has completed, false if it is still pending.
        Equivalent to `req.done() and not req.cancelled()`.
        @see done()
        """
    isReady = is_ready

class SavedContext(TypedObject):
    """This is the base class for all GSG-specific context objects, such as
    TextureContext and GeomContext.  It exists mainly to provide some
    structural organization.
    """

class BufferContext(SavedContext):
    """This is a base class for those kinds of SavedContexts that occupy an
    easily-measured (and substantial) number of bytes in the video card's frame
    buffer memory or AGP memory.  At the present, this includes most of the
    SavedContext types: VertexBufferContext and IndexBufferContext, as well as
    TextureContext.

    This class provides methods for tracking the video memory utilization, as
    well as residency of each object, via PStats.
    """

    @property
    def object(self) -> TypedWritableReferenceCount: ...
    @property
    def data_size_bytes(self) -> int: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @property
    def active(self) -> bool: ...
    @property
    def resident(self) -> bool: ...
    def upcast_to_SavedContext(self) -> SavedContext: ...
    def get_data_size_bytes(self) -> int:
        """Returns the number of bytes previously reported for the data object.  This
        is used to track changes in the data object's allocated size; if it changes
        from this, we need to create a new buffer.  This is also used to track
        memory utilization in PStats.
        """
    def get_modified(self) -> UpdateSeq:
        """Returns the UpdateSeq that was recorded the last time mark_loaded() was
        called.
        """
    def get_active(self) -> bool:
        """Returns the active flag associated with this object.  An object is
        considered "active" if it was rendered in the current frame.
        """
    def get_resident(self) -> bool:
        """Returns the resident flag associated with this object.  An object is
        considered "resident" if it appears to be resident in texture memory.
        """
    upcastToSavedContext = upcast_to_SavedContext
    getDataSizeBytes = get_data_size_bytes
    getModified = get_modified
    getActive = get_active
    getResident = get_resident

class GeomPrimitive(CopyOnWriteObject, GeomEnums):
    """This is an abstract base class for a family of classes that represent the
    fundamental geometry primitives that may be stored in a Geom.

    They all have in common the fact that they are defined by tables of vertex
    data stored in a GeomVertexData object.  Each GeomPrimitive object contains
    an ordered list of integers, which index into the vertex array defined by
    the GeomVertexData and define the particular vertices of the GeomVertexData
    that are used for this primitive.

    The meaning of a given arrangement of vertices is defined by each
    individual primitive type; for instance, a GeomTriangle renders a triangle
    from each three consecutive vertices, while a GeomTriangleStrip renders a
    strip of (n - 2) connected triangles from each sequence of n vertices.
    """

    @property
    def primitive_type(self) -> _GeomEnums_PrimitiveType: ...
    @property
    def geom_rendering(self) -> int: ...
    @property
    def shade_model(self) -> _GeomEnums_ShadeModel: ...
    @property
    def usage_hint(self) -> _GeomEnums_UsageHint: ...
    @property
    def index_type(self) -> _GeomEnums_NumericType: ...
    @property
    def num_bytes(self) -> int: ...
    @property
    def data_size_bytes(self) -> int: ...
    @property
    def modified(self) -> UpdateSeq: ...
    @property
    def index_stride(self) -> int: ...
    @property
    def strip_cut_index(self) -> int: ...
    @property
    def mins(self) -> GeomVertexArrayData: ...
    @property
    def maxs(self) -> GeomVertexArrayData: ...
    @property
    def num_vertices_per_primitive(self) -> int: ...
    @property
    def min_num_vertices_per_primitive(self) -> int: ...
    @property
    def num_unused_vertices_per_primitive(self) -> int: ...
    def upcast_to_CopyOnWriteObject(self) -> CopyOnWriteObject: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def assign(self, copy: Self) -> Self: ...
    def make_copy(self) -> GeomPrimitive: ...
    def get_primitive_type(self) -> _GeomEnums_PrimitiveType: ...
    def get_geom_rendering(self) -> int:
        """Returns the set of GeomRendering bits that represent the rendering
        properties required to properly render this primitive.
        """
    def get_shade_model(self) -> _GeomEnums_ShadeModel:
        """Returns the ShadeModel hint for this primitive.  This is intended as a hint
        to the renderer to tell it how the per-vertex colors and normals are
        applied.
        """
    def set_shade_model(self, shade_model: _GeomEnums_ShadeModel) -> None:
        """Changes the ShadeModel hint for this primitive.  This is different from the
        ShadeModelAttrib that might also be applied from the scene graph.  This
        does not affect the shade model that is in effect when rendering, but
        rather serves as a hint to the renderer to tell it how the per-vertex
        colors and normals on this primitive are applied.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the usage hint for this primitive.  See geomEnums.h.  This has
        nothing to do with the usage hint associated with the primitive's vertices;
        this only specifies how often the vertex indices that define the primitive
        will be modified.

        It is perfectly legal (and, in fact, common) for a GeomPrimitive to have
        UH_static on itself, while referencing vertex data with UH_dynamic.  This
        means that the vertices themselves will be animated, but the primitive will
        always reference the same set of vertices from the pool.
        """
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None:
        """Changes the UsageHint hint for this primitive.  See get_usage_hint().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_index_type(self) -> _GeomEnums_NumericType:
        """Returns the numeric type of the index column.  Normally, this will be
        either NT_uint16 or NT_uint32.
        """
    def set_index_type(self, index_type: _GeomEnums_NumericType) -> None:
        """Changes the numeric type of the index column.  Normally, this should be
        either NT_uint16 or NT_uint32.

        The index type must be large enough to include all of the index values in
        the primitive.  It may be automatically elevated, if necessary, to a larger
        index type, by a subsequent call to add_index() that names an index value
        that does not fit in the index type you specify.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def is_composite(self) -> bool:
        """Returns true if the primitive is a composite primitive such as a tristrip
        or trifan, or false if it is a fundamental primitive such as a collection
        of triangles.
        """
    def is_indexed(self) -> bool:
        """Returns true if the primitive is indexed, false otherwise.  An indexed
        primitive stores a table of index numbers into its GeomVertexData, so that
        it can reference the vertices in any order.  A nonindexed primitive, on the
        other hand, stores only the first vertex number and number of vertices
        used, so that it can only reference the vertices consecutively.
        """
    def get_first_vertex(self) -> int:
        """Returns the first vertex number referenced by the primitive.  This is
        particularly important in the case of a nonindexed primitive, in which case
        get_first_vertex() and get_num_vertices() completely define the extent of
        the vertex range.
        """
    def get_num_vertices(self) -> int:
        """Returns the number of indices used by all the primitives in this object."""
    def get_vertex(self, i: int) -> int:
        """Returns the ith vertex index in the table."""
    def add_vertex(self, vertex: int) -> None:
        """Adds the indicated vertex to the list of vertex indices used by the
        graphics primitive type.  To define a primitive, you must call add_vertex()
        for each vertex of the new primitive, and then call close_primitive() after
        you have specified the last vertex of each primitive.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    @overload
    def add_vertices(self, v1: int, v2: int, v3: int = ...) -> None:
        """Adds several vertices in a row."""
    @overload
    def add_vertices(self, v1: int, v2: int, v3: int, v4: int) -> None: ...
    def add_consecutive_vertices(self, start: int, num_vertices: int) -> None:
        """Adds a consecutive sequence of vertices, beginning at start, to the
        primitive.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def add_next_vertices(self, num_vertices: int) -> None:
        """Adds the next n vertices in sequence, beginning from the last vertex added
        to the primitive + 1.

        This is most useful when you are building up a primitive and a
        GeomVertexData at the same time, and you just want the primitive to
        reference the first n vertices from the data, then the next n, and so on.
        """
    def reserve_num_vertices(self, num_vertices: int) -> None:
        """This ensures that enough memory space for n vertices is allocated, so that
        you may increase the number of vertices to n without causing a new memory
        allocation.  This is a performance optimization only; it is especially
        useful when you know ahead of time that you will be adding n vertices to
        the primitive.

        Note that the total you specify here should also include implicit vertices
        which may be added at each close_primitive() call, according to
        get_num_unused_vertices_per_primitive().

        Note also that making this call will implicitly make the primitive indexed
        if it is not already, which could result in a performance *penalty*.  If
        you would prefer not to lose the nonindexed nature of your existing
        GeomPrimitives, check is_indexed() before making this call.
        """
    def close_primitive(self) -> bool:
        """Indicates that the previous n calls to add_vertex(), since the last call to
        close_primitive(), have fully defined a new primitive.  Returns true if
        successful, false otherwise.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def clear_vertices(self) -> None:
        """Removes all of the vertices and primitives from the object, so they can be
        re-added.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    @overload
    def offset_vertices(self, offset: int) -> None:
        """`(self, offset: int)`:
        Adds the indicated offset to all vertices used by the primitive.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        `(self, offset: int, begin_row: int, end_row: int)`:
        Adds the indicated offset to the indicated segment of vertices used by the
        primitive.  Unlike the other version of offset_vertices, this makes the
        geometry indexed if it isn't already.

        Note that end_row indicates one past the last row that should be offset.
        In other words, the number of vertices touched is (end_row - begin_row).

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    @overload
    def offset_vertices(self, offset: int, begin_row: int, end_row: int) -> None: ...
    def make_nonindexed(self, dest: GeomVertexData, source: GeomVertexData) -> None:
        """Converts the primitive from indexed to nonindexed by duplicating vertices
        as necessary into the indicated dest GeomVertexData.  Note: does not
        support primitives with strip cut indices.
        """
    def pack_vertices(self, dest: GeomVertexData, source: GeomVertexData) -> None:
        """Packs the vertices used by the primitive from the indicated source array
        onto the end of the indicated destination array.
        """
    def make_indexed(self) -> None:
        """Converts the primitive from nonindexed form to indexed form.  This will
        simply create an index table that is numbered consecutively from
        get_first_vertex(); it does not automatically collapse together identical
        vertices that may have been split apart by a previous call to
        make_nonindexed().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_num_primitives(self) -> int:
        """Returns the number of individual primitives stored within this object.  All
        primitives are the same type.
        """
    def get_primitive_start(self, n: int) -> int:
        """Returns the element within the _vertices list at which the nth primitive
        starts.

        If i is one more than the highest valid primitive vertex, the return value
        will be one more than the last valid vertex.  Thus, it is generally true
        that the vertices used by a particular primitive i are the set
        get_primitive_start(n) <= vi < get_primitive_start(n + 1) (although this
        range also includes the unused vertices between primitives).
        """
    def get_primitive_end(self, n: int) -> int:
        """Returns the element within the _vertices list at which the nth primitive
        ends.  This is one past the last valid element for the nth primitive.
        """
    def get_primitive_num_vertices(self, n: int) -> int:
        """Returns the number of vertices used by the nth primitive.  This is the same
        thing as get_primitive_end(n) - get_primitive_start(n).
        """
    def get_num_used_vertices(self) -> int:
        """Returns the number of vertices used by all of the primitives.  This is the
        same as summing get_primitive_num_vertices(n) for n in
        get_num_primitives().  It is like get_num_vertices except that it excludes
        all of the degenerate vertices and strip-cut indices.
        """
    def get_num_faces(self) -> int:
        """Returns the number of triangles or other fundamental type (such as line
        segments) represented by all the primitives in this object.
        """
    def get_primitive_num_faces(self, n: int) -> int:
        """Returns the number of triangles or other fundamental type (such as line
        segments) represented by the nth primitive in this object.
        """
    def get_min_vertex(self) -> int:
        """Returns the minimum vertex index number used by all the primitives in this
        object.
        """
    def get_primitive_min_vertex(self, n: int) -> int:
        """Returns the minimum vertex index number used by the nth primitive in this
        object.
        """
    def get_max_vertex(self) -> int:
        """Returns the maximum vertex index number used by all the primitives in this
        object.
        """
    def get_primitive_max_vertex(self, n: int) -> int:
        """Returns the maximum vertex index number used by the nth primitive in this
        object.
        """
    def decompose(self) -> GeomPrimitive:
        """Decomposes a complex primitive type into a simpler primitive type, for
        instance triangle strips to triangles, and returns a pointer to the new
        primitive definition.  If the decomposition cannot be performed, this might
        return the original object.

        This method is useful for application code that wants to iterate through
        the set of triangles on the primitive without having to write handlers for
        each possible kind of primitive type.
        """
    def rotate(self) -> GeomPrimitive:
        """Returns a new primitive with the shade_model reversed (if it is flat
        shaded), if possible.  If the primitive type cannot be rotated, returns the
        original primitive, unrotated.

        If the current shade_model indicates flat_vertex_last, this should bring
        the last vertex to the first position; if it indicates flat_vertex_first,
        this should bring the first vertex to the last position.
        """
    def doubleside(self) -> GeomPrimitive:
        """Duplicates triangles in the primitive so that each triangle is back-to-back
        with another triangle facing in the opposite direction.  Note that this
        doesn't affect vertex normals, so this operation alone won't work in the
        presence of lighting (but see SceneGraphReducer::doubleside()).

        Also see CullFaceAttrib, which can enable rendering of both sides of a
        triangle without having to duplicate it (but which doesn't necessarily work
        in the presence of lighting).
        """
    def reverse(self) -> GeomPrimitive:
        """Reverses the winding order in the primitive so that each triangle is facing
        in the opposite direction it was originally.  Note that this doesn't affect
        vertex normals, so this operation alone won't work in the presence of
        lighting (but see SceneGraphReducer::reverse()).

        Also see CullFaceAttrib, which can change the visible direction of a
        triangle without having to duplicate it (but which doesn't necessarily work
        in the presence of lighting).
        """
    def match_shade_model(self, shade_model: _GeomEnums_ShadeModel) -> GeomPrimitive:
        """Returns a new primitive that is compatible with the indicated shade model,
        if possible, or NULL if this is not possible.

        In most cases, this will return either NULL or the original primitive.  In
        the case of a SM_flat_first_vertex vs.  a SM_flat_last_vertex (or vice-
        versa), however, it will return a rotated primitive.
        """
    def make_points(self) -> GeomPrimitive:
        """Returns a new GeomPoints primitive that represents each of the vertices in
        the original primitive, rendered exactly once.  If the original primitive
        is already a GeomPoints primitive, returns the original primitive
        unchanged.
        """
    def make_lines(self) -> GeomPrimitive:
        """Returns a new GeomLines primitive that represents each of the edges in the
        original primitive rendered as a line.  If the original primitive is
        already a GeomLines primitive, returns the original primitive unchanged.
        """
    def make_patches(self) -> GeomPrimitive:
        """Decomposes a complex primitive type into a simpler primitive type, for
        instance triangle strips to triangles, puts these in a new GeomPatches
        object and returns a pointer to the new primitive definition.  If the
        decomposition cannot be performed, this might return the original object.

        This method is useful for application code that wants to use tesselation
        shaders on arbitrary geometry.
        """
    def make_adjacency(self) -> GeomPrimitive:
        """Adds adjacency information to this primitive.  May return null if this type
        of geometry does not support adjacency information.

        @since 1.10.0
        """
    def get_num_bytes(self) -> int:
        """Returns the number of bytes consumed by the primitive and its index
        table(s).
        """
    def get_data_size_bytes(self) -> int:
        """Returns the number of bytes stored in the vertices array."""
    def get_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the vertex index array is modified.
        """
    def request_resident(self, current_thread: Thread = ...) -> bool:
        """Returns true if the primitive data is currently resident in memory.  If
        this returns false, the primitive data will be brought back into memory
        shortly; try again later.
        """
    def check_valid(self, vertex_data: GeomVertexData) -> bool:
        """Verifies that the primitive only references vertices that actually exist
        within the indicated GeomVertexData.  Returns true if the primitive appears
        to be valid, false otherwise.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def get_vertices(self) -> GeomVertexArrayData:
        """Returns a const pointer to the vertex index array so application code can
        read it directly.  This might return NULL if the primitive is nonindexed.
        Do not attempt to modify the returned array; use modify_vertices() or
        set_vertices() for this.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_vertices_handle(self, current_thread: Thread) -> GeomVertexArrayDataHandle:
        """Equivalent to get_vertices().get_handle()."""
    def modify_vertices(self, num_vertices: int = ...) -> GeomVertexArrayData:
        """Returns a modifiable pointer to the vertex index list, so application code
        can directly fiddle with this data.  Use with caution, since there are no
        checks that the data will be left in a stable state.

        If this is called on a nonindexed primitive, it will implicitly be
        converted to an indexed primitive.

        If num_vertices is not -1, it specifies an artificial limit to the number
        of vertices in the array.  Otherwise, all of the vertices in the array will
        be used.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def modify_vertices_handle(self, current_thread: Thread) -> GeomVertexArrayDataHandle:
        """Equivalent to modify_vertices().get_handle()."""
    def set_vertices(self, vertices: GeomVertexArrayData, num_vertices: int = ...) -> None:
        """Completely replaces the vertex index list with a new table.  Chances are
        good that you should also replace the ends list with set_ends() at the same
        time.

        If num_vertices is not -1, it specifies an artificial limit to the number
        of vertices in the array.  Otherwise, all of the vertices in the array will
        be used.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def set_nonindexed_vertices(self, first_vertex: int, num_vertices: int) -> None:
        """Sets the primitive up as a nonindexed primitive, using the indicated vertex
        range.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_index_stride(self) -> int:
        """A convenience function to return the gap between successive index numbers,
        in bytes, of the index data.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_strip_cut_index(self) -> int:
        """If relevant, returns the index value that may be used in some cases to
        signify the end of a primitive.  This is typically the highest value that
        the numeric type can store.
        """
    def get_ends(self) -> CPTA_int:
        """Returns a const pointer to the primitive ends array so application code can
        read it directly.  Do not attempt to modify the returned array; use
        modify_ends() or set_ends() for this.

        Note that simple primitive types, like triangles, do not have a ends array:
        since all the primitives have the same number of vertices, it is not
        needed.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def modify_ends(self) -> PTA_int:
        """Returns a modifiable pointer to the primitive ends array, so application
        code can directly fiddle with this data.  Use with caution, since there are
        no checks that the data will be left in a stable state.

        Note that simple primitive types, like triangles, do not have a ends array:
        since all the primitives have the same number of vertices, it is not
        needed.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def set_ends(self, ends: PTA_int) -> None:
        """Completely replaces the primitive ends array with a new table.  Chances are
        good that you should also replace the vertices list with set_vertices() at
        the same time.

        Note that simple primitive types, like triangles, do not have a ends array:
        since all the primitives have the same number of vertices, it is not
        needed.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_mins(self) -> GeomVertexArrayData:
        """Returns a const pointer to the primitive mins array so application code can
        read it directly.  Do not attempt to modify the returned array; use
        set_minmax() for this.

        Note that simple primitive types, like triangles, do not have a mins array.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_maxs(self) -> GeomVertexArrayData:
        """Returns a const pointer to the primitive maxs array so application code can
        read it directly.  Do not attempt to modify the returned array; use
        set_minmax().

        Note that simple primitive types, like triangles, do not have a maxs array.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def set_minmax(self, min_vertex: int, max_vertex: int, mins: GeomVertexArrayData, maxs: GeomVertexArrayData) -> None:
        """Explicitly specifies the minimum and maximum vertices, as well as the lists
        of per-component min and max.

        Use this method with extreme caution.  It's generally better to let the
        GeomPrimitive compute these explicitly, unless for some reason you can do
        it faster and you absolutely need the speed improvement.

        Note that any modification to the vertex array will normally cause this to
        be recomputed, unless you set it immediately again.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def clear_minmax(self) -> None:
        """Undoes a previous call to set_minmax(), and allows the minimum and maximum
        values to be recomputed normally.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_num_vertices_per_primitive(self) -> int:
        """If the primitive type is a simple type in which all primitives have the
        same number of vertices, like triangles, returns the number of vertices per
        primitive.  If the primitive type is a more complex type in which different
        primitives might have different numbers of vertices, for instance a
        triangle strip, returns 0.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_min_num_vertices_per_primitive(self) -> int:
        """Returns the minimum number of vertices that must be added before
        close_primitive() may legally be called.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_num_unused_vertices_per_primitive(self) -> int:
        """Returns the number of vertices that are added between primitives that
        aren't, strictly speaking, part of the primitives themselves.  This is
        used, for instance, to define degenerate triangles to connect otherwise
        disconnected triangle strips.

        This method is intended for low-level usage only.  There are higher-level
        methods for more common usage.  We recommend you do not use this method
        directly.  If you do, be sure you know what you are doing!
        """
    def get_vertex_list(self) -> tuple[int, ...]: ...
    upcastToCopyOnWriteObject = upcast_to_CopyOnWriteObject
    upcastToGeomEnums = upcast_to_GeomEnums
    makeCopy = make_copy
    getPrimitiveType = get_primitive_type
    getGeomRendering = get_geom_rendering
    getShadeModel = get_shade_model
    setShadeModel = set_shade_model
    getUsageHint = get_usage_hint
    setUsageHint = set_usage_hint
    getIndexType = get_index_type
    setIndexType = set_index_type
    isComposite = is_composite
    isIndexed = is_indexed
    getFirstVertex = get_first_vertex
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    addVertex = add_vertex
    addVertices = add_vertices
    addConsecutiveVertices = add_consecutive_vertices
    addNextVertices = add_next_vertices
    reserveNumVertices = reserve_num_vertices
    closePrimitive = close_primitive
    clearVertices = clear_vertices
    offsetVertices = offset_vertices
    makeNonindexed = make_nonindexed
    packVertices = pack_vertices
    makeIndexed = make_indexed
    getNumPrimitives = get_num_primitives
    getPrimitiveStart = get_primitive_start
    getPrimitiveEnd = get_primitive_end
    getPrimitiveNumVertices = get_primitive_num_vertices
    getNumUsedVertices = get_num_used_vertices
    getNumFaces = get_num_faces
    getPrimitiveNumFaces = get_primitive_num_faces
    getMinVertex = get_min_vertex
    getPrimitiveMinVertex = get_primitive_min_vertex
    getMaxVertex = get_max_vertex
    getPrimitiveMaxVertex = get_primitive_max_vertex
    matchShadeModel = match_shade_model
    makePoints = make_points
    makeLines = make_lines
    makePatches = make_patches
    makeAdjacency = make_adjacency
    getNumBytes = get_num_bytes
    getDataSizeBytes = get_data_size_bytes
    getModified = get_modified
    requestResident = request_resident
    checkValid = check_valid
    getVertices = get_vertices
    getVerticesHandle = get_vertices_handle
    modifyVertices = modify_vertices
    modifyVerticesHandle = modify_vertices_handle
    setVertices = set_vertices
    setNonindexedVertices = set_nonindexed_vertices
    getIndexStride = get_index_stride
    getStripCutIndex = get_strip_cut_index
    getEnds = get_ends
    modifyEnds = modify_ends
    setEnds = set_ends
    getMins = get_mins
    getMaxs = get_maxs
    setMinmax = set_minmax
    clearMinmax = clear_minmax
    getNumVerticesPerPrimitive = get_num_vertices_per_primitive
    getMinNumVerticesPerPrimitive = get_min_num_vertices_per_primitive
    getNumUnusedVerticesPerPrimitive = get_num_unused_vertices_per_primitive
    getVertexList = get_vertex_list

class TextureStage(TypedWritableReferenceCount):
    """Defines the properties of a named stage of the multitexture pipeline.  The
    TextureAttrib will associated a number of these stages with Texture
    objects, and the GSG will render geometry by sorting all of the currently
    active TextureStages in order and then issuing the appropriate rendering
    calls to activate them.
    """

    M_modulate: Final = 0
    MModulate: Final = 0
    M_decal: Final = 1
    MDecal: Final = 1
    M_blend: Final = 2
    MBlend: Final = 2
    M_replace: Final = 3
    MReplace: Final = 3
    M_add: Final = 4
    MAdd: Final = 4
    M_combine: Final = 5
    MCombine: Final = 5
    M_blend_color_scale: Final = 6
    MBlendColorScale: Final = 6
    M_modulate_glow: Final = 7
    MModulateGlow: Final = 7
    M_modulate_gloss: Final = 8
    MModulateGloss: Final = 8
    M_normal: Final = 9
    MNormal: Final = 9
    M_normal_height: Final = 10
    MNormalHeight: Final = 10
    M_glow: Final = 11
    MGlow: Final = 11
    M_gloss: Final = 12
    MGloss: Final = 12
    M_height: Final = 13
    MHeight: Final = 13
    M_selector: Final = 14
    MSelector: Final = 14
    M_normal_gloss: Final = 15
    MNormalGloss: Final = 15
    M_emission: Final = 16
    MEmission: Final = 16
    CM_undefined: Final = 0
    CMUndefined: Final = 0
    CM_replace: Final = 1
    CMReplace: Final = 1
    CM_modulate: Final = 2
    CMModulate: Final = 2
    CM_add: Final = 3
    CMAdd: Final = 3
    CM_add_signed: Final = 4
    CMAddSigned: Final = 4
    CM_interpolate: Final = 5
    CMInterpolate: Final = 5
    CM_subtract: Final = 6
    CMSubtract: Final = 6
    CM_dot3_rgb: Final = 7
    CMDot3Rgb: Final = 7
    CM_dot3_rgba: Final = 8
    CMDot3Rgba: Final = 8
    CS_undefined: Final = 0
    CSUndefined: Final = 0
    CS_texture: Final = 1
    CSTexture: Final = 1
    CS_constant: Final = 2
    CSConstant: Final = 2
    CS_primary_color: Final = 3
    CSPrimaryColor: Final = 3
    CS_previous: Final = 4
    CSPrevious: Final = 4
    CS_constant_color_scale: Final = 5
    CSConstantColorScale: Final = 5
    CS_last_saved_result: Final = 6
    CSLastSavedResult: Final = 6
    CO_undefined: Final = 0
    COUndefined: Final = 0
    CO_src_color: Final = 1
    COSrcColor: Final = 1
    CO_one_minus_src_color: Final = 2
    COOneMinusSrcColor: Final = 2
    CO_src_alpha: Final = 3
    COSrcAlpha: Final = 3
    CO_one_minus_src_alpha: Final = 4
    COOneMinusSrcAlpha: Final = 4
    name: str
    sort: int
    priority: int
    texcoord_name: InternalName
    mode: _TextureStage_Mode
    color: LColor
    rgb_scale: int
    alpha_scale: int
    saved_result: bool
    tex_view_offset: int
    @property
    def tangent_name(self) -> InternalName: ...
    @property
    def binormal_name(self) -> InternalName: ...
    @property
    def default(self) -> TextureStage: ...
    @overload
    def __init__(self, copy: TextureStage) -> None:
        """`(self, copy: TextureStage)`:
        Initialize the texture stage from other

        `(self, name: str)`:
        Initialize the texture stage at construction
        """
    @overload
    def __init__(self, name: str) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: TextureStage) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def set_name(self, name: str) -> None:
        """Changes the name of this texture stage"""
    def get_name(self) -> str:
        """Returns the name of this texture stage"""
    def set_sort(self, sort: int) -> None:
        """Changes the order in which the texture associated with this stage is
        rendered relative to the other texture stages.  When geometry is rendered
        with multiple textures, the textures are rendered in order from the lowest
        sort number to the highest sort number.

        Also see set_priority(), which is used to select the most important
        textures for rendering when some must be omitted because of hardware
        limitations.
        """
    def get_sort(self) -> int:
        """Returns the sort order of this texture stage."""
    def set_priority(self, priority: int) -> None:
        """Changes the relative importance of the texture associated with this stage
        relative to the other texture stages that are applied simultaneously.

        This is unrelated to set_sort(), which controls the order in which multiple
        textures are applied.  The priority number is used to decide which of the
        requested textures are to be selected for rendering when more textures are
        requested than the hardware will support.  The highest-priority n textures
        are selected for rendering, and then rendered in order by their sort
        factor.
        """
    def get_priority(self) -> int:
        """Returns the priority associated with this stage.

        This is specially helpful for cards that do not support more than n stages
        of multi-texturing.
        """
    @overload
    def set_texcoord_name(self, name: InternalName) -> None:
        """Indicate which set of UV's this texture stage will use.  Geometry may have
        any number of associated UV sets, each of which must have a unique name.
        """
    @overload
    def set_texcoord_name(self, texcoord_name: str) -> None: ...
    def get_texcoord_name(self) -> InternalName:
        """See set_texcoord_name.  The default is InternalName::get_texcoord()."""
    def get_tangent_name(self) -> InternalName:
        """Returns the set of tangents this texture stage will use.  This is the same
        as get_texcoord_name(), except that the first part is "tangent".
        """
    def get_binormal_name(self) -> InternalName:
        """Returns the set of binormals this texture stage will use.  This is the same
        as get_binormal_name(), except that the first part is "binormal".
        """
    def set_mode(self, mode: _TextureStage_Mode) -> None:
        """Set the mode of this texture stage"""
    def get_mode(self) -> _TextureStage_Mode:
        """Return the mode of this stage"""
    def is_fixed_function(self) -> bool:
        """Returns true if the TextureStage is relevant to the classic fixed function
        pipeline.  This excludes texture stages such as normal mapping and the
        like.
        """
    def set_color(self, color: Vec4Like) -> None:
        """Set the color for this stage"""
    def get_color(self) -> LColor:
        """return the color for this stage"""
    def set_rgb_scale(self, rgb_scale: int) -> None:
        """Sets an additional factor that will scale all three r, g, b components
        after the texture has been applied.  This is used only when the mode is
        CM_combine.

        The only legal values are 1, 2, or 4.
        """
    def get_rgb_scale(self) -> int:
        """See set_rgb_scale()."""
    def set_alpha_scale(self, alpha_scale: int) -> None:
        """Sets an additional factor that will scale the alpha component after the
        texture has been applied.  This is used only when the mode is CM_combine.

        The only legal values are 1, 2, or 4.
        """
    def get_alpha_scale(self) -> int:
        """See set_alpha_scale()."""
    def set_saved_result(self, saved_result: bool) -> None:
        """Sets the saved_result flag.  When this is true, the output of this stage
        will be supplied as the "last_saved_result" source for any future stages,
        until the next TextureStage with a saved_result set true is encountered.

        This can be used to reuse the results of this texture stage as input to
        more than one stage later in the pipeline.

        The last texture in the pipeline (the one with the highest sort value)
        should not have this flag set.
        """
    def get_saved_result(self) -> bool:
        """Returns the current setting of the saved_result flag.  See
        set_saved_result().
        """
    def set_tex_view_offset(self, tex_view_offset: int) -> None:
        """Sets the tex_view_offset value.  This is used only when a special multiview
        texture is bound to the TextureStage, and it selects the particular view of
        the texture that is to be used.

        This value is added to the similar parameter on DisplayRegion to derive the
        final texture view index that is selected for rendering.
        """
    def get_tex_view_offset(self) -> int:
        """Returns the current setting of the tex_view_offset.  See
        set_tex_view_offset().
        """
    @overload
    def set_combine_rgb(
        self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand
    ) -> None:
        """`(self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand)`:
        Specifies any of the CombineMode values that represent a one-parameter
        operation.  Specifically, this is CM_replace only.

        `(self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand, source1: _TextureStage_CombineSource, operand1: _TextureStage_CombineOperand)`:
        Specifies any of the CombineMode values that represent a two-parameter
        operation.  Specifically, this is everything except for CM_replace and
        CM_interpolate.

        `(self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand, source1: _TextureStage_CombineSource, operand1: _TextureStage_CombineOperand, source2: _TextureStage_CombineSource, operand2: _TextureStage_CombineOperand)`:
        Specifies any of the CombineMode values that represent a one-parameter
        operation.  Specifically, this is CM_interpolate only.
        """
    @overload
    def set_combine_rgb(
        self,
        mode: _TextureStage_CombineMode,
        source0: _TextureStage_CombineSource,
        operand0: _TextureStage_CombineOperand,
        source1: _TextureStage_CombineSource,
        operand1: _TextureStage_CombineOperand,
    ) -> None: ...
    @overload
    def set_combine_rgb(
        self,
        mode: _TextureStage_CombineMode,
        source0: _TextureStage_CombineSource,
        operand0: _TextureStage_CombineOperand,
        source1: _TextureStage_CombineSource,
        operand1: _TextureStage_CombineOperand,
        source2: _TextureStage_CombineSource,
        operand2: _TextureStage_CombineOperand,
    ) -> None: ...
    def get_combine_rgb_mode(self) -> _TextureStage_CombineMode:
        """Get the combine_rgb_mode"""
    def get_num_combine_rgb_operands(self) -> int:
        """Returns the number of meaningful operands that may be retrieved via
        get_combine_rgb_sourceN() and get_combine_rgb_operandN().
        """
    def get_combine_rgb_source0(self) -> _TextureStage_CombineSource:
        """Get source0 of combine_rgb_mode"""
    def get_combine_rgb_operand0(self) -> _TextureStage_CombineOperand:
        """Get operand0 of combine_rgb_mode"""
    def get_combine_rgb_source1(self) -> _TextureStage_CombineSource:
        """Get source1 of combine_rgb_mode"""
    def get_combine_rgb_operand1(self) -> _TextureStage_CombineOperand:
        """Get operand1 of combine_rgb_mode"""
    def get_combine_rgb_source2(self) -> _TextureStage_CombineSource:
        """Get source2 of combine_rgb_mode"""
    def get_combine_rgb_operand2(self) -> _TextureStage_CombineOperand:
        """Get operand2 of combine_rgb_mode"""
    @overload
    def set_combine_alpha(
        self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand
    ) -> None:
        """`(self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand)`:
        Specifies any of the CombineMode values that represent a one-parameter
        operation.  Specifically, this is CM_replace only.

        `(self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand, source1: _TextureStage_CombineSource, operand1: _TextureStage_CombineOperand)`:
        Specifies any of the CombineMode values that represent a two-parameter
        operation.  Specifically, this is everything except for CM_replace and
        CM_interpolate.

        `(self, mode: _TextureStage_CombineMode, source0: _TextureStage_CombineSource, operand0: _TextureStage_CombineOperand, source1: _TextureStage_CombineSource, operand1: _TextureStage_CombineOperand, source2: _TextureStage_CombineSource, operand2: _TextureStage_CombineOperand)`:
        Specifies any of the CombineMode values that represent a one-parameter
        operation.  Specifically, this is CM_interpolate only.
        """
    @overload
    def set_combine_alpha(
        self,
        mode: _TextureStage_CombineMode,
        source0: _TextureStage_CombineSource,
        operand0: _TextureStage_CombineOperand,
        source1: _TextureStage_CombineSource,
        operand1: _TextureStage_CombineOperand,
    ) -> None: ...
    @overload
    def set_combine_alpha(
        self,
        mode: _TextureStage_CombineMode,
        source0: _TextureStage_CombineSource,
        operand0: _TextureStage_CombineOperand,
        source1: _TextureStage_CombineSource,
        operand1: _TextureStage_CombineOperand,
        source2: _TextureStage_CombineSource,
        operand2: _TextureStage_CombineOperand,
    ) -> None: ...
    def get_combine_alpha_mode(self) -> _TextureStage_CombineMode:
        """Get combine_alpha_mode"""
    def get_num_combine_alpha_operands(self) -> int:
        """Returns the number of meaningful operands that may be retrieved via
        get_combine_alpha_sourceN() and get_combine_alpha_operandN().
        """
    def get_combine_alpha_source0(self) -> _TextureStage_CombineSource:
        """Get source0 of combine_alpha_mode"""
    def get_combine_alpha_operand0(self) -> _TextureStage_CombineOperand:
        """Get operand0 of combine_alpha_mode"""
    def get_combine_alpha_source1(self) -> _TextureStage_CombineSource:
        """Get source1 of combine_alpha_mode"""
    def get_combine_alpha_operand1(self) -> _TextureStage_CombineOperand:
        """Get operand1 of combine_alpha_mode"""
    def get_combine_alpha_source2(self) -> _TextureStage_CombineSource:
        """Get source2 of combine_alpha_mode"""
    def get_combine_alpha_operand2(self) -> _TextureStage_CombineOperand:
        """Get operand2 of combine_alpha_mode"""
    def involves_color_scale(self) -> bool:
        """Returns true if the TextureStage is affected by the setting of the current
        ColorScaleAttrib, false otherwise.
        """
    def uses_color(self) -> bool:
        """Returns true if the TextureStage makes use of whatever color is specified
        in set_color(), false otherwise.
        """
    def uses_primary_color(self) -> bool:
        """Returns true if the TextureStage makes use of the CS_primary_color combine
        source.
        """
    def uses_last_saved_result(self) -> bool:
        """Returns true if the TextureStage makes use of the CS_primary_color combine
        source.
        """
    def compare_to(self, other: TextureStage) -> int:
        """Returns a number less than zero if this TextureStage sorts before the other
        one, greater than zero if it sorts after, or zero if they are equivalent.
        The sorting order is arbitrary and largely meaningless, except to
        differentiate different stages.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes the details of this stage"""
    def output(self, out: ostream) -> None:
        """Just a single line output"""
    @staticmethod
    def get_default() -> TextureStage:
        """Returns the default TextureStage that will be used for all texturing that
        does not name a particular stage.  This generally handles the normal
        single-texture case.
        """
    setName = set_name
    getName = get_name
    setSort = set_sort
    getSort = get_sort
    setPriority = set_priority
    getPriority = get_priority
    setTexcoordName = set_texcoord_name
    getTexcoordName = get_texcoord_name
    getTangentName = get_tangent_name
    getBinormalName = get_binormal_name
    setMode = set_mode
    getMode = get_mode
    isFixedFunction = is_fixed_function
    setColor = set_color
    getColor = get_color
    setRgbScale = set_rgb_scale
    getRgbScale = get_rgb_scale
    setAlphaScale = set_alpha_scale
    getAlphaScale = get_alpha_scale
    setSavedResult = set_saved_result
    getSavedResult = get_saved_result
    setTexViewOffset = set_tex_view_offset
    getTexViewOffset = get_tex_view_offset
    setCombineRgb = set_combine_rgb
    getCombineRgbMode = get_combine_rgb_mode
    getNumCombineRgbOperands = get_num_combine_rgb_operands
    getCombineRgbSource0 = get_combine_rgb_source0
    getCombineRgbOperand0 = get_combine_rgb_operand0
    getCombineRgbSource1 = get_combine_rgb_source1
    getCombineRgbOperand1 = get_combine_rgb_operand1
    getCombineRgbSource2 = get_combine_rgb_source2
    getCombineRgbOperand2 = get_combine_rgb_operand2
    setCombineAlpha = set_combine_alpha
    getCombineAlphaMode = get_combine_alpha_mode
    getNumCombineAlphaOperands = get_num_combine_alpha_operands
    getCombineAlphaSource0 = get_combine_alpha_source0
    getCombineAlphaOperand0 = get_combine_alpha_operand0
    getCombineAlphaSource1 = get_combine_alpha_source1
    getCombineAlphaOperand1 = get_combine_alpha_operand1
    getCombineAlphaSource2 = get_combine_alpha_source2
    getCombineAlphaOperand2 = get_combine_alpha_operand2
    involvesColorScale = involves_color_scale
    usesColor = uses_color
    usesPrimaryColor = uses_primary_color
    usesLastSavedResult = uses_last_saved_result
    compareTo = compare_to
    getDefault = get_default

class Geom(CopyOnWriteObject, GeomEnums):
    """A container for geometry primitives.  This class associates one or more
    GeomPrimitive objects with a table of vertices defined by a GeomVertexData
    object.  All of the primitives stored in a particular Geom are drawn from
    the same set of vertices (each primitive uses a subset of all of the
    vertices in the table), and all of them must be rendered at the same time,
    in the same graphics state.
    """

    bounds_type: _BoundingVolume_BoundsType
    @property
    def primitive_type(self) -> _GeomEnums_PrimitiveType: ...
    @property
    def shade_model(self) -> _GeomEnums_ShadeModel: ...
    @property
    def geom_rendering(self) -> int: ...
    @property
    def primitives(self) -> MutableSequence[GeomPrimitive]: ...
    @property
    def num_bytes(self) -> int: ...
    @property
    def modified(self) -> UpdateSeq: ...
    def __init__(self, data: GeomVertexData) -> None: ...
    def upcast_to_CopyOnWriteObject(self) -> CopyOnWriteObject: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def assign(self, copy: Self) -> Self: ...
    def make_copy(self) -> Geom:
        """Returns a newly-allocated Geom that is a shallow copy of this one.  It will
        be a different Geom pointer, but its internal data may or may not be shared
        with that of the original Geom.
        """
    def get_primitive_type(self) -> _GeomEnums_PrimitiveType:
        """Returns the fundamental primitive type that is common to all GeomPrimitives
        added within the Geom.  All nested primitives within a particular Geom must
        be the same type (that is, you can mix triangles and tristrips, because
        they are both the same fundamental type PT_polygons, but you cannot mix
        triangles and points withn the same Geom).
        """
    def get_shade_model(self) -> _GeomEnums_ShadeModel:
        """Returns the shade model common to all of the individual GeomPrimitives that
        have been added to the geom.
        """
    def get_geom_rendering(self) -> int:
        """Returns the set of GeomRendering bits that represent the rendering
        properties required to properly render this Geom.
        """
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the minimum (i.e.  most dynamic) usage_hint among all of the
        individual GeomPrimitives that have been added to the geom.
        @deprecated  This is no longer very useful.
        """
    def set_usage_hint(self, usage_hint: _GeomEnums_UsageHint) -> None:
        """Changes the UsageHint hint for all of the primitives on this Geom to the
        same value.  See get_usage_hint().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_vertex_data(self, current_thread: Thread = ...) -> GeomVertexData:
        """Returns a const pointer to the GeomVertexData, for application code to
        directly examine (but not modify) the geom's underlying data.
        """
    def modify_vertex_data(self) -> GeomVertexData:
        """Returns a modifiable pointer to the GeomVertexData, so that application
        code may directly maniuplate the geom's underlying data.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def set_vertex_data(self, data: GeomVertexData) -> None:
        """Replaces the Geom's underlying vertex data table with a completely new
        table.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def offset_vertices(self, data: GeomVertexData, offset: int) -> None:
        """Replaces a Geom's vertex table with a new table, and simultaneously adds
        the indicated offset to all vertex references within the Geom's primitives.
        This is intended to be used to combine multiple GeomVertexDatas from
        different Geoms into a single big buffer, with each Geom referencing a
        subset of the vertices in the buffer.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def make_nonindexed(self, composite_only: bool) -> int:
        """Converts the geom from indexed to nonindexed by duplicating vertices as
        necessary.  If composite_only is true, then only composite primitives such
        as trifans and tristrips are converted.  Returns the number of
        GeomPrimitive objects converted.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def get_animated_vertex_data(self, force: bool, current_thread: Thread = ...) -> GeomVertexData:
        """Returns a GeomVertexData that represents the results of computing the
        vertex animation on the CPU for this Geom's vertex data.

        If there is no CPU-defined vertex animation on this object, this just
        returns the original object.

        If there is vertex animation, but the VertexTransform values have not
        changed since last time, this may return the same pointer it returned
        previously.  Even if the VertexTransform values have changed, it may still
        return the same pointer, but with its contents modified (this is preferred,
        since it allows the graphics backend to update vertex buffers optimally).

        If force is false, this method may return immediately with stale data, if
        the vertex data is not completely resident.  If force is true, this method
        will never return stale data, but may block until the data is available.
        """
    def is_empty(self) -> bool:
        """Returns true if there appear to be no vertices to be rendered by this Geom,
        false if has some actual data.
        """
    def get_num_primitives(self) -> int:
        """Returns the number of GeomPrimitive objects stored within the Geom, each of
        which represents a number of primitives of a particular type.
        """
    def get_primitive(self, i: int) -> GeomPrimitive:
        """Returns a const pointer to the ith GeomPrimitive object stored within the
        Geom.  Use this call only to inspect the ith object; use modify_primitive()
        or set_primitive() if you want to modify it.
        """
    def modify_primitive(self, i: int) -> GeomPrimitive:
        """Returns a modifiable pointer to the ith GeomPrimitive object stored within
        the Geom, so application code can directly manipulate the properties of
        this primitive.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def set_primitive(self, i: int, primitive: GeomPrimitive) -> None:
        """Replaces the ith GeomPrimitive object stored within the Geom with the new
        object.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def insert_primitive(self, i: int, primitive: GeomPrimitive) -> None:
        """Inserts a new GeomPrimitive structure to the Geom object.  This specifies a
        particular subset of vertices that are used to define geometric primitives
        of the indicated type.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def add_primitive(self, primitive: GeomPrimitive) -> None:
        """Inserts a new GeomPrimitive structure to the Geom object.  This specifies a
        particular subset of vertices that are used to define geometric primitives
        of the indicated type.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def remove_primitive(self, i: int) -> None:
        """Removes the ith primitive from the list.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def clear_primitives(self) -> None:
        """Removes all the primitives from the Geom object (but keeps the same table
        of vertices).  You may then re-add primitives one at a time via calls to
        add_primitive().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def decompose(self) -> Geom:
        """Decomposes all of the primitives within this Geom, returning the result.
        See GeomPrimitive::decompose().
        """
    def doubleside(self) -> Geom:
        """Doublesides all of the primitives within this Geom, returning the result.
        See GeomPrimitive::doubleside().
        """
    def reverse(self) -> Geom:
        """Reverses all of the primitives within this Geom, returning the result.  See
        GeomPrimitive::reverse().
        """
    def rotate(self) -> Geom:
        """Rotates all of the primitives within this Geom, returning the result.  See
        GeomPrimitive::rotate().
        """
    def unify(self, max_indices: int, preserve_order: bool) -> Geom:
        """Unifies all of the primitives contained within this Geom into a single (or
        as few as possible, within the constraints of max_indices) primitive
        objects.  This may require decomposing the primitives if, for instance, the
        Geom contains both triangle strips and triangle fans.

        max_indices represents the maximum number of indices that will be put in
        any one GeomPrimitive.  If preserve_order is true, then the primitives will
        not be reordered during the operation, even if this results in a suboptimal
        result.
        """
    def make_points(self) -> Geom:
        """Returns a new Geom with points at all the vertices.  See
        GeomPrimitive::make_points().
        """
    def make_lines(self) -> Geom:
        """Returns a new Geom with lines at all the edges.  See
        GeomPrimitive::make_lines().
        """
    def make_patches(self) -> Geom:
        """Returns a new Geom with each primitive converted into a patch.  Calls
        decompose() first.
        """
    def make_adjacency(self) -> Geom:
        """Returns a new Geom with each primitive converted into a corresponding
        version with adjacency information.

        @since 1.10.0
        """
    def decompose_in_place(self) -> None:
        """Decomposes all of the primitives within this Geom, leaving the results in
        place.  See GeomPrimitive::decompose().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def doubleside_in_place(self) -> None:
        """Doublesides all of the primitives within this Geom, leaving the results in
        place.  See GeomPrimitive::doubleside().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def reverse_in_place(self) -> None:
        """Reverses all of the primitives within this Geom, leaving the results in
        place.  See GeomPrimitive::reverse().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def rotate_in_place(self) -> None:
        """Rotates all of the primitives within this Geom, leaving the results in
        place.  See GeomPrimitive::rotate().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def unify_in_place(self, max_indices: int, preserve_order: bool) -> None:
        """Unifies all of the primitives contained within this Geom into a single (or
        as few as possible, within the constraints of max_indices) primitive
        objects.  This may require decomposing the primitives if, for instance, the
        Geom contains both triangle strips and triangle fans.

        max_indices represents the maximum number of indices that will be put in
        any one GeomPrimitive.  If preserve_order is true, then the primitives will
        not be reordered during the operation, even if this results in a suboptimal
        result.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def make_points_in_place(self) -> None:
        """Replaces the GeomPrimitives within this Geom with corresponding GeomPoints.
        See GeomPrimitive::make_points().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def make_lines_in_place(self) -> None:
        """Replaces the GeomPrimitives within this Geom with corresponding GeomLines,
        representing a wireframe of the primitives.  See
        GeomPrimitive::make_lines().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def make_patches_in_place(self) -> None:
        """Replaces the GeomPrimitives within this Geom with corresponding
        GeomPatches.  See GeomPrimitive::make_patches().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def make_adjacency_in_place(self) -> None:
        """Replaces the GeomPrimitives within this Geom with corresponding versions
        with adjacency information.  See GeomPrimitive::make_adjacency().

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.

        @since 1.10.0
        """
    def copy_primitives_from(self, other: Geom) -> bool:
        """Copies the primitives from the indicated Geom into this one.  This does
        require that both Geoms contain the same fundamental type primitives, both
        have a compatible shade model, and both use the same GeomVertexData.  Both
        Geoms must also be the same specific class type (i.e.  if one is a
        GeomTextGlyph, they both must be.)

        Returns true if the copy is successful, or false otherwise (because the
        Geoms were mismatched).
        """
    def get_num_bytes(self) -> int:
        """Returns the number of bytes consumed by the geom and its primitives (but
        not including its vertex table).
        """
    def get_modified(self, current_thread: Thread = ...) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        any of the primitives in the Geom is modified, or the set of primitives is
        modified.  However, this does not include modifications to the vertex data,
        which should be tested separately.
        """
    def request_resident(self) -> bool:
        """Returns true if all the primitive arrays are currently resident in memory.
        If this returns false, the data will be brought back into memory shortly;
        try again later.

        This does not also test the Geom's associated GeomVertexData.  That must be
        tested separately.
        """
    def transform_vertices(self, mat: Mat4Like) -> None:
        """Applies the indicated transform to all of the vertices in the Geom.  If the
        Geom happens to share a vertex table with another Geom, this operation will
        duplicate the vertex table instead of breaking the other Geom; however, if
        multiple Geoms with shared tables are transformed by the same matrix, they
        will no longer share tables after the operation.  Consider using the
        GeomTransformer if you will be applying the same transform to multiple
        Geoms.
        """
    def check_valid(self, vertex_data: GeomVertexData = ...) -> bool:
        """`(self)`:
        Verifies that the all of the primitives within the geom reference vertices
        that actually exist within the geom's GeomVertexData.  Returns true if the
        geom appears to be valid, false otherwise.

        `(self, vertex_data: GeomVertexData)`:
        Verifies that the all of the primitives within the geom reference vertices
        that actually exist within the indicated GeomVertexData.  Returns true if
        the geom appears to be valid, false otherwise.
        """
    def get_bounds(self, current_thread: Thread = ...) -> BoundingVolume:
        """Returns the bounding volume for the Geom."""
    def get_nested_vertices(self, current_thread: Thread = ...) -> int:
        """Returns the number of vertices rendered by all primitives within the Geom."""
    def mark_bounds_stale(self) -> None:
        """Marks the bounding volume of the Geom as stale so that it should be
        recomputed.  Usually it is not necessary to call this explicitly.
        """
    def set_bounds_type(self, bounds_type: _BoundingVolume_BoundsType) -> None:
        """Specifies the desired type of bounding volume that will be created for this
        Geom.  This is normally BoundingVolume::BT_default, which means to set the
        type according to the config variable "bounds-type".

        If this is BT_sphere or BT_box, a BoundingSphere or BoundingBox is
        explicitly created.  If it is BT_best, a BoundingBox is created.

        This affects the implicit bounding volume only.  If an explicit bounding
        volume is set on the Geom with set_bounds(), that bounding volume type is
        used.  (This is different behavior from the similar method on PandaNode.)
        """
    def get_bounds_type(self) -> _BoundingVolume_BoundsType:
        """Returns the bounding volume type set with set_bounds_type()."""
    def set_bounds(self, volume: BoundingVolume) -> None:
        """Resets the bounding volume so that it is the indicated volume.  When it is
        explicitly set, the bounding volume will no longer be automatically
        computed; call clear_bounds() if you would like to return the bounding
        volume to its default behavior.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def clear_bounds(self) -> None:
        """Reverses the effect of a previous call to set_bounds(), and allows the
        bounding volume to be automatically computed once more based on the
        vertices.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def clear_cache(self) -> None:
        """Removes all of the previously-cached results of munge_geom().

        This blows away the entire cache, upstream and downstream the pipeline.
        Use clear_cache_stage() instead if you only want to blow away the cache at
        the current stage and upstream.
        """
    def clear_cache_stage(self, current_thread: Thread) -> None:
        """Removes all of the previously-cached results of munge_geom(), at the
        current pipeline stage and upstream.  Does not affect the downstream cache.

        Don't call this in a downstream thread unless you don't mind it blowing
        away other changes you might have recently made in an upstream thread.
        """
    def prepare(self, prepared_objects: PreparedGraphicsObjects) -> None:
        """Indicates that the geom should be enqueued to be prepared in the indicated
        prepared_objects at the beginning of the next frame.  This will ensure the
        geom is already loaded into geom memory if it is expected to be rendered
        soon.

        Use this function instead of prepare_now() to preload geoms from a user
        interface standpoint.
        """
    def is_prepared(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the geom has already been prepared or enqueued for
        preparation on the indicated GSG, false otherwise.
        """
    def release(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Frees the geom context only on the indicated object, if it exists there.
        Returns true if it was released, false if it had not been prepared.
        """
    def release_all(self) -> int:
        """Frees the context allocated on all objects for which the geom has been
        declared.  Returns the number of contexts which have been freed.
        """
    def prepare_now(self, prepared_objects: PreparedGraphicsObjects, gsg: GraphicsStateGuardianBase) -> GeomContext:
        """Creates a context for the geom on the particular GSG, if it does not
        already exist.  Returns the new (or old) GeomContext.  This assumes that
        the GraphicsStateGuardian is the currently active rendering context and
        that it is ready to accept new geoms.  If this is not necessarily the case,
        you should use prepare() instead.

        Normally, this is not called directly except by the GraphicsStateGuardian;
        a geom does not need to be explicitly prepared by the user before it may be
        rendered.
        """
    def get_primitives(self) -> tuple[GeomPrimitive, ...]: ...
    upcastToCopyOnWriteObject = upcast_to_CopyOnWriteObject
    upcastToGeomEnums = upcast_to_GeomEnums
    makeCopy = make_copy
    getPrimitiveType = get_primitive_type
    getShadeModel = get_shade_model
    getGeomRendering = get_geom_rendering
    getUsageHint = get_usage_hint
    setUsageHint = set_usage_hint
    getVertexData = get_vertex_data
    modifyVertexData = modify_vertex_data
    setVertexData = set_vertex_data
    offsetVertices = offset_vertices
    makeNonindexed = make_nonindexed
    getAnimatedVertexData = get_animated_vertex_data
    isEmpty = is_empty
    getNumPrimitives = get_num_primitives
    getPrimitive = get_primitive
    modifyPrimitive = modify_primitive
    setPrimitive = set_primitive
    insertPrimitive = insert_primitive
    addPrimitive = add_primitive
    removePrimitive = remove_primitive
    clearPrimitives = clear_primitives
    makePoints = make_points
    makeLines = make_lines
    makePatches = make_patches
    makeAdjacency = make_adjacency
    decomposeInPlace = decompose_in_place
    doublesideInPlace = doubleside_in_place
    reverseInPlace = reverse_in_place
    rotateInPlace = rotate_in_place
    unifyInPlace = unify_in_place
    makePointsInPlace = make_points_in_place
    makeLinesInPlace = make_lines_in_place
    makePatchesInPlace = make_patches_in_place
    makeAdjacencyInPlace = make_adjacency_in_place
    copyPrimitivesFrom = copy_primitives_from
    getNumBytes = get_num_bytes
    getModified = get_modified
    requestResident = request_resident
    transformVertices = transform_vertices
    checkValid = check_valid
    getBounds = get_bounds
    getNestedVertices = get_nested_vertices
    markBoundsStale = mark_bounds_stale
    setBoundsType = set_bounds_type
    getBoundsType = get_bounds_type
    setBounds = set_bounds
    clearBounds = clear_bounds
    clearCache = clear_cache
    clearCacheStage = clear_cache_stage
    isPrepared = is_prepared
    releaseAll = release_all
    prepareNow = prepare_now
    getPrimitives = get_primitives

class GeomContext(SavedContext):
    """This is a special class object that holds all the information returned by a
    particular GSG to indicate the geom's internal context identifier.

    Geoms typically have an immediate-mode and a retained-mode operation.  When
    using geoms in retained-mode (in response to Geom::prepare()), the GSG will
    create some internal handle for the geom and store it here.  The geom
    stores all of these handles internally.

    In the case of OpenGL, for example, a GeomContext corresponds to a display
    list identifier.
    """

    @property
    def geom(self) -> Geom: ...
    def get_geom(self) -> Geom: ...
    getGeom = get_geom

class GeomLines(GeomPrimitive):
    """Defines a series of disconnected line segments."""

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomLines) -> None: ...

class GeomLinesAdjacency(GeomPrimitive):
    """Defines a series of disconnected line segments with adjacency information,
    for use with geometry shaders.

    @since 1.10.0
    """

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomLinesAdjacency) -> None: ...

class GeomLinestrips(GeomPrimitive):
    """Defines a series of line strips."""

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomLinestrips) -> None: ...

class GeomLinestripsAdjacency(GeomPrimitive):
    """Defines a series of line strips with adjacency information.

    @since 1.10.0
    """

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomLinestripsAdjacency) -> None: ...

class GeomPatches(GeomPrimitive):
    """Defines a series of "patches", fixed-size groupings of vertices that must
    be processed by a tessellation shader.
    """

    @overload
    def __init__(self, copy: GeomPatches) -> None:
        """The number of vertices per patch must be specified to the GeomPatches
        constructor, and it may not be changed during the lifetime of the
        GeomPatches object.  Create a new GeomPatches if you need to have a
        different value.
        """
    @overload
    def __init__(self, num_vertices_per_patch: int, usage_hint: _GeomEnums_UsageHint) -> None: ...

class GeomPoints(GeomPrimitive):
    """Defines a series of disconnected points."""

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomPoints) -> None: ...

class GeomTriangles(GeomPrimitive):
    """Defines a series of disconnected triangles."""

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomTriangles) -> None: ...

class GeomTrianglesAdjacency(GeomPrimitive):
    """Defines a series of disconnected triangles, with adjacency information.

    @since 1.10.0
    """

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomTrianglesAdjacency) -> None: ...

class GeomTrifans(GeomPrimitive):
    """Defines a series of triangle fans."""

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomTrifans) -> None: ...

class GeomTristrips(GeomPrimitive):
    """Defines a series of triangle strips."""

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomTristrips) -> None: ...

class GeomTristripsAdjacency(GeomPrimitive):
    """Defines a series of triangle strips with adjacency information.

    @since 1.10.0
    """

    @overload
    def __init__(self, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, copy: GeomTristripsAdjacency) -> None: ...

class GeomVertexReader(GeomEnums):
    """This object provides a high-level interface for quickly reading a sequence
    of numeric values from a vertex table.

    It is particularly optimized for reading a single column of data values for
    a series of vertices, without changing columns between each number.
    Although you can also use one GeomVertexReader to read across the columns
    if it is convenient, by calling set_column() repeatedly at each vertex, it
    is faster to read down the columns, and to use a different GeomVertexReader
    for each column.

    Note that a GeomVertexReader does not keep a reference count to the actual
    vertex data buffer (it grabs the current data buffer from the
    GeomVertexData whenever set_column() is called).  This means that it is
    important not to keep a GeomVertexReader object around over a long period
    of time in which the data buffer is likely to be deallocated; it is
    intended for making a quick pass over the data in one session.

    It also means that you should create any GeomVertexWriters *before*
    creating GeomVertexReaders on the same data, since the writer itself might
    cause the vertex buffer to be deallocated.  Better yet, use a
    GeomVertexRewriter if you are going to create both of them anyway.
    """

    @overload
    def __init__(self, current_thread: Thread = ...) -> None:
        """`(self, array_data: GeomVertexArrayData, current_thread: Thread = ...)`; `(self, array_data: GeomVertexArrayData, column: int, current_thread: Thread = ...)`:
        Constructs a new reader to process the vertices of the indicated array
        only.

        `(self, vertex_data: GeomVertexData, name: InternalName, current_thread: Thread = ...)`:
        Constructs a new reader to process the vertices of the indicated data
        object.  This flavor creates the reader specifically to process the named
        data type.

        `(self, vertex_data: GeomVertexData, current_thread: Thread = ...)`:
        Constructs a new reader to process the vertices of the indicated data
        object.

        `(self, current_thread: Thread = ...)`:
        Constructs an invalid GeomVertexReader.  You must use the assignment
        operator to assign a valid GeomVertexReader to this object before you can
        use it.
        """
    @overload
    def __init__(self, copy: GeomVertexReader) -> None: ...
    @overload
    def __init__(self, array_data: GeomVertexArrayData, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, vertex_data: GeomVertexData, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, array_data: GeomVertexArrayData, column: int, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, vertex_data: GeomVertexData, name: InternalName | str, current_thread: Thread = ...) -> None: ...
    def assign(self, copy: GeomVertexArrayData | GeomVertexData | GeomVertexReader | Thread) -> Self: ...
    def get_vertex_data(self) -> GeomVertexData:
        """Returns the vertex data object that the reader is processing.  This may
        return NULL if the reader was constructed with just an array pointer.
        """
    def get_array_data(self) -> GeomVertexArrayData:
        """Returns the particular array object that the reader is currently
        processing.
        """
    def get_array_handle(self) -> GeomVertexArrayDataHandle:
        """Returns the read handle to the array object that the read is currently
        processing.  This low-level call should be used with caution.
        """
    def get_stride(self) -> int:
        """Returns the per-row stride (bytes between consecutive rows) of the
        underlying vertex array.  This low-level information is normally not needed
        to use the GeomVertexReader directly.
        """
    def get_current_thread(self) -> Thread:
        """Returns the Thread pointer of the currently-executing thread, as passed to
        the constructor of this object.
        """
    def set_force(self, force: bool) -> None:
        """Sets the value of the force flag.  When this is true (the default), vertex
        data will be paged in from disk if necessary.  When this is false, the
        GeomVertexData will simply return a failure code when attempting to read
        vertex data that is not resident (but will put it on the queue to become
        resident later).

        Normally, vertex data is always resident, so this will not be an issue.  It
        is only possible for vertex data to be nonresident if you have enabled
        vertex paging via the GeomVertexArrayData and VertexDataPage interfaces.
        """
    def get_force(self) -> bool:
        """Returns the value of the force flag.  See set_force()."""
    @overload
    def set_column(self, name: InternalName | str) -> bool:
        """`(self, name: InternalName)`:
        Sets up the reader to use the data type with the indicated name.

        This also resets the read row number to the start row (the same value
        passed to a previous call to set_row(), or 0 if set_row() was never
        called.)

        The return value is true if the data type is valid, false otherwise.

        `(self, column: int)`:
        Sets up the reader to use the nth data type of the GeomVertexFormat,
        numbering from 0.

        This also resets the read row number to the start row (the same value
        passed to a previous call to set_row(), or 0 if set_row() was never
        called.)

        The return value is true if the data type is valid, false otherwise.

        `(self, array: int, column: GeomVertexColumn)`:
        Sets up the reader to use the indicated column description on the given
        array.

        This also resets the current read row number to the start row (the same
        value passed to a previous call to set_row(), or 0 if set_row() was never
        called.)

        The return value is true if the data type is valid, false otherwise.
        """
    @overload
    def set_column(self, column: int) -> bool: ...
    @overload
    def set_column(self, array: int, column: GeomVertexColumn) -> bool: ...
    def clear(self) -> None:
        """Resets the GeomVertexReader to the initial state."""
    def has_column(self) -> bool:
        """Returns true if a valid data type has been successfully set, or false if
        the data type does not exist (or if get_force() is false and the vertex
        data is nonresident).
        """
    def get_array(self) -> int:
        """Returns the array index containing the data type that the reader is working
        on.
        """
    def get_column(self) -> GeomVertexColumn:
        """Returns the description of the data type that the reader is working on."""
    def set_row_unsafe(self, row: int) -> None:
        """Sets the start row to the indicated value, without internal checks.  This
        is the same as set_row(), but it does not check for the possibility that
        the array has been reallocated internally for some reason; use only when
        you are confident that the array is unchanged and you really need every bit
        of available performance.
        """
    def set_row(self, row: int) -> None:
        """Sets the start row to the indicated value.  The reader will begin reading
        from the indicated row; each subsequent get_data*() call will return the
        data from the subsequent row.  If set_column() is called, the reader will
        return to this row.
        """
    def get_start_row(self) -> int:
        """Returns the row index at which the reader started.  It will return to this
        row if you reset the current column.
        """
    def get_read_row(self) -> int:
        """Returns the row index from which the data will be retrieved by the next
        call to get_data*().
        """
    def is_at_end(self) -> bool:
        """Returns true if the reader is currently at the end of the list of vertices,
        false otherwise.  If this is true, another call to get_data*() will result
        in a crash.
        """
    def get_data1f(self) -> float:
        """Returns the data associated with the read row, expressed as a 1-component
        value, and advances the read row.
        """
    def get_data2f(self) -> LVecBase2f:
        """Returns the data associated with the read row, expressed as a 2-component
        value, and advances the read row.
        """
    def get_data3f(self) -> LVecBase3f:
        """Returns the data associated with the read row, expressed as a 3-component
        value, and advances the read row.
        """
    def get_data4f(self) -> LVecBase4f:
        """Returns the data associated with the read row, expressed as a 4-component
        value, and advances the read row.
        """
    def get_matrix3f(self) -> LMatrix3f:
        """Returns the 3-by-3 matrix associated with the read row and advances the
        read row.  This is a special method that only works when the column in
        question contains a matrix of an appropriate size.
        """
    def get_matrix4f(self) -> LMatrix4f:
        """Returns the 4-by-4 matrix associated with the read row and advances the
        read row.  This is a special method that only works when the column in
        question contains a matrix of an appropriate size.
        """
    def get_data1d(self) -> float:
        """Returns the data associated with the read row, expressed as a 1-component
        value, and advances the read row.
        """
    def get_data2d(self) -> LVecBase2d:
        """Returns the data associated with the read row, expressed as a 2-component
        value, and advances the read row.
        """
    def get_data3d(self) -> LVecBase3d:
        """Returns the data associated with the read row, expressed as a 3-component
        value, and advances the read row.
        """
    def get_data4d(self) -> LVecBase4d:
        """Returns the data associated with the read row, expressed as a 4-component
        value, and advances the read row.
        """
    def get_matrix3d(self) -> LMatrix3d:
        """Returns the 3-by-3 matrix associated with the read row and advances the
        read row.  This is a special method that only works when the column in
        question contains a matrix of an appropriate size.
        """
    def get_matrix4d(self) -> LMatrix4d:
        """Returns the 4-by-4 matrix associated with the read row and advances the
        read row.  This is a special method that only works when the column in
        question contains a matrix of an appropriate size.
        """
    def get_data1(self) -> float:
        """Returns the data associated with the read row, expressed as a 1-component
        value, and advances the read row.
        """
    def get_data2(self) -> LVecBase2:
        """Returns the data associated with the read row, expressed as a 2-component
        value, and advances the read row.
        """
    def get_data3(self) -> LVecBase3:
        """Returns the data associated with the read row, expressed as a 3-component
        value, and advances the read row.
        """
    def get_data4(self) -> LVecBase4:
        """Returns the data associated with the read row, expressed as a 4-component
        value, and advances the read row.
        """
    def get_matrix3(self) -> LMatrix3:
        """Returns the 3-by-3 matrix associated with the read row and advances the
        read row.  This is a special method that only works when the column in
        question contains a matrix of an appropriate size.
        """
    def get_matrix4(self) -> LMatrix4:
        """Returns the 4-by-4 matrix associated with the read row and advances the
        read row.  This is a special method that only works when the column in
        question contains a matrix of an appropriate size.
        """
    def get_data1i(self) -> int:
        """Returns the data associated with the read row, expressed as a 1-component
        value, and advances the read row.
        """
    def get_data2i(self) -> LVecBase2i:
        """Returns the data associated with the read row, expressed as a 2-component
        value, and advances the read row.
        """
    def get_data3i(self) -> LVecBase3i:
        """Returns the data associated with the read row, expressed as a 3-component
        value, and advances the read row.
        """
    def get_data4i(self) -> LVecBase4i:
        """Returns the data associated with the read row, expressed as a 4-component
        value, and advances the read row.
        """
    def output(self, out: ostream) -> None: ...
    getVertexData = get_vertex_data
    getArrayData = get_array_data
    getArrayHandle = get_array_handle
    getStride = get_stride
    getCurrentThread = get_current_thread
    setForce = set_force
    getForce = get_force
    setColumn = set_column
    hasColumn = has_column
    getArray = get_array
    getColumn = get_column
    setRowUnsafe = set_row_unsafe
    setRow = set_row
    getStartRow = get_start_row
    getReadRow = get_read_row
    isAtEnd = is_at_end
    getData1f = get_data1f
    getData2f = get_data2f
    getData3f = get_data3f
    getData4f = get_data4f
    getMatrix3f = get_matrix3f
    getMatrix4f = get_matrix4f
    getData1d = get_data1d
    getData2d = get_data2d
    getData3d = get_data3d
    getData4d = get_data4d
    getMatrix3d = get_matrix3d
    getMatrix4d = get_matrix4d
    getData1 = get_data1
    getData2 = get_data2
    getData3 = get_data3
    getData4 = get_data4
    getMatrix3 = get_matrix3
    getMatrix4 = get_matrix4
    getData1i = get_data1i
    getData2i = get_data2i
    getData3i = get_data3i
    getData4i = get_data4i

class GeomVertexWriter(GeomEnums):
    """This object provides a high-level interface for quickly writing a sequence
    of numeric values from a vertex table.

    This object can be used both to replace existing vertices in the table, or
    to extend the table with new vertices.  The set_data*() family of methods
    can only be used to replace existing data; it is an error to allow these to
    run past the end of the data.  The add_data*() family of methods, on the
    other hand, can be used to replace existing data or add new data; if you
    call set_row() into the middle of existing data the add_data*() methods
    will behave like the corresponding set_data*(), but if they run past the
    end of existing data they will quietly add new vertices.

    Like GeomVertexReader, the writer is particularly optimized for writing a
    single column of data values for a series of vertices, without changing
    columns between each number.  Although you can also use one
    GeomVertexWriter to write across the columns if it is convenient, by
    calling set_column() repeatedly at each vertex, it is faster to write down
    the columns, and to use a different GeomVertexWriter for each column.

    Note that, like a GeomVertexReader, a GeomVertexWriter does not keep a
    reference count to the actual vertex data buffer.  This means that it is
    important not to keep a GeomVertexWriter object around over a long period
    of time in which the data buffer is likely to be deallocated; it is
    intended for making a quick pass over the data in one session.

    It also means that you should create any GeomVertexWriters *before*
    creating GeomVertexReaders on the same data, since the writer itself might
    cause the vertex buffer to be deallocated.  Better yet, use a
    GeomVertexRewriter if you are going to create both of them anyway.
    """

    @overload
    def __init__(self, current_thread: Thread = ...) -> None:
        """`(self, array_data: GeomVertexArrayData, current_thread: Thread = ...)`; `(self, array_data: GeomVertexArrayData, column: int, current_thread: Thread = ...)`:
        Constructs a new writer to process the vertices of the indicated array
        only.

        `(self, vertex_data: GeomVertexData, name: InternalName, current_thread: Thread = ...)`:
        Constructs a new writer to process the vertices of the indicated data
        object.  This flavor creates the writer specifically to process the named
        data type.

        `(self, vertex_data: GeomVertexData, current_thread: Thread = ...)`:
        Constructs a new writer to process the vertices of the indicated data
        object.

        `(self, current_thread: Thread = ...)`:
        Constructs an invalid GeomVertexWriter.  You must use the assignment
        operator to assign a valid GeomVertexWriter to this object before you can
        use it.
        """
    @overload
    def __init__(self, copy: GeomVertexWriter) -> None: ...
    @overload
    def __init__(self, array_data: GeomVertexArrayData, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, vertex_data: GeomVertexData, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, array_data: GeomVertexArrayData, column: int, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, vertex_data: GeomVertexData, name: InternalName | str, current_thread: Thread = ...) -> None: ...
    def assign(self, copy: GeomVertexArrayData | GeomVertexData | GeomVertexWriter | Thread) -> Self: ...
    def get_vertex_data(self) -> GeomVertexData:
        """Returns the vertex data object that the writer is processing.  This may
        return NULL if the writer was constructed with just an array pointer.
        """
    def get_array_data(self) -> GeomVertexArrayData:
        """Returns the particular array object that the writer is currently
        processing.
        """
    def get_array_handle(self) -> GeomVertexArrayDataHandle:
        """Returns the write handle to the array object that the writer is currently
        processing.  This low-level call should be used with caution; be careful
        with modifying the data in the handle out from under the GeomVertexWriter.
        """
    def get_stride(self) -> int:
        """Returns the per-row stride (bytes between consecutive rows) of the
        underlying vertex array.  This low-level information is normally not needed
        to use the GeomVertexWriter directly.
        """
    def get_current_thread(self) -> Thread:
        """Returns the Thread pointer of the currently-executing thread, as passed to
        the constructor of this object.
        """
    @overload
    def set_column(self, name: InternalName | str) -> bool:
        """`(self, name: InternalName)`:
        Sets up the writer to use the data type with the indicated name.

        This also resets the write number to the start row (the same value passed
        to a previous call to set_row(), or 0 if set_row() was never called.)

        The return value is true if the data type is valid, false otherwise.

        `(self, column: int)`:
        Sets up the writer to use the nth data type of the GeomVertexFormat,
        numbering from 0.

        This also resets the write row number to the start row (the same value
        passed to a previous call to set_row(), or 0 if set_row() was never
        called.)

        The return value is true if the data type is valid, false otherwise.

        `(self, array: int, column: GeomVertexColumn)`:
        Sets up the writer to use the indicated column description on the given
        array.

        This also resets the current write row number to the start row (the same
        value passed to a previous call to set_row(), or 0 if set_row() was never
        called.)

        The return value is true if the data type is valid, false otherwise.
        """
    @overload
    def set_column(self, column: int) -> bool: ...
    @overload
    def set_column(self, array: int, column: GeomVertexColumn) -> bool: ...
    def clear(self) -> None:
        """Resets the GeomVertexWriter to the initial state."""
    def reserve_num_rows(self, num_rows: int) -> bool:
        """This ensures that enough memory space for num_rows is allocated, so that
        you may add up to num_rows rows without causing a new memory allocation.
        This is a performance optimization only; it is especially useful when you
        know the number of rows you will be adding ahead of time.
        """
    def has_column(self) -> bool:
        """Returns true if a valid data type has been successfully set, or false if
        the data type does not exist.
        """
    def get_array(self) -> int:
        """Returns the array index containing the data type that the writer is working
        on.
        """
    def get_column(self) -> GeomVertexColumn:
        """Returns the description of the data type that the writer is working on."""
    def set_row_unsafe(self, row: int) -> None:
        """Sets the start row to the indicated value, without internal checks.  This
        is the same as set_row(), but it does not check for the possibility that
        the array has been reallocated internally for some reason; use only when
        you are confident that the array is unchanged and you really need every bit
        of available performance.
        """
    def set_row(self, row: int) -> None:
        """Sets the start row to the indicated value.  The writer will begin writing
        to the indicated row; each subsequent set_data*() call will store the data
        into the subsequent row.  If set_column() is called, the writer will return
        to this row.
        """
    def get_start_row(self) -> int:
        """Returns the row index at which the writer started.  It will return to this
        row if you reset the current column.
        """
    def get_write_row(self) -> int:
        """Returns the row index to which the data will be written at the next call to
        set_data*() or add_data*().
        """
    def is_at_end(self) -> bool:
        """Returns true if the writer is currently at the end of the list of vertices,
        false otherwise.  If this is true, another call to set_data*() will result
        in a crash, but another call to add_data*() will add a new row.
        """
    def set_data1f(self, data: float) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2f(self, data: Vec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2f(self, x: float, y: float) -> None: ...
    @overload
    def set_data3f(self, data: Vec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data3f(self, x: float, y: float, z: float) -> None: ...
    @overload
    def set_data4f(self, data: Vec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data4f(self, x: float, y: float, z: float, w: float) -> None: ...
    def set_matrix3f(self, mat: LMatrix3f) -> None:
        """Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        It is an error for the write row to advance past the end of data.
        """
    def set_matrix4f(self, mat: Mat4Like) -> None:
        """Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        It is an error for the write row to advance past the end of data.
        """
    def set_data1d(self, data: float) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2d(self, data: DoubleVec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2d(self, x: float, y: float) -> None: ...
    @overload
    def set_data3d(self, data: DoubleVec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data3d(self, x: float, y: float, z: float) -> None: ...
    @overload
    def set_data4d(self, data: DoubleVec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data4d(self, x: float, y: float, z: float, w: float) -> None: ...
    def set_matrix3d(self, mat: LMatrix3d) -> None:
        """Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        It is an error for the write row to advance past the end of data.
        """
    def set_matrix4d(self, mat: DoubleMat4Like) -> None:
        """Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        It is an error for the write row to advance past the end of data.
        """
    def set_data1(self, data: float) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2(self, data: Vec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2(self, x: float, y: float) -> None: ...
    @overload
    def set_data3(self, data: Vec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data3(self, x: float, y: float, z: float) -> None: ...
    @overload
    def set_data4(self, data: Vec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data4(self, x: float, y: float, z: float, w: float) -> None: ...
    def set_matrix3(self, mat: LMatrix3) -> None:
        """Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        It is an error for the write row to advance past the end of data.
        """
    def set_matrix4(self, mat: Mat4Like) -> None:
        """Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        It is an error for the write row to advance past the end of data.
        """
    def set_data1i(self, data: int) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2i(self, data: IntVec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data2i(self, a: int, b: int) -> None: ...
    @overload
    def set_data3i(self, data: IntVec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data3i(self, a: int, b: int, c: int) -> None: ...
    @overload
    def set_data4i(self, data: IntVec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        It is an error for the write row to advance past the end of data.
        """
    @overload
    def set_data4i(self, a: int, b: int, c: int, d: int) -> None: ...
    def add_data1f(self, data: float) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2f(self, data: Vec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2f(self, x: float, y: float) -> None: ...
    @overload
    def add_data3f(self, data: Vec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data3f(self, x: float, y: float, z: float) -> None: ...
    @overload
    def add_data4f(self, data: Vec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data4f(self, x: float, y: float, z: float, w: float) -> None: ...
    def add_matrix3f(self, mat: LMatrix3f) -> None:
        """Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    def add_matrix4f(self, mat: Mat4Like) -> None:
        """Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    def add_data1d(self, data: float) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2d(self, data: DoubleVec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2d(self, x: float, y: float) -> None: ...
    @overload
    def add_data3d(self, data: DoubleVec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data3d(self, x: float, y: float, z: float) -> None: ...
    @overload
    def add_data4d(self, data: DoubleVec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data4d(self, x: float, y: float, z: float, w: float) -> None: ...
    def add_matrix3d(self, mat: LMatrix3d) -> None:
        """Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    def add_matrix4d(self, mat: DoubleMat4Like) -> None:
        """Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    def add_data1(self, data: float) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2(self, data: Vec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2(self, x: float, y: float) -> None: ...
    @overload
    def add_data3(self, data: Vec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data3(self, x: float, y: float, z: float) -> None: ...
    @overload
    def add_data4(self, data: Vec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data4(self, x: float, y: float, z: float, w: float) -> None: ...
    def add_matrix3(self, mat: LMatrix3) -> None:
        """Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    def add_matrix4(self, mat: Mat4Like) -> None:
        """Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
        a special method that can only be used on matrix columns.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    def add_data1i(self, data: int) -> None:
        """Sets the write row to a particular 1-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2i(self, data: IntVec2Like) -> None:
        """Sets the write row to a particular 2-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data2i(self, a: int, b: int) -> None: ...
    @overload
    def add_data3i(self, data: IntVec3Like) -> None:
        """Sets the write row to a particular 3-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data3i(self, a: int, b: int, c: int) -> None: ...
    @overload
    def add_data4i(self, data: IntVec4Like) -> None:
        """Sets the write row to a particular 4-component value, and advances the
        write row.

        If the write row advances past the end of data, implicitly adds a new row
        to the data.
        """
    @overload
    def add_data4i(self, a: int, b: int, c: int, d: int) -> None: ...
    def output(self, out: ostream) -> None: ...
    getVertexData = get_vertex_data
    getArrayData = get_array_data
    getArrayHandle = get_array_handle
    getStride = get_stride
    getCurrentThread = get_current_thread
    setColumn = set_column
    reserveNumRows = reserve_num_rows
    hasColumn = has_column
    getArray = get_array
    getColumn = get_column
    setRowUnsafe = set_row_unsafe
    setRow = set_row
    getStartRow = get_start_row
    getWriteRow = get_write_row
    isAtEnd = is_at_end
    setData1f = set_data1f
    setData2f = set_data2f
    setData3f = set_data3f
    setData4f = set_data4f
    setMatrix3f = set_matrix3f
    setMatrix4f = set_matrix4f
    setData1d = set_data1d
    setData2d = set_data2d
    setData3d = set_data3d
    setData4d = set_data4d
    setMatrix3d = set_matrix3d
    setMatrix4d = set_matrix4d
    setData1 = set_data1
    setData2 = set_data2
    setData3 = set_data3
    setData4 = set_data4
    setMatrix3 = set_matrix3
    setMatrix4 = set_matrix4
    setData1i = set_data1i
    setData2i = set_data2i
    setData3i = set_data3i
    setData4i = set_data4i
    addData1f = add_data1f
    addData2f = add_data2f
    addData3f = add_data3f
    addData4f = add_data4f
    addMatrix3f = add_matrix3f
    addMatrix4f = add_matrix4f
    addData1d = add_data1d
    addData2d = add_data2d
    addData3d = add_data3d
    addData4d = add_data4d
    addMatrix3d = add_matrix3d
    addMatrix4d = add_matrix4d
    addData1 = add_data1
    addData2 = add_data2
    addData3 = add_data3
    addData4 = add_data4
    addMatrix3 = add_matrix3
    addMatrix4 = add_matrix4
    addData1i = add_data1i
    addData2i = add_data2i
    addData3i = add_data3i
    addData4i = add_data4i

class GeomVertexRewriter(GeomVertexWriter, GeomVertexReader):  # type: ignore[misc]
    """This object provides the functionality of both a GeomVertexReader and a
    GeomVertexWriter, combined together into one convenient package.  It is
    designed for making a single pass over a GeomVertexData object, modifying
    rows as it goes.

    Although it doesn't provide any real performance benefit over using a
    separate reader and writer on the same data, it should probably be used in
    preference to a separate reader and writer, because it makes an effort to
    manage the reference counts properly between the reader and the writer to
    avoid accidentally dereferencing either array while recopying.
    """

    @overload
    def __init__(self, current_thread: Thread = ...) -> None:
        """`(self, array_data: GeomVertexArrayData, current_thread: Thread = ...)`; `(self, array_data: GeomVertexArrayData, column: int, current_thread: Thread = ...)`:
        Constructs a new rewriter to process the vertices of the indicated array
        only.

        `(self, vertex_data: GeomVertexData, name: InternalName, current_thread: Thread = ...)`:
        Constructs a new rewriter to process the vertices of the indicated data
        object.  This flavor creates the rewriter specifically to process the named
        data type.

        `(self, vertex_data: GeomVertexData, current_thread: Thread = ...)`:
        Constructs a new rewriter to process the vertices of the indicated data
        object.

        `(self, current_thread: Thread = ...)`:
        Constructs an invalid GeomVertexRewriter.  You must use the assignment
        operator to assign a valid GeomVertexRewriter to this object before you can
        use it.
        """
    @overload
    def __init__(self, copy: GeomVertexRewriter) -> None: ...
    @overload
    def __init__(self, array_data: GeomVertexArrayData, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, vertex_data: GeomVertexData, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, array_data: GeomVertexArrayData, column: int, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, vertex_data: GeomVertexData, name: InternalName | str, current_thread: Thread = ...) -> None: ...
    def upcast_to_GeomVertexWriter(self) -> GeomVertexWriter: ...
    def upcast_to_GeomVertexReader(self) -> GeomVertexReader: ...
    def assign(self, copy: GeomVertexArrayData | GeomVertexData | GeomVertexRewriter | Thread) -> Self: ...  # type: ignore[override]
    def get_vertex_data(self) -> GeomVertexData:
        """Returns the vertex data object that the rewriter is processing."""
    def get_array_data(self) -> GeomVertexArrayData:
        """Returns the particular array object that the rewriter is currently
        processing.
        """
    def get_array_handle(self) -> GeomVertexArrayDataHandle:
        """Returns the write handle to the array object that the rewriter is currently
        processing.  This low-level call should be used with caution; be careful
        with modifying the data in the handle out from under the
        GeomVertexRewriter.
        """
    def get_stride(self) -> int:
        """Returns the per-row stride (bytes between consecutive rows) of the
        underlying vertex array.  This low-level information is normally not needed
        to use the GeomVertexRewriter directly.
        """
    @overload
    def set_column(self, name: InternalName | str) -> bool:
        """`(self, name: InternalName)`:
        Sets up the rewriter to use the data type with the indicated name.

        This also resets both the read and write row numbers to the start row (the
        same value passed to a previous call to set_row(), or 0 if set_row() was
        never called.)

        The return value is true if the data type is valid, false otherwise.

        `(self, column: int)`:
        Sets up the rewriter to use the nth data type of the GeomVertexFormat,
        numbering from 0.

        This also resets both the read and write row numbers to the start row (the
        same value passed to a previous call to set_row(), or 0 if set_row() was
        never called.)

        The return value is true if the data type is valid, false otherwise.

        `(self, array: int, column: GeomVertexColumn)`:
        Sets up the rewriter to use the indicated column description on the given
        array.

        This also resets both the read and write row numbers to the start row (the
        same value passed to a previous call to set_row(), or 0 if set_row() was
        never called.)

        The return value is true if the data type is valid, false otherwise.
        """
    @overload
    def set_column(self, column: int) -> bool: ...
    @overload
    def set_column(self, array: int, column: GeomVertexColumn) -> bool: ...
    def clear(self) -> None:
        """Resets the GeomVertexRewriter to the initial state."""
    def get_array(self) -> int:
        """Returns the array index containing the data type that the rewriter is
        working on.
        """
    def get_column(self) -> GeomVertexColumn:
        """Returns the description of the data type that the rewriter is working on."""
    def set_row(self, row: int) -> None:
        """Sets the start, write, and write index to the indicated value.  The
        rewriter will begin traversing from the given row.
        """
    def get_start_row(self) -> int:
        """Returns the row index at which the rewriter started.  It will return to
        this row if you reset the current column.
        """
    def is_at_end(self) -> bool:
        """Returns true if the reader or writer is currently at the end of the list of
        vertices, false otherwise.
        """
    upcastToGeomVertexWriter = upcast_to_GeomVertexWriter
    upcastToGeomVertexReader = upcast_to_GeomVertexReader
    getVertexData = get_vertex_data
    getArrayData = get_array_data
    getArrayHandle = get_array_handle
    getStride = get_stride
    setColumn = set_column  # type: ignore[assignment]
    getArray = get_array
    getColumn = get_column
    setRow = set_row
    getStartRow = get_start_row
    isAtEnd = is_at_end

class SamplerState:
    """Represents a set of settings that indicate how a texture is sampled.  This
    can be used to sample the same texture using different settings in
    different places.
    """

    FT_nearest: Final = 0
    FTNearest: Final = 0
    FT_linear: Final = 1
    FTLinear: Final = 1
    FT_nearest_mipmap_nearest: Final = 2
    FTNearestMipmapNearest: Final = 2
    FT_linear_mipmap_nearest: Final = 3
    FTLinearMipmapNearest: Final = 3
    FT_nearest_mipmap_linear: Final = 4
    FTNearestMipmapLinear: Final = 4
    FT_linear_mipmap_linear: Final = 5
    FTLinearMipmapLinear: Final = 5
    FT_shadow: Final = 6
    FTShadow: Final = 6
    FT_default: Final = 7
    FTDefault: Final = 7
    FT_invalid: Final = 8
    FTInvalid: Final = 8
    WM_clamp: Final = 0
    WMClamp: Final = 0
    WM_repeat: Final = 1
    WMRepeat: Final = 1
    WM_mirror: Final = 2
    WMMirror: Final = 2
    WM_mirror_once: Final = 3
    WMMirrorOnce: Final = 3
    WM_border_color: Final = 4
    WMBorderColor: Final = 4
    WM_invalid: Final = 5
    WMInvalid: Final = 5
    DtoolClassDict: ClassVar[dict[str, Any]]
    wrap_u: _SamplerState_WrapMode
    wrap_v: _SamplerState_WrapMode
    wrap_w: _SamplerState_WrapMode
    minfilter: _SamplerState_FilterType
    magfilter: _SamplerState_FilterType
    anisotropic_degree: int
    border_color: LColor
    min_lod: float
    max_lod: float
    lod_bias: float
    @property
    def effective_minfilter(self) -> _SamplerState_FilterType: ...
    @property
    def effective_magfilter(self) -> _SamplerState_FilterType: ...
    @property
    def effective_anisotropic_degree(self) -> int: ...
    def __init__(self, __param0: SamplerState = ...) -> None:
        """Creates a new SamplerState initialized to the default values."""
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: SamplerState) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def get_default() -> SamplerState:
        """Returns a reference to the global default immutable SamplerState object."""
    def set_wrap_u(self, wrap: _SamplerState_WrapMode) -> None:
        """This setting determines what happens when the SamplerState is sampled with
        a U value outside the range 0.0-1.0.  The default is WM_repeat, which
        indicates that the SamplerState should repeat indefinitely.
        """
    def set_wrap_v(self, wrap: _SamplerState_WrapMode) -> None:
        """This setting determines what happens when the SamplerState is sampled with
        a V value outside the range 0.0-1.0.  The default is WM_repeat, which
        indicates that the SamplerState should repeat indefinitely.
        """
    def set_wrap_w(self, wrap: _SamplerState_WrapMode) -> None:
        """The W wrap direction is only used for 3-d SamplerStates."""
    def set_minfilter(self, filter: _SamplerState_FilterType) -> None:
        """Sets the filtering method that should be used when viewing the SamplerState
        from a distance.
        """
    def set_magfilter(self, filter: _SamplerState_FilterType) -> None:
        """Sets the filtering method that should be used when viewing the SamplerState
        up close.
        """
    def set_anisotropic_degree(self, anisotropic_degree: int) -> None:
        """Specifies the level of anisotropic filtering to apply to the SamplerState.
        Set this 0 to indicate the default value, which is specified in the
        SamplerState-anisotropic-degree config variable.

        To explicitly disable anisotropic filtering, set this value to 1.  To
        explicitly enable anisotropic filtering, set it to a value higher than 1;
        larger numbers indicate greater degrees of filtering.
        """
    def set_border_color(self, color: Vec4Like) -> None:
        """Specifies the solid color of the SamplerState's border.  Some OpenGL
        implementations use a border for tiling SamplerStates; in Panda, it is only
        used for specifying the clamp color.
        """
    def set_min_lod(self, min_lod: float) -> None:
        """Sets the minimum level of detail that will be used when sampling this
        texture.  This may be a negative value.
        """
    def set_max_lod(self, max_lod: float) -> None:
        """Sets the maximum level of detail that will be used when sampling this
        texture.  This may exceed the number of mipmap levels that the texture has.
        """
    def set_lod_bias(self, lod_bias: float) -> None:
        """Sets the value that will be added to the level of detail when sampling the
        texture.  This may be a negative value, although some graphics hardware may
        not support the use of negative LOD values.
        """
    def get_wrap_u(self) -> _SamplerState_WrapMode:
        """Returns the wrap mode of the texture in the U direction."""
    def get_wrap_v(self) -> _SamplerState_WrapMode:
        """Returns the wrap mode of the texture in the V direction."""
    def get_wrap_w(self) -> _SamplerState_WrapMode:
        """Returns the wrap mode of the texture in the W direction.  This is the depth
        direction of 3-d textures.
        """
    def get_minfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for minification.  If this is one of
        the mipmap constants, then the texture requires mipmaps.  This may return
        FT_default; see also get_effective_minfilter().
        """
    def get_magfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for magnification.  The mipmap
        constants are invalid here.  This may return FT_default; see also
        get_effective_minfilter().
        """
    def get_effective_minfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for minification, with special
        treatment for FT_default.  This will normally not return FT_default, unless
        there is an error in the config file.
        """
    def get_effective_magfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for magnification, with special
        treatment for FT_default.  This will normally not return FT_default, unless
        there is an error in the config file.
        """
    def get_anisotropic_degree(self) -> int:
        """Returns the degree of anisotropic filtering that should be applied to the
        texture.  This value may return 0, indicating the default value; see also
        get_effective_anisotropic_degree.
        """
    def get_effective_anisotropic_degree(self) -> int:
        """Returns the degree of anisotropic filtering that should be applied to the
        texture.  This value will normally not return 0, unless there is an error
        in the config file.
        """
    def get_border_color(self) -> LColor:
        """Returns the solid color of the texture's border.  Some OpenGL
        implementations use a border for tiling textures; in Panda, it is only used
        for specifying the clamp color.
        """
    def get_min_lod(self) -> float:
        """Returns the minimum level of detail that will be observed when sampling
        this texture.
        """
    def get_max_lod(self) -> float:
        """Returns the maximum level of detail that will be observed when sampling
        this texture.
        """
    def get_lod_bias(self) -> float:
        """Returns the bias that will be added to the texture level of detail when
        sampling this texture.
        """
    def uses_mipmaps(self) -> bool:
        """Returns true if the minfilter settings on this sampler indicate the use of
        mipmapping, false otherwise.
        """
    @staticmethod
    def is_mipmap(type: _SamplerState_FilterType) -> bool:
        """Returns true if the indicated filter type requires the use of mipmaps, or
        false if it does not.
        """
    @staticmethod
    def format_filter_type(ft: _SamplerState_FilterType) -> str:
        """Returns the indicated FilterType converted to a string word."""
    @staticmethod
    def string_filter_type(str: str) -> _SamplerState_FilterType:
        """Returns the FilterType value associated with the given string
        representation, or FT_invalid if the string does not match any known
        FilterType value.
        """
    @staticmethod
    def format_wrap_mode(wm: _SamplerState_WrapMode) -> str:
        """Returns the indicated WrapMode converted to a string word."""
    @staticmethod
    def string_wrap_mode(str: str) -> _SamplerState_WrapMode:
        """Returns the WrapMode value associated with the given string representation,
        or WM_invalid if the string does not match any known WrapMode value.
        """
    def prepare(self, prepared_objects: PreparedGraphicsObjects) -> None:
        """Indicates that the sampler should be enqueued to be prepared in the
        indicated prepared_objects at the beginning of the next frame.

        Use this function instead of prepare_now() to preload samplers from a user
        interface standpoint.
        """
    def is_prepared(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the sampler has already been prepared or enqueued for
        preparation on the indicated GSG, false otherwise.
        """
    def release(self, prepared_objects: PreparedGraphicsObjects) -> None:
        """Frees the texture context only on the indicated object, if it exists there.
        Returns true if it was released, false if it had not been prepared.
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getDefault = get_default
    setWrapU = set_wrap_u
    setWrapV = set_wrap_v
    setWrapW = set_wrap_w
    setMinfilter = set_minfilter
    setMagfilter = set_magfilter
    setAnisotropicDegree = set_anisotropic_degree
    setBorderColor = set_border_color
    setMinLod = set_min_lod
    setMaxLod = set_max_lod
    setLodBias = set_lod_bias
    getWrapU = get_wrap_u
    getWrapV = get_wrap_v
    getWrapW = get_wrap_w
    getMinfilter = get_minfilter
    getMagfilter = get_magfilter
    getEffectiveMinfilter = get_effective_minfilter
    getEffectiveMagfilter = get_effective_magfilter
    getAnisotropicDegree = get_anisotropic_degree
    getEffectiveAnisotropicDegree = get_effective_anisotropic_degree
    getBorderColor = get_border_color
    getMinLod = get_min_lod
    getMaxLod = get_max_lod
    getLodBias = get_lod_bias
    usesMipmaps = uses_mipmaps
    isMipmap = is_mipmap
    formatFilterType = format_filter_type
    stringFilterType = string_filter_type
    formatWrapMode = format_wrap_mode
    stringWrapMode = string_wrap_mode
    isPrepared = is_prepared
    getClassType = get_class_type

class Texture(TypedWritableReferenceCount, Namable):
    """Represents a texture object, which is typically a single 2-d image but may
    also represent a 1-d or 3-d texture image, or the six 2-d faces of a cube
    map texture.

    A texture's image data might be stored in system RAM (see get_ram_image())
    or its image may be represented in texture memory on one or more
    GraphicsStateGuardians (see prepare()), or both.  The typical usage pattern
    is that a texture is loaded from an image file on disk, which copies its
    image data into system RAM; then the first time the texture is rendered its
    image data is copied to texture memory (actually, to the graphics API), and
    the system RAM image is automatically freed.
    """

    TT_1d_texture: Final = 0
    TT1dTexture: Final = 0
    TT_2d_texture: Final = 1
    TT2dTexture: Final = 1
    TT_3d_texture: Final = 2
    TT3dTexture: Final = 2
    TT_2d_texture_array: Final = 3
    TT2dTextureArray: Final = 3
    TT_cube_map: Final = 4
    TTCubeMap: Final = 4
    TT_buffer_texture: Final = 5
    TTBufferTexture: Final = 5
    TT_cube_map_array: Final = 6
    TTCubeMapArray: Final = 6
    TT_1d_texture_array: Final = 7
    TT1dTextureArray: Final = 7
    T_unsigned_byte: Final = 0
    TUnsignedByte: Final = 0
    T_unsigned_short: Final = 1
    TUnsignedShort: Final = 1
    T_float: Final = 2
    TFloat: Final = 2
    T_unsigned_int_24_8: Final = 3
    TUnsignedInt248: Final = 3
    T_int: Final = 4
    TInt: Final = 4
    T_byte: Final = 5
    TByte: Final = 5
    T_short: Final = 6
    TShort: Final = 6
    T_half_float: Final = 7
    THalfFloat: Final = 7
    T_unsigned_int: Final = 8
    TUnsignedInt: Final = 8
    F_depth_stencil: Final = 1
    FDepthStencil: Final = 1
    F_color_index: Final = 2
    FColorIndex: Final = 2
    F_red: Final = 3
    FRed: Final = 3
    F_green: Final = 4
    FGreen: Final = 4
    F_blue: Final = 5
    FBlue: Final = 5
    F_alpha: Final = 6
    FAlpha: Final = 6
    F_rgb: Final = 7
    FRgb: Final = 7
    F_rgb5: Final = 8
    FRgb5: Final = 8
    F_rgb8: Final = 9
    FRgb8: Final = 9
    F_rgb12: Final = 10
    FRgb12: Final = 10
    F_rgb332: Final = 11
    FRgb332: Final = 11
    F_rgba: Final = 12
    FRgba: Final = 12
    F_rgbm: Final = 13
    FRgbm: Final = 13
    F_rgba4: Final = 14
    FRgba4: Final = 14
    F_rgba5: Final = 15
    FRgba5: Final = 15
    F_rgba8: Final = 16
    FRgba8: Final = 16
    F_rgba12: Final = 17
    FRgba12: Final = 17
    F_luminance: Final = 18
    FLuminance: Final = 18
    F_luminance_alpha: Final = 19
    FLuminanceAlpha: Final = 19
    F_luminance_alphamask: Final = 20
    FLuminanceAlphamask: Final = 20
    F_rgba16: Final = 21
    FRgba16: Final = 21
    F_rgba32: Final = 22
    FRgba32: Final = 22
    F_depth_component: Final = 23
    FDepthComponent: Final = 23
    F_depth_component16: Final = 24
    FDepthComponent16: Final = 24
    F_depth_component24: Final = 25
    FDepthComponent24: Final = 25
    F_depth_component32: Final = 26
    FDepthComponent32: Final = 26
    F_r16: Final = 27
    FR16: Final = 27
    F_rg16: Final = 28
    FRg16: Final = 28
    F_rgb16: Final = 29
    FRgb16: Final = 29
    F_srgb: Final = 30
    FSrgb: Final = 30
    F_srgb_alpha: Final = 31
    FSrgbAlpha: Final = 31
    F_sluminance: Final = 32
    FSluminance: Final = 32
    F_sluminance_alpha: Final = 33
    FSluminanceAlpha: Final = 33
    F_r32i: Final = 34
    FR32i: Final = 34
    F_r32: Final = 35
    FR32: Final = 35
    F_rg32: Final = 36
    FRg32: Final = 36
    F_rgb32: Final = 37
    FRgb32: Final = 37
    F_r8i: Final = 38
    FR8i: Final = 38
    F_rg8i: Final = 39
    FRg8i: Final = 39
    F_rgb8i: Final = 40
    FRgb8i: Final = 40
    F_rgba8i: Final = 41
    FRgba8i: Final = 41
    F_r11_g11_b10: Final = 42
    FR11G11B10: Final = 42
    F_rgb9_e5: Final = 43
    FRgb9E5: Final = 43
    F_rgb10_a2: Final = 44
    FRgb10A2: Final = 44
    F_rg: Final = 45
    FRg: Final = 45
    F_r16i: Final = 46
    FR16i: Final = 46
    F_rg16i: Final = 47
    FRg16i: Final = 47
    F_rgb16i: Final = 48
    FRgb16i: Final = 48
    F_rgba16i: Final = 49
    FRgba16i: Final = 49
    F_rg32i: Final = 50
    FRg32i: Final = 50
    F_rgb32i: Final = 51
    FRgb32i: Final = 51
    F_rgba32i: Final = 52
    FRgba32i: Final = 52
    FT_nearest: Final = 0
    FTNearest: Final = 0
    FT_linear: Final = 1
    FTLinear: Final = 1
    FT_nearest_mipmap_nearest: Final = 2
    FTNearestMipmapNearest: Final = 2
    FT_linear_mipmap_nearest: Final = 3
    FTLinearMipmapNearest: Final = 3
    FT_nearest_mipmap_linear: Final = 4
    FTNearestMipmapLinear: Final = 4
    FT_linear_mipmap_linear: Final = 5
    FTLinearMipmapLinear: Final = 5
    FT_shadow: Final = 6
    FTShadow: Final = 6
    FT_default: Final = 7
    FTDefault: Final = 7
    FT_invalid: Final = 8
    FTInvalid: Final = 8
    WM_clamp: Final = 0
    WMClamp: Final = 0
    WM_repeat: Final = 1
    WMRepeat: Final = 1
    WM_mirror: Final = 2
    WMMirror: Final = 2
    WM_mirror_once: Final = 3
    WMMirrorOnce: Final = 3
    WM_border_color: Final = 4
    WMBorderColor: Final = 4
    WM_invalid: Final = 5
    WMInvalid: Final = 5
    CM_default: Final = 0
    CMDefault: Final = 0
    CM_off: Final = 1
    CMOff: Final = 1
    CM_on: Final = 2
    CMOn: Final = 2
    CM_fxt1: Final = 3
    CMFxt1: Final = 3
    CM_dxt1: Final = 4
    CMDxt1: Final = 4
    CM_dxt2: Final = 5
    CMDxt2: Final = 5
    CM_dxt3: Final = 6
    CMDxt3: Final = 6
    CM_dxt4: Final = 7
    CMDxt4: Final = 7
    CM_dxt5: Final = 8
    CMDxt5: Final = 8
    CM_pvr1_2bpp: Final = 9
    CMPvr12bpp: Final = 9
    CM_pvr1_4bpp: Final = 10
    CMPvr14bpp: Final = 10
    CM_rgtc: Final = 11
    CMRgtc: Final = 11
    CM_etc1: Final = 12
    CMEtc1: Final = 12
    CM_etc2: Final = 13
    CMEtc2: Final = 13
    CM_eac: Final = 14
    CMEac: Final = 14
    QL_default: Final = 0
    QLDefault: Final = 0
    QL_fastest: Final = 1
    QLFastest: Final = 1
    QL_normal: Final = 2
    QLNormal: Final = 2
    QL_best: Final = 3
    QLBest: Final = 3
    clear_color: LColor
    filename: Filename
    alpha_filename: Filename
    fullpath: Filename
    alpha_fullpath: Filename
    x_size: int
    y_size: int
    z_size: int
    num_views: int
    format: _Texture_Format
    component_type: _Texture_ComponentType
    wrap_u: _SamplerState_WrapMode
    wrap_v: _SamplerState_WrapMode
    wrap_w: _SamplerState_WrapMode
    minfilter: _SamplerState_FilterType
    magfilter: _SamplerState_FilterType
    anisotropic_degree: int
    border_color: LColor
    compression: _Texture_CompressionMode
    """Could maybe use has_compression here, too"""
    render_to_texture: bool
    default_sampler: SamplerState
    quality_level: _Texture_QualityLevel
    keep_ram_image: bool
    auto_texture_scale: _AutoTextureScale
    loaded_from_image: bool
    loaded_from_txo: bool
    match_framebuffer_format: bool
    post_load_store_cache: bool
    @property
    def num_pages(self) -> int: ...
    @property
    def num_components(self) -> int: ...
    @property
    def component_width(self) -> int: ...
    @property
    def texture_type(self) -> _Texture_TextureType: ...
    @property
    def usage_hint(self) -> _GeomEnums_UsageHint: ...
    @property
    def effective_minfilter(self) -> _SamplerState_FilterType: ...
    @property
    def effective_magfilter(self) -> _SamplerState_FilterType: ...
    @property
    def effective_anisotropic_degree(self) -> int: ...
    @property
    def effective_quality_level(self) -> _Texture_QualityLevel: ...
    @property
    def expected_num_mipmap_levels(self) -> int: ...
    @property
    def ram_image_size(self) -> int: ...
    @property
    def ram_view_size(self) -> int: ...
    @property
    def ram_page_size(self) -> int: ...
    @property
    def expected_ram_image_size(self) -> int: ...
    @property
    def expected_ram_page_size(self) -> int: ...
    @property
    def ram_image_compression(self) -> _Texture_CompressionMode: ...
    @property
    def cacheable(self) -> bool: ...
    @property
    def num_ram_mipmap_images(self) -> int: ...
    @property
    def num_loadable_ram_mipmap_images(self) -> int: ...
    @property
    def simple_x_size(self) -> int: ...
    @property
    def simple_y_size(self) -> int: ...
    @property
    def simple_ram_image(self) -> CPTA_uchar: ...
    @property
    def properties_modified(self) -> UpdateSeq: ...
    @property
    def image_modified(self) -> UpdateSeq: ...
    @property
    def simple_image_modified(self) -> UpdateSeq: ...
    @property
    def aux_data(self) -> MutableMapping[str, TypedReferenceCount]: ...
    @property
    def orig_file_x_size(self) -> int: ...
    @property
    def orig_file_y_size(self) -> int: ...
    @property
    def orig_file_z_size(self) -> int: ...
    def __init__(self, name: str = ...) -> None:
        """Constructs an empty texture.  The default is to set up the texture as an
        empty 2-d texture; follow up with one of the variants of setup_texture() if
        this is not what you want.
        """
    def __deepcopy__(self, memo) -> Texture: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def make_copy(self) -> Texture:
        """Returns a new copy of the same Texture.  This copy, if applied to geometry,
        will be copied into texture as a separate texture from the original, so it
        will be duplicated in texture memory (and may be independently modified if
        desired).

        If the Texture is a VideoTexture, the resulting duplicate may be animated
        independently of the original.
        """
    def clear(self) -> None:
        """Reinitializes the texture to its default, empty state (except for the
        name).
        """
    def setup_texture(
        self,
        texture_type: _Texture_TextureType,
        x_size: int,
        y_size: int,
        z_size: int,
        component_type: _Texture_ComponentType,
        format: _Texture_Format,
    ) -> None:
        """Sets the texture to the indicated type and dimensions, presumably in
        preparation for calling read() or load(), or set_ram_image() or
        modify_ram_image(), or use set_clear_color to let the texture be cleared to
        a solid color.
        """
    @overload
    def setup_1d_texture(self) -> None:
        """`(self)`:
        Sets the texture as an empty 1-d texture with no dimensions.  Follow up
        with read() or load() to fill the texture properties and image data, or use
        set_clear_color to let the texture be cleared to a solid color.

        `(self, x_size: int, component_type: _Texture_ComponentType, format: _Texture_Format)`:
        Sets the texture as an empty 1-d texture with the specified dimensions and
        properties.  Follow up with set_ram_image() or modify_ram_image() to fill
        the image data, or use set_clear_color to let the texture be cleared to a
        solid color.
        """
    @overload
    def setup_1d_texture(self, x_size: int, component_type: _Texture_ComponentType, format: _Texture_Format) -> None: ...
    @overload
    def setup_2d_texture(self) -> None:
        """`(self)`:
        Sets the texture as an empty 2-d texture with no dimensions.  Follow up
        with read() or load() to fill the texture properties and image data, or use
        set_clear_color to let the texture be cleared to a solid color.

        `(self, x_size: int, y_size: int, component_type: _Texture_ComponentType, format: _Texture_Format)`:
        Sets the texture as an empty 2-d texture with the specified dimensions and
        properties.  Follow up with set_ram_image() or modify_ram_image() to fill
        the image data, or use set_clear_color to let the texture be cleared to a
        solid color.
        """
    @overload
    def setup_2d_texture(
        self, x_size: int, y_size: int, component_type: _Texture_ComponentType, format: _Texture_Format
    ) -> None: ...
    @overload
    def setup_3d_texture(self, z_size: int = ...) -> None:
        """`(self, z_size: int = ...)`:
        Sets the texture as an empty 3-d texture with no dimensions (though if you
        know the depth ahead of time, it saves a bit of reallocation later). Follow
        up with read() or load() to fill the texture properties and image data, or
        use set_clear_color to let the texture be cleared to a solid color.

        `(self, x_size: int, y_size: int, z_size: int, component_type: _Texture_ComponentType, format: _Texture_Format)`:
        Sets the texture as an empty 3-d texture with the specified dimensions and
        properties.  Follow up with set_ram_image() or modify_ram_image() to fill
        the image data.
        """
    @overload
    def setup_3d_texture(
        self, x_size: int, y_size: int, z_size: int, component_type: _Texture_ComponentType, format: _Texture_Format
    ) -> None: ...
    @overload
    def setup_cube_map(self) -> None:
        """`(self)`:
        Sets the texture as an empty cube map texture with no dimensions.  Follow
        up with read() or load() to fill the texture properties and image data, or
        use set_clear_color to let the texture be cleared to a solid color.

        `(self, size: int, component_type: _Texture_ComponentType, format: _Texture_Format)`:
        Sets the texture as an empty cube map texture with the specified dimensions
        and properties.  Follow up with set_ram_image() or modify_ram_image() to
        fill the image data, or use set_clear_color to let the texture be cleared
        to a solid color.

        Note that a cube map should always consist of six square images, so x_size
        and y_size will be the same, and z_size is always 6.
        """
    @overload
    def setup_cube_map(self, size: int, component_type: _Texture_ComponentType, format: _Texture_Format) -> None: ...
    @overload
    def setup_2d_texture_array(self, z_size: int = ...) -> None:
        """`(self, z_size: int = ...)`:
        Sets the texture as an empty 2-d texture array with no dimensions (though
        if you know the depth ahead of time, it saves a bit of reallocation later).
        Follow up with read() or load() to fill the texture properties and image
        data, or use set_clear_color to let the texture be cleared to a solid
        color.

        `(self, x_size: int, y_size: int, z_size: int, component_type: _Texture_ComponentType, format: _Texture_Format)`:
        Sets the texture as an empty 2-d texture array with the specified
        dimensions and properties.  Follow up with set_ram_image() or
        modify_ram_image() to fill the image data, or use set_clear_color to let
        the texture be cleared to a solid color.
        """
    @overload
    def setup_2d_texture_array(
        self, x_size: int, y_size: int, z_size: int, component_type: _Texture_ComponentType, format: _Texture_Format
    ) -> None: ...
    @overload
    def setup_cube_map_array(self, num_cube_maps: int) -> None:
        """`(self, num_cube_maps: int)`:
        Sets the texture as cube map array with N cube maps.  Note that this number
        is not the same as the z_size.  Follow up with read() or load() to fill the
        texture properties and image data, or use set_clear_color to let the
        texture be cleared to a solid color.

        @since 1.10.0

        `(self, size: int, num_cube_maps: int, component_type: _Texture_ComponentType, format: _Texture_Format)`:
        Sets the texture as cube map array with N cube maps with the specified
        dimensions and format.  Follow up with set_ram_image() or
        modify_ram_image() to fill the image data, or use set_clear_color to let
        the texture be cleared to a solid color.

        The num_cube_maps given here is multiplied by six to become the z_size of
        the image.

        @since 1.10.0
        """
    @overload
    def setup_cube_map_array(
        self, size: int, num_cube_maps: int, component_type: _Texture_ComponentType, format: _Texture_Format
    ) -> None: ...
    def setup_buffer_texture(
        self, size: int, component_type: _Texture_ComponentType, format: _Texture_Format, usage: _GeomEnums_UsageHint
    ) -> None:
        """Sets the texture as an empty buffer texture with the specified size and
        properties.  Follow up with set_ram_image() or modify_ram_image() to fill
        the image data, or use set_clear_color to let the texture be cleared to a
        solid color.

        Note that a buffer texture's format needs to match the component type.
        """
    def generate_normalization_cube_map(self, size: int) -> None:
        """Generates a special cube map image in the texture that can be used to apply
        bump mapping effects: for each texel in the cube map that is indexed by the
        3-d texture coordinates (x, y, z), the resulting value is the normalized
        vector (x, y, z) (compressed from -1..1 into 0..1).
        """
    def generate_alpha_scale_map(self) -> None:
        """Generates a special 256x1 1-d texture that can be used to apply an
        arbitrary alpha scale to objects by judicious use of texture matrix.  The
        texture is a gradient, with an alpha of 0 on the left (U = 0), and 255 on
        the right (U = 1).
        """
    def clear_image(self) -> None:
        """Clears the texture data without changing its format or resolution.  The
        texture is cleared on both the graphics hardware and from RAM, unlike
        clear_ram_image, which only removes the data from RAM.

        If a clear color has been specified using set_clear_color, the texture will
        be cleared using a solid color.

        The texture data will be cleared the first time in which the texture is
        used after this method is called.
        """
    def has_clear_color(self) -> bool:
        """Returns true if a color was previously set using set_clear_color."""
    def get_clear_color(self) -> LColor:
        """Returns the color that was previously set using set_clear_color."""
    def set_clear_color(self, color: Vec4Like) -> None:
        """Sets the color that will be used to fill the texture image in absence of
        any image data.  It is used when any of the setup_texture functions or
        clear_image is called and image data is not provided using read() or
        modify_ram_image().

        This does not affect a texture that has already been cleared; call
        clear_image to clear it again.
        """
    def clear_clear_color(self) -> None:
        """The opposite of set_clear_color.  If the image is cleared after setting
        this, its contents may be undefined (or may in fact not be cleared at all).
        """
    def get_clear_data(self) -> bytes:
        """Returns the raw image data for a single pixel if it were set to the clear
        color.
        """
    @overload
    def read(self, fullpath: StrOrBytesPath, options: LoaderOptions = ...) -> bool:
        """`(self, fullpath: Filename, alpha_fullpath: Filename, primary_file_num_channels: int, alpha_file_channel: int, options: LoaderOptions = ...)`:
        Combine a 3-component image with a grayscale image to get a 4-component
        image.

        See the description of the full-parameter read() method for the meaning of
        the primary_file_num_channels and alpha_file_channel parameters.

        `(self, fullpath: Filename, alpha_fullpath: Filename, primary_file_num_channels: int, alpha_file_channel: int, z: int, n: int, read_pages: bool, read_mipmaps: bool, record: BamCacheRecord = ..., options: LoaderOptions = ...)`:
        Reads the texture from the indicated filename.  If
        primary_file_num_channels is not 0, it specifies the number of components
        to downgrade the image to if it is greater than this number.

        If the filename has the extension .txo, this implicitly reads a texture
        object instead of a filename (which replaces all of the texture
        properties).  In this case, all the rest of the parameters are ignored, and
        the filename should not contain any hash marks; just the one named file
        will be read, since a single .txo file can contain all pages and mipmaps
        necessary to define a texture.

        If alpha_fullpath is not empty, it specifies the name of a file from which
        to retrieve the alpha.  In this case, alpha_file_channel represents the
        numeric channel of this image file to use as the resulting texture's alpha
        channel; usually, this is 0 to indicate the grayscale combination of r, g,
        b; or it may be a one-based channel number, e.g.  1 for the red channel, 2
        for the green channel, and so on.

        If read pages is false, then z indicates the page number into which this
        image will be assigned.  Normally this is 0 for the first (or only) page of
        the texture.  3-D textures have one page for each level of depth, and cube
        map textures always have six pages.

        If read_pages is true, multiple images will be read at once, one for each
        page of a cube map or a 3-D texture.  In this case, the filename should
        contain a sequence of one or more hash marks ("#") which will be filled in
        with the z value of each page, zero-based.  In this case, the z parameter
        indicates the maximum z value that will be loaded, or 0 to load all
        filenames that exist.

        If read_mipmaps is false, then n indicates the mipmap level to which this
        image will be assigned.  Normally this is 0 for the base texture image, but
        it is possible to load custom mipmap levels into the later images.  After
        the base texture image is loaded (thus defining the size of the texture),
        you can call get_expected_num_mipmap_levels() to determine the maximum
        sensible value for n.

        If read_mipmaps is true, multiple images will be read as above, but this
        time the images represent the different mipmap levels of the texture image.
        In this case, the n parameter indicates the maximum n value that will be
        loaded, or 0 to load all filenames that exist (up to the expected number of
        mipmap levels).

        If both read_pages and read_mipmaps is true, then both sequences will be
        read; the filename should contain two sequences of hash marks, separated by
        some character such as a hyphen, underscore, or dot.  The first hash mark
        sequence will be filled in with the mipmap level, while the second hash
        mark sequence will be the page index.

        This method implicitly sets keep_ram_image to false.

        `(self, fullpath: Filename, options: LoaderOptions = ...)`:
        Reads the named filename into the texture.

        `(self, fullpath: Filename, z: int, n: int, read_pages: bool, read_mipmaps: bool, options: LoaderOptions = ...)`:
        Reads a single file into a single page or mipmap level, or automatically
        reads a series of files into a series of pages and/or mipmap levels.

        See the description of the full-parameter read() method for the meaning of
        the various parameters.
        """
    @overload
    def read(
        self,
        fullpath: StrOrBytesPath,
        alpha_fullpath: StrOrBytesPath,
        primary_file_num_channels: int,
        alpha_file_channel: int,
        options: LoaderOptions = ...,
    ) -> bool: ...
    @overload
    def read(
        self, fullpath: StrOrBytesPath, z: int, n: int, read_pages: bool, read_mipmaps: bool, options: LoaderOptions = ...
    ) -> bool: ...
    @overload
    def read(
        self,
        fullpath: StrOrBytesPath,
        alpha_fullpath: StrOrBytesPath,
        primary_file_num_channels: int,
        alpha_file_channel: int,
        z: int,
        n: int,
        read_pages: bool,
        read_mipmaps: bool,
        record: BamCacheRecord = ...,
        options: LoaderOptions = ...,
    ) -> bool: ...
    @overload
    def write(self, fullpath: StrOrBytesPath) -> bool:
        """`(self, fullpath: Filename)`:
        Writes the texture to the named filename.

        `(self, fullpath: Filename, z: int, n: int, write_pages: bool, write_mipmaps: bool)`:
        Writes a single page or mipmap level to a single file, or automatically
        writes a series of pages and/or mipmap levels to a numbered series of
        files.

        If the filename ends in the extension .txo, this implicitly writes a Panda
        texture object (.txo) instead of an image file.  In this case, the
        remaining parameters are ignored, and only one file is written, which will
        contain all of the pages and resident mipmap levels in the texture.

        If write_pages is false, then z indicates the page number to write.  3-D
        textures have one page number for each level of depth; cube maps have six
        pages number 0 through 5.  Other kinds of textures have only one page,
        numbered 0.  If there are multiple views, the range of z is increased; the
        total range is [0, get_num_pages()).

        If write_pages is true, then all pages of the texture will be written.  In
        this case z is ignored, and the filename should contain a sequence of hash
        marks ("#") which will be filled in with the page index number.

        If write_mipmaps is false, then n indicates the mipmap level number to
        write.  Normally, this is 0, for the base texture image.  Normally, the
        mipmap levels of a texture are not available in RAM (they are generated
        automatically by the graphics card). However, if you have the mipmap levels
        available, for instance because you called generate_ram_mipmap_images() to
        generate them internally, or you called
        GraphicsEngine::extract_texture_data() to retrieve them from the graphics
        card, then you may write out each mipmap level with this parameter.

        If write_mipmaps is true, then all mipmap levels of the texture will be
        written.  In this case n is ignored, and the filename should contain a
        sequence of hash marks ("#") which will be filled in with the mipmap level
        number.

        If both write_pages and write_mipmaps is true, then all pages and all
        mipmap levels will be written.  In this case, the filename should contain
        two different sequences of hash marks, separated by a character such as a
        hyphen, underscore, or dot.  The first hash mark sequence will be filled in
        with the mipmap level, while the second hash mark sequence will be the page
        index.

        `(self, out: ostream, indent_level: int)`:
        Not to be confused with write(Filename), this method simply describes the
        texture properties.
        """
    @overload
    def write(self, out: ostream, indent_level: int) -> None: ...
    @overload
    def write(self, fullpath: StrOrBytesPath, z: int, n: int, write_pages: bool, write_mipmaps: bool) -> bool: ...
    def read_txo(self, _in: istream, filename: str = ...) -> bool:
        """Reads the texture from a Panda texture object.  This defines the complete
        Texture specification, including the image data as well as all texture
        properties.  This only works if the txo file contains a static Texture
        image, as opposed to a subclass of Texture such as a movie texture.

        Pass a real filename if it is available, or empty string if it is not.
        """
    @staticmethod
    def make_from_txo(_in: istream, filename: str = ...) -> Texture:
        """Constructs a new Texture object from the txo file.  This is similar to
        Texture::read_txo(), but it constructs and returns a new object, which
        allows it to return a subclass of Texture (for instance, a movie texture).

        Pass a real filename if it is available, or empty string if it is not.
        """
    def write_txo(self, out: ostream, filename: str = ...) -> bool:
        """Writes the texture to a Panda texture object.  This defines the complete
        Texture specification, including the image data as well as all texture
        properties.

        The filename is just for reference.
        """
    def read_dds(self, _in: istream, filename: str = ..., header_only: bool = ...) -> bool:
        """Reads the texture from a DDS file object.  This is a Microsoft-defined file
        format; it is similar in principle to a txo object, in that it is designed
        to contain the texture image in a form as similar as possible to its
        runtime image, and it can contain mipmaps, pre-compressed textures, and so
        on.

        As with read_txo, the filename is just for reference.
        """
    def read_ktx(self, _in: istream, filename: str = ..., header_only: bool = ...) -> bool:
        """Reads the texture from a KTX file object.  This is a Khronos-defined file
        format; it is similar in principle to a dds object, in that it is designed
        to contain the texture image in a form as similar as possible to its
        runtime image, and it can contain mipmaps, pre-compressed textures, and so
        on.

        As with read_dds, the filename is just for reference.
        """
    @overload
    def load(self, pnmimage: PNMImage, options: LoaderOptions = ...) -> bool:
        """`(self, pnmimage: PNMImage, options: LoaderOptions = ...)`; `(self, pfm: PfmFile, options: LoaderOptions = ...)`:
        Replaces the texture with the indicated image.

        `(self, pnmimage: PNMImage, z: int, n: int, options: LoaderOptions = ...)`; `(self, pfm: PfmFile, z: int, n: int, options: LoaderOptions = ...)`:
        Stores the indicated image in the given page and mipmap level.  See read().
        """
    @overload
    def load(self, pfm: PfmFile, options: LoaderOptions = ...) -> bool: ...
    @overload
    def load(self, pnmimage: PNMImage, z: int, n: int, options: LoaderOptions = ...) -> bool: ...
    @overload
    def load(self, pfm: PfmFile, z: int, n: int, options: LoaderOptions = ...) -> bool: ...
    def load_sub_image(self, pnmimage: PNMImage, x: int, y: int, z: int = ..., n: int = ...) -> bool:
        """Stores the indicated image in a region of the texture.  The texture
        properties remain unchanged.  This can be more efficient than updating an
        entire texture, but has a few restrictions: for one, you must ensure that
        the texture is still in RAM (eg.  using set_keep_ram_image) and it may not
        be compressed.
        """
    @overload
    def store(self, pnmimage: PNMImage) -> bool:
        """`(self, pnmimage: PNMImage)`:
        Saves the texture to the indicated PNMImage, but does not write it to disk.

        `(self, pnmimage: PNMImage, z: int, n: int)`:
        Saves the indicated page and mipmap level of the texture to the PNMImage.

        `(self, pfm: PfmFile)`:
        Saves the texture to the indicated PfmFile, but does not write it to disk.

        `(self, pfm: PfmFile, z: int, n: int)`:
        Saves the indicated page and mipmap level of the texture to the PfmFile.
        """
    @overload
    def store(self, pfm: PfmFile) -> bool: ...
    @overload
    def store(self, pnmimage: PNMImage, z: int, n: int) -> bool: ...
    @overload
    def store(self, pfm: PfmFile, z: int, n: int) -> bool: ...
    def reload(self) -> bool:
        """Re-reads the Texture from its disk file.  Useful when you know the image on
        disk has recently changed, and you want to update the Texture image.

        Returns true on success, false on failure (in which case, the Texture may
        or may not still be valid).
        """
    def load_related(self, suffix: InternalName | str) -> Texture:
        """Loads a texture whose filename is derived by concatenating a suffix to the
        filename of this texture.  May return NULL, for example, if this texture
        doesn't have a filename.
        """
    def has_filename(self) -> bool:
        """Returns true if the filename has been set and is available.  See
        set_filename().
        """
    def get_filename(self) -> Filename:
        """Returns the filename that has been set.  This is the name of the file as it
        was requested.  Also see get_fullpath().
        """
    def set_filename(self, filename: StrOrBytesPath) -> None:
        """Sets the name of the file that contains the image's contents.  Normally,
        this is set automatically when the image is loaded, for instance via
        Texture::read().

        The Texture's get_name() function used to return the filename, but now
        returns just the basename (without the extension), which is a more useful
        name for identifying an image in show code.
        """
    def clear_filename(self) -> None:
        """Removes the alpha filename, if it was previously set.  See set_filename()."""
    def has_alpha_filename(self) -> bool:
        """Returns true if the alpha_filename has been set and is available.  See
        set_alpha_filename().
        """
    def get_alpha_filename(self) -> Filename:
        """Returns the alpha_filename that has been set.  If this is set, it
        represents the name of the alpha component, which is stored in a separate
        file.  See also get_filename(), and get_alpha_fullpath().
        """
    def set_alpha_filename(self, alpha_filename: StrOrBytesPath) -> None:
        """Sets the name of the file that contains the image's alpha channel contents.
        Normally, this is set automatically when the image is loaded, for instance
        via Texture::read().

        The Texture's get_filename() function returns the name of the image file
        that was loaded into the buffer.  In the case where a texture specified two
        separate files to load, a 1- or 3-channel color image and a 1-channel alpha
        image, this Filename is update to contain the name of the image file that
        was loaded into the buffer's alpha channel.
        """
    def clear_alpha_filename(self) -> None:
        """Removes the alpha filename, if it was previously set.  See
        set_alpha_filename().
        """
    def has_fullpath(self) -> bool:
        """Returns true if the fullpath has been set and is available.  See
        set_fullpath().
        """
    def get_fullpath(self) -> Filename:
        """Returns the fullpath that has been set.  This is the full path to the file
        as it was found along the texture search path.
        """
    def set_fullpath(self, fullpath: StrOrBytesPath) -> None:
        """Sets the full pathname to the file that contains the image's contents, as
        found along the search path.  Normally, this is set automatically when the
        image is loaded, for instance via Texture::read().
        """
    def clear_fullpath(self) -> None:
        """Removes the alpha fullpath, if it was previously set.  See set_fullpath()."""
    def has_alpha_fullpath(self) -> bool:
        """Returns true if the alpha_fullpath has been set and is available.  See
        set_alpha_fullpath().
        """
    def get_alpha_fullpath(self) -> Filename:
        """Returns the alpha_fullpath that has been set.  This is the full path to the
        alpha part of the image file as it was found along the texture search path.
        """
    def set_alpha_fullpath(self, alpha_fullpath: StrOrBytesPath) -> None:
        """Sets the full pathname to the file that contains the image's alpha channel
        contents, as found along the search path.  Normally, this is set
        automatically when the image is loaded, for instance via Texture::read().
        """
    def clear_alpha_fullpath(self) -> None:
        """Removes the alpha fullpath, if it was previously set.  See
        set_alpha_fullpath().
        """
    def get_x_size(self) -> int:
        """Returns the width of the texture image in texels."""
    def set_x_size(self, x_size: int) -> None:
        """Changes the x size indicated for the texture.  This also implicitly unloads
        the texture if it has already been loaded.
        """
    def get_y_size(self) -> int:
        """Returns the height of the texture image in texels.  For a 1-d texture, this
        will be 1.
        """
    def set_y_size(self, y_size: int) -> None:
        """Changes the y size indicated for the texture.  This also implicitly unloads
        the texture if it has already been loaded.
        """
    def get_z_size(self) -> int:
        """Returns the depth of the texture image in texels.  For a 1-d texture or 2-d
        texture, this will be 1. For a cube map texture, this will be 6.
        """
    def set_z_size(self, z_size: int) -> None:
        """Changes the z size indicated for the texture.  This also implicitly unloads
        the texture if it has already been loaded.
        """
    def get_num_views(self) -> int:
        """Returns the number of "views" in the texture.  A view is a completely
        separate image stored within the Texture object.  Most textures have only
        one view, but a stereo texture, for instance, may have two views, a left
        and a right image.  Other uses for multiple views are not yet defined.

        If this value is greater than one, the additional views are accessed as
        additional pages beyond get_z_size().
        """
    def set_num_views(self, num_views: int) -> None:
        """Sets the number of "views" within a texture.  A view is a completely
        separate image stored within the Texture object.  Most textures have only
        one view, but a stereo texture, for instance, may have two views, a left
        and a right image.  Other uses for multiple views are not yet defined.

        If this value is greater than one, the additional views are accessed as
        additional pages beyond get_z_size().

        This also implicitly unloads the texture if it has already been loaded.
        """
    def get_num_pages(self) -> int:
        """Returns the total number of pages in the texture.  Each "page" is a 2-d
        texture image within the larger image--a face of a cube map, or a level of
        a 3-d texture.  Normally, get_num_pages() is the same as get_z_size().
        However, in a multiview texture, this returns get_z_size() *
        get_num_views().
        """
    def get_num_components(self) -> int:
        """Returns the number of color components for each texel of the texture image.
        This is 3 for an rgb texture or 4 for an rgba texture; it may also be 1 or
        2 for a grayscale texture.
        """
    def get_component_width(self) -> int:
        """Returns the number of bytes stored for each color component of a texel.
        Typically this is 1, but it may be 2 for 16-bit texels.
        """
    def get_texture_type(self) -> _Texture_TextureType:
        """Returns the overall interpretation of the texture."""
    def get_usage_hint(self) -> _GeomEnums_UsageHint:
        """Returns the usage hint specified for buffer textures, or UH_unspecified for
        all other texture types.
        """
    def get_format(self) -> _Texture_Format:
        """Returns the format of the texture, which represents both the semantic
        meaning of the texels and, to some extent, their storage information.
        """
    def set_format(self, format: _Texture_Format) -> None:
        """Changes the format value for the texture components.  This implicitly sets
        num_components as well.
        """
    def get_component_type(self) -> _Texture_ComponentType:
        """Returns the numeric interpretation of each component of the texture."""
    def set_component_type(self, component_type: _Texture_ComponentType) -> None:
        """Changes the data value for the texture components.  This implicitly sets
        component_width as well.
        """
    def get_wrap_u(self) -> _SamplerState_WrapMode:
        """Returns the wrap mode of the texture in the U direction.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_wrap_u(self, wrap: _SamplerState_WrapMode) -> None: ...
    def get_wrap_v(self) -> _SamplerState_WrapMode:
        """Returns the wrap mode of the texture in the V direction.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_wrap_v(self, wrap: _SamplerState_WrapMode) -> None: ...
    def get_wrap_w(self) -> _SamplerState_WrapMode:
        """Returns the wrap mode of the texture in the W direction.  This is the depth
        direction of 3-d textures.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_wrap_w(self, wrap: _SamplerState_WrapMode) -> None: ...
    def get_minfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for minification.  If this is one of
        the mipmap constants, then the texture requires mipmaps.  This may return
        FT_default; see also get_effective_minfilter().

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def get_effective_minfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for minification, with special
        treatment for FT_default.  This will normally not return FT_default, unless
        there is an error in the config file.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_minfilter(self, filter: _SamplerState_FilterType) -> None: ...
    def get_magfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for magnification.  The mipmap
        constants are invalid here.  This may return FT_default; see also
        get_effective_minfilter().

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def get_effective_magfilter(self) -> _SamplerState_FilterType:
        """Returns the filter mode of the texture for magnification, with special
        treatment for FT_default.  This will normally not return FT_default, unless
        there is an error in the config file.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_magfilter(self, filter: _SamplerState_FilterType) -> None: ...
    def get_anisotropic_degree(self) -> int:
        """Returns the degree of anisotropic filtering that should be applied to the
        texture.  This value may return 0, indicating the default value; see also
        get_effective_anisotropic_degree.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def get_effective_anisotropic_degree(self) -> int:
        """Returns the degree of anisotropic filtering that should be applied to the
        texture.  This value will normally not return 0, unless there is an error
        in the config file.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_anisotropic_degree(self, anisotropic_degree: int) -> None:
        """Specifies the level of anisotropic filtering to apply to the texture.  Set
        this 0 to indicate the default value, which is specified in the texture-
        anisotropic-degree config variable.

        To explicitly disable anisotropic filtering, set this value to 1.  To
        explicitly enable anisotropic filtering, set it to a value higher than 1;
        larger numbers indicate greater degrees of filtering.

        This sets the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def get_border_color(self) -> LColor:
        """Returns the solid color of the texture's border.  Some OpenGL
        implementations use a border for tiling textures; in Panda, it is only used
        for specifying the clamp color.

        This returns the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_border_color(self, color: Vec4Like) -> None:
        """Specifies the solid color of the texture's border.  Some OpenGL
        implementations use a border for tiling textures; in Panda, it is only used
        for specifying the clamp color.

        This sets the default sampler state for this texture; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def has_compression(self) -> bool:
        """Returns true if the texture indicates it wants to be compressed, either
        with CM_on or higher, or CM_default and compressed-textures is true.

        If true returned, this is not a guarantee that the texture is actually
        successfully compressed on the GSG.  It may be that the GSG does not
        support the requested compression mode, in which case the texture may
        actually be stored uncompressed in texture memory.
        """
    def get_compression(self) -> _Texture_CompressionMode:
        """Returns the compression mode requested for this particular texture, or
        CM_off if the texture is not to be compressed.

        If a value other than CM_off is returned, this is not a guarantee that the
        texture is actually successfully compressed on the GSG.  It may be that the
        GSG does not support the requested compression mode, in which case the
        texture may actually be stored uncompressed in texture memory.
        """
    def set_compression(self, compression: _Texture_CompressionMode) -> None:
        """Requests that this particular Texture be compressed when it is loaded into
        texture memory.

        This refers to the internal compression of the texture image within texture
        memory; it is not related to jpeg or png compression, which are disk file
        compression formats.  The actual disk file that generated this texture may
        be stored in a compressed or uncompressed format supported by Panda; it
        will be decompressed on load, and then recompressed by the graphics API if
        this parameter is not CM_off.

        If the GSG does not support this texture compression mode, the texture will
        silently be loaded uncompressed.
        """
    def get_render_to_texture(self) -> bool:
        """Returns a flag on the texture that indicates whether the texture is
        intended to be used as a direct-render target, by binding a framebuffer to
        a texture and rendering directly into the texture.

        Normally, a user should not need to set this flag directly; it is set
        automatically by the low-level display code when a texture is bound to a
        framebuffer.
        """
    def set_render_to_texture(self, render_to_texture: bool) -> None:
        """Sets a flag on the texture that indicates whether the texture is intended
        to be used as a direct-render target, by binding a framebuffer to a texture
        and rendering directly into the texture.

        This controls some low-level choices made about the texture object itself.
        For instance, compressed textures are disallowed when this flag is set
        true.

        Normally, a user should not need to set this flag directly; it is set
        automatically by the low-level display code when a texture is bound to a
        framebuffer.
        """
    def get_default_sampler(self) -> SamplerState:
        """This returns the default sampler state for this texture, containing the
        wrap and filter properties specified on the texture level; it may still be
        overridden by a sampler state specified at a higher level.
        """
    def set_default_sampler(self, sampler: SamplerState) -> None:
        """This sets the default sampler state for this texture, containing the wrap
        and filter properties specified on the texture level; it may still be
        overridden by a sampler state specified at a higher level.  This
        encompasses the settings for get_wrap_u, get_minfilter,
        get_anisotropic_degree, etc.

        This makes a copy of the SamplerState object, so future modifications of
        the same SamplerState will have no effect on this texture unless you call
        set_default_sampler again.
        """
    def uses_mipmaps(self) -> bool:
        """Returns true if the minfilter settings on this texture indicate the use of
        mipmapping, false otherwise.
        """
    def get_quality_level(self) -> _Texture_QualityLevel:
        """Returns the current quality_level hint.  See set_quality_level().  This
        value may return QL_default; see get_effective_quality_level().
        """
    def get_effective_quality_level(self) -> _Texture_QualityLevel:
        """Returns the current quality_level hint, or the global default quality_level
        if this texture doesn't specify a quality level.  This value will not
        normally return QL_default (unless there is an error in the config file)
        """
    def set_quality_level(self, quality_level: _Texture_QualityLevel) -> None:
        """Sets a hint to the renderer about the desired performance / quality
        tradeoff for this particular texture.  This is most useful for the
        tinydisplay software renderer; for normal, hardware-accelerated renderers,
        this may have little or no effect.
        """
    def get_expected_num_mipmap_levels(self) -> int:
        """Returns the number of mipmap levels that should be defined for this
        texture, given the texture's size.

        Note that this returns a number appropriate for mipmapping, even if the
        texture does not currently have mipmapping enabled.
        """
    def get_expected_mipmap_x_size(self, n: int) -> int:
        """Returns the x_size that the nth mipmap level should have, based on the
        texture's size.
        """
    def get_expected_mipmap_y_size(self, n: int) -> int:
        """Returns the y_size that the nth mipmap level should have, based on the
        texture's size.
        """
    def get_expected_mipmap_z_size(self, n: int) -> int:
        """Returns the z_size that the nth mipmap level should have, based on the
        texture's size.
        """
    def get_expected_mipmap_num_pages(self, n: int) -> int:
        """Returns the total number of pages that the nth mipmap level should have,
        based on the texture's size.  This is usually the same as
        get_expected_mipmap_z_size(), except for a multiview texture, in which case
        it is get_expected_mipmap_z_size() * get_num_views().
        """
    def has_ram_image(self) -> bool:
        """Returns true if the Texture has its image contents available in main RAM,
        false if it exists only in texture memory or in the prepared GSG context.

        Note that this has nothing to do with whether get_ram_image() will fail or
        not.  Even if has_ram_image() returns false, get_ram_image() may still
        return a valid RAM image, because get_ram_image() will automatically load
        the texture from disk if necessary.  The only thing has_ram_image() tells
        you is whether the texture is available right now without hitting the disk
        first.

        Note also that if an application uses only one GSG, it may appear that
        has_ram_image() returns true if the texture has not yet been loaded by the
        GSG, but this correlation is not true in general and should not be depended
        on.  Specifically, if an application ever uses multiple GSG's in its
        lifetime (for instance, by opening more than one window, or by closing its
        window and opening another one later), then has_ram_image() may well return
        false on textures that have never been loaded on the current GSG.
        """
    def has_uncompressed_ram_image(self) -> bool:
        """Returns true if the Texture has its image contents available in main RAM
        and is uncompressed, false otherwise.  See has_ram_image().
        """
    def might_have_ram_image(self) -> bool:
        """Returns true if the texture's image contents are currently available in
        main RAM, or there is reason to believe it can be loaded on demand.  That
        is, this function returns a "best guess" as to whether get_ram_image() will
        succeed without actually calling it first.
        """
    def get_ram_image_size(self) -> int:
        """Returns the total number of bytes used by the in-memory image, across all
        pages and views, or 0 if there is no in-memory image.
        """
    def get_ram_view_size(self) -> int:
        """Returns the number of bytes used by the in-memory image per view, or 0 if
        there is no in-memory image.  Since each view is a stack of z_size pages,
        this is get_z_size() * get_ram_page_size().
        """
    def get_ram_page_size(self) -> int:
        """Returns the number of bytes used by the in-memory image per page, or 0 if
        there is no in-memory image.

        For a non-compressed texture, this is the same as
        get_expected_ram_page_size().  For a compressed texture, this may be a
        smaller value.  (We do assume that all pages will be the same size on a
        compressed texture).
        """
    def get_expected_ram_image_size(self) -> int:
        """Returns the number of bytes that *ought* to be used by the in-memory image,
        based on the texture parameters.
        """
    def get_expected_ram_page_size(self) -> int:
        """Returns the number of bytes that should be used per each Z page of the 3-d
        texture.  For a 2-d or 1-d texture, this is the same as
        get_expected_ram_image_size().
        """
    def get_ram_image(self) -> CPTA_uchar:
        """Returns the system-RAM image data associated with the texture.  If the
        texture does not currently have an associated RAM image, and the texture
        was generated by loading an image from a disk file (the most common case),
        this forces the reload of the same texture.  This can happen if
        keep_texture_ram is configured to false, and we have previously prepared
        this texture with a GSG.

        Note that it is not correct to call has_ram_image() first to test whether
        this function will fail.  A false return value from has_ram_image()
        indicates only that get_ram_image() may need to reload the texture from
        disk, which it will do automatically.  However, you can call
        might_have_ram_image(), which will return true if the ram image exists, or
        there is a reasonable reason to believe it can be loaded.

        On the other hand, it is possible that the texture cannot be found on disk
        or is otherwise unavailable.  If that happens, this function will return
        NULL. There is no way to predict with 100% accuracy whether get_ram_image()
        will return NULL without calling it first; might_have_ram_image() is the
        closest.
        """
    def get_ram_image_compression(self) -> _Texture_CompressionMode:
        """Returns the compression mode in which the ram image is already stored pre-
        compressed.  If this is other than CM_off, you cannot rely on the contents
        of the ram image to be anything predicatable (it will not be an array of x
        by y pixels, and it probably won't have the same length as
        get_expected_ram_image_size()).
        """
    def get_uncompressed_ram_image(self) -> CPTA_uchar:
        """Returns the system-RAM image associated with the texture, in an
        uncompressed form if at all possible.

        If get_ram_image_compression() is CM_off, then the system-RAM image is
        already uncompressed, and this returns the same thing as get_ram_image().

        If get_ram_image_compression() is anything else, then the system-RAM image
        is compressed.  In this case, the image will be reloaded from the
        *original* file (not from the cache), in the hopes that an uncompressed
        image will be found there.

        If an uncompressed image cannot be found, returns NULL.
        """
    def get_ram_image_as(self, requested_format: str) -> CPTA_uchar:
        """Returns the uncompressed system-RAM image data associated with the texture.
        Rather than just returning a pointer to the data, like
        get_uncompressed_ram_image, this function first processes the data and
        reorders the components using the specified format string, and places these
        into a new char array.

        The 'format' argument should specify in which order the components of the
        texture must be.  For example, valid format strings are "RGBA", "GA",
        "ABRG" or "AAA".  A component can also be written as "0" or "1", which
        means an empty/black or a full/white channel, respectively.

        This function is particularly useful to copy an image in-memory to a
        different library (for example, PIL or wxWidgets) that require a different
        component order than Panda's internal format, BGRA. Note, however, that
        this conversion can still be too slow if you want to do it every frame, and
        should thus be avoided for that purpose.

        The only requirement for the reordering is that an uncompressed image must
        be available.  If the RAM image is compressed, it will attempt to re-load
        the texture from disk, if it doesn't find an uncompressed image there, it
        will return NULL.
        """
    def modify_ram_image(self) -> PTA_uchar:
        """Returns a modifiable pointer to the system-RAM image.  This assumes the RAM
        image should be uncompressed.  If the RAM image has been dumped, or is
        stored compressed, creates a new one.

        This does *not* affect keep_ram_image.
        """
    def make_ram_image(self) -> PTA_uchar:
        """Discards the current system-RAM image for the texture, if any, and
        allocates a new buffer of the appropriate size.  Returns the new buffer.

        This does *not* affect keep_ram_image.
        """
    def set_ram_image(self, image, compression: _Texture_CompressionMode = ..., page_size: int = ...) -> None: ...
    def set_ram_image_as(self, image, provided_format: str) -> None: ...
    def clear_ram_image(self) -> None:
        """Discards the current system-RAM image."""
    def set_keep_ram_image(self, keep_ram_image: bool) -> None:
        """Sets the flag that indicates whether this Texture is eligible to have its
        main RAM copy of the texture memory dumped when the texture is prepared for
        rendering.

        This will be false for most textures, which can reload their images if
        needed by rereading the input file.  However, textures that were generated
        dynamically and cannot be easily reloaded will want to set this flag to
        true, so that the texture will always keep its image copy around.
        """
    def get_keep_ram_image(self) -> bool:
        """Returns the flag that indicates whether this Texture is eligible to have
        its main RAM copy of the texture memory dumped when the texture is prepared
        for rendering.  See set_keep_ram_image().
        """
    def is_cacheable(self) -> bool:
        """Returns true if there is enough information in this Texture object to write
        it to the bam cache successfully, false otherwise.  For most textures, this
        is the same as has_ram_image().
        """
    def compress_ram_image(
        self,
        compression: _Texture_CompressionMode = ...,
        quality_level: _Texture_QualityLevel = ...,
        gsg: GraphicsStateGuardianBase = ...,
    ) -> bool:
        """Attempts to compress the texture's RAM image internally, to a format
        supported by the indicated GSG.  In order for this to work, the squish
        library must have been compiled into Panda.

        If compression is CM_on, then an appropriate compression method that is
        supported by the indicated GSG is automatically chosen.  If the GSG pointer
        is NULL, any of the standard DXT1/3/5 compression methods will be used,
        regardless of whether it is supported.

        If compression is any specific compression method, that method is used
        regardless of whether the GSG supports it.

        quality_level determines the speed/quality tradeoff of the compression.  If
        it is QL_default, the texture's own quality_level parameter is used.

        Returns true if successful, false otherwise.
        """
    def uncompress_ram_image(self) -> bool:
        """Attempts to uncompress the texture's RAM image internally.  In order for
        this to work, the squish library must have been compiled into Panda, and
        the ram image must be compressed in a format supported by squish.

        Returns true if successful, false otherwise.
        """
    def get_num_ram_mipmap_images(self) -> int:
        """Returns the maximum number of mipmap level images available in system
        memory.  The actual number may be less than this (that is, there might be
        gaps in the sequence); use has_ram_mipmap_image() to verify each level.

        Also see get_num_loadable_ram_mipmap_images().
        """
    def has_ram_mipmap_image(self, n: int) -> bool:
        """Returns true if the Texture has the nth mipmap level available in system
        memory, false otherwise.  If the texture's minfilter mode requires
        mipmapping (see uses_mipmaps()), and all the texture's mipmap levels are
        not available when the texture is rendered, they will be generated
        automatically.
        """
    def get_num_loadable_ram_mipmap_images(self) -> int:
        """Returns the number of contiguous mipmap levels that exist in RAM, up until
        the first gap in the sequence.  It is guaranteed that at least mipmap
        levels [0, get_num_ram_mipmap_images()) exist.

        The number returned will never exceed the number of required mipmap images
        based on the size of the texture and its filter mode.

        This method is different from get_num_ram_mipmap_images() in that it
        returns only the number of mipmap levels that can actually be usefully
        loaded, regardless of the actual number that may be stored.
        """
    def has_all_ram_mipmap_images(self) -> bool:
        """Returns true if all expected mipmap levels have been defined and exist in
        the system RAM, or false if even one mipmap level is missing.
        """
    def get_ram_mipmap_image_size(self, n: int) -> int:
        """Returns the number of bytes used by the in-memory image for mipmap level n,
        or 0 if there is no in-memory image for this mipmap level.
        """
    def get_ram_mipmap_view_size(self, n: int) -> int:
        """Returns the number of bytes used by the in-memory image per view for mipmap
        level n, or 0 if there is no in-memory image for this mipmap level.

        A "view" is a collection of z_size pages for each mipmap level.  Most
        textures have only one view, except for multiview or stereo textures.

        For a non-compressed texture, this is the same as
        get_expected_ram_mipmap_view_size().  For a compressed texture, this may be
        a smaller value.  (We do assume that all pages will be the same size on a
        compressed texture).
        """
    def get_ram_mipmap_page_size(self, n: int) -> int:
        """Returns the number of bytes used by the in-memory image per page for mipmap
        level n, or 0 if there is no in-memory image for this mipmap level.

        For a non-compressed texture, this is the same as
        get_expected_ram_mipmap_page_size().  For a compressed texture, this may be
        a smaller value.  (We do assume that all pages will be the same size on a
        compressed texture).
        """
    def get_expected_ram_mipmap_image_size(self, n: int) -> int:
        """Returns the number of bytes that *ought* to be used by the in-memory image
        for mipmap level n, based on the texture parameters.
        """
    def get_expected_ram_mipmap_view_size(self, n: int) -> int:
        """Returns the number of bytes that *ought* to be used by each view of the in-
        memory image for mipmap level n, based on the texture parameters.  For a
        normal, non-multiview texture, this is the same as
        get_expected_ram_mipmap_image_size(n).
        """
    def get_expected_ram_mipmap_page_size(self, n: int) -> int:
        """Returns the number of bytes that should be used per each Z page of the 3-d
        texture, for mipmap level n.  For a 2-d or 1-d texture, this is the same as
        get_expected_ram_mipmap_view_size(n).
        """
    def get_ram_mipmap_image(self, n: int) -> CPTA_uchar:
        """Returns the system-RAM image data associated with the nth mipmap level, if
        present.  Returns NULL if the nth mipmap level is not present.
        """
    def modify_ram_mipmap_image(self, n: int) -> PTA_uchar:
        """Returns a modifiable pointer to the system-RAM image for the nth mipmap
        level.  This assumes the RAM image is uncompressed; if this is not the
        case, raises an assertion.

        This does *not* affect keep_ram_image.
        """
    def make_ram_mipmap_image(self, n: int) -> PTA_uchar:
        """Discards the current system-RAM image for the nth mipmap level, if any, and
        allocates a new buffer of the appropriate size.  Returns the new buffer.

        This does *not* affect keep_ram_image.
        """
    def set_ram_mipmap_pointer_from_int(self, pointer: int, n: int, page_size: int) -> None:
        """Accepts a raw pointer cast as an int, which is then passed to
        set_ram_mipmap_pointer(); see the documentation for that method.

        This variant is particularly useful to set an external pointer from a
        language like Python, which doesn't support void pointers directly.
        """
    def set_ram_mipmap_image(self, n: int, image: CPTA_uchar | PointerToArray_unsigned_char, page_size: int = ...) -> None:
        """Replaces the current system-RAM image for the indicated mipmap level with
        the new data.  If compression is not CM_off, it indicates that the new data
        is already pre-compressed in the indicated format.

        This does *not* affect keep_ram_image.
        """
    def clear_ram_mipmap_image(self, n: int) -> None:
        """Discards the current system-RAM image for the nth mipmap level."""
    def clear_ram_mipmap_images(self) -> None:
        """Discards the current system-RAM image for all mipmap levels, except level 0
        (the base image).
        """
    def generate_ram_mipmap_images(self) -> None:
        """Automatically fills in the n mipmap levels of the Texture, based on the
        texture's source image.  This requires the texture's uncompressed ram image
        to be available in system memory.  If it is not already, it will be fetched
        if possible.

        This call is not normally necessary, since the mipmap levels will be
        generated automatically if needed.  But there may be certain cases in which
        you would like to call this explicitly.
        """
    def get_simple_x_size(self) -> int:
        """Returns the width of the "simple" image in texels."""
    def get_simple_y_size(self) -> int:
        """Returns the height of the "simple" image in texels."""
    def has_simple_ram_image(self) -> bool:
        """Returns true if the Texture has a "simple" image available in main RAM."""
    def get_simple_ram_image_size(self) -> int:
        """Returns the number of bytes used by the "simple" image, or 0 if there is no
        simple image.
        """
    def get_simple_ram_image(self) -> CPTA_uchar:
        """Returns the image data associated with the "simple" texture image.  This is
        provided for some textures as an option to display while the main texture
        image is being loaded from disk.

        Unlike get_ram_image(), this function will always return immediately.
        Either the simple image is available, or it is not.

        The "simple" image is always 4 components, 1 byte each, regardless of the
        parameters of the full texture.  The simple image is only supported for
        ordinary 2-d textures.
        """
    def set_simple_ram_image(self, image: CPTA_uchar | PointerToArray_unsigned_char, x_size: int, y_size: int) -> None:
        """Replaces the internal "simple" texture image.  This can be used as an
        option to display while the main texture image is being loaded from disk.
        It is normally a very small image, 16x16 or smaller (and maybe even 1x1),
        that is designed to give just enough sense of color to serve as a
        placeholder until the full texture is available.

        The "simple" image is always 4 components, 1 byte each, regardless of the
        parameters of the full texture.  The simple image is only supported for
        ordinary 2-d textures.

        Also see generate_simple_ram_image(), modify_simple_ram_image(), and
        new_simple_ram_image().
        """
    def modify_simple_ram_image(self) -> PTA_uchar:
        """Returns a modifiable pointer to the internal "simple" texture image.  See
        set_simple_ram_image().
        """
    def new_simple_ram_image(self, x_size: int, y_size: int) -> PTA_uchar:
        """Creates an empty array for the simple ram image of the indicated size, and
        returns a modifiable pointer to the new array.  See set_simple_ram_image().
        """
    def generate_simple_ram_image(self) -> None:
        """Computes the "simple" ram image by loading the main RAM image, if it is not
        already available, and reducing it to 16x16 or smaller.  This may be an
        expensive operation.
        """
    def clear_simple_ram_image(self) -> None:
        """Discards the current "simple" image."""
    def peek(self) -> TexturePeeker:
        """Returns a TexturePeeker object that can be used to examine the individual
        texels stored within this Texture by (u, v) coordinate.

        If the texture has a ram image resident, that image is used.  If it does
        not have a full ram image but does have a simple_ram_image resident, that
        image is used instead.  If neither image is resident the full image is
        reloaded.

        Returns NULL if the texture cannot find an image to load, or the texture
        format is incompatible.
        """
    def get_properties_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the texture properties (unrelated to the image) are modified.
        """
    def get_image_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the texture image data (including mipmap levels) are modified.
        """
    def get_simple_image_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the texture's "simple" image data is modified.
        """
    def has_auto_texture_scale(self) -> bool:
        """Returns true if set_auto_texture_scale() has been set to something other
        than ATS_unspecified for this particular texture.
        """
    def get_auto_texture_scale(self) -> _AutoTextureScale:
        """Returns the power-of-2 texture-scaling mode that will be applied to this
        particular texture when it is next loaded from disk.  See
        set_textures_power_2().
        """
    def set_auto_texture_scale(self, scale: _AutoTextureScale) -> None:
        """Specifies the power-of-2 texture-scaling mode that will be applied to this
        particular texture when it is next loaded from disk.  See
        set_textures_power_2().
        """
    def prepare(self, prepared_objects: PreparedGraphicsObjects) -> AsyncFuture:
        """Indicates that the texture should be enqueued to be prepared in the
        indicated prepared_objects at the beginning of the next frame.  This will
        ensure the texture is already loaded into texture memory if it is expected
        to be rendered soon.

        Use this function instead of prepare_now() to preload textures from a user
        interface standpoint.
        """
    def is_prepared(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the texture has already been prepared or enqueued for
        preparation on the indicated GSG, false otherwise.
        """
    def was_image_modified(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the texture needs to be re-loaded onto the indicated GSG,
        either because its image data is out-of-date, or because it's not fully
        prepared now.
        """
    def get_data_size_bytes(self, prepared_objects: PreparedGraphicsObjects) -> int:
        """Returns the number of bytes which the texture is reported to consume within
        graphics memory, for the indicated GSG.  This may return a nonzero value
        even if the texture is not currently resident; you should also check
        get_resident() if you want to know how much space the texture is actually
        consuming right now.
        """
    def get_active(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if this Texture was rendered in the most recent frame within
        the indicated GSG.
        """
    def get_resident(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if this Texture is reported to be resident within graphics
        memory for the indicated GSG.
        """
    def release(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Frees the texture context only on the indicated object, if it exists there.
        Returns true if it was released, false if it had not been prepared.
        """
    def release_all(self) -> int:
        """Frees the context allocated on all objects for which the texture has been
        declared.  Returns the number of contexts which have been freed.
        """
    def estimate_texture_memory(self) -> int:
        """Estimates the amount of texture memory that will be consumed by loading
        this texture.  This returns a value that is not specific to any particular
        graphics card or driver; it tries to make a reasonable assumption about how
        a driver will load the texture.  It does not account for texture
        compression or anything fancy.  This is mainly useful for debugging and
        reporting purposes.

        Returns a value in bytes.
        """
    def set_aux_data(self, key: str, aux_data: TypedReferenceCount) -> None:
        """Records an arbitrary object in the Texture, associated with a specified
        key.  The object may later be retrieved by calling get_aux_data() with the
        same key.

        These data objects are not recorded to a bam or txo file.
        """
    def clear_aux_data(self, key: str) -> None:
        """Removes a record previously recorded via set_aux_data()."""
    def get_aux_data(self, key: str) -> TypedReferenceCount:
        """Returns a record previously recorded via set_aux_data().  Returns NULL if
        there was no record associated with the indicated key.
        """
    @staticmethod
    def set_textures_power_2(scale: _AutoTextureScale) -> None:
        """Set this flag to ATS_none, ATS_up, ATS_down, or ATS_pad to control the
        scaling of textures in general, if a particular texture does not override
        this.  See also set_auto_texture_scale() for the per-texture override.
        """
    @staticmethod
    def get_textures_power_2() -> _AutoTextureScale:
        """This flag returns ATS_none, ATS_up, or ATS_down and controls the scaling of
        textures in general.  It is initialized from the config variable of the
        same name, but it can be subsequently adjusted.  See also
        get_auto_texture_scale().
        """
    @staticmethod
    def has_textures_power_2() -> bool:
        """If true, then get_textures_power_2 has been set using set_textures_power_2.
        If false, then get_textures_power_2 simply returns the config variable of
        the same name.
        """
    def get_pad_x_size(self) -> int:
        """Returns size of the pad region.  See set_pad_size."""
    def get_pad_y_size(self) -> int:
        """Returns size of the pad region.  See set_pad_size."""
    def get_pad_z_size(self) -> int:
        """Returns size of the pad region.  See set_pad_size."""
    def get_tex_scale(self) -> LVecBase2:
        """Returns a scale pair that is suitable for applying to geometry via
        NodePath::set_tex_scale(), which will convert texture coordinates on the
        geometry from the range 0..1 into the appropriate range to render the video
        part of the texture.

        This is necessary only if a padding size has been set via set_pad_size()
        (or implicitly via something like "textures-power-2 pad" in the config.prc
        file).  In this case, this is a convenient way to generate UV's that
        reflect the built-in padding size.
        """
    def set_pad_size(self, x: int = ..., y: int = ..., z: int = ...) -> None:
        """Sets the size of the pad region.

        Sometimes, when a video card demands power-of-two textures, it is necessary
        to create a big texture and then only use a portion of it.  The pad region
        indicates which portion of the texture is not really in use.  All
        operations use the texture as a whole, including the pad region, unless
        they explicitly state that they use only the non-pad region.

        Changing the texture's size clears the pad region.
        """
    def set_size_padded(self, x: int = ..., y: int = ..., z: int = ...) -> None:
        """Changes the size of the texture, padding if necessary, and setting the pad
        region as well.
        """
    def get_orig_file_x_size(self) -> int:
        """Returns the X size of the original disk image that this Texture was loaded
        from (if it came from a disk file), before any automatic rescaling by
        Panda.
        """
    def get_orig_file_y_size(self) -> int:
        """Returns the Y size of the original disk image that this Texture was loaded
        from (if it came from a disk file), before any automatic rescaling by
        Panda.
        """
    def get_orig_file_z_size(self) -> int:
        """Returns the Z size of the original disk image that this Texture was loaded
        from (if it came from a disk file), before any automatic rescaling by
        Panda.
        """
    def set_orig_file_size(self, x: int, y: int, z: int = ...) -> None:
        """Specifies the size of the texture as it exists in its original disk file,
        before any Panda scaling.
        """
    def set_loaded_from_image(self, flag: bool = ...) -> None:
        """Sets the flag that indicates the texture has been loaded from a disk file
        or PNMImage.  You should also ensure the filename has been set correctly.
        When this flag is true, the texture may be automatically reloaded when its
        ram image needs to be replaced.
        """
    def get_loaded_from_image(self) -> bool:
        """Returns the flag that indicates the texture has been loaded from a disk
        file or PNMImage.  See set_loaded_from_image().
        """
    def set_loaded_from_txo(self, flag: bool = ...) -> None:
        """Sets the flag that indicates the texture has been loaded from a txo file.
        You probably shouldn't be setting this directly; it is set automatically
        when a Texture is loaded.
        """
    def get_loaded_from_txo(self) -> bool:
        """Returns the flag that indicates the texture has been loaded from a txo
        file.
        """
    def get_match_framebuffer_format(self) -> bool:
        """Returns true if the special flag was set that indicates to the GSG that the
        Texture's format should be chosen to exactly match the framebuffer's
        format, presumably because the application intends to copy image data from
        the framebuffer into the Texture (or vice-versa).
        """
    def set_match_framebuffer_format(self, flag: bool) -> None:
        """Sets the special flag that, if true, indicates to the GSG that the
        Texture's format should be chosen to exactly match the framebuffer's
        format, presumably because the application intends to copy image data from
        the framebuffer into the Texture (or vice-versa).

        This sets only the graphics card's idea of the texture format; it is not
        related to the system-memory format.
        """
    def get_post_load_store_cache(self) -> bool:
        """Returns the setting of the post_load_store_cache flag.  See
        set_post_load_store_cache().
        """
    def set_post_load_store_cache(self, flag: bool) -> None:
        """Sets the post_load_store_cache flag.  When this is set, the next time the
        texture is loaded on a GSG, it will automatically extract its RAM image
        from the GSG and save it to the global BamCache.

        This is used to store compressed RAM images in the BamCache.  This flag
        should not be set explicitly; it is set automatically by the TexturePool
        when model-cache-compressed-textures is set true.
        """
    def prepare_now(self, view: int, prepared_objects: PreparedGraphicsObjects, gsg: GraphicsStateGuardianBase) -> TextureContext:
        """Creates a context for the texture on the particular GSG, if it does not
        already exist.  Returns the new (or old) TextureContext.  This assumes that
        the GraphicsStateGuardian is the currently active rendering context and
        that it is ready to accept new textures.  If this is not necessarily the
        case, you should use prepare() instead.

        Normally, this is not called directly except by the GraphicsStateGuardian;
        a texture does not need to be explicitly prepared by the user before it may
        be rendered.
        """
    @staticmethod
    def up_to_power_2(value: int) -> int:
        """Returns the smallest power of 2 greater than or equal to value."""
    @staticmethod
    def down_to_power_2(value: int) -> int:
        """Returns the largest power of 2 less than or equal to value."""
    @overload
    def consider_rescale(self, pnmimage: PNMImage) -> None:
        """Asks the PNMImage to change its scale when it reads the image, according to
        the whims of the Config.prc file.

        For most efficient results, this method should be called after
        pnmimage.read_header() has been called, but before pnmimage.read().  This
        method may also be called after pnmimage.read(), i.e.  when the pnmimage is
        already loaded; in this case it will rescale the image on the spot.  Also
        see rescale_texture().
        """
    @overload
    def consider_rescale(self, pnmimage: PNMImage, name: str, auto_texture_scale: _AutoTextureScale = ...) -> None: ...
    def rescale_texture(self) -> bool:
        """This method is similar to consider_rescale(), but instead of scaling a
        separate PNMImage, it will ask the Texture to rescale its own internal
        image to a power of 2, according to the config file requirements.  This may
        be useful after loading a Texture image by hand, instead of reading it from
        a disk file.  Returns true if the texture is changed, false if it was not.
        """
    @staticmethod
    def format_texture_type(tt: _Texture_TextureType) -> str:
        """Returns the indicated TextureType converted to a string word."""
    @staticmethod
    def string_texture_type(str: str) -> _Texture_TextureType:
        """Returns the TextureType corresponding to the indicated string word."""
    @staticmethod
    def format_component_type(ct: _Texture_ComponentType) -> str:
        """Returns the indicated ComponentType converted to a string word."""
    @staticmethod
    def string_component_type(str: str) -> _Texture_ComponentType:
        """Returns the ComponentType corresponding to the indicated string word."""
    @staticmethod
    def format_format(f: _Texture_Format) -> str:
        """Returns the indicated Format converted to a string word."""
    @staticmethod
    def string_format(str: str) -> _Texture_Format:
        """Returns the Format corresponding to the indicated string word."""
    @staticmethod
    def format_compression_mode(cm: _Texture_CompressionMode) -> str:
        """Returns the indicated CompressionMode converted to a string word."""
    @staticmethod
    def string_compression_mode(str: str) -> _Texture_CompressionMode:
        """Returns the CompressionMode value associated with the given string
        representation.
        """
    @staticmethod
    def format_quality_level(tql: _Texture_QualityLevel) -> str:
        """Returns the indicated QualityLevel converted to a string word."""
    @staticmethod
    def string_quality_level(str: str) -> _Texture_QualityLevel:
        """Returns the QualityLevel value associated with the given string
        representation.
        """
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    makeCopy = make_copy
    setupTexture = setup_texture
    setup1dTexture = setup_1d_texture
    setup2dTexture = setup_2d_texture
    setup3dTexture = setup_3d_texture
    setupCubeMap = setup_cube_map
    setup2dTextureArray = setup_2d_texture_array
    setupCubeMapArray = setup_cube_map_array
    setupBufferTexture = setup_buffer_texture
    generateNormalizationCubeMap = generate_normalization_cube_map
    generateAlphaScaleMap = generate_alpha_scale_map
    clearImage = clear_image
    hasClearColor = has_clear_color
    getClearColor = get_clear_color
    setClearColor = set_clear_color
    clearClearColor = clear_clear_color
    getClearData = get_clear_data
    readTxo = read_txo
    makeFromTxo = make_from_txo
    writeTxo = write_txo
    readDds = read_dds
    readKtx = read_ktx
    loadSubImage = load_sub_image
    loadRelated = load_related
    hasFilename = has_filename
    getFilename = get_filename
    setFilename = set_filename
    clearFilename = clear_filename
    hasAlphaFilename = has_alpha_filename
    getAlphaFilename = get_alpha_filename
    setAlphaFilename = set_alpha_filename
    clearAlphaFilename = clear_alpha_filename
    hasFullpath = has_fullpath
    getFullpath = get_fullpath
    setFullpath = set_fullpath
    clearFullpath = clear_fullpath
    hasAlphaFullpath = has_alpha_fullpath
    getAlphaFullpath = get_alpha_fullpath
    setAlphaFullpath = set_alpha_fullpath
    clearAlphaFullpath = clear_alpha_fullpath
    getXSize = get_x_size
    setXSize = set_x_size
    getYSize = get_y_size
    setYSize = set_y_size
    getZSize = get_z_size
    setZSize = set_z_size
    getNumViews = get_num_views
    setNumViews = set_num_views
    getNumPages = get_num_pages
    getNumComponents = get_num_components
    getComponentWidth = get_component_width
    getTextureType = get_texture_type
    getUsageHint = get_usage_hint
    getFormat = get_format
    setFormat = set_format
    getComponentType = get_component_type
    setComponentType = set_component_type
    getWrapU = get_wrap_u
    setWrapU = set_wrap_u
    getWrapV = get_wrap_v
    setWrapV = set_wrap_v
    getWrapW = get_wrap_w
    setWrapW = set_wrap_w
    getMinfilter = get_minfilter
    getEffectiveMinfilter = get_effective_minfilter
    setMinfilter = set_minfilter
    getMagfilter = get_magfilter
    getEffectiveMagfilter = get_effective_magfilter
    setMagfilter = set_magfilter
    getAnisotropicDegree = get_anisotropic_degree
    getEffectiveAnisotropicDegree = get_effective_anisotropic_degree
    setAnisotropicDegree = set_anisotropic_degree
    getBorderColor = get_border_color
    setBorderColor = set_border_color
    hasCompression = has_compression
    getCompression = get_compression
    setCompression = set_compression
    getRenderToTexture = get_render_to_texture
    setRenderToTexture = set_render_to_texture
    getDefaultSampler = get_default_sampler
    setDefaultSampler = set_default_sampler
    usesMipmaps = uses_mipmaps
    getQualityLevel = get_quality_level
    getEffectiveQualityLevel = get_effective_quality_level
    setQualityLevel = set_quality_level
    getExpectedNumMipmapLevels = get_expected_num_mipmap_levels
    getExpectedMipmapXSize = get_expected_mipmap_x_size
    getExpectedMipmapYSize = get_expected_mipmap_y_size
    getExpectedMipmapZSize = get_expected_mipmap_z_size
    getExpectedMipmapNumPages = get_expected_mipmap_num_pages
    hasRamImage = has_ram_image
    hasUncompressedRamImage = has_uncompressed_ram_image
    mightHaveRamImage = might_have_ram_image
    getRamImageSize = get_ram_image_size
    getRamViewSize = get_ram_view_size
    getRamPageSize = get_ram_page_size
    getExpectedRamImageSize = get_expected_ram_image_size
    getExpectedRamPageSize = get_expected_ram_page_size
    getRamImage = get_ram_image
    getRamImageCompression = get_ram_image_compression
    getUncompressedRamImage = get_uncompressed_ram_image
    getRamImageAs = get_ram_image_as
    modifyRamImage = modify_ram_image
    makeRamImage = make_ram_image
    setRamImage = set_ram_image
    setRamImageAs = set_ram_image_as
    clearRamImage = clear_ram_image
    setKeepRamImage = set_keep_ram_image
    getKeepRamImage = get_keep_ram_image
    isCacheable = is_cacheable
    compressRamImage = compress_ram_image
    uncompressRamImage = uncompress_ram_image
    getNumRamMipmapImages = get_num_ram_mipmap_images
    hasRamMipmapImage = has_ram_mipmap_image
    getNumLoadableRamMipmapImages = get_num_loadable_ram_mipmap_images
    hasAllRamMipmapImages = has_all_ram_mipmap_images
    getRamMipmapImageSize = get_ram_mipmap_image_size
    getRamMipmapViewSize = get_ram_mipmap_view_size
    getRamMipmapPageSize = get_ram_mipmap_page_size
    getExpectedRamMipmapImageSize = get_expected_ram_mipmap_image_size
    getExpectedRamMipmapViewSize = get_expected_ram_mipmap_view_size
    getExpectedRamMipmapPageSize = get_expected_ram_mipmap_page_size
    getRamMipmapImage = get_ram_mipmap_image
    modifyRamMipmapImage = modify_ram_mipmap_image
    makeRamMipmapImage = make_ram_mipmap_image
    setRamMipmapPointerFromInt = set_ram_mipmap_pointer_from_int
    setRamMipmapImage = set_ram_mipmap_image
    clearRamMipmapImage = clear_ram_mipmap_image
    clearRamMipmapImages = clear_ram_mipmap_images
    generateRamMipmapImages = generate_ram_mipmap_images
    getSimpleXSize = get_simple_x_size
    getSimpleYSize = get_simple_y_size
    hasSimpleRamImage = has_simple_ram_image
    getSimpleRamImageSize = get_simple_ram_image_size
    getSimpleRamImage = get_simple_ram_image
    setSimpleRamImage = set_simple_ram_image
    modifySimpleRamImage = modify_simple_ram_image
    newSimpleRamImage = new_simple_ram_image
    generateSimpleRamImage = generate_simple_ram_image
    clearSimpleRamImage = clear_simple_ram_image
    getPropertiesModified = get_properties_modified
    getImageModified = get_image_modified
    getSimpleImageModified = get_simple_image_modified
    hasAutoTextureScale = has_auto_texture_scale
    getAutoTextureScale = get_auto_texture_scale
    setAutoTextureScale = set_auto_texture_scale
    isPrepared = is_prepared
    wasImageModified = was_image_modified
    getDataSizeBytes = get_data_size_bytes
    getActive = get_active
    getResident = get_resident
    releaseAll = release_all
    estimateTextureMemory = estimate_texture_memory
    setAuxData = set_aux_data
    clearAuxData = clear_aux_data
    getAuxData = get_aux_data
    setTexturesPower2 = set_textures_power_2
    getTexturesPower2 = get_textures_power_2
    hasTexturesPower2 = has_textures_power_2
    getPadXSize = get_pad_x_size
    getPadYSize = get_pad_y_size
    getPadZSize = get_pad_z_size
    getTexScale = get_tex_scale
    setPadSize = set_pad_size
    setSizePadded = set_size_padded
    getOrigFileXSize = get_orig_file_x_size
    getOrigFileYSize = get_orig_file_y_size
    getOrigFileZSize = get_orig_file_z_size
    setOrigFileSize = set_orig_file_size
    setLoadedFromImage = set_loaded_from_image
    getLoadedFromImage = get_loaded_from_image
    setLoadedFromTxo = set_loaded_from_txo
    getLoadedFromTxo = get_loaded_from_txo
    getMatchFramebufferFormat = get_match_framebuffer_format
    setMatchFramebufferFormat = set_match_framebuffer_format
    getPostLoadStoreCache = get_post_load_store_cache
    setPostLoadStoreCache = set_post_load_store_cache
    prepareNow = prepare_now
    upToPower2 = up_to_power_2
    downToPower2 = down_to_power_2
    considerRescale = consider_rescale
    rescaleTexture = rescale_texture
    formatTextureType = format_texture_type
    stringTextureType = string_texture_type
    formatComponentType = format_component_type
    stringComponentType = string_component_type
    formatFormat = format_format
    stringFormat = string_format
    formatCompressionMode = format_compression_mode
    stringCompressionMode = string_compression_mode
    formatQualityLevel = format_quality_level
    stringQualityLevel = string_quality_level

class Shader(TypedWritableReferenceCount):
    SL_none: Final = 0
    SLNone: Final = 0
    SL_Cg: Final = 1
    SLCg: Final = 1
    SL_GLSL: Final = 2
    SLGLSL: Final = 2
    SL_HLSL: Final = 3
    SLHLSL: Final = 3
    SL_SPIR_V: Final = 4
    SLSPIRV: Final = 4
    ST_none: Final = 0
    STNone: Final = 0
    ST_vertex: Final = 1
    STVertex: Final = 1
    ST_fragment: Final = 2
    STFragment: Final = 2
    ST_geometry: Final = 3
    STGeometry: Final = 3
    ST_tess_control: Final = 4
    STTessControl: Final = 4
    ST_tess_evaluation: Final = 5
    STTessEvaluation: Final = 5
    ST_compute: Final = 6
    STCompute: Final = 6
    ST_COUNT: Final = 7
    STCOUNT: Final = 7
    AS_normal: Final = 1
    ASNormal: Final = 1
    AS_glow: Final = 2
    ASGlow: Final = 2
    AS_gloss: Final = 4
    ASGloss: Final = 4
    AS_ramp: Final = 8
    ASRamp: Final = 8
    AS_shadow: Final = 16
    ASShadow: Final = 16
    bit_AutoShaderNormal: Final = 0
    BitAutoShaderNormal: Final = 0
    bit_AutoShaderGlow: Final = 1
    BitAutoShaderGlow: Final = 1
    bit_AutoShaderGloss: Final = 2
    BitAutoShaderGloss: Final = 2
    bit_AutoShaderRamp: Final = 3
    BitAutoShaderRamp: Final = 3
    bit_AutoShaderShadow: Final = 4
    BitAutoShaderShadow: Final = 4
    def __init__(self, __param0: Shader) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    @staticmethod
    def load(file: StrOrBytesPath, lang: _Shader_ShaderLanguage = ...) -> Shader:
        """`(file: Filename, lang: _Shader_ShaderLanguage = ...)`:
        Loads the shader with the given filename.

        `(lang: _Shader_ShaderLanguage, vertex: Filename, fragment: Filename, geometry: Filename = ..., tess_control: Filename = ..., tess_evaluation: Filename = ...)`:
        This variant of Shader::load loads all shader programs separately.
        """
    @overload
    @staticmethod
    def load(
        lang: _Shader_ShaderLanguage,
        vertex: StrOrBytesPath,
        fragment: StrOrBytesPath,
        geometry: StrOrBytesPath = ...,
        tess_control: StrOrBytesPath = ...,
        tess_evaluation: StrOrBytesPath = ...,
    ) -> Shader: ...
    @overload
    @staticmethod
    def make(body: str, lang: _Shader_ShaderLanguage = ...) -> Shader:
        """`(lang: _Shader_ShaderLanguage, vertex: str, fragment: str, geometry: str = ..., tess_control: str = ..., tess_evaluation: str = ...)`:
        Loads the shader, using the strings as shader bodies.

        `(body: str, lang: _Shader_ShaderLanguage = ...)`:
        Loads the shader, using the string as shader body.
        """
    @overload
    @staticmethod
    def make(
        lang: _Shader_ShaderLanguage,
        vertex: str,
        fragment: str,
        geometry: str = ...,
        tess_control: str = ...,
        tess_evaluation: str = ...,
    ) -> Shader: ...
    @staticmethod
    def load_compute(lang: _Shader_ShaderLanguage, fn: StrOrBytesPath) -> Shader:
        """Loads a compute shader."""
    @staticmethod
    def make_compute(lang: _Shader_ShaderLanguage, body: str) -> Shader:
        """Loads the compute shader from the given string."""
    def get_filename(self, type: _Shader_ShaderType = ...) -> Filename:
        """Return the Shader's filename for the given shader type."""
    def set_filename(self, type: _Shader_ShaderType, filename: StrOrBytesPath) -> None:
        """Sets the Shader's filename for the given shader type.  Useful for
        associating a shader created with Shader.make with a name for diagnostics.
        """
    def get_text(self, type: _Shader_ShaderType = ...) -> str:
        """Return the Shader's text for the given shader type."""
    def get_error_flag(self) -> bool:
        """Returns true if the shader contains a compile-time error.  This doesn't
        tell you whether or not the shader is supported on the current video card.
        """
    def get_language(self) -> _Shader_ShaderLanguage:
        """Returns the shader language in which this shader was written."""
    def has_fullpath(self) -> bool:
        """Returns true if the fullpath has been set and is available.  See
        set_fullpath().
        """
    def get_fullpath(self) -> Filename:
        """Returns the fullpath that has been set.  This is the full path to the file
        as it was found along the model-path.
        """
    def get_cache_compiled_shader(self) -> bool:
        """Returns the setting of the cache_compiled_shader flag.  See
        set_cache_compiled_shader().
        """
    def set_cache_compiled_shader(self, flag: bool) -> None:
        """Sets the cache_compiled_shader flag.  When this is set, the next time the
        Shader is loaded on a GSG, it will automatically extract the compiled
        shader from the GSG and save it to the global BamCache.

        This is used to store compiled shaders in the BamCache.  This flag should
        not be set explicitly; it is set automatically by the ShaderPool when
        model-cache-compiled-shaders is set true.
        """
    def prepare(self, prepared_objects: PreparedGraphicsObjects) -> AsyncFuture:
        """Indicates that the shader should be enqueued to be prepared in the
        indicated prepared_objects at the beginning of the next frame.  This will
        ensure the texture is already loaded into texture memory if it is expected
        to be rendered soon.

        Use this function instead of prepare_now() to preload textures from a user
        interface standpoint.
        """
    def is_prepared(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the shader has already been prepared or enqueued for
        preparation on the indicated GSG, false otherwise.
        """
    def release(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Frees the texture context only on the indicated object, if it exists there.
        Returns true if it was released, false if it had not been prepared.
        """
    def release_all(self) -> int:
        """Frees the context allocated on all objects for which the texture has been
        declared.  Returns the number of contexts which have been freed.
        """
    def prepare_now(self, prepared_objects: PreparedGraphicsObjects, gsg: GraphicsStateGuardianBase) -> ShaderContext:
        """Creates a context for the shader on the particular GSG, if it does not
        already exist.  Returns the new (or old) ShaderContext.  This assumes that
        the GraphicsStateGuardian is the currently active rendering context and
        that it is ready to accept new textures.  If this is not necessarily the
        case, you should use prepare() instead.

        Normally, this is not called directly except by the GraphicsStateGuardian;
        a shader does not need to be explicitly prepared by the user before it may
        be rendered.
        """
    loadCompute = load_compute
    makeCompute = make_compute
    getFilename = get_filename
    setFilename = set_filename
    getText = get_text
    getErrorFlag = get_error_flag
    getLanguage = get_language
    hasFullpath = has_fullpath
    getFullpath = get_fullpath
    getCacheCompiledShader = get_cache_compiled_shader
    setCacheCompiledShader = set_cache_compiled_shader
    isPrepared = is_prepared
    releaseAll = release_all
    prepareNow = prepare_now

class ShaderBuffer(TypedWritableReferenceCount, Namable, GeomEnums):  # type: ignore[misc]
    """This is a generic buffer object that lives in graphics memory.

    @since 1.10.0
    """

    @property
    def data_size_bytes(self) -> int: ...
    @property
    def usage_hint(self) -> _GeomEnums_UsageHint: ...
    @overload
    def __init__(self, __param0: ShaderBuffer) -> None:
        """`(self, name: str, size: int, usage_hint: _GeomEnums_UsageHint)`:
        Creates an uninitialized buffer object with the given size.  For now, these
        parameters cannot be modified, but this may change in the future.

        `(self, name: str, initial_data: bytes, usage_hint: _GeomEnums_UsageHint)`:
        Creates a buffer object initialized with the given data.  For now, these
        parameters cannot be modified, but this may change in the future.
        """
    @overload
    def __init__(self, name: str, size: int, usage_hint: _GeomEnums_UsageHint) -> None: ...
    @overload
    def __init__(self, name: str, initial_data: bytes, usage_hint: _GeomEnums_UsageHint) -> None: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def upcast_to_GeomEnums(self) -> GeomEnums: ...
    def prepare(self, prepared_objects: PreparedGraphicsObjects) -> None:
        """Indicates that the data should be enqueued to be prepared in the indicated
        prepared_objects at the beginning of the next frame.  This will ensure the
        data is already loaded into the GSG if it is expected to be rendered soon.

        Use this function instead of prepare_now() to preload datas from a user
        interface standpoint.
        """
    def is_prepared(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Returns true if the data has already been prepared or enqueued for
        preparation on the indicated GSG, false otherwise.
        """
    def prepare_now(self, prepared_objects: PreparedGraphicsObjects, gsg: GraphicsStateGuardianBase) -> BufferContext:
        """Creates a context for the data on the particular GSG, if it does not
        already exist.  Returns the new (or old) BufferContext.  This assumes
        that the GraphicsStateGuardian is the currently active rendering context
        and that it is ready to accept new datas.  If this is not necessarily the
        case, you should use prepare() instead.

        Normally, this is not called directly except by the GraphicsStateGuardian;
        a data does not need to be explicitly prepared by the user before it may be
        rendered.
        """
    def release(self, prepared_objects: PreparedGraphicsObjects) -> bool:
        """Frees the data context only on the indicated object, if it exists there.
        Returns true if it was released, false if it had not been prepared.
        """
    def release_all(self) -> int:
        """Frees the context allocated on all objects for which the data has been
        declared.  Returns the number of contexts which have been freed.
        """
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    upcastToGeomEnums = upcast_to_GeomEnums
    isPrepared = is_prepared
    prepareNow = prepare_now
    releaseAll = release_all

class PreparedGraphicsObjects(ReferenceCount):
    """A table of objects that are saved within the graphics context for reference
    by handle later.  Generally, this represents things like OpenGL texture
    objects or display lists (or their equivalent on other platforms).

    This object simply records the pointers to the context objects created by
    the individual GSG's; these context objects will contain enough information
    to reference or release the actual object stored within the graphics
    context.

    These tables may potentially be shared between related graphics contexts,
    hence their storage here in a separate object rather than as a part of the
    GraphicsStateGuardian.
    """

    def get_name(self) -> str:
        """Returns the name of the PreparedGraphicsObjects structure.  This is an
        arbitrary name that serves mainly to uniquify the context for PStats
        reporting.
        """
    def set_graphics_memory_limit(self, limit: int) -> None:
        """Sets an artificial cap on graphics memory that will be imposed on this GSG.

        This limits the total amount of graphics memory, including texture memory
        and vertex buffer memory, that will be consumed by the GSG, regardless of
        whether the hardware claims to provide more graphics memory than this.  It
        is useful to put a ceiling on graphics memory consumed, since some drivers
        seem to allow the application to consume more memory than the hardware can
        realistically support.
        """
    def get_graphics_memory_limit(self) -> int:
        """Returns the artificial cap on graphics memory that will be imposed on this
        GSG.  See set_graphics_memory_limit().
        """
    def show_graphics_memory_lru(self, out: ostream) -> None:
        """Writes to the indicated ostream a report of how the various textures and
        vertex buffers are allocated in the LRU.
        """
    def show_residency_trackers(self, out: ostream) -> None:
        """Writes to the indicated ostream a report of how the various textures and
        vertex buffers are allocated in the LRU.
        """
    def release_all(self) -> None:
        """Releases all prepared objects of all kinds at once."""
    def get_num_queued(self) -> int:
        """Returns the number of objects of any kind that have been enqueued to be
        prepared on this GSG.
        """
    def get_num_prepared(self) -> int:
        """Returns the number of objects of any kind that have already been prepared
        on this GSG.
        """
    def enqueue_texture(self, tex: Texture) -> None:
        """Indicates that a texture would like to be put on the list to be prepared
        when the GSG is next ready to do this (presumably at the next frame).
        """
    def is_texture_queued(self, tex: Texture) -> bool:
        """Returns true if the texture has been queued on this GSG, false otherwise."""
    def dequeue_texture(self, tex: Texture) -> bool:
        """Removes a texture from the queued list of textures to be prepared.
        Normally it is not necessary to call this, unless you change your mind
        about preparing it at the last minute, since the texture will automatically
        be dequeued and prepared at the next frame.

        The return value is true if the texture is successfully dequeued, false if
        it had not been queued.
        """
    def is_texture_prepared(self, tex: Texture) -> bool:
        """Returns true if the texture has been prepared on this GSG, false otherwise."""
    @overload
    def release_texture(self, tex: Texture) -> None:
        """`(self, tex: Texture)`:
        Releases a texture if it has already been prepared, or removes it from the
        preparation queue.

        `(self, tc: TextureContext)`:
        Indicates that a texture context, created by a previous call to
        prepare_texture(), is no longer needed.  The driver resources will not be
        freed until some GSG calls update(), indicating it is at a stage where it
        is ready to release textures--this prevents conflicts from threading or
        multiple GSG's sharing textures (we have no way of knowing which graphics
        context is currently active, or what state it's in, at the time
        release_texture is called).
        """
    @overload
    def release_texture(self, tc: TextureContext) -> None: ...
    def release_all_textures(self) -> int:
        """Releases all textures at once.  This will force them to be reloaded into
        texture memory for all GSG's that share this object.  Returns the number of
        textures released.
        """
    def get_num_queued_textures(self) -> int:
        """Returns the number of textures that have been enqueued to be prepared on
        this GSG.
        """
    def get_num_prepared_textures(self) -> int:
        """Returns the number of textures that have already been prepared on this GSG."""
    def prepare_texture_now(self, tex: Texture, view: int, gsg: GraphicsStateGuardianBase) -> TextureContext:
        """Immediately creates a new TextureContext for the indicated texture and
        returns it.  This assumes that the GraphicsStateGuardian is the currently
        active rendering context and that it is ready to accept new textures.  If
        this is not necessarily the case, you should use enqueue_texture() instead.

        Normally, this function is not called directly.  Call
        Texture::prepare_now() instead.

        The TextureContext contains all of the pertinent information needed by the
        GSG to keep track of this one particular texture, and will exist as long as
        the texture is ready to be rendered.

        When either the Texture or the PreparedGraphicsObjects object destructs,
        the TextureContext will be deleted.
        """
    def enqueue_sampler(self, sampler: SamplerState) -> None:
        """Indicates that a sampler would like to be put on the list to be prepared
        when the GSG is next ready to do this (presumably at the next frame).
        """
    def is_sampler_queued(self, sampler: SamplerState) -> bool:
        """Returns true if the sampler has been queued on this GSG, false otherwise."""
    def dequeue_sampler(self, sampler: SamplerState) -> bool:
        """Removes a sampler from the queued list of samplers to be prepared.
        Normally it is not necessary to call this, unless you change your mind
        about preparing it at the last minute, since the sampler will automatically
        be dequeued and prepared at the next frame.

        The return value is true if the sampler is successfully dequeued, false if
        it had not been queued.
        """
    def is_sampler_prepared(self, sampler: SamplerState) -> bool:
        """Returns true if the sampler has been prepared on this GSG, false otherwise."""
    def release_sampler(self, sampler: SamplerState) -> None:
        """Releases a sampler if it has already been prepared, or removes it from the
        preparation queue.
        """
    def release_all_samplers(self) -> int:
        """Releases all samplers at once.  This will force them to be reloaded for all
        GSG's that share this object.  Returns the number of samplers released.
        """
    def get_num_queued_samplers(self) -> int:
        """Returns the number of samplers that have been enqueued to be prepared on
        this GSG.
        """
    def get_num_prepared_samplers(self) -> int:
        """Returns the number of samplers that have already been prepared on this GSG."""
    def enqueue_geom(self, geom: Geom) -> None:
        """Indicates that a geom would like to be put on the list to be prepared when
        the GSG is next ready to do this (presumably at the next frame).
        """
    def is_geom_queued(self, geom: Geom) -> bool:
        """Returns true if the geom has been queued on this GSG, false otherwise."""
    def dequeue_geom(self, geom: Geom) -> bool:
        """Removes a geom from the queued list of geoms to be prepared.  Normally it
        is not necessary to call this, unless you change your mind about preparing
        it at the last minute, since the geom will automatically be dequeued and
        prepared at the next frame.

        The return value is true if the geom is successfully dequeued, false if it
        had not been queued.
        """
    def is_geom_prepared(self, geom: Geom) -> bool:
        """Returns true if the vertex buffer has been prepared on this GSG, false
        otherwise.
        """
    def release_geom(self, gc: GeomContext) -> None:
        """Indicates that a geom context, created by a previous call to
        prepare_geom(), is no longer needed.  The driver resources will not be
        freed until some GSG calls update(), indicating it is at a stage where it
        is ready to release geoms--this prevents conflicts from threading or
        multiple GSG's sharing geoms (we have no way of knowing which graphics
        context is currently active, or what state it's in, at the time
        release_geom is called).
        """
    def release_all_geoms(self) -> int:
        """Releases all geoms at once.  This will force them to be reloaded into geom
        memory for all GSG's that share this object.  Returns the number of geoms
        released.
        """
    def get_num_queued_geoms(self) -> int:
        """Returns the number of geoms that have been enqueued to be prepared on this
        GSG.
        """
    def get_num_prepared_geoms(self) -> int:
        """Returns the number of geoms that have already been prepared on this GSG."""
    def prepare_geom_now(self, geom: Geom, gsg: GraphicsStateGuardianBase) -> GeomContext:
        """Immediately creates a new GeomContext for the indicated geom and returns
        it.  This assumes that the GraphicsStateGuardian is the currently active
        rendering context and that it is ready to accept new geoms.  If this is not
        necessarily the case, you should use enqueue_geom() instead.

        Normally, this function is not called directly.  Call Geom::prepare_now()
        instead.

        The GeomContext contains all of the pertinent information needed by the GSG
        to keep track of this one particular geom, and will exist as long as the
        geom is ready to be rendered.

        When either the Geom or the PreparedGraphicsObjects object destructs, the
        GeomContext will be deleted.
        """
    def enqueue_shader(self, shader: Shader) -> None:
        """Indicates that a shader would like to be put on the list to be prepared
        when the GSG is next ready to do this (presumably at the next frame).
        """
    def is_shader_queued(self, shader: Shader) -> bool:
        """Returns true if the shader has been queued on this GSG, false otherwise."""
    def dequeue_shader(self, shader: Shader) -> bool:
        """Removes a shader from the queued list of shaders to be prepared.  Normally
        it is not necessary to call this, unless you change your mind about
        preparing it at the last minute, since the shader will automatically be
        dequeued and prepared at the next frame.

        The return value is true if the shader is successfully dequeued, false if
        it had not been queued.
        """
    def is_shader_prepared(self, shader: Shader) -> bool:
        """Returns true if the shader has been prepared on this GSG, false otherwise."""
    def release_shader(self, sc: ShaderContext) -> None:
        """Indicates that a shader context, created by a previous call to
        prepare_shader(), is no longer needed.  The driver resources will not be
        freed until some GSG calls update(), indicating it is at a stage where it
        is ready to release shaders--this prevents conflicts from threading or
        multiple GSG's sharing shaders (we have no way of knowing which graphics
        context is currently active, or what state it's in, at the time
        release_shader is called).
        """
    def release_all_shaders(self) -> int:
        """Releases all shaders at once.  This will force them to be reloaded into
        shader memory for all GSG's that share this object.  Returns the number of
        shaders released.
        """
    def get_num_queued_shaders(self) -> int:
        """Returns the number of shaders that have been enqueued to be prepared on
        this GSG.
        """
    def get_num_prepared_shaders(self) -> int:
        """Returns the number of shaders that have already been prepared on this GSG."""
    def prepare_shader_now(self, shader: Shader, gsg: GraphicsStateGuardianBase) -> ShaderContext:
        """Immediately creates a new ShaderContext for the indicated shader and
        returns it.  This assumes that the GraphicsStateGuardian is the currently
        active rendering context and that it is ready to accept new shaders.  If
        this is not necessarily the case, you should use enqueue_shader() instead.

        Normally, this function is not called directly.  Call Shader::prepare_now()
        instead.

        The ShaderContext contains all of the pertinent information needed by the
        GSG to keep track of this one particular shader, and will exist as long as
        the shader is ready to be rendered.

        When either the Shader or the PreparedGraphicsObjects object destructs, the
        ShaderContext will be deleted.
        """
    def enqueue_vertex_buffer(self, data: GeomVertexArrayData) -> None:
        """Indicates that a buffer would like to be put on the list to be prepared
        when the GSG is next ready to do this (presumably at the next frame).
        """
    def is_vertex_buffer_queued(self, data: GeomVertexArrayData) -> bool:
        """Returns true if the vertex buffer has been queued on this GSG, false
        otherwise.
        """
    def dequeue_vertex_buffer(self, data: GeomVertexArrayData) -> bool:
        """Removes a buffer from the queued list of data arrays to be prepared.
        Normally it is not necessary to call this, unless you change your mind
        about preparing it at the last minute, since the data will automatically be
        dequeued and prepared at the next frame.

        The return value is true if the buffer is successfully dequeued, false if
        it had not been queued.
        """
    def is_vertex_buffer_prepared(self, data: GeomVertexArrayData) -> bool:
        """Returns true if the vertex buffer has been prepared on this GSG, false
        otherwise.
        """
    def release_vertex_buffer(self, vbc: VertexBufferContext) -> None:
        """Indicates that a data context, created by a previous call to
        prepare_vertex_buffer(), is no longer needed.  The driver resources will
        not be freed until some GSG calls update(), indicating it is at a stage
        where it is ready to release datas--this prevents conflicts from threading
        or multiple GSG's sharing datas (we have no way of knowing which graphics
        context is currently active, or what state it's in, at the time
        release_vertex_buffer is called).
        """
    def release_all_vertex_buffers(self) -> int:
        """Releases all datas at once.  This will force them to be reloaded into data
        memory for all GSG's that share this object.  Returns the number of datas
        released.
        """
    def get_num_queued_vertex_buffers(self) -> int:
        """Returns the number of vertex buffers that have been enqueued to be prepared
        on this GSG.
        """
    def get_num_prepared_vertex_buffers(self) -> int:
        """Returns the number of vertex buffers that have already been prepared on
        this GSG.
        """
    def prepare_vertex_buffer_now(self, data: GeomVertexArrayData, gsg: GraphicsStateGuardianBase) -> VertexBufferContext:
        """Immediately creates a new VertexBufferContext for the indicated data and
        returns it.  This assumes that the GraphicsStateGuardian is the currently
        active rendering context and that it is ready to accept new datas.  If this
        is not necessarily the case, you should use enqueue_vertex_buffer()
        instead.

        Normally, this function is not called directly.  Call Data::prepare_now()
        instead.

        The VertexBufferContext contains all of the pertinent information needed by
        the GSG to keep track of this one particular data, and will exist as long
        as the data is ready to be rendered.

        When either the Data or the PreparedGraphicsObjects object destructs, the
        VertexBufferContext will be deleted.
        """
    def enqueue_index_buffer(self, data: GeomPrimitive) -> None:
        """Indicates that a buffer would like to be put on the list to be prepared
        when the GSG is next ready to do this (presumably at the next frame).
        """
    def is_index_buffer_queued(self, data: GeomPrimitive) -> bool:
        """Returns true if the index buffer has been queued on this GSG, false
        otherwise.
        """
    def dequeue_index_buffer(self, data: GeomPrimitive) -> bool:
        """Removes a buffer from the queued list of data arrays to be prepared.
        Normally it is not necessary to call this, unless you change your mind
        about preparing it at the last minute, since the data will automatically be
        dequeued and prepared at the next frame.

        The return value is true if the buffer is successfully dequeued, false if
        it had not been queued.
        """
    def is_index_buffer_prepared(self, data: GeomPrimitive) -> bool:
        """Returns true if the index buffer has been prepared on this GSG, false
        otherwise.
        """
    def release_index_buffer(self, ibc: IndexBufferContext) -> None:
        """Indicates that a data context, created by a previous call to
        prepare_index_buffer(), is no longer needed.  The driver resources will not
        be freed until some GSG calls update(), indicating it is at a stage where
        it is ready to release datas--this prevents conflicts from threading or
        multiple GSG's sharing datas (we have no way of knowing which graphics
        context is currently active, or what state it's in, at the time
        release_index_buffer is called).
        """
    def release_all_index_buffers(self) -> int:
        """Releases all datas at once.  This will force them to be reloaded into data
        memory for all GSG's that share this object.  Returns the number of datas
        released.
        """
    def get_num_queued_index_buffers(self) -> int:
        """Returns the number of index buffers that have been enqueued to be prepared
        on this GSG.
        """
    def get_num_prepared_index_buffers(self) -> int:
        """Returns the number of index buffers that have already been prepared on this
        GSG.
        """
    def prepare_index_buffer_now(self, data: GeomPrimitive, gsg: GraphicsStateGuardianBase) -> IndexBufferContext:
        """Immediately creates a new IndexBufferContext for the indicated data and
        returns it.  This assumes that the GraphicsStateGuardian is the currently
        active rendering context and that it is ready to accept new datas.  If this
        is not necessarily the case, you should use enqueue_index_buffer() instead.

        Normally, this function is not called directly.  Call Data::prepare_now()
        instead.

        The IndexBufferContext contains all of the pertinent information needed by
        the GSG to keep track of this one particular data, and will exist as long
        as the data is ready to be rendered.

        When either the Data or the PreparedGraphicsObjects object destructs, the
        IndexBufferContext will be deleted.
        """
    def enqueue_shader_buffer(self, data: ShaderBuffer) -> None:
        """Indicates that a buffer would like to be put on the list to be prepared
        when the GSG is next ready to do this (presumably at the next frame).
        """
    def is_shader_buffer_queued(self, data: ShaderBuffer) -> bool:
        """Returns true if the index buffer has been queued on this GSG, false
        otherwise.
        """
    def dequeue_shader_buffer(self, data: ShaderBuffer) -> bool:
        """Removes a buffer from the queued list of data arrays to be prepared.
        Normally it is not necessary to call this, unless you change your mind
        about preparing it at the last minute, since the data will automatically be
        dequeued and prepared at the next frame.

        The return value is true if the buffer is successfully dequeued, false if
        it had not been queued.
        """
    def is_shader_buffer_prepared(self, data: ShaderBuffer) -> bool:
        """Returns true if the index buffer has been prepared on this GSG, false
        otherwise.
        """
    def release_shader_buffer(self, bc: BufferContext) -> None:
        """Indicates that a data context, created by a previous call to
        prepare_shader_buffer(), is no longer needed.  The driver resources will not
        be freed until some GSG calls update(), indicating it is at a stage where
        it is ready to release datas--this prevents conflicts from threading or
        multiple GSG's sharing datas (we have no way of knowing which graphics
        context is currently active, or what state it's in, at the time
        release_shader_buffer is called).
        """
    def release_all_shader_buffers(self) -> int:
        """Releases all datas at once.  This will force them to be reloaded into data
        memory for all GSG's that share this object.  Returns the number of datas
        released.
        """
    def get_num_queued_shader_buffers(self) -> int:
        """Returns the number of index buffers that have been enqueued to be prepared
        on this GSG.
        """
    def get_num_prepared_shader_buffers(self) -> int:
        """Returns the number of index buffers that have already been prepared on this
        GSG.
        """
    def prepare_shader_buffer_now(self, data: ShaderBuffer, gsg: GraphicsStateGuardianBase) -> BufferContext:
        """Immediately creates a new BufferContext for the indicated data and
        returns it.  This assumes that the GraphicsStateGuardian is the currently
        active rendering context and that it is ready to accept new datas.  If this
        is not necessarily the case, you should use enqueue_shader_buffer() instead.

        Normally, this function is not called directly.  Call Data::prepare_now()
        instead.

        The BufferContext contains all of the pertinent information needed by
        the GSG to keep track of this one particular data, and will exist as long
        as the data is ready to be rendered.

        When either the Data or the PreparedGraphicsObjects object destructs, the
        BufferContext will be deleted.
        """
    getName = get_name
    setGraphicsMemoryLimit = set_graphics_memory_limit
    getGraphicsMemoryLimit = get_graphics_memory_limit
    showGraphicsMemoryLru = show_graphics_memory_lru
    showResidencyTrackers = show_residency_trackers
    releaseAll = release_all
    getNumQueued = get_num_queued
    getNumPrepared = get_num_prepared
    enqueueTexture = enqueue_texture
    isTextureQueued = is_texture_queued
    dequeueTexture = dequeue_texture
    isTexturePrepared = is_texture_prepared
    releaseTexture = release_texture
    releaseAllTextures = release_all_textures
    getNumQueuedTextures = get_num_queued_textures
    getNumPreparedTextures = get_num_prepared_textures
    prepareTextureNow = prepare_texture_now
    enqueueSampler = enqueue_sampler
    isSamplerQueued = is_sampler_queued
    dequeueSampler = dequeue_sampler
    isSamplerPrepared = is_sampler_prepared
    releaseSampler = release_sampler
    releaseAllSamplers = release_all_samplers
    getNumQueuedSamplers = get_num_queued_samplers
    getNumPreparedSamplers = get_num_prepared_samplers
    enqueueGeom = enqueue_geom
    isGeomQueued = is_geom_queued
    dequeueGeom = dequeue_geom
    isGeomPrepared = is_geom_prepared
    releaseGeom = release_geom
    releaseAllGeoms = release_all_geoms
    getNumQueuedGeoms = get_num_queued_geoms
    getNumPreparedGeoms = get_num_prepared_geoms
    prepareGeomNow = prepare_geom_now
    enqueueShader = enqueue_shader
    isShaderQueued = is_shader_queued
    dequeueShader = dequeue_shader
    isShaderPrepared = is_shader_prepared
    releaseShader = release_shader
    releaseAllShaders = release_all_shaders
    getNumQueuedShaders = get_num_queued_shaders
    getNumPreparedShaders = get_num_prepared_shaders
    prepareShaderNow = prepare_shader_now
    enqueueVertexBuffer = enqueue_vertex_buffer
    isVertexBufferQueued = is_vertex_buffer_queued
    dequeueVertexBuffer = dequeue_vertex_buffer
    isVertexBufferPrepared = is_vertex_buffer_prepared
    releaseVertexBuffer = release_vertex_buffer
    releaseAllVertexBuffers = release_all_vertex_buffers
    getNumQueuedVertexBuffers = get_num_queued_vertex_buffers
    getNumPreparedVertexBuffers = get_num_prepared_vertex_buffers
    prepareVertexBufferNow = prepare_vertex_buffer_now
    enqueueIndexBuffer = enqueue_index_buffer
    isIndexBufferQueued = is_index_buffer_queued
    dequeueIndexBuffer = dequeue_index_buffer
    isIndexBufferPrepared = is_index_buffer_prepared
    releaseIndexBuffer = release_index_buffer
    releaseAllIndexBuffers = release_all_index_buffers
    getNumQueuedIndexBuffers = get_num_queued_index_buffers
    getNumPreparedIndexBuffers = get_num_prepared_index_buffers
    prepareIndexBufferNow = prepare_index_buffer_now
    enqueueShaderBuffer = enqueue_shader_buffer
    isShaderBufferQueued = is_shader_buffer_queued
    dequeueShaderBuffer = dequeue_shader_buffer
    isShaderBufferPrepared = is_shader_buffer_prepared
    releaseShaderBuffer = release_shader_buffer
    releaseAllShaderBuffers = release_all_shader_buffers
    getNumQueuedShaderBuffers = get_num_queued_shader_buffers
    getNumPreparedShaderBuffers = get_num_prepared_shader_buffers
    prepareShaderBufferNow = prepare_shader_buffer_now

class IndexBufferContext(BufferContext, AdaptiveLruPage):
    """This is a special class object that holds all the information returned by a
    particular GSG to indicate the vertex data array's internal context
    identifier.

    This allows the GSG to cache the vertex data array in whatever way makes
    sense.  For instance, DirectX can allocate a vertex buffer for the array.
    OpenGL can create a buffer object.
    """

    def upcast_to_BufferContext(self) -> BufferContext: ...
    def upcast_to_AdaptiveLruPage(self) -> AdaptiveLruPage: ...
    def get_data(self) -> GeomPrimitive:
        """Returns the pointer to the client-side array data object."""
    upcastToBufferContext = upcast_to_BufferContext
    upcastToAdaptiveLruPage = upcast_to_AdaptiveLruPage
    getData = get_data

class Lens(TypedWritableReferenceCount):
    """A base class for any number of different kinds of lenses, linear and
    otherwise.  Presently, this includes perspective and orthographic lenses.

    A Lens object is the main part of a Camera node, which defines the
    fundamental interface to point-of-view for rendering.  Lenses are also used
    in other contexts, however; for instance, a Spotlight is also defined using
    a lens.
    """

    SC_mono: Final = 0
    SCMono: Final = 0
    SC_left: Final = 1
    SCLeft: Final = 1
    SC_right: Final = 2
    SCRight: Final = 2
    SC_stereo: Final = 3
    SCStereo: Final = 3
    FC_roll: Final = 1
    FCRoll: Final = 1
    FC_camera_plane: Final = 2
    FCCameraPlane: Final = 2
    FC_off_axis: Final = 4
    FCOffAxis: Final = 4
    FC_aspect_ratio: Final = 8
    FCAspectRatio: Final = 8
    FC_shear: Final = 16
    FCShear: Final = 16
    FC_keystone: Final = 32
    FCKeystone: Final = 32
    change_event: str
    coordinate_system: _CoordinateSystem
    film_size: LVecBase2
    film_offset: LVector2
    focal_length: float
    fov: LVecBase2
    min_fov: float
    aspect_ratio: float
    near: float
    far: float
    view_hpr: LVecBase3
    interocular_distance: float
    convergence_distance: float
    view_mat: LMatrix4
    keystone: LVecBase2
    @property
    def nodal_point(self) -> LPoint3: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def make_copy(self) -> Lens: ...
    def extrude(self, point2d: Vec2Like | Vec3Like, near_point: Vec3Like, far_point: Vec3Like) -> bool:
        """`(self, point2d: LPoint2, near_point: LPoint3, far_point: LPoint3)`:
        Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
        the center of the lens and (-1,-1) is the lower-left corner, compute the
        corresponding vector in space that maps to this point, if such a vector can
        be determined.  The vector is returned by indicating the points on the near
        plane and far plane that both map to the indicated 2-d point.

        Returns true if the vector is defined, or false otherwise.

        `(self, point2d: LPoint3, near_point: LPoint3, far_point: LPoint3)`:
        Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
        the center of the lens and (-1,-1) is the lower-left corner, compute the
        corresponding vector in space that maps to this point, if such a vector can
        be determined.  The vector is returned by indicating the points on the near
        plane and far plane that both map to the indicated 2-d point.

        The z coordinate of the 2-d point is ignored.

        Returns true if the vector is defined, or false otherwise.
        """
    def extrude_depth(self, point2d: Vec3Like, point3d: Vec3Like) -> bool:
        """Uses the depth component of the 3-d result from project() to compute the
        original point in 3-d space corresponding to a particular point on the
        lens.  This exactly reverses project(), assuming the point does fall
        legitimately within the lens.
        """
    def extrude_vec(self, point2d: Vec2Like | Vec3Like, vec3d: Vec3Like) -> bool:
        """`(self, point2d: LPoint2, vec3d: LVector3)`:
        Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
        the center of the lens and (-1,-1) is the lower-left corner, compute the
        vector that corresponds to the view direction.  This will be parallel to
        the normal on the surface (the far plane) corresponding to the lens shape
        at this point.

        See the comment block on Lens::extrude_vec_impl() for a more in-depth
        comment on the meaning of this vector.

        Returns true if the vector is defined, or false otherwise.

        `(self, point2d: LPoint3, vec3d: LVector3)`:
        Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
        the center of the lens and (-1,-1) is the lower-left corner, compute the
        vector that corresponds to the view direction.  This will be parallel to
        the normal on the surface (the far plane) corresponding to the lens shape
        at this point.

        See the comment block on Lens::extrude_vec_impl() for a more in-depth
        comment on the meaning of this vector.

        The z coordinate of the 2-d point is ignored.

        Returns true if the vector is defined, or false otherwise.
        """
    def project(self, point3d: Vec3Like, point2d: Vec2Like | Vec3Like) -> bool:
        """`(self, point3d: LPoint3, point2d: LPoint2)`:
        Given a 3-d point in space, determine the 2-d point this maps to, in the
        range (-1,1) in both dimensions, where (0,0) is the center of the lens and
        (-1,-1) is the lower-left corner.

        Returns true if the 3-d point is in front of the lens and within the
        viewing frustum (in which case point2d is filled in), or false otherwise
        (in which case point2d will be filled in with something, which may or may
        not be meaningful).

        `(self, point3d: LPoint3, point2d: LPoint3)`:
        Given a 3-d point in space, determine the 2-d point this maps to, in the
        range (-1,1) in both dimensions, where (0,0) is the center of the lens and
        (-1,-1) is the lower-left corner.

        The z coordinate will also be set to a value in the range (-1, 1), where 1
        represents a point on the near plane, and -1 represents a point on the far
        plane.

        Returns true if the 3-d point is in front of the lens and within the
        viewing frustum (in which case point2d is filled in), or false otherwise
        (in which case point2d will be filled in with something, which may or may
        not be meaningful).
        """
    def set_change_event(self, event: str) -> None:
        """Sets the name of the event that will be generated whenever any properties
        of the Lens have changed.  If this is not set for a particular lens, no
        event will be generated.

        The event is thrown with one parameter, the lens itself.  This can be used
        to automatically track changes to camera fov, etc.  in the application.
        """
    def get_change_event(self) -> str:
        """Returns the name of the event that will be generated whenever any
        properties of this particular Lens have changed.
        """
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None:
        """Specifies the coordinate system that all 3-d computations are performed
        within for this Lens.  Normally, this is CS_default.
        """
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system that all 3-d computations are performed
        within for this Lens.  Normally, this is CS_default.
        """
    def clear(self) -> None:
        """Resets all lens parameters to their initial default settings."""
    @overload
    def set_film_size(self, film_size: Vec2Like) -> None:
        """`(self, film_size: LVecBase2)`; `(self, width: float, height: float)`:
        Sets the size and shape of the "film" within the lens.  This both
        establishes the units used by calls like set_focal_length(), and
        establishes the aspect ratio of the frame.

        In a physical camera, the field of view of a lens is determined by the
        lens' focal length and by the size of the film area exposed by the lens.
        For instance, a 35mm camera exposes a rectangle on the film about 24mm x
        36mm, which means a 50mm lens gives about a 40-degree horizontal field of
        view.

        In the virtual camera, you may set the film size to any units here, and
        specify a focal length in the same units to simulate the same effect.  Or,
        you may ignore this parameter, and specify the field of view and aspect
        ratio of the lens directly.

        `(self, width: float)`:
        Sets the horizontal size of the film without changing its shape.  The
        aspect ratio remains unchanged; this computes the vertical size of the film
        to automatically maintain the aspect ratio.
        """
    @overload
    def set_film_size(self, width: float, height: float = ...) -> None: ...
    def get_film_size(self) -> LVecBase2:
        """Returns the horizontal and vertical film size of the virtual film.  See
        set_film_size().
        """
    @overload
    def set_film_offset(self, film_offset: Vec2Like) -> None:
        """Sets the horizontal and vertical offset amounts of this Lens.  These are
        both in the same units specified in set_film_size().

        This can be used to establish an off-axis lens.
        """
    @overload
    def set_film_offset(self, x: float, y: float) -> None: ...
    def get_film_offset(self) -> LVector2:
        """Returns the horizontal and vertical offset amounts of this Lens.  See
        set_film_offset().
        """
    def set_focal_length(self, focal_length: float) -> None:
        """Sets the focal length of the lens.  This may adjust the field-of-view
        correspondingly, and is an alternate way to specify field of view.

        For certain kinds of lenses (e.g.  OrthographicLens), the focal length has
        no meaning.
        """
    def get_focal_length(self) -> float:
        """Returns the focal length of the lens.  This may have been set explicitly by
        a previous call to set_focal_length(), or it may be computed based on the
        lens' fov and film_size.  For certain kinds of lenses, the focal length has
        no meaning.
        """
    def set_min_fov(self, min_fov: float) -> None:
        """Sets the field of view of the smallest dimension of the window.  If the
        window is wider than it is tall, this specifies the vertical field of view;
        if it is taller than it is wide, this specifies the horizontal field of
        view.

        In many cases, this is preferable to setting either the horizontal or
        vertical field of view explicitly.  Setting this parameter means that
        pulling the window wider will widen the field of view, which is usually
        what you expect to happen.
        """
    @overload
    def set_fov(self, fov: Vec2Like | float) -> None:
        """`(self, fov: LVecBase2)`:
        Sets the field of view of the lens in both dimensions.  This establishes
        both the field of view and the aspect ratio of the lens.  This is one way
        to specify the field of view of a lens; set_focal_length() is another way.

        For certain kinds of lenses (like OrthographicLens), the field of view has
        no meaning.

        `(self, fov: float)`:
        Sets the horizontal field of view of the lens without changing the aspect
        ratio.  The vertical field of view is adjusted to maintain the same aspect
        ratio.

        `(self, hfov: float, vfov: float)`:
        Sets the field of view of the lens in both dimensions.  This establishes
        both the field of view and the aspect ratio of the lens.  This is one way
        to specify the field of view of a lens; set_focal_length() is another way.

        For certain kinds of lenses (like OrthoLens), the field of view has no
        meaning.
        """
    @overload
    def set_fov(self, hfov: float, vfov: float) -> None: ...
    def get_fov(self) -> LVecBase2:
        """Returns the horizontal and vertical film size of the virtual film.  See
        set_fov().
        """
    def get_hfov(self) -> float:
        """Returns the horizontal component of fov only.  See get_fov()."""
    def get_vfov(self) -> float:
        """Returns the vertical component of fov only.  See get_fov()."""
    def get_min_fov(self) -> float:
        """Returns the field of view of the narrowest dimension of the window.  See
        set_min_fov().
        """
    def set_aspect_ratio(self, aspect_ratio: float) -> None:
        """Sets the aspect ratio of the lens.  This is the ratio of the height to the
        width of the generated image.  Setting this overrides the two-parameter fov
        or film size setting.
        """
    def get_aspect_ratio(self) -> float:
        """Returns the aspect ratio of the Lens.  This is determined based on the
        indicated film size; see set_film_size().
        """
    def set_near(self, near_distance: float) -> None:
        """Defines the position of the near plane (or cylinder, sphere, whatever).
        Points closer to the lens than this may not be rendered.
        """
    def get_near(self) -> float:
        """Returns the position of the near plane (or cylinder, sphere, whatever)."""
    def set_far(self, far_distance: float) -> None:
        """Defines the position of the far plane (or cylinder, sphere, whatever).
        Points farther from the lens than this may not be rendered.
        """
    def get_far(self) -> float:
        """Returns the position of the far plane (or cylinder, sphere, whatever)."""
    def set_near_far(self, near_distance: float, far_distance: float) -> None:
        """Simultaneously changes the near and far planes."""
    @staticmethod
    def get_default_near() -> float:
        """Returns the default near plane distance that will be assigned to each
        newly-created lens.  This is read from the Config.prc file.
        """
    @staticmethod
    def get_default_far() -> float:
        """Returns the default far plane distance that will be assigned to each newly-
        created lens.  This is read from the Config.prc file.
        """
    @overload
    def set_view_hpr(self, view_hpr: Vec3Like) -> None:
        """Sets the direction in which the lens is facing.  Normally, this is down the
        forward axis (usually the Y axis), but it may be rotated.  This is only one
        way of specifying the rotation; you may also specify an explicit vector in
        which to look, or you may give a complete transformation matrix.
        """
    @overload
    def set_view_hpr(self, h: float, p: float, r: float) -> None: ...
    def get_view_hpr(self) -> LVecBase3:
        """Returns the direction in which the lens is facing."""
    @overload
    def set_view_vector(self, view_vector: Vec3Like, up_vector: Vec3Like) -> None:
        """Specifies the direction in which the lens is facing by giving an axis to
        look along, and a perpendicular (or at least non-parallel) up axis.

        See also set_view_hpr().
        """
    @overload
    def set_view_vector(self, x: float, y: float, z: float, i: float, j: float, k: float) -> None: ...
    def get_view_vector(self) -> LVector3:
        """Returns the axis along which the lens is facing."""
    def get_up_vector(self) -> LVector3:
        """Returns the axis perpendicular to the camera's view vector that indicates
        the "up" direction.
        """
    def get_nodal_point(self) -> LPoint3:
        """Returns the center point of the lens: the point from which the lens is
        viewing.
        """
    def set_interocular_distance(self, interocular_distance: float) -> None:
        """Sets the distance between the left and right eyes of a stereo camera.  This
        distance is used to apply a stereo effect when the lens is rendered on a
        stereo display region.  It only has an effect on a PerspectiveLens.

        The left eye and the right eye are each offset along the X axis by half of
        this distance, so that this parameter specifies the total distance between
        them.

        Also see set_convergence_distance(), which relates.
        """
    def get_interocular_distance(self) -> float:
        """See set_interocular_distance()."""
    def set_convergence_distance(self, convergence_distance: float) -> None:
        """Sets the distance between between the camera plane and the point in the
        distance that the left and right eyes are both looking at.  This distance
        is used to apply a stereo effect when the lens is rendered on a stereo
        display region.  It only has an effect on a PerspectiveLens.

        This parameter must be greater than 0, but may be as large as you like.  It
        controls the distance at which the two stereo images will appear to
        converge, which is a normal property of stereo vision.  Normally this
        should be set to the distance from the camera to the area of interest in
        your scene.  Anything beyond this distance will appear to go into the
        screen, and anything closer will appear to come out of the screen.  If you
        want to simulate parallel stereo, set this to infinity.

        Note that this creates an off-axis frustum, which means that the lenses are
        still pointing in the same direction, which is usually more desirable than
        the more naive toe-in approach, where the two lenses are simply tilted
        toward each other.

        Prior to Panda3D 1.9.0, the convergence was being calculated incorrectly.
        It has since been corrected.  To restore the legacy behavior you can set
        the stereo-lens-old-convergence variable to true.

        Also see set_interocular_distance(), which relates.
        """
    def get_convergence_distance(self) -> float:
        """See set_convergence_distance()."""
    def set_view_mat(self, view_mat: Mat4Like) -> None:
        """Sets an arbitrary transformation on the lens.  This replaces the individual
        transformation components like set_view_hpr().

        Setting a transformation here will have a slightly different effect than
        putting one on the LensNode that contains this lens.  In particular,
        lighting and other effects computations will still be performed on the lens
        in its untransformed (facing forward) position, but the actual projection
        matrix will be transformed by this matrix.
        """
    def get_view_mat(self) -> LMatrix4:
        """Returns the direction in which the lens is facing."""
    def clear_view_mat(self) -> None:
        """Resets the lens transform to identity."""
    def set_keystone(self, keystone: Vec2Like) -> None:
        """Indicates the ratio of keystone correction to perform on the lens, in each
        of three axes.  This will build a special non-affine scale factor into the
        projection matrix that will compensate for keystoning of a projected image;
        this can be used to compensate for a projector that for physical reasons
        cannot be aimed directly at its screen.

        The default value is taken from the default-keystone Config variable.  0, 0
        indicates no keystone correction; specify a small value (usually in the
        range -1 .. 1) in either the x or y position to generate a keystone
        correction in that axis.
        """
    def get_keystone(self) -> LVecBase2:
        """Returns the keystone correction specified for the lens."""
    def clear_keystone(self) -> None:
        """Disables the lens keystone correction."""
    def set_custom_film_mat(self, custom_film_mat: Mat4Like) -> None:
        """Specifies a custom matrix to transform the points on the film after they
        have been converted into nominal film space (-1 .. 1 in U and V).  This can
        be used to introduce arbitrary scales, rotations, or other linear
        transforms to the media plane.  This is normally a 2-d matrix, but a full
        4x4 matrix may be specified.  This is applied on top of any film size, lens
        shift, and/or keystone correction.
        """
    def get_custom_film_mat(self) -> LMatrix4:
        """Returns the custom_film_mat specified for the lens."""
    def clear_custom_film_mat(self) -> None:
        """Disables the lens custom_film_mat correction."""
    def set_frustum_from_corners(self, ul: Vec3Like, ur: Vec3Like, ll: Vec3Like, lr: Vec3Like, flags: int) -> None:
        """Sets up the lens to use the frustum defined by the four indicated points.
        This is most useful for a PerspectiveLens, but it may be called for other
        kinds of lenses as well.

        The frustum will be rooted at the origin (or by whatever translation might
        have been specified in a previous call to set_view_mat).

        It is legal for the four points not to be arranged in a rectangle; if this
        is the case, the frustum will be fitted as tightly as possible to cover all
        four points.

        The flags parameter contains the union of one or more of the following bits
        to control the behavior of this function:

        FC_roll - If this is included, the camera may be rotated so that its up
        vector is perpendicular to the top line.  Otherwise, the standard up vector
        is used.

        FC_camera_plane - This allows the camera plane to be adjusted to be as
        nearly perpendicular to the center of the frustum as possible.  Without
        this bit, the orientation camera plane is defined by position of the four
        points (which should all be coplanar).  With this bit, the camera plane is
        arbitrary, and may be chosen so that the four points do not themselves lie
        in the camera plane (but the points will still be within the frustum).

        FC_off_axis - This allows the resulting frustum to be off-axis to get the
        tightest possible fit.  Without this bit, the viewing axis will be centered
        within the frustum, but there may be more wasted space along the edges.

        FC_aspect_ratio - This allows the frustum to be scaled non-proportionately
        in the vertical and horizontal dimensions, if necessary, to get a tighter
        fit.  Without this bit, the current aspect ratio will be preserved.

        FC_shear - This allows the frustum to be sheared, if necessary, to get the
        tightest possible fit.  This may result in a parallelogram-based frustum,
        which will give a slanted appearance to the rendered image.  Without this
        bit, the frustum will be rectangle-based.

        In general, if 0 is passed in as the value for flags, the generated frustum
        will be a loose fit but sane; if -1 is passed in, it will be a tighter fit
        and possibly screwy.
        """
    def recompute_all(self) -> None:
        """Forces all internal parameters of the Lens to be recomputed.  Normally,
        this should never need to be called; it is provided only to assist in
        debugging.
        """
    def is_linear(self) -> bool:
        """Returns true if the lens represents a linear projection (e.g.
        PerspectiveLens, OrthographicLens), and therefore there is a valid matrix
        returned by get_projection_mat(), or false otherwise.
        """
    def is_perspective(self) -> bool:
        """Returns true if the lens represents a perspective projection (i.e.  it is a
        PerspectiveLens), false otherwise.
        """
    def is_orthographic(self) -> bool:
        """Returns true if the lens represents a orthographic projection (i.e.  it is
        a OrthographicLens), false otherwise.
        """
    def make_geometry(self) -> Geom:
        """Allocates and returns a new Geom that can be rendered to show a visible
        representation of the frustum used for this kind of lens, if it makes sense
        to do so.  If a visible representation cannot be created, returns NULL.
        """
    def make_bounds(self) -> BoundingVolume:
        """Allocates and returns a new BoundingVolume that encloses the frustum used
        for this kind of lens, if possible.  If a suitable bounding volume cannot
        be created, returns NULL.
        """
    def get_projection_mat(self, channel: _Lens_StereoChannel = ...) -> LMatrix4:
        """Returns the complete transformation matrix from a 3-d point in space to a
        point on the film, if such a matrix exists, or the identity matrix if the
        lens is nonlinear.
        """
    def get_projection_mat_inv(self, channel: _Lens_StereoChannel = ...) -> LMatrix4:
        """Returns the matrix that transforms from a 2-d point on the film to a 3-d
        vector in space, if such a matrix exists.
        """
    def get_film_mat(self) -> LMatrix4:
        """Returns the matrix that transforms from a point behind the lens to a point
        on the film.
        """
    def get_film_mat_inv(self) -> LMatrix4:
        """Returns the matrix that transforms from a point on the film to a point
        behind the lens.
        """
    def get_lens_mat(self) -> LMatrix4:
        """Returns the matrix that transforms from a point in front of the lens to a
        point in space.
        """
    def get_lens_mat_inv(self) -> LMatrix4:
        """Returns the matrix that transforms from a point in space to a point in
        front of the lens.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def get_last_change(self) -> UpdateSeq:
        """Returns the UpdateSeq that is incremented whenever the lens properties are
        changed.  As long as this number remains the same, you may assume the lens
        properties are unchanged.
        """
    makeCopy = make_copy
    extrudeDepth = extrude_depth
    extrudeVec = extrude_vec
    setChangeEvent = set_change_event
    getChangeEvent = get_change_event
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    setFilmSize = set_film_size
    getFilmSize = get_film_size
    setFilmOffset = set_film_offset
    getFilmOffset = get_film_offset
    setFocalLength = set_focal_length
    getFocalLength = get_focal_length
    setMinFov = set_min_fov
    setFov = set_fov
    getFov = get_fov
    getHfov = get_hfov
    getVfov = get_vfov
    getMinFov = get_min_fov
    setAspectRatio = set_aspect_ratio
    getAspectRatio = get_aspect_ratio
    setNear = set_near
    getNear = get_near
    setFar = set_far
    getFar = get_far
    setNearFar = set_near_far
    getDefaultNear = get_default_near
    getDefaultFar = get_default_far
    setViewHpr = set_view_hpr
    getViewHpr = get_view_hpr
    setViewVector = set_view_vector
    getViewVector = get_view_vector
    getUpVector = get_up_vector
    getNodalPoint = get_nodal_point
    setInterocularDistance = set_interocular_distance
    getInterocularDistance = get_interocular_distance
    setConvergenceDistance = set_convergence_distance
    getConvergenceDistance = get_convergence_distance
    setViewMat = set_view_mat
    getViewMat = get_view_mat
    clearViewMat = clear_view_mat
    setKeystone = set_keystone
    getKeystone = get_keystone
    clearKeystone = clear_keystone
    setCustomFilmMat = set_custom_film_mat
    getCustomFilmMat = get_custom_film_mat
    clearCustomFilmMat = clear_custom_film_mat
    setFrustumFromCorners = set_frustum_from_corners
    recomputeAll = recompute_all
    isLinear = is_linear
    isPerspective = is_perspective
    isOrthographic = is_orthographic
    makeGeometry = make_geometry
    makeBounds = make_bounds
    getProjectionMat = get_projection_mat
    getProjectionMatInv = get_projection_mat_inv
    getFilmMat = get_film_mat
    getFilmMatInv = get_film_mat_inv
    getLensMat = get_lens_mat
    getLensMatInv = get_lens_mat_inv
    getLastChange = get_last_change

class Material(TypedWritableReferenceCount, Namable):
    """Defines the way an object appears in the presence of lighting.  A material
    is only necessary if lighting is to be enabled; otherwise, the material
    isn't used.

    There are two workflows that are supported: the "classic" workflow of
    providing separate ambient, diffuse and specular colors, and the
    "metalness" workflow, in which a base color is specified along with a
    "metallic" value that indicates whether the material is a metal or a
    dielectric.

    The size of the specular highlight can be specified by either specifying
    the specular exponent (shininess) or by specifying a roughness value that
    in perceptually linear in the range of 0-1.
    """

    base_color: LColor
    ambient: LColor
    diffuse: LColor
    specular: LColor
    emission: LColor
    shininess: float
    roughness: float
    metallic: float
    refractive_index: float
    local: bool
    twoside: bool
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: Material) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: Material) -> bool: ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def assign(self, copy: Self) -> Self: ...
    @staticmethod
    def get_default() -> Material:
        """Returns the default material."""
    def has_base_color(self) -> bool:
        """Returns true if the base color has been explicitly set for this material,
        false otherwise.
        """
    def get_base_color(self) -> LColor:
        """Returns the base_color color setting, if it has been set.  If neither the
        base color nor the metallic have been set, this returns the diffuse color.
        """
    def set_base_color(self, color: Vec4Like) -> None:
        """Specifies the base color of the material.  In conjunction with
        set_metallic, this is an alternate way to specify the color of a material.
        For dielectrics, this will determine the value of the diffuse color, and
        for metals, this will determine the value of the specular color.

        Setting this will clear an explicit specular, diffuse or ambient color
        assignment.

        If this is not set, the object color will be used.
        """
    def clear_base_color(self) -> None:
        """Removes the explicit base_color color from the material."""
    def has_ambient(self) -> bool:
        """Returns true if the ambient color has been explicitly set for this
        material, false otherwise.
        """
    def get_ambient(self) -> LColor:
        """Returns the ambient color setting, if it has been set.  Returns (0,0,0,0)
        if the ambient color has not been set.
        """
    def set_ambient(self, color: Vec4Like) -> None:
        """Specifies the ambient color setting of the material.  This will be the
        multiplied by any ambient lights in effect on the material to set its base
        color.

        This is the color of the object as it appears in the absence of direct
        light.

        If this is not set, the object color will be used.
        """
    def clear_ambient(self) -> None:
        """Removes the explicit ambient color from the material."""
    def has_diffuse(self) -> bool:
        """Returns true if the diffuse color has been explicitly set for this
        material, false otherwise.
        """
    def get_diffuse(self) -> LColor:
        """Returns the diffuse color setting, if it has been set.  Returns (1,1,1,1)
        if the diffuse color has not been set.
        """
    def set_diffuse(self, color: Vec4Like) -> None:
        """Specifies the diffuse color setting of the material.  This will be
        multiplied by any lights in effect on the material to get the color in the
        parts of the object illuminated by the lights.

        This is the primary color of an object; the color of the object as it
        appears in direct light, in the absence of highlights.

        If this is not set, the object color will be used.
        """
    def clear_diffuse(self) -> None:
        """Removes the explicit diffuse color from the material."""
    def has_specular(self) -> bool:
        """Returns true if the specular color has been explicitly set for this
        material, false otherwise.
        """
    def get_specular(self) -> LColor:
        """Returns the specular color setting, if it has been set.  Returns (0,0,0,0)
        if the specular color has not been set.
        """
    def set_specular(self, color: Vec4Like) -> None:
        """Specifies the specular color setting of the material.  This will be
        multiplied by any lights in effect on the material to compute the color of
        specular highlights on the object.

        This is the highlight color of an object: the color of small highlight
        reflections.

        If this is not set, the specular color is taken from the index of
        refraction, which is 1 by default (meaning no specular reflections are
        generated).
        """
    def clear_specular(self) -> None:
        """Removes the explicit specular color from the material."""
    def has_emission(self) -> bool:
        """Returns true if the emission color has been explicitly set for this
        material, false otherwise.
        """
    def get_emission(self) -> LColor:
        """Returns the emission color setting, if it has been set.  Returns (0,0,0,0)
        if the emission color has not been set.
        """
    def set_emission(self, color: Vec4Like) -> None:
        """Specifies the emission color setting of the material.  This is the color of
        the object as it appears in the absence of any light whatsover, including
        ambient light.  It is as if the object is glowing by this color (although
        of course it will not illuminate neighboring objects).

        If this is not set, the object will not glow by its own light and will only
        appear visible in the presence of one or more lights.
        """
    def clear_emission(self) -> None:
        """Removes the explicit emission color from the material."""
    def get_shininess(self) -> float:
        """Returns the shininess exponent of the material."""
    def set_shininess(self, shininess: float) -> None:
        """Sets the shininess exponent of the material.  This controls the size of the
        specular highlight spot.  In general, larger number produce a smaller
        specular highlight, which makes the object appear shinier.  Smaller numbers
        produce a larger highlight, which makes the object appear less shiny.

        This is usually in the range 0..128.

        Setting a shininess value removes any previous roughness assignment.
        """
    def has_roughness(self) -> bool:
        """Returns true if the roughness has been explicitly set for this material,
        false otherwise.
        """
    def get_roughness(self) -> float:
        """Returns the roughness previously specified by set_roughness.  If none was
        previously set, this value is computed from the shininess value.
        """
    def set_roughness(self, roughness: float) -> None:
        """Sets the roughness exponent of the material, where 0 is completely shiny
        (infinite shininess), and 1 is a completely dull object (0 shininess).
        This is a different, more perceptually intuitive way of controlling the
        size of the specular spot, and more commonly used in physically-based
        rendering.

        Setting a roughness recalculates the shininess value.
        """
    def has_metallic(self) -> bool:
        """Returns true if the metallic has been explicitly set for this material,
        false otherwise.
        """
    def get_metallic(self) -> float:
        """Returns the metallic setting, if it has been set.  Returns 0 if it has not
        been set.
        """
    def set_metallic(self, metallic: float) -> None:
        """Sets the metallic setting of the material, which is is used for physically-
        based rendering models.  This is usually 0 for dielectric materials and 1
        for metals.  It really does not make sense to set this to a value other
        than 0 or 1, but it is nonetheless a float for compatibility with tools
        that allow setting this to values other than 0 or 1.
        """
    def clear_metallic(self) -> None:
        """Removes the explicit metallic setting from the material."""
    def has_refractive_index(self) -> bool:
        """Returns true if a refractive index has explicitly been specified for this
        material.
        """
    def get_refractive_index(self) -> float:
        """Returns the index of refraction, or 1 if none has been set for this
        material.
        """
    def set_refractive_index(self, refractive_index: float) -> None:
        """Sets the index of refraction of the material, which is used to determine
        the specular color in absence of an explicit specular color assignment.
        This is usually 1.5 for dielectric materials.  It is not very useful for
        metals, since they cannot be described as easily with a single number.

        Should be 1 or higher.  The default is 1.
        """
    def get_local(self) -> bool:
        """Returns the local viewer flag.  Set set_local()."""
    def set_local(self, local: bool) -> None:
        """Sets the local viewer flag.  Set this true to enable camera-relative
        specular highlights, or false to use orthogonal specular highlights.  The
        default value is true.  Applications that use orthogonal projection should
        specify false.
        """
    def get_twoside(self) -> bool:
        """Returns the state of the two-sided lighting flag.  See set_twoside()."""
    def set_twoside(self, twoside: bool) -> None:
        """Set this true to enable two-sided lighting.  When two-sided lighting is on,
        both sides of a polygon will be lit by this material.  The default is for
        two-sided lighting to be off, in which case only the front surface is lit.
        """
    def compare_to(self, other: Material) -> int:
        """Returns a number less than zero if this material sorts before the other
        one, greater than zero if it sorts after, or zero if they are equivalent.
        The sorting order is arbitrary and largely meaningless, except to
        differentiate different materials.
        """
    def write(self, out: ostream, indent: int) -> None: ...
    def is_attrib_locked(self) -> bool:
        """@deprecated This no longer has any meaning in 1.10."""
    def set_attrib_lock(self) -> None:
        """@deprecated This no longer has any meaning in 1.10."""
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    getDefault = get_default
    hasBaseColor = has_base_color
    getBaseColor = get_base_color
    setBaseColor = set_base_color
    clearBaseColor = clear_base_color
    hasAmbient = has_ambient
    getAmbient = get_ambient
    setAmbient = set_ambient
    clearAmbient = clear_ambient
    hasDiffuse = has_diffuse
    getDiffuse = get_diffuse
    setDiffuse = set_diffuse
    clearDiffuse = clear_diffuse
    hasSpecular = has_specular
    getSpecular = get_specular
    setSpecular = set_specular
    clearSpecular = clear_specular
    hasEmission = has_emission
    getEmission = get_emission
    setEmission = set_emission
    clearEmission = clear_emission
    getShininess = get_shininess
    setShininess = set_shininess
    hasRoughness = has_roughness
    getRoughness = get_roughness
    setRoughness = set_roughness
    hasMetallic = has_metallic
    getMetallic = get_metallic
    setMetallic = set_metallic
    clearMetallic = clear_metallic
    hasRefractiveIndex = has_refractive_index
    getRefractiveIndex = get_refractive_index
    setRefractiveIndex = set_refractive_index
    getLocal = get_local
    setLocal = set_local
    getTwoside = get_twoside
    setTwoside = set_twoside
    compareTo = compare_to
    isAttribLocked = is_attrib_locked
    setAttribLock = set_attrib_lock

class MaterialPool:
    """The MaterialPool (there is only one in the universe) serves to unify
    different pointers to the same Material, so we do not (a) waste memory with
    many different Material objects that are all equivalent, and (b) waste time
    switching the graphics engine between different Material states that are
    really the same thing.

    The idea is to create a temporary Material representing the lighting state
    you want to apply, then call get_material(), passing in your temporary
    Material.  The return value will either be a new Material object, or it may
    be the the same object you supplied; in either case, it will have the same
    value.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_material(temp: Material) -> Material:
        """Returns a Material pointer that represents the same material described by
        temp, except that it is a shared pointer.

        Each call to get_material() passing an equivalent Material pointer will
        return the same shared pointer.

        If you modify the shared pointer, it will automatically disassociate it
        from the pool.

        Also, the return value may be a different pointer than that passed in, or
        it may be the same pointer.  In either case, the passed in pointer has now
        been sacrificed to the greater good and should not be used again (like any
        other PointerTo, it will be freed when the last reference count is
        removed).
        """
    @staticmethod
    def release_material(temp: Material) -> None:
        """Removes the indicated material from the pool."""
    @staticmethod
    def release_all_materials() -> None:
        """Releases all materials in the pool and restores the pool to the empty
        state.
        """
    @staticmethod
    def garbage_collect() -> int:
        """Releases only those materials in the pool that have a reference count of
        exactly 1; i.e.  only those materials that are not being used outside of
        the pool.  Returns the number of materials released.
        """
    @staticmethod
    def list_contents(out: ostream) -> None:
        """Lists the contents of the material pool to the indicated output stream."""
    @staticmethod
    def write(out: ostream) -> None:
        """Lists the contents of the material pool to the indicated output stream."""
    getMaterial = get_material
    releaseMaterial = release_material
    releaseAllMaterials = release_all_materials
    garbageCollect = garbage_collect
    listContents = list_contents

class MatrixLens(Lens):
    """A completely generic linear lens.  This is provided for the benefit of low-
    level code that wants to specify a perspective or orthographic frustum via
    an explicit projection matrix, but not mess around with fov's or focal
    lengths or any of that nonsense.
    """

    user_mat: LMatrix4
    def __init__(self) -> None: ...
    def set_user_mat(self, user_mat: Mat4Like) -> None:
        """Explicitly specifies the projection matrix.  This matrix should convert X
        and Y to the range [-film_size/2, film_size/2], where (-fs/2,-fs/2) is the
        lower left corner of the screen and (fs/2, fs/2) is the upper right.  Z
        should go to the range [-1, 1], where -1 is the near plane and 1 is the far
        plane.  Note that this is a left-handed Y-up coordinate system.

        The default film_size for a MatrixLens is 2, so the default range is [-1,
        1] for both X and Y.  This is consistent with the GL conventions for
        projection matrices.
        """
    def get_user_mat(self) -> LMatrix4:
        """Returns the explicit projection matrix as set by the user.  This does not
        include transforms on the lens or film (e.g.  a film offset or view hpr).
        """
    def set_left_eye_mat(self, user_mat: Mat4Like) -> None:
        """Sets a custom projection matrix for the left eye.  This is only used if the
        lens is attached to a stereo camera, in which case the left eye matrix will
        be used to draw the scene in the left eye (but the center matrix--the
        user_mat--will still be used to cull the scene).

        This matrix should not be too different from the center matrix (set by
        set_user_mat()) or culling errors may become obvious.
        """
    def clear_left_eye_mat(self) -> None:
        """Removes the custom projection matrix set for the left eye, and uses the
        center matrix (set by set_user_mat) instead.
        """
    def has_left_eye_mat(self) -> bool:
        """Returns true if the camera has a custom projection matrix set for the left
        eye, or false if the center matrix (set by set_user_mat) will be used for
        the left eye.
        """
    def get_left_eye_mat(self) -> LMatrix4:
        """Returns the custom projection matrix for the left eye, if any, or the
        center matrix if there is no custom matrix set for the left eye.
        """
    def set_right_eye_mat(self, user_mat: Mat4Like) -> None:
        """Sets a custom projection matrix for the right eye.  This is only used if
        the lens is attached to a stereo camera, in which case the right eye matrix
        will be used to draw the scene in the right eye (but the center matrix--the
        user_mat--will still be used to cull the scene).

        This matrix should not be too different from the center matrix (set by
        set_user_mat()) or culling errors may become obvious.
        """
    def clear_right_eye_mat(self) -> None:
        """Removes the custom projection matrix set for the right eye, and uses the
        center matrix (set by set_user_mat) instead.
        """
    def has_right_eye_mat(self) -> bool:
        """Returns true if the camera has a custom projection matrix set for the right
        eye, or false if the center matrix (set by set_user_mat) will be used for
        the right eye.
        """
    def get_right_eye_mat(self) -> LMatrix4:
        """Returns the custom projection matrix for the right eye, if any, or the
        center matrix if there is no custom matrix set for the right eye.
        """
    setUserMat = set_user_mat
    getUserMat = get_user_mat
    setLeftEyeMat = set_left_eye_mat
    clearLeftEyeMat = clear_left_eye_mat
    hasLeftEyeMat = has_left_eye_mat
    getLeftEyeMat = get_left_eye_mat
    setRightEyeMat = set_right_eye_mat
    clearRightEyeMat = clear_right_eye_mat
    hasRightEyeMat = has_right_eye_mat
    getRightEyeMat = get_right_eye_mat

class OrthographicLens(Lens):
    """An orthographic lens.  Although this kind of lens is linear, like a
    PerspectiveLens, it doesn't respect field-of-view or focal length
    parameters, and adjusting these will have no effect.  Instead, its field of
    view is controlled by adjusting the film_size; the orthographic lens
    represents a planar projection onto its imaginary film of the specified
    size, hanging in space.
    """

    def __init__(self) -> None: ...

class ParamTextureSampler(ParamValueBase):
    """A class object for storing a pointer to a Texture along with a sampler
    state that indicates how to to sample the given texture.
    """

    @property
    def texture(self) -> Texture: ...
    @property
    def sampler(self) -> SamplerState: ...
    def __init__(self, tex: Texture, sampler: SamplerState) -> None:
        """Creates a new ParamTextureSampler storing the given texture and sampler
        objects.
        """
    def get_texture(self) -> Texture:
        """Retrieves the texture stored in the parameter."""
    def get_sampler(self) -> SamplerState:
        """Retrieves the sampler state stored in the parameter."""
    getTexture = get_texture
    getSampler = get_sampler

class ParamTextureImage(ParamValueBase):
    """A class object for storing a pointer to a Texture along with a set of
    properties that indicates which image to bind to a shader input.

    This class is useful for binding texture images to a shader, which is a
    fairly esoteric feature.
    """

    @property
    def texture(self) -> Texture: ...
    @property
    def read_access(self) -> bool: ...
    @property
    def write_access(self) -> bool: ...
    @property
    def bind_level(self) -> int: ...
    @property
    def bind_layer(self) -> int: ...
    def __init__(self, tex: Texture, read: bool, write: bool, z: int = ..., n: int = ...) -> None:
        """Creates a new ParamTextureImage storing the given texture and image binding
        parameters.
        """
    def get_texture(self) -> Texture:
        """Retrieves the texture stored in the parameter."""
    def has_read_access(self) -> bool:
        """Returns true if this image should be bound with read access enabled."""
    def has_write_access(self) -> bool:
        """Returns true if this image should be bound with write access enabled."""
    def get_bind_layered(self) -> bool:
        """Returns true if all layers of this image should be bound simultaneously."""
    def get_bind_level(self) -> int:
        """Returns the image level that should be bound."""
    def get_bind_layer(self) -> int:
        """Returns the image layer that should be bound.  This is undefined if
        get_bind_layered() returns false.
        """
    getTexture = get_texture
    hasReadAccess = has_read_access
    hasWriteAccess = has_write_access
    getBindLayered = get_bind_layered
    getBindLevel = get_bind_level
    getBindLayer = get_bind_layer

class PerspectiveLens(Lens):
    """A perspective-type lens: a normal camera."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, hfov: float, vfov: float) -> None: ...

class TextureReloadRequest(AsyncTask):
    """This loader request will call Texture::get_ram_image() in a sub-thread, to
    force the texture's image to be re-read from disk.  It is used by
    GraphicsStateGuardian::async_reload_texture(), when get_incomplete_render()
    is true.
    """

    @property
    def texture(self) -> Texture: ...
    @overload
    def __init__(self, __param0: TextureReloadRequest) -> None:
        """Create a new TextureReloadRequest, and add it to the loader via
        load_async(), to begin an asynchronous load.
        """
    @overload
    def __init__(self, name: str, pgo: PreparedGraphicsObjects, texture: Texture, allow_compressed: bool) -> None: ...
    def get_prepared_graphics_objects(self) -> PreparedGraphicsObjects:
        """Returns the PreparedGraphicsObjects object associated with this
        asynchronous TextureReloadRequest.
        """
    def get_texture(self) -> Texture:
        """Returns the Texture object associated with this asynchronous
        TextureReloadRequest.
        """
    def get_allow_compressed(self) -> bool:
        """Returns the "allow compressed" flag associated with this asynchronous
        TextureReloadRequest.
        """
    def is_ready(self) -> bool:
        """Returns true if this request has completed, false if it is still pending.
        Equivalent to `req.done() and not req.cancelled()`.
        @see done()
        """
    getPreparedGraphicsObjects = get_prepared_graphics_objects
    getTexture = get_texture
    getAllowCompressed = get_allow_compressed
    isReady = is_ready

class TextureContext(BufferContext, AdaptiveLruPage):
    """This is a special class object that holds all the information returned by a
    particular GSG to indicate the texture's internal context identifier.

    Textures typically have an immediate-mode and a retained-mode operation.
    When using textures in retained-mode (in response to Texture::prepare()),
    the GSG will create some internal handle for the texture and store it here.
    The texture stores all of these handles internally.
    """

    def upcast_to_BufferContext(self) -> BufferContext: ...
    def upcast_to_AdaptiveLruPage(self) -> AdaptiveLruPage: ...
    def get_texture(self) -> Texture:
        """Returns the pointer to the associated Texture object."""
    def get_view(self) -> int:
        """Returns the specific view of a multiview texture this context represents.
        In the usual case, with a non-multiview texture, this will be 0.
        """
    def get_native_id(self) -> int:
        """Returns an implementation-defined handle or pointer that can be used
        to interface directly with the underlying API.
        Returns 0 if the underlying implementation does not support this.
        """
    def get_native_buffer_id(self) -> int:
        """Similar to get_native_id, but some implementations use a separate
        identifier for the buffer object associated with buffer textures.
        Returns 0 if the underlying implementation does not support this, or
        if this is not a buffer texture.
        """
    def was_modified(self) -> bool:
        """Returns true if the texture properties or image have been modified since
        the last time mark_loaded() was called.
        """
    def was_properties_modified(self) -> bool:
        """Returns true if the texture properties (unrelated to the image) have been
        modified since the last time mark_loaded() was called.
        """
    def was_image_modified(self) -> bool:
        """Returns true if the texture image has been modified since the last time
        mark_loaded() was called.
        """
    def was_simple_image_modified(self) -> bool:
        """Returns true if the texture's "simple" image has been modified since the
        last time mark_simple_loaded() was called.
        """
    def get_properties_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the texture properties (unrelated to the image) are modified.
        """
    def get_image_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the texture image data (including mipmap levels) are modified.
        """
    def get_simple_image_modified(self) -> UpdateSeq:
        """Returns a sequence number which is guaranteed to change at least every time
        the texture's "simple" image data is modified.
        """
    upcastToBufferContext = upcast_to_BufferContext
    upcastToAdaptiveLruPage = upcast_to_AdaptiveLruPage
    getTexture = get_texture
    getView = get_view
    getNativeId = get_native_id
    getNativeBufferId = get_native_buffer_id
    wasModified = was_modified
    wasPropertiesModified = was_properties_modified
    wasImageModified = was_image_modified
    wasSimpleImageModified = was_simple_image_modified
    getPropertiesModified = get_properties_modified
    getImageModified = get_image_modified
    getSimpleImageModified = get_simple_image_modified

class ShaderContext(SavedContext):
    @property
    def shader(self) -> Shader: ...
    def get_shader(self) -> Shader: ...
    getShader = get_shader

class UserVertexSlider(VertexSlider):
    """This is a specialization on VertexSlider that allows the user to specify
    any arbitrary slider valie he likes.  This is rarely used except for
    testing.
    """

    def __init__(self, name: InternalName | str) -> None: ...
    def set_slider(self, slider: float) -> None:
        """Stores the indicated slider value."""
    setSlider = set_slider

class UserVertexTransform(VertexTransform):
    """This is a specialization on VertexTransform that allows the user to specify
    any arbitrary transform matrix he likes.  This is rarely used except for
    testing.
    """

    def __init__(self, name: str) -> None: ...
    def get_name(self) -> str:
        """Returns the name passed to the constructor.  Completely arbitrary."""
    def set_matrix(self, matrix: Mat4Like) -> None:
        """Stores the indicated matrix."""
    getName = get_name
    setMatrix = set_matrix

class VideoTexture(Texture, AnimInterface):
    """The base class for a family of animated Textures that take their input from
    a video source, such as a movie file.  These Textures may be stopped,
    started, etc.  using the AnimInterface controls, similar to an animated
    character.
    """

    @property
    def video_width(self) -> int: ...
    @property
    def video_height(self) -> int: ...
    def upcast_to_Texture(self) -> Texture: ...
    def upcast_to_AnimInterface(self) -> AnimInterface: ...
    def get_video_width(self) -> int:
        """Returns the width in texels of the source video stream.  This is not
        necessarily the width of the actual texture, since the texture may have
        been expanded to raise it to a power of 2.
        """
    def get_video_height(self) -> int:
        """Returns the height in texels of the source video stream.  This is not
        necessarily the height of the actual texture, since the texture may have
        been expanded to raise it to a power of 2.
        """
    upcastToTexture = upcast_to_Texture
    upcastToAnimInterface = upcast_to_AnimInterface
    getVideoWidth = get_video_width
    getVideoHeight = get_video_height

class VertexBufferContext(BufferContext, AdaptiveLruPage):
    """This is a special class object that holds all the information returned by a
    particular GSG to indicate the vertex data array's internal context
    identifier.

    This allows the GSG to cache the vertex data array in whatever way makes
    sense.  For instance, DirectX can allocate a vertex buffer for the array.
    OpenGL can create a buffer object.
    """

    def upcast_to_BufferContext(self) -> BufferContext: ...
    def upcast_to_AdaptiveLruPage(self) -> AdaptiveLruPage: ...
    def get_data(self) -> GeomVertexArrayData:
        """Returns the pointer to the client-side array data object."""
    def changed_size(self, reader: GeomVertexArrayDataHandle) -> bool:
        """Returns true if the data has changed size since the last time mark_loaded()
        was called.
        """
    def changed_usage_hint(self, reader: GeomVertexArrayDataHandle) -> bool:
        """Returns true if the data has changed its usage hint since the last time
        mark_loaded() was called.
        """
    def was_modified(self, reader: GeomVertexArrayDataHandle) -> bool:
        """Returns true if the data has been modified since the last time
        mark_loaded() was called.
        """
    upcastToBufferContext = upcast_to_BufferContext
    upcastToAdaptiveLruPage = upcast_to_AdaptiveLruPage
    getData = get_data
    changedSize = changed_size
    changedUsageHint = changed_usage_hint
    wasModified = was_modified

class TextureCollection:
    """Manages a list of Texture objects, as returned by
    TexturePool::find_all_textures().
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: TextureCollection = ...) -> None: ...
    @overload
    def __init__(self, sequence) -> None: ...
    def __getitem__(self, index: int) -> Texture:
        """Returns the nth Texture in the collection.  This is the same as
        get_texture(), but it may be a more convenient way to access it.
        """
    def __len__(self) -> int:
        """Returns the number of textures in the collection.  This is the same thing
        as get_num_textures().
        """
    def __iadd__(self, other: TextureCollection) -> Self: ...
    def __add__(self, other: TextureCollection) -> TextureCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[Texture]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def add_texture(self, texture: Texture) -> None:
        """Adds a new Texture to the collection."""
    def remove_texture(self, texture: Texture) -> bool:
        """Removes the indicated Texture from the collection.  Returns true if the
        texture was removed, false if it was not a member of the collection.
        """
    def add_textures_from(self, other: TextureCollection) -> None:
        """Adds all the Textures indicated in the other collection to this texture.
        The other textures are simply appended to the end of the textures in this
        list; duplicates are not automatically removed.
        """
    def remove_textures_from(self, other: TextureCollection) -> None:
        """Removes from this collection all of the Textures listed in the other
        collection.
        """
    def remove_duplicate_textures(self) -> None:
        """Removes any duplicate entries of the same Textures on this collection.  If
        a Texture appears multiple times, the first appearance is retained;
        subsequent appearances are removed.
        """
    def has_texture(self, texture: Texture) -> bool:
        """Returns true if the indicated Texture appears in this collection, false
        otherwise.
        """
    def clear(self) -> None:
        """Removes all Textures from the collection."""
    def reserve(self, num: int) -> None:
        """This is a hint to Panda to allocate enough memory to hold the given number
        of NodePaths, if you know ahead of time how many you will be adding.
        """
    def find_texture(self, name: str) -> Texture:
        """Returns the texture in the collection with the indicated name, if any, or
        NULL if no texture has that name.
        """
    def get_num_textures(self) -> int:
        """Returns the number of Textures in the collection."""
    def get_texture(self, index: int) -> Texture:
        """Returns the nth Texture in the collection."""
    def append(self, texture: Texture) -> None:
        """Adds a new Texture to the collection.  This method duplicates the
        add_texture() method; it is provided to satisfy Python's naming convention.
        """
    def extend(self, other: TextureCollection) -> None:
        """Appends the other list onto the end of this one.  This method duplicates
        the += operator; it is provided to satisfy Python's naming convention.
        """
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the TextureCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the TextureCollection to the
        indicated output stream.
        """
    def get_textures(self) -> tuple[Texture, ...]: ...
    addTexture = add_texture
    removeTexture = remove_texture
    addTexturesFrom = add_textures_from
    removeTexturesFrom = remove_textures_from
    removeDuplicateTextures = remove_duplicate_textures
    hasTexture = has_texture
    findTexture = find_texture
    getNumTextures = get_num_textures
    getTexture = get_texture
    getTextures = get_textures

class TexturePool:
    """This is the preferred interface for loading textures from image files.  It
    unifies all references to the same filename, so that multiple models that
    reference the same textures don't waste texture memory unnecessarily.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def has_texture(filename: StrOrBytesPath) -> bool:
        """Returns true if the texture has ever been loaded, false otherwise."""
    @staticmethod
    def verify_texture(filename: StrOrBytesPath) -> bool:
        """Loads the given filename up into a texture, if it has not already been
        loaded, and returns true to indicate success, or false to indicate failure.
        If this returns true, it is guaranteed that a subsequent call to
        load_texture() with the same texture name will return a valid Texture
        pointer.
        """
    @overload
    @staticmethod
    def get_texture(filename: StrOrBytesPath, primary_file_num_channels: int = ..., read_mipmaps: bool = ...) -> Texture:
        """Returns the texture that has already been previously loaded, or NULL
        otherwise.
        """
    @overload
    @staticmethod
    def get_texture(
        filename: StrOrBytesPath,
        alpha_filename: StrOrBytesPath,
        primary_file_num_channels: int = ...,
        alpha_file_channel: int = ...,
        read_mipmaps: bool = ...,
    ) -> Texture: ...
    @overload
    @staticmethod
    def load_texture(
        filename: StrOrBytesPath, primary_file_num_channels: int = ..., read_mipmaps: bool = ..., options: LoaderOptions = ...
    ) -> Texture:
        """`(filename: Filename, alpha_filename: Filename, primary_file_num_channels: int = ..., alpha_file_channel: int = ..., read_mipmaps: bool = ..., options: LoaderOptions = ...)`:
        Loads the given filename up into a texture, if it has not already been
        loaded, and returns the new texture.  If a texture with the same filename
        was previously loaded, returns that one instead.  If the texture file
        cannot be found, returns NULL.

        If read_mipmaps is true, both filenames should contain a hash mark ('#'),
        which will be filled in with the mipmap level number; and the texture will
        be defined with a series of images, two for each mipmap level.

        `(filename: Filename, primary_file_num_channels: int = ..., read_mipmaps: bool = ..., options: LoaderOptions = ...)`:
        Loads the given filename up into a texture, if it has not already been
        loaded, and returns the new texture.  If a texture with the same filename
        was previously loaded, returns that one instead.  If the texture file
        cannot be found, returns NULL.

        If read_mipmaps is true, the filename should contain a hash mark ('#'),
        which will be filled in with the mipmap level number; and the texture will
        be defined with a series of images, one for each mipmap level.
        """
    @overload
    @staticmethod
    def load_texture(
        filename: StrOrBytesPath,
        alpha_filename: StrOrBytesPath,
        primary_file_num_channels: int = ...,
        alpha_file_channel: int = ...,
        read_mipmaps: bool = ...,
        options: LoaderOptions = ...,
    ) -> Texture: ...
    @staticmethod
    def load_3d_texture(filename_pattern: StrOrBytesPath, read_mipmaps: bool = ..., options: LoaderOptions = ...) -> Texture:
        """Loads a 3-D texture that is specified with a series of n pages, all
        numbered in sequence, and beginning with index 0.  The filename should
        include a sequence of one or more hash characters ("#") which will be
        filled in with the index number of each level.

        If read_mipmaps is true, the filename should contain an additional hash
        mark.  The first hash mark will be filled in with the mipmap level number,
        and the second with the index number of each 3-d level.
        """
    @staticmethod
    def load_2d_texture_array(
        filename_pattern: StrOrBytesPath, read_mipmaps: bool = ..., options: LoaderOptions = ...
    ) -> Texture:
        """Loads a 2-D texture array that is specified with a series of n pages, all
        numbered in sequence, and beginning with index 0.  The filename should
        include a sequence of one or more hash characters ("#") which will be
        filled in with the index number of each level.

        If read_mipmaps is true, the filename should contain an additional hash
        mark.  The first hash mark will be filled in with the mipmap level number,
        and the second with the index number of each 2-d level.
        """
    @staticmethod
    def load_cube_map(filename_pattern: StrOrBytesPath, read_mipmaps: bool = ..., options: LoaderOptions = ...) -> Texture:
        """Loads a cube map texture that is specified with a series of 6 pages,
        numbered 0 through 5.  The filename should include a sequence of one or
        more hash characters ("#") which will be filled in with the index number of
        each pagee.

        If read_mipmaps is true, the filename should contain an additional hash
        mark.  The first hash mark will be filled in with the mipmap level number,
        and the second with the face number, 0 through 5.
        """
    @staticmethod
    def get_normalization_cube_map(size: int) -> Texture:
        """Returns a standard Texture object that has been created with
        Texture::generate_normalization_cube_map().  This Texture may be shared by
        any application code requiring a normalization cube map.  It will be at
        least as large as the specified size, though it may be larger.
        """
    @staticmethod
    def get_alpha_scale_map() -> Texture:
        """Returns a standard Texture object that has been created with
        Texture::generate_alpha_scale_map().

        This Texture object is used internally by Panda to apply an alpha scale to
        an object (instead of munging its vertices) when
        gsg->get_alpha_scale_via_texture() returns true.
        """
    @staticmethod
    def add_texture(texture: Texture) -> None:
        """Adds the indicated already-loaded texture to the pool.  The texture must
        have a filename set for its name.  The texture will always replace any
        previously-loaded texture in the pool that had the same filename.
        """
    @staticmethod
    def release_texture(texture: Texture) -> None:
        """Removes the indicated texture from the pool, indicating it will never be
        loaded again; the texture may then be freed.  If this function is never
        called, a reference count will be maintained on every texture every loaded,
        and textures will never be freed.

        The texture's name should not have been changed during its lifetime, or
        this function may fail to locate it in the pool.
        """
    @staticmethod
    def release_all_textures() -> None:
        """Releases all textures in the pool and restores the pool to the empty state."""
    @staticmethod
    def rehash() -> None:
        """Should be called when the model-path changes, to blow away the cache of
        texture pathnames found along the model-path.
        """
    @staticmethod
    def garbage_collect() -> int:
        """Releases only those textures in the pool that have a reference count of
        exactly 1; i.e.  only those textures that are not being used outside of the
        pool.  Returns the number of textures released.
        """
    @staticmethod
    def list_contents(out: ostream = ...) -> None:
        """`()`:
        Lists the contents of the texture pool to cout

        `(out: ostream)`:
        Lists the contents of the texture pool to the indicated output stream.
        """
    @staticmethod
    def find_texture(name: str) -> Texture:
        """Returns the first texture found in the pool that matches the indicated name
        (which may contain wildcards).  Returns the texture if it is found, or NULL
        if it is not.
        """
    @staticmethod
    def find_all_textures(name: str = ...) -> TextureCollection:
        """Returns the set of all textures found in the pool that match the indicated
        name (which may contain wildcards).
        """
    @staticmethod
    def set_fake_texture_image(filename: StrOrBytesPath) -> None:
        """Sets a bogus filename that will be loaded in lieu of any textures requested
        from this point on.
        """
    @staticmethod
    def clear_fake_texture_image() -> None:
        """Restores normal behavior of loading the textures actually requested."""
    @staticmethod
    def has_fake_texture_image() -> bool:
        """Returns true if fake_texture_image mode has been enabled, false if we are
        in the normal mode.
        """
    @staticmethod
    def get_fake_texture_image() -> Filename:
        """Returns the filename that was specified with a previous call to
        set_fake_texture_image().
        """
    @staticmethod
    def make_texture(extension: str) -> Texture:
        """Creates a new Texture object of the appropriate type for the indicated
        filename extension, according to the types that have been registered via
        register_texture_type().
        """
    @staticmethod
    def write(out: ostream) -> None:
        """Lists the contents of the texture pool to the indicated output stream.  For
        debugging.
        """
    hasTexture = has_texture
    verifyTexture = verify_texture
    getTexture = get_texture
    loadTexture = load_texture
    load3dTexture = load_3d_texture
    load2dTextureArray = load_2d_texture_array
    loadCubeMap = load_cube_map
    getNormalizationCubeMap = get_normalization_cube_map
    getAlphaScaleMap = get_alpha_scale_map
    addTexture = add_texture
    releaseTexture = release_texture
    releaseAllTextures = release_all_textures
    garbageCollect = garbage_collect
    listContents = list_contents
    findTexture = find_texture
    findAllTextures = find_all_textures
    setFakeTextureImage = set_fake_texture_image
    clearFakeTextureImage = clear_fake_texture_image
    hasFakeTextureImage = has_fake_texture_image
    getFakeTextureImage = get_fake_texture_image
    makeTexture = make_texture

class TexturePeeker(ReferenceCount):
    """An instance of this object is returned by Texture::peek().  This object
    allows quick and easy inspection of a texture's texels by (u, v)
    coordinates.
    """

    def __init__(self, __param0: TexturePeeker) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_x_size(self) -> int:
        """Returns the width of the texture image that is contributing to the
        TexturePeeker's information.  This may be either the Texture's full width,
        or its simple ram image's width.
        """
    def get_y_size(self) -> int:
        """Returns the height of the texture image that is contributing to the
        TexturePeeker's information.  This may be either the Texture's full height,
        or its simple ram image's height.
        """
    def get_z_size(self) -> int:
        """Returns the depth of the texture image that is contributing to the
        TexturePeeker's information.
        """
    def has_pixel(self, x: int, y: int, z: int = ...) -> bool:
        """Returns whether a given coordinate is inside of the texture dimensions."""
    def lookup(self, color: Vec4Like, u: float, v: float, w: float = ...) -> None:
        """`(self, color: LColor, u: float, v: float)`:
        Fills "color" with the RGBA color of the texel at point (u, v).

        The texel color is determined via nearest-point sampling (no filtering of
        adjacent pixels), regardless of the filter type associated with the
        texture.  u, v, and w will wrap around regardless of the texture's wrap
        mode.

        `(self, color: LColor, u: float, v: float, w: float)`:
        Fills "color" with the RGBA color of the texel at point (u, v, w).

        The texel color is determined via nearest-point sampling (no filtering of
        adjacent pixels), regardless of the filter type associated with the
        texture.  u, v, and w will wrap around regardless of the texture's wrap
        mode.
        """
    def fetch_pixel(self, color: Vec4Like, x: int, y: int, z: int = ...) -> None:
        """Works like TexturePeeker::lookup(), but instead of uv-coordinates, integer
        coordinates are used.
        """
    def lookup_bilinear(self, color: Vec4Like, u: float, v: float) -> bool:
        """Performs a bilinear lookup to retrieve the color value stored at the uv
        coordinate (u, v).

        In case the point is outside of the uv range, color is set to zero,
        and false is returned.  Otherwise true is returned.
        """
    @overload
    def filter_rect(self, color: Vec4Like, min_u: float, min_v: float, max_u: float, max_v: float) -> None:
        """Fills "color" with the average RGBA color of the texels within the
        rectangle defined by the specified coordinate range.

        The texel color is linearly filtered over the entire region.  u, v, and w
        must be in the range [0, 1].
        """
    @overload
    def filter_rect(
        self, color: Vec4Like, min_u: float, min_v: float, min_w: float, max_u: float, max_v: float, max_w: float
    ) -> None: ...
    getXSize = get_x_size
    getYSize = get_y_size
    getZSize = get_z_size
    hasPixel = has_pixel
    fetchPixel = fetch_pixel
    lookupBilinear = lookup_bilinear
    filterRect = filter_rect

class TextureStagePool:
    """The TextureStagePool (there is only one in the universe) serves to unify
    different pointers to the same TextureStage, mainly to help developers use
    a common pointer to access things that are loaded from different model
    files.

    It runs in one of three different modes, according to set_mode().  See that
    method for more information.
    """

    M_none: Final = 0
    MNone: Final = 0
    M_name: Final = 1
    MName: Final = 1
    M_unique: Final = 2
    MUnique: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    mode: _TextureStagePool_Mode
    @staticmethod
    def get_stage(temp: TextureStage) -> TextureStage:
        """Returns a TextureStage pointer that represents the same TextureStage
        described by temp, except that it is a shared pointer.

        Each call to get_stage() passing an equivalent TextureStage pointer will
        return the same shared pointer.

        If you modify the shared pointer, it will automatically disassociate it
        from the pool.

        Also, the return value may be a different pointer than that passed in, or
        it may be the same pointer.  In either case, the passed in pointer has now
        been sacrificed to the greater good and should not be used again (like any
        other PointerTo, it will be freed when the last reference count is
        removed).
        """
    @staticmethod
    def release_stage(temp: TextureStage) -> None:
        """Removes the indicated TextureStage from the pool."""
    @staticmethod
    def release_all_stages() -> None:
        """Releases all TextureStages in the pool and restores the pool to the empty
        state.
        """
    @staticmethod
    def set_mode(mode: _TextureStagePool_Mode) -> None:
        """Specifies the fundamental operating mode of the TextureStagePool.

        If this is M_none, each call to get_stage() returns the same TextureStage
        pointer that was passed in (the pool is effectively disabled).  If this is
        M_name, each call to get_stage() returns the last TextureStage passed in
        with the same name, whether it has different properties or not.  If this is
        M_unique, then each call to get_stage() returns only TextureStages with
        identical properties.
        """
    @staticmethod
    def get_mode() -> _TextureStagePool_Mode:
        """Returns the fundamental operating mode of the TextureStagePool.  See
        set_mode().
        """
    @staticmethod
    def garbage_collect() -> int:
        """Releases only those TextureStages in the pool that have a reference count
        of exactly 1; i.e.  only those TextureStages that are not being used
        outside of the pool.  Returns the number of TextureStages released.
        """
    @staticmethod
    def list_contents(out: ostream) -> None:
        """Lists the contents of the TextureStage pool to the indicated output stream."""
    @staticmethod
    def write(out: ostream) -> None:
        """Lists the contents of the TextureStage pool to the indicated output stream."""
    getStage = get_stage
    releaseStage = release_stage
    releaseAllStages = release_all_stages
    setMode = set_mode
    getMode = get_mode
    garbageCollect = garbage_collect
    listContents = list_contents
