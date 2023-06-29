from _typeshed import StrOrBytesPath
from collections.abc import Iterator, Mapping, MutableMapping, MutableSequence, Sequence
from typing import Any, ClassVar, Generic, TypeVar, overload
from typing_extensions import Final, Literal, Never, Self, TypeAlias, final

from panda3d._typing import Mat4Like, Vec2Like, Vec3Like, Vec4Like
from panda3d.core._display import DisplayRegion
from panda3d.core._dtoolbase import TypedObject, TypeHandle
from panda3d.core._dtoolutil import Filename, istream, ostream
from panda3d.core._event import AsyncTask, AsyncTaskManager
from panda3d.core._express import Namable, ReferenceCount, TypedReferenceCount
from panda3d.core._gobj import (
    Geom,
    InternalName,
    Lens,
    Material,
    SamplerState,
    Shader,
    ShaderBuffer,
    Texture,
    TextureCollection,
    TextureStage,
)
from panda3d.core._gsgbase import GraphicsStateGuardianBase
from panda3d.core._linmath import (
    LColor,
    LMatrix3,
    LMatrix4,
    LPoint3,
    LPoint3f,
    LQuaternion,
    LTexCoord3,
    LVecBase2,
    LVecBase3,
    LVecBase4,
    LVector3,
)
from panda3d.core._mathutil import BoundingVolume, GeometricBoundingVolume, LPlane
from panda3d.core._pipeline import Thread
from panda3d.core._putil import (
    BamEnums,
    BamReader,
    BamWriter,
    BitMask32,
    CallbackData,
    CollideMask,
    DrawMask,
    LoaderOptions,
    NodeCachedReferenceCount,
    ParamValueBase,
    PortalMask,
    TypedWritable,
    TypedWritableReferenceCount,
    UpdateSeq,
)

_N = TypeVar('_N', bound=PandaNode, default=PandaNode, covariant=True)
_M = TypeVar('_M', bound=PandaNode, default=PandaNode)
_RenderModeAttrib_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_RenderAttrib_PandaCompareFunc: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_BoundingVolume_BoundsType: TypeAlias = Literal[0, 1, 2, 3, 4]
_TransparencyAttrib_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_LogicOpAttrib_Operation: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_NodePath_ErrorType: TypeAlias = Literal[0, 1, 2, 3]
_RenderAttrib_TexGenMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
_BamEnums_BamEndian: TypeAlias = Literal[0, 1, 1]
_ClipPlaneAttrib_Operation: TypeAlias = Literal[0, 1, 2]
_ColorAttrib_Type: TypeAlias = Literal[0, 1, 2]
_ColorBlendAttrib_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_ColorBlendAttrib_Operand: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
_CullBinEnums_BinType: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_CullFaceAttrib_Mode: TypeAlias = Literal[0, 1, 2, 3]
_Fog_Mode: TypeAlias = Literal[0, 1, 2]
_RescaleNormalAttrib_Mode: TypeAlias = Literal[0, 1, 2, 3]
_DepthWriteAttrib_Mode: TypeAlias = Literal[0, 1]
_LightAttrib_Operation: TypeAlias = Literal[0, 1, 2]
_LightRampAttrib_LightRampMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_ModelNode_PreserveTransform: TypeAlias = Literal[0, 1, 2, 3, 4]
_PolylightNode_Attenuation_Type: TypeAlias = Literal[0, 1]
_PolylightNode_Flicker_Type: TypeAlias = Literal[0, 1, 2]
_PolylightEffect_ContribType: TypeAlias = Literal[0, 1]
_ShadeModelAttrib_Mode: TypeAlias = Literal[0, 1]
_StencilAttrib_StencilOperation: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_StencilAttrib_StencilRenderState: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

@final
class TransformState(NodeCachedReferenceCount):
    """Indicates a coordinate-system transform on vertices.  TransformStates are
    the primary means for storing transformations on the scene graph.

    Transforms may be specified in one of two ways: componentwise, with a pos-
    hpr-scale, or with an arbitrary transform matrix.  If you specify a
    transform componentwise, it will remember its original components.

    TransformState objects are managed very much like RenderState objects.
    They are immutable and reference-counted automatically.

    You should not attempt to create or modify a TransformState object
    directly.  Instead, call one of the make() functions to create one for you.
    And instead of modifying a TransformState object, create a new one.
    """

    @property
    def pos(self) -> LPoint3: ...
    @property
    def hpr(self) -> LVecBase3: ...
    @property
    def quat(self) -> LQuaternion: ...
    @property
    def norm_quat(self) -> LQuaternion: ...
    @property
    def scale(self) -> LVecBase3: ...
    @property
    def shear(self) -> LVecBase3: ...
    @property
    def mat(self) -> LMatrix4: ...
    def __ne__(self, __other: object) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def compare_to(self, other: TransformState, uniquify_matrix: bool = ...) -> int:
        """`(self, other: TransformState)`:
        Provides an arbitrary ordering among all unique TransformStates, so we can
        store the essentially different ones in a big set and throw away the rest.

        Note that if this returns 0, it doesn't necessarily imply that operator ==
        returns true; it uses a very slightly different comparison threshold.

        `(self, other: TransformState, uniquify_matrix: bool)`:
        Provides an arbitrary ordering among all unique TransformStates, so we can
        store the essentially different ones in a big set and throw away the rest.

        Note that if this returns 0, it doesn't necessarily imply that operator ==
        returns true; it uses a very slightly different comparison threshold.

        If uniquify_matrix is true, then matrix-defined TransformStates are also
        uniqified.  If uniquify_matrix is false, then only component-defined
        TransformStates are uniquified, which is less expensive.
        """
    def get_hash(self) -> int:
        """Returns a suitable hash value for phash_map."""
    @staticmethod
    def make_identity() -> TransformState:
        """Constructs an identity transform."""
    @staticmethod
    def make_invalid() -> TransformState:
        """Constructs an invalid transform; for instance, the result of inverting a
        singular matrix.
        """
    @staticmethod
    def make_pos(pos: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_hpr(hpr: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_quat(quat: Vec4Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_pos_hpr(pos: Vec3Like, hpr: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_scale(scale: Vec3Like | float) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_shear(shear: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_pos_hpr_scale(pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_pos_quat_scale(pos: Vec3Like, quat: Vec4Like, scale: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_pos_hpr_scale_shear(pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like, shear: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_pos_quat_scale_shear(pos: Vec3Like, quat: Vec4Like, scale: Vec3Like, shear: Vec3Like) -> TransformState:
        """Makes a new TransformState with the specified components."""
    @staticmethod
    def make_mat(mat: Mat4Like) -> TransformState:
        """Makes a new TransformState with the specified transformation matrix."""
    @staticmethod
    def make_pos2d(pos: Vec2Like) -> TransformState:
        """Makes a new 2-d TransformState with the specified components."""
    @staticmethod
    def make_rotate2d(rotate: float) -> TransformState:
        """Makes a new 2-d TransformState with the specified components."""
    @staticmethod
    def make_pos_rotate2d(pos: Vec2Like, rotate: float) -> TransformState:
        """Makes a new 2-d TransformState with the specified components."""
    @staticmethod
    def make_scale2d(scale: Vec2Like | float) -> TransformState:
        """Makes a new 2-d TransformState with the specified components."""
    @staticmethod
    def make_shear2d(shear: float) -> TransformState:
        """Makes a new 2-d TransformState with the specified components."""
    @staticmethod
    def make_pos_rotate_scale2d(pos: Vec2Like, rotate: float, scale: Vec2Like) -> TransformState:
        """Makes a new 2-d TransformState with the specified components."""
    @staticmethod
    def make_pos_rotate_scale_shear2d(pos: Vec2Like, rotate: float, scale: Vec2Like, shear: float) -> TransformState:
        """Makes a new two-dimensional TransformState with the specified components."""
    @staticmethod
    def make_mat3(mat: LMatrix3) -> TransformState:
        """Makes a new two-dimensional TransformState with the specified 3x3
        transformation matrix.
        """
    def is_identity(self) -> bool:
        """Returns true if the transform represents the identity matrix, false
        otherwise.
        """
    def is_invalid(self) -> bool:
        """Returns true if the transform represents an invalid matrix, for instance
        the result of inverting a singular matrix, or false if the transform is
        valid.
        """
    def is_singular(self) -> bool:
        """Returns true if the transform represents a singular transform (that is, it
        has a zero scale, and it cannot be inverted), or false otherwise.
        """
    def is_2d(self) -> bool:
        """Returns true if the transform has been constructed entirely using the 2-d
        transform operations, e.g.  make_pos2d(), and therefore operates strictly
        in two-dimensional space on X and Y only.
        """
    def has_components(self) -> bool:
        """Returns true if the transform can be described by separate pos, hpr, and
        scale components.  Most transforms we use in everyday life can be so
        described, but some kinds of transforms (for instance, those involving a
        skew) cannot.

        This is not related to whether the transform was originally described
        componentwise.  Even a transform that was constructed with a 4x4 may return
        true here if the matrix is a simple affine matrix with no skew.

        If this returns true, you may safely call get_hpr() and get_scale() to
        retrieve the components.  (You may always safely call get_pos() whether
        this returns true or false.)
        """
    def components_given(self) -> bool:
        """Returns true if the transform was specified componentwise, or false if it
        was specified with a general 4x4 matrix.  If this is true, the components
        returned by get_pos() and get_scale() will be exactly those that were set;
        otherwise, these functions will return computed values.  If this is true,
        the rotation may have been set either with a hpr trio or with a quaternion;
        hpr_given() or quat_given() can resolve the difference.
        """
    def hpr_given(self) -> bool:
        """Returns true if the rotation was specified via a trio of Euler angles,
        false otherwise.  If this is true, get_hpr() will be exactly as set;
        otherwise, it will return a computed value.
        """
    def quat_given(self) -> bool:
        """Returns true if the rotation was specified via a quaternion, false
        otherwise.  If this is true, get_quat() will be exactly as set; otherwise,
        it will return a computed value.
        """
    def has_pos(self) -> bool:
        """Returns true if the transform's pos component can be extracted out
        separately.  This is generally always true, unless the transform is invalid
        (i.e.  is_invalid() returns true).
        """
    def has_hpr(self) -> bool:
        """Returns true if the transform's rotation component can be extracted out
        separately and described as a set of Euler angles.  This is generally true
        only when has_components() is true.
        """
    def has_quat(self) -> bool:
        """Returns true if the transform's rotation component can be extracted out
        separately and described as a quaternion.  This is generally true only when
        has_components() is true.
        """
    def has_scale(self) -> bool:
        """Returns true if the transform's scale component can be extracted out
        separately.  This is generally true only when has_components() is true.
        """
    def has_identity_scale(self) -> bool:
        """Returns true if the scale is uniform 1.0, or false if the scale has some
        real value.
        """
    def has_uniform_scale(self) -> bool:
        """Returns true if the scale is uniform across all three axes (and therefore
        can be expressed as a single number), or false if the transform has a
        different scale in different dimensions.
        """
    def has_shear(self) -> bool:
        """Returns true if the transform's shear component can be extracted out
        separately.  This is generally true only when has_components() is true.
        """
    def has_nonzero_shear(self) -> bool:
        """Returns true if the shear component is non-zero, false if it is zero or if
        the matrix cannot be decomposed.
        """
    def has_mat(self) -> bool:
        """Returns true if the transform can be described as a matrix.  This is
        generally always true, unless is_invalid() is true.
        """
    def get_pos(self) -> LPoint3:
        """Returns the pos component of the transform.  It is an error to call this if
        has_pos() returned false.
        """
    def get_hpr(self) -> LVecBase3:
        """Returns the rotation component of the transform as a trio of Euler angles.
        It is an error to call this if has_components() returned false.
        """
    def get_quat(self) -> LQuaternion:
        """Returns the rotation component of the transform as a quaternion.  The
        return value will be normalized if a normalized quaternion was given to the
        constructor (or if the quaternion was computed implicitly); it will be non-
        normalized if a non-normalized quaternion was given to the constructor.
        See also get_norm_quat().

        It is an error to call this if has_components() returned false.
        """
    def get_norm_quat(self) -> LQuaternion:
        """Returns the rotation component of the transform as a quaternion.  Unlike
        the result of get_quat(), the return value of this method is guaranteed to
        be normalized.  It is an error to call this if has_components() returned
        false.
        """
    def get_scale(self) -> LVecBase3:
        """Returns the scale component of the transform.  It is an error to call this
        if has_components() returned false.
        """
    def get_uniform_scale(self) -> float:
        """Returns the scale component of the transform, as a single number.  It is an
        error to call this if has_uniform_scale() returned false.
        """
    def get_shear(self) -> LVecBase3:
        """Returns the shear component of the transform.  It is an error to call this
        if has_components() returned false.
        """
    def get_mat(self) -> LMatrix4:
        """Returns the matrix that describes the transform."""
    def get_pos2d(self) -> LVecBase2:
        """Returns the pos component of the 2-d transform.  It is an error to call
        this if has_pos() or is_2d() returned false.
        """
    def get_rotate2d(self) -> float:
        """Returns the rotation component of the 2-d transform as an angle in degrees
        clockwise about the origin.  It is an error to call this if
        has_components() or is_2d() returned false.
        """
    def get_scale2d(self) -> LVecBase2:
        """Returns the scale component of the 2-d transform.  It is an error to call
        this if has_components() or is_2d() returned false.
        """
    def get_shear2d(self) -> float:
        """Returns the shear component of the 2-d transform.  It is an error to call
        this if has_components() or is_2d() returned false.
        """
    def get_mat3(self) -> LMatrix3:
        """Returns the 3x3 matrix that describes the 2-d transform.  It is an error to
        call this if is_2d() returned false.
        """
    def set_pos(self, pos: Vec3Like) -> TransformState:
        """Returns a new TransformState object that represents the original
        TransformState with its pos component replaced with the indicated value.
        """
    def set_hpr(self, hpr: Vec3Like) -> TransformState:
        """Returns a new TransformState object that represents the original
        TransformState with its rotation component replaced with the indicated
        value, if possible.
        """
    def set_quat(self, quat: Vec4Like) -> TransformState:
        """Returns a new TransformState object that represents the original
        TransformState with its rotation component replaced with the indicated
        value, if possible.
        """
    def set_scale(self, scale: Vec3Like) -> TransformState:
        """Returns a new TransformState object that represents the original
        TransformState with its scale component replaced with the indicated value,
        if possible.
        """
    def set_shear(self, shear: Vec3Like) -> TransformState:
        """Returns a new TransformState object that represents the original
        TransformState with its shear component replaced with the indicated value,
        if possible.
        """
    def set_pos2d(self, pos: Vec2Like) -> TransformState:
        """Returns a new TransformState object that represents the original 2-d
        TransformState with its pos component replaced with the indicated value.
        """
    def set_rotate2d(self, rotate: float) -> TransformState:
        """Returns a new TransformState object that represents the original 2-d
        TransformState with its rotation component replaced with the indicated
        value, if possible.
        """
    def set_scale2d(self, scale: Vec2Like) -> TransformState:
        """Returns a new TransformState object that represents the original 2-d
        TransformState with its scale component replaced with the indicated value,
        if possible.
        """
    def set_shear2d(self, shear: float) -> TransformState:
        """Returns a new TransformState object that represents the original 2-d
        TransformState with its shear component replaced with the indicated value,
        if possible.
        """
    def compose(self, other: TransformState) -> TransformState:
        """Returns a new TransformState object that represents the composition of this
        state with the other state.

        The result of this operation is cached, and will be retained as long as
        both this TransformState object and the other TransformState object
        continue to exist.  Should one of them destruct, the cached entry will be
        removed, and its pointer will be allowed to destruct as well.
        """
    def invert_compose(self, other: TransformState) -> TransformState:
        """Returns a new TransformState object that represents the composition of this
        state's inverse with the other state.

        This is similar to compose(), but is particularly useful for computing the
        relative state of a node as viewed from some other node.
        """
    def get_inverse(self) -> TransformState:
        """Returns the inverse of this transform.  If you are going to immediately
        compose this result with another TransformState, it is faster to do it in
        one operation with invert_compose().
        """
    def get_unique(self) -> TransformState:
        """Returns the pointer to the unique TransformState in the cache that is
        equivalent to this one.  This may be the same pointer as this object, or it
        may be a different pointer; but it will be an equivalent object, and it
        will be a shared pointer.  This may be called from time to time to improve
        cache benefits.
        """
    def get_geom_rendering(self, geom_rendering: int) -> int:
        """Returns the union of the Geom::GeomRendering bits that will be required
        once this TransformState is applied to a geom which includes the indicated
        geom_rendering bits.  The RenderState's get_geom_rendering() should already
        have been applied.
        """
    def cache_ref(self) -> None:
        """Overrides this method to update PStats appropriately."""
    def cache_unref(self) -> bool:
        """Overrides this method to update PStats appropriately."""
    def node_ref(self) -> None:
        """Overrides this method to update PStats appropriately."""
    def node_unref(self) -> bool:
        """Overrides this method to update PStats appropriately."""
    def get_composition_cache_num_entries(self) -> int:
        """Returns the number of entries in the composition cache for this
        TransformState.  This is the number of other TransformStates whose
        composition with this one has been cached.  This number is not useful for
        any practical reason other than performance analysis.
        """
    def get_invert_composition_cache_num_entries(self) -> int:
        """Returns the number of entries in the invert_composition cache for this
        TransformState.  This is similar to the composition cache, but it records
        cache entries for the invert_compose() operation.  See
        get_composition_cache_num_entries().
        """
    def get_composition_cache_size(self) -> int:
        """Returns the number of slots in the composition cache for this
        TransformState.  You may use this as an upper bound when walking through
        all of the composition cache results via get_composition_cache_source() or
        result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_composition_cache_source(self, n: int) -> TransformState:
        """Returns the source TransformState of the nth element in the composition
        cache.  Returns NULL if there doesn't happen to be an entry in the nth
        element.  See get_composition_cache_result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_composition_cache_result(self, n: int) -> TransformState:
        """Returns the result TransformState of the nth element in the composition
        cache.  Returns NULL if there doesn't happen to be an entry in the nth
        element.

        In general, a->compose(a->get_composition_cache_source(n)) ==
        a->get_composition_cache_result(n).

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_invert_composition_cache_size(self) -> int:
        """Returns the number of slots in the composition cache for this
        TransformState.  You may use this as an upper bound when walking through
        all of the composition cache results via
        get_invert_composition_cache_source() or result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_invert_composition_cache_source(self, n: int) -> TransformState:
        """Returns the source TransformState of the nth element in the invert
        composition cache.  Returns NULL if there doesn't happen to be an entry in
        the nth element.  See get_invert_composition_cache_result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_invert_composition_cache_result(self, n: int) -> TransformState:
        """Returns the result TransformState of the nth element in the invert
        composition cache.  Returns NULL if there doesn't happen to be an entry in
        the nth element.

        In general, a->invert_compose(a->get_invert_composition_cache_source(n)) ==
        a->get_invert_composition_cache_result(n).

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def validate_composition_cache(self) -> bool:
        """Returns true if the composition cache and invert composition cache for this
        particular TransformState are self-consistent and valid, false otherwise.
        """
    def get_composition_cache(self) -> list[tuple[Any, Any] | tuple[None, None]]: ...
    def get_invert_composition_cache(self) -> list[tuple[Any, Any] | tuple[None, None]]: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def write_composition_cache(self, out: ostream, indent_level: int) -> None:
        """Writes a brief description of the composition cache and invert composition
        cache to the indicated ostream.  This is not useful except for performance
        analysis, to examine the cache structure.
        """
    @staticmethod
    def get_num_states() -> int:
        """Returns the total number of unique TransformState objects allocated in the
        world.  This will go up and down during normal operations.
        """
    @staticmethod
    def get_num_unused_states() -> int:
        """Returns the total number of TransformState objects that have been allocated
        but have no references outside of the internal TransformState cache.

        A nonzero return value is not necessarily indicative of leaked references;
        it is normal for two TransformState objects, both of which have references
        held outside the cache, to have the result of their composition stored
        within the cache.  This result will be retained within the cache until one
        of the base TransformStates is released.

        Use list_cycles() to get an idea of the number of actual "leaked"
        TransformState objects.
        """
    @staticmethod
    def clear_cache() -> int:
        """Empties the cache of composed TransformStates.  This makes every
        TransformState forget what results when it is composed with other
        TransformStates.

        This will eliminate any TransformState objects that have been allocated but
        have no references outside of the internal TransformState map.  It will not
        eliminate TransformState objects that are still in use.

        Nowadays, this method should not be necessary, as reference-count cycles in
        the composition cache should be automatically detected and broken.

        The return value is the number of TransformStates freed by this operation.
        """
    @staticmethod
    def garbage_collect() -> int:
        """Performs a garbage-collection cycle.  This must be called periodically if
        garbage-collect-states is true to ensure that TransformStates get cleaned
        up appropriately.  It does no harm to call it even if this variable is not
        true, but there is probably no advantage in that case.
        """
    @staticmethod
    def list_cycles(out: ostream) -> None:
        """Detects all of the reference-count cycles in the cache and reports them to
        standard output.

        These cycles may be inadvertently created when state compositions cycle
        back to a starting point.  Nowadays, these cycles should be automatically
        detected and broken, so this method should never list any cycles unless
        there is a bug in that detection logic.

        The cycles listed here are not leaks in the strictest sense of the word,
        since they can be reclaimed by a call to clear_cache(); but they will not
        be reclaimed automatically.
        """
    @staticmethod
    def list_states(out: ostream) -> None:
        """Lists all of the TransformStates in the cache to the output stream, one per
        line.  This can be quite a lot of output if the cache is large, so be
        prepared.
        """
    @staticmethod
    def validate_states() -> bool:
        """Ensures that the cache is still stored in sorted order, and that none of
        the cache elements have been inadvertently deleted.  Returns true if so,
        false if there is a problem (which implies someone has modified one of the
        supposedly-const TransformState objects).
        """
    @staticmethod
    def get_states() -> list[TransformState]: ...
    @staticmethod
    def get_unused_states() -> list[TransformState]: ...
    compareTo = compare_to
    getHash = get_hash
    makeIdentity = make_identity
    makeInvalid = make_invalid
    makePos = make_pos
    makeHpr = make_hpr
    makeQuat = make_quat
    makePosHpr = make_pos_hpr
    makeScale = make_scale
    makeShear = make_shear
    makePosHprScale = make_pos_hpr_scale
    makePosQuatScale = make_pos_quat_scale
    makePosHprScaleShear = make_pos_hpr_scale_shear
    makePosQuatScaleShear = make_pos_quat_scale_shear
    makeMat = make_mat
    makePos2d = make_pos2d
    makeRotate2d = make_rotate2d
    makePosRotate2d = make_pos_rotate2d
    makeScale2d = make_scale2d
    makeShear2d = make_shear2d
    makePosRotateScale2d = make_pos_rotate_scale2d
    makePosRotateScaleShear2d = make_pos_rotate_scale_shear2d
    makeMat3 = make_mat3
    isIdentity = is_identity
    isInvalid = is_invalid
    isSingular = is_singular
    is2d = is_2d
    hasComponents = has_components
    componentsGiven = components_given
    hprGiven = hpr_given
    quatGiven = quat_given
    hasPos = has_pos
    hasHpr = has_hpr
    hasQuat = has_quat
    hasScale = has_scale
    hasIdentityScale = has_identity_scale
    hasUniformScale = has_uniform_scale
    hasShear = has_shear
    hasNonzeroShear = has_nonzero_shear
    hasMat = has_mat
    getPos = get_pos
    getHpr = get_hpr
    getQuat = get_quat
    getNormQuat = get_norm_quat
    getScale = get_scale
    getUniformScale = get_uniform_scale
    getShear = get_shear
    getMat = get_mat
    getPos2d = get_pos2d
    getRotate2d = get_rotate2d
    getScale2d = get_scale2d
    getShear2d = get_shear2d
    getMat3 = get_mat3
    setPos = set_pos
    setHpr = set_hpr
    setQuat = set_quat
    setScale = set_scale
    setShear = set_shear
    setPos2d = set_pos2d
    setRotate2d = set_rotate2d
    setScale2d = set_scale2d
    setShear2d = set_shear2d
    invertCompose = invert_compose
    getInverse = get_inverse
    getUnique = get_unique
    getGeomRendering = get_geom_rendering
    cacheRef = cache_ref
    cacheUnref = cache_unref
    nodeRef = node_ref
    nodeUnref = node_unref
    getCompositionCacheNumEntries = get_composition_cache_num_entries
    getInvertCompositionCacheNumEntries = get_invert_composition_cache_num_entries
    getCompositionCacheSize = get_composition_cache_size
    getCompositionCacheSource = get_composition_cache_source
    getCompositionCacheResult = get_composition_cache_result
    getInvertCompositionCacheSize = get_invert_composition_cache_size
    getInvertCompositionCacheSource = get_invert_composition_cache_source
    getInvertCompositionCacheResult = get_invert_composition_cache_result
    validateCompositionCache = validate_composition_cache
    getCompositionCache = get_composition_cache
    getInvertCompositionCache = get_invert_composition_cache
    writeCompositionCache = write_composition_cache
    getNumStates = get_num_states
    getNumUnusedStates = get_num_unused_states
    clearCache = clear_cache
    garbageCollect = garbage_collect
    listCycles = list_cycles
    listStates = list_states
    validateStates = validate_states
    getStates = get_states
    getUnusedStates = get_unused_states

class RenderAttribRegistry:
    """This class is used to associate each RenderAttrib with a different slot
    index at runtime, so we can store a list of RenderAttribs in the
    RenderState object, and very quickly look them up by type.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_slot(self, type_handle: TypeHandle | type) -> int:
        """Returns the slot number assigned to the indicated TypeHandle, or 0 if no
        slot number has been assigned.
        """
    @staticmethod
    def get_max_slots() -> int: ...
    def get_num_slots(self) -> int:
        """Returns the number of RenderAttrib slots that have been allocated.  This is
        one more than the highest slot number in use.
        """
    def get_slot_type(self, slot: int) -> TypeHandle:
        """Returns the TypeHandle associated with slot n."""
    def get_slot_sort(self, slot: int) -> int:
        """Returns the sort number associated with slot n."""
    def set_slot_sort(self, slot: int, sort: int) -> None:
        """Changes the sort number associated with slot n."""
    def get_slot_default(self, slot: int) -> RenderAttrib:
        """Returns the default RenderAttrib object associated with slot n.  This is
        the attrib that should be applied in the absence of any other attrib of
        this type.
        """
    def get_num_sorted_slots(self) -> int:
        """Returns the number of entries in the sorted_slots list."""
    def get_sorted_slot(self, n: int) -> int:
        """Returns the nth slot in sorted order.  By traversing this list, you will
        retrieve all the slot numbers in order according to their registered sort
        value.
        """
    @staticmethod
    def get_global_ptr() -> RenderAttribRegistry: ...
    getSlot = get_slot
    getMaxSlots = get_max_slots
    getNumSlots = get_num_slots
    getSlotType = get_slot_type
    getSlotSort = get_slot_sort
    setSlotSort = set_slot_sort
    getSlotDefault = get_slot_default
    getNumSortedSlots = get_num_sorted_slots
    getSortedSlot = get_sorted_slot
    getGlobalPtr = get_global_ptr

class RenderAttrib(TypedWritableReferenceCount):
    """This is the base class for a number of render attributes (other than
    transform) that may be set on scene graph nodes to control the appearance
    of geometry.  This includes TextureAttrib, ColorAttrib, etc.

    RenderAttrib represents render attributes that always propagate down to the
    leaves without regard to the particular node they are assigned to.  A
    RenderAttrib will have the same effect on a leaf node whether it is
    assigned to the graph at the leaf or several nodes above.  This is
    different from RenderEffect, which represents a particular render property
    that is applied immediately to the node on which it is encountered, like
    billboarding or decaling.

    You should not attempt to create or modify a RenderAttrib directly;
    instead, use the make() method of the appropriate kind of attrib you want.
    This will allocate and return a new RenderAttrib of the appropriate type,
    and it may share pointers if possible.  Do not modify the new RenderAttrib
    if you wish to change its properties; instead, create a new one.
    """

    M_none: Final = 0
    MNone: Final = 0
    M_never: Final = 1
    MNever: Final = 1
    M_less: Final = 2
    MLess: Final = 2
    M_equal: Final = 3
    MEqual: Final = 3
    M_less_equal: Final = 4
    MLessEqual: Final = 4
    M_greater: Final = 5
    MGreater: Final = 5
    M_not_equal: Final = 6
    MNotEqual: Final = 6
    M_greater_equal: Final = 7
    MGreaterEqual: Final = 7
    M_always: Final = 8
    MAlways: Final = 8
    M_off: Final = 0
    MOff: Final = 0
    M_eye_sphere_map: Final = 1
    MEyeSphereMap: Final = 1
    M_world_cube_map: Final = 2
    MWorldCubeMap: Final = 2
    M_eye_cube_map: Final = 3
    MEyeCubeMap: Final = 3
    M_world_normal: Final = 4
    MWorldNormal: Final = 4
    M_eye_normal: Final = 5
    MEyeNormal: Final = 5
    M_world_position: Final = 6
    MWorldPosition: Final = 6
    M_unused: Final = 7
    MUnused: Final = 7
    M_eye_position: Final = 8
    MEyePosition: Final = 8
    M_point_sprite: Final = 9
    MPointSprite: Final = 9
    M_unused2: Final = 10
    MUnused2: Final = 10
    M_constant: Final = 11
    MConstant: Final = 11
    @property
    def slot(self) -> int: ...
    def compose(self, other: RenderAttrib) -> RenderAttrib:
        """Returns a new RenderAttrib object that represents the composition of this
        attrib with the other attrib.  In most cases, this is the same as the other
        attrib; a compose b produces b.  Some kinds of attributes, like a
        TextureTransform, for instance, might produce a new result: a compose b
        produces c.
        """
    def invert_compose(self, other: RenderAttrib) -> RenderAttrib:
        """Returns a new RenderAttrib object that represents the composition of the
        inverse of this attrib with the other attrib.  In most cases, this is the
        same as the other attrib; !a compose b produces b.  Some kinds of
        attributes, like a TextureTransform, for instance, might produce a new
        result: !a compose b produces c.

        This is similar to compose() except that the source attrib is inverted
        first.  This is used to compute the relative attribute for one node as
        viewed from some other node, which is especially useful for transform-type
        attributes.
        """
    def lower_attrib_can_override(self) -> bool:
        """Intended to be overridden by derived RenderAttrib types to specify how two
        consecutive RenderAttrib objects of the same type interact.

        This should return false if a RenderAttrib on a higher node will compose
        into a RenderAttrib on a lower node that has a higher override value, or
        true if the lower RenderAttrib will completely replace the state.

        The default behavior is false: normally, a RenderAttrib in the graph cannot
        completely override a RenderAttrib above it, regardless of its override
        value--instead, the two attribs are composed.  But for some kinds of
        RenderAttribs, it is useful to allow this kind of override.

        This method only handles the one special case of a lower RenderAttrib with
        a higher override value.  If the higher RenderAttrib has a higher override
        value, it always completely overrides.  And if both RenderAttribs have the
        same override value, they are always composed.
        """
    def compare_to(self, other: RenderAttrib) -> int:
        """Provides an arbitrary ordering among all unique RenderAttribs, so we can
        store the essentially different ones in a big set and throw away the rest.

        This method is not needed outside of the RenderAttrib class because all
        equivalent RenderAttrib objects are guaranteed to share the same pointer;
        thus, a pointer comparison is always sufficient.
        """
    def get_hash(self) -> int:
        """Returns a suitable hash value for phash_map."""
    def get_unique(self) -> RenderAttrib:
        """Returns the pointer to the unique RenderAttrib in the cache that is
        equivalent to this one.  This may be the same pointer as this object, or it
        may be a different pointer; but it will be an equivalent object, and it
        will be a shared pointer.  This may be called from time to time to improve
        cache benefits.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_num_attribs() -> int:
        """Returns the total number of unique RenderAttrib objects allocated in the
        world.  This will go up and down during normal operations.
        """
    @staticmethod
    def list_attribs(out: ostream) -> None:
        """Lists all of the RenderAttribs in the cache to the output stream, one per
        line.  This can be quite a lot of output if the cache is large, so be
        prepared.
        """
    @staticmethod
    def garbage_collect() -> int:
        """Performs a garbage-collection cycle.  This is called automatically from
        RenderState::garbage_collect(); see that method for more information.
        """
    @staticmethod
    def validate_attribs() -> bool:
        """Ensures that the cache is still stored in sorted order.  Returns true if
        so, false if there is a problem (which implies someone has modified one of
        the supposedly-const RenderAttrib objects).
        """
    def get_slot(self) -> int: ...
    invertCompose = invert_compose
    lowerAttribCanOverride = lower_attrib_can_override
    compareTo = compare_to
    getHash = get_hash
    getUnique = get_unique
    getNumAttribs = get_num_attribs
    listAttribs = list_attribs
    garbageCollect = garbage_collect
    validateAttribs = validate_attribs
    getSlot = get_slot

class RenderModeAttrib(RenderAttrib):
    """Specifies how polygons are to be drawn."""

    M_unchanged: Final = 0
    MUnchanged: Final = 0
    M_filled: Final = 1
    MFilled: Final = 1
    M_wireframe: Final = 2
    MWireframe: Final = 2
    M_point: Final = 3
    MPoint: Final = 3
    M_filled_flat: Final = 4
    MFilledFlat: Final = 4
    M_filled_wireframe: Final = 5
    MFilledWireframe: Final = 5
    @property
    def mode(self) -> _RenderModeAttrib_Mode: ...
    @property
    def thickness(self) -> float: ...
    @property
    def perspective(self) -> bool: ...
    @property
    def wireframe_color(self) -> LColor: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(
        mode: _RenderModeAttrib_Mode, thickness: float = ..., perspective: bool = ..., wireframe_color: Vec4Like = ...
    ) -> RenderAttrib:
        """Constructs a new RenderModeAttrib object that specifies whether to draw
        polygons in the normal, filled mode, or wireframe mode, or in some other
        yet-to-be-defined mode.

        The thickness parameter specifies the thickness to be used for wireframe
        lines, as well as for ordinary linestrip lines; it also specifies the
        diameter of points.  (Thick lines are presently only supported in OpenGL;
        but thick points are supported on either platform.)

        If perspective is true, the point thickness represented is actually a width
        in 3-d units, and the points should scale according to perspective.  When
        it is false, the point thickness is actually a width in pixels, and points
        are a uniform screen size regardless of distance from the camera.

        In M_filled_wireframe mode, you should also specify the wireframe_color,
        indicating the flat color to assign to the overlayed wireframe.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> _RenderModeAttrib_Mode:
        """Returns the render mode."""
    def get_thickness(self) -> float:
        """Returns the line width or point thickness.  This is only relevant when
        rendering points or lines, such as when the mode is M_wireframe or M_point
        (or when rendering actual points or lines primitives in M_polygon mode).
        """
    def get_perspective(self) -> bool:
        """Returns the perspective flag.  When this is true, the point thickness
        represented by get_thickness() is actually a width in 3-d units, and the
        points should scale according to perspective.  When it is false, the
        default, the point thickness is actually a width in pixels, and points are
        a uniform size regardless of distance from the camera.
        """
    def get_wireframe_color(self) -> LColor:
        """Returns the color that is used in M_filled_wireframe mode to distinguish
        the wireframe from the rest of the geometry.
        """
    def get_geom_rendering(self, geom_rendering: int) -> int:
        """Returns the union of the Geom::GeomRendering bits that will be required
        once this RenderModeAttrib is applied to a geom which includes the
        indicated geom_rendering bits.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getThickness = get_thickness
    getPerspective = get_perspective
    getWireframeColor = get_wireframe_color
    getGeomRendering = get_geom_rendering
    getClassSlot = get_class_slot

class TexMatrixAttrib(RenderAttrib):
    """Applies a transform matrix to UV's before they are rendered."""

    @property
    def class_slot(self) -> int: ...
    @overload
    @staticmethod
    def make(mat: Mat4Like = ...) -> RenderAttrib:
        """`()`:
        Constructs a TexMatrixAttrib that applies no stages at all.

        `(mat: LMatrix4)`:
        Constructs a TexMatrixAttrib that applies the indicated matrix to the
        default texture stage.  This interface is deprecated.

        @deprecated Use the constructor that takes a TextureStage instead.

        `(stage: TextureStage, transform: TransformState)`:
        Constructs a TexMatrixAttrib that applies the indicated transform to the
        named texture stage.
        """
    @overload
    @staticmethod
    def make(stage: TextureStage, transform: TransformState) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def add_stage(self, stage: TextureStage, transform: TransformState, override: int = ...) -> RenderAttrib:
        """Returns a new TexMatrixAttrib just like this one, with the indicated
        transform for the given stage.  If this stage already exists, its transform
        is replaced.
        """
    def remove_stage(self, stage: TextureStage) -> RenderAttrib:
        """Returns a new TexMatrixAttrib just like this one, with the indicated stage
        removed.
        """
    def is_empty(self) -> bool:
        """Returns true if no stages are defined in the TexMatrixAttrib, false if at
        least one is.
        """
    def has_stage(self, stage: TextureStage) -> bool:
        """Returns true if there is a transform associated with the indicated stage,
        or false otherwise (in which case get_transform(stage) will return the
        identity transform).
        """
    def get_num_stages(self) -> int:
        """Returns the number of stages that are represented by this attrib."""
    def get_stage(self, n: int) -> TextureStage:
        """Returns the nth stage that is represented by this attrib.  The
        TextureStages are in no particular order.
        """
    def get_mat(self, stage: TextureStage = ...) -> LMatrix4:
        """`(self)`:
        Returns the transformation matrix associated with the default texture
        stage.

        `(self, stage: TextureStage)`:
        Returns the transformation matrix associated with the indicated texture
        stage, or identity matrix if nothing is associated with the indicated
        stage.
        """
    def get_transform(self, stage: TextureStage) -> TransformState:
        """Returns the transformation associated with the indicated texture stage, or
        identity matrix if nothing is associated with the indicated stage.
        """
    def get_override(self, stage: TextureStage) -> int:
        """Returns the override value associated with the indicated stage."""
    def get_geom_rendering(self, geom_rendering: int) -> int:
        """Returns the union of the Geom::GeomRendering bits that will be required
        once this TexMatrixAttrib is applied to a geom which includes the indicated
        geom_rendering bits.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    def get_stages(self) -> tuple[TextureStage, ...]: ...
    makeDefault = make_default
    addStage = add_stage
    removeStage = remove_stage
    isEmpty = is_empty
    hasStage = has_stage
    getNumStages = get_num_stages
    getStage = get_stage
    getMat = get_mat
    getTransform = get_transform
    getOverride = get_override
    getGeomRendering = get_geom_rendering
    getClassSlot = get_class_slot
    getStages = get_stages

class RenderState(NodeCachedReferenceCount):
    """This represents a unique collection of RenderAttrib objects that correspond
    to a particular renderable state.

    You should not attempt to create or modify a RenderState object directly.
    Instead, call one of the make() functions to create one for you.  And
    instead of modifying a RenderState object, create a new one.
    """

    @property
    def attribs(self) -> Mapping[TypeHandle, RenderAttrib]: ...
    def compare_to(self, other: RenderState) -> int:
        """Provides an arbitrary ordering among all unique RenderStates, so we can
        store the essentially different ones in a big set and throw away the rest.

        This method is not needed outside of the RenderState class because all
        equivalent RenderState objects are guaranteed to share the same pointer;
        thus, a pointer comparison is always sufficient.
        """
    def compare_sort(self, other: RenderState) -> int:
        """Returns -1, 0, or 1 according to the relative sorting of these two
        RenderStates, with regards to rendering performance, so that "heavier"
        RenderAttribs (as defined by RenderAttribRegistry::get_slot_sort()) are
        more likely to be grouped together.  This is not related to the sorting
        order defined by compare_to.
        """
    def compare_mask(self, other: RenderState, compare_mask: BitMask32 | int) -> int:
        """This version of compare_to takes a slot mask that indicates which
        attributes to include in the comparison.  Unlike compare_to, this method
        compares the attributes by pointer.
        """
    def get_hash(self) -> int:
        """Returns a suitable hash value for phash_map."""
    def is_empty(self) -> bool:
        """Returns true if the state is empty, false otherwise."""
    def has_cull_callback(self) -> bool:
        """Returns true if any of the RenderAttribs in this state request a
        cull_callback(), false if none of them do.
        """
    def cull_callback(self, trav: CullTraverser, data: CullTraverserData) -> bool:
        """Calls cull_callback() on each attrib.  If any attrib returns false,
        interrupts the list and returns false immediately; otherwise, completes the
        list and returns true.
        """
    @staticmethod
    def make_empty() -> RenderState:
        """Returns a RenderState with no attributes set."""
    @overload
    @staticmethod
    def make(attrib: RenderAttrib, override: int = ...) -> RenderState:
        """`(attrib1: RenderAttrib, attrib2: RenderAttrib, attrib3: RenderAttrib, attrib4: RenderAttrib, attrib5: RenderAttrib, override: int = ...)`:
        Returns a RenderState with five attributes set.

        `(attrib1: RenderAttrib, attrib2: RenderAttrib, attrib3: RenderAttrib, attrib4: RenderAttrib, override: int = ...)`:
        Returns a RenderState with four attributes set.

        `(attrib1: RenderAttrib, attrib2: RenderAttrib, attrib3: RenderAttrib, override: int = ...)`:
        Returns a RenderState with three attributes set.

        `(attrib1: RenderAttrib, attrib2: RenderAttrib, override: int = ...)`:
        Returns a RenderState with two attributes set.

        `(attrib: RenderAttrib, override: int = ...)`:
        Returns a RenderState with one attribute set.
        """
    @overload
    @staticmethod
    def make(attrib1: RenderAttrib, attrib2: RenderAttrib, override: int = ...) -> RenderState: ...
    @overload
    @staticmethod
    def make(attrib1: RenderAttrib, attrib2: RenderAttrib, attrib3: RenderAttrib, override: int = ...) -> RenderState: ...
    @overload
    @staticmethod
    def make(
        attrib1: RenderAttrib, attrib2: RenderAttrib, attrib3: RenderAttrib, attrib4: RenderAttrib, override: int = ...
    ) -> RenderState: ...
    @overload
    @staticmethod
    def make(
        attrib1: RenderAttrib,
        attrib2: RenderAttrib,
        attrib3: RenderAttrib,
        attrib4: RenderAttrib,
        attrib5: RenderAttrib,
        override: int = ...,
    ) -> RenderState: ...
    def compose(self, other: RenderState) -> RenderState:
        """Returns a new RenderState object that represents the composition of this
        state with the other state.

        The result of this operation is cached, and will be retained as long as
        both this RenderState object and the other RenderState object continue to
        exist.  Should one of them destruct, the cached entry will be removed, and
        its pointer will be allowed to destruct as well.
        """
    def invert_compose(self, other: RenderState) -> RenderState:
        """Returns a new RenderState object that represents the composition of this
        state's inverse with the other state.

        This is similar to compose(), but is particularly useful for computing the
        relative state of a node as viewed from some other node.
        """
    def add_attrib(self, attrib: RenderAttrib, override: int = ...) -> RenderState:
        """Returns a new RenderState object that represents the same as the source
        state, with the new RenderAttrib added.  If there is already a RenderAttrib
        with the same type, it is replaced (unless the override is lower).
        """
    def set_attrib(self, attrib: RenderAttrib, override: int = ...) -> RenderState:
        """`(self, attrib: RenderAttrib)`:
        Returns a new RenderState object that represents the same as the source
        state, with the new RenderAttrib added.  If there is already a RenderAttrib
        with the same type, it is replaced unconditionally.  The override is not
        changed.

        `(self, attrib: RenderAttrib, override: int)`:
        Returns a new RenderState object that represents the same as the source
        state, with the new RenderAttrib added.  If there is already a RenderAttrib
        with the same type, it is replaced unconditionally.  The override is also
        replaced unconditionally.
        """
    @overload
    def remove_attrib(self, type: TypeHandle | type) -> RenderState:
        """Returns a new RenderState object that represents the same as the source
        state, with the indicated RenderAttrib removed.
        """
    @overload
    def remove_attrib(self, slot: int) -> RenderState: ...
    def adjust_all_priorities(self, adjustment: int) -> RenderState:
        """Returns a new RenderState object that represents the same as the source
        state, with all attributes' override values incremented (or decremented, if
        negative) by the indicated amount.  If the override would drop below zero,
        it is set to zero.
        """
    @overload
    def has_attrib(self, type: TypeHandle | type) -> bool:
        """Returns true if an attrib of the indicated type is present, false
        otherwise.
        """
    @overload
    def has_attrib(self, slot: int) -> bool: ...
    @overload
    def get_attrib(self, type: TypeHandle | type) -> RenderAttrib:
        """`(self, type: TypeHandle)`:
        Looks for a RenderAttrib of the indicated type in the state, and returns it
        if it is found, or NULL if it is not.

        `(self, slot: int)`:
        Returns the RenderAttrib with the indicated slot index, or NULL if there is
        no such RenderAttrib in the state.
        """
    @overload
    def get_attrib(self, slot: int) -> RenderAttrib: ...
    def get_attrib_def(self, slot: int) -> RenderAttrib:
        """Returns the RenderAttrib with the indicated slot index, or the default
        attrib for that slot if there is no such RenderAttrib in the state.
        """
    @overload
    def get_override(self, type: TypeHandle | type) -> int:
        """Looks for a RenderAttrib of the indicated type in the state, and returns
        its override value if it is found, or 0 if it is not.
        """
    @overload
    def get_override(self, slot: int) -> int: ...
    def get_unique(self) -> RenderState:
        """Returns the pointer to the unique RenderState in the cache that is
        equivalent to this one.  This may be the same pointer as this object, or it
        may be a different pointer; but it will be an equivalent object, and it
        will be a shared pointer.  This may be called from time to time to improve
        cache benefits.
        """
    def cache_ref(self) -> None:
        """Overrides this method to update PStats appropriately."""
    def cache_unref(self) -> bool:
        """Overrides this method to update PStats appropriately."""
    def node_ref(self) -> None:
        """Overrides this method to update PStats appropriately."""
    def node_unref(self) -> bool:
        """Overrides this method to update PStats appropriately."""
    def get_composition_cache_num_entries(self) -> int:
        """Returns the number of entries in the composition cache for this
        RenderState.  This is the number of other RenderStates whose composition
        with this one has been cached.  This number is not useful for any practical
        reason other than performance analysis.
        """
    def get_invert_composition_cache_num_entries(self) -> int:
        """Returns the number of entries in the invert_composition cache for this
        RenderState.  This is similar to the composition cache, but it records
        cache entries for the invert_compose() operation.  See
        get_composition_cache_num_entries().
        """
    def get_composition_cache_size(self) -> int:
        """Returns the number of slots in the composition cache for this RenderState.
        You may use this as an upper bound when walking through all of the
        composition cache results via get_composition_cache_source() or result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_composition_cache_source(self, n: int) -> RenderState:
        """Returns the source RenderState of the nth element in the composition cache.
        Returns NULL if there doesn't happen to be an entry in the nth element.
        See get_composition_cache_result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_composition_cache_result(self, n: int) -> RenderState:
        """Returns the result RenderState of the nth element in the composition cache.
        Returns NULL if there doesn't happen to be an entry in the nth element.

        In general, a->compose(a->get_composition_cache_source(n)) ==
        a->get_composition_cache_result(n).

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_invert_composition_cache_size(self) -> int:
        """Returns the number of slots in the composition cache for this RenderState.
        You may use this as an upper bound when walking through all of the
        composition cache results via get_invert_composition_cache_source() or
        result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_invert_composition_cache_source(self, n: int) -> RenderState:
        """Returns the source RenderState of the nth element in the invert composition
        cache.  Returns NULL if there doesn't happen to be an entry in the nth
        element.  See get_invert_composition_cache_result().

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_invert_composition_cache_result(self, n: int) -> RenderState:
        """Returns the result RenderState of the nth element in the invert composition
        cache.  Returns NULL if there doesn't happen to be an entry in the nth
        element.

        In general, a->invert_compose(a->get_invert_composition_cache_source(n)) ==
        a->get_invert_composition_cache_result(n).

        This has no practical value other than for examining the cache for
        performance analysis.
        """
    def get_composition_cache(self) -> list[tuple[Any, Any] | tuple[None, None]]: ...
    def get_invert_composition_cache(self) -> list[tuple[Any, Any] | tuple[None, None]]: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_max_priority() -> int:
        """Returns the maximum priority number (sometimes called override) that may be
        set on any node.  This may or may not be enforced, but the scene graph code
        assumes that no priority numbers will be larger than this, and some effects
        may not work properly if you use a larger number.
        """
    @staticmethod
    def get_num_states() -> int:
        """Returns the total number of unique RenderState objects allocated in the
        world.  This will go up and down during normal operations.
        """
    @staticmethod
    def get_num_unused_states() -> int:
        """Returns the total number of RenderState objects that have been allocated
        but have no references outside of the internal RenderState cache.

        A nonzero return value is not necessarily indicative of leaked references;
        it is normal for two RenderState objects, both of which have references
        held outside the cache, to have to result of their composition stored
        within the cache.  This result will be retained within the cache until one
        of the base RenderStates is released.

        Use list_cycles() to get an idea of the number of actual "leaked"
        RenderState objects.
        """
    @staticmethod
    def clear_cache() -> int:
        """Empties the cache of composed RenderStates.  This makes every RenderState
        forget what results when it is composed with other RenderStates.

        This will eliminate any RenderState objects that have been allocated but
        have no references outside of the internal RenderState map.  It will not
        eliminate RenderState objects that are still in use.

        Nowadays, this method should not be necessary, as reference-count cycles in
        the composition cache should be automatically detected and broken.

        The return value is the number of RenderStates freed by this operation.
        """
    @staticmethod
    def clear_munger_cache() -> None:
        """Completely empties the cache of state + gsg -> munger, for all states and
        all gsg's.  Normally there is no need to empty this cache.
        """
    @staticmethod
    def garbage_collect() -> int:
        """Performs a garbage-collection cycle.  This must be called periodically if
        garbage-collect-states is true to ensure that RenderStates get cleaned up
        appropriately.  It does no harm to call it even if this variable is not
        true, but there is probably no advantage in that case.

        This automatically calls RenderAttrib::garbage_collect() as well.
        """
    @staticmethod
    def list_cycles(out: ostream) -> None:
        """Detects all of the reference-count cycles in the cache and reports them to
        standard output.

        These cycles may be inadvertently created when state compositions cycle
        back to a starting point.  Nowadays, these cycles should be automatically
        detected and broken, so this method should never list any cycles unless
        there is a bug in that detection logic.

        The cycles listed here are not leaks in the strictest sense of the word,
        since they can be reclaimed by a call to clear_cache(); but they will not
        be reclaimed automatically.
        """
    @staticmethod
    def list_states(out: ostream) -> None:
        """Lists all of the RenderStates in the cache to the output stream, one per
        line.  This can be quite a lot of output if the cache is large, so be
        prepared.
        """
    @staticmethod
    def validate_states() -> bool:
        """Ensures that the cache is still stored in sorted order, and that none of
        the cache elements have been inadvertently deleted.  Returns true if so,
        false if there is a problem (which implies someone has modified one of the
        supposedly-const RenderState objects).
        """
    @staticmethod
    def get_states() -> list[RenderState]: ...
    @staticmethod
    def get_unused_states() -> list[RenderState]: ...
    def get_draw_order(self) -> int:
        """Returns the draw order indicated by the CullBinAttrib, if any, associated
        by this state (or 0 if there is no CullBinAttrib).  See get_bin_index().
        """
    def get_bin_index(self) -> int:
        """Returns the bin index indicated by the CullBinAttrib, if any, associated by
        this state (or the default bin index if there is no CullBinAttrib).  This
        function is provided as an optimization for determining this at render
        time.
        """
    def get_geom_rendering(self, geom_rendering: int) -> int:
        """Returns the union of the Geom::GeomRendering bits that will be required
        once this RenderState is applied to a geom which includes the indicated
        geom_rendering bits.
        """
    compareTo = compare_to
    compareSort = compare_sort
    compareMask = compare_mask
    getHash = get_hash
    isEmpty = is_empty
    hasCullCallback = has_cull_callback
    cullCallback = cull_callback
    makeEmpty = make_empty
    invertCompose = invert_compose
    addAttrib = add_attrib
    setAttrib = set_attrib
    removeAttrib = remove_attrib
    adjustAllPriorities = adjust_all_priorities
    hasAttrib = has_attrib
    getAttrib = get_attrib
    getAttribDef = get_attrib_def
    getOverride = get_override
    getUnique = get_unique
    cacheRef = cache_ref
    cacheUnref = cache_unref
    nodeRef = node_ref
    nodeUnref = node_unref
    getCompositionCacheNumEntries = get_composition_cache_num_entries
    getInvertCompositionCacheNumEntries = get_invert_composition_cache_num_entries
    getCompositionCacheSize = get_composition_cache_size
    getCompositionCacheSource = get_composition_cache_source
    getCompositionCacheResult = get_composition_cache_result
    getInvertCompositionCacheSize = get_invert_composition_cache_size
    getInvertCompositionCacheSource = get_invert_composition_cache_source
    getInvertCompositionCacheResult = get_invert_composition_cache_result
    getCompositionCache = get_composition_cache
    getInvertCompositionCache = get_invert_composition_cache
    getMaxPriority = get_max_priority
    getNumStates = get_num_states
    getNumUnusedStates = get_num_unused_states
    clearCache = clear_cache
    clearMungerCache = clear_munger_cache
    garbageCollect = garbage_collect
    listCycles = list_cycles
    listStates = list_states
    validateStates = validate_states
    getStates = get_states
    getUnusedStates = get_unused_states
    getDrawOrder = get_draw_order
    getBinIndex = get_bin_index
    getGeomRendering = get_geom_rendering

class AlphaTestAttrib(RenderAttrib):
    """Enables or disables writing of pixel to framebuffer based on its alpha
    value relative to a reference alpha value
    """

    @property
    def reference_alpha(self) -> float: ...
    @property
    def mode(self) -> _RenderAttrib_PandaCompareFunc: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _RenderAttrib_PandaCompareFunc, reference_alpha: float) -> RenderAttrib:
        """Constructs a new AlphaTestAttrib object."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_reference_alpha(self) -> float:
        """Returns the alpha reference value."""
    def get_mode(self) -> _RenderAttrib_PandaCompareFunc:
        """Returns the alpha write mode."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getReferenceAlpha = get_reference_alpha
    getMode = get_mode
    getClassSlot = get_class_slot

class AntialiasAttrib(RenderAttrib):
    """Specifies whether or how to enable antialiasing, if supported by the
    backend renderer.
    """

    M_point: Final = 1
    MPoint: Final = 1
    M_line: Final = 2
    MLine: Final = 2
    M_polygon: Final = 4
    MPolygon: Final = 4
    M_multisample: Final = 8
    MMultisample: Final = 8
    M_auto: Final = 31
    MAuto: Final = 31
    M_type_mask: Final = 31
    MTypeMask: Final = 31
    M_faster: Final = 32
    MFaster: Final = 32
    M_better: Final = 64
    MBetter: Final = 64
    M_dont_care: Final = 96
    MDontCare: Final = 96
    @property
    def mode(self) -> int: ...
    @property
    def mode_type(self) -> int: ...
    @property
    def mode_quality(self) -> int: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: int) -> RenderAttrib:
        """Constructs a new AntialiasAttrib object.

        The mode should be either M_none, M_auto, or a union of any or all of
        M_point, M_line, M_polygon, and M_multisample.  Also, in addition to the
        above choices, it may include either of M_better of M_faster to specify a
        performance/quality tradeoff hint.

        If M_none is specified, no antialiasing is performed.

        If M_multisample is specified, it means to use the special framebuffer
        multisample bits for antialiasing, if it is available.  If so, the M_point,
        M_line, and M_polygon modes are ignored.  This advanced antialiasing mode
        is only available on certain graphics hardware.  If it is not available,
        the M_multisample bit is ignored (and the other modes may be used instead,
        if specified).

        M_point, M_line, and/or M_polygon specify per-primitive smoothing.  When
        enabled, M_point and M_line may force transparency on.  M_polygon requires
        a frame buffer that includes an alpha channel, and it works best if the
        primitives are sorted front-to-back.

        If M_auto is specified, M_multisample is selected if it is available,
        otherwise M_polygon is selected, unless drawing lines or points, in which
        case M_line or M_point is selected (these two generally produce better
        results than M_multisample)
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> int:
        """Returns the specified antialias mode."""
    def get_mode_type(self) -> int:
        """Returns the specified antialias mode, with the quality bits masked out.
        This therefore indicates only the requested type of antialiasing: M_none,
        M_auto, or some specific combination.
        """
    def get_mode_quality(self) -> int:
        """Returns the specified antialias mode, with the type bits masked out.  This
        therefore indicates only the requested quality settings: one of M_faster,
        M_better, M_dont_care, or zero (unspecified).
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getModeType = get_mode_type
    getModeQuality = get_mode_quality
    getClassSlot = get_class_slot

class RenderEffect(TypedWritableReferenceCount):
    """This is the base class for a number of special render effects that may be
    set on scene graph nodes to change the way they render.  This includes
    BillboardEffect, DecalEffect, etc.

    RenderEffect represents render properties that must be applied as soon as
    they are encountered in the scene graph, rather than propagating down to
    the leaves.  This is different from RenderAttrib, which represents
    properties like color and texture that don't do anything until they
    propagate down to a GeomNode.

    You should not attempt to create or modify a RenderEffect directly;
    instead, use the make() method of the appropriate kind of effect you want.
    This will allocate and return a new RenderEffect of the appropriate type,
    and it may share pointers if possible.  Do not modify the new RenderEffect
    if you wish to change its properties; instead, create a new one.
    """

    def compare_to(self, other: RenderEffect) -> int:
        """Provides an arbitrary ordering among all unique RenderEffects, so we can
        store the essentially different ones in a big set and throw away the rest.

        This method is not needed outside of the RenderEffect class because all
        equivalent RenderEffect objects are guaranteed to share the same pointer;
        thus, a pointer comparison is always sufficient.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_num_effects() -> int:
        """Returns the total number of unique RenderEffect objects allocated in the
        world.  This will go up and down during normal operations.
        """
    @staticmethod
    def list_effects(out: ostream) -> None:
        """Lists all of the RenderEffects in the cache to the output stream, one per
        line.  This can be quite a lot of output if the cache is large, so be
        prepared.
        """
    @staticmethod
    def validate_effects() -> bool:
        """Ensures that the cache is still stored in sorted order.  Returns true if
        so, false if there is a problem (which implies someone has modified one of
        the supposedly-const RenderEffect objects).
        """
    compareTo = compare_to
    getNumEffects = get_num_effects
    listEffects = list_effects
    validateEffects = validate_effects

class RenderEffects(TypedWritableReferenceCount):
    """This represents a unique collection of RenderEffect objects that correspond
    to a particular renderable state.

    You should not attempt to create or modify a RenderEffects object directly.
    Instead, call one of the make() functions to create one for you.  And
    instead of modifying a RenderEffects object, create a new one.
    """

    def __lt__(self, other: RenderEffect | RenderEffects) -> bool: ...
    def __len__(self) -> int:
        """Returns the number of separate effects indicated in the state."""
    @overload
    def __getitem__(self, type: TypeHandle | type) -> RenderEffect:
        """`(self, type: TypeHandle)`:
        Returns the effect in the state with the given type.

        `(self, n: int)`:
        Returns the nth effect in the state.
        """
    @overload
    def __getitem__(self, n: int) -> RenderEffect: ...
    def is_empty(self) -> bool:
        """Returns true if the state is empty, false otherwise."""
    def get_num_effects(self) -> int:
        """Returns the number of separate effects indicated in the state.
        @deprecated in Python, use len(effects) instead, or effects.size() in C++.
        """
    @overload
    def get_effect(self, type: TypeHandle | type) -> RenderEffect:
        """`(self, type: TypeHandle)`:
        Looks for a RenderEffect of the indicated type in the state, and returns it
        if it is found, or NULL if it is not.

        `(self, n: int)`:
        Returns the nth effect in the state.
        """
    @overload
    def get_effect(self, n: int) -> RenderEffect: ...
    def find_effect(self, type: TypeHandle | type) -> int:
        """Searches for an effect with the indicated type in the state, and returns
        its index if it is found, or -1 if it is not.
        """
    @staticmethod
    def make_empty() -> RenderEffects:
        """Returns a RenderEffects with no effects set."""
    @overload
    @staticmethod
    def make(effect: RenderEffect) -> RenderEffects:
        """`(effect: RenderEffect)`:
        Returns a RenderEffects with one effect set.

        `(effect1: RenderEffect, effect2: RenderEffect)`:
        Returns a RenderEffects with two effects set.

        `(effect1: RenderEffect, effect2: RenderEffect, effect3: RenderEffect)`:
        Returns a RenderEffects with three effects set.

        `(effect1: RenderEffect, effect2: RenderEffect, effect3: RenderEffect, effect4: RenderEffect)`:
        Returns a RenderEffects with four effects set.
        """
    @overload
    @staticmethod
    def make(effect1: RenderEffect, effect2: RenderEffect, effect3: RenderEffect = ...) -> RenderEffects: ...
    @overload
    @staticmethod
    def make(effect1: RenderEffect, effect2: RenderEffect, effect3: RenderEffect, effect4: RenderEffect) -> RenderEffects: ...
    def add_effect(self, effect: RenderEffect) -> RenderEffects:
        """Returns a new RenderEffects object that represents the same as the source
        state, with the new RenderEffect added.  If there is already a RenderEffect
        with the same type, it is replaced.
        """
    def remove_effect(self, type: TypeHandle | type) -> RenderEffects:
        """Returns a new RenderEffects object that represents the same as the source
        state, with the indicated RenderEffect removed.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    @staticmethod
    def get_num_states() -> int:
        """Returns the total number of unique RenderEffects objects allocated in the
        world.  This will go up and down during normal operations.
        """
    @staticmethod
    def list_states(out: ostream) -> None:
        """Lists all of the RenderEffects in the cache to the output stream, one per
        line.  This can be quite a lot of output if the cache is large, so be
        prepared.
        """
    @staticmethod
    def validate_states() -> bool:
        """Ensures that the cache is still stored in sorted order.  Returns true if
        so, false if there is a problem (which implies someone has modified one of
        the supposedly-const RenderEffects objects).
        """
    isEmpty = is_empty
    getNumEffects = get_num_effects
    getEffect = get_effect
    findEffect = find_effect
    makeEmpty = make_empty
    addEffect = add_effect
    removeEffect = remove_effect
    getNumStates = get_num_states
    listStates = list_states
    validateStates = validate_states

class PandaNode(TypedWritableReferenceCount, Namable):
    """A basic node of the scene graph or data graph.  This is the base class of
    all specialized nodes, and also serves as a generic node with no special
    properties.
    """

    class Children:
        """This class is returned from get_children().  Use it to walk through the
        list of children.  This is faster, and safer, than walking through the
        children one at a time via get_num_children()/get_child(), since the list
        of children is saved out ahead of time, rather than having to reacquire
        the lock with each iteration, or to keep the lock held for the entire
        pass.
        """

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __getitem__(self, n: int) -> PandaNode: ...
        def __len__(self) -> int: ...
        def __iter__(self) -> Iterator[PandaNode]: ...  # Doesn't actually exist

    class Stashed:
        """Similarly for stashed children."""

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __getitem__(self, n: int) -> PandaNode: ...
        def __len__(self) -> int: ...
        def __iter__(self) -> Iterator[PandaNode]: ...  # Doesn't actually exist

    class Parents:
        """This class is returned from get_parents()."""

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __getitem__(self, n: int) -> PandaNode: ...
        def __len__(self) -> int: ...
        def __iter__(self) -> Iterator[PandaNode]: ...  # Doesn't actually exist

    UC_parents: Final = 1
    UCParents: Final = 1
    UC_children: Final = 2
    UCChildren: Final = 2
    UC_transform: Final = 4
    UCTransform: Final = 4
    UC_state: Final = 8
    UCState: Final = 8
    UC_draw_mask: Final = 16
    UCDrawMask: Final = 16
    FB_transform: Final = 1
    FBTransform: Final = 1
    FB_state: Final = 2
    FBState: Final = 2
    FB_effects: Final = 4
    FBEffects: Final = 4
    FB_tag: Final = 16
    FBTag: Final = 16
    FB_draw_mask: Final = 32
    FBDrawMask: Final = 32
    FB_cull_callback: Final = 64
    FBCullCallback: Final = 64
    state: RenderState
    effects: RenderEffects
    transform: TransformState
    overall_hidden: bool
    into_collide_mask: CollideMask
    bounds_type: _BoundingVolume_BoundsType
    final: bool
    @property
    def prev_transform(self) -> TransformState: ...
    @property
    def tags(self) -> MutableMapping[str, str]: ...
    @property
    def python_tags(self) -> dict[Any, Any]: ...
    @property
    def overall_bit(self) -> DrawMask: ...
    @property
    def all_camera_mask(self) -> DrawMask: ...
    @property
    def draw_control_mask(self) -> DrawMask: ...
    @property
    def draw_show_mask(self) -> DrawMask: ...
    @property
    def legal_collide_mask(self) -> CollideMask: ...
    @property
    def nested_vertices(self) -> int: ...
    @property
    def internal_bounds(self) -> BoundingVolume: ...
    @property
    def internal_vertices(self) -> int: ...
    @property
    def bounds_stale(self) -> bool: ...
    @property
    def children(self) -> PandaNode.Children: ...
    @property
    def stashed(self) -> PandaNode.Stashed: ...
    @property
    def parents(self) -> PandaNode.Parents: ...
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> PandaNode: ...
    def __deepcopy__(self, memo): ...
    def upcast_to_TypedWritableReferenceCount(self) -> TypedWritableReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def combine_with(self, other: PandaNode) -> PandaNode:
        """Collapses this PandaNode with the other PandaNode, if possible, and returns
        a pointer to the combined PandaNode, or NULL if the two PandaNodes cannot
        safely be combined.

        The return value may be this, other, or a new PandaNode altogether.

        This function is called from GraphReducer::flatten(), and need not deal
        with children; its job is just to decide whether to collapse the two
        PandaNodes and what the collapsed PandaNode should look like.
        """
    def make_copy(self) -> PandaNode:
        """Returns a newly-allocated PandaNode that is a shallow copy of this one.  It
        will be a different pointer, but its internal data may or may not be shared
        with that of the original PandaNode.  No children will be copied.
        """
    def copy_subgraph(self, current_thread: Thread = ...) -> PandaNode:
        """Allocates and returns a complete copy of this PandaNode and the entire
        scene graph rooted at this PandaNode.  Some data may still be shared from
        the original (e.g.  vertex index tables), but nothing that will impede
        normal use of the PandaNode.
        """
    def get_num_parents(self, current_thread: Thread = ...) -> int:
        """Returns the number of parent nodes this node has.  If this number is
        greater than 1, the node has been multiply instanced.  The order of the
        parent nodes is not meaningful and is not related to the order in which the
        node was instanced to them.
        """
    def get_parent(self, n: int, current_thread: Thread = ...) -> PandaNode:
        """Returns the nth parent node of this node.  See get_num_parents().  Also see
        get_parents(), if your intention is to iterate through the complete list of
        parents; get_parents() is preferable in this case.
        """
    def find_parent(self, node: PandaNode, current_thread: Thread = ...) -> int:
        """Returns the index of the indicated parent node, if it is a parent, or -1 if
        it is not.
        """
    def get_num_children(self, current_thread: Thread = ...) -> int:
        """Returns the number of child nodes this node has.  The order of the child
        nodes *is* meaningful and is based on the sort number that was passed to
        add_child(), and also on the order in which the nodes were added.
        """
    def get_child(self, n: int, current_thread: Thread = ...) -> PandaNode:
        """Returns the nth child node of this node.  See get_num_children().  Also see
        get_children(), if your intention is to iterate through the complete list
        of children; get_children() is preferable in this case.
        """
    def get_child_sort(self, n: int, current_thread: Thread = ...) -> int:
        """Returns the sort index of the nth child node of this node (that is, the
        number that was passed to add_child()).  See get_num_children().
        """
    def find_child(self, node: PandaNode, current_thread: Thread = ...) -> int:
        """Returns the index of the indicated child node, if it is a child, or -1 if
        it is not.
        """
    def count_num_descendants(self) -> int:
        """Returns the number of nodes at and below this level."""
    def add_child(self, child_node: PandaNode, sort: int = ..., current_thread: Thread = ...) -> None:
        """Adds a new child to the node.  The child is added in the relative position
        indicated by sort; if all children have the same sort index, the child is
        added at the end.

        If the same child is added to a node more than once, the previous instance
        is first removed.
        """
    @overload
    def remove_child(self, child_node: PandaNode, current_thread: Thread = ...) -> bool:
        """`(self, child_node: PandaNode, current_thread: Thread = ...)`:
        Removes the indicated child from the node.  Returns true if the child was
        removed, false if it was not already a child of the node.  This will also
        successfully remove the child if it had been stashed.

        `(self, child_index: int, current_thread: Thread = ...)`:
        Removes the nth child from the node.
        """
    @overload
    def remove_child(self, child_index: int, current_thread: Thread = ...) -> None: ...
    def replace_child(self, orig_child: PandaNode, new_child: PandaNode, current_thread: Thread = ...) -> bool:
        """Searches for the orig_child node in the node's list of children, and
        replaces it with the new_child instead.  Returns true if the replacement is
        made, or false if the node is not a child or if there is some other
        problem.
        """
    @overload
    def stash_child(self, child_node: PandaNode, current_thread: Thread = ...) -> bool:
        """`(self, child_node: PandaNode, current_thread: Thread = ...)`:
        Stashes the indicated child node.  This removes the child from the list of
        active children and puts it on a special list of stashed children.  This
        child node no longer contributes to the bounding volume of the PandaNode,
        and is not visited in normal traversals.  It is invisible and uncollidable.
        The child may later be restored by calling unstash_child().

        This function returns true if the child node was successfully stashed, or
        false if it was not a child of the node in the first place (e.g.  it was
        previously stashed).

        `(self, child_index: int, current_thread: Thread = ...)`:
        Stashes the indicated child node.  This removes the child from the list of
        active children and puts it on a special list of stashed children.  This
        child node no longer contributes to the bounding volume of the PandaNode,
        and is not visited in normal traversals.  It is invisible and uncollidable.
        The child may later be restored by calling unstash_child().

        This can only be called from the top pipeline stage (i.e.  from App).
        """
    @overload
    def stash_child(self, child_index: int, current_thread: Thread = ...) -> None: ...
    @overload
    def unstash_child(self, child_node: PandaNode, current_thread: Thread = ...) -> bool:
        """`(self, child_node: PandaNode, current_thread: Thread = ...)`:
        Returns the indicated stashed node to normal child status.  This removes
        the child from the list of stashed children and puts it on the normal list
        of active children.  This child node once again contributes to the bounding
        volume of the PandaNode, and will be visited in normal traversals.  It is
        visible and collidable.

        This function returns true if the child node was successfully stashed, or
        false if it was not a child of the node in the first place (e.g.  it was
        previously stashed).

        `(self, stashed_index: int, current_thread: Thread = ...)`:
        Returns the indicated stashed node to normal child status.  This removes
        the child from the list of stashed children and puts it on the normal list
        of active children.  This child node once again contributes to the bounding
        volume of the PandaNode, and will be visited in normal traversals.  It is
        visible and collidable.

        This can only be called from the top pipeline stage (i.e.  from App).
        """
    @overload
    def unstash_child(self, stashed_index: int, current_thread: Thread = ...) -> None: ...
    def get_num_stashed(self, current_thread: Thread = ...) -> int:
        """Returns the number of stashed nodes this node has.  These are former
        children of the node that have been moved to the special stashed list via
        stash_child().
        """
    @overload
    def get_stashed(self, current_thread: Thread = ...) -> PandaNode.Stashed:
        """`(self, current_thread: Thread = ...)`:
        Returns an object that can be used to walk through the list of children of
        the node.  When you intend to visit multiple children, using this is
        slightly faster than calling get_stashed() directly on the PandaNode, since
        this object avoids reopening the PipelineCycler each time.

        This object also protects you from self-modifying loops (e.g.  adding or
        removing children during traversal), since a virtual copy of the children
        is made ahead of time.  The virtual copy is fast--it is a form of copy-on-
        write, so the list is not actually copied unless it is modified during the
        traversal.

        `(self, n: int, current_thread: Thread = ...)`:
        Returns the nth stashed child of this node.  See get_num_stashed().  Also
        see get_stashed(), if your intention is to iterate through the complete
        list of stashed children; get_stashed() is preferable in this case.
        """
    @overload
    def get_stashed(self, n: int, current_thread: Thread = ...) -> PandaNode: ...
    def get_stashed_sort(self, n: int, current_thread: Thread = ...) -> int:
        """Returns the sort index of the nth stashed node of this node (that is, the
        number that was passed to add_child()).  See get_num_stashed().
        """
    def find_stashed(self, node: PandaNode, current_thread: Thread = ...) -> int:
        """Returns the index of the indicated stashed node, if it is a stashed child,
        or -1 if it is not.
        """
    def add_stashed(self, child_node: PandaNode, sort: int = ..., current_thread: Thread = ...) -> None:
        """Adds a new child to the node, directly as a stashed child.  The child is
        not added in the normal sense, but will be revealed if unstash_child() is
        called on it later.

        If the same child is added to a node more than once, the previous instance
        is first removed.

        This can only be called from the top pipeline stage (i.e.  from App).
        """
    def remove_stashed(self, child_index: int, current_thread: Thread = ...) -> None:
        """Removes the nth stashed child from the node."""
    def remove_all_children(self, current_thread: Thread = ...) -> None:
        """Removes all the children from the node at once, including stashed children.

        This can only be called from the top pipeline stage (i.e.  from App).
        """
    def steal_children(self, other: PandaNode, current_thread: Thread = ...) -> None:
        """Moves all the children from the other node onto this node.

        Any NodePaths to child nodes of the other node are truncated, rather than
        moved to the new parent.
        """
    def copy_children(self, other: PandaNode, current_thread: Thread = ...) -> None:
        """Makes another instance of all the children of the other node, copying them
        to this node.
        """
    def set_attrib(self, attrib: RenderAttrib, override: int = ...) -> None:
        """Adds the indicated render attribute to the scene graph on this node.  This
        attribute will now apply to this node and everything below.  If there was
        already an attribute of the same type, it is replaced.
        """
    @overload
    def get_attrib(self, type: TypeHandle | type) -> RenderAttrib:
        """Returns the render attribute of the indicated type, if it is defined on the
        node, or NULL if it is not.  This checks only what is set on this
        particular node level, and has nothing to do with what render attributes
        may be inherited from parent nodes.
        """
    @overload
    def get_attrib(self, slot: int) -> RenderAttrib: ...
    @overload
    def has_attrib(self, type: TypeHandle | type) -> bool:
        """Returns true if there is a render attribute of the indicated type defined
        on this node, or false if there is not.
        """
    @overload
    def has_attrib(self, slot: int) -> bool: ...
    @overload
    def clear_attrib(self, type: TypeHandle | type) -> None:
        """Removes the render attribute of the given type from this node.  This node,
        and the subgraph below, will now inherit the indicated render attribute
        from the nodes above this one.
        """
    @overload
    def clear_attrib(self, slot: int) -> None: ...
    def set_effect(self, effect: RenderEffect) -> None:
        """Adds the indicated render effect to the scene graph on this node.  If there
        was already an effect of the same type, it is replaced.
        """
    def get_effect(self, type: TypeHandle | type) -> RenderEffect:
        """Returns the render effect of the indicated type, if it is defined on the
        node, or NULL if it is not.
        """
    def has_effect(self, type: TypeHandle | type) -> bool:
        """Returns true if there is a render effect of the indicated type defined on
        this node, or false if there is not.
        """
    def clear_effect(self, type: TypeHandle | type) -> None:
        """Removes the render effect of the given type from this node."""
    def set_state(self, state: RenderState, current_thread: Thread = ...) -> None:
        """Sets the complete RenderState that will be applied to all nodes at this
        level and below.  (The actual state that will be applied to lower nodes is
        based on the composition of RenderStates from above this node as well).
        This completely replaces whatever has been set on this node via repeated
        calls to set_attrib().
        """
    def get_state(self, current_thread: Thread = ...) -> RenderState:
        """Returns the complete RenderState that will be applied to all nodes at this
        level and below, as set on this node.  This returns only the RenderState
        set on this particular node, and has nothing to do with state that might be
        inherited from above.
        """
    def clear_state(self, current_thread: Thread = ...) -> None:
        """Resets this node to leave the render state alone.  Nodes at this level and
        below will once again inherit their render state unchanged from the nodes
        above this level.
        """
    def set_effects(self, effects: RenderEffect | RenderEffects, current_thread: Thread = ...) -> None:
        """Sets the complete RenderEffects that will be applied this node.  This
        completely replaces whatever has been set on this node via repeated calls
        to set_attrib().
        """
    def get_effects(self, current_thread: Thread = ...) -> RenderEffects:
        """Returns the complete RenderEffects that will be applied to this node."""
    def clear_effects(self, current_thread: Thread = ...) -> None:
        """Resets this node to have no render effects."""
    def set_transform(self, transform: TransformState, current_thread: Thread = ...) -> None:
        """Sets the transform that will be applied to this node and below.  This
        defines a new coordinate space at this point in the scene graph and below.
        """
    def get_transform(self, current_thread: Thread = ...) -> TransformState:
        """Returns the transform that has been set on this particular node.  This is
        not the net transform from the root, but simply the transform on this
        particular node.
        """
    def clear_transform(self, current_thread: Thread = ...) -> None:
        """Resets the transform on this node to the identity transform."""
    def set_prev_transform(self, transform: TransformState, current_thread: Thread = ...) -> None:
        """Sets the transform that represents this node's "previous" position, one
        frame ago, for the purposes of detecting motion for accurate collision
        calculations.
        """
    def get_prev_transform(self, current_thread: Thread = ...) -> TransformState:
        """Returns the transform that has been set as this node's "previous" position.
        See set_prev_transform().
        """
    def reset_prev_transform(self, current_thread: Thread = ...) -> None:
        """Resets the transform that represents this node's "previous" position to the
        same as the current transform.  This is not the same thing as clearing it
        to identity.
        """
    def has_dirty_prev_transform(self) -> bool:
        """Returns true if this node has the _dirty_prev_transform flag set, which
        indicates its _prev_transform is different from its _transform value (in
        pipeline stage 0).  In this case, the node will be visited by
        reset_prev_transform().
        """
    @staticmethod
    def reset_all_prev_transform(current_thread: Thread = ...) -> None:
        """Visits all nodes in the world with the _dirty_prev_transform flag--that is,
        all nodes whose _prev_transform is different from the _transform in
        pipeline stage 0--and resets the _prev_transform to be the same as
        _transform.
        """
    def set_tag(self, key: str, value: str, current_thread: Thread = ...) -> None:
        """Associates a user-defined value with a user-defined key which is stored on
        the node.  This value has no meaning to Panda; but it is stored
        indefinitely on the node until it is requested again.

        Each unique key stores a different string value.  There is no effective
        limit on the number of different keys that may be stored or on the length
        of any one key's value.
        """
    def get_tag(self, key: str, current_thread: Thread = ...) -> str:
        """Retrieves the user-defined value that was previously set on this node for
        the particular key, if any.  If no value has been previously set, returns
        the empty string.
        """
    def has_tag(self, key: str, current_thread: Thread = ...) -> bool:
        """Returns true if a value has been defined on this node for the particular
        key (even if that value is the empty string), or false if no value has been
        set.
        """
    def clear_tag(self, key: str, current_thread: Thread = ...) -> None:
        """Removes the value defined for this key on this particular node.  After a
        call to clear_tag(), has_tag() will return false for the indicated key.
        """
    def get_tag_keys(self) -> tuple[str, ...]: ...
    def get_python_tags(self) -> dict[Any, Any]: ...
    def set_python_tag(self, key: Any, value: Any) -> None: ...
    def get_python_tag(self, key: Any) -> Any | None: ...
    def has_python_tag(self, key: Any) -> bool: ...
    def clear_python_tag(self, key: Any) -> None: ...
    def get_python_tag_keys(self) -> list[Any] | tuple[()]: ...
    def has_tags(self) -> bool:
        """Returns true if the node has any tags (or any Python tags) at all, false if
        it has none.
        """
    def copy_tags(self, other: PandaNode) -> None:
        """Copies all of the tags stored on the other node onto this node.  If a
        particular tag exists on both nodes, the contents of this node's value is
        replaced by that of the other.
        """
    def list_tags(self, out: ostream, separator: str = ...) -> None:
        """Writes a list of all the tag keys assigned to the node to the indicated
        stream.  Writes one instance of the separator following each key (but does
        not write a terminal separator).  The value associated with each key is not
        written.

        This is mainly for the benefit of the realtime user, to see the list of all
        of the associated tag keys.
        """
    def compare_tags(self, other: PandaNode) -> int:
        """Returns a number less than 0, 0, or greater than 0, to indicate the
        similarity of tags between this node and the other one.  If this returns 0,
        the tags are identical.  If it returns other than 0, then the tags are
        different; and the nodes may be sorted into a consistent (but arbitrary)
        ordering based on this number.
        """
    def copy_all_properties(self, other: PandaNode) -> None:
        """Copies the TransformState, RenderState, RenderEffects, tags, Python tags,
        and the show/hide state from the other node onto this one.  Typically this
        is used to prepare a node to replace another node in the scene graph (also
        see replace_node()).
        """
    def replace_node(self, other: PandaNode) -> None:
        """Inserts this node into the scene graph in place of the other one, and
        removes the other node.  All scene graph attributes (TransformState,
        RenderState, etc.) are copied to this node.

        All children are moved to this node, and removed from the old node.  The
        new node is left in the same place in the old node's parent's list of
        children.

        Even NodePaths that reference the old node are updated in-place to
        reference the new node instead.

        This method is intended to be used to replace a node of a given type in the
        scene graph with a node of a different type.
        """
    def set_unexpected_change(self, flags: int) -> None:
        """Sets one or more of the PandaNode::UnexpectedChange bits on, indicating
        that the corresponding property should not change again on this node.  Once
        one of these bits has been set, if the property changes, an assertion
        failure will be raised, which is designed to assist the developer in
        identifying the troublesome code that modified the property unexpectedly.

        The input parameter is the union of bits that are to be set.  To clear
        these bits later, use clear_unexpected_change().

        Since this is a developer debugging tool only, this function does nothing
        in a production (NDEBUG) build.
        """
    def get_unexpected_change(self, flags: int) -> int:
        """Returns nonzero if any of the bits in the input parameter are set on this
        node, or zero if none of them are set.  More specifically, this returns the
        particular set of bits (masked by the input parameter) that have been set
        on this node.  See set_unexpected_change().

        Since this is a developer debugging tool only, this function always returns
        zero in a production (NDEBUG) build.
        """
    def clear_unexpected_change(self, flags: int) -> None:
        """Sets one or more of the PandaNode::UnexpectedChange bits off, indicating
        that the corresponding property may once again change on this node.  See
        set_unexpected_change().

        The input parameter is the union of bits that are to be cleared.

        Since this is a developer debugging tool only, this function does nothing
        in a production (NDEBUG) build.
        """
    @staticmethod
    def get_overall_bit() -> DrawMask:
        """Returns the special bit that, when specifically cleared in the node's
        DrawMask, indicates that the node is hidden to all cameras, regardless of
        the remaining DrawMask bits.
        """
    @staticmethod
    def get_all_camera_mask() -> DrawMask:
        """Returns a DrawMask that is appropriate for rendering to all cameras."""
    def is_overall_hidden(self) -> bool:
        """Returns true if the node has been hidden to all cameras by clearing its
        overall bit.
        """
    def set_overall_hidden(self, overall_hidden: bool) -> None:
        """Sets or clears the hidden flag.  When the hidden flag is true, the node and
        all of its children are invisible to all cameras, regardless of the setting
        of any draw masks.  Setting the hidden flag to false restores the previous
        visibility as established by the draw masks.

        This actually works by twiddling the reserved _overall_bit in the node's
        draw mask, which has special meaning.
        """
    def adjust_draw_mask(self, show_mask: DrawMask | int, hide_mask: DrawMask | int, clear_mask: DrawMask | int) -> None:
        """Adjusts the hide/show bits of this particular node.

        These three parameters can be used to adjust the _draw_control_mask and
        _draw_show_mask independently, which work together to provide per-camera
        visibility for the node and its descendents.

        _draw_control_mask indicates the bits in _draw_show_mask that are
        significant.  Each different bit corresponds to a different camera (and
        these bits are assigned via Camera::set_camera_mask()).

        Where _draw_control_mask has a 1 bit, a 1 bit in _draw_show_mask indicates
        the node is visible to that camera, and a 0 bit indicates the node is
        hidden to that camera.  Where _draw_control_mask is 0, the node is hidden
        only if a parent node is hidden.

        The meaning of the three parameters is as follows:

        * Wherever show_mask is 1, _draw_show_mask and _draw_control_mask will be
        set 1.  Thus, show_mask indicates the set of cameras to which the node
        should be shown.

        * Wherever hide_mask is 1, _draw_show_mask will be set 0 and
        _draw_control_mask will be set 1.  Thus, hide_mask indicates the set of
        cameras from which the node should be hidden.

        * Wherever clear_mask is 1, _draw_control_mask will be set 0.  Thus,
        clear_mask indicates the set of cameras from which the hidden state should
        be inherited from a parent.
        """
    def get_draw_control_mask(self) -> DrawMask:
        """Returns the set of bits in draw_show_mask that are considered meaningful.
        See adjust_draw_mask().
        """
    def get_draw_show_mask(self) -> DrawMask:
        """Returns the hide/show bits of this particular node.  See
        adjust_draw_mask().
        """
    def get_net_draw_control_mask(self) -> DrawMask:
        """Returns the set of bits in get_net_draw_show_mask() that have been
        explicitly set via adjust_draw_mask(), rather than implicitly inherited.

        A 1 bit in any position of this mask indicates that (a) this node has
        renderable children, and (b) some child of this node has made an explicit
        hide() or show_through() call for the corresponding bit.
        """
    def get_net_draw_show_mask(self) -> DrawMask:
        """Returns the union of all draw_show_mask values--of renderable nodes only--
        at this level and below.  If any bit in this mask is 0, there is no reason
        to traverse below this node for a camera with the corresponding
        camera_mask.

        The bits in this mask that do not correspond to a 1 bit in the
        net_draw_control_mask are meaningless (and will be set to 1).  For bits
        that *do* correspond to a 1 bit in the net_draw_control_mask, a 1 bit
        indicates that at least one child should be visible, while a 0 bit
        indicates that all children are hidden.
        """
    def set_into_collide_mask(self, mask: CollideMask | int) -> None:
        """Sets the "into" CollideMask.

        This specifies the set of bits that must be shared with a CollisionNode's
        "from" CollideMask in order for the CollisionNode to detect a collision
        with this particular node.

        The actual CollideMask that will be set is masked by the return value from
        get_legal_collide_mask(). Thus, the into_collide_mask cannot be set to
        anything other than nonzero except for those types of nodes that can be
        collided into, such as CollisionNodes and GeomNodes.
        """
    def get_into_collide_mask(self) -> CollideMask:
        """Returns the "into" collide mask for this node."""
    def get_legal_collide_mask(self) -> CollideMask:
        """Returns the subset of CollideMask bits that may be set for this particular
        type of PandaNode.  For most nodes, this is 0; it doesn't make sense to set
        a CollideMask for most kinds of nodes.

        For nodes that can be collided with, such as GeomNode and CollisionNode,
        this returns all bits on.
        """
    def get_net_collide_mask(self, current_thread: Thread = ...) -> CollideMask:
        """Returns the union of all into_collide_mask() values set at CollisionNodes
        at this level and below.
        """
    def get_off_clip_planes(self, current_thread: Thread = ...) -> RenderAttrib:
        """Returns a ClipPlaneAttrib which represents the union of all of the clip
        planes that have been turned *off* at this level and below.
        """
    def prepare_scene(self, gsg: GraphicsStateGuardianBase, node_state: RenderState) -> None:
        """Walks through the scene graph beginning at this node, and does whatever
        initialization is required to render the scene properly with the indicated
        GSG.  It is not strictly necessary to call this, since the GSG will
        initialize itself when the scene is rendered, but this may take some of the
        overhead away from that process.

        In particular, this will ensure that textures and vertex buffers within the
        scene are loaded into graphics memory.
        """
    def is_scene_root(self) -> bool:
        """Returns true if this particular node is known to be the render root of some
        active DisplayRegion associated with the global GraphicsEngine, false
        otherwise.
        """
    def is_under_scene_root(self) -> bool:
        """Returns true if this particular node is in a live scene graph: that is, it
        is a child or descendent of a node that is itself a scene root.  If this is
        true, this node may potentially be traversed by the render traverser.
        Stashed nodes don't count for this purpose, but hidden nodes do.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    def ls(self, out: ostream, indent_level: int) -> None:
        """Lists all the nodes at and below the current path hierarchically."""
    def set_bounds_type(self, bounds_type: _BoundingVolume_BoundsType) -> None:
        """Specifies the desired type of bounding volume that will be created for this
        node.  This is normally BoundingVolume::BT_default, which means to set the
        type according to the config variable "bounds-type".

        If this is BT_sphere or BT_box, a BoundingSphere or BoundingBox is
        explicitly created.  If it is BT_best, the appropriate type to best enclose
        the node's children is created.

        This affects the bounding volume returned by get_bounds(), which is not
        exactly the same bounding volume modified by set_bounds(), because a new
        bounding volume has to be created that includes this node and all of its
        children.
        """
    def get_bounds_type(self) -> _BoundingVolume_BoundsType:
        """Returns the bounding volume type set with set_bounds_type()."""
    def set_bounds(self, volume: BoundingVolume) -> None:
        """Resets the bounding volume so that it is the indicated volume.  When it is
        explicitly set, the bounding volume will no longer be automatically
        computed according to the contents of the node itself, for nodes like
        GeomNodes and TextNodes that contain substance (but the bounding volume
        will still be automatically expanded to include its children).

        Call clear_bounds() if you would like to return the bounding volume to its
        default behavior later.
        """
    def set_bound(self, volume: BoundingVolume) -> None:
        """@deprecated Use set_bounds() instead."""
    def clear_bounds(self) -> None:
        """Reverses the effect of a previous call to set_bounds(), and allows the
        node's bounding volume to be automatically computed once more based on the
        contents of the node.
        """
    @overload
    def get_bounds(self, current_thread: Thread = ...) -> BoundingVolume:
        """`(self, current_thread: Thread = ...)`:
        Returns the external bounding volume of this node: a bounding volume that
        contains the user bounding volume, the internal bounding volume, and all of
        the children's bounding volumes.

        `(self, seq: UpdateSeq, current_thread: Thread = ...)`:
        This flavor of get_bounds() return the external bounding volume, and also
        fills in seq with the bounding volume's current sequence number.  When this
        sequence number changes, it indicates that the bounding volume might have
        changed, e.g.  because some nested child's bounding volume has changed.

        Although this might occasionally increment without changing the bounding
        volume, the bounding volume will never change without incrementing this
        counter, so as long as this counter remains unchanged you can be confident
        the bounding volume is also unchanged.
        """
    @overload
    def get_bounds(self, seq: UpdateSeq, current_thread: Thread = ...) -> BoundingVolume: ...
    def get_nested_vertices(self, current_thread: Thread = ...) -> int:
        """Returns the total number of vertices that will be rendered by this node and
        all of its descendents.

        This is not necessarily an accurate count of vertices that will actually be
        rendered, since this will include all vertices of all LOD's, and it will
        also include hidden nodes.  It may also omit or only approximate certain
        kinds of dynamic geometry.  However, it will not include stashed nodes.
        """
    def get_internal_bounds(self, current_thread: Thread = ...) -> BoundingVolume:
        """Returns the node's internal bounding volume.  This is the bounding volume
        around the node alone, without including children.  If the user has called
        set_bounds(), it will be the specified bounding volume.
        """
    def get_internal_vertices(self, current_thread: Thread = ...) -> int:
        """Returns the total number of vertices that will be rendered by this
        particular node alone, not accounting for its children.

        This may not include all vertices for certain dynamic effects.
        """
    def mark_bounds_stale(self, current_thread: Thread = ...) -> None:
        """Indicates that the bounding volume, or something that influences the
        bounding volume (or any of the other things stored in CData, like
        net_collide_mask), may have changed for this node, and that it must be
        recomputed.

        With no parameters, this means to iterate through all stages including and
        upstream of the current pipeline stage.

        This method is intended for internal use; usually it is not necessary for a
        user to call this directly.  It will be called automatically by derived
        classes when appropriate.
        """
    def mark_internal_bounds_stale(self, current_thread: Thread = ...) -> None:
        """Should be called by a derived class to mark the internal bounding volume
        stale, so that compute_internal_bounds() will be called when the bounding
        volume is next requested.

        With no parameters, this means to iterate through all stages including and
        upstream of the current pipeline stage.

        It is normally not necessary to call this method directly; each node should
        be responsible for calling it when its internals have changed.
        """
    def is_bounds_stale(self) -> bool:
        """Returns true if the bounding volume of this node is stale and will be
        implicitly recomputed at the next call to get_bounds(), or false if it is
        fresh and need not be recomputed.
        """
    def set_final(self, flag: bool) -> None:
        """Sets the "final" flag on this PandaNode.  If this is true, than no bounding
        volume need be tested below it; a positive intersection with this node's
        bounding volume is deemed to be a positive intersection with all geometry
        inside.

        This is useful to quickly force a larger bounding volume around a node when
        the GeomNodes themselves are inaccurate for some reason, without forcing a
        recompute of every nested bounding volume.  It's also helpful when the
        bounding volume is tricked by some special properties, like billboards,
        that may move geometry out of its bounding volume otherwise.
        """
    def is_final(self, current_thread: Thread = ...) -> bool:
        """Returns the current state of the "final" flag.  Initially, this flag is off
        (false), but it may be changed by an explicit call to set_final().  See
        set_final().
        """
    def is_geom_node(self) -> bool:
        """A simple downcast check.  Returns true if this kind of node happens to
        inherit from GeomNode, false otherwise.

        This is provided as a a faster alternative to calling
        is_of_type(GeomNode::get_class_type()), since this test is so important to
        rendering.
        """
    def is_lod_node(self) -> bool:
        """A simple downcast check.  Returns true if this kind of node happens to
        inherit from LODNode, false otherwise.

        This is provided as a a faster alternative to calling
        is_of_type(LODNode::get_class_type()).
        """
    def is_collision_node(self) -> bool:
        """A simple downcast check.  Returns true if this kind of node happens to
        inherit from CollisionNode, false otherwise.

        This is provided as a a faster alternative to calling
        is_of_type(CollisionNode::get_class_type()).
        """
    def as_light(self) -> Light:
        """Cross-casts the node to a Light pointer, if it is one of the four kinds of
        Light nodes, or returns NULL if it is not.
        """
    def is_ambient_light(self) -> bool:
        """Returns true if this is an AmbientLight, false if it is not a light, or it
        is some other kind of light.
        """
    def get_fancy_bits(self, current_thread: Thread = ...) -> int:
        """Returns the union of all of the enum FancyBits values corresponding to the
        various "fancy" attributes that are set on the node.  If this returns 0,
        the node has nothing interesting about it.  This is intended to speed
        traversal by quickly skipping past nodes that don't particularly affect the
        render state.
        """
    @staticmethod
    def decode_from_bam_stream(data: bytes, reader: BamReader = ...) -> PandaNode:
        """Reads the bytes created by a previous call to encode_to_bam_stream(), and
        extracts and returns the single object on those bytes.  Returns NULL on
        error.

        This method is intended to replace decode_raw_from_bam_stream() when you
        know the stream in question returns an object of type PandaNode, allowing
        for easier reference count management.  Note that the caller is still
        responsible for maintaining the reference count on the return value.
        """
    def get_parents(self) -> tuple[PandaNode, ...]: ...
    def get_children(self) -> tuple[PandaNode, ...]: ...
    upcastToTypedWritableReferenceCount = upcast_to_TypedWritableReferenceCount
    upcastToNamable = upcast_to_Namable
    combineWith = combine_with
    makeCopy = make_copy
    copySubgraph = copy_subgraph
    getNumParents = get_num_parents
    getParent = get_parent
    findParent = find_parent
    getNumChildren = get_num_children
    getChild = get_child
    getChildSort = get_child_sort
    findChild = find_child
    countNumDescendants = count_num_descendants
    addChild = add_child
    removeChild = remove_child
    replaceChild = replace_child
    stashChild = stash_child
    unstashChild = unstash_child
    getNumStashed = get_num_stashed
    getStashed = get_stashed
    getStashedSort = get_stashed_sort
    findStashed = find_stashed
    addStashed = add_stashed
    removeStashed = remove_stashed
    removeAllChildren = remove_all_children
    stealChildren = steal_children
    copyChildren = copy_children
    setAttrib = set_attrib
    getAttrib = get_attrib
    hasAttrib = has_attrib
    clearAttrib = clear_attrib
    setEffect = set_effect
    getEffect = get_effect
    hasEffect = has_effect
    clearEffect = clear_effect
    setState = set_state
    getState = get_state
    clearState = clear_state
    setEffects = set_effects
    getEffects = get_effects
    clearEffects = clear_effects
    setTransform = set_transform
    getTransform = get_transform
    clearTransform = clear_transform
    setPrevTransform = set_prev_transform
    getPrevTransform = get_prev_transform
    resetPrevTransform = reset_prev_transform
    hasDirtyPrevTransform = has_dirty_prev_transform
    resetAllPrevTransform = reset_all_prev_transform
    setTag = set_tag
    getTag = get_tag
    hasTag = has_tag
    clearTag = clear_tag
    getTagKeys = get_tag_keys
    getPythonTags = get_python_tags
    setPythonTag = set_python_tag
    getPythonTag = get_python_tag
    hasPythonTag = has_python_tag
    clearPythonTag = clear_python_tag
    getPythonTagKeys = get_python_tag_keys
    hasTags = has_tags
    copyTags = copy_tags
    listTags = list_tags
    compareTags = compare_tags
    copyAllProperties = copy_all_properties
    replaceNode = replace_node
    setUnexpectedChange = set_unexpected_change
    getUnexpectedChange = get_unexpected_change
    clearUnexpectedChange = clear_unexpected_change
    getOverallBit = get_overall_bit
    getAllCameraMask = get_all_camera_mask
    isOverallHidden = is_overall_hidden
    setOverallHidden = set_overall_hidden
    adjustDrawMask = adjust_draw_mask
    getDrawControlMask = get_draw_control_mask
    getDrawShowMask = get_draw_show_mask
    getNetDrawControlMask = get_net_draw_control_mask
    getNetDrawShowMask = get_net_draw_show_mask
    setIntoCollideMask = set_into_collide_mask
    getIntoCollideMask = get_into_collide_mask
    getLegalCollideMask = get_legal_collide_mask
    getNetCollideMask = get_net_collide_mask
    getOffClipPlanes = get_off_clip_planes
    prepareScene = prepare_scene
    isSceneRoot = is_scene_root
    isUnderSceneRoot = is_under_scene_root
    setBoundsType = set_bounds_type
    getBoundsType = get_bounds_type
    setBounds = set_bounds
    setBound = set_bound
    clearBounds = clear_bounds
    getBounds = get_bounds
    getNestedVertices = get_nested_vertices
    getInternalBounds = get_internal_bounds
    getInternalVertices = get_internal_vertices
    markBoundsStale = mark_bounds_stale
    markInternalBoundsStale = mark_internal_bounds_stale
    isBoundsStale = is_bounds_stale
    setFinal = set_final
    isFinal = is_final
    isGeomNode = is_geom_node
    isLodNode = is_lod_node
    isCollisionNode = is_collision_node
    asLight = as_light
    isAmbientLight = is_ambient_light
    getFancyBits = get_fancy_bits
    decodeFromBamStream = decode_from_bam_stream
    getParents = get_parents
    getChildren = get_children

class TransparencyAttrib(RenderAttrib):
    """This controls the enabling of transparency.  Simply setting an alpha
    component to non-1 does not in itself make an object transparent; you must
    also enable transparency mode with a suitable TransparencyAttrib.
    Similarly, it is wasteful to render an object with a TransparencyAttrib in
    effect unless you actually want it to be at least partially transparent
    (and it has alpha components less than 1).
    """

    M_alpha: Final = 1
    MAlpha: Final = 1
    M_premultiplied_alpha: Final = 2
    MPremultipliedAlpha: Final = 2
    M_multisample: Final = 3
    MMultisample: Final = 3
    M_multisample_mask: Final = 4
    MMultisampleMask: Final = 4
    M_binary: Final = 5
    MBinary: Final = 5
    M_dual: Final = 6
    MDual: Final = 6
    @property
    def mode(self) -> _TransparencyAttrib_Mode: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _TransparencyAttrib_Mode) -> RenderAttrib:
        """Constructs a new TransparencyAttrib object."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> _TransparencyAttrib_Mode:
        """Returns the transparency mode."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getClassSlot = get_class_slot

class LogicOpAttrib(RenderAttrib):
    """If enabled, specifies that a custom logical operation be performed instead
    of any color blending.  Setting it to a value other than M_none will cause
    color blending to be disabled and the given logic operation to be performed.

    @since 1.10.0
    """

    O_none: Final = 0
    ONone: Final = 0
    O_clear: Final = 1
    OClear: Final = 1
    O_and: Final = 2
    OAnd: Final = 2
    O_and_reverse: Final = 3
    OAndReverse: Final = 3
    O_copy: Final = 4
    OCopy: Final = 4
    O_and_inverted: Final = 5
    OAndInverted: Final = 5
    O_noop: Final = 6
    ONoop: Final = 6
    O_xor: Final = 7
    OXor: Final = 7
    O_or: Final = 8
    OOr: Final = 8
    O_nor: Final = 9
    ONor: Final = 9
    O_equivalent: Final = 10
    OEquivalent: Final = 10
    O_invert: Final = 11
    OInvert: Final = 11
    O_or_reverse: Final = 12
    OOrReverse: Final = 12
    O_copy_inverted: Final = 13
    OCopyInverted: Final = 13
    O_or_inverted: Final = 14
    OOrInverted: Final = 14
    O_nand: Final = 15
    ONand: Final = 15
    O_set: Final = 16
    OSet: Final = 16
    @property
    def operation(self) -> _LogicOpAttrib_Operation: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new LogicOpAttrib object that disables special-effect
        blending, allowing normal transparency to be used instead.
        """
    @staticmethod
    def make(op: _LogicOpAttrib_Operation) -> RenderAttrib:
        """Constructs a new LogicOpAttrib object with the given logic operation."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_operation(self) -> _LogicOpAttrib_Operation:
        """Returns the logic operation specified by this attribute."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    getOperation = get_operation
    getClassSlot = get_class_slot

class ShaderInput:
    """This is a small container class that can hold any one of the value types
    that can be passed as input to a shader.
    """

    A_read: Final = 1
    ARead: Final = 1
    A_write: Final = 2
    AWrite: Final = 2
    A_layered: Final = 4
    ALayered: Final = 4
    M_invalid: Final = 0
    MInvalid: Final = 0
    M_texture: Final = 1
    MTexture: Final = 1
    M_nodepath: Final = 2
    MNodepath: Final = 2
    M_vector: Final = 3
    MVector: Final = 3
    M_numeric: Final = 4
    MNumeric: Final = 4
    M_texture_sampler: Final = 5
    MTextureSampler: Final = 5
    M_param: Final = 6
    MParam: Final = 6
    M_texture_image: Final = 7
    MTextureImage: Final = 7
    M_buffer: Final = 8
    MBuffer: Final = 8
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: ShaderInput) -> None: ...
    @overload
    def __init__(self, name: InternalName | str, priority: int = ...) -> None: ...
    @overload
    def __init__(self, name: InternalName | str, value, priority: int = ...) -> None: ...
    @overload
    def __init__(self, name: InternalName | str, tex: Texture, sampler: SamplerState, priority: int = ...) -> None: ...
    @overload
    def __init__(
        self, name: InternalName | str, tex: Texture, read: bool, write: bool, z: int = ..., n: int = ..., priority: int = ...
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: ShaderInput) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def get_blank() -> ShaderInput:
        """Returns a static ShaderInput object with name NULL, priority zero, type
        INVALID, and all value-fields cleared.
        """
    def add_hash(self, hash: int) -> int: ...
    def get_name(self) -> InternalName: ...
    def get_value_type(self) -> int: ...
    def get_priority(self) -> int: ...
    def get_vector(self) -> LVecBase4: ...
    def get_nodepath(self) -> NodePath:
        """Warning: no error checking is done.  This *will* crash if get_value_type()
        is not M_nodepath.
        """
    def get_texture(self) -> Texture: ...
    def get_sampler(self) -> SamplerState:
        """Warning: no error checking is done."""
    getBlank = get_blank
    addHash = add_hash
    getName = get_name
    getValueType = get_value_type
    getPriority = get_priority
    getVector = get_vector
    getNodepath = get_nodepath
    getTexture = get_texture
    getSampler = get_sampler

class InternalNameCollection:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: InternalNameCollection = ...) -> None: ...
    def __getitem__(self, index: int) -> InternalName:
        """Returns the nth InternalName in the collection.  This is the same as
        get_name(), but it may be a more convenient way to access it.
        """
    def __len__(self) -> int:
        """Returns the number of names in the collection.  This is the same thing as
        get_num_names().
        """
    def __iadd__(self, other: InternalNameCollection) -> Self: ...
    def __add__(self, other: InternalNameCollection) -> InternalNameCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[InternalName]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def add_name(self, name: InternalName | str) -> None:
        """Adds a new InternalName to the collection."""
    def remove_name(self, name: InternalName | str) -> bool:
        """Removes the indicated InternalName from the collection.  Returns true if
        the name was removed, false if it was not a member of the collection.
        """
    def add_names_from(self, other: InternalNameCollection) -> None:
        """Adds all the InternalNames indicated in the other collection to this name.
        The other names are simply appended to the end of the names in this list;
        duplicates are not automatically removed.
        """
    def remove_names_from(self, other: InternalNameCollection) -> None:
        """Removes from this collection all of the InternalNames listed in the other
        collection.
        """
    def remove_duplicate_names(self) -> None:
        """Removes any duplicate entries of the same InternalNames on this collection.
        If a InternalName appears multiple times, the first appearance is retained;
        subsequent appearances are removed.
        """
    def has_name(self, name: InternalName | str) -> bool:
        """Returns true if the indicated InternalName appears in this collection,
        false otherwise.
        """
    def clear(self) -> None:
        """Removes all InternalNames from the collection."""
    def get_num_names(self) -> int:
        """Returns the number of InternalNames in the collection."""
    def get_name(self, index: int) -> InternalName:
        """Returns the nth InternalName in the collection."""
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the InternalNameCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the InternalNameCollection to
        the indicated output stream.
        """
    def get_names(self) -> tuple[InternalName, ...]: ...
    addName = add_name
    removeName = remove_name
    addNamesFrom = add_names_from
    removeNamesFrom = remove_names_from
    removeDuplicateNames = remove_duplicate_names
    hasName = has_name
    getNumNames = get_num_names
    getName = get_name
    getNames = get_names

class MaterialCollection:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: MaterialCollection = ...) -> None: ...
    def __getitem__(self, index: int) -> Material:
        """Returns the nth Material in the collection.  This is the same as
        get_material(), but it may be a more convenient way to access it.
        """
    def __len__(self) -> int:
        """Returns the number of materials in the collection.  This is the same thing
        as get_num_materials().
        """
    def __iadd__(self, other: MaterialCollection) -> Self: ...
    def __add__(self, other: MaterialCollection) -> MaterialCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[Material]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def add_material(self, node_material: Material) -> None:
        """Adds a new Material to the collection."""
    def remove_material(self, node_material: Material) -> bool:
        """Removes the indicated Material from the collection.  Returns true if the
        material was removed, false if it was not a member of the collection.
        """
    def add_materials_from(self, other: MaterialCollection) -> None:
        """Adds all the Materials indicated in the other collection to this material.
        The other materials are simply appended to the end of the materials in this
        list; duplicates are not automatically removed.
        """
    def remove_materials_from(self, other: MaterialCollection) -> None:
        """Removes from this collection all of the Materials listed in the other
        collection.
        """
    def remove_duplicate_materials(self) -> None:
        """Removes any duplicate entries of the same Materials on this collection.  If
        a Material appears multiple times, the first appearance is retained;
        subsequent appearances are removed.
        """
    def has_material(self, material: Material) -> bool:
        """Returns true if the indicated Material appears in this collection, false
        otherwise.
        """
    def clear(self) -> None:
        """Removes all Materials from the collection."""
    def find_material(self, name: str) -> Material:
        """Returns the material in the collection with the indicated name, if any, or
        NULL if no material has that name.
        """
    def get_num_materials(self) -> int:
        """Returns the number of Materials in the collection."""
    def get_material(self, index: int) -> Material:
        """Returns the nth Material in the collection."""
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the MaterialCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the MaterialCollection to the
        indicated output stream.
        """
    addMaterial = add_material
    removeMaterial = remove_material
    addMaterialsFrom = add_materials_from
    removeMaterialsFrom = remove_materials_from
    removeDuplicateMaterials = remove_duplicate_materials
    hasMaterial = has_material
    findMaterial = find_material
    getNumMaterials = get_num_materials
    getMaterial = get_material

class TextureStageCollection:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: TextureStageCollection = ...) -> None: ...
    def __getitem__(self, index: int) -> TextureStage:
        """Returns the nth TextureStage in the collection.  This is the same as
        get_texture_stage(), but it may be a more convenient way to access it.
        """
    def __len__(self) -> int:
        """Returns the number of texture stages in the collection.  This is the same
        thing as get_num_texture_stages().
        """
    def __iadd__(self, other: TextureStageCollection) -> Self: ...
    def __add__(self, other: TextureStageCollection) -> TextureStageCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[TextureStage]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def add_texture_stage(self, node_texture_stage: TextureStage) -> None:
        """Adds a new TextureStage to the collection."""
    def remove_texture_stage(self, node_texture_stage: TextureStage) -> bool:
        """Removes the indicated TextureStage from the collection.  Returns true if
        the texture_stage was removed, false if it was not a member of the
        collection.
        """
    def add_texture_stages_from(self, other: TextureStageCollection) -> None:
        """Adds all the TextureStages indicated in the other collection to this
        texture_stage.  The other texture_stages are simply appended to the end of
        the texture_stages in this list; duplicates are not automatically removed.
        """
    def remove_texture_stages_from(self, other: TextureStageCollection) -> None:
        """Removes from this collection all of the TextureStages listed in the other
        collection.
        """
    def remove_duplicate_texture_stages(self) -> None:
        """Removes any duplicate entries of the same TextureStages on this collection.
        If a TextureStage appears multiple times, the first appearance is retained;
        subsequent appearances are removed.
        """
    def has_texture_stage(self, texture_stage: TextureStage) -> bool:
        """Returns true if the indicated TextureStage appears in this collection,
        false otherwise.
        """
    def clear(self) -> None:
        """Removes all TextureStages from the collection."""
    def find_texture_stage(self, name: str) -> TextureStage:
        """Returns the texture_stage in the collection with the indicated name, if
        any, or NULL if no texture_stage has that name.
        """
    def get_num_texture_stages(self) -> int:
        """Returns the number of TextureStages in the collection."""
    def get_texture_stage(self, index: int) -> TextureStage:
        """Returns the nth TextureStage in the collection."""
    def sort(self) -> None:
        """Sorts the TextureStages in this collection into order by
        TextureStage::sort(), from lowest to highest.
        """
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the TextureStageCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the TextureStageCollection to
        the indicated output stream.
        """
    def get_texture_stages(self) -> tuple[TextureStage, ...]: ...
    addTextureStage = add_texture_stage
    removeTextureStage = remove_texture_stage
    addTextureStagesFrom = add_texture_stages_from
    removeTextureStagesFrom = remove_texture_stages_from
    removeDuplicateTextureStages = remove_duplicate_texture_stages
    hasTextureStage = has_texture_stage
    findTextureStage = find_texture_stage
    getNumTextureStages = get_num_texture_stages
    getTextureStage = get_texture_stage
    getTextureStages = get_texture_stages

class NodePath(Generic[_N]):
    """NodePath is the fundamental system for disambiguating instances, and also
    provides a higher-level interface for manipulating the scene graph.

    A NodePath is a list of connected nodes from the root of the graph to any
    sub-node.  Each NodePath therefore uniquely describes one instance of a
    node.

    NodePaths themselves are lightweight objects that may easily be copied and
    passed by value.  Their data is stored as a series of NodePathComponents
    that are stored on the nodes.  Holding a NodePath will keep a reference
    count to all the nodes in the path.  However, if any node in the path is
    removed or reparented (perhaps through a different NodePath), the NodePath
    will automatically be updated to reflect the changes.
    """

    ET_ok: Final = 0
    ETOk: Final = 0
    ET_not_found: Final = 1
    ETNotFound: Final = 1
    ET_removed: Final = 2
    ETRemoved: Final = 2
    ET_fail: Final = 3
    ETFail: Final = 3
    DtoolClassDict: ClassVar[dict[str, Any]]
    name: str
    @property
    def nodes(self) -> Sequence[PandaNode]: ...
    @property
    def ancestors(self) -> Sequence[NodePath]: ...
    @property
    def error_type(self) -> _NodePath_ErrorType: ...
    @property
    def children(self) -> NodePathCollection: ...
    @property
    def stashed_children(self) -> NodePathCollection: ...
    @property
    def parent(self) -> NodePath: ...
    @property
    def sort(self) -> int: ...
    @property
    def net_tags(self) -> Mapping[str, str]: ...
    @property
    def tags(self) -> MutableMapping[str, str] | None: ...
    @property
    def python_tags(self) -> dict[Any, Any] | None: ...
    @overload
    def __init__(self: NodePath[Never]) -> None:
        """`(self)`:
        This constructs an empty NodePath with no nodes.

        `(self, parent: NodePath, child_node: PandaNode, current_thread: Thread = ...)`:
        Constructs a NodePath with the indicated parent NodePath and child node;
        the child node must be a stashed or unstashed child of the parent.

        `(self, node: PandaNode, current_thread: Thread = ...)`:
        This constructs a NodePath for the indicated node.  If the node does not
        have any parents, this creates a singleton NodePath; otherwise, it
        automatically finds the path from the node to the root.  If the node has
        multiple paths to the root, one path is chosen arbitrarily and a warning
        message is printed (but see also NodePath::any_path(), below).

        `(self, top_node_name: str, current_thread: Thread = ...)`:
        This constructs a new NodePath with a single node.  An ordinary, unattached
        PandaNode is created with the indicated name.
        """
    @overload
    def __init__(self, copy: NodePath[_N]) -> None: ...
    @overload
    def __init__(self, node: _N, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self: NodePath[PandaNode], top_node_name: str, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, parent: NodePath, child_node: _N, current_thread: Thread = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> NodePath: ...
    def __deepcopy__(self, memo): ...
    def __reduce_persist__(self, pickler): ...
    def __eq__(self, __other: object) -> bool:
        """Comparison methods"""
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: NodePath | WeakNodePath) -> bool: ...
    @staticmethod
    def any_path(node: _M, current_thread: Thread = ...) -> NodePath[_M]:
        """Returns a new NodePath that represents any arbitrary path from the root to
        the indicated node.  This is the same thing that would be returned by
        NodePath(node), except that no warning is issued if the path is ambiguous.
        """
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Sets this NodePath to the empty NodePath.  It will no longer point to any
        node.
        """
    @staticmethod
    def not_found() -> NodePath:
        """Creates a NodePath with the ET_not_found error type set."""
    @staticmethod
    def removed() -> NodePath:
        """Creates a NodePath with the ET_removed error type set."""
    @staticmethod
    def fail() -> NodePath:
        """Creates a NodePath with the ET_fail error type set."""
    @staticmethod
    def set_max_search_depth(max_search_depth: int) -> None:
        """Certain operations, such as find() or find_all_matches(), require a
        traversal of the scene graph to search for the target node or nodes.  This
        traversal does not attempt to detect cycles, so an arbitrary cap is set on
        the depth of the traversal as a poor man's cycle detection, in the event
        that a cycle has inadvertently been introduced into the scene graph.

        There may be other reasons you'd want to truncate a search before the
        bottom of the scene graph has been reached.  In any event, this function
        sets the limit on the number of levels that a traversal will continue, and
        hence the maximum length of a path that may be returned by a traversal.

        This is a static method, and so changing this parameter affects all of the
        NodePaths in the universe.
        """
    @staticmethod
    def get_max_search_depth() -> int:
        """Returns the current setting of the search depth limit.  See
        set_max_search_depth.
        """
    def is_empty(self) -> bool:
        """Returns true if the NodePath contains no nodes."""
    def is_singleton(self, current_thread: Thread = ...) -> bool:
        """Returns true if the NodePath contains exactly one node."""
    def get_num_nodes(self, current_thread: Thread = ...) -> int:
        """Returns the number of nodes in the path."""
    def get_node(self, index: int, current_thread: Thread = ...) -> PandaNode:
        """Returns the nth node of the path, where 0 is the referenced (bottom) node
        and get_num_nodes() - 1 is the top node.  This requires iterating through
        the path.

        Also see node(), which is a convenience function to return the same thing
        as get_node(0) (since the bottom node is the most important node in the
        NodePath, and is the one most frequently referenced).

        Note that this function returns the same thing as
        get_ancestor(index).node().
        """
    def get_ancestor(self, index: int, current_thread: Thread = ...) -> NodePath:
        """Returns the nth ancestor of the path, where 0 is the NodePath itself and
        get_num_nodes() - 1 is get_top(). This requires iterating through the path.

        Also see get_node(), which returns the same thing as a PandaNode pointer,
        not a NodePath.
        """
    def get_error_type(self) -> _NodePath_ErrorType:
        """If is_empty() is true, this returns a code that represents the reason why
        the NodePath is empty.
        """
    def get_top_node(self, current_thread: Thread = ...) -> PandaNode:
        """Returns the top node of the path, or NULL if the path is empty.  This
        requires iterating through the path.
        """
    def get_top(self, current_thread: Thread = ...) -> NodePath:
        """Returns a singleton NodePath that represents the top of the path, or empty
        NodePath if this path is empty.
        """
    def node(self) -> _N:
        """Returns the referenced node of the path."""
    def get_key(self) -> int:
        """Returns an integer that is guaranteed to be the same for all NodePaths that
        represent the same node instance, and different for all NodePaths that
        represent a different node instance.

        The same key will be returned for a particular instance as long as at least
        one NodePath exists that represents that instance; if all NodePaths for a
        particular instance destruct and a new one is later created, it may have a
        different index.  However, a given key will never be reused for a different
        instance (unless the app has been running long enough that we overflow the
        integer key value).
        """
    def add_hash(self, hash: int) -> int:
        """Adds the NodePath into the running hash.  This is intended to be used by
        lower-level code that computes a hash for each NodePath.  It modifies the
        hash value passed in by a unique adjustment for each NodePath, and returns
        the modified hash.

        This is similar to the unique integer returned by get_key(), but it is not
        guaranteed to remain unique beyond the lifetime of this particular
        NodePath.  Once this NodePath destructs, a different NodePath may be
        created which shares the same hash value.
        """
    def is_same_graph(self, other: NodePath, current_thread: Thread = ...) -> bool:
        """Returns true if the node represented by this NodePath is parented within
        the same graph as that of the other NodePath.  This is essentially the same
        thing as asking whether get_top() of both NodePaths is the same (e.g., both
        "render").
        """
    def is_ancestor_of(self, other: NodePath, current_thread: Thread = ...) -> bool:
        """Returns true if the node represented by this NodePath is a parent or other
        ancestor of the other NodePath, or false if it is not.
        """
    def get_common_ancestor(self, other: NodePath, current_thread: Thread = ...) -> NodePath:
        """Returns the lowest NodePath that both of these two NodePaths have in
        common: the first ancestor that both of them share.  If the two NodePaths
        are unrelated, returns NodePath::not_found().
        """
    def get_children(self, current_thread: Thread = ...) -> NodePathCollection:
        """Returns the set of all child nodes of the referenced node."""
    def get_num_children(self, current_thread: Thread = ...) -> int:
        """Returns the number of children of the referenced node."""
    def get_child(self, n: int, current_thread: Thread = ...) -> NodePath:
        """Returns a NodePath representing the nth child of the referenced node."""
    def get_stashed_children(self, current_thread: Thread = ...) -> NodePathCollection:
        """Returns the set of all child nodes of the referenced node that have been
        stashed.  These children are not normally visible on the node, and do not
        appear in the list returned by get_children().
        """
    def count_num_descendants(self) -> int:
        """Returns the number of nodes at and below this level."""
    def has_parent(self, current_thread: Thread = ...) -> bool:
        """Returns true if the referenced node has a parent; i.e.  the NodePath chain
        contains at least two nodes.
        """
    def get_parent(self, current_thread: Thread = ...) -> NodePath:
        """Returns the NodePath to the parent of the referenced node: that is, this
        NodePath, shortened by one node.  The parent of a singleton NodePath is
        defined to be the empty NodePath.
        """
    def get_sort(self, current_thread: Thread = ...) -> int:
        """Returns the sort value of the referenced node within its parent; that is,
        the sort number passed on the last reparenting operation for this node.
        This will control the position of the node within its parent's list of
        children.
        """
    def find(self, path: str) -> NodePath:
        """Searches for a node below the referenced node that matches the indicated
        string.  Returns the shortest match found, if any, or an empty NodePath if
        no match can be found.

        The referenced node itself is not considered in the search.
        """
    def find_path_to(self, node: PandaNode) -> NodePath:
        """Searches for the indicated node below this node and returns the shortest
        NodePath that connects them.
        """
    def find_all_matches(self, path: str) -> NodePathCollection:
        """Returns the complete set of all NodePaths that begin with this NodePath and
        can be extended by path.  The shortest paths will be listed first.

        The referenced node itself is not considered in the search.
        """
    def find_all_paths_to(self, node: PandaNode) -> NodePathCollection:
        """Returns the set of all NodePaths that extend from this NodePath down to the
        indicated node.  The shortest paths will be listed first.
        """
    def reparent_to(self, other: NodePath, sort: int = ..., current_thread: Thread = ...) -> None:
        """Removes the referenced node of the NodePath from its current parent and
        attaches it to the referenced node of the indicated NodePath.

        If the destination NodePath is empty, this is the same thing as
        detach_node().

        If the referenced node is already a child of the indicated NodePath (via
        some other instance), this operation fails and leaves the NodePath
        detached.
        """
    def stash_to(self, other: NodePath, sort: int = ..., current_thread: Thread = ...) -> None:
        """Similar to reparent_to(), but the node is added to its new parent's stashed
        list, so that the result is equivalent to calling reparent_to() immediately
        followed by stash().
        """
    def wrt_reparent_to(self, other: NodePath, sort: int = ..., current_thread: Thread = ...) -> None:
        """This functions identically to reparent_to(), except the transform on this
        node is also adjusted so that the node remains in the same place in world
        coordinates, even if it is reparented into a different coordinate system.
        """
    def instance_to(self, other: NodePath, sort: int = ..., current_thread: Thread = ...) -> NodePath:
        """Adds the referenced node of the NodePath as a child of the referenced node
        of the indicated other NodePath.  Any other parent-child relations of the
        node are unchanged; in particular, the node is not removed from its
        existing parent, if any.

        If the node already had an existing parent, this method will create a new
        instance of the node within the scene graph.

        This does not change the NodePath itself, but does return a new NodePath
        that reflects the new instance node.

        If the destination NodePath is empty, this creates a new instance which is
        not yet parented to any node.  A new instance of this sort cannot easily be
        differentiated from other similar instances, but it is nevertheless a
        different instance and it will return a different get_id() value.

        If the referenced node is already a child of the indicated NodePath,
        returns that already-existing instance, unstashing it first if necessary.
        """
    def instance_under_node(self, other: NodePath, name: str, sort: int = ..., current_thread: Thread = ...) -> NodePath:
        """Behaves like instance_to(), but implicitly creates a new node to instance
        the geometry under, and returns a NodePath to that new node.  This allows
        the programmer to set a unique state and/or transform on this instance.
        """
    def copy_to(self, other: NodePath, sort: int = ..., current_thread: Thread = ...) -> NodePath:
        """Functions like instance_to(), except a deep copy is made of the referenced
        node and all of its descendents, which is then parented to the indicated
        node.  A NodePath to the newly created copy is returned.
        """
    @overload
    def attach_new_node(self, node: _M, sort: int = ..., current_thread: Thread = ...) -> NodePath[_M]:
        """`(self, node: PandaNode, sort: int = ..., current_thread: Thread = ...)`:
        Attaches a new node, with or without existing parents, to the scene graph
        below the referenced node of this NodePath.  This is the preferred way to
        add nodes to the graph.

        If the node was already a child of the parent, this returns a NodePath to
        the existing child.

        This does *not* automatically extend the current NodePath to reflect the
        attachment; however, a NodePath that does reflect this extension is
        returned.

        `(self, name: str, sort: int = ..., current_thread: Thread = ...)`:
        Creates an ordinary PandaNode and attaches it below the current NodePath,
        returning a new NodePath that references it.
        """
    @overload
    def attach_new_node(self, name: str, sort: int = ..., current_thread: Thread = ...) -> NodePath: ...
    def remove_node(self, current_thread: Thread = ...) -> None:
        """Disconnects the referenced node from the scene graph.  This will also
        delete the node if there are no other pointers to it.

        Normally, this should be called only when you are really done with the
        node.  If you want to remove a node from the scene graph but keep it around
        for later, you should probably use detach_node() instead.

        In practice, the only difference between remove_node() and detach_node() is
        that remove_node() also resets the NodePath to empty, which will cause the
        node to be deleted immediately if there are no other references.  On the
        other hand, detach_node() leaves the NodePath referencing the node, which
        will keep at least one reference to the node for as long as the NodePath
        exists.
        """
    def detach_node(self, current_thread: Thread = ...) -> None:
        """Disconnects the referenced node from its parent, but does not immediately
        delete it.  The NodePath retains a pointer to the node, and becomes a
        singleton NodePath.

        This should be called to detach a node from the scene graph, with the
        option of reattaching it later to the same parent or to a different parent.

        In practice, the only difference between remove_node() and detach_node() is
        that remove_node() also resets the NodePath to empty, which will cause the
        node to be deleted immediately if there are no other references.  On the
        other hand, detach_node() leaves the NodePath referencing the node, which
        will keep at least one reference to the node for as long as the NodePath
        exists.
        """
    def output(self, out: ostream) -> None:
        """Writes a sensible description of the NodePath to the indicated output
        stream.
        """
    @overload
    def ls(self) -> None:
        """Lists the hierarchy at and below the referenced node."""
    @overload
    def ls(self, out: ostream, indent_level: int = ...) -> None: ...
    @overload
    def reverse_ls(self) -> None:
        """Lists the hierarchy at and above the referenced node."""
    @overload
    def reverse_ls(self, out: ostream, indent_level: int = ...) -> int: ...
    @overload
    def get_state(self, current_thread: Thread = ...) -> RenderState:
        """`(self, other: NodePath, current_thread: Thread = ...)`:
        Returns the state changes that must be made to transition to the render
        state of this node from the render state of the other node.

        `(self, current_thread: Thread = ...)`:
        Returns the complete state object set on this node.
        """
    @overload
    def get_state(self, other: NodePath, current_thread: Thread = ...) -> RenderState: ...
    @overload
    def set_state(self, state: RenderState, current_thread: Thread = ...) -> None:
        """`(self, other: NodePath, state: RenderState, current_thread: Thread = ...)`:
        Sets the state object on this node, relative to the other node.  This
        computes a new state object that will have the indicated value when seen
        from the other node.

        `(self, state: RenderState, current_thread: Thread = ...)`:
        Changes the complete state object on this node.
        """
    @overload
    def set_state(self, other: NodePath, state: RenderState, current_thread: Thread = ...) -> None: ...
    def get_net_state(self, current_thread: Thread = ...) -> RenderState:
        """Returns the net state on this node from the root."""
    def set_attrib(self, attrib: RenderAttrib, priority: int = ...) -> None:
        """Adds the indicated render attribute to the scene graph on this node.  This
        attribute will now apply to this node and everything below.  If there was
        already an attribute of the same type, it is replaced.
        """
    def get_attrib(self, type: TypeHandle | type) -> RenderAttrib:
        """Returns the render attribute of the indicated type, if it is defined on the
        node, or NULL if it is not.  This checks only what is set on this
        particular node level, and has nothing to do with what render attributes
        may be inherited from parent nodes.
        """
    def has_attrib(self, type: TypeHandle | type) -> bool:
        """Returns true if there is a render attribute of the indicated type defined
        on this node, or false if there is not.
        """
    def clear_attrib(self, type: TypeHandle | type) -> None:
        """Removes the render attribute of the given type from this node.  This node,
        and the subgraph below, will now inherit the indicated render attribute
        from the nodes above this one.
        """
    def set_effect(self, effect: RenderEffect) -> None:
        """Adds the indicated render effect to the scene graph on this node.  If there
        was already an effect of the same type, it is replaced.
        """
    def get_effect(self, type: TypeHandle | type) -> RenderEffect:
        """Returns the render effect of the indicated type, if it is defined on the
        node, or NULL if it is not.
        """
    def has_effect(self, type: TypeHandle | type) -> bool:
        """Returns true if there is a render effect of the indicated type defined on
        this node, or false if there is not.
        """
    def clear_effect(self, type: TypeHandle | type) -> None:
        """Removes the render effect of the given type from this node."""
    def set_effects(self, effects: RenderEffect | RenderEffects) -> None:
        """Sets the complete RenderEffects that will be applied this node.  This
        completely replaces whatever has been set on this node via repeated calls
        to set_attrib().
        """
    def get_effects(self) -> RenderEffects:
        """Returns the complete RenderEffects that will be applied to this node."""
    def clear_effects(self) -> None:
        """Resets this node to have no render effects."""
    @overload
    def get_transform(self, current_thread: Thread = ...) -> TransformState:
        """`(self, other: NodePath, current_thread: Thread = ...)`:
        Returns the relative transform to this node from the other node; i.e.  the
        transformation of this node as seen from the other node.

        `(self, current_thread: Thread = ...)`:
        Returns the complete transform object set on this node.
        """
    @overload
    def get_transform(self, other: NodePath, current_thread: Thread = ...) -> TransformState: ...
    @overload
    def clear_transform(self, current_thread: Thread = ...) -> None:
        """`(self, other: NodePath, current_thread: Thread = ...)`:
        Sets the transform object on this node to identity, relative to the other
        node.  This effectively places this node at the same position as the other
        node.

        `(self, current_thread: Thread = ...)`:
        Sets the transform object on this node to identity.
        """
    @overload
    def clear_transform(self, other: NodePath, current_thread: Thread = ...) -> None: ...
    @overload
    def set_transform(self, transform: TransformState, current_thread: Thread = ...) -> None:
        """`(self, other: NodePath, transform: TransformState, current_thread: Thread = ...)`:
        Sets the transform object on this node, relative to the other node.  This
        computes a new transform object that will have the indicated value when
        seen from the other node.

        `(self, transform: TransformState, current_thread: Thread = ...)`:
        Changes the complete transform object on this node.
        """
    @overload
    def set_transform(self, other: NodePath, transform: TransformState, current_thread: Thread = ...) -> None: ...
    def get_net_transform(self, current_thread: Thread = ...) -> TransformState:
        """Returns the net transform on this node from the root."""
    @overload
    def get_prev_transform(self, current_thread: Thread = ...) -> TransformState:
        """`(self, other: NodePath, current_thread: Thread = ...)`:
        Returns the relative "previous" transform to this node from the other node;
        i.e.  the position of this node in the previous frame, as seen by the other
        node in the previous frame.

        `(self, current_thread: Thread = ...)`:
        Returns the transform that has been set as this node's "previous" position.
        See set_prev_transform().
        """
    @overload
    def get_prev_transform(self, other: NodePath, current_thread: Thread = ...) -> TransformState: ...
    @overload
    def set_prev_transform(self, transform: TransformState, current_thread: Thread = ...) -> None:
        """`(self, other: NodePath, transform: TransformState, current_thread: Thread = ...)`:
        Sets the "previous" transform object on this node, relative to the other
        node.  This computes a new transform object that will have the indicated
        value when seen from the other node.

        `(self, transform: TransformState, current_thread: Thread = ...)`:
        Sets the transform that represents this node's "previous" position, one
        frame ago, for the purposes of detecting motion for accurate collision
        calculations.
        """
    @overload
    def set_prev_transform(self, other: NodePath, transform: TransformState, current_thread: Thread = ...) -> None: ...
    def get_net_prev_transform(self, current_thread: Thread = ...) -> TransformState:
        """Returns the net "previous" transform on this node from the root.  See
        set_prev_transform().
        """
    @overload
    def set_pos(self, pos: Vec3Like) -> None:
        """`(self, pos: LVecBase3)`:
        Sets the translation component of the transform, leaving rotation and scale
        untouched.  This also resets the node's "previous" position, so that the
        collision system will see the node as having suddenly appeared in the new
        position, without passing any points in between.  See Also:
        NodePath::set_fluid_pos

        `(self, other: NodePath, pos: LVecBase3)`; `(self, other: NodePath, x: float, y: float, z: float)`:
        Sets the translation component of the transform, relative to the other
        node.

        `(self, x: float, y: float, z: float)`:
        Sets the translation component of the transform, leaving rotation and scale
        untouched.  This also resets the node's "previous" position, so that the
        collision system will see the node as having suddenly appeared in the new
        position, without passing any points in between.
        """
    @overload
    def set_pos(self, other: NodePath, pos: Vec3Like) -> None: ...
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    @overload
    def set_pos(self, other: NodePath, x: float, y: float, z: float) -> None: ...
    @overload
    def set_x(self, x: float) -> None:
        """Sets the X component of the position transform, leaving other components
        untouched.
        @see set_pos()
        """
    @overload
    def set_x(self, other: NodePath, x: float) -> None: ...
    @overload
    def set_y(self, y: float) -> None:
        """Sets the Y component of the position transform, leaving other components
        untouched.
        @see set_pos()
        """
    @overload
    def set_y(self, other: NodePath, y: float) -> None: ...
    @overload
    def set_z(self, z: float) -> None:
        """Sets the Z component of the position transform, leaving other components
        untouched.
        @see set_pos()
        """
    @overload
    def set_z(self, other: NodePath, z: float) -> None: ...
    @overload
    def set_fluid_pos(self, pos: Vec3Like) -> None:
        """`(self, pos: LVecBase3)`:
        Sets the translation component, without changing the "previous" position,
        so that the collision system will see the node as moving fluidly from its
        previous position to its new position.  See Also: NodePath::set_pos

        `(self, other: NodePath, pos: LVecBase3)`:
        Sets the translation component of the transform, relative to the other
        node.

        `(self, other: NodePath, x: float, y: float, z: float)`; `(self, x: float, y: float, z: float)`:
        Sets the translation component, without changing the "previous" position,
        so that the collision system will see the node as moving fluidly from its
        previous position to its new position.
        """
    @overload
    def set_fluid_pos(self, other: NodePath, pos: Vec3Like) -> None: ...
    @overload
    def set_fluid_pos(self, x: float, y: float, z: float) -> None: ...
    @overload
    def set_fluid_pos(self, other: NodePath, x: float, y: float, z: float) -> None: ...
    @overload
    def set_fluid_x(self, x: float) -> None: ...
    @overload
    def set_fluid_x(self, other: NodePath, x: float) -> None: ...
    @overload
    def set_fluid_y(self, y: float) -> None: ...
    @overload
    def set_fluid_y(self, other: NodePath, y: float) -> None: ...
    @overload
    def set_fluid_z(self, z: float) -> None: ...
    @overload
    def set_fluid_z(self, other: NodePath, z: float) -> None: ...
    def get_pos(self, other: NodePath = ...) -> LPoint3:
        """`(self)`:
        Retrieves the translation component of the transform.

        `(self, other: NodePath)`:
        Returns the relative position of the referenced node as seen from the other
        node.
        """
    def get_x(self, other: NodePath = ...) -> float: ...
    def get_y(self, other: NodePath = ...) -> float: ...
    def get_z(self, other: NodePath = ...) -> float: ...
    def get_pos_delta(self, other: NodePath = ...) -> LVector3:
        """`(self)`:
        Returns the delta vector from this node's position in the previous frame
        (according to set_prev_transform(), typically set via the use of
        set_fluid_pos()) and its position in the current frame.  This is the vector
        used to determine collisions.  Generally, if the node was last repositioned
        via set_pos(), the delta will be zero; if it was adjusted via
        set_fluid_pos(), the delta will represent the change from the previous
        frame's position.

        `(self, other: NodePath)`:
        Returns the delta vector from this node's position in the previous frame
        (according to set_prev_transform(), typically set via the use of
        set_fluid_pos()) and its position in the current frame, as seen in the
        indicated node's coordinate space.  This is the vector used to determine
        collisions.  Generally, if the node was last repositioned via set_pos(),
        the delta will be zero; if it was adjusted via set_fluid_pos(), the delta
        will represent the change from the previous frame's position.
        """
    @overload
    def set_hpr(self, hpr: Vec3Like) -> None:
        """`(self, hpr: LVecBase3)`; `(self, h: float, p: float, r: float)`:
        Sets the rotation component of the transform, leaving translation and scale
        untouched.

        `(self, other: NodePath, hpr: LVecBase3)`; `(self, other: NodePath, h: float, p: float, r: float)`:
        Sets the rotation component of the transform, relative to the other node.
        """
    @overload
    def set_hpr(self, other: NodePath, hpr: Vec3Like) -> None: ...
    @overload
    def set_hpr(self, h: float, p: float, r: float) -> None: ...
    @overload
    def set_hpr(self, other: NodePath, h: float, p: float, r: float) -> None: ...
    @overload
    def set_h(self, h: float) -> None: ...
    @overload
    def set_h(self, other: NodePath, h: float) -> None: ...
    @overload
    def set_p(self, p: float) -> None: ...
    @overload
    def set_p(self, other: NodePath, p: float) -> None: ...
    @overload
    def set_r(self, r: float) -> None: ...
    @overload
    def set_r(self, other: NodePath, r: float) -> None: ...
    def get_hpr(self, other: NodePath = ...) -> LVecBase3:
        """`(self)`:
        Retrieves the rotation component of the transform.

        `(self, other: NodePath)`:
        Returns the relative orientation of the bottom node as seen from the other
        node.
        """
    def get_h(self, other: NodePath = ...) -> float: ...
    def get_p(self, other: NodePath = ...) -> float: ...
    def get_r(self, other: NodePath = ...) -> float: ...
    @overload
    def set_quat(self, quat: Vec4Like) -> None:
        """`(self, quat: LQuaternion)`:
        Sets the rotation component of the transform, leaving translation and scale
        untouched.

        `(self, other: NodePath, quat: LQuaternion)`:
        Sets the rotation component of the transform, relative to the other node.
        """
    @overload
    def set_quat(self, other: NodePath, quat: Vec4Like) -> None: ...
    def get_quat(self, other: NodePath = ...) -> LQuaternion:
        """`(self)`:
        Retrieves the rotation component of the transform.

        `(self, other: NodePath)`:
        Returns the relative orientation of the bottom node as seen from the other
        node.
        """
    @overload
    def set_scale(self, scale: Vec3Like | float) -> None:
        """`(self, scale: LVecBase3)`; `(self, scale: float)`:
        Sets the scale component of the transform, leaving translation and rotation
        untouched.

        `(self, other: NodePath, scale: LVecBase3)`; `(self, other: NodePath, scale: float)`; `(self, other: NodePath, sx: float, sy: float, sz: float)`:
        Sets the scale component of the transform, relative to the other node.
        """
    @overload
    def set_scale(self, other: NodePath, scale: Vec3Like | float) -> None: ...
    @overload
    def set_scale(self, sx: float, sy: float, sz: float) -> None: ...
    @overload
    def set_scale(self, other: NodePath, sx: float, sy: float, sz: float) -> None: ...
    @overload
    def set_sx(self, sx: float) -> None:
        """Sets the x-scale component of the transform, leaving other components
        untouched.
        @see set_scale()
        """
    @overload
    def set_sx(self, other: NodePath, sx: float) -> None: ...
    @overload
    def set_sy(self, sy: float) -> None:
        """Sets the y-scale component of the transform, leaving other components
        untouched.
        @see set_scale()
        """
    @overload
    def set_sy(self, other: NodePath, sy: float) -> None: ...
    @overload
    def set_sz(self, sz: float) -> None:
        """Sets the z-scale component of the transform, leaving other components
        untouched.
        @see set_scale()
        """
    @overload
    def set_sz(self, other: NodePath, sz: float) -> None: ...
    def get_scale(self, other: NodePath = ...) -> LVecBase3:
        """`(self)`:
        Retrieves the scale component of the transform.

        `(self, other: NodePath)`:
        Returns the relative scale of the bottom node as seen from the other node.
        """
    def get_sx(self, other: NodePath = ...) -> float:
        """Returns the relative scale of the referenced node as seen from the other
        node.
        """
    def get_sy(self, other: NodePath = ...) -> float: ...
    def get_sz(self, other: NodePath = ...) -> float: ...
    @overload
    def set_shear(self, shear: Vec3Like) -> None:
        """`(self, shear: LVecBase3)`:
        Sets the shear component of the transform, leaving translation and rotation
        untouched.

        `(self, other: NodePath, shear: LVecBase3)`; `(self, other: NodePath, shxy: float, shxz: float, shyz: float)`:
        Sets the shear component of the transform, relative to the other node.

        `(self, shxy: float, shxz: float, shyz: float)`:
        Sets the shear component of the transform, leaving translation, rotation,
        and scale untouched.
        """
    @overload
    def set_shear(self, other: NodePath, shear: Vec3Like) -> None: ...
    @overload
    def set_shear(self, shxy: float, shxz: float, shyz: float) -> None: ...
    @overload
    def set_shear(self, other: NodePath, shxy: float, shxz: float, shyz: float) -> None: ...
    @overload
    def set_shxy(self, shxy: float) -> None: ...
    @overload
    def set_shxy(self, other: NodePath, shxy: float) -> None: ...
    @overload
    def set_shxz(self, shxz: float) -> None: ...
    @overload
    def set_shxz(self, other: NodePath, shxz: float) -> None: ...
    @overload
    def set_shyz(self, shyz: float) -> None: ...
    @overload
    def set_shyz(self, other: NodePath, shyz: float) -> None: ...
    def get_shear(self, other: NodePath = ...) -> LVecBase3:
        """`(self)`:
        Retrieves the shear component of the transform.

        `(self, other: NodePath)`:
        Returns the relative shear of the bottom node as seen from the other node.
        """
    def get_shxy(self, other: NodePath = ...) -> float:
        """Returns the relative shear of the referenced node as seen from the other
        node.
        """
    def get_shxz(self, other: NodePath = ...) -> float: ...
    def get_shyz(self, other: NodePath = ...) -> float: ...
    @overload
    def set_pos_hpr(self, pos: Vec3Like, hpr: Vec3Like) -> None:
        """`(self, pos: LVecBase3, hpr: LVecBase3)`; `(self, x: float, y: float, z: float, h: float, p: float, r: float)`:
        Sets the translation and rotation component of the transform, leaving scale
        untouched.

        `(self, other: NodePath, pos: LVecBase3, hpr: LVecBase3)`; `(self, other: NodePath, x: float, y: float, z: float, h: float, p: float, r: float)`:
        Sets the translation and rotation component of the transform, relative to
        the other node.
        """
    @overload
    def set_pos_hpr(self, other: NodePath, pos: Vec3Like, hpr: Vec3Like) -> None: ...
    @overload
    def set_pos_hpr(self, x: float, y: float, z: float, h: float, p: float, r: float) -> None: ...
    @overload
    def set_pos_hpr(self, other: NodePath, x: float, y: float, z: float, h: float, p: float, r: float) -> None: ...
    @overload
    def set_pos_quat(self, pos: Vec3Like, quat: Vec4Like) -> None:
        """`(self, pos: LVecBase3, quat: LQuaternion)`:
        Sets the translation and rotation component of the transform, leaving scale
        untouched.

        `(self, other: NodePath, pos: LVecBase3, quat: LQuaternion)`:
        Sets the translation and rotation component of the transform, relative to
        the other node.
        """
    @overload
    def set_pos_quat(self, other: NodePath, pos: Vec3Like, quat: Vec4Like) -> None: ...
    @overload
    def set_hpr_scale(self, hpr: Vec3Like, scale: Vec3Like) -> None:
        """`(self, hpr: LVecBase3, scale: LVecBase3)`; `(self, h: float, p: float, r: float, sx: float, sy: float, sz: float)`:
        Sets the rotation and scale components of the transform, leaving
        translation untouched.

        `(self, other: NodePath, hpr: LVecBase3, scale: LVecBase3)`; `(self, other: NodePath, h: float, p: float, r: float, sx: float, sy: float, sz: float)`:
        Sets the rotation and scale components of the transform, leaving
        translation untouched.  This, or set_pos_hpr_scale, is the preferred way to
        update a transform when both hpr and scale are to be changed.
        """
    @overload
    def set_hpr_scale(self, other: NodePath, hpr: Vec3Like, scale: Vec3Like) -> None: ...
    @overload
    def set_hpr_scale(self, h: float, p: float, r: float, sx: float, sy: float, sz: float) -> None: ...
    @overload
    def set_hpr_scale(self, other: NodePath, h: float, p: float, r: float, sx: float, sy: float, sz: float) -> None: ...
    @overload
    def set_quat_scale(self, quat: Vec4Like, scale: Vec3Like) -> None:
        """`(self, quat: LQuaternion, scale: LVecBase3)`:
        Sets the rotation and scale components of the transform, leaving
        translation untouched.

        `(self, other: NodePath, quat: LQuaternion, scale: LVecBase3)`:
        Sets the rotation and scale components of the transform, leaving
        translation untouched.  This, or set_pos_quat_scale, is the preferred way
        to update a transform when both quat and scale are to be changed.
        """
    @overload
    def set_quat_scale(self, other: NodePath, quat: Vec4Like, scale: Vec3Like) -> None: ...
    @overload
    def set_pos_hpr_scale(self, pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> None:
        """`(self, pos: LVecBase3, hpr: LVecBase3, scale: LVecBase3)`:
        Replaces the translation, rotation, and scale components, implicitly
        setting shear to 0.

        `(self, other: NodePath, pos: LVecBase3, hpr: LVecBase3, scale: LVecBase3)`:
        Completely replaces the transform with new translation, rotation, and scale
        components, relative to the other node, implicitly setting shear to 0.

        `(self, other: NodePath, x: float, y: float, z: float, h: float, p: float, r: float, sx: float, sy: float, sz: float)`:
        Completely replaces the transform with new translation, rotation, and scale
        components, relative to the other node.

        `(self, x: float, y: float, z: float, h: float, p: float, r: float, sx: float, sy: float, sz: float)`:
        Completely replaces the transform with new translation, rotation, and scale
        components.
        """
    @overload
    def set_pos_hpr_scale(self, other: NodePath, pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> None: ...
    @overload
    def set_pos_hpr_scale(
        self, x: float, y: float, z: float, h: float, p: float, r: float, sx: float, sy: float, sz: float
    ) -> None: ...
    @overload
    def set_pos_hpr_scale(
        self, other: NodePath, x: float, y: float, z: float, h: float, p: float, r: float, sx: float, sy: float, sz: float
    ) -> None: ...
    @overload
    def set_pos_quat_scale(self, pos: Vec3Like, quat: Vec4Like, scale: Vec3Like) -> None:
        """`(self, pos: LVecBase3, quat: LQuaternion, scale: LVecBase3)`:
        Replaces the translation, rotation, and scale components, implicitly
        setting shear to 0.

        `(self, other: NodePath, pos: LVecBase3, quat: LQuaternion, scale: LVecBase3)`:
        Completely replaces the transform with new translation, rotation, and scale
        components, relative to the other node, implicitly setting shear to 0.
        """
    @overload
    def set_pos_quat_scale(self, other: NodePath, pos: Vec3Like, quat: Vec4Like, scale: Vec3Like) -> None: ...
    @overload
    def set_pos_hpr_scale_shear(self, pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like, shear: Vec3Like) -> None:
        """`(self, pos: LVecBase3, hpr: LVecBase3, scale: LVecBase3, shear: LVecBase3)`:
        Completely replaces the transform with new translation, rotation, scale,
        and shear components.

        `(self, other: NodePath, pos: LVecBase3, hpr: LVecBase3, scale: LVecBase3, shear: LVecBase3)`:
        Completely replaces the transform with new translation, rotation, scale,
        and shear components, relative to the other node.
        """
    @overload
    def set_pos_hpr_scale_shear(
        self, other: NodePath, pos: Vec3Like, hpr: Vec3Like, scale: Vec3Like, shear: Vec3Like
    ) -> None: ...
    @overload
    def set_pos_quat_scale_shear(self, pos: Vec3Like, quat: Vec4Like, scale: Vec3Like, shear: Vec3Like) -> None:
        """`(self, pos: LVecBase3, quat: LQuaternion, scale: LVecBase3, shear: LVecBase3)`:
        Completely replaces the transform with new translation, rotation, scale,
        and shear components.

        `(self, other: NodePath, pos: LVecBase3, quat: LQuaternion, scale: LVecBase3, shear: LVecBase3)`:
        Completely replaces the transform with new translation, rotation, scale,
        and shear components, relative to the other node.
        """
    @overload
    def set_pos_quat_scale_shear(
        self, other: NodePath, pos: Vec3Like, quat: Vec4Like, scale: Vec3Like, shear: Vec3Like
    ) -> None: ...
    @overload
    def set_mat(self, mat: Mat4Like) -> None:
        """`(self, mat: LMatrix4)`:
        Directly sets an arbitrary 4x4 transform matrix.

        `(self, other: NodePath, mat: LMatrix4)`:
        Converts the indicated matrix from the other's coordinate space to the
        local coordinate space, and applies it to the node.
        """
    @overload
    def set_mat(self, other: NodePath, mat: Mat4Like) -> None: ...
    def clear_mat(self) -> None:
        """Completely removes any transform from the referenced node."""
    def has_mat(self) -> bool:
        """Returns true if a non-identity transform matrix has been applied to the
        referenced node, false otherwise.
        """
    def get_mat(self, other: NodePath = ...) -> LMatrix4:
        """`(self)`:
        Returns the transform matrix that has been applied to the referenced node,
        or the identity matrix if no matrix has been applied.

        `(self, other: NodePath)`:
        Returns the matrix that describes the coordinate space of the bottom node,
        relative to the other path's bottom node's coordinate space.
        """
    @overload
    def look_at(self, point: Vec3Like, up: Vec3Like = ...) -> None:
        """`(self, point: LPoint3, up: LVector3 = ...)`:
        Sets the hpr on this NodePath so that it rotates to face the indicated
        point in space.

        `(self, other: NodePath, point: LPoint3 = ..., up: LVector3 = ...)`:
        Sets the transform on this NodePath so that it rotates to face the
        indicated point in space, which is relative to the other NodePath.

        `(self, other: NodePath, x: float, y: float, z: float)`:
        Sets the hpr on this NodePath so that it rotates to face the indicated
        point in space, which is relative to the other NodePath.

        `(self, x: float, y: float, z: float)`:
        Sets the transform on this NodePath so that it rotates to face the
        indicated point in space.  This will overwrite any previously existing
        scale on the node, although it will preserve any translation.
        """
    @overload
    def look_at(self, other: NodePath, point: Vec3Like = ..., up: Vec3Like = ...) -> None: ...
    @overload
    def look_at(self, x: float, y: float, z: float) -> None: ...
    @overload
    def look_at(self, other: NodePath, x: float, y: float, z: float) -> None: ...
    @overload
    def heads_up(self, point: Vec3Like, up: Vec3Like = ...) -> None:
        """Behaves like look_at(), but with a strong preference to keeping the up
        vector oriented in the indicated "up" direction.
        """
    @overload
    def heads_up(self, other: NodePath, point: Vec3Like = ..., up: Vec3Like = ...) -> None: ...
    @overload
    def heads_up(self, x: float, y: float, z: float) -> None: ...
    @overload
    def heads_up(self, other: NodePath, x: float, y: float, z: float) -> None: ...
    def get_relative_point(self, other: NodePath, point: Vec3Like) -> LPoint3:
        """Given that the indicated point is in the coordinate system of the other
        node, returns the same point in this node's coordinate system.
        """
    def get_relative_vector(self, other: NodePath, vec: Vec3Like) -> LVector3:
        """Given that the indicated vector is in the coordinate system of the other
        node, returns the same vector in this node's coordinate system.
        """
    def get_distance(self, other: NodePath) -> float:
        """Returns the straight-line distance between this referenced node's
        coordinate frame's origin, and that of the other node's origin.
        """
    @overload
    def set_color(self, color: Vec4Like, priority: int = ...) -> None:
        """Applies a scene-graph color to the referenced node.  This color will apply
        to all geometry at this level and below (that does not specify a new color
        or a set_color_off()).
        """
    @overload
    def set_color(self, r: float, g: float, b: float, a: float = ..., priority: int = ...) -> None: ...
    def set_color_off(self, priority: int = ...) -> None:
        """Sets the geometry at this level and below to render using the geometry
        color.  This is normally the default, but it may be useful to use this to
        contradict set_color() at a higher node level (or, with a priority, to
        override a set_color() at a lower level).
        """
    def clear_color(self) -> None:
        """Completely removes any color adjustment from the node.  This allows the
        natural color of the geometry, or whatever color transitions might be
        otherwise affecting the geometry, to show instead.
        """
    def has_color(self) -> bool:
        """Returns true if a color has been applied to the given node, false
        otherwise.
        """
    def get_color(self) -> LColor:
        """Returns the color that has been assigned to the node, or black if no color
        has been assigned.
        """
    def has_color_scale(self) -> bool:
        """Returns true if a color scale has been applied to the referenced node,
        false otherwise.  It is still possible that color at this node might have
        been scaled by an ancestor node.
        """
    def clear_color_scale(self) -> None:
        """Completely removes any color scale from the referenced node.  This is
        preferable to simply setting the color scale to identity, as it also
        removes the overhead associated with having a color scale at all.
        """
    @overload
    def set_color_scale(self, scale: Vec4Like, priority: int = ...) -> None:
        """`(self, scale: LVecBase4, priority: int = ...)`:
        Sets the color scale component of the transform, leaving translation and
        rotation untouched.

        `(self, sx: float, sy: float, sz: float, sa: float, priority: int = ...)`:
        Sets the color scale component of the transform
        """
    @overload
    def set_color_scale(self, sx: float, sy: float, sz: float, sa: float, priority: int = ...) -> None: ...
    @overload
    def compose_color_scale(self, scale: Vec4Like, priority: int = ...) -> None:
        """`(self, scale: LVecBase4, priority: int = ...)`:
        multiplies the color scale component of the transform, with previous color
        scale leaving translation and rotation untouched.

        `(self, sx: float, sy: float, sz: float, sa: float, priority: int = ...)`:
        Sets the color scale component of the transform
        """
    @overload
    def compose_color_scale(self, sx: float, sy: float, sz: float, sa: float, priority: int = ...) -> None: ...
    def set_color_scale_off(self, priority: int = ...) -> None:
        """Disables any color scale attribute inherited from above.  This is not the
        same thing as clear_color_scale(), which undoes any previous
        set_color_scale() operation on this node; rather, this actively disables
        any set_color_scale() that might be inherited from a parent node.  This
        also disables set_alpha_scale() at the same time.

        It is legal to specify a new color scale on the same node with a subsequent
        call to set_color_scale() or set_alpha_scale(); this new scale will apply
        to lower geometry.
        """
    def set_alpha_scale(self, scale: float, priority: int = ...) -> None:
        """Sets the alpha scale component of the transform without (much) affecting
        the color scale.  Note that any priority specified will also apply to the
        color scale.
        """
    def set_all_color_scale(self, scale: float, priority: int = ...) -> None:
        """Scales all the color components of the object by the same amount, darkening
        the object, without (much) affecting alpha.  Note that any priority
        specified will also apply to the alpha scale.
        """
    def set_sr(self, sr: float) -> None:
        """Sets the red component of the color scale.
        @see set_color_scale()
        """
    def set_sg(self, sg: float) -> None:
        """Sets the green component of the color scale.
        @see set_color_scale()
        """
    def set_sb(self, sb: float) -> None:
        """Sets the blue component of the color scale.
        @see set_color_scale()
        """
    def set_sa(self, sa: float) -> None:
        """Sets the alpha component of the color scale.
        @see set_color_scale()
        """
    def get_color_scale(self) -> LVecBase4:
        """Returns the complete color scale vector that has been applied to this node
        via a previous call to set_color_scale() and/or set_alpha_scale(), or all
        1's (identity) if no scale has been applied to this particular node.
        """
    def get_sr(self) -> float:
        """Gets the red component of the color scale.
        @see get_color_scale()
        """
    def get_sg(self) -> float:
        """Gets the green component of the color scale.
        @see get_color_scale()
        """
    def get_sb(self) -> float:
        """Gets the blue component of the color scale.
        @see get_color_scale()
        """
    def get_sa(self) -> float:
        """Gets the alpha component of the color scale.
        @see get_color_scale()
        """
    def set_light(self, light: NodePath, priority: int = ...) -> None:
        """Adds the indicated Light or PolylightNode to the list of lights that
        illuminate geometry at this node and below.  The light itself should be
        parented into the scene graph elsewhere, to represent the light's position
        in space; but until set_light() is called it will illuminate no geometry.
        """
    @overload
    def set_light_off(self, priority: int = ...) -> None:
        """`(self, light: NodePath, priority: int = ...)`:
        Sets the geometry at this level and below to render without using the
        indicated Light.  This is different from not specifying the Light; rather,
        this specifically contradicts set_light() at a higher node level (or, with
        a priority, overrides a set_light() at a lower level).

        This interface does not support PolylightNodes, which cannot be turned off
        at a lower level.

        `(self, priority: int = ...)`:
        Sets the geometry at this level and below to render using no lights at all.
        This is different from not specifying a light; rather, this specifically
        contradicts set_light() at a higher node level (or, with a priority,
        overrides a set_light() at a lower level).

        If no lights are in effect on a particular piece of geometry, that geometry
        is rendered with lighting disabled.
        """
    @overload
    def set_light_off(self, light: NodePath, priority: int = ...) -> None: ...
    def clear_light(self, light: NodePath = ...) -> None:
        """`(self)`:
        Completely removes any lighting operations that may have been set via
        set_light() or set_light_off() from this particular node.

        `(self, light: NodePath)`:
        Removes any reference to the indicated Light or PolylightNode from the
        NodePath.
        """
    def has_light(self, light: NodePath) -> bool:
        """Returns true if the indicated Light or PolylightNode has been specifically
        enabled on this particular node.  This means that someone called
        set_light() on this node with the indicated light.
        """
    def has_light_off(self, light: NodePath = ...) -> bool:
        """`(self)`:
        Returns true if all Lights have been specifically disabled on this
        particular node.  This means that someone called set_light_off() on this
        node with no parameters.

        `(self, light: NodePath)`:
        Returns true if the indicated Light has been specifically disabled on this
        particular node.  This means that someone called set_light_off() on this
        node with the indicated light.

        This interface does not support PolylightNodes, which cannot be turned off
        at a lower level.
        """
    def set_clip_plane(self, clip_plane: NodePath, priority: int = ...) -> None:
        """Adds the indicated clipping plane to the list of planes that apply to
        geometry at this node and below.  The clipping plane itself, a PlaneNode,
        should be parented into the scene graph elsewhere, to represent the plane's
        position in space; but until set_clip_plane() is called it will clip no
        geometry.
        """
    @overload
    def set_clip_plane_off(self, priority: int = ...) -> None:
        """`(self, clip_plane: NodePath, priority: int = ...)`:
        Sets the geometry at this level and below to render without being clipped
        by the indicated PlaneNode.  This is different from not specifying the
        PlaneNode; rather, this specifically contradicts set_clip_plane() at a
        higher node level (or, with a priority, overrides a set_clip_plane() at a
        lower level).

        `(self, priority: int = ...)`:
        Sets the geometry at this level and below to render using no clip_planes at
        all.  This is different from not specifying a clip_plane; rather, this
        specifically contradicts set_clip_plane() at a higher node level (or, with
        a priority, overrides a set_clip_plane() at a lower level).

        If no clip_planes are in effect on a particular piece of geometry, that
        geometry is rendered without being clipped (other than by the viewing
        frustum).
        """
    @overload
    def set_clip_plane_off(self, clip_plane: NodePath, priority: int = ...) -> None: ...
    def clear_clip_plane(self, clip_plane: NodePath = ...) -> None:
        """`(self)`:
        Completely removes any clip planes that may have been set via
        set_clip_plane() or set_clip_plane_off() from this particular node.

        `(self, clip_plane: NodePath)`:
        Removes any reference to the indicated clipping plane from the NodePath.
        """
    def has_clip_plane(self, clip_plane: NodePath) -> bool:
        """Returns true if the indicated clipping plane has been specifically applied
        to this particular node.  This means that someone called set_clip_plane()
        on this node with the indicated clip_plane.
        """
    def has_clip_plane_off(self, clip_plane: NodePath = ...) -> bool:
        """`(self)`:
        Returns true if all clipping planes have been specifically disabled on this
        particular node.  This means that someone called set_clip_plane_off() on
        this node with no parameters.

        `(self, clip_plane: NodePath)`:
        Returns true if the indicated clipping plane has been specifically disabled
        on this particular node.  This means that someone called
        set_clip_plane_off() on this node with the indicated clip_plane.
        """
    @overload
    def set_scissor(self, a: Vec3Like, b: Vec3Like) -> None:
        """`(self, a: LPoint3, b: LPoint3)`:
        Sets up a scissor region on the nodes rendered at this level and below.
        The two points are understood to be relative to this node.  When these
        points are projected into screen space, they define the diagonally-opposite
        points that determine the scissor region.

        `(self, a: LPoint3, b: LPoint3, c: LPoint3, d: LPoint3)`:
        Sets up a scissor region on the nodes rendered at this level and below.
        The four points are understood to be relative to this node.  When these
        points are projected into screen space, they define the bounding volume of
        the scissor region (the scissor region is the smallest onscreen rectangle
        that encloses all four points).

        `(self, other: NodePath, a: LPoint3, b: LPoint3)`:
        Sets up a scissor region on the nodes rendered at this level and below.
        The two points are understood to be relative to the indicated other node.
        When these points are projected into screen space, they define the
        diagonally-opposite points that determine the scissor region.

        `(self, other: NodePath, a: LPoint3, b: LPoint3, c: LPoint3, d: LPoint3)`:
        Sets up a scissor region on the nodes rendered at this level and below.
        The four points are understood to be relative to the indicated other node.
        When these points are projected into screen space, they define the bounding
        volume of the scissor region (the scissor region is the smallest onscreen
        rectangle that encloses all four points).

        `(self, left: float, right: float, bottom: float, top: float)`:
        Sets up a scissor region on the nodes rendered at this level and below.
        The four coordinates are understood to define a rectangle in screen space.
        These numbers are relative to the current DisplayRegion, where (0,0) is the
        lower-left corner of the DisplayRegion, and (1,1) is the upper-right
        corner.
        """
    @overload
    def set_scissor(self, other: NodePath, a: Vec3Like, b: Vec3Like) -> None: ...
    @overload
    def set_scissor(self, a: Vec3Like, b: Vec3Like, c: Vec3Like, d: Vec3Like) -> None: ...
    @overload
    def set_scissor(self, left: float, right: float, bottom: float, top: float) -> None: ...
    @overload
    def set_scissor(self, other: NodePath, a: Vec3Like, b: Vec3Like, c: Vec3Like, d: Vec3Like) -> None: ...
    def clear_scissor(self) -> None:
        """Removes the scissor region that was defined at this node level by a
        previous call to set_scissor().
        """
    def has_scissor(self) -> bool:
        """Returns true if a scissor region was defined at this node by a previous
        call to set_scissor().  This does not check for scissor regions inherited
        from a parent class.  It also does not check for the presence of a low-
        level ScissorAttrib, which is different from the ScissorEffect added by
        set_scissor.
        """
    def set_occluder(self, occluder: NodePath) -> None:
        """Adds the indicated occluder to the list of occluders that apply to geometry
        at this node and below.  The occluder itself, an OccluderNode, should be
        parented into the scene graph elsewhere, to represent the occluder's
        position in space; but until set_occluder() is called it will clip no
        geometry.
        """
    def clear_occluder(self, occluder: NodePath = ...) -> None:
        """`(self)`:
        Completely removes any occluders that may have been set via set_occluder()
        from this particular node.

        `(self, occluder: NodePath)`:
        Removes any reference to the indicated occluder from the NodePath.
        """
    def has_occluder(self, occluder: NodePath) -> bool:
        """Returns true if the indicated occluder has been specifically applied to
        this particular node.  This means that someone called set_occluder() on
        this node with the indicated occluder.
        """
    def set_bin(self, bin_name: str, draw_order: int, priority: int = ...) -> None:
        """Assigns the geometry at this level and below to the named rendering bin.
        It is the user's responsibility to ensure that such a bin already exists,
        either via the cull-bin Configrc variable, or by explicitly creating a
        GeomBin of the appropriate type at runtime.

        There are two default bins created when Panda is started: "default" and
        "fixed".  Normally, all geometry is assigned to "default" unless specified
        otherwise.  This bin renders opaque geometry in state-sorted order,
        followed by transparent geometry sorted back-to-front.  If any geometry is
        assigned to "fixed", this will be rendered following all the geometry in
        "default", in the order specified by draw_order for each piece of geometry
        so assigned.

        The draw_order parameter is meaningful only for GeomBinFixed type bins,
        e.g.  "fixed".  Other kinds of bins ignore it.
        """
    def clear_bin(self) -> None:
        """Completely removes any bin adjustment that may have been set via set_bin()
        from this particular node.
        """
    def has_bin(self) -> bool:
        """Returns true if the node has been assigned to the a particular rendering
        bin via set_bin(), false otherwise.
        """
    def get_bin_name(self) -> str:
        """Returns the name of the bin that this particular node was assigned to via
        set_bin(), or the empty string if no bin was assigned.  See set_bin() and
        has_bin().
        """
    def get_bin_draw_order(self) -> int:
        """Returns the drawing order associated with the bin that this particular node
        was assigned to via set_bin(), or 0 if no bin was assigned.  See set_bin()
        and has_bin().
        """
    @overload
    def set_texture(self, tex: Texture, priority: int = ...) -> None:
        """`(self, tex: Texture, sampler: SamplerState, priority: int = ...)`:
        Adds the indicated texture to the list of textures that will be rendered on
        the default texture stage.

        The given sampler state will override the sampling settings on the texture
        itself.  Note that this method makes a copy of the sampler settings that
        you give; further changes to this object will not be reflected.

        This is the convenience single-texture variant of this method; it is now
        superceded by set_texture() that accepts a stage and texture.  You may use
        this method if you just want to adjust the default stage.

        `(self, tex: Texture, priority: int = ...)`:
        Adds the indicated texture to the list of textures that will be rendered on
        the default texture stage.

        This is the convenience single-texture variant of this method; it is now
        superceded by set_texture() that accepts a stage and texture.  You may use
        this method if you just want to adjust the default stage.

        `(self, stage: TextureStage, tex: Texture, sampler: SamplerState, priority: int = ...)`:
        Adds the indicated texture to the list of textures that will be rendered on
        the indicated multitexture stage.  If there are multiple texture stages
        specified (possibly on multiple different nodes at different levels), they
        will all be applied to geometry together, according to the stage
        specification set up in the TextureStage object.

        The given sampler state will override the sampling settings on the texture
        itself.  Note that this method makes a copy of the sampler settings that
        you give; further changes to this object will not be reflected.

        `(self, stage: TextureStage, tex: Texture, priority: int = ...)`:
        Adds the indicated texture to the list of textures that will be rendered on
        the indicated multitexture stage.  If there are multiple texture stages
        specified (possibly on multiple different nodes at different levels), they
        will all be applied to geometry together, according to the stage
        specification set up in the TextureStage object.
        """
    @overload
    def set_texture(self, tex: Texture, sampler: SamplerState, priority: int = ...) -> None: ...
    @overload
    def set_texture(self, stage: TextureStage, tex: Texture, priority: int = ...) -> None: ...
    @overload
    def set_texture(self, stage: TextureStage, tex: Texture, sampler: SamplerState, priority: int = ...) -> None: ...
    @overload
    def set_texture_off(self, priority: int = ...) -> None:
        """`(self, stage: TextureStage, priority: int = ...)`:
        Sets the geometry at this level and below to render using no texture, on
        the indicated stage.  This is different from not specifying a texture;
        rather, this specifically contradicts set_texture() at a higher node level
        (or, with a priority, overrides a set_texture() at a lower level).

        `(self, priority: int = ...)`:
        Sets the geometry at this level and below to render using no texture, on
        any stage.  This is different from not specifying a texture; rather, this
        specifically contradicts set_texture() at a higher node level (or, with a
        priority, overrides a set_texture() at a lower level).
        """
    @overload
    def set_texture_off(self, stage: TextureStage, priority: int = ...) -> None: ...
    def clear_texture(self, stage: TextureStage = ...) -> None:
        """`(self)`:
        Completely removes any texture adjustment that may have been set via
        set_texture() or set_texture_off() from this particular node.  This allows
        whatever textures might be otherwise affecting the geometry to show
        instead.

        `(self, stage: TextureStage)`:
        Removes any reference to the indicated texture stage from the NodePath.
        """
    def has_texture(self, stage: TextureStage = ...) -> bool:
        """`(self)`:
        Returns true if a texture has been applied to this particular node via
        set_texture(), false otherwise.  This is not the same thing as asking
        whether the geometry at this node will be rendered with texturing, as there
        may be a texture in effect from a higher or lower level.

        `(self, stage: TextureStage)`:
        Returns true if texturing has been specifically enabled on this particular
        node for the indicated stage.  This means that someone called set_texture()
        on this node with the indicated stage name, or the stage_name is the
        default stage_name, and someone called set_texture() on this node.
        """
    def has_texture_off(self, stage: TextureStage = ...) -> bool:
        """`(self)`:
        Returns true if texturing has been specifically disabled on this particular
        node via set_texture_off(), false otherwise.  This is not the same thing as
        asking whether the geometry at this node will be rendered untextured, as
        there may be a texture in effect from a higher or lower level.

        `(self, stage: TextureStage)`:
        Returns true if texturing has been specifically disabled on this particular
        node for the indicated stage.  This means that someone called
        set_texture_off() on this node with the indicated stage name, or that
        someone called set_texture_off() on this node to remove all stages.
        """
    def get_texture(self, stage: TextureStage = ...) -> Texture:
        """`(self)`:
        Returns the base-level texture that has been set on this particular node,
        or NULL if no texture has been set.  This is not necessarily the texture
        that will be applied to the geometry at or below this level, as another
        texture at a higher or lower level may override.

        See also find_texture().

        `(self, stage: TextureStage)`:
        Returns the texture that has been set on the indicated stage for this
        particular node, or NULL if no texture has been set for this stage.
        """
    def replace_texture(self, tex: Texture, new_tex: Texture | None) -> None:
        """`(self, tex: Texture, new_tex: Texture)`:
        Recursively searches the scene graph for references to the given texture,
        and replaces them with the new texture.

        As of Panda3D 1.10.13, new_tex may be null to remove the texture.

        @since 1.10.4

        `(self, tex: Texture, new_tex: None)`:
        Let interrogate know this also accepts None
        """
    def get_texture_sampler(self, stage: TextureStage = ...) -> SamplerState:
        """`(self)`:
        Returns the sampler state that has been given for the base-level texture
        that has been set on this particular node.  If no sampler state was given,
        this returns the texture's default sampler settings.

        It is an error to call this if there is no base-level texture applied to
        this particular node.

        `(self, stage: TextureStage)`:
        Returns the sampler state that has been given for the indicated texture
        stage that has been set on this particular node.  If no sampler state was
        given, this returns the texture's default sampler settings.

        It is an error to call this if there is no texture set for this stage on
        this particular node.
        """
    def set_shader(self, sha: Shader, priority: int = ...) -> None: ...
    def set_shader_off(self, priority: int = ...) -> None: ...
    @overload
    def set_shader_auto(self, priority: int = ...) -> None:
        """overloaded for auto shader customization"""
    @overload
    def set_shader_auto(self, shader_switch: BitMask32, priority: int = ...) -> None: ...
    def clear_shader(self) -> None: ...
    @overload
    def set_shader_input(self, input: ShaderInput) -> None: ...
    @overload
    def set_shader_input(self, __param0: InternalName | str, __param1, priority: int = ...) -> None: ...
    @overload
    def set_shader_input(self, id: InternalName | str, tex: Texture, sampler: SamplerState, priority: int = ...) -> None: ...
    @overload
    def set_shader_input(
        self, id: InternalName | str, n1: float, n2: float, n3: float = ..., n4: float = ..., priority: int = ...
    ) -> None: ...
    @overload
    def set_shader_input(
        self, id: InternalName | str, tex: Texture, read: bool, write: bool, z: int = ..., n: int = ..., priority: int = ...
    ) -> None: ...
    def set_shader_inputs(self, *args, **kwargs) -> None: ...
    def clear_shader_input(self, id: InternalName | str) -> None: ...
    def set_instance_count(self, instance_count: int) -> None:
        """Sets the geometry instance count, or 0 if geometry instancing should be
        disabled.  Do not confuse with instanceTo which only applies to animation
        instancing.
        """
    def get_shader(self) -> Shader: ...
    def get_shader_input(self, id: InternalName | str) -> ShaderInput: ...
    def get_instance_count(self) -> int:
        """Returns the geometry instance count, or 0 if disabled.  See
        set_instance_count.
        """
    @overload
    def set_tex_transform(self, stage: TextureStage, transform: TransformState) -> None:
        """Sets the texture matrix on the current node to the indicated transform for
        the given stage.
        """
    @overload
    def set_tex_transform(self, other: NodePath, stage: TextureStage, transform: TransformState) -> None: ...
    def clear_tex_transform(self, stage: TextureStage = ...) -> None:
        """`(self)`:
        Removes all texture matrices from the current node.

        `(self, stage: TextureStage)`:
        Removes the texture matrix on the current node for the given stage.
        """
    def has_tex_transform(self, stage: TextureStage) -> bool:
        """Returns true if there is an explicit texture matrix on the current node for
        the given stage.
        """
    @overload
    def get_tex_transform(self, stage: TextureStage) -> TransformState:
        """`(self, other: NodePath, stage: TextureStage)`:
        Returns the texture matrix on the current node for the given stage,
        relative to the other node.

        `(self, stage: TextureStage)`:
        Returns the texture matrix on the current node for the given stage, or
        identity transform if there is no explicit transform set for the given
        stage.
        """
    @overload
    def get_tex_transform(self, other: NodePath, stage: TextureStage) -> TransformState: ...
    @overload
    def set_tex_offset(self, stage: TextureStage, uv: Vec2Like) -> None:
        """Sets a texture matrix on the current node to apply the indicated offset to
        UV's for the given stage.

        This call is appropriate for ordinary 2-d texture coordinates.
        """
    @overload
    def set_tex_offset(self, other: NodePath, stage: TextureStage, uv: Vec2Like) -> None: ...
    @overload
    def set_tex_offset(self, stage: TextureStage, u: float, v: float) -> None: ...
    @overload
    def set_tex_offset(self, other: NodePath, stage: TextureStage, u: float, v: float) -> None: ...
    @overload
    def set_tex_rotate(self, stage: TextureStage, r: float) -> None:
        """Sets a texture matrix on the current node to apply the indicated rotation,
        clockwise in degrees, to UV's for the given stage.

        This call is appropriate for ordinary 2-d texture coordinates.
        """
    @overload
    def set_tex_rotate(self, other: NodePath, stage: TextureStage, r: float) -> None: ...
    @overload
    def set_tex_scale(self, stage: TextureStage, scale: Vec2Like | Vec3Like | float) -> None:
        """`(self, other: NodePath, stage: TextureStage, scale: LVecBase2)`; `(self, other: NodePath, stage: TextureStage, su: float, sv: float)`; `(self, stage: TextureStage, scale: LVecBase2)`; `(self, stage: TextureStage, su: float, sv: float)`:
        Sets a texture matrix on the current node to apply the indicated scale to
        UV's for the given stage.

        This call is appropriate for ordinary 2-d texture coordinates.

        `(self, other: NodePath, stage: TextureStage, scale: LVecBase3)`; `(self, other: NodePath, stage: TextureStage, su: float, sv: float, sw: float)`; `(self, stage: TextureStage, scale: LVecBase3)`; `(self, stage: TextureStage, su: float, sv: float, sw: float)`:
        Sets a texture matrix on the current node to apply the indicated scale to
        UVW's for the given stage.

        This call is appropriate for 3-d texture coordinates.

        `(self, other: NodePath, stage: TextureStage, scale: float)`:
        Sets a texture matrix on the current node to apply the indicated scale to
        UV's for the given stage.

        This call is appropriate for 2-d or 3-d texture coordinates.

        `(self, stage: TextureStage, scale: float)`:
        Sets a texture matrix on the current node to apply the indicated scale to
        UVW's for the given stage.

        This call is appropriate for 2-d or 3-d texture coordinates.
        """
    @overload
    def set_tex_scale(self, other: NodePath, stage: TextureStage, scale: Vec2Like | Vec3Like | float) -> None: ...
    @overload
    def set_tex_scale(self, stage: TextureStage, su: float, sv: float, sw: float = ...) -> None: ...
    @overload
    def set_tex_scale(self, other: NodePath, stage: TextureStage, su: float, sv: float, sw: float = ...) -> None: ...
    @overload
    def get_tex_offset(self, stage: TextureStage) -> LVecBase2:
        """Returns the offset set for the UV's for the given stage on the current
        node.

        This call is appropriate for ordinary 2-d texture coordinates.
        """
    @overload
    def get_tex_offset(self, other: NodePath, stage: TextureStage) -> LVecBase2: ...
    @overload
    def get_tex_rotate(self, stage: TextureStage) -> float:
        """Returns the rotation set for the UV's for the given stage on the current
        node.

        This call is appropriate for ordinary 2-d texture coordinates.
        """
    @overload
    def get_tex_rotate(self, other: NodePath, stage: TextureStage) -> float: ...
    @overload
    def get_tex_scale(self, stage: TextureStage) -> LVecBase2:
        """Returns the scale set for the UV's for the given stage on the current node.

        This call is appropriate for ordinary 2-d texture coordinates.
        """
    @overload
    def get_tex_scale(self, other: NodePath, stage: TextureStage) -> LVecBase2: ...
    @overload
    def set_tex_pos(self, stage: TextureStage, uvw: Vec3Like) -> None:
        """Sets a texture matrix on the current node to apply the indicated offset to
        UVW's for the given stage.

        This call is appropriate for 3-d texture coordinates.
        """
    @overload
    def set_tex_pos(self, other: NodePath, stage: TextureStage, uvw: Vec3Like) -> None: ...
    @overload
    def set_tex_pos(self, stage: TextureStage, u: float, v: float, w: float) -> None: ...
    @overload
    def set_tex_pos(self, other: NodePath, stage: TextureStage, u: float, v: float, w: float) -> None: ...
    @overload
    def set_tex_hpr(self, stage: TextureStage, hpr: Vec3Like) -> None:
        """Sets a texture matrix on the current node to apply the indicated rotation,
        as a 3-D HPR, to UVW's for the given stage.

        This call is appropriate for 3-d texture coordinates.
        """
    @overload
    def set_tex_hpr(self, other: NodePath, stage: TextureStage, hpr: Vec3Like) -> None: ...
    @overload
    def set_tex_hpr(self, stage: TextureStage, h: float, p: float, r: float) -> None: ...
    @overload
    def set_tex_hpr(self, other: NodePath, stage: TextureStage, h: float, p: float, r: float) -> None: ...
    @overload
    def get_tex_pos(self, stage: TextureStage) -> LVecBase3:
        """Returns the offset set for the UVW's for the given stage on the current
        node.

        This call is appropriate for 3-d texture coordinates.
        """
    @overload
    def get_tex_pos(self, other: NodePath, stage: TextureStage) -> LVecBase3: ...
    @overload
    def get_tex_hpr(self, stage: TextureStage) -> LVecBase3:
        """Returns the 3-D HPR set for the UVW's for the given stage on the current
        node.

        This call is appropriate for 3-d texture coordinates.
        """
    @overload
    def get_tex_hpr(self, other: NodePath, stage: TextureStage) -> LVecBase3: ...
    @overload
    def get_tex_scale_3d(self, stage: TextureStage) -> LVecBase3:
        """Returns the scale set for the UVW's for the given stage on the current
        node.

        This call is appropriate for 3-d texture coordinates.
        """
    @overload
    def get_tex_scale_3d(self, other: NodePath, stage: TextureStage) -> LVecBase3: ...
    @overload
    def set_tex_gen(self, stage: TextureStage, mode: _RenderAttrib_TexGenMode, priority: int = ...) -> None:
        """`(self, stage: TextureStage, mode: _RenderAttrib_TexGenMode, constant_value: LTexCoord3, priority: int = ...)`:
        Enables automatic texture coordinate generation for the indicated texture
        stage.  This version of this method is useful when setting M_constant,
        which requires a constant texture coordinate value.

        `(self, stage: TextureStage, mode: _RenderAttrib_TexGenMode, priority: int = ...)`:
        Enables automatic texture coordinate generation for the indicated texture
        stage.
        """
    @overload
    def set_tex_gen(
        self, stage: TextureStage, mode: _RenderAttrib_TexGenMode, constant_value: Vec3Like, priority: int = ...
    ) -> None: ...
    def clear_tex_gen(self, stage: TextureStage = ...) -> None:
        """`(self)`:
        Removes the texture coordinate generation mode from all texture stages on
        this node.

        `(self, stage: TextureStage)`:
        Disables automatic texture coordinate generation for the indicated texture
        stage.
        """
    def has_tex_gen(self, stage: TextureStage) -> bool:
        """Returns true if there is a mode for automatic texture coordinate generation
        on the current node for the given stage.
        """
    def get_tex_gen(self, stage: TextureStage) -> _RenderAttrib_TexGenMode:
        """Returns the texture coordinate generation mode for the given stage, or
        M_off if there is no explicit mode set for the given stage.
        """
    def set_tex_projector(self, stage: TextureStage, _from: NodePath, to: NodePath, lens_index: int = ...) -> None:
        """Establishes a TexProjectorEffect on this node, which can be used to
        establish projective texturing (but see also the
        NodePath::project_texture() convenience function), or it can be used to
        bind this node's texture transform to particular node's position in space,
        allowing a LerpInterval (for instance) to adjust this node's texture
        coordinates.

        If to is a LensNode, then the fourth parameter, lens_index, can be provided
        to select a particular lens to apply.  Otherwise lens_index is not used.
        """
    def clear_tex_projector(self, stage: TextureStage = ...) -> None:
        """`(self)`:
        Removes the TexProjectorEffect for all stages from this node.

        `(self, stage: TextureStage)`:
        Removes the TexProjectorEffect for the indicated stage from this node.
        """
    def has_tex_projector(self, stage: TextureStage) -> bool:
        """Returns true if this node has a TexProjectorEffect for the indicated stage,
        false otherwise.
        """
    def get_tex_projector_from(self, stage: TextureStage) -> NodePath:
        """Returns the "from" node associated with the TexProjectorEffect on the
        indicated stage.  The relative transform between the "from" and the "to"
        nodes is automatically applied to the texture transform each frame.
        """
    def get_tex_projector_to(self, stage: TextureStage) -> NodePath:
        """Returns the "to" node associated with the TexProjectorEffect on the
        indicated stage.  The relative transform between the "from" and the "to"
        nodes is automatically applied to the texture transform each frame.
        """
    def project_texture(self, stage: TextureStage, tex: Texture, projector: NodePath) -> None:
        """A convenience function to enable projective texturing at this node level
        and below, using the indicated NodePath (which should contain a LensNode)
        as the projector.
        """
    def clear_project_texture(self, stage: TextureStage) -> None:
        """Undoes the effect of project_texture()."""
    def has_texcoord(self, texcoord_name: str) -> bool:
        """Returns true if there are at least some vertices at this node and below
        that use the named texture coordinate set, false otherwise.  Pass the empty
        string for the default texture coordinate set.
        """
    def has_vertex_column(self, name: InternalName | str) -> bool:
        """Returns true if there are at least some vertices at this node and below
        that contain a reference to the indicated vertex data column name, false
        otherwise.

        This is particularly useful for testing whether a particular model has a
        given texture coordinate set (but see has_texcoord()).
        """
    def find_all_vertex_columns(self, name: str = ...) -> InternalNameCollection:
        """`(self)`:
        Returns a list of all vertex array columns stored on some geometry found at
        this node level and below.

        `(self, name: str)`:
        Returns a list of all vertex array columns stored on some geometry found at
        this node level and below that match the indicated name (which may contain
        wildcard characters).
        """
    def find_all_texcoords(self, name: str = ...) -> InternalNameCollection:
        """`(self)`:
        Returns a list of all texture coordinate sets used by any geometry at this
        node level and below.

        `(self, name: str)`:
        Returns a list of all texture coordinate sets used by any geometry at this
        node level and below that match the indicated name (which may contain
        wildcard characters).
        """
    @overload
    def find_texture(self, stage: TextureStage) -> Texture:
        """`(self, stage: TextureStage)`:
        Returns the first texture found applied to geometry at this node or below
        that is assigned to the indicated texture stage.  Returns the texture if it
        is found, or NULL if it is not.

        `(self, name: str)`:
        Returns the first texture found applied to geometry at this node or below
        that matches the indicated name (which may contain wildcards).  Returns the
        texture if it is found, or NULL if it is not.
        """
    @overload
    def find_texture(self, name: str) -> Texture: ...
    @overload
    def find_all_textures(self, stage: TextureStage = ...) -> TextureCollection:
        """`(self)`:
        Returns a list of a textures applied to geometry at this node and below.

        `(self, stage: TextureStage)`:
        Returns a list of a textures on geometry at this node and below that are
        assigned to the indicated texture stage.

        `(self, name: str)`:
        Returns a list of a textures applied to geometry at this node and below
        that match the indicated name (which may contain wildcard characters).
        """
    @overload
    def find_all_textures(self, name: str) -> TextureCollection: ...
    def find_texture_stage(self, name: str) -> TextureStage:
        """Returns the first TextureStage found applied to geometry at this node or
        below that matches the indicated name (which may contain wildcards).
        Returns the TextureStage if it is found, or NULL if it is not.
        """
    def find_all_texture_stages(self, name: str = ...) -> TextureStageCollection:
        """`(self)`:
        Returns a list of a TextureStages applied to geometry at this node and
        below.

        `(self, name: str)`:
        Returns a list of a TextureStages applied to geometry at this node and
        below that match the indicated name (which may contain wildcard
        characters).
        """
    def unify_texture_stages(self, stage: TextureStage) -> None:
        """Searches through all TextureStages at this node and below.  Any
        TextureStages that share the same name as the indicated TextureStage object
        are replaced with this object, thus ensuring that all geometry at this node
        and below with a particular TextureStage name is using the same
        TextureStage object.
        """
    def find_material(self, name: str) -> Material:
        """Returns the first material found applied to geometry at this node or below
        that matches the indicated name (which may contain wildcards).  Returns the
        material if it is found, or NULL if it is not.
        """
    def find_all_materials(self, name: str = ...) -> MaterialCollection:
        """`(self)`:
        Returns a list of a materials applied to geometry at this node and below.

        `(self, name: str)`:
        Returns a list of a materials applied to geometry at this node and below
        that match the indicated name (which may contain wildcard characters).
        """
    def set_material(self, tex: Material, priority: int = ...) -> None:
        """Sets the geometry at this level and below to render using the indicated
        material.

        Previously, this operation made a copy of the material structure, but
        nowadays it assigns the pointer directly.
        """
    def set_material_off(self, priority: int = ...) -> None:
        """Sets the geometry at this level and below to render using no material.
        This is normally the default, but it may be useful to use this to
        contradict set_material() at a higher node level (or, with a priority, to
        override a set_material() at a lower level).
        """
    def clear_material(self) -> None:
        """Completely removes any material adjustment that may have been set via
        set_material() from this particular node.
        """
    def has_material(self) -> bool:
        """Returns true if a material has been applied to this particular node via
        set_material(), false otherwise.
        """
    def get_material(self) -> Material:
        """Returns the material that has been set on this particular node, or NULL if
        no material has been set.  This is not necessarily the material that will
        be applied to the geometry at or below this level, as another material at a
        higher or lower level may override.

        See also find_material().
        """
    def replace_material(self, mat: Material, new_mat: Material | None) -> None:
        """`(self, mat: Material, new_mat: Material)`:
        Recursively searches the scene graph for references to the given material,
        and replaces them with the new material.

        As of Panda3D 1.10.13, new_mat may be null to remove the material.

        @since 1.10.0

        `(self, mat: Material, new_mat: None)`:
        Let interrogate know this also accepts None
        """
    def set_fog(self, fog: Fog, priority: int = ...) -> None:
        """Sets the geometry at this level and below to render using the indicated
        fog.
        """
    def set_fog_off(self, priority: int = ...) -> None:
        """Sets the geometry at this level and below to render using no fog.  This is
        normally the default, but it may be useful to use this to contradict
        set_fog() at a higher node level (or, with a priority, to override a
        set_fog() at a lower level).
        """
    def clear_fog(self) -> None:
        """Completely removes any fog adjustment that may have been set via set_fog()
        or set_fog_off() from this particular node.  This allows whatever fogs
        might be otherwise affecting the geometry to show instead.
        """
    def has_fog(self) -> bool:
        """Returns true if a fog has been applied to this particular node via
        set_fog(), false otherwise.  This is not the same thing as asking whether
        the geometry at this node will be rendered with fog, as there may be a fog
        in effect from a higher or lower level.
        """
    def has_fog_off(self) -> bool:
        """Returns true if a fog has been specifically disabled on this particular
        node via set_fog_off(), false otherwise.  This is not the same thing as
        asking whether the geometry at this node will be rendered unfogged, as
        there may be a fog in effect from a higher or lower level.
        """
    def get_fog(self) -> Fog:
        """Returns the fog that has been set on this particular node, or NULL if no
        fog has been set.  This is not necessarily the fog that will be applied to
        the geometry at or below this level, as another fog at a higher or lower
        level may override.
        """
    def set_render_mode_wireframe(self, priority: int = ...) -> None:
        """Sets up the geometry at this level and below (unless overridden) to render
        in wireframe mode.
        """
    def set_render_mode_filled(self, priority: int = ...) -> None:
        """Sets up the geometry at this level and below (unless overridden) to render
        in filled (i.e.  not wireframe) mode.
        """
    def set_render_mode_filled_wireframe(self, wireframe_color: Vec4Like, priority: int = ...) -> None:
        """Sets up the geometry at this level and below (unless overridden) to render
        in filled, but overlay the wireframe on top with a fixed color.  This is
        useful for debug visualizations.
        """
    def set_render_mode_thickness(self, thickness: float, priority: int = ...) -> None:
        """Sets up the point geometry at this level and below to render as thick
        points (that is, billboarded quads).  The thickness is in pixels, unless
        set_render_mode_perspective is also true, in which case it is in 3-D units.

        If you want the quads to be individually textured, you should also set a
        TexGenAttrib::M_point_sprite on the node.
        """
    def set_render_mode_perspective(self, perspective: bool, priority: int = ...) -> None:
        """Sets up the point geometry at this level and below to render as perspective
        sprites (that is, billboarded quads).  The thickness, as specified with
        set_render_mode_thickness(), is the width of each point in 3-D units,
        unless it is overridden on a per-vertex basis.  This does not affect
        geometry other than points.

        If you want the quads to be individually textured, you should also set a
        TexGenAttrib::M_point_sprite on the node.
        """
    def set_render_mode(self, mode: _RenderModeAttrib_Mode, thickness: float, priority: int = ...) -> None:
        """Sets up the geometry at this level and below (unless overridden) to render
        in the specified mode and with the indicated line and/or point thickness.
        """
    def clear_render_mode(self) -> None:
        """Completely removes any render mode adjustment that may have been set on
        this node via set_render_mode_wireframe() or set_render_mode_filled().
        """
    def has_render_mode(self) -> bool:
        """Returns true if a render mode has been explicitly set on this particular
        node via set_render_mode() (or set_render_mode_wireframe() or
        set_render_mode_filled()), false otherwise.
        """
    def get_render_mode(self) -> _RenderModeAttrib_Mode:
        """Returns the render mode that has been specifically set on this node via
        set_render_mode(), or M_unchanged if nothing has been set.
        """
    def get_render_mode_thickness(self) -> float:
        """Returns the render mode thickness that has been specifically set on this
        node via set_render_mode(), or 1.0 if nothing has been set.
        """
    def get_render_mode_perspective(self) -> bool:
        """Returns the flag that has been set on this node via
        set_render_mode_perspective(), or false if no flag has been set.
        """
    def set_two_sided(self, two_sided: bool, priority: int = ...) -> None:
        """Specifically sets or disables two-sided rendering mode on this particular
        node.  If no other nodes override, this will cause backfacing polygons to
        be drawn (in two-sided mode, true) or culled (in one-sided mode, false).
        """
    def clear_two_sided(self) -> None:
        """Completely removes any two-sided adjustment that may have been set on this
        node via set_two_sided(). The geometry at this level and below will
        subsequently be rendered either two-sided or one-sided, according to
        whatever other nodes may have had set_two_sided() on it, or according to
        the initial state otherwise.
        """
    def has_two_sided(self) -> bool:
        """Returns true if a two-sided adjustment has been explicitly set on this
        particular node via set_two_sided().  If this returns true, then
        get_two_sided() may be called to determine which has been set.
        """
    def get_two_sided(self) -> bool:
        """Returns true if two-sided rendering has been specifically set on this node
        via set_two_sided(), or false if one-sided rendering has been specifically
        set, or if nothing has been specifically set.  See also has_two_sided().
        This does not necessarily imply that the geometry will or will not be
        rendered two-sided, as there may be other nodes that override.
        """
    def set_depth_test(self, depth_test: bool, priority: int = ...) -> None:
        """Specifically sets or disables the testing of the depth buffer on this
        particular node.  This is normally on in the 3-d scene graph and off in the
        2-d scene graph; it should be on for rendering most 3-d objects properly.
        """
    def clear_depth_test(self) -> None:
        """Completely removes any depth-test adjustment that may have been set on this
        node via set_depth_test().
        """
    def has_depth_test(self) -> bool:
        """Returns true if a depth-test adjustment has been explicitly set on this
        particular node via set_depth_test().  If this returns true, then
        get_depth_test() may be called to determine which has been set.
        """
    def get_depth_test(self) -> bool:
        """Returns true if depth-test rendering has been specifically set on this node
        via set_depth_test(), or false if depth-test rendering has been
        specifically disabled.  If nothing has been specifically set, returns true.
        See also has_depth_test().
        """
    def set_depth_write(self, depth_write: bool, priority: int = ...) -> None:
        """Specifically sets or disables the writing to the depth buffer on this
        particular node.  This is normally on in the 3-d scene graph and off in the
        2-d scene graph; it should be on for rendering most 3-d objects properly.
        """
    def clear_depth_write(self) -> None:
        """Completely removes any depth-write adjustment that may have been set on
        this node via set_depth_write().
        """
    def has_depth_write(self) -> bool:
        """Returns true if a depth-write adjustment has been explicitly set on this
        particular node via set_depth_write().  If this returns true, then
        get_depth_write() may be called to determine which has been set.
        """
    def get_depth_write(self) -> bool:
        """Returns true if depth-write rendering has been specifically set on this
        node via set_depth_write(), or false if depth-write rendering has been
        specifically disabled.  If nothing has been specifically set, returns true.
        See also has_depth_write().
        """
    def set_depth_offset(self, bias: int, priority: int = ...) -> None:
        """This instructs the graphics driver to apply an offset or bias to the
        generated depth values for rendered polygons, before they are written to
        the depth buffer.  This can be used to shift polygons forward slightly, to
        resolve depth conflicts, or self-shadowing artifacts on thin objects.  The
        bias is always an integer number, and each integer increment represents the
        smallest possible increment in Z that is sufficient to completely resolve
        two coplanar polygons.  Positive numbers are closer towards the camera.
        """
    def clear_depth_offset(self) -> None:
        """Completely removes any depth-offset adjustment that may have been set on
        this node via set_depth_offset().
        """
    def has_depth_offset(self) -> bool:
        """Returns true if a depth-offset adjustment has been explicitly set on this
        particular node via set_depth_offset().  If this returns true, then
        get_depth_offset() may be called to determine which has been set.
        """
    def get_depth_offset(self) -> int:
        """Returns the depth offset value if it has been specified using
        set_depth_offset, or 0 if not.
        """
    def do_billboard_axis(self, camera: NodePath, offset: float) -> None:
        """Performs a billboard-type rotate to the indicated camera node, one time
        only, and leaves the object rotated.  This is similar in principle to
        heads_up().
        """
    def do_billboard_point_eye(self, camera: NodePath, offset: float) -> None:
        """Performs a billboard-type rotate to the indicated camera node, one time
        only, and leaves the object rotated.  This is similar in principle to
        look_at(), although the point_eye billboard effect cannot be achieved using
        the ordinary look_at() call.
        """
    def do_billboard_point_world(self, camera: NodePath, offset: float) -> None:
        """Performs a billboard-type rotate to the indicated camera node, one time
        only, and leaves the object rotated.  This is similar in principle to
        look_at().
        """
    @overload
    def set_billboard_axis(self, offset: float = ...) -> None:
        """`(self, camera: NodePath, offset: float)`:
        Puts a billboard transition on the node such that it will rotate in two
        dimensions around the up axis, towards a specified "camera" instead of to
        the viewing camera.

        `(self, offset: float = ...)`:
        Puts a billboard transition on the node such that it will rotate in two
        dimensions around the up axis.
        """
    @overload
    def set_billboard_axis(self, camera: NodePath, offset: float) -> None: ...
    @overload
    def set_billboard_point_eye(self, offset: float = ..., fixed_depth: bool = ...) -> None:
        """`(self, camera: NodePath, offset: float, fixed_depth: bool = ...)`:
        Puts a billboard transition on the node such that it will rotate in three
        dimensions about the origin, keeping its up vector oriented to the top of
        the camera, towards a specified "camera" instead of to the viewing camera.

        `(self, offset: float = ..., fixed_depth: bool = ...)`:
        Puts a billboard transition on the node such that it will rotate in three
        dimensions about the origin, keeping its up vector oriented to the top of
        the camera.
        """
    @overload
    def set_billboard_point_eye(self, camera: NodePath, offset: float, fixed_depth: bool = ...) -> None: ...
    @overload
    def set_billboard_point_world(self, offset: float = ...) -> None:
        """`(self, camera: NodePath, offset: float)`:
        Puts a billboard transition on the node such that it will rotate in three
        dimensions about the origin, keeping its up vector oriented to the sky,
        towards a specified "camera" instead of to the viewing camera.

        `(self, offset: float = ...)`:
        Puts a billboard transition on the node such that it will rotate in three
        dimensions about the origin, keeping its up vector oriented to the sky.
        """
    @overload
    def set_billboard_point_world(self, camera: NodePath, offset: float) -> None: ...
    def clear_billboard(self) -> None:
        """Removes any billboard effect from the node."""
    def has_billboard(self) -> bool:
        """Returns true if there is any billboard effect on the node."""
    def set_compass(self, reference: NodePath = ...) -> None:
        """Puts a compass effect on the node, so that it will retain a fixed rotation
        relative to the reference node (or render if the reference node is empty)
        regardless of the transforms above it.
        """
    def clear_compass(self) -> None:
        """Removes any compass effect from the node."""
    def has_compass(self) -> bool:
        """Returns true if there is any compass effect on the node."""
    def set_transparency(self, mode: _TransparencyAttrib_Mode, priority: int = ...) -> None:
        """Specifically sets or disables transparent rendering mode on this particular
        node.  If no other nodes override, this will cause items with a non-1 value
        for alpha color to be rendered partially transparent.
        """
    def clear_transparency(self) -> None:
        """Completely removes any transparency adjustment that may have been set on
        this node via set_transparency(). The geometry at this level and below will
        subsequently be rendered either transparent or not, to whatever other nodes
        may have had set_transparency() on them.
        """
    def has_transparency(self) -> bool:
        """Returns true if a transparent-rendering adjustment has been explicitly set
        on this particular node via set_transparency().  If this returns true, then
        get_transparency() may be called to determine whether transparency has been
        explicitly enabled or explicitly disabled for this node.
        """
    def get_transparency(self) -> _TransparencyAttrib_Mode:
        """Returns the transparent rendering that has been specifically set on this
        node via set_transparency(), or M_none if nontransparent rendering has been
        specifically set, or if nothing has been specifically set.  See also
        has_transparency().  This does not necessarily imply that the geometry will
        or will not be rendered transparent, as there may be other nodes that
        override.
        """
    def set_logic_op(self, op: _LogicOpAttrib_Operation, priority: int = ...) -> None:
        """Specifically sets or disables a logical operation on this particular node.
        If no other nodes override, this will cause geometry to be rendered without
        color blending but instead using the given logical operator.

        @since 1.10.0
        """
    def clear_logic_op(self) -> None:
        """Completely removes any logical operation that may have been set on this
        node via set_logic_op(). The geometry at this level and below will
        subsequently be rendered using standard color blending.

        @since 1.10.0
        """
    def has_logic_op(self) -> bool:
        """Returns true if a logical operation has been explicitly set on this
        particular node via set_logic_op().  If this returns true, then
        get_logic_op() may be called to determine whether a logical operation has
        been explicitly disabled for this node or set to particular operation.

        @since 1.10.0
        """
    def get_logic_op(self) -> _LogicOpAttrib_Operation:
        """Returns the logical operation that has been specifically set on this node
        via set_logic_op(), or O_none if standard color blending has been
        specifically set, or if nothing has been specifically set.  See also
        has_logic_op().  This does not necessarily imply that the geometry will
        or will not be rendered with the given logical operation, as there may be
        other nodes that override.

        @since 1.10.0
        """
    def set_antialias(self, mode: int, priority: int = ...) -> None:
        """Specifies the antialiasing type that should be applied at this node and
        below.  See AntialiasAttrib.
        """
    def clear_antialias(self) -> None:
        """Completely removes any antialias setting that may have been set on this
        node via set_antialias().
        """
    def has_antialias(self) -> bool:
        """Returns true if an antialias setting has been explicitly mode on this
        particular node via set_antialias().  If this returns true, then
        get_antialias() may be called to determine what the setting was.
        """
    def get_antialias(self) -> int:
        """Returns the antialias setting that has been specifically set on this node
        via set_antialias(), or M_none if no setting has been made.
        """
    def has_audio_volume(self) -> bool:
        """Returns true if an audio volume has been applied to the referenced node,
        false otherwise.  It is still possible that volume at this node might have
        been scaled by an ancestor node.
        """
    def clear_audio_volume(self) -> None:
        """Completely removes any audio volume from the referenced node.  This is
        preferable to simply setting the audio volume to identity, as it also
        removes the overhead associated with having an audio volume at all.
        """
    def set_audio_volume(self, volume: float, priority: int = ...) -> None:
        """Sets the audio volume component of the transform"""
    def set_audio_volume_off(self, priority: int = ...) -> None:
        """Disables any audio volume attribute inherited from above.  This is not the
        same thing as clear_audio_volume(), which undoes any previous
        set_audio_volume() operation on this node; rather, this actively disables
        any set_audio_volume() that might be inherited from a parent node.

        It is legal to specify a new volume on the same node with a subsequent call
        to set_audio_volume(); this new scale will apply to lower nodes.
        """
    def get_audio_volume(self) -> float:
        """Returns the complete audio volume that has been applied to this node via a
        previous call to set_audio_volume(), or 1. (identity) if no volume has been
        applied to this particular node.
        """
    def get_net_audio_volume(self) -> float:
        """Returns the complete audio volume for this node taking highers nodes in the
        graph into account.
        """
    def adjust_all_priorities(self, adjustment: int) -> None:
        """Adds the indicated adjustment amount (which may be negative) to the
        priority for all transitions on the referenced node, and for all nodes in
        the subgraph below.  This can be used to force these nodes not to be
        overridden by a high-level state change above.  If the priority would drop
        below zero, it is set to zero.
        """
    def show(self, camera_mask: DrawMask | int = ...) -> None:
        """`(self)`:
        Undoes the effect of a previous hide() on this node: makes the referenced
        node (and the entire subgraph below this node) visible to all cameras.

        This will not reveal the node if a parent node has been hidden.

        `(self, camera_mask: DrawMask)`:
        Makes the referenced node visible just to the cameras whose camera_mask
        shares the indicated bits.

        This undoes the effect of a previous hide() call.  It will not reveal the
        node if a parent node has been hidden.  However, see show_through().
        """
    def show_through(self, camera_mask: DrawMask | int = ...) -> None:
        """`(self)`:
        Makes the referenced node visible just to the cameras whose camera_mask
        shares the indicated bits.

        Unlike show(), this will reveal the node even if a parent node has been
        hidden, thus "showing through" a parent's hide().

        `(self, camera_mask: DrawMask)`:
        Makes the referenced node visible just to the cameras whose camera_mask
        shares the indicated bits.

        Unlike show(), this will reveal the node even if a parent node has been
        hidden via the one-parameter hide() method, thus "showing through" a
        parent's hide().  (However, it will not show through a parent's hide() call
        if the no-parameter form of hide() was used.)
        """
    def hide(self, camera_mask: DrawMask | int = ...) -> None:
        """`(self)`:
        Makes the referenced node (and the entire subgraph below this node)
        invisible to all cameras.  It remains part of the scene graph, its bounding
        volume still contributes to its parent's bounding volume, and it will still
        be involved in collision tests.

        To undo this, call show().

        `(self, camera_mask: DrawMask)`:
        Makes the referenced node invisible just to the cameras whose camera_mask
        shares the indicated bits.

        This will also hide any nodes below this node in the scene graph, including
        those nodes for which show() has been called, but it will not hide
        descendent nodes for which show_through() has been called.
        """
    def is_hidden(self, camera_mask: DrawMask | int = ...) -> bool:
        """Returns true if the referenced node is hidden from the indicated camera(s)
        either directly, or because some ancestor is hidden.
        """
    def get_hidden_ancestor(self, camera_mask: DrawMask | int = ..., current_thread: Thread = ...) -> NodePath:
        """Returns the NodePath at or above the referenced node that is hidden to the
        indicated camera(s), or an empty NodePath if no ancestor of the referenced
        node is hidden (and the node should be visible).
        """
    def stash(self, sort: int = ..., current_thread: Thread = ...) -> None:
        """Removes the referenced node (and the entire subgraph below this node) from
        the scene graph in any normal sense.  The node will no longer be visible
        and is not tested for collisions; furthermore, no normal scene graph
        traversal will visit the node.  The node's bounding volume no longer
        contributes to its parent's bounding volume.

        A stashed node cannot be located by a normal find() operation (although a
        special find string can still retrieve it).
        """
    def unstash(self, sort: int = ..., current_thread: Thread = ...) -> None:
        """Undoes the effect of a previous stash() on this node: makes the referenced
        node (and the entire subgraph below this node) once again part of the scene
        graph.
        """
    def unstash_all(self, current_thread: Thread = ...) -> None:
        """Unstashes this node and all stashed child nodes."""
    def is_stashed(self) -> bool:
        """Returns true if the referenced node is stashed either directly, or because
        some ancestor is stashed.
        """
    def get_stashed_ancestor(self, current_thread: Thread = ...) -> NodePath:
        """Returns the NodePath at or above the referenced node that is stashed, or an
        empty NodePath if no ancestor of the referenced node is stashed (and the
        node should be visible).
        """
    def get_collide_mask(self) -> CollideMask:
        """Returns the union of all of the into_collide_masks for nodes at this level
        and below.  This is the same thing as node()->get_net_collide_mask().

        If you want to return what the into_collide_mask of this node itself is,
        without regard to its children, use node()->get_into_collide_mask().
        """
    def set_collide_mask(
        self, new_mask: CollideMask | int, bits_to_change: CollideMask | int = ..., node_type: TypeHandle | type = ...
    ) -> None:
        """Recursively applies the indicated CollideMask to the into_collide_masks for
        all nodes at this level and below.  If node_type is not TypeHandle::none(),
        then only nodes matching (or inheriting from) the indicated PandaNode
        subclass are modified.

        The default is to change all bits, but if bits_to_change is not all bits
        on, then only the bits that are set in bits_to_change are modified,
        allowing this call to change only a subset of the bits in the subgraph.
        """
    def compare_to(self, other: NodePath | WeakNodePath) -> int:
        """Returns a number less than zero if this NodePath sorts before the other
        one, greater than zero if it sorts after, or zero if they are equivalent.

        Two NodePaths are considered equivalent if they consist of exactly the same
        list of nodes in the same order.  Otherwise, they are different; different
        NodePaths will be ranked in a consistent but undefined ordering; the
        ordering is useful only for placing the NodePaths in a sorted container
        like an STL set.
        """
    def verify_complete(self, current_thread: Thread = ...) -> bool:
        """Returns true if all of the nodes described in the NodePath are connected,
        or false otherwise.
        """
    def premunge_scene(self, gsg: GraphicsStateGuardianBase = ...) -> None:
        """Walks through the scene graph beginning at the bottom node, and internally
        adjusts any GeomVertexFormats for optimal rendering on the indicated GSG.
        If this step is not done prior to rendering, the formats will be optimized
        at render time instead, for a small cost.

        It is not normally necessary to do this on a model loaded directly from
        disk, since the loader will do this by default.
        """
    def prepare_scene(self, gsg: GraphicsStateGuardianBase) -> None:
        """Walks through the scene graph beginning at the bottom node, and does
        whatever initialization is required to render the scene properly with the
        indicated GSG.  It is not strictly necessary to call this, since the GSG
        will initialize itself when the scene is rendered, but this may take some
        of the overhead away from that process.

        In particular, this will ensure that textures and vertex buffers within the
        scene are loaded into graphics memory.
        """
    def show_bounds(self) -> None:
        """Causes the bounding volume of the bottom node and all of its descendants
        (that is, the bounding volume associated with the the bottom arc) to be
        rendered, if possible.  The rendering method is less than optimal; this is
        intended primarily for debugging.
        """
    def show_tight_bounds(self) -> None:
        """Similar to show_bounds(), this draws a bounding box representing the
        "tight" bounds of this node and all of its descendants.  The bounding box
        is recomputed every frame by reexamining all of the vertices; this is far
        from efficient, but this is intended for debugging.
        """
    def hide_bounds(self) -> None:
        """Stops the rendering of the bounding volume begun with show_bounds()."""
    def get_bounds(self, current_thread: Thread = ...) -> BoundingVolume:
        """Returns a newly-allocated bounding volume containing the bottom node and
        all of its descendants.  This is the bounding volume on the bottom arc,
        converted to the local coordinate space of the node.
        """
    def force_recompute_bounds(self) -> None:
        """Forces the recomputing of all the bounding volumes at every node in the
        subgraph beginning at this node and below.

        This should not normally need to be called, since the bounding volumes are
        supposed to be recomputed automatically when necessary.  It may be useful
        when debugging, to verify that the bounding volumes have not become
        inadvertently stale; it may also be useful to force animated characters to
        update their bounding volumes (which does not presently happen
        automatically).
        """
    def write_bounds(self, out: ostream) -> None:
        """Writes a description of the bounding volume containing the bottom node and
        all of its descendants to the indicated output stream.
        """
    def calc_tight_bounds(
        self, min_point: Vec3Like, max_point: Vec3Like, other: NodePath = ..., current_thread: Thread = ...
    ) -> bool:
        """Calculates the minimum and maximum vertices of all Geoms at this NodePath's
        bottom node and below.  This is a tight bounding box; it will generally be
        tighter than the bounding volume returned by get_bounds() (but it is more
        expensive to compute).

        The bounding box is computed relative to the parent node's coordinate
        system by default.  You can optionally specify a different NodePath to
        compute the bounds relative to.  Note that the box is always axis-aligned
        against the given NodePath's coordinate system, so you might get a
        differently sized box depending on which node you pass.

        The return value is true if any points are within the bounding volume, or
        false if none are.
        """
    def get_tight_bounds(self, other: NodePath = ...) -> tuple[LPoint3f, LPoint3f] | None: ...
    def flatten_light(self) -> Literal[0]:
        """Lightly flattens out the hierarchy below this node by applying transforms,
        colors, and texture matrices from the nodes onto the vertices, but does not
        remove any nodes.

        This can result in improved rendering performance because there will be
        fewer transforms in the resulting scene graph, but the number of nodes will
        remain the same.

        In particular, any NodePaths that reference nodes within this hierarchy
        will not be damaged.  However, since this operation will remove transforms
        from the scene graph, it may be dangerous to apply to nodes where you
        expect to dynamically modify the transform, or where you expect the
        geometry to remain in a particular local coordinate system.

        The return value is always 0, since flatten_light does not remove any
        nodes.
        """
    def flatten_medium(self) -> int:
        """A more thorough flattening than flatten_light(), this first applies all the
        transforms, colors, and texture matrices from the nodes onto the vertices,
        and then removes unneeded grouping nodes--nodes that have exactly one
        child, for instance, but have no special properties in themselves.

        This results in improved performance over flatten_light() because the
        number of nodes in the scene graph is reduced.

        The return value is the number of nodes removed.
        """
    def flatten_strong(self) -> int:
        """The strongest possible flattening.  This first applies all of the
        transforms to the vertices, as in flatten_medium(), but then it will
        combine sibling nodes together when possible, in addition to removing
        unnecessary parent-child nodes.  This can result in substantially fewer
        nodes, but any nicely-grouped hierachical bounding volumes may be lost.

        It is generally a good idea to apply this kind of flattening only to nodes
        that will be culled largely as a single unit, like a car.  Applying this to
        an entire scene may result in overall poorer performance because of less-
        effective culling.
        """
    def apply_texture_colors(self) -> None:
        """Removes textures from Geoms at this node and below by applying the texture
        colors to the vertices.  This is primarily useful to simplify a low-LOD
        model.  The texture colors are replaced by flat colors that approximate the
        original textures.

        Only the bottommost texture on each Geom is used (if there is more than
        one), and it is applied as if it were M_modulate, and WM_repeat, regardless
        of its actual settings.  If the texture has a simple_ram_image, this may be
        used if the main image isn't resident.

        After this call, there will be no texturing specified at this level and
        below.  Of course, there might still be texturing inherited from above.
        """
    def clear_model_nodes(self) -> int:
        """Recursively walks through the scene graph at this level and below, looking
        for ModelNodes, and calls model_node->set_preserve_transform(PT_drop_node)
        on each one.  This allows a subsequent call to flatten_strong() to
        eliminate all of the ModelNodes.

        Returns the number of ModelNodes found.
        """
    def set_tag(self, key: str, value: str) -> None:
        """Associates a user-defined value with a user-defined key which is stored on
        the node.  This value has no meaning to Panda; but it is stored
        indefinitely on the node until it is requested again.

        Each unique key stores a different string value.  There is no effective
        limit on the number of different keys that may be stored or on the length
        of any one key's value.
        """
    def get_tag(self, key: str) -> str:
        """Retrieves the user-defined value that was previously set on this node for
        the particular key, if any.  If no value has been previously set, returns
        the empty string.  See also get_net_tag().
        """
    def get_tag_keys(self) -> tuple[str, ...] | None: ...
    def has_tag(self, key: str) -> bool:
        """Returns true if a value has been defined on this node for the particular
        key (even if that value is the empty string), or false if no value has been
        set.  See also has_net_tag().
        """
    def clear_tag(self, key: str) -> None:
        """Removes the value defined for this key on this particular node.  After a
        call to clear_tag(), has_tag() will return false for the indicated key.
        """
    def get_net_tag(self, key: str) -> str:
        """Returns the tag value that has been defined on this node, or the nearest
        ancestor node, for the indicated key.  If no value has been defined for the
        indicated key on any ancestor node, returns the empty string.  See also
        get_tag().
        """
    def has_net_tag(self, key: str) -> bool:
        """Returns true if the indicated tag value has been defined on this node or on
        any ancestor node, or false otherwise.  See also has_tag().
        """
    def find_net_tag(self, key: str) -> NodePath:
        """Returns the lowest ancestor of this node that contains a tag definition
        with the indicated key, if any, or an empty NodePath if no ancestor of this
        node contains this tag definition.  See set_tag().
        """
    def get_tags(self) -> MutableMapping[str, str] | None: ...
    def get_python_tags(self) -> dict[Any, Any] | None: ...
    def set_python_tag(self, keys: Any, value: Any) -> None: ...
    def get_python_tag(self, keys: Any) -> Any | None: ...
    def get_python_tag_keys(self) -> list[Any] | tuple[()]: ...
    def has_python_tag(self, keys: Any) -> bool: ...
    def clear_python_tag(self, keys: Any) -> None: ...
    def get_net_python_tag(self, keys: Any) -> Any | None: ...
    def has_net_python_tag(self, keys: Any) -> bool: ...
    def find_net_python_tag(self, keys: Any) -> NodePath: ...
    def list_tags(self) -> None:
        """Lists the tags to the nout stream, one per line.  See
        PandaNode::list_tags() for a variant that allows you to specify the output
        stream.
        """
    def set_name(self, name: str) -> None:
        """Changes the name of the referenced node."""
    def get_name(self) -> str:
        """Returns the name of the referenced node."""
    def write_bam_file(self, filename: StrOrBytesPath) -> bool:
        """Writes the contents of this node and below out to a bam file with the
        indicated filename.  This file may then be read in again, as is, at some
        later point.  Returns true if successful, false on some kind of error.
        """
    def write_bam_stream(self, out: ostream) -> bool:
        """Writes the contents of this node and below out to the indicated stream."""
    @overload
    def encode_to_bam_stream(self) -> bytes:
        """`(self)`:
        Converts the NodePath object into a single stream of data using a
        BamWriter, and returns that data as a string string.  Returns empty string
        on failure.  This is similar to write_bam_stream().

        This method is used by __reduce__ to handle streaming of NodePaths to a
        pickle file.

        `(self, data: bytes, writer: BamWriter = ...)`:
        Converts the NodePath object into a single stream of data using a
        BamWriter, and stores that data in the indicated string.  Returns true on
        success, false on failure.

        If the BamWriter is NULL, this behaves the same way as
        NodePath::write_bam_stream() and PandaNode::encode_to_bam_stream(), in the
        sense that it only writes this node and all nodes below it.

        However, if the BamWriter is not NULL, it behaves very differently.  In
        this case, it encodes the *entire graph* of all nodes connected to the
        NodePath, including all parent nodes and siblings.  This is necessary for
        correct streaming of related NodePaths and restoration of instances, etc.,
        but it does mean you must detach() a node before writing it if you want to
        limit the nodes that get written.

        This method is used by __reduce__ to handle streaming of NodePaths to a
        pickle file.  The BamWriter case is used by the direct.stdpy.pickle module,
        while the saner, non-BamWriter case is used when the standard pickle module
        calls this function.
        """
    @overload
    def encode_to_bam_stream(self, data: bytes, writer: BamWriter = ...) -> bool: ...
    @staticmethod
    def decode_from_bam_stream(data: bytes, reader: BamReader = ...) -> NodePath:
        """Reads the string created by a previous call to encode_to_bam_stream(), and
        extracts and returns the NodePath on that string.  Returns NULL on error.
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_nodes(self) -> tuple[PandaNode, ...]: ...
    def get_ancestors(self) -> tuple[NodePath, ...]: ...
    anyPath = any_path
    notFound = not_found
    setMaxSearchDepth = set_max_search_depth
    getMaxSearchDepth = get_max_search_depth
    isEmpty = is_empty
    isSingleton = is_singleton
    getNumNodes = get_num_nodes
    getNode = get_node
    getAncestor = get_ancestor
    getErrorType = get_error_type
    getTopNode = get_top_node
    getTop = get_top
    getKey = get_key
    addHash = add_hash
    isSameGraph = is_same_graph
    isAncestorOf = is_ancestor_of
    getCommonAncestor = get_common_ancestor
    getChildren = get_children
    getNumChildren = get_num_children
    getChild = get_child
    getStashedChildren = get_stashed_children
    countNumDescendants = count_num_descendants
    hasParent = has_parent
    getParent = get_parent
    getSort = get_sort
    findPathTo = find_path_to
    findAllMatches = find_all_matches
    findAllPathsTo = find_all_paths_to
    reparentTo = reparent_to
    stashTo = stash_to
    wrtReparentTo = wrt_reparent_to
    instanceTo = instance_to
    instanceUnderNode = instance_under_node
    copyTo = copy_to
    attachNewNode = attach_new_node
    removeNode = remove_node
    detachNode = detach_node
    reverseLs = reverse_ls
    getState = get_state
    setState = set_state
    getNetState = get_net_state
    setAttrib = set_attrib
    getAttrib = get_attrib
    hasAttrib = has_attrib
    clearAttrib = clear_attrib
    setEffect = set_effect
    getEffect = get_effect
    hasEffect = has_effect
    clearEffect = clear_effect
    setEffects = set_effects
    getEffects = get_effects
    clearEffects = clear_effects
    getTransform = get_transform
    clearTransform = clear_transform
    setTransform = set_transform
    getNetTransform = get_net_transform
    getPrevTransform = get_prev_transform
    setPrevTransform = set_prev_transform
    getNetPrevTransform = get_net_prev_transform
    setPos = set_pos
    setX = set_x
    setY = set_y
    setZ = set_z
    setFluidPos = set_fluid_pos
    setFluidX = set_fluid_x
    setFluidY = set_fluid_y
    setFluidZ = set_fluid_z
    getPos = get_pos
    getX = get_x
    getY = get_y
    getZ = get_z
    getPosDelta = get_pos_delta
    setHpr = set_hpr
    setH = set_h
    setP = set_p
    setR = set_r
    getHpr = get_hpr
    getH = get_h
    getP = get_p
    getR = get_r
    setQuat = set_quat
    getQuat = get_quat
    setScale = set_scale
    setSx = set_sx
    setSy = set_sy
    setSz = set_sz
    getScale = get_scale
    getSx = get_sx
    getSy = get_sy
    getSz = get_sz
    setShear = set_shear
    setShxy = set_shxy
    setShxz = set_shxz
    setShyz = set_shyz
    getShear = get_shear
    getShxy = get_shxy
    getShxz = get_shxz
    getShyz = get_shyz
    setPosHpr = set_pos_hpr
    setPosQuat = set_pos_quat
    setHprScale = set_hpr_scale
    setQuatScale = set_quat_scale
    setPosHprScale = set_pos_hpr_scale
    setPosQuatScale = set_pos_quat_scale
    setPosHprScaleShear = set_pos_hpr_scale_shear
    setPosQuatScaleShear = set_pos_quat_scale_shear
    setMat = set_mat
    clearMat = clear_mat
    hasMat = has_mat
    getMat = get_mat
    lookAt = look_at
    headsUp = heads_up
    getRelativePoint = get_relative_point
    getRelativeVector = get_relative_vector
    getDistance = get_distance
    setColor = set_color
    setColorOff = set_color_off
    clearColor = clear_color
    hasColor = has_color
    getColor = get_color
    hasColorScale = has_color_scale
    clearColorScale = clear_color_scale
    setColorScale = set_color_scale
    composeColorScale = compose_color_scale
    setColorScaleOff = set_color_scale_off
    setAlphaScale = set_alpha_scale
    setAllColorScale = set_all_color_scale
    setSr = set_sr
    setSg = set_sg
    setSb = set_sb
    setSa = set_sa
    getColorScale = get_color_scale
    getSr = get_sr
    getSg = get_sg
    getSb = get_sb
    getSa = get_sa
    setLight = set_light
    setLightOff = set_light_off
    clearLight = clear_light
    hasLight = has_light
    hasLightOff = has_light_off
    setClipPlane = set_clip_plane
    setClipPlaneOff = set_clip_plane_off
    clearClipPlane = clear_clip_plane
    hasClipPlane = has_clip_plane
    hasClipPlaneOff = has_clip_plane_off
    setScissor = set_scissor
    clearScissor = clear_scissor
    hasScissor = has_scissor
    setOccluder = set_occluder
    clearOccluder = clear_occluder
    hasOccluder = has_occluder
    setBin = set_bin
    clearBin = clear_bin
    hasBin = has_bin
    getBinName = get_bin_name
    getBinDrawOrder = get_bin_draw_order
    setTexture = set_texture
    setTextureOff = set_texture_off
    clearTexture = clear_texture
    hasTexture = has_texture
    hasTextureOff = has_texture_off
    getTexture = get_texture
    replaceTexture = replace_texture
    getTextureSampler = get_texture_sampler
    setShader = set_shader
    setShaderOff = set_shader_off
    setShaderAuto = set_shader_auto
    clearShader = clear_shader
    setShaderInput = set_shader_input
    setShaderInputs = set_shader_inputs
    clearShaderInput = clear_shader_input
    setInstanceCount = set_instance_count
    getShader = get_shader
    getShaderInput = get_shader_input
    getInstanceCount = get_instance_count
    setTexTransform = set_tex_transform
    clearTexTransform = clear_tex_transform
    hasTexTransform = has_tex_transform
    getTexTransform = get_tex_transform
    setTexOffset = set_tex_offset
    setTexRotate = set_tex_rotate
    setTexScale = set_tex_scale
    getTexOffset = get_tex_offset
    getTexRotate = get_tex_rotate
    getTexScale = get_tex_scale
    setTexPos = set_tex_pos
    setTexHpr = set_tex_hpr
    getTexPos = get_tex_pos
    getTexHpr = get_tex_hpr
    getTexScale3d = get_tex_scale_3d
    setTexGen = set_tex_gen
    clearTexGen = clear_tex_gen
    hasTexGen = has_tex_gen
    getTexGen = get_tex_gen
    setTexProjector = set_tex_projector
    clearTexProjector = clear_tex_projector
    hasTexProjector = has_tex_projector
    getTexProjectorFrom = get_tex_projector_from
    getTexProjectorTo = get_tex_projector_to
    projectTexture = project_texture
    clearProjectTexture = clear_project_texture
    hasTexcoord = has_texcoord
    hasVertexColumn = has_vertex_column
    findAllVertexColumns = find_all_vertex_columns
    findAllTexcoords = find_all_texcoords
    findTexture = find_texture
    findAllTextures = find_all_textures
    findTextureStage = find_texture_stage
    findAllTextureStages = find_all_texture_stages
    unifyTextureStages = unify_texture_stages
    findMaterial = find_material
    findAllMaterials = find_all_materials
    setMaterial = set_material
    setMaterialOff = set_material_off
    clearMaterial = clear_material
    hasMaterial = has_material
    getMaterial = get_material
    replaceMaterial = replace_material
    setFog = set_fog
    setFogOff = set_fog_off
    clearFog = clear_fog
    hasFog = has_fog
    hasFogOff = has_fog_off
    getFog = get_fog
    setRenderModeWireframe = set_render_mode_wireframe
    setRenderModeFilled = set_render_mode_filled
    setRenderModeFilledWireframe = set_render_mode_filled_wireframe
    setRenderModeThickness = set_render_mode_thickness
    setRenderModePerspective = set_render_mode_perspective
    setRenderMode = set_render_mode
    clearRenderMode = clear_render_mode
    hasRenderMode = has_render_mode
    getRenderMode = get_render_mode
    getRenderModeThickness = get_render_mode_thickness
    getRenderModePerspective = get_render_mode_perspective
    setTwoSided = set_two_sided
    clearTwoSided = clear_two_sided
    hasTwoSided = has_two_sided
    getTwoSided = get_two_sided
    setDepthTest = set_depth_test
    clearDepthTest = clear_depth_test
    hasDepthTest = has_depth_test
    getDepthTest = get_depth_test
    setDepthWrite = set_depth_write
    clearDepthWrite = clear_depth_write
    hasDepthWrite = has_depth_write
    getDepthWrite = get_depth_write
    setDepthOffset = set_depth_offset
    clearDepthOffset = clear_depth_offset
    hasDepthOffset = has_depth_offset
    getDepthOffset = get_depth_offset
    doBillboardAxis = do_billboard_axis
    doBillboardPointEye = do_billboard_point_eye
    doBillboardPointWorld = do_billboard_point_world
    setBillboardAxis = set_billboard_axis
    setBillboardPointEye = set_billboard_point_eye
    setBillboardPointWorld = set_billboard_point_world
    clearBillboard = clear_billboard
    hasBillboard = has_billboard
    setCompass = set_compass
    clearCompass = clear_compass
    hasCompass = has_compass
    setTransparency = set_transparency
    clearTransparency = clear_transparency
    hasTransparency = has_transparency
    getTransparency = get_transparency
    setLogicOp = set_logic_op
    clearLogicOp = clear_logic_op
    hasLogicOp = has_logic_op
    getLogicOp = get_logic_op
    setAntialias = set_antialias
    clearAntialias = clear_antialias
    hasAntialias = has_antialias
    getAntialias = get_antialias
    hasAudioVolume = has_audio_volume
    clearAudioVolume = clear_audio_volume
    setAudioVolume = set_audio_volume
    setAudioVolumeOff = set_audio_volume_off
    getAudioVolume = get_audio_volume
    getNetAudioVolume = get_net_audio_volume
    adjustAllPriorities = adjust_all_priorities
    showThrough = show_through
    isHidden = is_hidden
    getHiddenAncestor = get_hidden_ancestor
    unstashAll = unstash_all
    isStashed = is_stashed
    getStashedAncestor = get_stashed_ancestor
    getCollideMask = get_collide_mask
    setCollideMask = set_collide_mask
    compareTo = compare_to
    verifyComplete = verify_complete
    premungeScene = premunge_scene
    prepareScene = prepare_scene
    showBounds = show_bounds
    showTightBounds = show_tight_bounds
    hideBounds = hide_bounds
    getBounds = get_bounds
    forceRecomputeBounds = force_recompute_bounds
    writeBounds = write_bounds
    calcTightBounds = calc_tight_bounds
    getTightBounds = get_tight_bounds
    flattenLight = flatten_light
    flattenMedium = flatten_medium
    flattenStrong = flatten_strong
    applyTextureColors = apply_texture_colors
    clearModelNodes = clear_model_nodes
    setTag = set_tag
    getTag = get_tag
    getTagKeys = get_tag_keys
    hasTag = has_tag
    clearTag = clear_tag
    getNetTag = get_net_tag
    hasNetTag = has_net_tag
    findNetTag = find_net_tag
    getTags = get_tags
    getPythonTags = get_python_tags
    setPythonTag = set_python_tag
    getPythonTag = get_python_tag
    getPythonTagKeys = get_python_tag_keys
    hasPythonTag = has_python_tag
    clearPythonTag = clear_python_tag
    getNetPythonTag = get_net_python_tag
    hasNetPythonTag = has_net_python_tag
    findNetPythonTag = find_net_python_tag
    listTags = list_tags
    setName = set_name
    getName = get_name
    writeBamFile = write_bam_file
    writeBamStream = write_bam_stream
    encodeToBamStream = encode_to_bam_stream
    decodeFromBamStream = decode_from_bam_stream
    getClassType = get_class_type
    getNodes = get_nodes
    getAncestors = get_ancestors

class NodePathCollection:
    """This is a set of zero or more NodePaths.  It's handy for returning from
    functions that need to return multiple NodePaths (for instance,
    NodePaths::get_children).
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: NodePathCollection = ...) -> None: ...
    @overload
    def __init__(self, sequence: Sequence[NodePath]) -> None: ...
    def __getitem__(self, index: int) -> NodePath: ...
    def __len__(self) -> int:
        """Returns the number of paths in the collection.  This is the same thing as
        get_num_paths().
        """
    def __iadd__(self, other: NodePathCollection) -> Self: ...
    def __add__(self, other: NodePathCollection) -> NodePathCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[NodePath]: ...  # Doesn't actually exist
    def add_path(self, node_path: NodePath) -> None:
        """Adds a new NodePath to the collection."""
    def remove_path(self, node_path: NodePath) -> bool:
        """Removes the indicated NodePath from the collection.  Returns true if the
        path was removed, false if it was not a member of the collection.
        """
    def add_paths_from(self, other: NodePathCollection) -> None:
        """Adds all the NodePaths indicated in the other collection to this path.  The
        other paths are simply appended to the end of the paths in this list;
        duplicates are not automatically removed.
        """
    def remove_paths_from(self, other: NodePathCollection) -> None:
        """Removes from this collection all of the NodePaths listed in the other
        collection.
        """
    def remove_duplicate_paths(self) -> None:
        """Removes any duplicate entries of the same NodePaths on this collection.  If
        a NodePath appears multiple times, the first appearance is retained;
        subsequent appearances are removed.
        """
    def has_path(self, path: NodePath) -> bool:
        """Returns true if the indicated NodePath appears in this collection, false
        otherwise.
        """
    def clear(self) -> None:
        """Removes all NodePaths from the collection."""
    def reserve(self, num: int) -> None:
        """This is a hint to Panda to allocate enough memory to hold the given number
        of NodePaths, if you know ahead of time how many you will be adding.
        """
    def is_empty(self) -> bool:
        """Returns true if there are no NodePaths in the collection, false otherwise."""
    def get_num_paths(self) -> int:
        """Returns the number of NodePaths in the collection."""
    def get_path(self, index: int) -> NodePath:
        """Returns the nth NodePath in the collection."""
    def append(self, node_path: NodePath) -> None:
        """Adds a new NodePath to the collection.  This method duplicates the
        add_path() method; it is provided to satisfy Python's naming convention.
        """
    def extend(self, other: NodePathCollection) -> None:
        """Appends the other list onto the end of this one.  This method duplicates
        the += operator; it is provided to satisfy Python's naming convention.
        """
    @overload
    def ls(self) -> None:
        """Lists all the nodes at and below each node in the collection
        hierarchically.
        """
    @overload
    def ls(self, out: ostream, indent_level: int = ...) -> None: ...
    def find_all_matches(self, path: str) -> NodePathCollection:
        """Returns the complete set of all NodePaths that begin with any NodePath in
        this collection and can be extended by path.  The shortest paths will be
        listed first.
        """
    def reparent_to(self, other: NodePath) -> None:
        """Reparents all the NodePaths in the collection to the indicated node."""
    def wrt_reparent_to(self, other: NodePath) -> None:
        """Reparents all the NodePaths in the collection to the indicated node,
        adjusting each transform so as not to move in world coordinates.
        """
    def show(self) -> None:
        """Shows all NodePaths in the collection."""
    def hide(self) -> None:
        """Hides all NodePaths in the collection."""
    def stash(self) -> None:
        """Stashes all NodePaths in the collection."""
    def unstash(self) -> None:
        """Unstashes all NodePaths in the collection."""
    def detach(self) -> None:
        """Detaches all NodePaths in the collection."""
    def get_collide_mask(self) -> CollideMask:
        """Returns the union of all of the into_collide_masks for nodes at this level
        and below.  This is the same thing as node()->get_net_collide_mask().

        If you want to return what the into_collide_mask of this node itself is,
        without regard to its children, use node()->get_into_collide_mask().
        """
    def set_collide_mask(
        self, new_mask: CollideMask | int, bits_to_change: CollideMask | int = ..., node_type: TypeHandle | type = ...
    ) -> None:
        """Recursively applies the indicated CollideMask to the into_collide_masks for
        all nodes at this level and below.

        The default is to change all bits, but if bits_to_change is not all bits
        on, then only the bits that are set in bits_to_change are modified,
        allowing this call to change only a subset of the bits in the subgraph.
        """
    def calc_tight_bounds(self, min_point: Vec3Like, max_point: Vec3Like) -> bool:
        """Calculates the minimum and maximum vertices of all Geoms at these
        NodePath's bottom nodes and below This is a tight bounding box; it will
        generally be tighter than the bounding volume returned by get_bounds() (but
        it is more expensive to compute).

        The return value is true if any points are within the bounding volume, or
        false if none are.
        """
    def get_tight_bounds(self) -> tuple[LPoint3f, LPoint3f] | None: ...
    @overload
    def set_texture(self, tex: Texture, priority: int = ...) -> None:
        """`(self, tex: Texture, priority: int = ...)`:
        Adds the indicated texture to the list of textures that will be rendered on
        the default texture stage.

        This is the deprecated single-texture variant of this method; it is now
        superceded by set_texture() that accepts a stage and texture.  However,
        this method may be used in the presence of multitexture if you just want to
        adjust the default stage.

        `(self, stage: TextureStage, tex: Texture, priority: int = ...)`:
        Adds the indicated texture to the list of textures that will be rendered on
        the indicated multitexture stage.  If there are multiple texture stages
        specified (possibly on multiple different nodes at different levels), they
        will all be applied to geometry together, according to the stage
        specification set up in the TextureStage object.
        """
    @overload
    def set_texture(self, stage: TextureStage, tex: Texture, priority: int = ...) -> None: ...
    @overload
    def set_texture_off(self, priority: int = ...) -> None:
        """`(self, stage: TextureStage, priority: int = ...)`:
        Sets the geometry at this level and below to render using no texture, on
        the indicated stage.  This is different from not specifying a texture;
        rather, this specifically contradicts set_texture() at a higher node level
        (or, with a priority, overrides a set_texture() at a lower level).

        `(self, priority: int = ...)`:
        Sets the geometry at this level and below to render using no texture, on
        any stage.  This is different from not specifying a texture; rather, this
        specifically contradicts set_texture() at a higher node level (or, with a
        priority, overrides a set_texture() at a lower level).
        """
    @overload
    def set_texture_off(self, stage: TextureStage, priority: int = ...) -> None: ...
    @overload
    def set_color(self, color: Vec4Like, priority: int = ...) -> None:
        """Colors all NodePaths in the collection"""
    @overload
    def set_color(self, r: float, g: float, b: float, a: float = ..., priority: int = ...) -> None: ...
    @overload
    def set_color_scale(self, scale: Vec4Like, priority: int = ...) -> None:
        """Applies color scales to all NodePaths in the collection.  The existing
        color scale is replaced.
        """
    @overload
    def set_color_scale(self, r: float, g: float, b: float, a: float = ..., priority: int = ...) -> None: ...
    @overload
    def compose_color_scale(self, scale: Vec4Like, priority: int = ...) -> None:
        """Applies color scales to all NodePaths in the collection.  The existing
        color scale, if any, is multiplied by the specified color scale.
        """
    @overload
    def compose_color_scale(self, r: float, g: float, b: float, a: float = ..., priority: int = ...) -> None: ...
    def set_attrib(self, attrib: RenderAttrib, priority: int = ...) -> None:
        """Applies the indicated RenderAttrib to all NodePaths in the collection.  An
        effort is made to apply the attrib to many NodePaths as quickly as
        possible; redundant RenderState compositions are not duplicated.
        """
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the NodePathCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the NodePathCollection to the
        indicated output stream.
        """
    def get_paths(self) -> tuple[NodePath, ...]: ...
    addPath = add_path
    removePath = remove_path
    addPathsFrom = add_paths_from
    removePathsFrom = remove_paths_from
    removeDuplicatePaths = remove_duplicate_paths
    hasPath = has_path
    isEmpty = is_empty
    getNumPaths = get_num_paths
    getPath = get_path
    findAllMatches = find_all_matches
    reparentTo = reparent_to
    wrtReparentTo = wrt_reparent_to
    getCollideMask = get_collide_mask
    setCollideMask = set_collide_mask
    calcTightBounds = calc_tight_bounds
    getTightBounds = get_tight_bounds
    setTexture = set_texture
    setTextureOff = set_texture_off
    setColor = set_color
    setColorScale = set_color_scale
    composeColorScale = compose_color_scale
    setAttrib = set_attrib
    getPaths = get_paths

class AttribNodeRegistry:
    """This global object records NodePaths that are referenced by scene graph
    attribs, such as ClipPlaneAttribs and LightAttribs.

    Its primary purpose is to unify attribs that are loaded in from bam files.
    Attrib nodes are identified by name and type; when a bam file that contains
    references to some attrib nodes is loaded, those nodes are first looked up
    here in the AttribNodeRegistry.  If there is a match (by name and node
    type), the identified node is used instead of the node referenced within
    the bam file itself.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def add_node(self, attrib_node: NodePath) -> None:
        """Adds the indicated NodePath to the registry.  The name and type of the node
        are noted at the time of this call; if the name changes later, it will not
        update the registry index.

        The NodePath must reference some kind of an attribute node, such as a
        LightNode or a PlaneNode.  When bam files that reference an attribute node
        of the same type and the same name are loaded, they will quietly be
        redirected to reference this NodePath.

        If there is already a node matching the indicated name and type, it will be
        replaced.
        """
    @overload
    def remove_node(self, attrib_node: NodePath) -> bool:
        """`(self, attrib_node: NodePath)`:
        Removes the indicated NodePath from the registry.  The name of the node
        must not have changed since the matching call to add_node(), or it will not
        be successfully removed.

        Returns true if the NodePath is found and removed, false if it is not found
        (for instance, because the name has changed).

        `(self, n: int)`:
        Removes the nth node from the registry.
        """
    @overload
    def remove_node(self, n: int) -> None: ...
    def lookup_node(self, orig_node: NodePath) -> NodePath:
        """Looks up the indicated NodePath in the registry.  If there is a node
        already in the registry with the matching name and type, returns that
        NodePath instead; otherwise, returns the original NodePath.
        """
    def get_num_nodes(self) -> int:
        """Returns the total number of nodes in the registry."""
    def get_node(self, n: int) -> NodePath:
        """Returns the nth NodePath recorded in the registry."""
    def get_node_type(self, n: int) -> TypeHandle:
        """Returns the type of the nth node, as recorded in the registry."""
    def get_node_name(self, n: int) -> str:
        """Returns the name of the nth node, as recorded in the registry.  This will
        be the node name as it was at the time the node was recorded; if the node
        has changed names since then, this will still return the original name.
        """
    @overload
    def find_node(self, attrib_node: NodePath) -> int:
        """`(self, attrib_node: NodePath)`:
        Returns the index number of the indicated NodePath in the registry
        (assuming its name hasn't changed since it was recorded in the registry),
        or -1 if the NodePath cannot be found (for instance, because its name has
        changed).

        `(self, type: TypeHandle, name: str)`:
        Returns the index number of the node with the indicated type and name in
        the registry, or -1 if there is no such node in the registry.
        """
    @overload
    def find_node(self, type: TypeHandle | type, name: str) -> int: ...
    def clear(self) -> None:
        """Removes all nodes from the registry."""
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_ptr() -> AttribNodeRegistry: ...
    def get_nodes(self) -> tuple[NodePath, ...]: ...
    addNode = add_node
    removeNode = remove_node
    lookupNode = lookup_node
    getNumNodes = get_num_nodes
    getNode = get_node
    getNodeType = get_node_type
    getNodeName = get_node_name
    findNode = find_node
    getGlobalPtr = get_global_ptr
    getNodes = get_nodes

class AudioVolumeAttrib(RenderAttrib):
    """Applies a scale to audio volume for positional sounds in the scene graph."""

    @property
    def volume(self) -> float: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_identity() -> RenderAttrib:
        """Constructs an identity audio volume attrib."""
    @staticmethod
    def make(volume: float) -> RenderAttrib:
        """Constructs a new AudioVolumeAttrib object that indicates audio volume
        should be scaled by the indicated factor.
        """
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new AudioVolumeAttrib object that ignores any
        AudioVolumeAttrib inherited from above.  You may also specify an additional
        volume scale to apply to geometry below (using set_volume()).
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def is_off(self) -> bool:
        """Returns true if the AudioVolumeAttrib will ignore any color scales
        inherited from above, false otherwise.  This is not the same thing as
        !has_scale(); a AudioVolumeAttrib may have the "off" flag set and also have
        another scale specified.
        """
    def has_volume(self) -> bool:
        """Returns true if the AudioVolumeAttrib has a non-identity volume, false
        otherwise (in which case it might be an off attrib or an identity attrib).
        """
    def get_volume(self) -> float:
        """Returns the volume to be applied to sounds."""
    def set_volume(self, volume: float) -> RenderAttrib:
        """Returns a new AudioVolumeAttrib, just like this one, but with the volume
        changed to the indicated value.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeIdentity = make_identity
    makeOff = make_off
    makeDefault = make_default
    isOff = is_off
    hasVolume = has_volume
    getVolume = get_volume
    setVolume = set_volume
    getClassSlot = get_class_slot

class AuxBitplaneAttrib(RenderAttrib):
    """Modern frame buffers can have 'aux' bitplanes, which are additional
    bitplanes above and beyond the standard depth and color.  This attrib
    controls what gets rendered into those additional bitplanes.  It can also
    affect what goes into the alpha channel of the primary color buffer.

    ABO_glow: copy the glow map into the alpha channel of the primary frame
    buffer.  If there is no glow map, set it to zero.  Caveat: it is not
    possible to write glow or depth values to the framebuffer alpha channel at
    the same time as using alpha blending or alpha testing.  Any attempt to use
    transparency, blending, or alpha testing will cause this flag to be
    overridden.

    ABO_aux_normal: put the camera-space normal into the into the R,G
    components of the first auxiliary bitplane.

    ABO_aux_modelz: put the clip-space Z coordinate of the center of the model
    (after perspective divide) into the B channel of the first auxiliary
    bitplane.

    ABO_aux_glow: put a copy of the glow map into the alpha channel of the
    first auxiliary bitplane.  If there is no glow map, set it to zero.

    AuxBitplaneAttrib is relevant only when shader generation is enabled.
    Otherwise, it has no effect.
    """

    ABO_glow: Final = 1
    ABOGlow: Final = 1
    ABO_aux_normal: Final = 2
    ABOAuxNormal: Final = 2
    ABO_aux_glow: Final = 4
    ABOAuxGlow: Final = 4
    @property
    def outputs(self) -> int: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(outputs: int = ...) -> RenderAttrib:
        """`()`:
        Constructs a default AuxBitplaneAttrib object.

        `(outputs: int)`:
        Constructs a specified AuxBitplaneAttrib object.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_outputs(self) -> int:
        """Returns the AuxBitplaneAttrib output bits."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getOutputs = get_outputs
    getClassSlot = get_class_slot

class AuxSceneData(TypedReferenceCount):
    """This is a base class for a generic data structure that can be attached per-
    instance to the camera, to store per-instance data that must be preserved
    over multiple frames.

    In particular, this is used to implement the FadeLODNode, which must
    remember during traversal at what point it is in the fade, separately for
    each instance and for each camera.
    """

    def __init__(self, __param0: AuxSceneData) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_duration(self, duration: float) -> None:
        """Specifies the minimum length in time, in seconds, to keep this AuxSceneData
        object around in the scene graph after the last time it was rendered.
        """
    def get_duration(self) -> float:
        """Returns the minimum length in time, in seconds, to keep this AuxSceneData
        object around in the scene graph after the last time it was rendered.
        """
    def set_last_render_time(self, render_time: float) -> None:
        """Should be called with the current frame_time each time the AuxSceneData is
        used during traversal.
        """
    def get_last_render_time(self) -> float:
        """Returns the last time this object was used during traversal (according to
        set_last_render_time()).
        """
    def get_expiration_time(self) -> float:
        """Returns the frame_time at which this AuxSceneData object is currently
        scheduled to be removed from the scene graph.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    setDuration = set_duration
    getDuration = get_duration
    setLastRenderTime = set_last_render_time
    getLastRenderTime = get_last_render_time
    getExpirationTime = get_expiration_time

class BamFile(BamEnums):
    """The principle public interface to reading and writing Bam disk files.  See
    also BamReader and BamWriter, the more general implementation of this
    class.

    Bam files are most often used to store scene graphs or subgraphs, and by
    convention they are given filenames ending in the extension ".bam" when
    they are used for this purpose.  However, a Bam file may store any
    arbitrary list of TypedWritable objects; in this more general usage, they
    are given filenames ending in ".boo" to differentiate them from the more
    common scene graph files.
    """

    @property
    def file_endian(self) -> _BamEnums_BamEndian: ...
    @property
    def file_stdfloat_double(self) -> bool: ...
    @property
    def reader(self) -> BamReader: ...
    @property
    def writer(self) -> BamWriter: ...
    def __init__(self) -> None: ...
    @overload
    def open_read(self, bam_filename: StrOrBytesPath, report_errors: bool = ...) -> bool:
        """`(self, bam_filename: Filename, report_errors: bool = ...)`:
        Attempts to open the indicated filename for reading.  Returns true if
        successful, false on error.

        `(self, _in: istream, bam_filename: str = ..., report_errors: bool = ...)`:
        Attempts to open the indicated stream for reading.  The filename is just
        for information purposes only.  Returns true if successful, false on error.
        """
    @overload
    def open_read(self, _in: istream, bam_filename: str = ..., report_errors: bool = ...) -> bool: ...
    def read_object(self) -> TypedWritable:
        """Reads and returns the next object from the Bam file, or NULL if the end of
        the file has been reached, or if there is an error condition.  Use is_eof()
        to differentiate these two cases.

        The pointers returned by this method will not be valid for use until
        resolve() is subsequently called.
        """
    def is_eof(self) -> bool:
        """Returns true if the reader has reached end-of-file, false otherwise.  This
        call is only valid after a call to read_object().
        """
    def resolve(self) -> bool:
        """This must be called after one or more objects have been read via calls to
        read_object() in order to resolve all internal pointer references in the
        objects read and make all the pointers valid.  It returns true if all
        objects are successfully resolved, or false if some have not been (in which
        case you must call resolve() again later).
        """
    def read_node(self, report_errors: bool = ...) -> PandaNode:
        """Although the bam file format is general enough to store a list of objects
        of arbitrary type, bam files on disk usually contain just one object, a
        PandaNode that is the root of a scene graph.  (Bam files that store other
        kinds of things are usually given the extension "boo", for "binary other
        objects", to differentiate them from the normal scene graph type file.)

        This is a convenience method for when you believe you are reading a scene
        graph bam file.  It reads the one PandaNode and returns it.  It also calls
        resolve() to fully resolve the object, since we expect this will be the
        only object in the file.

        If the bam file contains something other than a PandaNode, an error is
        printed and NULL is returned.
        """
    @overload
    def open_write(self, bam_filename: StrOrBytesPath, report_errors: bool = ...) -> bool:
        """`(self, bam_filename: Filename, report_errors: bool = ...)`:
        Attempts to open the indicated file for writing.  If another file by the
        same name already exists, it will be silently removed.  Returns true if
        successful, false otherwise.

        `(self, out: ostream, bam_filename: str = ..., report_errors: bool = ...)`:
        Attempts to open the indicated stream for writing.  The filename is just
        for information purposes only.  Returns true if successful, false on error.
        """
    @overload
    def open_write(self, out: ostream, bam_filename: str = ..., report_errors: bool = ...) -> bool: ...
    def write_object(self, object: TypedWritable) -> bool:
        """Writes the indicated object to the Bam file.  Returns true if successful,
        false on error.
        """
    def close(self) -> None:
        """Closes the input or output stream."""
    def is_valid_read(self) -> bool:
        """Returns true if the Bam file is open and ready for reading with no errors
        so far detected, or false otherwise.
        """
    def is_valid_write(self) -> bool:
        """Returns true if the Bam file is open and ready for writing with no errors
        so far detected, or false otherwise.
        """
    def get_file_major_ver(self) -> int:
        """Returns the major version number of the file currently being read, or the
        system current major version number if no file is currently open for
        reading.
        """
    def get_file_minor_ver(self) -> int:
        """Returns the minor version number of the file currently being read, or the
        system current minor version number if no file is currently open for
        reading.
        """
    def get_file_endian(self) -> _BamEnums_BamEndian:
        """Returns the endian preference indicated by the Bam file currently being
        read or written.
        """
    def get_file_stdfloat_double(self) -> bool:
        """Returns true if the file stores all "standard" floats as 64-bit doubles, or
        false if they are 32-bit floats.
        """
    def get_current_major_ver(self) -> int:
        """Returns the system current major version number.  This is the version
        number that will be assigned to any generated Bam files.
        """
    def get_current_minor_ver(self) -> int:
        """Returns the system current minor version number.  This is the version
        number that will be assigned to any generated Bam files.
        """
    def get_reader(self) -> BamReader:
        """Returns the BamReader in charge of performing the read operations.  This
        will return NULL unless open_read() was called.
        """
    def get_writer(self) -> BamWriter:
        """Returns the BamWriter in charge of performing the write operations.  This
        will return NULL unless open_write() was called.
        """
    openRead = open_read
    readObject = read_object
    isEof = is_eof
    readNode = read_node
    openWrite = open_write
    writeObject = write_object
    isValidRead = is_valid_read
    isValidWrite = is_valid_write
    getFileMajorVer = get_file_major_ver
    getFileMinorVer = get_file_minor_ver
    getFileEndian = get_file_endian
    getFileStdfloatDouble = get_file_stdfloat_double
    getCurrentMajorVer = get_current_major_ver
    getCurrentMinorVer = get_current_minor_ver
    getReader = get_reader
    getWriter = get_writer

class BillboardEffect(RenderEffect):
    """Indicates that geometry at this node should automatically rotate to face
    the camera, or any other arbitrary node.
    """

    @staticmethod
    def make(
        up_vector: Vec3Like,
        eye_relative: bool,
        axial_rotate: bool,
        offset: float,
        look_at: NodePath,
        look_at_point: Vec3Like,
        fixed_depth: bool = ...,
    ) -> RenderEffect:
        """Constructs a new BillboardEffect object with the indicated properties."""
    @staticmethod
    def make_axis() -> RenderEffect:
        """A convenience function to make a typical axis-rotating billboard."""
    @staticmethod
    def make_point_eye() -> RenderEffect:
        """A convenience function to make a typical eye-relative point-rotating
        billboard.
        """
    @staticmethod
    def make_point_world() -> RenderEffect:
        """A convenience function to make a typical world-relative point-rotating
        billboard.
        """
    def is_off(self) -> bool:
        """Returns true if the BillboardEffect is an 'off' BillboardEffect, indicating
        that it does not enable billboarding.  This kind of BillboardEffect isn't
        particularly useful and isn't normally created or stored in the graph; it
        might be implicitly discovered as the result of a
        NodePath::get_rel_state().
        """
    def get_up_vector(self) -> LVector3:
        """Returns the up vector in effect for this billboard."""
    def get_eye_relative(self) -> bool:
        """Returns true if this billboard interprets the up vector relative to the
        camera, or false if it is relative to the world.
        """
    def get_axial_rotate(self) -> bool:
        """Returns true if this billboard rotates only around the axis of the up
        vector, or false if it rotates freely in three dimensions.
        """
    def get_fixed_depth(self) -> bool:
        """Returns true if this billboard always appears at a fixed distance from the
        camera.
        """
    def get_offset(self) -> float:
        """Returns the distance toward the camera (or the look_at_point) the billboard
        is moved towards, after rotating.  This can be used to ensure the billboard
        is not obscured by nearby geometry.
        """
    def get_look_at(self) -> NodePath:
        """Returns the node this billboard will rotate to look towards.  If this is
        empty, it means the billboard will rotate towards the current camera node,
        wherever that might be.
        """
    def get_look_at_point(self) -> LPoint3:
        """Returns the point, relative to the look_at node, towards which the
        billboard will rotate.  Normally this is (0, 0, 0).
        """
    makeAxis = make_axis
    makePointEye = make_point_eye
    makePointWorld = make_point_world
    isOff = is_off
    getUpVector = get_up_vector
    getEyeRelative = get_eye_relative
    getAxialRotate = get_axial_rotate
    getFixedDepth = get_fixed_depth
    getOffset = get_offset
    getLookAt = get_look_at
    getLookAtPoint = get_look_at_point

class LensNode(PandaNode):
    """A node that contains a Lens.  The most important example of this kind of
    node is a Camera, but other kinds of nodes also contain a lens (for
    instance, a Spotlight).
    """

    def __init__(self, name: str, lens: Lens = ...) -> None: ...
    @overload
    def copy_lens(self, lens: Lens) -> None:
        """`(self, lens: Lens)`:
        Sets up the LensNode using a copy of the indicated Lens.  If the original
        Lens is changed or destroyed, this LensNode is not affected.

        `(self, index: int, lens: Lens)`:
        Copies the indicated lens into the specified slot.
        """
    @overload
    def copy_lens(self, index: int, lens: Lens) -> None: ...
    @overload
    def set_lens(self, lens: Lens) -> None:
        """`(self, lens: Lens)`:
        Sets up the LensNode using this particular Lens pointer.  If the lens is
        subsequently modified, the LensNode properties immediately reflect the
        change.

        `(self, index: int, lens: Lens)`:
        Sets the indicated lens.  Although a LensNode normally holds only one lens,
        it may optionally include multiple lenses, each with a different index
        number.  The different lenses may be referenced by index number on the
        DisplayRegion.  Adding a new lens automatically makes it active.
        """
    @overload
    def set_lens(self, index: int, lens: Lens) -> None: ...
    def get_lens(self, index: int = ...) -> Lens:
        """Returns a pointer to the particular Lens associated with this LensNode, or
        NULL if there is not yet a Lens associated.  If an index number is
        specified, returns the nth lens.
        """
    def set_lens_active(self, index: int, active: bool) -> bool:
        """Sets the active flag for the nth lens.  When a lens is inactive, it is not
        used for rendering, and any DisplayRegions associated with it are
        implicitly inactive as well.  Returns true if the flag is changed, false if
        it already had this value.
        """
    def get_lens_active(self, index: int) -> bool:
        """Returns the active flag for the nth lens."""
    def activate_lens(self, index: int) -> bool:
        """An alternate way to call set_lens_active(index, true)."""
    def deactivate_lens(self, index: int) -> bool:
        """An alternate way to call set_lens_active(index, false)."""
    @overload
    def is_in_view(self, pos: Vec3Like) -> bool:
        """Returns true if the given point is within the bounds of the lens of the
        LensNode (i.e.  if the camera can see the point).
        """
    @overload
    def is_in_view(self, index: int, pos: Vec3Like) -> bool: ...
    def show_frustum(self) -> None:
        """Enables the drawing of the lens's frustum to aid in visualization.  This
        actually creates a GeomNode which is parented to the LensNode.
        """
    def hide_frustum(self) -> None:
        """Disables the drawing of the lens's frustum to aid in visualization."""
    copyLens = copy_lens
    setLens = set_lens
    getLens = get_lens
    setLensActive = set_lens_active
    getLensActive = get_lens_active
    activateLens = activate_lens
    deactivateLens = deactivate_lens
    isInView = is_in_view
    showFrustum = show_frustum
    hideFrustum = hide_frustum

class WeakNodePath:
    """This class is a wrapper around a NodePath that, unlike the actual NodePath
    class, doesn't hold a reference count to the node.  Thus the node may be
    detached from the scene graph and destructed at any time.

    You can call is_valid() or was_deleted() at any time to determine whether
    the node is still around; if it is, get_node_path() will return the
    associated NodePath.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, node_path: NodePath) -> None: ...
    @overload
    def __init__(self, copy: WeakNodePath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: NodePath | WeakNodePath) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def assign(self, node_path: NodePath) -> Self: ...
    @overload
    def assign(self, copy: WeakNodePath) -> Self: ...
    def clear(self) -> None:
        """Sets this NodePath to the empty NodePath.  It will no longer point to any
        node.
        """
    def is_empty(self) -> bool:
        """Returns true if the NodePath contains no nodes, or if it has been deleted."""
    def was_deleted(self) -> bool:
        """Returns true if the NodePath we were referencing has been quietly deleted
        outside of the WeakNodePath.
        """
    def get_node_path(self) -> NodePath:
        """Returns the NodePath held within this object, or an empty NodePath with the
        error flag set if the object was deleted.
        """
    def node(self) -> PandaNode:
        """Returns the PandaNode held within this object, or nullptr if the object was
        deleted.
        """
    def compare_to(self, other: NodePath | WeakNodePath) -> int:
        """`(self, other: NodePath)`:
        Returns a number less than zero if this NodePath sorts before the other
        one, greater than zero if it sorts after, or zero if they are equivalent.

        Two NodePaths are considered equivalent if they consist of exactly the same
        list of nodes in the same order.  Otherwise, they are different; different
        NodePaths will be ranked in a consistent but undefined ordering; the
        ordering is useful only for placing the NodePaths in a sorted container
        like an STL set.

        `(self, other: WeakNodePath)`:
        Returns a number less than zero if this WeakNodePath sorts before the other
        one, greater than zero if it sorts after, or zero if they are equivalent.

        Two WeakNodePaths are considered equivalent if they consist of exactly the
        same list of nodes in the same order.  Otherwise, they are different;
        different WeakNodePaths will be ranked in a consistent but undefined
        ordering; the ordering is useful only for placing the WeakNodePaths in a
        sorted container like an STL set.
        """
    def get_key(self) -> int:
        """Returns the same values as NodePath::get_key()."""
    def output(self, out: ostream) -> None: ...
    isEmpty = is_empty
    wasDeleted = was_deleted
    getNodePath = get_node_path
    compareTo = compare_to
    getKey = get_key

class Camera(LensNode):
    """A node that can be positioned around in the scene graph to represent a
    point of view for rendering a scene.
    """

    active: bool
    scene: NodePath
    camera_mask: DrawMask
    cull_center: NodePath
    cull_bounds: BoundingVolume
    lod_center: NodePath
    initial_state: RenderState
    tag_state_key: str
    lod_scale: float
    @property
    def display_regions(self) -> Sequence[DisplayRegion]: ...
    @property
    def tag_states(self) -> MutableMapping[str, RenderState]: ...
    @property
    def aux_scene_data(self) -> MutableMapping[NodePath, AuxSceneData]: ...
    @overload
    def __init__(self, copy: Camera) -> None: ...
    @overload
    def __init__(self, name: str, lens: Lens = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_active(self, active: bool) -> None:
        """Sets the active flag on the camera.  When the camera is not active, nothing
        will be rendered.
        """
    def is_active(self) -> bool:
        """Returns the current setting of the active flag on the camera."""
    def set_scene(self, scene: NodePath) -> None:
        """Sets the scene that will be rendered by the camera.  This is normally the
        root node of a scene graph, typically a node called 'render', although it
        could represent the root of any subgraph.

        Note that the use of this method is now deprecated.  In the absence of an
        explicit scene set on the camera, the camera will render whatever scene it
        is parented into.  This is the preferred way to specify the scene, since it
        is the more intuitive mechanism.
        """
    def get_scene(self) -> NodePath:
        """Returns the scene that will be rendered by the camera.  See set_scene()."""
    def get_num_display_regions(self) -> int:
        """Returns the number of display regions associated with the camera."""
    def get_display_region(self, n: int) -> DisplayRegion:
        """Returns the nth display region associated with the camera."""
    def set_camera_mask(self, mask: DrawMask | int) -> None:
        """Changes the set of bits that represent the subset of the scene graph the
        camera will render.

        During the cull traversal, a node is not visited if none of its draw mask
        bits intersect with the camera's camera mask bits.  These masks can be used
        to selectively hide and show different parts of the scene graph from
        different cameras that are otherwise viewing the same scene.
        """
    def get_camera_mask(self) -> DrawMask:
        """Returns the set of bits that represent the subset of the scene graph the
        camera will render.  See set_camera_mask().
        """
    def set_cull_center(self, cull_center: NodePath) -> None:
        """Specifies the point from which the culling operations are performed.
        Normally, this is the same as the camera, and that is the default if this
        is not specified; but it may sometimes be useful to perform the culling
        from some other viewpoint, particularly when you are debugging the culling
        itself.
        """
    def get_cull_center(self) -> NodePath:
        """Returns the point from which the culling operations will be performed, if
        it was set by set_cull_center(), or the empty NodePath otherwise.
        """
    def set_cull_bounds(self, cull_bounds: BoundingVolume) -> None:
        """Specifies the bounding volume that should be used to perform culling from
        this camera.  Normally, this is the bounding volume returned from the
        active lens' make_bounds() call, but you may override this to specify a
        custom volume if you require.  The specified bounding volume will be
        understood to be in the coordinate space of the get_cull_center() node.
        """
    def get_cull_bounds(self) -> BoundingVolume:
        """Returns the custom cull volume that was set by set_cull_bounds(), if any,
        or NULL if no custom cull volume was set.
        """
    def set_lod_center(self, lod_center: NodePath) -> None:
        """Specifies the point from which the LOD distances are measured.  Normally,
        this is the same as the camera, and that is the default if this is not
        specified; but it may sometimes be useful to perform the distance test from
        some other viewpoint.  This may be used, for instance, to reduce LOD
        popping when the camera rotates in a small circle about an avatar.
        """
    def get_lod_center(self) -> NodePath:
        """Returns the point from which the LOD distances will be measured, if it was
        set by set_lod_center(), or the empty NodePath otherwise.
        """
    def set_initial_state(self, state: RenderState) -> None:
        """Sets the initial state which is applied to all nodes in the scene, as if it
        were set at the top of the scene graph.
        """
    def get_initial_state(self) -> RenderState:
        """Returns the initial state as set by a previous call to set_initial_state()."""
    def set_tag_state_key(self, tag_state_key: str) -> None:
        """Sets the tag key which, when encountered as a tag on nodes in the scene
        graph, causes this Camera to apply an arbitrary state transition based on
        the value of the tag (as specified to set_tag_state()).
        """
    def get_tag_state_key(self) -> str:
        """Returns the tag key as set by a previous call to set_tag_state_key()."""
    def set_lod_scale(self, value: float) -> None:
        """Sets the multiplier for LOD distances.  This value is multiplied with the
        LOD scale set on LodNodes.
        """
    def get_lod_scale(self) -> float:
        """Returns the multiplier for LOD distances."""
    def set_tag_state(self, tag_state: str, state: RenderState) -> None:
        """Associates a particular state transition with the indicated tag value.
        When a node is encountered during traversal with the tag key specified by
        set_tag_state_key(), if the value of that tag matches tag_state, then the
        indicated state is applied to this node--but only when it is rendered by
        this camera.

        This can be used to apply special effects to nodes when they are rendered
        by certain cameras.  It is particularly useful for multipass rendering, in
        which specialty cameras might be needed to render the scene with a
        particular set of effects.
        """
    def clear_tag_state(self, tag_state: str) -> None:
        """Removes the association established by a previous call to set_tag_state()."""
    def clear_tag_states(self) -> None:
        """Removes all associations established by previous calls to set_tag_state()."""
    def has_tag_state(self, tag_state: str) -> bool:
        """Returns true if set_tag_state() has previously been called with the
        indicated tag state, false otherwise.
        """
    def get_tag_state(self, tag_state: str) -> RenderState:
        """Returns the state associated with the indicated tag state by a previous
        call to set_tag_state(), or the empty state if nothing has been associated.
        """
    def set_aux_scene_data(self, node_path: NodePath, data: AuxSceneData) -> None:
        """Associates the indicated AuxSceneData object with the given NodePath,
        possibly replacing a previous data defined for the same NodePath, if any.
        """
    def clear_aux_scene_data(self, node_path: NodePath) -> bool:
        """Removes the AuxSceneData associated with the indicated NodePath.  Returns
        true if it is removed successfully, false if it was already gone.
        """
    def get_aux_scene_data(self, node_path: NodePath) -> AuxSceneData:
        """Returns the AuxSceneData associated with the indicated NodePath, or NULL if
        nothing is associated.
        """
    def list_aux_scene_data(self, out: ostream) -> None:
        """Outputs all of the NodePaths and AuxSceneDatas in use."""
    def cleanup_aux_scene_data(self, current_thread: Thread = ...) -> int:
        """Walks through the list of currently-assigned AuxSceneData objects and
        releases any that are past their expiration times.  Returns the number of
        elements released.
        """
    def get_display_regions(self) -> tuple[DisplayRegion, ...]: ...
    setActive = set_active
    isActive = is_active
    setScene = set_scene
    getScene = get_scene
    getNumDisplayRegions = get_num_display_regions
    getDisplayRegion = get_display_region
    setCameraMask = set_camera_mask
    getCameraMask = get_camera_mask
    setCullCenter = set_cull_center
    getCullCenter = get_cull_center
    setCullBounds = set_cull_bounds
    getCullBounds = get_cull_bounds
    setLodCenter = set_lod_center
    getLodCenter = get_lod_center
    setInitialState = set_initial_state
    getInitialState = get_initial_state
    setTagStateKey = set_tag_state_key
    getTagStateKey = get_tag_state_key
    setLodScale = set_lod_scale
    getLodScale = get_lod_scale
    setTagState = set_tag_state
    clearTagState = clear_tag_state
    clearTagStates = clear_tag_states
    hasTagState = has_tag_state
    getTagState = get_tag_state
    setAuxSceneData = set_aux_scene_data
    clearAuxSceneData = clear_aux_scene_data
    getAuxSceneData = get_aux_scene_data
    listAuxSceneData = list_aux_scene_data
    cleanupAuxSceneData = cleanup_aux_scene_data
    getDisplayRegions = get_display_regions

class PlaneNode(PandaNode):
    """A node that contains a plane.  This is most often used as a clipping plane,
    but it can serve other purposes as well; whenever a plane is needed to be
    defined in some coordinate space in the world.
    """

    CE_visible: Final = 1
    CEVisible: Final = 1
    CE_collision: Final = 2
    CECollision: Final = 2
    plane: LPlane
    viz_scale: float
    priority: int
    clip_effect: int
    def __init__(self, name: str, plane: Vec4Like = ...) -> None: ...
    def set_plane(self, plane: Vec4Like) -> None:
        """Sets the particular plane represented by the PlaneNode."""
    def get_plane(self) -> LPlane:
        """Returns the plane represented by the PlaneNode."""
    def set_viz_scale(self, viz_scale: float) -> None:
        """Specifies the size of the visual representation of the plane that is drawn
        if the PlaneNode is shown.
        """
    def get_viz_scale(self) -> float:
        """Returns the size of the visual representation of the plane that is drawn if
        the PlaneNode is shown.
        """
    def set_priority(self, priority: int) -> None:
        """Changes the relative importance of this PlaneNode (when it is used as a
        clip plane) relative to the other clip planes that are applied
        simultaneously.

        The priority number is used to decide which of the requested clip planes
        are to be activated when more clip planes are requested than the hardware
        will support.  The highest-priority n planes are selected for rendering.

        This is similar to TextureStage::set_priority().
        """
    def get_priority(self) -> int:
        """Returns the priority associated with this clip plane.  See set_priority()."""
    def set_clip_effect(self, clip_effect: int) -> None:
        """Specifies the sort of things this plane will actually clip (when it is used
        as a clip plane).  This is a bitmask union of ClipEffect values.  If it
        includes CE_visible, then it will clip visible geometry; if it includes
        CE_collision, then it will clip collision polygons.  If it includes neither
        bit, it will still affect culling, but objects will either be wholly behind
        the clipping plane, or wholly present.
        """
    def get_clip_effect(self) -> int:
        """Returns the clip_effect bits for this clip plane.  See set_clip_effect()."""
    setPlane = set_plane
    getPlane = get_plane
    setVizScale = set_viz_scale
    getVizScale = get_viz_scale
    setPriority = set_priority
    getPriority = get_priority
    setClipEffect = set_clip_effect
    getClipEffect = get_clip_effect

class ClipPlaneAttrib(RenderAttrib):
    """This functions similarly to a LightAttrib.  It indicates the set of
    clipping planes that modify the geometry at this level and below.  A
    ClipPlaneAttrib can either add planes or remove planes from the total set
    of clipping planes in effect.
    """

    O_set: Final = 0
    OSet: Final = 0
    O_add: Final = 1
    OAdd: Final = 1
    O_remove: Final = 2
    ORemove: Final = 2
    @property
    def class_slot(self) -> int: ...
    @overload
    @staticmethod
    def make() -> RenderAttrib:
        """`()`:
        The following is the new, more general interface to the ClipPlaneAttrib.

        `(op: _ClipPlaneAttrib_Operation, plane: PlaneNode)`:
        Constructs a new ClipPlaneAttrib object that enables (or disables,
        according to op) the indicated plane(s).

        @deprecated Use add_on_plane() or add_off_plane() instead.

        `(op: _ClipPlaneAttrib_Operation, plane1: PlaneNode, plane2: PlaneNode)`; `(op: _ClipPlaneAttrib_Operation, plane1: PlaneNode, plane2: PlaneNode, plane3: PlaneNode)`; `(op: _ClipPlaneAttrib_Operation, plane1: PlaneNode, plane2: PlaneNode, plane3: PlaneNode, plane4: PlaneNode)`:
        Constructs a new ClipPlaneAttrib object that turns on (or off, according to
        op) the indicate plane(s).

        @deprecated Use add_on_plane() or add_off_plane() instead.
        """
    @overload
    @staticmethod
    def make(op: _ClipPlaneAttrib_Operation, plane: PlaneNode) -> RenderAttrib: ...
    @overload
    @staticmethod
    def make(op: _ClipPlaneAttrib_Operation, plane1: PlaneNode, plane2: PlaneNode, plane3: PlaneNode = ...) -> RenderAttrib: ...
    @overload
    @staticmethod
    def make(
        op: _ClipPlaneAttrib_Operation, plane1: PlaneNode, plane2: PlaneNode, plane3: PlaneNode, plane4: PlaneNode
    ) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_operation(self) -> _ClipPlaneAttrib_Operation:
        """Returns the basic operation type of the ClipPlaneAttrib.  If this is O_set,
        the planes listed here completely replace any planes that were already on.
        If this is O_add, the planes here are added to the set of planes that
        were already on, and if O_remove, the planes here are removed from the set
        of planes that were on.

        @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
        off_planes, so this method no longer makes sense.  Query the lists
        independently.
        """
    def get_num_planes(self) -> int:
        """Returns the number of planes listed in the attribute.

        @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
        off_planes, so this method no longer makes sense.  Query the lists
        independently.
        """
    def get_plane(self, n: int) -> PlaneNode:
        """Returns the nth plane listed in the attribute.

        @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
        off_planes, so this method no longer makes sense.  Query the lists
        independently.
        """
    def has_plane(self, plane: PlaneNode) -> bool:
        """Returns true if the indicated plane is listed in the attrib, false
        otherwise.

        @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
        off_planes, so this method no longer makes sense.  Query the lists
        independently.
        """
    def add_plane(self, plane: PlaneNode) -> RenderAttrib:
        """Returns a new ClipPlaneAttrib, just like this one, but with the indicated
        plane added to the list of planes.

        @deprecated Use add_on_plane() or add_off_plane() instead.
        """
    def remove_plane(self, plane: PlaneNode) -> RenderAttrib:
        """Returns a new ClipPlaneAttrib, just like this one, but with the indicated
        plane removed from the list of planes.

        @deprecated Use remove_on_plane() or remove_off_plane() instead.
        """
    @staticmethod
    def make_all_off() -> RenderAttrib:
        """Constructs a new ClipPlaneAttrib object that disables all planes (and hence
        disables clipping).
        """
    def get_num_on_planes(self) -> int:
        """Returns the number of planes that are enabled by the attribute."""
    def get_on_plane(self, n: int) -> NodePath:
        """Returns the nth plane enabled by the attribute, sorted in render order."""
    def has_on_plane(self, plane: NodePath) -> bool:
        """Returns true if the indicated plane is enabled by the attrib, false
        otherwise.
        """
    def get_num_off_planes(self) -> int:
        """Returns the number of planes that are disabled by the attribute."""
    def get_off_plane(self, n: int) -> NodePath:
        """Returns the nth plane disabled by the attribute, sorted in arbitrary
        (pointer) order.
        """
    def has_off_plane(self, plane: NodePath) -> bool:
        """Returns true if the indicated plane is disabled by the attrib, false
        otherwise.
        """
    def has_all_off(self) -> bool:
        """Returns true if this attrib disables all planes (although it may also
        enable some).
        """
    def is_identity(self) -> bool:
        """Returns true if this is an identity attrib: it does not change the set of
        planes in use.
        """
    def add_on_plane(self, plane: NodePath) -> RenderAttrib:
        """Returns a new ClipPlaneAttrib, just like this one, but with the indicated
        plane added to the list of planes enabled by this attrib.
        """
    def remove_on_plane(self, plane: NodePath) -> RenderAttrib:
        """Returns a new ClipPlaneAttrib, just like this one, but with the indicated
        plane removed from the list of planes enabled by this attrib.
        """
    def add_off_plane(self, plane: NodePath) -> RenderAttrib:
        """Returns a new ClipPlaneAttrib, just like this one, but with the indicated
        plane added to the list of planes disabled by this attrib.
        """
    def remove_off_plane(self, plane: NodePath) -> RenderAttrib:
        """Returns a new ClipPlaneAttrib, just like this one, but with the indicated
        plane removed from the list of planes disabled by this attrib.
        """
    def filter_to_max(self, max_clip_planes: int) -> ClipPlaneAttrib:
        """Returns a new ClipPlaneAttrib, very much like this one, but with the number
        of on_planes reduced to be no more than max_clip_planes.  The number of
        off_planes in the new ClipPlaneAttrib is undefined.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    def get_on_planes(self) -> tuple[NodePath, ...]: ...
    def get_off_planes(self) -> tuple[NodePath, ...]: ...
    makeDefault = make_default
    getOperation = get_operation
    getNumPlanes = get_num_planes
    getPlane = get_plane
    hasPlane = has_plane
    addPlane = add_plane
    removePlane = remove_plane
    makeAllOff = make_all_off
    getNumOnPlanes = get_num_on_planes
    getOnPlane = get_on_plane
    hasOnPlane = has_on_plane
    getNumOffPlanes = get_num_off_planes
    getOffPlane = get_off_plane
    hasOffPlane = has_off_plane
    hasAllOff = has_all_off
    isIdentity = is_identity
    addOnPlane = add_on_plane
    removeOnPlane = remove_on_plane
    addOffPlane = add_off_plane
    removeOffPlane = remove_off_plane
    filterToMax = filter_to_max
    getClassSlot = get_class_slot
    getOnPlanes = get_on_planes
    getOffPlanes = get_off_planes

class ColorAttrib(RenderAttrib):
    """Indicates what color should be applied to renderable geometry."""

    T_vertex: Final = 0
    TVertex: Final = 0
    T_flat: Final = 1
    TFlat: Final = 1
    T_off: Final = 2
    TOff: Final = 2
    @property
    def color_type(self) -> _ColorAttrib_Type: ...
    @property
    def color(self) -> LColor: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_vertex() -> RenderAttrib:
        """Constructs a new ColorAttrib object that indicates geometry should be
        rendered according to its own vertex color.
        """
    @staticmethod
    def make_flat(color: Vec4Like) -> RenderAttrib:
        """Constructs a new ColorAttrib object that indicates geometry should be
        rendered in the indicated color.
        """
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new ColorAttrib object that indicates geometry should be
        rendered in white.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_color_type(self) -> _ColorAttrib_Type:
        """Returns the type of color specified by this ColorAttrib.  The options are:

        T_vertex - use the vertex color specified in the geometry itself.

        T_flat - use the color specified in this ColorAttrib for all geometry.  You
        can get this color via get_color().

        T_off - use the color white.
        """
    def get_color(self) -> LColor:
        """If the type is T_flat or T_off, this returns the color that will be applied
        to geometry.  If the type is T_vertex, this is meaningless.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeVertex = make_vertex
    makeFlat = make_flat
    makeOff = make_off
    makeDefault = make_default
    getColorType = get_color_type
    getColor = get_color
    getClassSlot = get_class_slot

class ColorBlendAttrib(RenderAttrib):
    """This specifies how colors are blended into the frame buffer, for special
    effects.  This overrides transparency if transparency is also specified.
    """

    M_add: Final = 1
    MAdd: Final = 1
    M_subtract: Final = 2
    MSubtract: Final = 2
    M_inv_subtract: Final = 3
    MInvSubtract: Final = 3
    M_min: Final = 4
    MMin: Final = 4
    M_max: Final = 5
    MMax: Final = 5
    O_zero: Final = 0
    OZero: Final = 0
    O_one: Final = 1
    OOne: Final = 1
    O_incoming_color: Final = 2
    OIncomingColor: Final = 2
    O_one_minus_incoming_color: Final = 3
    OOneMinusIncomingColor: Final = 3
    O_fbuffer_color: Final = 4
    OFbufferColor: Final = 4
    O_one_minus_fbuffer_color: Final = 5
    OOneMinusFbufferColor: Final = 5
    O_incoming_alpha: Final = 6
    OIncomingAlpha: Final = 6
    O_one_minus_incoming_alpha: Final = 7
    OOneMinusIncomingAlpha: Final = 7
    O_fbuffer_alpha: Final = 8
    OFbufferAlpha: Final = 8
    O_one_minus_fbuffer_alpha: Final = 9
    OOneMinusFbufferAlpha: Final = 9
    O_constant_color: Final = 10
    OConstantColor: Final = 10
    O_one_minus_constant_color: Final = 11
    OOneMinusConstantColor: Final = 11
    O_constant_alpha: Final = 12
    OConstantAlpha: Final = 12
    O_one_minus_constant_alpha: Final = 13
    OOneMinusConstantAlpha: Final = 13
    O_incoming_color_saturate: Final = 14
    OIncomingColorSaturate: Final = 14
    O_incoming1_color: Final = 15
    OIncoming1Color: Final = 15
    O_one_minus_incoming1_color: Final = 16
    OOneMinusIncoming1Color: Final = 16
    O_incoming1_alpha: Final = 17
    OIncoming1Alpha: Final = 17
    O_one_minus_incoming1_alpha: Final = 18
    OOneMinusIncoming1Alpha: Final = 18
    O_color_scale: Final = 19
    OColorScale: Final = 19
    O_one_minus_color_scale: Final = 20
    OOneMinusColorScale: Final = 20
    O_alpha_scale: Final = 21
    OAlphaScale: Final = 21
    O_one_minus_alpha_scale: Final = 22
    OOneMinusAlphaScale: Final = 22
    @property
    def rgb_mode(self) -> _ColorBlendAttrib_Mode: ...
    @property
    def rgb_operand_a(self) -> _ColorBlendAttrib_Operand: ...
    @property
    def rgb_operand_b(self) -> _ColorBlendAttrib_Operand: ...
    @property
    def alpha_mode(self) -> _ColorBlendAttrib_Mode: ...
    @property
    def alpha_operand_a(self) -> _ColorBlendAttrib_Operand: ...
    @property
    def alpha_operand_b(self) -> _ColorBlendAttrib_Operand: ...
    @property
    def color(self) -> LColor: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new ColorBlendAttrib object that disables special-effect
        blending, allowing normal transparency to be used instead.
        """
    @overload
    @staticmethod
    def make(mode: _ColorBlendAttrib_Mode) -> RenderAttrib:
        """`(mode: _ColorBlendAttrib_Mode)`:
        Constructs a new ColorBlendAttrib object.

        @deprecated Use the three- or four-parameter constructor instead.

        `(rgb_mode: _ColorBlendAttrib_Mode, rgb_a: _ColorBlendAttrib_Operand, rgb_b: _ColorBlendAttrib_Operand, alpha_mode: _ColorBlendAttrib_Mode, alpha_a: _ColorBlendAttrib_Operand, alpha_b: _ColorBlendAttrib_Operand, color: LColor = ...)`:
        Constructs a new ColorBlendAttrib object that enables special-effect
        blending.  This supercedes transparency.  This form is used to specify
        separate blending parameters for the RGB and alpha channels.

        `(mode: _ColorBlendAttrib_Mode, a: _ColorBlendAttrib_Operand, b: _ColorBlendAttrib_Operand, color: LColor = ...)`:
        Constructs a new ColorBlendAttrib object that enables special-effect
        blending.  This supercedes transparency.  The given mode and operands are
        used for both the RGB and alpha channels.
        """
    @overload
    @staticmethod
    def make(
        mode: _ColorBlendAttrib_Mode, a: _ColorBlendAttrib_Operand, b: _ColorBlendAttrib_Operand, color: Vec4Like = ...
    ) -> RenderAttrib: ...
    @overload
    @staticmethod
    def make(
        rgb_mode: _ColorBlendAttrib_Mode,
        rgb_a: _ColorBlendAttrib_Operand,
        rgb_b: _ColorBlendAttrib_Operand,
        alpha_mode: _ColorBlendAttrib_Mode,
        alpha_a: _ColorBlendAttrib_Operand,
        alpha_b: _ColorBlendAttrib_Operand,
        color: Vec4Like = ...,
    ) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> _ColorBlendAttrib_Mode:
        """Returns the blending mode for the RGB channels."""
    def get_operand_a(self) -> _ColorBlendAttrib_Operand:
        """Returns the RGB multiplier for the first component."""
    def get_operand_b(self) -> _ColorBlendAttrib_Operand:
        """Returns the RGB multiplier for the second component."""
    def get_alpha_mode(self) -> _ColorBlendAttrib_Mode:
        """Returns the blending mode for the alpha channel."""
    def get_alpha_operand_a(self) -> _ColorBlendAttrib_Operand:
        """Returns the alpha multiplier for the first component."""
    def get_alpha_operand_b(self) -> _ColorBlendAttrib_Operand:
        """Returns the alpha multiplier for the second component."""
    def get_color(self) -> LColor:
        """Returns the constant color associated with the attrib."""
    def involves_constant_color(self, operand: _ColorBlendAttrib_Operand = ...) -> bool:
        """`(self)`:
        Returns true if the this attrib uses the constant color, false otherwise.

        `(self, operand: _ColorBlendAttrib_Operand)`:
        Returns true if the indicated operand uses the constant color, false
        otherwise.
        """
    def involves_color_scale(self, operand: _ColorBlendAttrib_Operand = ...) -> bool:
        """`(self)`:
        Returns true if the this attrib uses the color scale attrib, false
        otherwise.

        `(self, operand: _ColorBlendAttrib_Operand)`:
        Returns true if the indicated operand uses the color scale attrib, false
        otherwise.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    getMode = get_mode
    getOperandA = get_operand_a
    getOperandB = get_operand_b
    getAlphaMode = get_alpha_mode
    getAlphaOperandA = get_alpha_operand_a
    getAlphaOperandB = get_alpha_operand_b
    getColor = get_color
    involvesConstantColor = involves_constant_color
    involvesColorScale = involves_color_scale
    getClassSlot = get_class_slot

class ColorScaleAttrib(RenderAttrib):
    """Applies a scale to colors in the scene graph and on vertices."""

    @property
    def scale(self) -> LVecBase4: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_identity() -> RenderAttrib:
        """Constructs an identity scale attrib."""
    @staticmethod
    def make(scale: Vec4Like) -> RenderAttrib:
        """Constructs a new ColorScaleAttrib object that indicates geometry should be
        scaled by the indicated factor.
        """
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new ColorScaleAttrib object that ignores any ColorScaleAttrib
        inherited from above.  You may also specify an additional color scale to
        apply to geometry below (using set_scale()).
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def is_off(self) -> bool:
        """Returns true if the ColorScaleAttrib will ignore any color scales inherited
        from above, false otherwise.  This is not the same thing as !has_scale(); a
        ColorScaleAttrib may have the "off" flag set and also have another scale
        specified.
        """
    def is_identity(self) -> bool:
        """Returns true if the ColorScaleAttrib is an identity attrib, false if it is
        either an off attrib or it has a scale.
        """
    def has_scale(self) -> bool:
        """Returns true if the ColorScaleAttrib has a non-identity scale, false
        otherwise (in which case it might be an off attrib or an identity attrib).
        """
    def has_rgb_scale(self) -> bool:
        """Returns true if the ColorScaleAttrib has a non-identity scale in the RGB
        components (ignoring alpha), or false otherwise.
        """
    def has_alpha_scale(self) -> bool:
        """Returns true if the ColorScaleAttrib has a non-identity scale in the alpha
        component (ignoring RGB), or false otherwise.
        """
    def get_scale(self) -> LVecBase4:
        """Returns the scale to be applied to colors."""
    def set_scale(self, scale: Vec4Like) -> RenderAttrib:
        """Returns a new ColorScaleAttrib, just like this one, but with the scale
        changed to the indicated value.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeIdentity = make_identity
    makeOff = make_off
    makeDefault = make_default
    isOff = is_off
    isIdentity = is_identity
    hasScale = has_scale
    hasRgbScale = has_rgb_scale
    hasAlphaScale = has_alpha_scale
    getScale = get_scale
    setScale = set_scale
    getClassSlot = get_class_slot

class ColorWriteAttrib(RenderAttrib):
    """Enables or disables writing to the color buffer.  This is primarily useful
    for certain special effects in which it is important to write to the depth
    buffer without affecting the color buffer.
    """

    C_off: Final = 0
    COff: Final = 0
    C_red: Final = 1
    CRed: Final = 1
    C_green: Final = 2
    CGreen: Final = 2
    C_blue: Final = 4
    CBlue: Final = 4
    C_rgb: Final = 7
    CRgb: Final = 7
    C_alpha: Final = 8
    CAlpha: Final = 8
    C_all: Final = 15
    CAll: Final = 15
    @property
    def channels(self) -> int: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(channels: int) -> RenderAttrib:
        """Constructs a new ColorWriteAttrib object."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_channels(self) -> int:
        """Returns the mask of color channels that are enabled by this attrib."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getChannels = get_channels
    getClassSlot = get_class_slot

class CompassEffect(RenderEffect):
    """A CompassEffect causes a node to inherit its rotation (or pos or scale, if
    specified) from some other reference node in the graph, or more often from
    the root.

    In its purest form, a CompassEffect is used to keep the node's rotation
    fixed relative to the top of the scene graph, despite other transforms that
    may exist above the node.  Hence the name: the node behaves like a magnetic
    compass, always pointing in the same direction.

    As an couple of generalizing extensions, the CompassEffect may also be set
    up to always orient its node according to some other reference node than
    the root of the scene graph.  Furthermore, it may optionally adjust any of
    pos, rotation, or scale, instead of necessarily rotation; and it may adjust
    individual pos and scale components.  (Rotation may not be adjusted on an
    individual component basis; that's just asking for trouble.)

    Be careful when using the pos and scale modes.  In these modes, it's
    possible for the CompassEffect to move its node far from its normal
    bounding volume, causing culling to fail.  If this is an issue, you may
    need to explicitly set a large (or infinite) bounding volume on the effect
    node.
    """

    P_x: Final = 1
    PX: Final = 1
    P_y: Final = 2
    PY: Final = 2
    P_z: Final = 4
    PZ: Final = 4
    P_pos: Final = 7
    PPos: Final = 7
    P_rot: Final = 8
    PRot: Final = 8
    P_sx: Final = 16
    PSx: Final = 16
    P_sy: Final = 32
    PSy: Final = 32
    P_sz: Final = 64
    PSz: Final = 64
    P_scale: Final = 112
    PScale: Final = 112
    P_all: Final = 127
    PAll: Final = 127
    @staticmethod
    def make(reference: NodePath, properties: int = ...) -> RenderEffect:
        """Constructs a new CompassEffect object.  If the reference is an empty
        NodePath, it means the CompassEffect is relative to the root of the scene
        graph; otherwise, it's relative to the indicated node.  The properties
        bitmask specifies the set of properties that the compass node inherits from
        the reference instead of from its parent.
        """
    def get_reference(self) -> NodePath:
        """Returns the reference node from which the CompassEffect inherits its
        transform.  If this is empty, it means the root of the scene graph.
        """
    def get_properties(self) -> int:
        """Returns the bitmask of properties that this CompassEffect object inherits
        from its reference node (or from the root).
        """
    getReference = get_reference
    getProperties = get_properties

class CullBinEnums:
    """Provides scoping for the enumerated type shared by CullBin and
    CullBinManager.
    """

    BT_invalid: Final = 0
    BTInvalid: Final = 0
    BT_unsorted: Final = 1
    BTUnsorted: Final = 1
    BT_state_sorted: Final = 2
    BTStateSorted: Final = 2
    BT_back_to_front: Final = 3
    BTBackToFront: Final = 3
    BT_front_to_back: Final = 4
    BTFrontToBack: Final = 4
    BT_fixed: Final = 5
    BTFixed: Final = 5
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: CullBinEnums = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class GeomNode(PandaNode):
    """A node that holds Geom objects, renderable pieces of geometry.  This is the
    primary kind of leaf node in the scene graph; almost all visible objects
    will be contained in a GeomNode somewhere.
    """

    @property
    def default_collide_mask(self) -> CollideMask: ...
    def set_preserved(self, value: bool) -> None:
        """Sets the "preserved" flag.  When this is true, the GeomNode will be left
        untouched by any flatten operations.
        """
    def get_preserved(self) -> bool:
        """Returns the "preserved" flag.  When this is true, the GeomNode will be left
        untouched by any flatten operations.
        """
    def get_num_geoms(self) -> int:
        """Returns the number of geoms in the node."""
    def get_geom(self, n: int) -> Geom:
        """Returns the nth geom of the node.  This object should not be modified,
        since the same object might be shared between multiple different GeomNodes,
        but see modify_geom().
        """
    def modify_geom(self, n: int) -> Geom:
        """Returns the nth geom of the node, suitable for modifying it.  If the nth
        Geom has multiple reference counts to it, reassigns it to an identical copy
        first, and returns the new copy--this provides a "copy on write" that
        ensures that the Geom that is returned is unique to this GeomNode and is
        not shared with any other GeomNodes.

        Note that if this method is called in a downstream stage (for instance,
        during cull or draw), then it will propagate the new list of Geoms upstream
        all the way to pipeline stage 0, which may step on changes that were made
        independently in pipeline stage 0. Use with caution.
        """
    def get_geom_state(self, n: int) -> RenderState:
        """Returns the RenderState associated with the nth geom of the node.  This is
        just the RenderState directly associated with the Geom; the actual state in
        which the Geom is rendered will also be affected by RenderStates that
        appear on the scene graph in nodes above this GeomNode.
        """
    def set_geom_state(self, n: int, state: RenderState) -> None:
        """Changes the RenderState associated with the nth geom of the node.  This is
        just the RenderState directly associated with the Geom; the actual state in
        which the Geom is rendered will also be affected by RenderStates that
        appear on the scene graph in nodes above this GeomNode.

        Note that if this method is called in a downstream stage (for instance,
        during cull or draw), then it will propagate the new list of Geoms upstream
        all the way to pipeline stage 0, which may step on changes that were made
        independently in pipeline stage 0. Use with caution.
        """
    def add_geom(self, geom: Geom, state: RenderState = ...) -> None:
        """Adds a new Geom to the node.  The geom is given the indicated state (which
        may be RenderState::make_empty(), to completely inherit its state from the
        scene graph).
        """
    def add_geoms_from(self, other: GeomNode) -> None:
        """Copies the Geoms (and their associated RenderStates) from the indicated
        GeomNode into this one.
        """
    def set_geom(self, n: int, geom: Geom) -> None:
        """Replaces the nth Geom of the node with a new pointer.  There must already
        be a Geom in this slot.

        Note that if this method is called in a downstream stage (for instance,
        during cull or draw), then it will propagate the new list of Geoms upstream
        all the way to pipeline stage 0, which may step on changes that were made
        independently in pipeline stage 0. Use with caution.
        """
    def remove_geom(self, n: int) -> None:
        """Removes the nth geom from the node."""
    def remove_all_geoms(self) -> None:
        """Removes all the geoms from the node at once."""
    def check_valid(self) -> bool:
        """Verifies that the each Geom within the GeomNode reference vertices that
        actually exist within its GeomVertexData.  Returns true if the GeomNode
        appears to be valid, false otherwise.
        """
    def decompose(self) -> None:
        """Calls decompose() on each Geom with the GeomNode.  This decomposes higher-
        order primitive types, like triangle strips, into lower-order types like
        indexed triangles.  Normally there is no reason to do this, but it can be
        useful as an early preprocessing step, to allow a later call to unify() to
        proceed more quickly.

        See also SceneGraphReducer::decompose(), which is the normal way this is
        called.
        """
    def unify(self, max_indices: int, preserve_order: bool) -> None:
        """Attempts to unify all of the Geoms contained within this node into a single
        Geom, or at least as few Geoms as possible.  In turn, the individual
        GeomPrimitives contained within each resulting Geom are also unified.  The
        goal is to reduce the number of GeomPrimitives within the node as far as
        possible.  This may result in composite primitives, such as triangle strips
        and triangle fans, being decomposed into triangles.  See also
        Geom::unify().

        max_indices represents the maximum number of indices that will be put in
        any one GeomPrimitive.  If preserve_order is true, then the primitives will
        not be reordered during the operation, even if this results in a suboptimal
        result.

        In order for this to be successful, the primitives must reference the same
        GeomVertexData, have the same fundamental primitive type, and have
        compatible shade models.
        """
    def write_geoms(self, out: ostream, indent_level: int) -> None:
        """Writes a short description of all the Geoms in the node."""
    def write_verbose(self, out: ostream, indent_level: int) -> None:
        """Writes a detailed description of all the Geoms in the node."""
    @staticmethod
    def get_default_collide_mask() -> CollideMask:
        """Returns the default into_collide_mask assigned to new GeomNodes."""
    def get_geoms(self) -> tuple[Geom, ...]: ...
    def modify_geoms(self) -> tuple[Geom, ...]: ...
    def get_geom_states(self) -> tuple[RenderState, ...]: ...
    setPreserved = set_preserved
    getPreserved = get_preserved
    getNumGeoms = get_num_geoms
    getGeom = get_geom
    modifyGeom = modify_geom
    getGeomState = get_geom_state
    setGeomState = set_geom_state
    addGeom = add_geom
    addGeomsFrom = add_geoms_from
    setGeom = set_geom
    removeGeom = remove_geom
    removeAllGeoms = remove_all_geoms
    checkValid = check_valid
    writeGeoms = write_geoms
    writeVerbose = write_verbose
    getDefaultCollideMask = get_default_collide_mask
    getGeoms = get_geoms
    modifyGeoms = modify_geoms
    getGeomStates = get_geom_states

class CullBinAttrib(RenderAttrib):
    """Assigns geometry to a particular bin by name.  The bins must be created
    separately via the CullBinManager interface.
    """

    @property
    def bin_name(self) -> str: ...
    @property
    def draw_order(self) -> int: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(bin_name: str, draw_order: int) -> RenderAttrib:
        """Constructs a new CullBinAttrib assigning geometry into the named bin.  If
        the bin name is the empty string, the default bin is used.

        The draw_order specifies further ordering information which is relevant
        only to certain kinds of bins (in particular CullBinFixed type bins).
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_bin_name(self) -> str:
        """Returns the name of the bin this attribute specifies.  If this is the empty
        string, it refers to the default bin.
        """
    def get_draw_order(self) -> int:
        """Returns the draw order this attribute specifies.  Some bins (in particular,
        CullBinFixed bins) use this to further specify the order in which objects
        should be rendered.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getBinName = get_bin_name
    getDrawOrder = get_draw_order
    getClassSlot = get_class_slot

class CullBinManager(CullBinEnums):
    """This is a global object that maintains the collection of named CullBins in
    the world.
    """

    def add_bin(self, name: str, type: _CullBinEnums_BinType, sort: int) -> int:
        """Defines a new bin with the indicated name, and returns the new bin_index.
        If there is already a bin with the same name returns its bin_index if it
        had the same properties; otherwise, reports an error and returns -1.
        """
    def remove_bin(self, bin_index: int) -> None:
        """Permanently removes the indicated bin.  This operation is not protected
        from the pipeline and will disturb whatever is currently rendering in draw.
        You should not call this during the normal course of rendering a frame; it
        is intended only as an aid to development, to allow the developer to
        interactively fiddle with the set of bins.
        """
    def get_num_bins(self) -> int:
        """Returns the number of bins in the world."""
    def get_bin(self, n: int) -> int:
        """Returns the bin_index of the nth bin in the set, where n is a number
        between 0 and get_num_bins(). This returns the list of bin_index numbers,
        in sorted order (that is, in the order in which the bins should be
        rendered).
        """
    def find_bin(self, name: str) -> int:
        """Returns the bin_index associated with the bin of the given name, or -1 if
        no bin has that name.
        """
    def get_bin_name(self, bin_index: int) -> str:
        """Returns the name of the bin with the indicated bin_index (where bin_index
        was retrieved by get_bin() or find_bin()).  The bin's name may not be
        changed during the life of the bin.
        """
    @overload
    def get_bin_type(self, bin_index: int) -> _CullBinEnums_BinType:
        """`(self, bin_index: int)`:
        Returns the type of the bin with the indicated bin_index (where bin_index
        was retrieved by get_bin() or find_bin()).

        `(self, name: str)`:
        Returns the type of the bin with the indicated name.
        """
    @overload
    def get_bin_type(self, name: str) -> _CullBinEnums_BinType: ...
    @overload
    def set_bin_type(self, bin_index: int, type: _CullBinEnums_BinType) -> None:
        """`(self, bin_index: int, type: _CullBinEnums_BinType)`:
        Changes the type of the bin with the indicated bin_index (where bin_index
        was retrieved by get_bin() or find_bin()).

        The change might be effective immediately, or it might take place next
        frame, depending on the bin type.

        `(self, name: str, type: _CullBinEnums_BinType)`:
        Changes the type of the bin with the indicated name.

        The change might be effective immediately, or it might take place next
        frame, depending on the bin type.
        """
    @overload
    def set_bin_type(self, name: str, type: _CullBinEnums_BinType) -> None: ...
    @overload
    def get_bin_sort(self, bin_index: int) -> int:
        """`(self, bin_index: int)`:
        Returns the sort order of the bin with the indicated bin_index (where
        bin_index was retrieved by get_bin() or find_bin()).

        The bins are rendered in increasing order by their sort order; this number
        may be changed from time to time to reorder the bins.

        `(self, name: str)`:
        Returns the sort order of the bin with the indicated name.

        The bins are rendered in increasing order by their sort order; this number
        may be changed from time to time to reorder the bins.
        """
    @overload
    def get_bin_sort(self, name: str) -> int: ...
    @overload
    def set_bin_sort(self, bin_index: int, sort: int) -> None:
        """`(self, bin_index: int, sort: int)`:
        Changes the sort order of the bin with the indicated bin_index (where
        bin_index was retrieved by get_bin() or find_bin()).

        The bins are rendered in increasing order by their sort order; this number
        may be changed from time to time to reorder the bins.

        `(self, name: str, sort: int)`:
        Changes the sort order of the bin with the indicated name.

        The bins are rendered in increasing order by their sort order; this number
        may be changed from time to time to reorder the bins.
        """
    @overload
    def set_bin_sort(self, name: str, sort: int) -> None: ...
    @overload
    def get_bin_active(self, bin_index: int) -> bool:
        """`(self, bin_index: int)`:
        Returns the active flag of the bin with the indicated bin_index (where
        bin_index was retrieved by get_bin() or find_bin()).

        When a bin is marked inactive, all geometry assigned to it is not rendered.

        `(self, name: str)`:
        Returns the active flag of the bin with the indicated name.

        When a bin is marked inactive, all geometry assigned to it is not rendered.
        """
    @overload
    def get_bin_active(self, name: str) -> bool: ...
    @overload
    def set_bin_active(self, bin_index: int, active: bool) -> None:
        """`(self, bin_index: int, active: bool)`:
        Changes the active flag of the bin with the indicated bin_index (where
        bin_index was retrieved by get_bin() or find_bin()).

        When a bin is marked inactive, all geometry assigned to it is not rendered.

        `(self, name: str, active: bool)`:
        Changes the active flag of the bin with the indicated name.

        When a bin is marked inactive, all geometry assigned to it is not rendered.
        """
    @overload
    def set_bin_active(self, name: str, active: bool) -> None: ...
    def get_bin_flash_active(self, bin_index: int) -> bool:
        """Returns true if the bin with the given bin_index is configured to flash at
        a predetermined color (where bin_index was retrieved by get_bin() or
        find_bin()).

        This method is not available in release builds.
        """
    def get_bin_flash_color(self, bin_index: int) -> LColor:
        """Returns the color that this bin has been configured to flash to, if
        configured.

        This method is not available in release builds.
        """
    def set_bin_flash_active(self, bin_index: int, active: bool) -> None:
        """When set to true, the given bin_index is configured to flash at a
        predetermined color (where bin_index was retrieved by get_bin() or
        find_bin()).

        This method is not available in release builds.
        """
    def set_bin_flash_color(self, bin_index: int, color: Vec4Like) -> None:
        """Changes the flash color for the given bin index.

        This method is not available in release builds.
        """
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_ptr() -> CullBinManager:
        """Returns the pointer to the global CullBinManager object."""
    def get_bins(self) -> tuple[int, ...]: ...
    addBin = add_bin
    removeBin = remove_bin
    getNumBins = get_num_bins
    getBin = get_bin
    findBin = find_bin
    getBinName = get_bin_name
    getBinType = get_bin_type
    setBinType = set_bin_type
    getBinSort = get_bin_sort
    setBinSort = set_bin_sort
    getBinActive = get_bin_active
    setBinActive = set_bin_active
    getBinFlashActive = get_bin_flash_active
    getBinFlashColor = get_bin_flash_color
    setBinFlashActive = set_bin_flash_active
    setBinFlashColor = set_bin_flash_color
    getGlobalPtr = get_global_ptr
    getBins = get_bins

class CullFaceAttrib(RenderAttrib):
    """Indicates which faces should be culled based on their vertex ordering."""

    M_cull_none: Final = 0
    MCullNone: Final = 0
    M_cull_clockwise: Final = 1
    MCullClockwise: Final = 1
    M_cull_counter_clockwise: Final = 2
    MCullCounterClockwise: Final = 2
    M_cull_unchanged: Final = 3
    MCullUnchanged: Final = 3
    @property
    def mode(self) -> _CullFaceAttrib_Mode: ...
    @property
    def reverse(self) -> bool: ...
    @property
    def effective_mode(self) -> _CullFaceAttrib_Mode: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _CullFaceAttrib_Mode = ...) -> RenderAttrib:
        """Constructs a new CullFaceAttrib object that specifies how to cull geometry.
        By Panda convention, vertices are ordered counterclockwise when seen from
        the front, so the M_cull_clockwise will cull backfacing polygons.

        M_cull_unchanged is an identity attrib; if this is applied to vertices
        without any other intervening attrib, it is the same as applying the
        default attrib.
        """
    @staticmethod
    def make_reverse() -> RenderAttrib:
        """Constructs a new CullFaceAttrib object that reverses the effects of any
        other CullFaceAttrib objects in the scene graph.  M_cull_clockwise will be
        treated as M_cull_counter_clockwise, and vice-versa.  M_cull_none is
        unchanged.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_actual_mode(self) -> _CullFaceAttrib_Mode:
        """Returns the actual culling mode, without considering the effects of the
        reverse flag.  See also get_effective_mode().
        """
    def get_reverse(self) -> bool:
        """Returns the 'reverse' flag.  If this is true, the actual cull direction
        (clockwise vs.  counterclockwise) is the reverse of what is specified here.
        This allows support for make_reverse(), which defines a CullFaceAttrib that
        reverses whatever the sense of culling would have been.
        """
    def get_effective_mode(self) -> _CullFaceAttrib_Mode:
        """Returns the effective culling mode.  This is the same as the actual culling
        mode, unless the reverse flag is set, which swaps CW for CCW and vice-
        versa.  Also, M_cull_unchanged is mapped to M_cull_none.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeReverse = make_reverse
    makeDefault = make_default
    getActualMode = get_actual_mode
    getReverse = get_reverse
    getEffectiveMode = get_effective_mode
    getClassSlot = get_class_slot

class WorkingNodePath:
    """This is a class designed to support low-overhead traversals of the complete
    scene graph, with a memory of the complete path through the graph at any
    given point.

    You could just use a regular NodePath to do this, but since the NodePath
    requires storing NodePathComponents on each node as it is constructed, and
    then removing them when it destructs, there is considerable overhead in
    that approach.

    The WorkingNodePath eliminates this overhead (but does not guarantee
    consistency if the scene graph changes while the path is held).

    At any given point, you may ask the WorkingNodePath for its actual
    NodePath, and it will construct and return a new NodePath representing the
    complete generated chain.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def valid(self) -> bool: ...
    @property
    def node_path(self) -> NodePath: ...

class CullTraverserData:
    """This collects together the pieces of data that are accumulated for each
    node while walking the scene graph during the cull traversal.

    Having this as a separate object simplifies the parameter list to
    CullTraverser::r_traverse(), as well as to other functions like
    PandaNode::cull_callback().  It also makes it easier to add cull
    parameters, and provides a place to abstract out some of the cull behavior
    (like view-frustum culling).
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def node_path(self) -> NodePath: ...
    def __init__(self, __param0: CullTraverserData) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def node(self) -> PandaNode:
        """Returns the node traversed to so far."""
    def get_modelview_transform(self, trav: CullTraverser) -> TransformState:
        """Returns the modelview transform: the relative transform from the camera to
        the model.
        """
    def get_internal_transform(self, trav: CullTraverser) -> TransformState:
        """Returns the internal transform: the modelview transform in the GSG's
        internal coordinate system.
        """
    def get_net_transform(self, trav: CullTraverser) -> TransformState:
        """Returns the net transform: the relative transform from root of the scene
        graph to the current node.
        """
    def is_in_view(self, camera_mask: DrawMask | int) -> bool:
        """Returns true if the current node is within the view frustum, false
        otherwise.  If the node's bounding volume falls completely within the view
        frustum, this will also reset the view frustum pointer, saving some work
        for future nodes.
        """
    def is_this_node_hidden(self, camera_mask: DrawMask | int) -> bool:
        """Returns true if this particular node is hidden, even though we might be
        traversing past this node to find a child node that has had show_through()
        called for it.  If this returns true, the node should not be rendered.
        """
    def apply_transform_and_state(self, trav: CullTraverser) -> None:
        """Applies the transform and state from the current node onto the current
        data.  This also evaluates billboards, etc.
        """
    def apply_transform(self, node_transform: TransformState) -> None:
        """Applies the indicated transform changes onto the current data."""
    getModelviewTransform = get_modelview_transform
    getInternalTransform = get_internal_transform
    getNetTransform = get_net_transform
    isInView = is_in_view
    isThisNodeHidden = is_this_node_hidden
    applyTransformAndState = apply_transform_and_state
    applyTransform = apply_transform

class SceneSetup(TypedReferenceCount):
    """This object holds the camera position, etc., and other general setup
    information for rendering a particular scene.
    """

    def __init__(self, __param0: SceneSetup) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_display_region(self, display_region: DisplayRegion) -> None:
        """Specifies the display region for the scene."""
    def get_display_region(self) -> DisplayRegion:
        """Returns the display region for the scene."""
    def set_viewport_size(self, width: int, height: int) -> None:
        """Specifies the size of the viewport (display region), in pixels."""
    def get_viewport_width(self) -> int:
        """Returns the width of the viewport (display region) in pixels."""
    def get_viewport_height(self) -> int:
        """Returns the height of the viewport (display region) in pixels."""
    def set_scene_root(self, scene_root: NodePath) -> None:
        """Specifies the root node of the scene."""
    def get_scene_root(self) -> NodePath:
        """Returns the root node of the scene."""
    def set_camera_path(self, camera_path: NodePath) -> None:
        """Specifies the NodePath to the camera."""
    def get_camera_path(self) -> NodePath:
        """Returns the NodePath to the camera."""
    def set_camera_node(self, camera_node: Camera) -> None:
        """Specifies the camera used to render the scene."""
    def get_camera_node(self) -> Camera:
        """Returns the camera used to render the scene."""
    def set_lens(self, lens: Lens) -> None:
        """Indicates the particular Lens used for rendering."""
    def get_lens(self) -> Lens:
        """Returns the particular Lens used for rendering."""
    def set_inverted(self, inverted: bool) -> None:
        """Changes the current setting of the inverted flag.  When this is true, the
        scene is rendered into the window upside-down and backwards, that is,
        inverted as if viewed through a mirror placed on the floor.
        """
    def get_inverted(self) -> bool:
        """Returns the current setting of the inverted flag.  When this is true, the
        scene is rendered into the window upside-down, flipped like a mirror along
        the X axis.
        """
    def get_cull_center(self) -> NodePath:
        """Returns the point from which the culling operations will be performed.
        This is normally the camera, but if camera->set_cull_center() has been
        specified, it will be that special node instead.
        """
    def get_cull_bounds(self) -> BoundingVolume:
        """Returns the bounding volume that should be used to perform view-frustum
        culling (in the space of get_cull_center()).  This is normally the current
        lens' bounding volume, but it may be overridden with
        Camera::set_cull_bounds().
        """
    def set_initial_state(self, initial_state: RenderState) -> None:
        """Sets the initial state which is applied to all nodes in the scene, as if it
        were set at the top of the scene graph.
        """
    def get_initial_state(self) -> RenderState:
        """Returns the initial state as set by a previous call to set_initial_state()."""
    def set_camera_transform(self, camera_transform: TransformState) -> None:
        """Specifies the position of the camera relative to the starting node."""
    def get_camera_transform(self) -> TransformState:
        """Returns the position of the camera relative to the starting node."""
    def set_world_transform(self, world_transform: TransformState) -> None:
        """Specifies the position of the starting node relative to the camera.  This
        is the inverse of the camera transform.
        """
    def get_world_transform(self) -> TransformState:
        """Returns the position of the starting node relative to the camera.  This is
        the inverse of the camera transform.
        """
    def set_cs_transform(self, cs_transform: TransformState) -> None:
        """Specifies the transform from the camera's coordinate system to the GSG's
        internal coordinate system.
        """
    def get_cs_transform(self) -> TransformState:
        """Returns the transform from the camera's coordinate system to the GSG's
        internal coordinate system.
        """
    def set_cs_world_transform(self, cs_world_transform: TransformState) -> None:
        """Specifies the position from the starting node relative to the camera, in
        the GSG's internal coordinate system.
        """
    def get_cs_world_transform(self) -> TransformState:
        """Returns the position from the starting node relative to the camera, in the
        GSG's internal coordinate system.
        """
    setDisplayRegion = set_display_region
    getDisplayRegion = get_display_region
    setViewportSize = set_viewport_size
    getViewportWidth = get_viewport_width
    getViewportHeight = get_viewport_height
    setSceneRoot = set_scene_root
    getSceneRoot = get_scene_root
    setCameraPath = set_camera_path
    getCameraPath = get_camera_path
    setCameraNode = set_camera_node
    getCameraNode = get_camera_node
    setLens = set_lens
    getLens = get_lens
    setInverted = set_inverted
    getInverted = get_inverted
    getCullCenter = get_cull_center
    getCullBounds = get_cull_bounds
    setInitialState = set_initial_state
    getInitialState = get_initial_state
    setCameraTransform = set_camera_transform
    getCameraTransform = get_camera_transform
    setWorldTransform = set_world_transform
    getWorldTransform = get_world_transform
    setCsTransform = set_cs_transform
    getCsTransform = get_cs_transform
    setCsWorldTransform = set_cs_world_transform
    getCsWorldTransform = get_cs_world_transform

class Fog(PandaNode):
    """Specifies how atmospheric fog effects are applied to geometry.  The Fog
    object is now a PandaNode, which means it can be used similarly to a Light
    to define effects relative to a particular coordinate system within the
    scene graph.

    In exponential mode, the fog effects are always camera-relative, and it
    does not matter where the Fog node is parented.  However, in linear mode,
    the onset and opaque distances are defined as offsets along the local
    forward axis (e.g.  the Y axis).  This allows the fog effect to be
    localized to a particular region in space, rather than always camera-
    relative.  If the fog object is not parented to any node, it is used to
    generate traditonal camera-relative fog, as if it were parented to the
    camera.
    """

    M_linear: Final = 0
    MLinear: Final = 0
    M_exponential: Final = 1
    MExponential: Final = 1
    M_exponential_squared: Final = 2
    MExponentialSquared: Final = 2
    mode: _Fog_Mode
    color: LColor
    linear_onset_point: LPoint3
    linear_opaque_point: LPoint3
    exp_density: float
    def get_mode(self) -> _Fog_Mode: ...
    def set_mode(self, mode: _Fog_Mode) -> None:
        """Specifies the computation that is used to determine the fog effect.  If
        this is M_linear, then the fog will range from linearly from the onset
        point to the opaque point (or for the distances specified in
        set_linear_range), and the fog object should be parented into the scene
        graph, or to the camera.

        If this is anything else, the onset point and opaque point are not used,
        and the fog effect is based on the value specified to set_exp_density(),
        and it doesn't matter to which node the fog object is parented, or if it is
        parented anywhere at all.
        """
    def get_color(self) -> LColor:
        """Returns the color of the fog."""
    @overload
    def set_color(self, color: Vec4Like) -> None:
        """`(self, color: LColor)`:
        Sets the color of the fog.  The alpha component is not used.

        `(self, r: float, g: float, b: float)`:
        Sets the color of the fog.
        """
    @overload
    def set_color(self, r: float, g: float, b: float) -> None: ...
    def set_linear_range(self, onset: float, opaque: float) -> None:
        """Specifies the effects of the fog in linear distance units.  This is only
        used if the mode is M_linear.

        This specifies a fog that begins at distance onset units from the origin,
        and becomes totally opaque at distance opaque units from the origin, along
        the forward axis (usually Y).

        This function also implicitly sets the mode the M_linear, if it is not
        already set.
        """
    def get_linear_onset_point(self) -> LPoint3:
        """Returns the point in space at which the fog begins.  This is only used if
        the mode is M_linear.
        """
    @overload
    def set_linear_onset_point(self, linear_onset_point: Vec3Like) -> None:
        """Specifies the point in space at which the fog begins.  This is only used if
        the mode is M_linear.
        """
    @overload
    def set_linear_onset_point(self, x: float, y: float, z: float) -> None: ...
    def get_linear_opaque_point(self) -> LPoint3:
        """Returns the point in space at which the fog completely obscures geometry.
        This is only used if the mode is M_linear.
        """
    @overload
    def set_linear_opaque_point(self, linear_opaque_point: Vec3Like) -> None:
        """Specifies the point in space at which the fog completely obscures geometry.
        This is only used if the mode is M_linear.
        """
    @overload
    def set_linear_opaque_point(self, x: float, y: float, z: float) -> None: ...
    def set_linear_fallback(self, angle: float, onset: float, opaque: float) -> None:
        """Fog effects are traditionally defined in camera-relative space, but the
        Panda Fog node has a special mode in which it can define a linear fog
        effect in an arbitrary coordinate space.

        This is done by specifying 3-d onset and opaque points, and parenting the
        Fog object somewhere within the scene graph.  In this mode, the fog will be
        rendered as if it extended along the vector from the onset point to the
        opaque point, in 3-d space.

        However, the underlying fog effect supported by hardware is generally only
        one-dimensional, and must be rendered based on linear distance from the
        camera plane.  Thus, this in-the-world effect is most effective when the
        fog vector from onset point to opaque point is most nearly parallel to the
        camera's eye vector.

        As the angle between the fog vector and the eye vector increases, the
        accuracy of the effect diminishes, up to a complete breakdown of the effect
        at a 90 degree angle.

        This function exists to define the workaround to this problem.  The linear
        fallback parameters given here specify how the fog should be rendered when
        the parameters are exceeded in this way.

        The angle parameter is the minimum angle, in degrees, of the fog vector to
        the eye vector, at which the fallback effect should be employed.  The onset
        and opaque parameters specify the camera-relative onset and opaque
        distances to pass to the rendering hardware when employing the fallback
        effect.  This supercedes the 3-d onset point and opaque points.
        """
    def get_exp_density(self) -> float:
        """Returns the density of the fog for exponential calculations.  This is only
        used if the mode is not M_linear.
        """
    def set_exp_density(self, exp_density: float) -> None:
        """Sets the density of the fog for exponential calculations.  This is only
        used if the mode is not M_linear.

        If the mode is currently set to M_linear, this function implicitly sets it
        to M_exponential.
        """
    getMode = get_mode
    setMode = set_mode
    getColor = get_color
    setColor = set_color
    setLinearRange = set_linear_range
    getLinearOnsetPoint = get_linear_onset_point
    setLinearOnsetPoint = set_linear_onset_point
    getLinearOpaquePoint = get_linear_opaque_point
    setLinearOpaquePoint = set_linear_opaque_point
    setLinearFallback = set_linear_fallback
    getExpDensity = get_exp_density
    setExpDensity = set_exp_density

class FogAttrib(RenderAttrib):
    """Applies a Fog to the geometry at and below this node."""

    @property
    def fog(self) -> Fog: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(fog: Fog) -> RenderAttrib:
        """Constructs a new FogAttrib object suitable for rendering the indicated fog
        onto geometry.
        """
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new FogAttrib object suitable for rendering unfogd geometry."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def is_off(self) -> bool:
        """Returns true if the FogAttrib is an 'off' FogAttrib, indicating that it
        should disable fog.
        """
    def get_fog(self) -> Fog:
        """If the FogAttrib is not an 'off' FogAttrib, returns the fog that is
        associated.  Otherwise, return NULL.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    isOff = is_off
    getFog = get_fog
    getClassSlot = get_class_slot

class CullTraverser(TypedReferenceCount):
    """This object performs a depth-first traversal of the scene graph, with
    optional view-frustum culling, collecting CullState and searching for
    GeomNodes.  Each renderable Geom encountered is passed along with its
    associated RenderState to the CullHandler object.
    """

    def __init__(self, copy: CullTraverser = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_gsg(self) -> GraphicsStateGuardianBase:
        """Returns the GraphicsStateGuardian in effect."""
    def get_current_thread(self) -> Thread:
        """Returns the currently-executing thread object, as passed to the
        CullTraverser constructor.
        """
    def set_scene(self, scene_setup: SceneSetup, gsg: GraphicsStateGuardianBase, dr_incomplete_render: bool) -> None:
        """Sets the SceneSetup object that indicates the initial camera position, etc.
        This must be called before traversal begins.
        """
    def get_scene(self) -> SceneSetup:
        """Returns the SceneSetup object."""
    def has_tag_state_key(self) -> bool:
        """Returns true if a nonempty tag state key has been specified for the scene's
        camera, false otherwise.
        """
    def get_tag_state_key(self) -> str:
        """Returns the tag state key that has been specified for the scene's camera,
        if any.
        """
    def set_camera_mask(self, camera_mask: DrawMask | int) -> None:
        """Changes the visibility mask for the camera viewing the scene.  This is
        normally set automatically at the time setup_scene() is called; you should
        change this only if you want to render some set of objects different from
        what the camera normally would draw.
        """
    def get_camera_mask(self) -> DrawMask:
        """Returns the visibility mask from the camera viewing the scene."""
    def get_camera_transform(self) -> TransformState:
        """Returns the position of the camera relative to the starting node."""
    def get_world_transform(self) -> TransformState:
        """Returns the position of the starting node relative to the camera.  This is
        the inverse of the camera transform.

        Note that this value is always the position of the starting node, not the
        current node, even if it is sampled during a traversal.  To get the
        transform of the current node use
        CullTraverserData::get_modelview_transform().
        """
    def get_initial_state(self) -> RenderState:
        """Returns the initial RenderState at the top of the scene graph we are
        traversing, or the empty state if the initial state was never set.
        """
    def get_depth_offset_decals(self) -> bool:
        """Returns true, as depth offsets are the only way that we implement decals
        nowadays.
        """
    def set_view_frustum(self, view_frustum: GeometricBoundingVolume) -> None:
        """Specifies the bounding volume that corresponds to the view frustum.  Any
        primitives that fall entirely outside of this volume are not drawn.
        """
    def get_view_frustum(self) -> GeometricBoundingVolume:
        """Returns the bounding volume that corresponds to the view frustum, or NULL
        if the view frustum is not in use or has not been set.

        Note that the view frustum returned here is always in the coordinate space
        of the starting node, not the current node, even if it is sampled during a
        traversal.  To get the view frustum in the current node's coordinate space,
        check in the current CullTraverserData.
        """
    def get_effective_incomplete_render(self) -> bool:
        """Returns true if the cull traversal is effectively in incomplete_render
        state, considering both the GSG's incomplete_render and the current
        DisplayRegion's incomplete_render flags.  This returns the flag during the
        cull traversal; see GSG::get_effective_incomplete_render() for this same
        flag during the draw traversal.
        """
    @overload
    def traverse(self, data: CullTraverserData) -> None:
        """`(self, data: CullTraverserData)`:
        Traverses from the next node with the given data, which has been
        constructed with the node but has not yet been converted into the node's
        space.

        `(self, root: NodePath)`:
        Begins the traversal from the indicated node.
        """
    @overload
    def traverse(self, root: NodePath) -> None: ...
    def traverse_below(self, data: CullTraverserData) -> None:
        """Traverses all the children of the indicated node, with the given data,
        which has been converted into the node's space.
        """
    def end_traverse(self) -> None:
        """Should be called when the traverser has finished traversing its scene, this
        gives it a chance to do any necessary finalization.
        """
    @staticmethod
    def flush_level() -> None:
        """Flushes the PStatCollectors used during traversal."""
    def draw_bounding_volume(self, vol: BoundingVolume, internal_transform: TransformState) -> None:
        """Draws an appropriate visualization of the indicated bounding volume."""
    getGsg = get_gsg
    getCurrentThread = get_current_thread
    setScene = set_scene
    getScene = get_scene
    hasTagStateKey = has_tag_state_key
    getTagStateKey = get_tag_state_key
    setCameraMask = set_camera_mask
    getCameraMask = get_camera_mask
    getCameraTransform = get_camera_transform
    getWorldTransform = get_world_transform
    getInitialState = get_initial_state
    getDepthOffsetDecals = get_depth_offset_decals
    setViewFrustum = set_view_frustum
    getViewFrustum = get_view_frustum
    getEffectiveIncompleteRender = get_effective_incomplete_render
    traverseBelow = traverse_below
    endTraverse = end_traverse
    flushLevel = flush_level
    drawBoundingVolume = draw_bounding_volume

class GeomDrawCallbackData(CallbackData):
    """This specialization on CallbackData is passed when the callback is
    initiated from deep within the draw traversal, for a particular Geom.
    """

    def get_gsg(self) -> GraphicsStateGuardianBase:
        """Returns a pointer to the current GSG."""
    def get_force(self) -> bool:
        """Returns true if any required data should be forced into memory if necessary
        to render the object, or false if the object should be omitted if some of
        the data is not available (at least until the data becomes available
        later).
        """
    def set_lost_state(self, lost_state: bool) -> None:
        """Sets the lost_state flag.  If this is true, the callback does not have to
        be quite so careful to clean up after itself; Panda will assume that the
        graphics state is in an unknown state after the callback has finished, and
        will issue all the necessary calls to restore it.  If this is false, Panda
        will assume the callback will leave the graphics state exactly as it came
        in, and won't bother to try to restore it.  The default is true.
        """
    def get_lost_state(self) -> bool:
        """Returns the lost_state flag.  See set_lost_state()."""
    getGsg = get_gsg
    getForce = get_force
    setLostState = set_lost_state
    getLostState = get_lost_state

class RescaleNormalAttrib(RenderAttrib):
    """Specifies how polygons are to be drawn."""

    M_rescale: Final = 1
    MRescale: Final = 1
    M_normalize: Final = 2
    MNormalize: Final = 2
    M_auto: Final = 3
    MAuto: Final = 3
    @property
    def mode(self) -> _RescaleNormalAttrib_Mode: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _RescaleNormalAttrib_Mode) -> RenderAttrib:
        """Constructs a new RescaleNormalAttrib object that specifies whether to
        rescale normals to compensate for transform scales or incorrectly defined
        normals.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Constructs a RescaleNormalAttrib object that's suitable for putting at the
        top of a scene graph.  This will contain whatever attrib was suggested by
        the user's rescale-normals Config variable.
        """
    def get_mode(self) -> _RescaleNormalAttrib_Mode:
        """Returns the render mode."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getClassSlot = get_class_slot

class CullResult(ReferenceCount):
    """This stores the result of a BinCullHandler traversal: an ordered collection
    of CullBins, each of which holds a number of Geoms and RenderStates to be
    rendered in some defined order.

    This is also used to keep the results of last frame's cull traversal around
    to make next frame's traversal of the same scene a little easier.
    """

    def __init__(self, __param0: CullResult) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def make_next(self) -> CullResult:
        """Returns a newly-allocated CullResult object that contains a copy of just
        the subset of the data from this CullResult object that is worth keeping
        around for next frame.
        """
    def finish_cull(self, scene_setup: SceneSetup, current_thread: Thread) -> None:
        """Called after all the geoms have been added, this indicates that the cull
        process is finished for this frame and gives the bins a chance to do any
        post-processing (like sorting) before moving on to draw.
        """
    def draw(self, current_thread: Thread) -> None:
        """Asks all the bins to draw themselves in the correct order."""
    def make_result_graph(self) -> PandaNode:
        """Returns a special scene graph constructed to represent the results of the
        cull.  This will be a hierarchy of nodes, one node for each bin, each of
        which will in term be a parent of a number of GeomNodes, representing the
        geometry drawn in each bin.

        This is useful mainly for high-level debugging and abstraction tools; it
        should not be mistaken for the low-level cull result itself.  For the low-
        level cull result, use draw() to efficiently draw the culled scene.
        """
    makeNext = make_next
    finishCull = finish_cull
    makeResultGraph = make_result_graph

class DecalEffect(RenderEffect):
    """Applied to a GeomNode to indicate that the children of this GeomNode are
    coplanar and should be drawn as decals (eliminating Z-fighting).
    """

    @staticmethod
    def make() -> RenderEffect:
        """Constructs a new DecalEffect object."""

class DepthOffsetAttrib(RenderAttrib):
    """This is a special kind of attribute that instructs the graphics driver to
    apply an offset or bias to the generated depth values for rendered
    polygons, before they are written to the depth buffer.

    This can be used to shift polygons forward slightly, to resolve depth
    conflicts.  The cull traverser may optionally use this, for instance, to
    implement decals.  However, driver support for this feature seems to be
    spotty, so use with caution.

    The bias is always an integer number, and each integer increment represents
    the smallest possible increment in Z that is sufficient to completely
    resolve two coplanar polygons.  Positive numbers are closer towards the
    camera.

    Nested DepthOffsetAttrib values accumulate; that is, a DepthOffsetAttrib
    with a value of 1 beneath another DepthOffsetAttrib with a value of 2
    presents a net offset of 3.  (A DepthOffsetAttrib will not, however,
    combine with any other DepthOffsetAttribs with a lower override parameter.)
    The net value should probably not exceed 16 or drop below 0 for maximum
    portability.

    Also, and only tangentially related, the DepthOffsetAttrib can be used to
    constrain the Z output value to a subset of the usual [0, 1] range (or
    reversing its direction) by specifying a new min_value and max_value.
    """

    @property
    def offset(self) -> int: ...
    @property
    def min_value(self) -> float: ...
    @property
    def max_value(self) -> float: ...
    @property
    def class_slot(self) -> int: ...
    @overload
    @staticmethod
    def make(offset: int = ...) -> RenderAttrib:
        """`(offset: int = ...)`:
        Constructs a new DepthOffsetAttrib object that indicates the relative
        amount of bias to write to the depth buffer for subsequent geometry.

        `(offset: int, min_value: float, max_value: float)`:
        Constructs a new DepthOffsetAttrib object that indicates the bias, and also
        specifies a minimum and maximum (or, more precisely, nearest and farthest)
        values to write to the depth buffer, in the range 0 .. 1.  This range is 0,
        1 by default; setting it to some other range can be used to create
        additional depth buffer effects.
        """
    @overload
    @staticmethod
    def make(offset: int, min_value: float, max_value: float) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_offset(self) -> int:
        """Returns the depth offset represented by this attrib."""
    def get_min_value(self) -> float:
        """Returns the value for the minimum (closest) depth value to be stored in the
        buffer, in the range 0 .. 1.
        """
    def get_max_value(self) -> float:
        """Returns the value for the maximum (farthest) depth value to be stored in
        the buffer, in the range 0 .. 1.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getOffset = get_offset
    getMinValue = get_min_value
    getMaxValue = get_max_value
    getClassSlot = get_class_slot

class DepthTestAttrib(RenderAttrib):
    """Enables or disables writing to the depth buffer."""

    @property
    def mode(self) -> _RenderAttrib_PandaCompareFunc: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _RenderAttrib_PandaCompareFunc) -> RenderAttrib:
        """Constructs a new DepthTestAttrib object."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> _RenderAttrib_PandaCompareFunc:
        """Returns the depth write mode."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getClassSlot = get_class_slot

class DepthWriteAttrib(RenderAttrib):
    """Enables or disables writing to the depth buffer."""

    M_on: Final = 1
    MOn: Final = 1
    @property
    def mode(self) -> _DepthWriteAttrib_Mode: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _DepthWriteAttrib_Mode) -> RenderAttrib:
        """Constructs a new DepthWriteAttrib object."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> _DepthWriteAttrib_Mode:
        """Returns the depth write mode."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getClassSlot = get_class_slot

class Light:
    """The abstract interface to all kinds of lights.  The actual light objects
    also inherit from PandaNode, and can therefore be added to the scene graph
    at some arbitrary point to define the coordinate system of effect.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    color: LColor
    color_temperature: float
    priority: int
    def as_node(self) -> PandaNode: ...
    def is_ambient_light(self) -> bool:
        """Returns true if this is an AmbientLight, false if it is some other kind of
        light.
        """
    def get_color(self) -> LColor:
        """Returns the basic color of the light."""
    def set_color(self, color: Vec4Like) -> None:
        """Sets the basic color of the light."""
    def has_color_temperature(self) -> bool:
        """Returns true if the color was specified as a temperature in kelvins, and
        get_color_temperature is defined.

        @since 1.10.0
        """
    def get_color_temperature(self) -> float:
        """Returns the basic color temperature of the light, assuming
        has_color_temperature() returns true.

        @since 1.10.0
        """
    def set_color_temperature(self, temperature: float) -> None:
        """Sets the color temperature of the light in kelvins.  This will recalculate
        the light's color.

        The default value is 6500 K, corresponding to a perfectly white light
        assuming a D65 white point.

        @since 1.10.0
        """
    def get_exponent(self) -> float:
        """For spotlights, returns the exponent that controls the amount of light
        falloff from the center of the spotlight.  For other kinds of lights,
        returns 0.
        """
    def get_specular_color(self) -> LColor:
        """Returns the color of specular highlights generated by the light.  This
        value is meaningless for ambient lights.
        """
    def get_attenuation(self) -> LVecBase3:
        """Returns the terms of the attenuation equation for the light.  These are, in
        order, the constant, linear, and quadratic terms based on the distance from
        the point to the vertex.
        """
    def set_priority(self, priority: int) -> None:
        """Changes the relative importance of this light relative to the other lights
        that are applied simultaneously.

        The priority number is used to decide which of the requested lights are to
        be selected for rendering when more lights are requested than the hardware
        will support.  The highest-priority n lights are selected for rendering.

        This is similar to TextureStage::set_priority().
        """
    def get_priority(self) -> int:
        """Returns the priority associated with this light.  See set_priority()."""
    def get_class_priority(self) -> int: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    asNode = as_node
    isAmbientLight = is_ambient_light
    getColor = get_color
    setColor = set_color
    hasColorTemperature = has_color_temperature
    getColorTemperature = get_color_temperature
    setColorTemperature = set_color_temperature
    getExponent = get_exponent
    getSpecularColor = get_specular_color
    getAttenuation = get_attenuation
    setPriority = set_priority
    getPriority = get_priority
    getClassPriority = get_class_priority
    getClassType = get_class_type

class LightAttrib(RenderAttrib):
    """Indicates which set of lights should be considered "on" to illuminate
    geometry at this level and below.  A LightAttrib can either add lights or
    remove lights from the total set of "on" lights.
    """

    O_set: Final = 0
    OSet: Final = 0
    O_add: Final = 1
    OAdd: Final = 1
    O_remove: Final = 2
    ORemove: Final = 2
    @property
    def on_lights(self) -> Sequence[NodePath]: ...
    @property
    def off_lights(self) -> Sequence[NodePath]: ...
    @property
    def class_slot(self) -> int: ...
    @overload
    @staticmethod
    def make() -> RenderAttrib:
        """`()`:
        The following is the new, more general interface to the LightAttrib.

        `(op: _LightAttrib_Operation, light: Light)`:
        Constructs a new LightAttrib object that turns on (or off, according to op)
        the indicated light(s).

        @deprecated Use add_on_light() or add_off_light() instead.

        `(op: _LightAttrib_Operation, light1: Light, light2: Light)`; `(op: _LightAttrib_Operation, light1: Light, light2: Light, light3: Light)`; `(op: _LightAttrib_Operation, light1: Light, light2: Light, light3: Light, light4: Light)`:
        Constructs a new LightAttrib object that turns on (or off, according to op)
        the indicate light(s).

        @deprecated Use add_on_light() or add_off_light() instead.
        """
    @overload
    @staticmethod
    def make(op: _LightAttrib_Operation, light: Light) -> RenderAttrib: ...
    @overload
    @staticmethod
    def make(op: _LightAttrib_Operation, light1: Light, light2: Light, light3: Light = ...) -> RenderAttrib: ...
    @overload
    @staticmethod
    def make(op: _LightAttrib_Operation, light1: Light, light2: Light, light3: Light, light4: Light) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_operation(self) -> _LightAttrib_Operation:
        """Returns the basic operation type of the LightAttrib.  If this is O_set, the
        lights listed here completely replace any lights that were already on.  If
        this is O_add, the lights here are added to the set of lights that were
        already on, and if O_remove, the lights here are removed from the set of
        lights that were on.

        @deprecated LightAttribs nowadays have a separate list of on_lights and
        off_lights, so this method no longer makes sense.  Query the lists
        independently.
        """
    def get_num_lights(self) -> int:
        """Returns the number of lights listed in the attribute.

        @deprecated LightAttribs nowadays have a separate list of on_lights and
        off_lights, so this method no longer makes sense.  Query the lists
        independently.
        """
    def get_light(self, n: int) -> Light:
        """Returns the nth light listed in the attribute.

        @deprecated LightAttribs nowadays have a separate list of on_lights and
        off_lights, so this method no longer makes sense.  Query the lists
        independently.
        """
    def has_light(self, light: Light) -> bool:
        """Returns true if the indicated light is listed in the attrib, false
        otherwise.

        @deprecated LightAttribs nowadays have a separate list of on_lights and
        off_lights, so this method no longer makes sense.  Query the lists
        independently.
        """
    def add_light(self, light: Light) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        added to the list of lights.

        @deprecated Use add_on_light() or add_off_light() instead.
        """
    def remove_light(self, light: Light) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        removed from the list of lights.

        @deprecated Use remove_on_light() or remove_off_light() instead.
        """
    @staticmethod
    def make_all_off() -> RenderAttrib:
        """Constructs a new LightAttrib object that turns off all lights (and hence
        disables lighting).
        """
    def get_num_on_lights(self) -> int:
        """Returns the number of lights that are turned on by the attribute."""
    def get_num_non_ambient_lights(self) -> int:
        """Returns the number of non-ambient lights that are turned on by this
        attribute.
        """
    def get_on_light(self, n: int) -> NodePath:
        """Returns the nth light turned on by the attribute, sorted in render order."""
    def has_on_light(self, light: NodePath) -> bool:
        """Returns true if the indicated light is turned on by the attrib, false
        otherwise.
        """
    def has_any_on_light(self) -> bool:
        """Returns true if any light is turned on by the attrib, false otherwise."""
    def get_num_off_lights(self) -> int:
        """Returns the number of lights that are turned off by the attribute."""
    def get_off_light(self, n: int) -> NodePath:
        """Returns the nth light turned off by the attribute, sorted in arbitrary
        (pointer) order.
        """
    def has_off_light(self, light: NodePath) -> bool:
        """Returns true if the indicated light is turned off by the attrib, false
        otherwise.
        """
    def has_all_off(self) -> bool:
        """Returns true if this attrib turns off all lights (although it may also turn
        some on).
        """
    def is_identity(self) -> bool:
        """Returns true if this is an identity attrib: it does not change the set of
        lights in use.
        """
    def add_on_light(self, light: NodePath) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        added to the list of lights turned on by this attrib.
        """
    def remove_on_light(self, light: NodePath) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        removed from the list of lights turned on by this attrib.
        """
    def replace_on_light(self, source: NodePath, dest: NodePath) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        replaced with the given other light.
        """
    def add_off_light(self, light: NodePath) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        added to the list of lights turned off by this attrib.
        """
    def remove_off_light(self, light: NodePath) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        removed from the list of lights turned off by this attrib.
        """
    def replace_off_light(self, source: NodePath, dest: NodePath) -> RenderAttrib:
        """Returns a new LightAttrib, just like this one, but with the indicated light
        replaced with the given other light.
        """
    def get_most_important_light(self) -> NodePath:
        """Returns the most important light (that is, the light with the highest
        priority) in the LightAttrib, excluding any ambient lights.  Returns an
        empty NodePath if no non-ambient lights are found.
        """
    def get_ambient_contribution(self) -> LColor:
        """Returns the total contribution of all the ambient lights."""
    @staticmethod
    def get_class_slot() -> int: ...
    def get_on_lights(self) -> tuple[NodePath, ...]: ...
    def get_off_lights(self) -> tuple[NodePath, ...]: ...
    makeDefault = make_default
    getOperation = get_operation
    getNumLights = get_num_lights
    getLight = get_light
    hasLight = has_light
    addLight = add_light
    removeLight = remove_light
    makeAllOff = make_all_off
    getNumOnLights = get_num_on_lights
    getNumNonAmbientLights = get_num_non_ambient_lights
    getOnLight = get_on_light
    hasOnLight = has_on_light
    hasAnyOnLight = has_any_on_light
    getNumOffLights = get_num_off_lights
    getOffLight = get_off_light
    hasOffLight = has_off_light
    hasAllOff = has_all_off
    isIdentity = is_identity
    addOnLight = add_on_light
    removeOnLight = remove_on_light
    replaceOnLight = replace_on_light
    addOffLight = add_off_light
    removeOffLight = remove_off_light
    replaceOffLight = replace_off_light
    getMostImportantLight = get_most_important_light
    getAmbientContribution = get_ambient_contribution
    getClassSlot = get_class_slot
    getOnLights = get_on_lights
    getOffLights = get_off_lights

class LightRampAttrib(RenderAttrib):
    """A Light Ramp is any unary operator that takes a rendered pixel as input,
    and adjusts the brightness of that pixel.  For example, gamma correction is
    a kind of light ramp.  So is HDR tone mapping.  So is cartoon shading.  See
    the constructors for an explanation of each kind of ramp.
    """

    LRT_default: Final = 0
    LRTDefault: Final = 0
    LRT_identity: Final = 1
    LRTIdentity: Final = 1
    LRT_single_threshold: Final = 2
    LRTSingleThreshold: Final = 2
    LRT_double_threshold: Final = 3
    LRTDoubleThreshold: Final = 3
    LRT_hdr0: Final = 4
    LRTHdr0: Final = 4
    LRT_hdr1: Final = 5
    LRTHdr1: Final = 5
    LRT_hdr2: Final = 6
    LRTHdr2: Final = 6
    @property
    def mode(self) -> _LightRampAttrib_LightRampMode: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This is the standard OpenGL
        lighting ramp, which clamps the final light total to the 0-1 range.
        """
    @staticmethod
    def make_identity() -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This differs from the usual
        OpenGL lighting model in that it does not clamp the final lighting total to
        (0,1).
        """
    @staticmethod
    def make_single_threshold(thresh0: float, lev0: float) -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This causes the luminance of the
        diffuse lighting contribution to be quantized using a single threshold:

        @code
        if (original_luminance > threshold0) {
          luminance = level0;
        } else {
          luminance = 0.0;
        }
        @endcode
        """
    @staticmethod
    def make_double_threshold(thresh0: float, lev0: float, thresh1: float, lev1: float) -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This causes the luminance of the
        diffuse lighting contribution to be quantized using two thresholds:

        @code
        if (original_luminance > threshold1) {
          luminance = level1;
        } else if (original_luminance > threshold0) {
          luminance = level0;
        } else {
          luminance = 0.0;
        }
        @endcode
        """
    @staticmethod
    def make_hdr0() -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
        operation to be applied.

        Normally, brightness values greater than 1 cannot be distinguished from
        each other, causing very brightly lit objects to wash out white and all
        detail to be erased.  HDR tone mapping remaps brightness values in the
        range 0-infinity into the range (0,1), making it possible to distinguish
        detail in scenes whose brightness exceeds 1.

        However, the monitor has finite contrast.  Normally, all of that contrast
        is used to represent brightnesses in the range 0-1.  The HDR0 tone mapping
        operator 'steals' one quarter of that contrast to represent brightnesses in
        the range 1-infinity.

        @code
        FINAL_RGB = (RGB^3 + RGB^2 + RGB) / (RGB^3 + RGB^2 + RGB + 1)
        @endcode
        """
    @staticmethod
    def make_hdr1() -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
        operation to be applied.

        Normally, brightness values greater than 1 cannot be distinguished from
        each other, causing very brightly lit objects to wash out white and all
        detail to be erased.  HDR tone mapping remaps brightness values in the
        range 0-infinity into the range (0,1), making it possible to distinguish
        detail in scenes whose brightness exceeds 1.

        However, the monitor has finite contrast.  Normally, all of that contrast
        is used to represent brightnesses in the range 0-1.  The HDR1 tone mapping
        operator 'steals' one third of that contrast to represent brightnesses in
        the range 1-infinity.

        @code
        FINAL_RGB = (RGB^2 + RGB) / (RGB^2 + RGB + 1)
        @endcode
        """
    @staticmethod
    def make_hdr2() -> RenderAttrib:
        """Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
        operation to be applied.

        Normally, brightness values greater than 1 cannot be distinguished from
        each other, causing very brightly lit objects to wash out white and all
        detail to be erased.  HDR tone mapping remaps brightness values in the
        range 0-infinity into the range (0,1), making it possible to distinguish
        detail in scenes whose brightness exceeds 1.

        However, the monitor has finite contrast.  Normally, all of that contrast
        is used to represent brightnesses in the range 0-1.  The HDR2 tone mapping
        operator 'steals' one half of that contrast to represent brightnesses in
        the range 1-infinity.

        @code
        FINAL_RGB = (RGB) / (RGB + 1)
        @endcode
        """
    def get_mode(self) -> _LightRampAttrib_LightRampMode:
        """Returns the LightRampAttrib mode."""
    def get_level(self, n: int) -> float:
        """Returns the nth lighting level."""
    def get_threshold(self, n: int) -> float:
        """Returns the nth threshold level."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    makeIdentity = make_identity
    makeSingleThreshold = make_single_threshold
    makeDoubleThreshold = make_double_threshold
    makeHdr0 = make_hdr0
    makeHdr1 = make_hdr1
    makeHdr2 = make_hdr2
    getMode = get_mode
    getLevel = get_level
    getThreshold = get_threshold
    getClassSlot = get_class_slot

class Loader(TypedReferenceCount, Namable):
    """A convenient class for loading models from disk, in bam or egg format (or
    any of a number of other formats implemented by a LoaderFileType, such as
    ptloader).

    This class supports synchronous as well as asynchronous loading.  In
    asynchronous loading, the model is loaded in the background by a thread,
    and an event will be generated when the model is available.  If threading
    is not available, the asynchronous loading interface may be used, but it
    loads synchronously.
    """

    class Results:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, copy: Loader.Results = ...) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def assign(self, copy: Loader.Results) -> Self: ...
        def clear(self) -> None:
            """Removes all the files from the list."""
        def get_num_files(self) -> int:
            """Returns the number of files on the result list."""
        def get_file(self, n: int) -> Filename:
            """Returns the nth file on the result list."""
        def get_file_type(self, n: int) -> LoaderFileType:
            """Returns the file type of the nth file on the result list."""
        def get_files(self) -> tuple[Filename, ...]: ...
        def get_file_types(self) -> tuple[LoaderFileType, ...]: ...
        getNumFiles = get_num_files
        getFile = get_file
        getFileType = get_file_type
        getFiles = get_files
        getFileTypes = get_file_types

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: Loader) -> None: ...
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def set_task_manager(self, task_manager: AsyncTaskManager) -> None:
        """Specifies the task manager that is used for asynchronous loads.  The
        default is the global task manager.
        """
    def get_task_manager(self) -> AsyncTaskManager:
        """Returns the task manager that is used for asynchronous loads."""
    def set_task_chain(self, task_chain: str) -> None:
        """Specifies the task chain that is used for asynchronous loads.  The default
        is the initial name of the Loader object.
        """
    def get_task_chain(self) -> str:
        """Returns the task chain that is used for asynchronous loads."""
    def stop_threads(self) -> None:
        """Stop any threads used for asynchronous loads."""
    def remove(self, task: AsyncTask) -> bool:
        """Removes a pending asynchronous load request.  Returns true if successful,
        false otherwise.
        @deprecated use task.cancel() to cancel the request instead.
        """
    def load_sync(self, filename: StrOrBytesPath, options: LoaderOptions = ...) -> PandaNode:
        """Loads the file immediately, waiting for it to complete.

        If search is true, the file is searched for along the model path;
        otherwise, only the exact filename is loaded.
        """
    def make_async_request(self, filename: StrOrBytesPath, options: LoaderOptions = ...) -> AsyncTask:
        """Returns a new AsyncTask object suitable for adding to load_async() to start
        an asynchronous model load.
        """
    def load_async(self, request: AsyncTask) -> None:
        """Begins an asynchronous load request.  To use this call, first call
        make_async_request() to create a new ModelLoadRequest object with the
        filename you wish to load, and then add that object to the Loader with
        load_async.  This function will return immediately, and the model will be
        loaded in the background.

        To determine when the model has completely loaded, you may poll
        request->is_ready() from time to time, or set the done_event on the request
        object and listen for that event.  When the model is ready, you may
        retrieve it via request->get_model().
        """
    def save_sync(self, filename: StrOrBytesPath, options: LoaderOptions, node: PandaNode) -> bool:
        """Saves the file immediately, waiting for it to complete."""
    def make_async_save_request(self, filename: StrOrBytesPath, options: LoaderOptions, node: PandaNode) -> AsyncTask:
        """Returns a new AsyncTask object suitable for adding to save_async() to start
        an asynchronous model save.
        """
    def save_async(self, request: AsyncTask) -> None:
        """Begins an asynchronous save request.  To use this call, first call
        make_async_save_request() to create a new ModelSaveRequest object with the
        filename you wish to load, and then add that object to the Loader with
        save_async.  This function will return immediately, and the model will be
        loaded in the background.

        To determine when the model has completely loaded, you may poll
        request->is_ready() from time to time, or set the done_event on the request
        object and listen for that event.  When the request is ready, you may
        retrieve the success or failure via request->get_success().
        """
    def load_bam_stream(self, _in: istream) -> PandaNode:
        """Attempts to read a bam file from the indicated stream and return the scene
        graph defined there.
        """
    @staticmethod
    def get_global_ptr() -> Loader:
        """Returns a pointer to the global Loader.  This is the Loader that most code
        should use for loading models.
        """
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToNamable = upcast_to_Namable
    setTaskManager = set_task_manager
    getTaskManager = get_task_manager
    setTaskChain = set_task_chain
    getTaskChain = get_task_chain
    stopThreads = stop_threads
    loadSync = load_sync
    makeAsyncRequest = make_async_request
    loadAsync = load_async
    saveSync = save_sync
    makeAsyncSaveRequest = make_async_save_request
    saveAsync = save_async
    loadBamStream = load_bam_stream
    getGlobalPtr = get_global_ptr

class LoaderFileType(TypedObject):
    """This is the base class for a family of scene-graph file types that the
    Loader supports.  Each kind of loader that's available should define a
    corresponding LoaderFileType object and register itself.
    """

    def get_name(self) -> str: ...
    def get_extension(self) -> str: ...
    def get_additional_extensions(self) -> str:
        """Returns a space-separated list of extension, in addition to the one
        returned by get_extension(), that are recognized by this loader.
        """
    def supports_compressed(self) -> bool:
        """Returns true if this file type can transparently load compressed files
        (with a .pz or .gz extension), false otherwise.
        """
    def get_allow_disk_cache(self, options: LoaderOptions) -> bool:
        """Returns true if the loader flags allow retrieving the model from the on-
        disk bam cache (if it is enabled), false otherwise.
        """
    def get_allow_ram_cache(self, options: LoaderOptions) -> bool:
        """Returns true if the loader flags allow retrieving the model from the in-
        memory ModelPool cache, false otherwise.
        """
    def supports_load(self) -> bool:
        """Returns true if the file type can be used to load files, and load_file() is
        supported.  Returns false if load_file() is unimplemented and will always
        fail.
        """
    def supports_save(self) -> bool:
        """Returns true if the file type can be used to save files, and save_file() is
        supported.  Returns false if save_file() is unimplemented and will always
        fail.
        """
    getName = get_name
    getExtension = get_extension
    getAdditionalExtensions = get_additional_extensions
    supportsCompressed = supports_compressed
    getAllowDiskCache = get_allow_disk_cache
    getAllowRamCache = get_allow_ram_cache
    supportsLoad = supports_load
    supportsSave = supports_save

class LoaderFileTypeRegistry:
    """This class maintains the set of all known LoaderFileTypes in the universe."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def types(self) -> Sequence[LoaderFileType]: ...
    def __init__(self, __param0: LoaderFileTypeRegistry) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def register_type(self, type) -> None: ...
    def register_deferred_type(self, entry_point) -> None: ...
    def unregister_type(self, type) -> None: ...
    def get_num_types(self) -> int:
        """Returns the total number of types registered."""
    def get_type(self, n: int) -> LoaderFileType:
        """Returns the nth type registered."""
    def get_type_from_extension(self, extension: str) -> LoaderFileType:
        """Determines the type of the file based on the indicated extension (without a
        leading dot).  Returns NULL if the extension matches no known file types.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a list of supported file types to the indicated output stream, one
        per line.
        """
    @staticmethod
    def get_global_ptr() -> LoaderFileTypeRegistry:
        """Returns a pointer to the global LoaderFileTypeRegistry object."""
    def get_types(self) -> tuple[LoaderFileType, ...]: ...
    registerType = register_type
    registerDeferredType = register_deferred_type
    unregisterType = unregister_type
    getNumTypes = get_num_types
    getType = get_type
    getTypeFromExtension = get_type_from_extension
    getGlobalPtr = get_global_ptr
    getTypes = get_types

class MaterialAttrib(RenderAttrib):
    """Indicates which, if any, material should be applied to geometry.  The
    material is used primarily to control lighting effects, and isn't necessary
    (or useful) in the absence of lighting.
    """

    @property
    def material(self) -> Material: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(material: Material) -> RenderAttrib:
        """Constructs a new MaterialAttrib object suitable for rendering the indicated
        material onto geometry.
        """
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new MaterialAttrib object suitable for rendering unmateriald
        geometry.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def is_off(self) -> bool:
        """Returns true if the MaterialAttrib is an 'off' MaterialAttrib, indicating
        that it should disable the use of materials.
        """
    def get_material(self) -> Material:
        """If the MaterialAttrib is not an 'off' MaterialAttrib, returns the material
        that is associated.  Otherwise, return NULL.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    isOff = is_off
    getMaterial = get_material
    getClassSlot = get_class_slot

class ModelFlattenRequest(AsyncTask):
    """This class object manages a single asynchronous request to flatten a model.
    The model will be duplicated and flattened in a sub-thread (if threading is
    available), without affecting the original model; and when the result is
    done it may be retrieved from this object.
    """

    @property
    def orig(self) -> PandaNode: ...
    @overload
    def __init__(self, __param0: ModelFlattenRequest) -> None:
        """Create a new ModelFlattenRequest, and add it to the loader via
        load_async(), to begin an asynchronous load.
        """
    @overload
    def __init__(self, orig: PandaNode) -> None: ...
    def get_orig(self) -> PandaNode:
        """Returns the original, unflattened node."""
    def is_ready(self) -> bool:
        """Returns true if this request has completed, false if it is still pending.
        When this returns true, you may retrieve the model loaded by calling
        result().
        Equivalent to `req.done() and not req.cancelled()`.
        @see done()
        """
    def get_model(self) -> PandaNode:
        """Returns the flattened copy of the model.  It is an error to call this
        unless done() returns true.
        @deprecated Use result() instead.
        """
    getOrig = get_orig
    isReady = is_ready
    getModel = get_model

class ModelLoadRequest(AsyncTask):
    """A class object that manages a single asynchronous model load request.
    Create a new ModelLoadRequest, and add it to the loader via load_async(),
    to begin an asynchronous load.
    """

    @property
    def filename(self) -> Filename: ...
    @property
    def options(self) -> LoaderOptions: ...
    @property
    def loader(self) -> Loader: ...
    @overload
    def __init__(self, __param0: ModelLoadRequest) -> None:
        """Create a new ModelLoadRequest, and add it to the loader via load_async(),
        to begin an asynchronous load.
        """
    @overload
    def __init__(self, name: str, filename: StrOrBytesPath, options: LoaderOptions, loader: Loader) -> None: ...
    def get_filename(self) -> Filename:
        """Returns the filename associated with this asynchronous ModelLoadRequest."""
    def get_options(self) -> LoaderOptions:
        """Returns the LoaderOptions associated with this asynchronous
        ModelLoadRequest.
        """
    def get_loader(self) -> Loader:
        """Returns the Loader object associated with this asynchronous
        ModelLoadRequest.
        """
    def is_ready(self) -> bool:
        """Returns true if this request has completed, false if it is still pending or
        if it has been cancelled.  When this returns true, you may retrieve the
        model loaded by calling get_model().
        Equivalent to `req.done() and not req.cancelled()`.
        @see done()
        """
    def get_model(self) -> PandaNode:
        """Returns the model that was loaded asynchronously, if any, or null if there
        was an error.  It is an error to call this unless done() returns true.
        @deprecated Use result() instead.
        """
    getFilename = get_filename
    getOptions = get_options
    getLoader = get_loader
    isReady = is_ready
    getModel = get_model

class ModelNode(PandaNode):
    """This node is placed at key points within the scene graph to indicate the
    roots of "models": subtrees that are conceptually to be treated as a single
    unit, like a car or a room, for instance.  It doesn't affect rendering or
    any other operations; it's primarily useful as a high-level model
    indication.

    ModelNodes are created in response to a <Model> { 1 } flag within an egg
    file.
    """

    PT_none: Final = 0
    PTNone: Final = 0
    PT_local: Final = 1
    PTLocal: Final = 1
    PT_net: Final = 2
    PTNet: Final = 2
    PT_drop_node: Final = 3
    PTDropNode: Final = 3
    PT_no_touch: Final = 4
    PTNoTouch: Final = 4
    def set_preserve_transform(self, preserve_transform: _ModelNode_PreserveTransform) -> None:
        """Sets the preserve_transform flag.  This restricts the ability of a flatten
        operation to affect the transform stored on this node, and/or the node
        itself.  In the order from weakest to strongest restrictions, the possible
        flags are:

        PT_drop_node - This node should be removed at the next flatten call.

        PT_none - The transform may be adjusted at will.  The node itself will not
        be removed.  This is the default.

        PT_net - Preserve the net transform from the root, but it's acceptable to
        modify the local transform stored on this particular node if necessary, so
        long as the net transform is not changed.  This eliminates the need to drop
        an extra transform on the node above.

        PT_local - The local (and net) transform should not be changed in any way.
        If necessary, an extra transform will be left on the node above to
        guarantee this.  This is a stronger restriction than PT_net.

        PT_no_touch - The local transform will not be changed, the node will not be
        removed, and furthermore any flatten operation will not continue below this
        node--this node and all descendents are protected from the effects of
        flatten.
        """
    def get_preserve_transform(self) -> _ModelNode_PreserveTransform:
        """Returns the current setting of the preserve_transform flag.  See
        set_preserve_transform().
        """
    def set_preserve_attributes(self, attrib_mask: int) -> None:
        """Sets the preserve_attributes flag.  This restricts the ability of a flatten
        operation to affect the render attributes stored on this node.

        The value should be the union of bits from SceneGraphReducer::AttribTypes
        that represent the attributes that should *not* be changed.
        """
    def get_preserve_attributes(self) -> int:
        """Returns the current setting of the preserve_attributes flag.  See
        set_preserve_attributes().
        """
    def set_transform_limit(self, limit: float) -> None: ...
    setPreserveTransform = set_preserve_transform
    getPreserveTransform = get_preserve_transform
    setPreserveAttributes = set_preserve_attributes
    getPreserveAttributes = get_preserve_attributes
    setTransformLimit = set_transform_limit

class ModelRoot(ModelNode):
    """A node of this type is created automatically at the root of each model file
    that is loaded.  It may eventually contain some information about the
    contents of the model; at the moment, it contains no special information,
    but can be used as a flag to indicate the presence of a loaded model file.
    """

    class ModelReference(ReferenceCount):
        """This class is used to unify references to the same model."""

        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: ModelRoot.ModelReference = ...) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...

    fullpath: Filename
    timestamp: int
    reference: ModelRoot.ModelReference
    @property
    def model_ref_count(self) -> int: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, fullpath: StrOrBytesPath, timestamp: int) -> None: ...
    def get_model_ref_count(self) -> int:
        """Returns the number of copies that exist of this particular ModelRoot node.
        Each time ModelRoot::copy_subgraph() or make_copy() is called (or some
        other copying mechanism, such as NodePath.copy_to(), is used), this count
        will increment by one in all copies; when one of the copies is destructed,
        this count will decrement.
        """
    def get_fullpath(self) -> Filename:
        """Returns the full pathname of the model represented by this node, as found
        on disk.  This is mainly useful for reference purposes, but is also used to
        index the ModelRoot into the ModelPool.
        """
    def set_fullpath(self, fullpath: StrOrBytesPath) -> None:
        """Sets the full pathname of the model represented by this node, as found on
        disk.  This is mainly useful for reference purposes, but is also used to
        index the ModelRoot into the ModelPool.

        This is normally set automatically when a model is loaded, and should not
        be set directly by the user.  If you change this on a loaded model, then
        ModelPool::release_model() may fail.
        """
    def get_timestamp(self) -> int:
        """Returns the timestamp of the file on disk that was read for this model, at
        the time it was read, if it is known.  Returns 0 if the timestamp is not
        known or could not be provided.  This can be used as a quick (but fallible)
        check to verify whether the file might have changed since the model was
        read.
        """
    def set_timestamp(self, timestamp: int) -> None:
        """Sets the timestamp of the file on disk that was read for this model.  This
        is normally set automatically when a model is loaded, and should not be set
        directly by the user.
        """
    def get_reference(self) -> ModelRoot.ModelReference:
        """Returns the pointer that represents the object shared between all copies of
        this ModelRoot.  Since there's not much associated with this object other
        than a reference count, normally there's not much reason to get the pointer
        (though it may be compared pointerwise with other ModelRoot objects).
        """
    def set_reference(self, ref: ModelRoot.ModelReference) -> None:
        """Changes the pointer that represents the object shared between all copies of
        this ModelRoot.  This will disassociate this ModelRoot from all of its
        copies.  Normally, there's no reason to do this.
        """
    getModelRefCount = get_model_ref_count
    getFullpath = get_fullpath
    setFullpath = set_fullpath
    getTimestamp = get_timestamp
    setTimestamp = set_timestamp
    getReference = get_reference
    setReference = set_reference

class ModelPool:
    """This class unifies all references to the same filename, so that multiple
    attempts to load the same model will return the same pointer.  Note that
    the default behavior is thus to make instances: use with caution.  Use the
    copy_subgraph() method on Node (or use NodePath::copy_to) to make
    modifiable copies of the node.

    Unlike TexturePool, this class does not automatically resolve the model
    filenames before loading, so a relative path and an absolute path to the
    same model will appear to be different filenames.

    However, see the Loader class, which is now the preferred interface for
    loading models.  The Loader class can resolve filenames, supports threaded
    loading, and can automatically consult the ModelPool, according to the
    supplied LoaderOptions.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def has_model(filename: StrOrBytesPath) -> bool:
        """Returns true if the model has ever been loaded, false otherwise.  Note that
        this does not guarantee that the model is still up-to-date.
        """
    @staticmethod
    def verify_model(filename: StrOrBytesPath) -> bool:
        """Loads the given filename up as a model, if it has not already been loaded,
        and returns true to indicate success, or false to indicate failure.  If
        this returns true, it is probable that a subsequent call to load_model()
        with the same model name will return a valid PandaNode.

        However, even if this returns true, it is still possible for a subsequent
        call to load_model() to fail.  This can happen if cache-check-timestamps is
        true, and the on-disk file is subsequently modified to replace it with an
        invalid model.
        """
    @staticmethod
    def get_model(filename: StrOrBytesPath, verify: bool) -> ModelRoot:
        """Returns the model that has already been previously loaded, or NULL
        otherwise.  If verify is true, it will check if the file is still up-to-
        date (and hasn't been modified in the meantime), and if not, will still
        return NULL.
        """
    @staticmethod
    def load_model(filename: StrOrBytesPath, options: LoaderOptions = ...) -> ModelRoot:
        """Loads the given filename up as a model, if it has not already been loaded,
        and returns the new model.  If a model with the same filename was
        previously loaded, returns that one instead (unless cache-check-timestamps
        is true and the file has recently changed).  If the model file cannot be
        found, or cannot be loaded for some reason, returns NULL.
        """
    @overload
    @staticmethod
    def add_model(model: ModelRoot) -> None:
        """`(filename: Filename, model: ModelRoot)`:
        Adds the indicated already-loaded model to the pool.  The model will
        replace any previously-loaded model in the pool that had the same filename.

        @deprecated Use the one-parameter add_model(model) instead.

        `(model: ModelRoot)`:
        Adds the indicated already-loaded model to the pool.  The model will
        replace any previously-loaded model in the pool that had the same filename.
        """
    @overload
    @staticmethod
    def add_model(filename: StrOrBytesPath, model: ModelRoot) -> None: ...
    @overload
    @staticmethod
    def release_model(filename: StrOrBytesPath) -> None:
        """`(filename: Filename)`:
        Removes the indicated model from the pool, indicating it will never be
        loaded again; the model may then be freed.  If this function is never
        called, a reference count will be maintained on every model every loaded,
        and models will never be freed.

        @deprecated Use release_model(model) instead.

        `(model: ModelRoot)`:
        Removes the indicated model from the pool, indicating it will never be
        loaded again; the model may then be freed.  If this function (and
        garbage_collect()) is never called, a reference count will be maintained on
        every model every loaded, and models will never be freed.

        The model's get_fullpath() value should not have been changed during its
        lifetime, or this function may fail to locate it in the pool.
        """
    @overload
    @staticmethod
    def release_model(model: ModelRoot) -> None: ...
    @staticmethod
    def release_all_models() -> None:
        """Releases all models in the pool and restores the pool to the empty state."""
    @staticmethod
    def garbage_collect() -> int:
        """Releases only those models in the pool that have a reference count of
        exactly 1; i.e.  only those models that are not being used outside of the
        pool.  Returns the number of models released.
        """
    @staticmethod
    def list_contents(out: ostream = ...) -> None:
        """`()`:
        Lists the contents of the model pool to cout.

        `(out: ostream)`:
        Lists the contents of the model pool to the indicated output stream.
        """
    @staticmethod
    def write(out: ostream) -> None:
        """Lists the contents of the model pool to the indicated output stream.  Helps
        with debugging.
        """
    hasModel = has_model
    verifyModel = verify_model
    getModel = get_model
    loadModel = load_model
    addModel = add_model
    releaseModel = release_model
    releaseAllModels = release_all_models
    garbageCollect = garbage_collect
    listContents = list_contents

class ModelSaveRequest(AsyncTask):
    """A class object that manages a single asynchronous model save request.
    Create a new ModelSaveRequest, and add it to the loader via save_async(),
    to begin an asynchronous save.
    """

    @property
    def filename(self) -> Filename: ...
    @property
    def options(self) -> LoaderOptions: ...
    @property
    def node(self) -> PandaNode: ...
    @property
    def loader(self) -> Loader: ...
    @overload
    def __init__(self, __param0: ModelSaveRequest) -> None:
        """Create a new ModelSaveRequest, and add it to the loader via save_async(),
        to begin an asynchronous save.
        """
    @overload
    def __init__(self, name: str, filename: StrOrBytesPath, options: LoaderOptions, node: PandaNode, loader: Loader) -> None: ...
    def get_filename(self) -> Filename:
        """Returns the filename associated with this asynchronous ModelSaveRequest."""
    def get_options(self) -> LoaderOptions:
        """Returns the LoaderOptions associated with this asynchronous
        ModelSaveRequest.
        """
    def get_node(self) -> PandaNode:
        """Returns the node that was passed to the constructor."""
    def get_loader(self) -> Loader:
        """Returns the Loader object associated with this asynchronous
        ModelSaveRequest.
        """
    def is_ready(self) -> bool:
        """Returns true if this request has completed, false if it is still pending.
        When this returns true, you may retrieve the success flag with
        get_success().
        Equivalent to `req.done() and not req.cancelled()`.
        @see done()
        """
    def get_success(self) -> bool:
        """Returns the true if the model was saved successfully, false otherwise.  It
        is an error to call this unless done() returns true.
        """
    getFilename = get_filename
    getOptions = get_options
    getNode = get_node
    getLoader = get_loader
    isReady = is_ready
    getSuccess = get_success

class TextureAttrib(RenderAttrib):
    """Indicates the set of TextureStages and their associated Textures that
    should be applied to (or removed from) a node.
    """

    @property
    def on_stages(self) -> Sequence[TextureStage]: ...
    @property
    def textures(self) -> Mapping[TextureStage, Texture]: ...
    @property
    def samplers(self) -> Mapping[TextureStage, SamplerState]: ...
    @property
    def off_stages(self) -> Sequence[TextureStage]: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(tex: Texture = ...) -> RenderAttrib:
        """`()`:
        The following methods define the new multitexture mode for TextureAttrib.
        Each TextureAttrib can add or remove individual texture stages from the
        complete set of textures that are to be applied; this is similar to the
        mechanism of LightAttrib.

        `(tex: Texture)`:
        Constructs a new TextureAttrib object suitable for rendering the indicated
        texture onto geometry, using the default TextureStage.
        """
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new TextureAttrib object suitable for rendering untextured
        geometry.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def is_off(self) -> bool:
        """Returns true if the TextureAttrib is an 'off' TextureAttrib, indicating
        that it should disable texturing.

        If multitexture is in effect, a TextureAttrib may not be strictly "on" or
        "off"; therefore, to get a more precise answer to this question, you should
        consider using has_all_off() or get_num_off_stages() or has_off_stage()
        instead.
        """
    def get_texture(self) -> Texture:
        """If the TextureAttrib is not an 'off' TextureAttrib, returns the base-level
        texture that is associated.  Otherwise, return NULL.
        """
    @staticmethod
    def make_all_off() -> RenderAttrib:
        """Constructs a new TextureAttrib object that turns off all stages (and hence
        disables texturing).
        """
    def get_num_on_stages(self) -> int:
        """Returns the number of stages that are turned on by the attribute."""
    def get_on_stage(self, n: int) -> TextureStage:
        """Returns the nth stage turned on by the attribute, sorted in render order."""
    def get_num_on_ff_stages(self) -> int:
        """Returns the number of on-stages that are relevant to the classic fixed
        function pipeline.  This excludes texture stages such as normal maps.
        """
    def get_on_ff_stage(self, n: int) -> TextureStage:
        """Returns the nth stage turned on by the attribute, sorted in render order,
        including only those relevant to the classic fixed function pipeline.  This
        excludes texture stages such as normal maps.
        """
    def get_ff_tc_index(self, n: int) -> int:
        """For each TextureStage listed in get_on_ff_stage(), this returns a unique
        index number for the texture coordinate name used by that TextureStage.  It
        is guaranteed to remain the same index number for each texcoord name (for a
        given set of TextureStages), even if the texture render order changes.
        """
    def has_on_stage(self, stage: TextureStage) -> bool:
        """Returns true if the indicated stage is turned on by the attrib, false
        otherwise.
        """
    def get_on_texture(self, stage: TextureStage) -> Texture:
        """Returns the texture associated with the indicated stage, or NULL if no
        texture is associated.
        """
    def get_on_sampler(self, stage: TextureStage) -> SamplerState:
        """Returns the sampler associated with the indicated stage, or the one
        associated with its texture if no custom stage has been specified.  It is
        an error to call this if the stage does not exist.
        """
    def get_on_stage_override(self, stage: TextureStage) -> int:
        """Returns the override value associated with the indicated stage."""
    def find_on_stage(self, stage: TextureStage) -> int:
        """Returns the index number of the indicated TextureStage within the list of
        on_stages, or -1 if the indicated stage is not listed.
        """
    def get_num_off_stages(self) -> int:
        """Returns the number of stages that are turned off by the attribute."""
    def get_off_stage(self, n: int) -> TextureStage:
        """Returns the nth stage turned off by the attribute, sorted in arbitrary
        (pointer) order.
        """
    def has_off_stage(self, stage: TextureStage) -> bool:
        """Returns true if the indicated stage is turned off by the attrib, false
        otherwise.
        """
    def has_all_off(self) -> bool:
        """Returns true if this attrib turns off all stages (although it may also turn
        some on).
        """
    def is_identity(self) -> bool:
        """Returns true if this is an identity attrib: it does not change the set of
        stages in use.
        """
    @overload
    def add_on_stage(self, stage: TextureStage, tex: Texture, override: int = ...) -> RenderAttrib:
        """Returns a new TextureAttrib, just like this one, but with the indicated
        stage added to the list of stages turned on by this attrib.
        """
    @overload
    def add_on_stage(self, stage: TextureStage, tex: Texture, sampler: SamplerState, override: int = ...) -> RenderAttrib: ...
    def remove_on_stage(self, stage: TextureStage) -> RenderAttrib:
        """Returns a new TextureAttrib, just like this one, but with the indicated
        stage removed from the list of stages turned on by this attrib.
        """
    def add_off_stage(self, stage: TextureStage, override: int = ...) -> RenderAttrib:
        """Returns a new TextureAttrib, just like this one, but with the indicated
        stage added to the list of stages turned off by this attrib.
        """
    def remove_off_stage(self, stage: TextureStage) -> RenderAttrib:
        """Returns a new TextureAttrib, just like this one, but with the indicated
        stage removed from the list of stages turned off by this attrib.
        """
    def unify_texture_stages(self, stage: TextureStage) -> RenderAttrib:
        """Returns a new TextureAttrib, just like this one, but with any included
        TextureAttribs that happen to have the same name as the given object
        replaced with the object.
        """
    def replace_texture(self, tex: Texture, new_tex: Texture | None) -> RenderAttrib:
        """`(self, tex: Texture, new_tex: Texture)`:
        Returns a new TextureAttrib, just like this one, but with all references to
        the given texture replaced with the new texture.

        As of Panda3D 1.10.13, new_tex may be null to remove the texture.

        @since 1.10.4

        `(self, tex: Texture, new_tex: None)`:
        Let interrogate know this also accepts None
        """
    @staticmethod
    def get_class_slot() -> int: ...
    def get_on_stages(self) -> tuple[TextureStage, ...]: ...
    def get_on_ff_stages(self) -> tuple[TextureStage, ...]: ...
    def get_off_stages(self) -> tuple[TextureStage, ...]: ...
    makeOff = make_off
    makeDefault = make_default
    isOff = is_off
    getTexture = get_texture
    makeAllOff = make_all_off
    getNumOnStages = get_num_on_stages
    getOnStage = get_on_stage
    getNumOnFfStages = get_num_on_ff_stages
    getOnFfStage = get_on_ff_stage
    getFfTcIndex = get_ff_tc_index
    hasOnStage = has_on_stage
    getOnTexture = get_on_texture
    getOnSampler = get_on_sampler
    getOnStageOverride = get_on_stage_override
    findOnStage = find_on_stage
    getNumOffStages = get_num_off_stages
    getOffStage = get_off_stage
    hasOffStage = has_off_stage
    hasAllOff = has_all_off
    isIdentity = is_identity
    addOnStage = add_on_stage
    removeOnStage = remove_on_stage
    addOffStage = add_off_stage
    removeOffStage = remove_off_stage
    unifyTextureStages = unify_texture_stages
    replaceTexture = replace_texture
    getClassSlot = get_class_slot
    getOnStages = get_on_stages
    getOnFfStages = get_on_ff_stages
    getOffStages = get_off_stages

class TexGenAttrib(RenderAttrib):
    """Computes texture coordinates for geometry automatically based on vertex
    position and/or normal.  This can be used to implement reflection and/or
    refraction maps, for instance to make shiny surfaces, as well as other
    special effects such as projective texturing.
    """

    @property
    def class_slot(self) -> int: ...
    @overload
    @staticmethod
    def make() -> RenderAttrib:
        """`()`:
        Constructs a TexGenAttrib that generates no stages at all.

        `(stage: TextureStage, mode: _RenderAttrib_TexGenMode)`:
        Constructs a TexGenAttrib that generates just the indicated stage.
        """
    @overload
    @staticmethod
    def make(stage: TextureStage, mode: _RenderAttrib_TexGenMode) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def add_stage(self, stage: TextureStage, mode: _RenderAttrib_TexGenMode, constant_value: Vec3Like = ...) -> RenderAttrib:
        """`(self, stage: TextureStage, mode: _RenderAttrib_TexGenMode)`:
        Returns a new TexGenAttrib just like this one, with the indicated
        generation mode for the given stage.  If this stage already exists, its
        mode is replaced.

        `(self, stage: TextureStage, mode: _RenderAttrib_TexGenMode, constant_value: LTexCoord3)`:
        Returns a new TexGenAttrib just like this one, with the indicated
        generation mode for the given stage.  If this stage already exists, its
        mode is replaced.

        This variant also accepts constant_value, which is only meaningful if mode
        is M_constant.
        """
    def remove_stage(self, stage: TextureStage) -> RenderAttrib:
        """Returns a new TexGenAttrib just like this one, with the indicated stage
        removed.
        """
    def is_empty(self) -> bool:
        """Returns true if no stages are defined in the TexGenAttrib, false if at
        least one is.
        """
    def has_stage(self, stage: TextureStage) -> bool:
        """Returns true if there is a mode associated with the indicated stage, or
        false otherwise (in which case get_transform(stage) will return M_off).
        """
    def get_mode(self, stage: TextureStage) -> _RenderAttrib_TexGenMode:
        """Returns the generation mode associated with the named texture stage, or
        M_off if nothing is associated with the indicated stage.
        """
    def has_gen_texcoord_stage(self, stage: TextureStage) -> bool:
        """Returns true if the indicated TextureStage will have texture coordinates
        generated for it automatically (and thus there is no need to upload the
        texture coordinates encoded in the vertices).
        """
    def get_constant_value(self, stage: TextureStage) -> LTexCoord3:
        """Returns the constant value associated with the named texture stage.  This
        is only meaningful if the mode is M_constant.
        """
    def get_geom_rendering(self, geom_rendering: int) -> int:
        """Returns the union of the Geom::GeomRendering bits that will be required
        once this TexGenAttrib is applied to a geom which includes the indicated
        geom_rendering bits.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    addStage = add_stage
    removeStage = remove_stage
    isEmpty = is_empty
    hasStage = has_stage
    getMode = get_mode
    hasGenTexcoordStage = has_gen_texcoord_stage
    getConstantValue = get_constant_value
    getGeomRendering = get_geom_rendering
    getClassSlot = get_class_slot

class OccluderNode(PandaNode):
    """A node in the scene graph that can hold an occluder polygon, which must be
    a rectangle.  When the occluder is activated with something like
    render.set_occluder(), then objects whose bouding volume lies entirely
    behind the occluder will not be rendered.
    """

    double_sided: bool
    min_coverage: float
    @property
    def vertices(self) -> MutableSequence[LPoint3]: ...
    def __init__(self, name: str) -> None:
        """The default constructor creates a default occlusion polygon in the XZ plane
        (or XY plane in a y-up coordinate system).  Use the normal Panda set_pos(),
        set_hpr(), set_scale() to position it appropriately, or replace the
        vertices with set_vertices().
        """
    def set_double_sided(self, value: bool) -> None:
        """If true, the back-face will also be used to occlude"""
    def is_double_sided(self) -> bool:
        """Is this occluder double-sided"""
    def set_min_coverage(self, value: float) -> None:
        """Minimum screen coverage needed before occluder used.  Range should be 0 to
        1. For example, setting to 0.2 would mean that the occluder needs to cover
        20% of the screen to be considered.
        """
    def get_min_coverage(self) -> float:
        """Returns the minimum screen coverage."""
    def set_vertices(self, v0: Vec3Like, v1: Vec3Like, v2: Vec3Like, v3: Vec3Like) -> None:
        """Replaces the four vertices of the occluder polygon.  The vertices should be
        defined in a counterclockwise orientation when looking at the face of the
        occluder.
        """
    def get_num_vertices(self) -> int:
        """Returns the number of vertices in the occluder polygon.  This should always
        return 4.
        """
    def get_vertex(self, n: int) -> LPoint3:
        """Returns the nth vertex of the occluder polygon."""
    def set_vertex(self, n: int, v: Vec3Like) -> None:
        """Sets the nth vertex of the occluder polygon."""
    def get_vertices(self) -> tuple[LPoint3, ...]: ...
    setDoubleSided = set_double_sided
    isDoubleSided = is_double_sided
    setMinCoverage = set_min_coverage
    getMinCoverage = get_min_coverage
    setVertices = set_vertices
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    setVertex = set_vertex
    getVertices = get_vertices

class OccluderEffect(RenderEffect):
    """This functions similarly to a LightAttrib or ClipPlaneAttrib.  It indicates
    the set of occluders that modify the geometry at this level and below.
    Unlike a ClipPlaneAttrib, an OccluderEffect takes effect immediately when
    it is encountered during traversal, and thus can only add occluders; it may
    not remove them.
    """

    @staticmethod
    def make() -> RenderEffect:
        """Constructs a new OccluderEffect object that does nothing."""
    def get_num_on_occluders(self) -> int:
        """Returns the number of occluders that are enabled by the effectute."""
    def get_on_occluder(self, n: int) -> NodePath:
        """Returns the nth occluder enabled by the effectute, sorted in render order."""
    def has_on_occluder(self, occluder: NodePath) -> bool:
        """Returns true if the indicated occluder is enabled by the effect, false
        otherwise.
        """
    def is_identity(self) -> bool:
        """Returns true if this is an identity effect: it does not change the set of
        occluders in use.
        """
    def add_on_occluder(self, occluder: NodePath) -> RenderEffect:
        """Returns a new OccluderEffect, just like this one, but with the indicated
        occluder added to the list of occluders enabled by this effect.
        """
    def remove_on_occluder(self, occluder: NodePath) -> RenderEffect:
        """Returns a new OccluderEffect, just like this one, but with the indicated
        occluder removed from the list of occluders enabled by this effect.
        """
    def get_on_occluders(self) -> tuple[NodePath, ...]: ...
    getNumOnOccluders = get_num_on_occluders
    getOnOccluder = get_on_occluder
    hasOnOccluder = has_on_occluder
    isIdentity = is_identity
    addOnOccluder = add_on_occluder
    removeOnOccluder = remove_on_occluder
    getOnOccluders = get_on_occluders

class PolylightNode(PandaNode):
    """A PolylightNode"""

    FRANDOM: Final = 0
    FSIN: Final = 1
    FCUSTOM: Final = 2
    ALINEAR: Final = 0
    AQUADRATIC: Final = 1
    @overload
    def __init__(self, __param0: PolylightNode) -> None:
        """Use PolylightNode() to construct a new PolylightNode object."""
    @overload
    def __init__(self, name: str) -> None: ...
    def __eq__(self, __other: object) -> bool:
        """Comparison methods"""
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: PolylightNode) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def enable(self) -> None:
        """Enable this light"""
    def disable(self) -> None:
        """Disable this light"""
    @overload
    def set_pos(self, position: Vec3Like) -> None:
        """Set this light's position"""
    @overload
    def set_pos(self, x: float, y: float, z: float) -> None: ...
    def get_pos(self) -> LPoint3:
        """Returns position as a LPoint3"""
    @overload
    def set_color(self, color: Vec4Like) -> None:
        """`(self, color: LColor)`:
        Set the light's color...

        `(self, r: float, g: float, b: float)`:
        Set the light's color... 3 floats between 0 and 1
        """
    @overload
    def set_color(self, r: float, g: float, b: float) -> None: ...
    def get_color(self) -> LColor:
        """Returns the light's color as LColor"""
    def get_color_scenegraph(self) -> LColor:
        """This differs from get_color in that when applying the light color we need
        to make sure that a color flattening external to the PolylightNode is not
        ignored.
        """
    def set_radius(self, r: float) -> None:
        """Set radius of the spherical light volume"""
    def get_radius(self) -> float:
        """Get radius of the spherical light volume"""
    def set_attenuation(self, type: _PolylightNode_Attenuation_Type) -> bool:
        """Set ALINEAR or AQUADRATIC attenuation"""
    def get_attenuation(self) -> _PolylightNode_Attenuation_Type:
        """Get "linear" or "quadratic" attenuation type"""
    def set_a0(self, a0: float) -> None:
        """Set the quadratic attenuation factor a0 fd = 1 / ( a0 + a1*distance +
        a2*distance*distance)
        """
    def set_a1(self, a1: float) -> None:
        """Set the quadratic attenuation factor a1 fd = 1 / ( a0 + a1*distance +
        a2*distance*distance)
        """
    def set_a2(self, a2: float) -> None:
        """Set the quadratic attenuation factor a2 fd = 1 / ( a0 + a1*distance +
        a2*distance*distance)
        """
    def get_a0(self) -> float:
        """Get the quadratic attenuation factor a0 fd = 1 / ( a0 + a1*distance +
        a2*distance*distance)
        """
    def get_a1(self) -> float:
        """Get the quadratic attenuation factor a1 fd = 1 / ( a0 + a1*distance +
        a2*distance*distance)
        """
    def get_a2(self) -> float:
        """Get the quadratic attenuation factor a2 fd = 1 / ( a0 + a1*distance +
        a2*distance*distance)
        """
    def flicker_on(self) -> None:
        """Set flickering to true so at every loop this light's color is varied based
        on flicker_type
        """
    def flicker_off(self) -> None:
        """Turn flickering off"""
    def is_flickering(self) -> bool:
        """Check is this light is flickering"""
    def set_flicker_type(self, type: _PolylightNode_Flicker_Type) -> bool:
        """Flicker type can be FRANDOM or FSIN At a later point there might be a
        FCUSTOM Custom flicker will be a set of fix points recorded by animating
        the light's intensity
        """
    def get_flicker_type(self) -> _PolylightNode_Flicker_Type:
        """Returns FRANDOM or FSIN"""
    def set_offset(self, offset: float) -> None:
        """Set the offset value for the random and sin flicker variations... used to
        tweak the flicker This value is added to the variation
        """
    def get_offset(self) -> float:
        """Get the offset value for the random and sin flicker variations"""
    def set_scale(self, scale: float) -> None:
        """Set the scale value for the random and sin flicker variations... used to
        tweak the flicker This value is multiplied with the variation
        """
    def get_scale(self) -> float:
        """Get the scale value for the random and sin flicker variations"""
    def set_step_size(self, step: float) -> None:
        """Set the step size for the sin function in flicker This is the increment
        size for the value supplied to the sin function
        """
    def get_step_size(self) -> float:
        """Get the step size for the sin function in flicker This is the increment
        size for the value supplied to the sin function
        """
    def set_freq(self, f: float) -> None:
        """Set frequency of sin flicker"""
    def get_freq(self) -> float:
        """Get frequency of sin flicker"""
    def compare_to(self, other: PolylightNode) -> int:
        """Returns a number less than zero if this PolylightNode sorts before the
        other one, greater than zero if it sorts after, or zero if they are
        equivalent.

        Two PolylightNodes are considered equivalent if they consist of exactly the
        same properties Otherwise, they are different; different PolylightNodes
        will be ranked in a consistent but undefined ordering; the ordering is
        useful only for placing the PolylightNodes in a sorted container like an
        STL set.
        """
    def is_enabled(self) -> bool:
        """Is this light is enabled/disabled?"""
    setPos = set_pos
    getPos = get_pos
    setColor = set_color
    getColor = get_color
    getColorScenegraph = get_color_scenegraph
    setRadius = set_radius
    getRadius = get_radius
    setAttenuation = set_attenuation
    getAttenuation = get_attenuation
    setA0 = set_a0
    setA1 = set_a1
    setA2 = set_a2
    getA0 = get_a0
    getA1 = get_a1
    getA2 = get_a2
    flickerOn = flicker_on
    flickerOff = flicker_off
    isFlickering = is_flickering
    setFlickerType = set_flicker_type
    getFlickerType = get_flicker_type
    setOffset = set_offset
    getOffset = get_offset
    setScale = set_scale
    getScale = get_scale
    setStepSize = set_step_size
    getStepSize = get_step_size
    setFreq = set_freq
    getFreq = get_freq
    compareTo = compare_to
    isEnabled = is_enabled

class PolylightEffect(RenderEffect):
    """A PolylightEffect can be used on a node to define a LightGroup  for that
    node.  A LightGroup contains PolylightNodes which are essentially nodes
    that add color to the polygons of a model based on distance.  PolylightNode
    is a cheap way to get lighting effects specially for night scenes
    """

    CT_proximal: Final = 0
    CTProximal: Final = 0
    CT_all: Final = 1
    CTAll: Final = 1
    @overload
    @staticmethod
    def make() -> RenderEffect:
        """Constructs a new PolylightEffect object."""
    @overload
    @staticmethod
    def make(weight: float, contrib: _PolylightEffect_ContribType, effect_center: Vec3Like) -> RenderEffect: ...
    def add_light(self, newlight: NodePath) -> RenderEffect:
        """Add a PolylightNode object to this effect and return a new effect"""
    def remove_light(self, newlight: NodePath) -> RenderEffect:
        """Remove a light from this effect.  Return the new updated effect"""
    def set_weight(self, w: float) -> RenderEffect:
        """Set weight and return a new effect... the reason this couldnt be done
        through make was because that would return a new effect without the
        lightgroup which is static and cant be accessed Here, we just pass that to
        the make
        """
    def set_contrib(self, c: _PolylightEffect_ContribType) -> RenderEffect:
        """Set Contrib Type and return a new effect... the reason this couldnt be done
        through make was because that would return a new effect without the
        lightgroup which is static and cant be accessed Here, we just pass that to
        the make
        """
    def set_effect_center(self, ec: Vec3Like) -> RenderEffect:
        """Set weight and return a new effect... the reason this couldnt be done
        through make was because that would return a new effect without the
        lightgroup which is static and cant be accessed Here, we just pass that to
        the make
        """
    def get_weight(self) -> float:
        """Get the weight value"""
    def get_contrib(self) -> _PolylightEffect_ContribType:
        """Returns CT_all or CT_proximal"""
    def get_effect_center(self) -> LPoint3:
        """Return the value of the _effect_center"""
    def has_light(self, light: NodePath) -> bool:
        """Returns true if the indicated light is listed in the PolylightEffect, false
        otherwise.
        """
    addLight = add_light
    removeLight = remove_light
    setWeight = set_weight
    setContrib = set_contrib
    setEffectCenter = set_effect_center
    getWeight = get_weight
    getContrib = get_contrib
    getEffectCenter = get_effect_center
    hasLight = has_light

class ShaderAttrib(RenderAttrib):
    F_disable_alpha_write: Final = 0
    F_subsume_alpha_test: Final = 1
    F_hardware_skinning: Final = 2
    F_shader_point_size: Final = 3
    @property
    def shader(self) -> Shader: ...
    @property
    def instance_count(self) -> int: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(shader: Shader = ..., priority: int = ...) -> RenderAttrib:
        """Constructs a new ShaderAttrib object with nothing set."""
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new ShaderAttrib object that disables the use of shaders (it
        does not clear out all shader data, however.)
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def has_shader(self) -> bool:
        """If true, the shader field of this attribute overrides the shader field of
        the parent attribute.
        """
    def auto_shader(self) -> bool:
        """If true, then this ShaderAttrib does not contain an explicit shader -
        instead, it requests the automatic generation of a shader.
        """
    def get_shader_priority(self) -> int: ...
    def get_instance_count(self) -> int:
        """Returns the number of geometry instances.  A value of 0 means not to use
        instancing at all.
        """
    def auto_normal_on(self) -> bool: ...
    def auto_glow_on(self) -> bool: ...
    def auto_gloss_on(self) -> bool: ...
    def auto_ramp_on(self) -> bool: ...
    def auto_shadow_on(self) -> bool: ...
    def set_shader(self, s: Shader, priority: int = ...) -> RenderAttrib: ...
    def set_shader_off(self, priority: int = ...) -> RenderAttrib: ...
    @overload
    def set_shader_auto(self, priority: int = ...) -> RenderAttrib:
        """Set auto shader with bitmask to customize use, e.g., to keep normal, glow,
        etc., on or off
        """
    @overload
    def set_shader_auto(self, shader_switch: BitMask32, priority: int = ...) -> RenderAttrib: ...
    def clear_shader(self) -> RenderAttrib: ...
    @overload
    def set_shader_input(self, input: ShaderInput) -> RenderAttrib:
        """Shader Inputs"""
    @overload
    def set_shader_input(self, __param0: InternalName | str, __param1, priority: int = ...) -> RenderAttrib: ...
    def set_shader_inputs(self, *args, **kwargs) -> RenderAttrib: ...
    def set_instance_count(self, instance_count: int) -> RenderAttrib:
        """Sets the geometry instance count.  Do not confuse this with instanceTo,
        which is used for animation instancing, and has nothing to do with this.  A
        value of 0 means not to use instancing at all.
        """
    def set_flag(self, flag: int, value: bool) -> RenderAttrib: ...
    def clear_flag(self, flag: int) -> RenderAttrib: ...
    def clear_shader_input(self, id: InternalName | str) -> RenderAttrib: ...
    def clear_all_shader_inputs(self) -> RenderAttrib:
        """Clears all the shader inputs on the attrib."""
    def get_flag(self, flag: int) -> bool: ...
    def has_shader_input(self, id: InternalName | str) -> bool:
        """Returns true if there is a ShaderInput of the given name."""
    def get_shader(self) -> Shader:
        """Returns the shader object associated with the node.  If get_override
        returns true, but get_shader returns NULL, that means that this attribute
        should disable the shader.
        """
    def get_shader_input(self, id: InternalName | str) -> ShaderInput:
        """Returns the ShaderInput of the given name.  If no such name is found, this
        function does not return NULL --- it returns the "blank" ShaderInput.
        """
    def get_shader_input_nodepath(self, id: InternalName | str) -> NodePath:
        """Returns the ShaderInput as a nodepath.  Assertion fails if there is none,
        or if it is not a nodepath.
        """
    def get_shader_input_vector(self, id: InternalName | str) -> LVecBase4:
        """Returns the ShaderInput as a vector.  Assertion fails if there is none, or
        if it is not a vector.
        """
    def get_shader_input_texture(self, id: InternalName | str, sampler: SamplerState = ...) -> Texture:
        """Returns the ShaderInput as a texture.  Assertion fails if there is none, or
        if it is not a texture.

        If sampler is not NULL, the sampler state to use for this texture is
        assigned to it.
        """
    def get_shader_input_matrix(self, id: InternalName | str, matrix: Mat4Like) -> LMatrix4:
        """Returns the ShaderInput as a matrix.  Assertion fails if there is none, or
        if it is not a matrix or NodePath.
        """
    def get_shader_input_buffer(self, id: InternalName | str) -> ShaderBuffer:
        """Returns the ShaderInput as a ShaderBuffer.  Assertion fails if there is
        none, or if it is not a ShaderBuffer.
        """
    @staticmethod
    def register_with_read_factory() -> None:
        """Factory method to generate a Shader object"""
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    hasShader = has_shader
    autoShader = auto_shader
    getShaderPriority = get_shader_priority
    getInstanceCount = get_instance_count
    autoNormalOn = auto_normal_on
    autoGlowOn = auto_glow_on
    autoGlossOn = auto_gloss_on
    autoRampOn = auto_ramp_on
    autoShadowOn = auto_shadow_on
    setShader = set_shader
    setShaderOff = set_shader_off
    setShaderAuto = set_shader_auto
    clearShader = clear_shader
    setShaderInput = set_shader_input
    setShaderInputs = set_shader_inputs
    setInstanceCount = set_instance_count
    setFlag = set_flag
    clearFlag = clear_flag
    clearShaderInput = clear_shader_input
    clearAllShaderInputs = clear_all_shader_inputs
    getFlag = get_flag
    hasShaderInput = has_shader_input
    getShader = get_shader
    getShaderInput = get_shader_input
    getShaderInputNodepath = get_shader_input_nodepath
    getShaderInputVector = get_shader_input_vector
    getShaderInputTexture = get_shader_input_texture
    getShaderInputMatrix = get_shader_input_matrix
    getShaderInputBuffer = get_shader_input_buffer
    registerWithReadFactory = register_with_read_factory
    getClassSlot = get_class_slot

class ShowBoundsEffect(RenderEffect):
    """Applied to a GeomNode to cause a visible bounding volume to be drawn for
    this node.  This is generally used only during development to help identify
    bounding volume issues.
    """

    @staticmethod
    def make(tight: bool = ...) -> RenderEffect:
        """Constructs a new ShowBoundsEffect object."""
    def get_tight(self) -> bool:
        """Returns true if the "tight" flag was set, meaning the effect should compute
        and draw the tight bounding-box of the node's vertices every frame.
        """
    getTight = get_tight

class TexProjectorEffect(RenderEffect):
    """This effect automatically applies a computed texture matrix to the
    specified texture stage, according to the relative position of two
    specified nodes.

    The relative transform from the "from" node to the "to" node is applied
    directly to the texture matrix each frame.  If the "to" node happens to be
    a LensNode, its lens projection matrix is applied as well.

    This can be used to apply a number of special effects.  Fundamentally, it
    may simply be used to provide a separate PandaNode that may be adjusted
    (e.g.  via a LerpInterval) in order to easily apply a linear transformation
    to an object's texture coordinates (rather than having to explicitly call
    NodePath.set_tex_transform() each frame).

    In a more sophisticated case, the TexProjectorEffect is particularly useful
    in conjunction with a TexGenAttrib that specifies a mode of
    M_world_position (which copies the world position of each vertex to the
    texture coordinates).  Then the TexProjector can be used to convert these
    world coordinates to the relative coordinates of a particular node, causing
    (for instance) a texture to appear to follow a node around as it moves
    through the world.  With a LensNode, you can project a texture onto the
    walls, for instance to apply a flashlight effect or an image-based shadow.
    """

    @staticmethod
    def make() -> RenderEffect:
        """Constructs a TexProjectorEffect that modifies no stages at all."""
    def add_stage(self, stage: TextureStage, _from: NodePath, to: NodePath, lens_index: int = ...) -> RenderEffect:
        """Returns a new TexProjectorEffect just like this one, with the indicated
        projection for the given stage.  If this stage already exists, its
        projection definition is replaced.

        The relative transform between the "from" and the "to" nodes is
        automatically applied to the texture transform each frame.

        Furthermore, if the "to" node is a LensNode, its projection matrix is also
        applied to the texture transform.  In this case, the lens_index may be used
        to select the particular lens that should be used.
        """
    def remove_stage(self, stage: TextureStage) -> RenderEffect:
        """Returns a new TexProjectorEffect just like this one, with the indicated
        stage removed.
        """
    def is_empty(self) -> bool:
        """Returns true if no stages are defined in the TexProjectorEffect, false if
        at least one is.
        """
    def has_stage(self, stage: TextureStage) -> bool:
        """Returns true if there is a transform associated with the indicated stage,
        or false otherwise (in which case get_transform(stage) will return the
        identity transform).
        """
    def get_from(self, stage: TextureStage) -> NodePath:
        """Returns the "from" node associated with the TexProjectorEffect on the
        indicated stage.  The relative transform between the "from" and the "to"
        nodes is automatically applied to the texture transform each frame.
        """
    def get_to(self, stage: TextureStage) -> NodePath:
        """Returns the "to" node associated with the TexProjectorEffect on the
        indicated stage.  The relative transform between the "from" and the "to"
        nodes is automatically applied to the texture transform each frame.

        Furthermore, if the "to" node is a LensNode, its projection matrix is also
        applied to the texture transform.
        """
    def get_lens_index(self, stage: TextureStage) -> int:
        """Returns the lens_index associated with the TexProjectorEffect on the
        indicated stage.  This is only used if the "to" node is a LensNode, in
        which case it specifies the particular lens that should be used.
        """
    addStage = add_stage
    removeStage = remove_stage
    isEmpty = is_empty
    hasStage = has_stage
    getFrom = get_from
    getTo = get_to
    getLensIndex = get_lens_index

class ScissorEffect(RenderEffect):
    """This provides a higher-level wrapper around ScissorAttrib.  It allows for
    the scissor region to be defined via points relative to the current node,
    and also performs culling based on the scissor region.
    """

    @staticmethod
    def make_screen(frame: Vec4Like, clip: bool = ...) -> RenderEffect:
        """Constructs a new screen-relative ScissorEffect.  The frame defines a left,
        right, bottom, top region, relative to the DisplayRegion.  See
        ScissorAttrib.
        """
    @overload
    @staticmethod
    def make_node(clip: bool = ...) -> RenderEffect:
        """`(a: LPoint3, b: LPoint3, c: LPoint3, d: LPoint3, node: NodePath = ...)`:
        Constructs a new node-relative ScissorEffect.  The four points are
        understood to be relative to the indicated node, or the current node if the
        indicated NodePath is empty, and determine four points surrounding the
        scissor region.

        `(a: LPoint3, b: LPoint3, node: NodePath = ...)`:
        Constructs a new node-relative ScissorEffect.  The two points are
        understood to be relative to the indicated node, or the current node if the
        NodePath is empty, and determine the diagonally opposite corners of the
        scissor region.

        `(clip: bool = ...)`:
        Constructs a new node-relative ScissorEffect, with no points.  This empty
        ScissorEffect does nothing.  You must then call add_point a number of times
        to add the points you require.
        """
    @overload
    @staticmethod
    def make_node(a: Vec3Like, b: Vec3Like, node: NodePath = ...) -> RenderEffect: ...
    @overload
    @staticmethod
    def make_node(a: Vec3Like, b: Vec3Like, c: Vec3Like, d: Vec3Like, node: NodePath = ...) -> RenderEffect: ...
    def add_point(self, point: Vec3Like, node: NodePath = ...) -> RenderEffect:
        """Returns a new ScissorEffect with the indicated point added.  It is only
        valid to call this on a "node" type ScissorEffect.  The full set of points,
        projected into screen space, defines the bounding volume of the rectangular
        scissor region.

        Each point may be relative to a different node, if desired.
        """
    def is_screen(self) -> bool:
        """Returns true if the ScissorEffect is a screen-based effect, meaning
        get_frame() has a meaningful value, but get_a() and get_b() do not.
        """
    def get_frame(self) -> LVecBase4:
        """If is_screen() returns true, this method may be called to query the screen-
        based scissor frame.  This is a series of left, right, bottom, top,
        representing the scissor frame relative to the current DisplayRegion.  See
        ScissorAttrib.
        """
    def get_num_points(self) -> int:
        """Returns the number of node-based scissor points.  See get_point()."""
    def get_point(self, n: int) -> LPoint3:
        """If is_screen() returns false, then get_num_points() and get_point() may be
        called to query the node-based scissor frame.  These return n points (at
        least two), which are understood to be in the space of this node, and which
        define any opposite corners of the scissor frame.
        """
    def get_node(self, n: int) -> NodePath:
        """Returns the node to which the nth point is relative, or empty NodePath to
        indicate the current node.
        """
    def get_clip(self) -> bool:
        """Returns true if this ScissorEffect actually enables scissoring, or false if
        it culls only.
        """
    def get_points(self) -> tuple[LPoint3, ...]: ...
    def get_nodes(self) -> tuple[NodePath, ...]: ...
    makeScreen = make_screen
    makeNode = make_node
    addPoint = add_point
    isScreen = is_screen
    getFrame = get_frame
    getNumPoints = get_num_points
    getPoint = get_point
    getNode = get_node
    getClip = get_clip
    getPoints = get_points
    getNodes = get_nodes

class SceneGraphReducer:
    """An interface for simplifying ("flattening") scene graphs by eliminating
    unneeded nodes and collapsing out unneeded state changes and transforms.

    This class is designed so that it may be inherited from and specialized, if
    needed, to fine-tune the flattening behavior, but normally the default
    behavior is sufficient.
    """

    TT_transform: Final = 1
    TTTransform: Final = 1
    TT_color: Final = 2
    TTColor: Final = 2
    TT_color_scale: Final = 4
    TTColorScale: Final = 4
    TT_tex_matrix: Final = 8
    TTTexMatrix: Final = 8
    TT_clip_plane: Final = 16
    TTClipPlane: Final = 16
    TT_cull_face: Final = 32
    TTCullFace: Final = 32
    TT_apply_texture_color: Final = 64
    TTApplyTextureColor: Final = 64
    TT_other: Final = 128
    TTOther: Final = 128
    CS_geom_node: Final = 1
    CSGeomNode: Final = 1
    CS_within_radius: Final = 2
    CSWithinRadius: Final = 2
    CS_other: Final = 4
    CSOther: Final = 4
    CS_recurse: Final = 8
    CSRecurse: Final = 8
    CVD_name: Final = 1
    CVDName: Final = 1
    CVD_model: Final = 2
    CVDModel: Final = 2
    CVD_transform: Final = 4
    CVDTransform: Final = 4
    CVD_avoid_dynamic: Final = 8
    CVDAvoidDynamic: Final = 8
    CVD_one_node_only: Final = 16
    CVDOneNodeOnly: Final = 16
    CVD_format: Final = 32
    CVDFormat: Final = 32
    CVD_usage_hint: Final = 64
    CVDUsageHint: Final = 64
    CVD_animation_type: Final = 128
    CVDAnimationType: Final = 128
    MN_composite_only: Final = 1
    MNCompositeOnly: Final = 1
    MN_avoid_animated: Final = 2
    MNAvoidAnimated: Final = 2
    MN_avoid_dynamic: Final = 4
    MNAvoidDynamic: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, gsg: GraphicsStateGuardianBase = ...) -> None: ...
    @overload
    def __init__(self, __param0: SceneGraphReducer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_gsg(self, gsg: GraphicsStateGuardianBase) -> None:
        """Specifies the particular GraphicsStateGuardian that this object will
        attempt to optimize to.  The GSG may specify parameters such as maximum
        number of vertices per vertex data, max number of vertices per primitive,
        and whether triangle strips are preferred.  It also affects the types of
        vertex column data that is created by premunge().
        """
    def clear_gsg(self) -> None:
        """Specifies that no particular GraphicsStateGuardian will be used to guide
        the optimization.  The SceneGraphReducer will instead use config variables
        such as max-collect-vertices and max-collect-indices.
        """
    def get_gsg(self) -> GraphicsStateGuardianBase:
        """Returns the particular GraphicsStateGuardian that this object will attempt
        to optimize to.  See set_gsg().
        """
    def set_combine_radius(self, combine_radius: float) -> None:
        """Specifies the radius that is used in conjunction with CS_within_radius to
        decide whether a subgraph's siblings should be combined into a single node
        or not.

        If the CS_within_radius bit is included in the combine_siblings_bits
        parameter passed to flatten, than any nodes whose bounding volume is
        smaller than the indicated radius will be combined together (as if CS_other
        were set).
        """
    def get_combine_radius(self) -> float:
        """Returns the radius that is used in conjunction with CS_within_radius.  See
        set_combine_radius().
        """
    def apply_attribs(self, node: PandaNode, attrib_types: int = ...) -> None:
        """Walks the scene graph, accumulating attribs of the indicated types,
        applying them to the vertices, and removing them from the scene graph.
        This has a performance optimization benefit in itself, but is especially
        useful to pave the way for a call to flatten() and greatly improve the
        effectiveness of the flattening operation.

        Multiply instanced geometry is duplicated before the attribs are applied.

        Of course, this operation does make certain dynamic operations impossible.
        """
    def flatten(self, root: PandaNode, combine_siblings_bits: int) -> int:
        """Simplifies the graph by removing unnecessary nodes and nodes.

        In general, a node (and its parent node) is a candidate for removal if the
        node has no siblings and the node has no special properties.

        If combine_siblings_bits is nonzero, some sibling nodes (according to the
        bits set in combine_siblings_bits) may also be collapsed into a single
        node.  This will further reduce scene graph complexity, sometimes
        substantially, at the cost of reduced spatial separation.

        Returns the number of nodes removed from the graph.
        """
    def remove_column(self, root: PandaNode, column: InternalName | str) -> int:
        """Removes the indicated data column from any GeomVertexDatas found at the
        indicated root and below.  Returns the number of GeomNodes modified.
        """
    def make_compatible_state(self, root: PandaNode) -> int:
        """Searches for GeomNodes that contain multiple Geoms that differ only in
        their ColorAttribs.  If such a GeomNode is found, then all the colors are
        pushed down into the vertices.  This makes it feasible for the geoms to be
        unified later.
        """
    def make_compatible_format(self, root: PandaNode, collect_bits: int = ...) -> int:
        """Walks through the tree at this node and below and unifies the
        GeomVertexFormat for any GeomVertexData objects that are found, so that all
        eligible vdatas (according to collect_bits; see collect_vertex_data) will
        share the same vertex format.

        This will add unused columns where necessary to match formats.  It can
        result in suboptimal performance if used needlessly.

        There is usually no reason to call this explicitly, since
        collect_vertex_data() will do this anyway if it has not been done already.
        However, calling it ahead of time can make that future call to
        collect_vertex_data() run a little bit faster.

        The return value is the number of vertex datas modified.
        """
    def decompose(self, root: PandaNode) -> None:
        """Calls decompose() on every GeomNode at this level and below.

        There is usually no reason to call this explicitly, since unify() will do
        this anyway if it needs to be done.  However, calling it ahead of time can
        make that future call to unify() run a little bit faster.

        This operation has no effect if the config variable preserve-triangle-
        strips has been set true.
        """
    def collect_vertex_data(self, root: PandaNode, collect_bits: int = ...) -> int:
        """Collects all different GeomVertexData blocks that have compatible formats
        at this node and below into a single, unified block (or at least multiple
        larger blocks).  This is intended to reduce rendering overhead incurred by
        switching vertex buffers.  It can also make a subsequent call to unify()
        much more effective than it would have been otherwise.

        The set of bits passed in collect_bits indicates which properties are used
        to differentiate GeomVertexData blocks.  If it is 0, then more blocks will
        be combined together than if it is nonzero.
        """
    def make_nonindexed(self, root: PandaNode, nonindexed_bits: int = ...) -> int:
        """Converts indexed geometry to nonindexed geometry at the indicated node and
        below, by duplicating vertices where necessary.  The parameter
        nonindexed_bits is a union of bits defined in
        SceneGraphReducer::MakeNonindexed, which specifes which types of geometry
        to avoid making nonindexed.
        """
    def unify(self, root: PandaNode, preserve_order: bool) -> None:
        """Calls unify() on every GeomNode at this level and below.  This attempts to
        reduce the total number of individual Geoms and GeomPrimitives by combining
        these objects wherever possible.  See GeomNode::unify().
        """
    def remove_unused_vertices(self, root: PandaNode) -> None:
        """Removes any vertices in GeomVertexDatas that are no longer used at this
        level and below.  This requires remapping vertex indices in all of the
        GeomPrimitives, to remove holes in the GeomVertexDatas.  It is normally not
        necessary to call this explicitly.
        """
    def premunge(self, root: PandaNode, initial_state: RenderState) -> None:
        """Walks the scene graph rooted at this node and below, and uses the indicated
        GSG to premunge every Geom found to optimize it for eventual rendering on
        the indicated GSG.  If there is no GSG indicated for the SceneGraphReducer,
        this is a no-op.

        This operation will also apply to stashed children.
        """
    def check_live_flatten(self, node: PandaNode) -> bool:
        """In a non-release build, returns false if the node is correctly not in a
        live scene graph.  (Calling flatten on a node that is part of a live scene
        graph, for instance, a node somewhere under render, can cause problems in a
        multithreaded environment.)

        If allow_live_flatten is true, or in a release build, this always returns
        true.
        """
    setGsg = set_gsg
    clearGsg = clear_gsg
    getGsg = get_gsg
    setCombineRadius = set_combine_radius
    getCombineRadius = get_combine_radius
    applyAttribs = apply_attribs
    removeColumn = remove_column
    makeCompatibleState = make_compatible_state
    makeCompatibleFormat = make_compatible_format
    collectVertexData = collect_vertex_data
    makeNonindexed = make_nonindexed
    removeUnusedVertices = remove_unused_vertices
    checkLiveFlatten = check_live_flatten

class ParamNodePath(ParamValueBase):
    """A class object for storing a NodePath as a parameter."""

    def __init__(self, node_path: NodePath) -> None:
        """Creates a new ParamNodePath storing the given node path object."""
    def get_value(self) -> NodePath:
        """Retrieves the NodePath stored in the parameter."""
    getValue = get_value

class PortalNode(PandaNode):
    """A node in the scene graph that can hold a Portal Polygon, which is a
    rectangle.  Other types of polygons are not supported for now.  It also
    holds a PT(PandaNode) Cell that this portal is connected to
    """

    into_portal_mask: PortalMask
    from_portal_mask: PortalMask
    portal_geom: bool
    cell_in: NodePath
    cell_out: NodePath
    clip_plane: bool
    visible: bool
    max_depth: int
    open: bool
    @property
    def vertices(self) -> Sequence[LPoint3]: ...
    @overload
    def __init__(self, name: str) -> None:
        """`(self, name: str)`:
        Default constructor, just an empty node, no geo This is used to read portal
        from model.  You can also use this from python to create an empty portal.
        Then you can set the vertices yourself, with addVertex.

        `(self, name: str, pos: LPoint3, scale: float = ...)`:
        Create a default rectangle as portal.  Use this to create an arbitrary
        portal and setup from Python
        """
    @overload
    def __init__(self, name: str, pos: Vec3Like, scale: float = ...) -> None: ...
    def set_portal_mask(self, mask: PortalMask | int) -> None:
        """Simultaneously sets both the "from" and "into" PortalMask values to the
        same thing.
        """
    def set_from_portal_mask(self, mask: PortalMask | int) -> None:
        """Sets the "from" PortalMask.  In order for a portal to be detected from this
        object into another object, the intersection of this object's "from" mask
        and the other object's "into" mask must be nonzero.
        """
    def set_into_portal_mask(self, mask: PortalMask | int) -> None:
        """Sets the "into" PortalMask.  In order for a portal to be detected from
        another object into this object, the intersection of the other object's
        "from" mask and this object's "into" mask must be nonzero.
        """
    def get_from_portal_mask(self) -> PortalMask:
        """Returns the current "from" PortalMask.  In order for a portal to be
        detected from this object into another object, the intersection of this
        object's "from" mask and the other object's "into" mask must be nonzero.
        """
    def get_into_portal_mask(self) -> PortalMask:
        """Returns the current "into" PortalMask.  In order for a portal to be
        detected from another object into this object, the intersection of the
        other object's "from" mask and this object's "into" mask must be nonzero.
        """
    def set_portal_geom(self, flag: bool) -> None:
        """Sets the state of the "portal geom" flag for this PortalNode.  Normally,
        this is false; when this is set true, the PortalSolids in this node will
        test for portals with actual renderable geometry, in addition to whatever
        PortalSolids may be indicated by the from_portal_mask.

        Setting this to true causes this to test *all* GeomNodes for portals.  It
        is an all-or-none thing; there is no way to portal with only some
        GeomNodes, as GeomNodes have no into_portal_mask.
        """
    def get_portal_geom(self) -> bool:
        """Returns the current state of the portal_geom flag.  See set_portal_geom()."""
    def clear_vertices(self) -> None:
        """Resets the vertices of the portal to the empty list."""
    def add_vertex(self, vertex: Vec3Like) -> None:
        """Adds a new vertex to the portal polygon.  The vertices should be defined in
        a counterclockwise orientation when viewing through the portal.
        """
    def get_num_vertices(self) -> int:
        """Returns the number of vertices in the portal polygon."""
    def get_vertex(self, n: int) -> LPoint3:
        """Returns the nth vertex of the portal polygon."""
    def set_cell_in(self, cell: NodePath) -> None:
        """Sets the cell that this portal belongs to"""
    def get_cell_in(self) -> NodePath:
        """Sets the cell that this portal belongs to"""
    def set_cell_out(self, cell: NodePath) -> None:
        """Sets the cell that this portal leads out to"""
    def get_cell_out(self) -> NodePath:
        """Sets the cell that this portal leads out to"""
    def set_clip_plane(self, value: bool) -> None:
        """this is set if the portal will clip against its left and right planes"""
    def is_clip_plane(self) -> bool:
        """Is this portal clipping against its left-right planes"""
    def set_visible(self, value: bool) -> None:
        """this is set if the portal is facing camera"""
    def is_visible(self) -> bool:
        """Is this portal facing the camera"""
    def set_max_depth(self, value: int) -> None:
        """Set the maximum depth this portal will be visible at"""
    def get_max_depth(self) -> int:
        """Returns the maximum depth this portal will be visible at"""
    def set_open(self, value: bool) -> None:
        """Python sets this based on curent camera zone"""
    def is_open(self) -> bool:
        """Is this portal open from current camera zone"""
    def get_vertices(self) -> tuple[LPoint3, ...]: ...
    setPortalMask = set_portal_mask
    setFromPortalMask = set_from_portal_mask
    setIntoPortalMask = set_into_portal_mask
    getFromPortalMask = get_from_portal_mask
    getIntoPortalMask = get_into_portal_mask
    setPortalGeom = set_portal_geom
    getPortalGeom = get_portal_geom
    clearVertices = clear_vertices
    addVertex = add_vertex
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    setCellIn = set_cell_in
    getCellIn = get_cell_in
    setCellOut = set_cell_out
    getCellOut = get_cell_out
    setClipPlane = set_clip_plane
    isClipPlane = is_clip_plane
    setVisible = set_visible
    isVisible = is_visible
    setMaxDepth = set_max_depth
    getMaxDepth = get_max_depth
    setOpen = set_open
    isOpen = is_open
    getVertices = get_vertices

class ScissorAttrib(RenderAttrib):
    """This restricts rendering to within a rectangular region of the scene,
    without otherwise affecting the viewport or lens properties.  Geometry that
    falls outside the scissor region is not rendered.  It is akin to the OpenGL
    glScissor() function.

    The ScissorAttrib always specifies its region relative to its enclosing
    DisplayRegion, in screen space, and performs no culling.

    See ScissorEffect if you wish to define a region relative to 2-D or 3-D
    coordinates in the scene graph, with culling.
    """

    @property
    def frame(self) -> LVecBase4: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a new ScissorAttrib object that removes the scissor region and
        fills the DisplayRegion.
        """
    @overload
    @staticmethod
    def make(frame: Vec4Like) -> RenderAttrib:
        """Constructs a ScissorAttrib that restricts rendering to the indicated frame
        within the current DisplayRegion.  (0,0) is the lower-left corner of the
        DisplayRegion, and (1,1) is the upper-right corner.
        """
    @overload
    @staticmethod
    def make(left: float, right: float, bottom: float, top: float) -> RenderAttrib: ...
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def is_off(self) -> bool:
        """Returns true if the ScissorAttrib is an 'off' ScissorAttrib, indicating
        that scissor testing is disabled.
        """
    def get_frame(self) -> LVecBase4:
        """Returns the left, right, bottom, top coordinates of the scissor frame.
        This defines a frame within the current DisplayRegion, where 0,0 is the
        lower-left corner of the DisplayRegion, and 1,1 is the upper-right corner.
        """
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    isOff = is_off
    getFrame = get_frame
    getClassSlot = get_class_slot

class ShadeModelAttrib(RenderAttrib):
    """Specifies whether flat shading (per-polygon) or smooth shading (per-vertex)
    is in effect.
    """

    M_flat: Final = 0
    MFlat: Final = 0
    M_smooth: Final = 1
    MSmooth: Final = 1
    @property
    def mode(self) -> _ShadeModelAttrib_Mode: ...
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make(mode: _ShadeModelAttrib_Mode) -> RenderAttrib:
        """Constructs a new ShadeModelAttrib object that specifies whether to draw
        polygons with flat shading or with per-vertex (smooth) shading.
        """
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    def get_mode(self) -> _ShadeModelAttrib_Mode:
        """Returns the shade mode."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeDefault = make_default
    getMode = get_mode
    getClassSlot = get_class_slot

class StencilAttrib(RenderAttrib):
    """A StencilAttrib is a collection of all stencil render states.  The render
    states in a StencilAttrib are read-only.  A StencilAttrib is created with
    make or make_2_sided.  To determine if two sided stencil is supported, call
    the function GraphicsStateGuardian:: get_supports_two_sided_stencil.
    """

    SRS_front_comparison_function: Final = 0
    SRSFrontComparisonFunction: Final = 0
    SRS_front_stencil_fail_operation: Final = 1
    SRSFrontStencilFailOperation: Final = 1
    SRS_front_stencil_pass_z_fail_operation: Final = 2
    SRSFrontStencilPassZFailOperation: Final = 2
    SRS_front_stencil_pass_z_pass_operation: Final = 3
    SRSFrontStencilPassZPassOperation: Final = 3
    SRS_reference: Final = 4
    SRSReference: Final = 4
    SRS_read_mask: Final = 5
    SRSReadMask: Final = 5
    SRS_write_mask: Final = 6
    SRSWriteMask: Final = 6
    SRS_back_comparison_function: Final = 7
    SRSBackComparisonFunction: Final = 7
    SRS_back_stencil_fail_operation: Final = 8
    SRSBackStencilFailOperation: Final = 8
    SRS_back_stencil_pass_z_fail_operation: Final = 9
    SRSBackStencilPassZFailOperation: Final = 9
    SRS_back_stencil_pass_z_pass_operation: Final = 10
    SRSBackStencilPassZPassOperation: Final = 10
    SRS_clear: Final = 11
    SRSClear: Final = 11
    SRS_clear_value: Final = 12
    SRSClearValue: Final = 12
    SRS_total: Final = 13
    SRSTotal: Final = 13
    SCF_never: Final = 1
    SCFNever: Final = 1
    SCF_less_than: Final = 2
    SCFLessThan: Final = 2
    SCF_equal: Final = 3
    SCFEqual: Final = 3
    SCF_less_than_or_equal: Final = 4
    SCFLessThanOrEqual: Final = 4
    SCF_greater_than: Final = 5
    SCFGreaterThan: Final = 5
    SCF_not_equal: Final = 6
    SCFNotEqual: Final = 6
    SCF_greater_than_or_equal: Final = 7
    SCFGreaterThanOrEqual: Final = 7
    SCF_always: Final = 8
    SCFAlways: Final = 8
    SO_keep: Final = 0
    SOKeep: Final = 0
    SO_zero: Final = 1
    SOZero: Final = 1
    SO_replace: Final = 2
    SOReplace: Final = 2
    SO_increment: Final = 3
    SOIncrement: Final = 3
    SO_decrement: Final = 4
    SODecrement: Final = 4
    SO_invert: Final = 5
    SOInvert: Final = 5
    SO_increment_saturate: Final = 6
    SOIncrementSaturate: Final = 6
    SO_decrement_saturate: Final = 7
    SODecrementSaturate: Final = 7
    @property
    def class_slot(self) -> int: ...
    @staticmethod
    def make_off() -> RenderAttrib:
        """Constructs a StencilAttrib that has stenciling turned off."""
    @staticmethod
    def make_default() -> RenderAttrib:
        """Returns a RenderAttrib that corresponds to whatever the standard default
        properties for render attributes of this type ought to be.
        """
    @staticmethod
    def make(
        front_enable: bool,
        front_comparison_function: _RenderAttrib_PandaCompareFunc,
        stencil_fail_operation: _StencilAttrib_StencilOperation,
        stencil_pass_z_fail_operation: _StencilAttrib_StencilOperation,
        front_stencil_pass_z_pass_operation: _StencilAttrib_StencilOperation,
        reference: int,
        read_mask: int,
        write_mask: int = ...,
    ) -> RenderAttrib:
        """Constructs a front face StencilAttrib."""
    @staticmethod
    def make_2_sided(
        front_enable: bool,
        back_enable: bool,
        front_comparison_function: _RenderAttrib_PandaCompareFunc,
        stencil_fail_operation: _StencilAttrib_StencilOperation,
        stencil_pass_z_fail_operation: _StencilAttrib_StencilOperation,
        front_stencil_pass_z_pass_operation: _StencilAttrib_StencilOperation,
        reference: int,
        read_mask: int,
        write_mask: int,
        back_comparison_function: _RenderAttrib_PandaCompareFunc,
        back_stencil_fail_operation: _StencilAttrib_StencilOperation,
        back_stencil_pass_z_fail_operation: _StencilAttrib_StencilOperation,
        back_stencil_pass_z_pass_operation: _StencilAttrib_StencilOperation,
    ) -> RenderAttrib:
        """Constructs a two-sided StencilAttrib."""
    @staticmethod
    def make_with_clear(
        front_enable: bool,
        front_comparison_function: _RenderAttrib_PandaCompareFunc,
        stencil_fail_operation: _StencilAttrib_StencilOperation,
        stencil_pass_z_fail_operation: _StencilAttrib_StencilOperation,
        front_stencil_pass_z_pass_operation: _StencilAttrib_StencilOperation,
        reference: int,
        read_mask: int,
        write_mask: int,
        clear: bool,
        clear_value: int,
    ) -> RenderAttrib:
        """Constructs a front face StencilAttrib."""
    @staticmethod
    def make_2_sided_with_clear(
        front_enable: bool,
        back_enable: bool,
        front_comparison_function: _RenderAttrib_PandaCompareFunc,
        stencil_fail_operation: _StencilAttrib_StencilOperation,
        stencil_pass_z_fail_operation: _StencilAttrib_StencilOperation,
        front_stencil_pass_z_pass_operation: _StencilAttrib_StencilOperation,
        reference: int,
        read_mask: int,
        write_mask: int,
        back_comparison_function: _RenderAttrib_PandaCompareFunc,
        back_stencil_fail_operation: _StencilAttrib_StencilOperation,
        back_stencil_pass_z_fail_operation: _StencilAttrib_StencilOperation,
        back_stencil_pass_z_pass_operation: _StencilAttrib_StencilOperation,
        clear: bool,
        clear_value: int,
    ) -> RenderAttrib:
        """Constructs a two-sided StencilAttrib."""
    def get_render_state(self, render_state_identifier: _StencilAttrib_StencilRenderState) -> int:
        """Returns render state."""
    @staticmethod
    def get_class_slot() -> int: ...
    makeOff = make_off
    makeDefault = make_default
    make2Sided = make_2_sided
    makeWithClear = make_with_clear
    make2SidedWithClear = make_2_sided_with_clear
    getRenderState = get_render_state
    getClassSlot = get_class_slot

class ShaderPool:
    """This is the preferred interface for loading shaders for the TextNode
    system.  It is similar to ModelPool and TexturePool in that it unifies
    references to the same filename.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def has_shader(filename: StrOrBytesPath) -> bool:
        """Returns true if the shader has ever been loaded, false otherwise."""
    @staticmethod
    def verify_shader(filename: StrOrBytesPath) -> bool:
        """Loads the given filename up into a shader, if it has not already been
        loaded, and returns true to indicate success, or false to indicate failure.
        If this returns true, it is guaranteed that a subsequent call to
        load_shader() with the same shader name will return a valid Shader pointer.
        """
    @staticmethod
    def load_shader(filename: StrOrBytesPath) -> Shader:
        """Loads the given filename up into a shader, if it has not already been
        loaded, and returns the new shader.  If a shader with the same filename was
        previously loaded, returns that one instead.  If the shader file cannot be
        found, returns NULL.
        """
    @staticmethod
    def add_shader(filename: StrOrBytesPath, shader: Shader) -> None:
        """Adds the indicated already-loaded shader to the pool.  The shader will
        always replace any previously-loaded shader in the pool that had the same
        filename.
        """
    @staticmethod
    def release_shader(filename: StrOrBytesPath) -> None:
        """Removes the indicated shader from the pool, indicating it will never be
        loaded again; the shader may then be freed.  If this function is never
        called, a reference count will be maintained on every shader every loaded,
        and shaders will never be freed.
        """
    @staticmethod
    def release_all_shaders() -> None:
        """Releases all shaders in the pool and restores the pool to the empty state."""
    @staticmethod
    def garbage_collect() -> int:
        """Releases only those shaders in the pool that have a reference count of
        exactly 1; i.e.  only those shaders that are not being used outside of the
        pool.  Returns the number of shaders released.
        """
    @staticmethod
    def list_contents(out: ostream) -> None:
        """Lists the contents of the shader pool to the indicated output stream."""
    @staticmethod
    def write(out: ostream) -> None:
        """Lists the contents of the shader pool to the indicated output stream."""
    hasShader = has_shader
    verifyShader = verify_shader
    loadShader = load_shader
    addShader = add_shader
    releaseShader = release_shader
    releaseAllShaders = release_all_shaders
    garbageCollect = garbage_collect
    listContents = list_contents

def py_decode_NodePath_from_bam_stream(data: bytes) -> NodePath: ...
def py_decode_NodePath_from_bam_stream_persist(unpickler, data: bytes) -> NodePath: ...

pyDecodeNodePathFromBamStream = py_decode_NodePath_from_bam_stream
pyDecodeNodePathFromBamStreamPersist = py_decode_NodePath_from_bam_stream_persist
