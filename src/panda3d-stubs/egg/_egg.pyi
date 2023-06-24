from _typeshed import StrOrBytesPath
from collections.abc import Iterator, MutableSequence, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import DoubleMat4Like, DoubleVec2Like, DoubleVec3Like, DoubleVec4Like, SearchPathLike, Vec4Like
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import Filename, GlobPattern, istream, ostream
from panda3d.core._express import Namable, TypedReferenceCount
from panda3d.core._linmath import (
    LColor,
    LMatrix3d,
    LMatrix4d,
    LNormald,
    LPoint2d,
    LPoint3d,
    LPoint4d,
    LTexCoord3d,
    LTexCoordd,
    LVecBase2d,
    LVecBase3d,
    LVecBase4d,
    LVertexd,
)
from panda3d.core._putil import BamCacheRecord, CollideMask

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_EggRenderMode_AlphaMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_EggRenderMode_DepthWriteMode: TypeAlias = Literal[0, 1, 2]
_EggRenderMode_DepthTestMode: TypeAlias = Literal[0, 1, 2]
_EggRenderMode_VisibilityMode: TypeAlias = Literal[0, 1, 2]
_EggTransform_ComponentType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
_EggGroup_GroupType: TypeAlias = Literal[-1, 0, 1, 2]
_EggGroup_BillboardType: TypeAlias = Literal[0, 32, 64, 128]
_EggGroup_CollisionSolidType: TypeAlias = Literal[0, 65536, 131072, 196608, 262144, 327680, 393216, 458752, 524288]
_EggGroup_CollideFlags: TypeAlias = Literal[0, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728]
_EggGroup_DCSType: TypeAlias = Literal[0, 16, 32, 48, 64, 80]
_EggGroup_DartType: TypeAlias = Literal[0, 268435456, 536870912, 805306368, 1073741824]
_EggGroup_BlendMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_EggGroup_BlendOperand: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
_EggTexture_TextureType: TypeAlias = Literal[0, 1, 2, 3, 4]
_EggTexture_Format: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
_EggTexture_CompressionMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_EggTexture_WrapMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_EggTexture_FilterType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_EggTexture_EnvType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_EggTexture_TexGen: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_EggTexture_QualityLevel: TypeAlias = Literal[0, 1, 2, 3, 4]
_EggTexture_CombineChannel: TypeAlias = Literal[0, 1, 2]
_EggTexture_CombineMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
_EggTexture_CombineSource: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_EggTexture_CombineOperand: TypeAlias = Literal[0, 1, 2, 3, 4]
_EggPrimitive_Shading: TypeAlias = Literal[0, 1, 2, 3]
_EggCurve_CurveType: TypeAlias = Literal[0, 1, 2, 3]
_EggTable_TableType: TypeAlias = Literal[0, 1, 2]

class EggUserData(TypedReferenceCount):
    """This is a base class for a user-defined data type to extend egg structures
    in processing code.  The user of the egg library may derive from
    EggUserData to associate any arbitrary data with various egg objects.

    However, this data will not be written out to the disk when the egg file is
    written; it is an in-memory object only.
    """

    def __init__(self, copy: EggUserData = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...

class EggObject(TypedReferenceCount):
    """The highest-level base class in the egg directory.  (Almost) all things egg
    inherit from this.
    """

    def __init__(self, copy: EggObject = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def set_user_data(self, user_data: EggUserData) -> None:
        """Sets the user data associated with this object.  This may be any
        EggUserData-derived object.  The egg library will do nothing with this
        pointer, except to hold its reference count and return the pointer on
        request.

        The EggObject maintains multiple different EggUserData pointers, one for
        each unique type (as reported by get_type()).  If you know that only one
        type of EggUserData object will be added in your application, you may use
        the query functions that accept no parameters, but it is recommended that
        in general you pass in the type of your particular user data, to allow
        multiple applications to coexist in the same egg data.

        This pointer is also copied by the copy assignment operator and copy
        constructor.
        """
    def get_user_data(self, type: TypeHandle | type = ...) -> EggUserData:
        """`(self)`:
        Returns the user data pointer most recently stored on this object, or NULL
        if nothing was previously stored.

        `(self, type: TypeHandle)`:
        Returns the user data pointer of the indicated type, if it exists, or NULL
        if it does not.
        """
    def has_user_data(self, type: TypeHandle | type = ...) -> bool:
        """`(self)`:
        Returns true if a generic user data pointer has recently been set and not
        yet cleared, false otherwise.

        `(self, type: TypeHandle)`:
        Returns true if the user data pointer of the indicated type has been set,
        false otherwise.
        """
    def clear_user_data(self, type: TypeHandle | type = ...) -> None:
        """`(self)`:
        Removes *all* user data pointers from the node.

        `(self, type: TypeHandle)`:
        Removes the user data pointer of the indicated type.
        """
    setUserData = set_user_data
    getUserData = get_user_data
    hasUserData = has_user_data
    clearUserData = clear_user_data

class EggNamedObject(EggObject, Namable):  # type: ignore[misc]
    """This is a fairly low-level base class--any egg object that has a name."""

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggNamedObject) -> None: ...
    def upcast_to_EggObject(self) -> EggObject: ...
    def upcast_to_Namable(self) -> Namable: ...
    upcastToEggObject = upcast_to_EggObject
    upcastToNamable = upcast_to_Namable

class EggNode(EggNamedObject):
    """A base class for things that may be directly added into the egg hierarchy.
    This includes groups, joints, polygons, vertex pools, etc., but does not
    include things like vertices.
    """

    @property
    def parent(self) -> EggGroupNode: ...
    @property
    def depth(self) -> int: ...
    def get_parent(self) -> EggGroupNode: ...
    def get_depth(self) -> int:
        """Returns the number of nodes above this node in the egg hierarchy."""
    def is_under_instance(self) -> bool:
        """Returns true if there is an <Instance> node somewhere in the egg tree at or
        above this node, false otherwise.
        """
    def is_under_transform(self) -> bool:
        """Returns true if there is a <Transform> entry somewhere in the egg tree at
        or above this node, false otherwise.
        """
    def is_local_coord(self) -> bool:
        """Returns true if this node's vertices are not in the global coordinate
        space.  This will be the case if there was an <Instance> node under a
        transform at or above this node.
        """
    def get_vertex_frame(self) -> LMatrix4d:
        """Returns the coordinate frame of the vertices referenced by primitives at or
        under this node.  This is not the same as get_node_frame().

        Generally, vertices in an egg file are stored in the global coordinate
        space, regardless of the transforms defined at each node.  Thus,
        get_vertex_frame() will usually return the identity transform (global
        coordinate space).  However, primitives under an <Instance> entry reference
        their vertices in the coordinate system under effect at the time of the
        <Instance>.  Thus, nodes under an <Instance> entry may return this non-
        identity matrix.

        Specifically, this may return a non-identity matrix only if
        is_local_coord() is true.
        """
    def get_node_frame(self) -> LMatrix4d:
        """Returns the coordinate frame of the node itself.  This is simply the net
        product of all transformations up to the root.
        """
    def get_vertex_frame_inv(self) -> LMatrix4d:
        """Returns the inverse of the matrix returned by get_vertex_frame().  See
        get_vertex_frame().
        """
    def get_node_frame_inv(self) -> LMatrix4d:
        """Returns the inverse of the matrix returned by get_node_frame().  See
        get_node_frame().
        """
    def get_vertex_to_node(self) -> LMatrix4d:
        """Returns the transformation matrix suitable for converting the vertices as
        read from the egg file into the coordinate space of the node.  This is the
        same thing as:

        get_vertex_frame() * get_node_frame_inv()
        """
    def get_node_to_vertex(self) -> LMatrix4d:
        """Returns the transformation matrix suitable for converting vertices in the
        coordinate space of the node to the appropriate coordinate space for
        storing in the egg file.  This is the same thing as:

        get_node_frame() * get_vertex_frame_inv()
        """
    def get_vertex_frame_ptr(self) -> LMatrix4d:
        """Returns either a NULL pointer or a unique pointer shared by nodes with the
        same get_vertex_frame() matrix.
        """
    def get_node_frame_ptr(self) -> LMatrix4d:
        """Returns either a NULL pointer or a unique pointer shared by nodes with the
        same get_node_frame() matrix.
        """
    def get_vertex_frame_inv_ptr(self) -> LMatrix4d:
        """Returns either a NULL pointer or a unique pointer shared by nodes with the
        same get_vertex_frame_inv() matrix.
        """
    def get_node_frame_inv_ptr(self) -> LMatrix4d:
        """Returns either a NULL pointer or a unique pointer shared by nodes with the
        same get_node_frame_inv() matrix.
        """
    def get_vertex_to_node_ptr(self) -> LMatrix4d:
        """Returns either a NULL pointer or a unique pointer shared by nodes with the
        same get_vertex_to_node() matrix.
        """
    def get_node_to_vertex_ptr(self) -> LMatrix4d:
        """Returns either a NULL pointer or a unique pointer shared by nodes with the
        same get_node_to_vertex() matrix.
        """
    def transform(self, mat: DoubleMat4Like) -> None:
        """Applies the indicated transformation to the node and all of its
        descendants.
        """
    def transform_vertices_only(self, mat: DoubleMat4Like) -> None:
        """Applies the indicated transformation only to vertices that appear in global
        space within vertex pools at this node and below.  Joints and other
        transforms are not affected, nor are local vertices.
        """
    def flatten_transforms(self) -> None:
        """Removes any transform and instance records from this node in the scene
        graph and below.  If an instance node is encountered, removes the instance
        and applies the transform to its vertices, duplicating vertices if
        necessary.

        Since this function may result in duplicated vertices, it may be a good
        idea to call remove_unused_vertices() after calling this.
        """
    def apply_texmats(self) -> None:
        """Applies the texture matrices to the UV's of the vertices that reference
        them, and then removes the texture matrices from the textures themselves.
        """
    def is_joint(self) -> bool:
        """Returns true if this particular node represents a <Joint> entry or not.
        This is a handy thing to know since Joints are sorted to the end of their
        sibling list when writing an egg file.  See EggGroupNode::write().
        """
    def is_anim_matrix(self) -> bool:
        """Returns true if this node represents a table of animation transformation
        data, false otherwise.
        """
    def determine_alpha_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has an alpha_mode
        other than AM_unspecified.  Returns a valid EggRenderMode pointer if one is
        found, or NULL otherwise.
        """
    def determine_depth_write_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has a
        depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_depth_test_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has a
        depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_visibility_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has a
        visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_depth_offset(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has a depth_offset
        specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
        otherwise.
        """
    def determine_draw_order(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has a draw_order
        specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
        otherwise.
        """
    def determine_bin(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this node that has a bin specified.
        Returns a valid EggRenderMode pointer if one is found, or NULL otherwise.
        """
    def determine_indexed(self) -> bool:
        """Walks back up the hierarchy, looking for an EggGroup at this level or above
        that has the "indexed" scalar set.  Returns the value of the indexed scalar
        if it is found, or false if it is not.

        In other words, returns true if the "indexed" flag is in effect for the
        indicated node, false otherwise.
        """
    def determine_decal(self) -> bool:
        """Walks back up the hierarchy, looking for an EggGroup at this level or above
        that has the "decal" flag set.  Returns the value of the decal flag if it
        is found, or false if it is not.

        In other words, returns true if the "decal" flag is in effect for the
        indicated node, false otherwise.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    def parse_egg(self, egg_syntax: str) -> bool:
        """Parses the egg syntax given in the indicate string as if it had been read
        from the egg file within this object's definition.  Updates the object
        accordingly.  Returns true if successful, false if there was some parse
        error or if the object does not support this functionality.
        """
    def test_under_integrity(self) -> None: ...
    getParent = get_parent
    getDepth = get_depth
    isUnderInstance = is_under_instance
    isUnderTransform = is_under_transform
    isLocalCoord = is_local_coord
    getVertexFrame = get_vertex_frame
    getNodeFrame = get_node_frame
    getVertexFrameInv = get_vertex_frame_inv
    getNodeFrameInv = get_node_frame_inv
    getVertexToNode = get_vertex_to_node
    getNodeToVertex = get_node_to_vertex
    getVertexFramePtr = get_vertex_frame_ptr
    getNodeFramePtr = get_node_frame_ptr
    getVertexFrameInvPtr = get_vertex_frame_inv_ptr
    getNodeFrameInvPtr = get_node_frame_inv_ptr
    getVertexToNodePtr = get_vertex_to_node_ptr
    getNodeToVertexPtr = get_node_to_vertex_ptr
    transformVerticesOnly = transform_vertices_only
    flattenTransforms = flatten_transforms
    applyTexmats = apply_texmats
    isJoint = is_joint
    isAnimMatrix = is_anim_matrix
    determineAlphaMode = determine_alpha_mode
    determineDepthWriteMode = determine_depth_write_mode
    determineDepthTestMode = determine_depth_test_mode
    determineVisibilityMode = determine_visibility_mode
    determineDepthOffset = determine_depth_offset
    determineDrawOrder = determine_draw_order
    determineBin = determine_bin
    determineIndexed = determine_indexed
    determineDecal = determine_decal
    parseEgg = parse_egg
    testUnderIntegrity = test_under_integrity

class EggGroupNode(EggNode):
    """A base class for nodes in the hierarchy that are not leaf nodes.  (See also
    EggGroup, which is specifically the "<Group>" node in egg.)

    An EggGroupNode is an STL-style container of pointers to EggNodes, like a
    vector.  Functions push_back()/pop_back() and insert()/erase() are provided
    to manipulate the list.  The list may also be operated on (read-only) via
    iterators and begin()/end().
    """

    T_polygon: Final = 1
    TPolygon: Final = 1
    T_convex: Final = 2
    TConvex: Final = 2
    T_composite: Final = 4
    TComposite: Final = 4
    T_recurse: Final = 8
    TRecurse: Final = 8
    T_flat_shaded: Final = 16
    TFlatShaded: Final = 16
    @property
    def children(self) -> list[EggNode]: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggGroupNode) -> None: ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...
    def clear(self) -> None: ...
    def get_first_child(self) -> EggNode:
        """Returns the first child in the group's list of children, or NULL if the
        list of children is empty.  Can be used with get_next_child() to return the
        complete list of children without using the iterator class; however, this
        is non-thread-safe, and so is not recommended except for languages other
        than C++ which cannot use the iterators.
        """
    def get_next_child(self) -> EggNode:
        """Returns the next child in the group's list of children since the last call
        to get_first_child() or get_next_child(), or NULL if the last child has
        been returned.  Can be used with get_first_child() to return the complete
        list of children without using the iterator class; however, this is non-
        thread-safe, and so is not recommended except for languages other than C++
        which cannot use the iterators.

        It is an error to call this without previously calling get_first_child().
        """
    def get_children(self) -> list[EggNode]: ...
    def add_child(self, node: EggNode) -> EggNode:
        """Adds the indicated child to the group and returns it.  If the child node is
        already a child of some other node, removes it first.
        """
    def remove_child(self, node: EggNode) -> EggNode:
        """Removes the indicated child node from the group and returns it.  If the
        child was not already in the group, does nothing and returns NULL.
        """
    def steal_children(self, other: EggGroupNode) -> None:
        """Moves all the children from the other node to this one.  This is especially
        useful because the group node copy assignment operator does not copy
        children.
        """
    def find_child(self, name: str) -> EggNode:
        """Returns the child of this node whose name is the indicated string, or NULL
        if there is no child of this node by that name.  Does not search
        recursively.
        """
    def has_absolute_pathnames(self) -> bool:
        """Returns true if any nodes at this level and below include a reference to a
        file via an absolute pathname, or false if all references are relative.
        """
    def resolve_filenames(self, searchpath: SearchPathLike) -> None:
        """Walks the tree and attempts to resolve any filenames encountered.  This
        looks up filenames along the specified search path; it does not
        automatically search the model_path for missing files.
        """
    def force_filenames(self, directory: StrOrBytesPath) -> None:
        """Similar to resolve_filenames, but each non-absolute filename encountered is
        arbitrarily taken to be in the indicated directory, whether or not the so-
        named filename exists.
        """
    def reverse_vertex_ordering(self) -> None:
        """Reverses the vertex ordering of all polygons defined at this node and
        below.  Does not change the surface normals, if any.
        """
    def recompute_vertex_normals(self, threshold: float, cs: _CoordinateSystem = ...) -> None:
        """Recomputes all the vertex normals for polygon geometry at this group node
        and below so that they accurately reflect the vertex positions.  A shared
        edge between two polygons (even in different groups) is considered smooth
        if the angle between the two edges is less than threshold degrees.

        This function also removes degenerate polygons that do not have enough
        vertices to define a normal.  It does not affect normals for other kinds of
        primitives like Nurbs or Points.

        This function does not remove or adjust vertices in the vertex pool; it
        only adds new vertices with the correct normals.  Thus, it is a good idea
        to call remove_unused_vertices() after calling this.
        """
    def recompute_polygon_normals(self, cs: _CoordinateSystem = ...) -> None:
        """Recomputes all the polygon normals for polygon geometry at this group node
        and below so that they accurately reflect the vertex positions.  Normals
        are removed from the vertices and defined only on polygons, giving the
        geometry a faceted appearance.

        This function also removes degenerate polygons that do not have enough
        vertices to define a normal.  It does not affect normals for other kinds of
        primitives like Nurbs or Points.

        This function does not remove or adjust vertices in the vertex pool; it
        only adds new vertices with the normals removed.  Thus, it is a good idea
        to call remove_unused_vertices() after calling this.
        """
    def strip_normals(self) -> None:
        """Removes all normals from primitives, and the vertices they reference, at
        this node and below.

        This function does not remove or adjust vertices in the vertex pool; it
        only adds new vertices with the normal removed.  Thus, it is a good idea to
        call remove_unused_vertices() after calling this.
        """
    def recompute_tangent_binormal(self, uv_name: GlobPattern | str) -> bool:
        """This function recomputes the tangent and binormal for the named texture
        coordinate set for all vertices at this level and below.  Use the empty
        string for the default texture coordinate set.

        It is necessary for each vertex to already have a normal (or at least a
        polygon normal), as well as a texture coordinate in the named texture
        coordinate set, before calling this function.  You might precede this with
        recompute_vertex_normals() to ensure that the normals exist.

        Like recompute_vertex_normals(), this function does not remove or adjust
        vertices in the vertex pool; it only adds new vertices with the new
        tangents and binormals computed.  Thus, it is a good idea to call
        remove_unused_vertices() after calling this.
        """
    def recompute_tangent_binormal_auto(self) -> bool:
        """This function recomputes the tangent and binormal for any texture
        coordinate set that affects a normal map.  Returns true if anything was
        done.
        """
    def triangulate_polygons(self, flags: int) -> int:
        """Replace all higher-order polygons at this point in the scene graph and
        below with triangles.  Returns the total number of new triangles produced,
        less degenerate polygons removed.

        If flags contains T_polygon and T_convex, both concave and convex polygons
        will be subdivided into triangles; with only T_polygon, only concave
        polygons will be subdivided, and convex polygons will be largely unchanged.
        """
    def mesh_triangles(self, flags: int) -> None:
        """Combine triangles together into triangle strips, at this group and below."""
    def make_point_primitives(self) -> None:
        """Creates PointLight primitives to reference any otherwise unreferences
        vertices discovered in this group or below.
        """
    def remove_unused_vertices(self, recurse: bool) -> int:
        """Removes all vertices from VertexPools within this group or below that are
        not referenced by at least one primitive.  Also collapses together
        equivalent vertices, and renumbers all vertices after the operation so
        their indices are consecutive, beginning at zero.  Returns the total number
        of vertices removed.

        Note that this operates on the VertexPools within this group level, without
        respect to primitives that reference these vertices (unlike other functions
        like strip_normals()).  It is therefore most useful to call this on the
        EggData root, rather than on a subgroup within the hierarchy, since a
        VertexPool may appear anywhere in the hierarchy.
        """
    def remove_invalid_primitives(self, recurse: bool) -> int:
        """Removes primitives at this level and below which appear to be degenerate;
        e.g.  polygons with fewer than 3 vertices, etc.  Returns the number of
        primitives removed.
        """
    def clear_connected_shading(self) -> None:
        """Resets the connected_shading information on all primitives at this node and
        below, so that it may be accurately rederived by the next call to
        get_connected_shading().

        It may be a good idea to call remove_unused_vertices() as well, to
        establish the correct connectivity between common vertices.
        """
    def get_connected_shading(self) -> None:
        """Queries the connected_shading information on all primitives at this node
        and below, to ensure that it has been completely filled in before we start
        mucking around with vertices.
        """
    def unify_attributes(self, use_connected_shading: bool, allow_per_primitive: bool, recurse: bool) -> None:
        """Applies per-vertex normal and color to all vertices, if they are in fact
        per-vertex (and different for each vertex), or moves them to the primitive
        if they are all the same.

        After this call, either the primitive will have normals or its vertices
        will, but not both.  Ditto for colors.

        If use_connected_shading is true, each polygon is considered in conjunction
        with all connected polygons; otherwise, each polygon is considered
        individually.

        If allow_per_primitive is false, S_per_face or S_overall will treated like
        S_per_vertex: normals and colors will always be assigned to the vertices.
        In this case, there will never be per-primitive colors or normals after
        this call returns.  On the other hand, if allow_per_primitive is true, then
        S_per_face means that normals and colors should be assigned to the
        primitives, and removed from the vertices, as described above.

        This may create redundant vertices in the vertex pool, so it may be a good
        idea to follow this up with remove_unused_vertices().
        """
    def apply_last_attribute(self, recurse: bool) -> None:
        """Sets the last vertex of the triangle (or each component) to the primitive
        normal and/or color, if the primitive is flat-shaded.  This reflects the
        OpenGL convention of storing flat-shaded properties on the last vertex,
        although it is not usually a convention in Egg.

        This may create redundant vertices in the vertex pool, so it may be a good
        idea to follow this up with remove_unused_vertices().
        """
    def apply_first_attribute(self, recurse: bool) -> None:
        """Sets the first vertex of the triangle (or each component) to the primitive
        normal and/or color, if the primitive is flat-shaded.  This reflects the
        DirectX convention of storing flat-shaded properties on the first vertex,
        although it is not usually a convention in Egg.

        This may create redundant vertices in the vertex pool, so it may be a good
        idea to follow this up with remove_unused_vertices().
        """
    def post_apply_flat_attribute(self, recurse: bool) -> None:
        """Intended as a followup to apply_last_attribute(), this also sets an
        attribute on the first vertices of the primitive, if they don't already
        have an attribute set, just so they end up with *something*.
        """
    def has_primitives(self) -> bool:
        """Returns true if there are any primitives (e.g.  polygons) defined within
        this group or below, false otherwise.
        """
    def joint_has_primitives(self) -> bool:
        """Returns true if there are any primitives (e.g.  polygons) defined within
        this group or below, but the search does not include nested joints.
        """
    def has_normals(self) -> bool:
        """Returns true if any of the primitives (e.g.  polygons) defined within this
        group or below have either face or vertex normals defined, false otherwise.
        """
    @staticmethod
    def is_right(v1: DoubleVec2Like, v2: DoubleVec2Like) -> bool:
        """Returns true if the 2-d v1 is to the right of v2."""
    getFirstChild = get_first_child
    getNextChild = get_next_child
    getChildren = get_children
    addChild = add_child
    removeChild = remove_child
    stealChildren = steal_children
    findChild = find_child
    hasAbsolutePathnames = has_absolute_pathnames
    resolveFilenames = resolve_filenames
    forceFilenames = force_filenames
    reverseVertexOrdering = reverse_vertex_ordering
    recomputeVertexNormals = recompute_vertex_normals
    recomputePolygonNormals = recompute_polygon_normals
    stripNormals = strip_normals
    recomputeTangentBinormal = recompute_tangent_binormal
    recomputeTangentBinormalAuto = recompute_tangent_binormal_auto
    triangulatePolygons = triangulate_polygons
    meshTriangles = mesh_triangles
    makePointPrimitives = make_point_primitives
    removeUnusedVertices = remove_unused_vertices
    removeInvalidPrimitives = remove_invalid_primitives
    clearConnectedShading = clear_connected_shading
    getConnectedShading = get_connected_shading
    unifyAttributes = unify_attributes
    applyLastAttribute = apply_last_attribute
    applyFirstAttribute = apply_first_attribute
    postApplyFlatAttribute = post_apply_flat_attribute
    hasPrimitives = has_primitives
    jointHasPrimitives = joint_has_primitives
    hasNormals = has_normals
    isRight = is_right

class EggAnimData(EggNode):
    """A base class for EggSAnimData and EggXfmAnimData, which contain rows and
    columns of numbers.
    """

    def set_fps(self, type: float) -> None: ...
    def clear_fps(self) -> None: ...
    def has_fps(self) -> bool: ...
    def get_fps(self) -> float:
        """This is only valid if has_fps() returns true."""
    def clear_data(self) -> None:
        """Removes all data and empties the table."""
    def add_data(self, value: float) -> None:
        """Adds a single element to the table."""
    def get_size(self) -> int:
        """Returns the number of elements in the table."""
    def quantize(self, quantum: float) -> None:
        """Rounds each element of the table to the nearest multiple of quantum."""
    setFps = set_fps
    clearFps = clear_fps
    hasFps = has_fps
    getFps = get_fps
    clearData = clear_data
    addData = add_data
    getSize = get_size

class EggAnimPreload(EggNode):
    """This corresponds to an <AnimPreload> entry."""

    fps: float
    num_frames: int
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggAnimPreload) -> None: ...
    def set_fps(self, fps: float) -> None: ...
    def clear_fps(self) -> None: ...
    def has_fps(self) -> bool: ...
    def get_fps(self) -> float:
        """This is only valid if has_fps() returns true."""
    def set_num_frames(self, num_frames: int) -> None: ...
    def clear_num_frames(self) -> None: ...
    def has_num_frames(self) -> bool: ...
    def get_num_frames(self) -> int:
        """This is only valid if has_num_frames() returns true."""
    setFps = set_fps
    clearFps = clear_fps
    hasFps = has_fps
    getFps = get_fps
    setNumFrames = set_num_frames
    clearNumFrames = clear_num_frames
    hasNumFrames = has_num_frames
    getNumFrames = get_num_frames

class EggAttributes:
    """The set of attributes that may be applied to vertices as well as polygons,
    such as surface normal and color.

    This class cannot inherit from EggObject, because it causes problems at the
    EggPolygon level with multiple appearances of the EggObject base class.
    And making EggObject a virtual base class is just no fun.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: EggAttributes = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def has_normal(self) -> bool: ...
    def get_normal(self) -> LNormald: ...
    def set_normal(self, normal: DoubleVec3Like) -> None: ...
    def clear_normal(self) -> None: ...
    def matches_normal(self, other: EggAttributes) -> bool:
        """Returns true if this normal matches that of the other EggAttributes object,
        include the morph list.
        """
    def copy_normal(self, other: EggAttributes) -> None:
        """Sets this normal to be the same as the other's, include morphs.  If the
        other has no normal, this clears the normal.
        """
    def has_color(self) -> bool: ...
    def get_color(self) -> LColor:
        """Returns the color set on this particular attribute.  If there is no color
        set, returns white.
        """
    def set_color(self, Color: Vec4Like) -> None: ...
    def clear_color(self) -> None: ...
    def matches_color(self, other: EggAttributes) -> bool:
        """Returns true if this color matches that of the other EggAttributes object,
        include the morph list.
        """
    def copy_color(self, other: EggAttributes) -> None:
        """Sets this color to be the same as the other's, include morphs.  If the
        other has no color, this clears the color.
        """
    def write(self, out: ostream, indent_level: int) -> None:
        """Writes the attributes to the indicated output stream in Egg format."""
    def sorts_less_than(self, other: EggAttributes) -> bool:
        """An ordering operator to compare two vertices for sorting order.  This
        imposes an arbitrary ordering useful to identify unique vertices.
        """
    def compare_to(self, other: EggAttributes) -> int:
        """An ordering operator to compare two vertices for sorting order.  This
        imposes an arbitrary ordering useful to identify unique vertices.
        """
    def transform(self, mat: DoubleMat4Like) -> None:
        """Applies the indicated transformation matrix to the attributes."""
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    hasNormal = has_normal
    getNormal = get_normal
    setNormal = set_normal
    clearNormal = clear_normal
    matchesNormal = matches_normal
    copyNormal = copy_normal
    hasColor = has_color
    getColor = get_color
    setColor = set_color
    clearColor = clear_color
    matchesColor = matches_color
    copyColor = copy_color
    sortsLessThan = sorts_less_than
    compareTo = compare_to
    getClassType = get_class_type

class EggVertexUV(EggNamedObject):
    """The set of UV's that may or may not be assigned to a vertex.  To support
    multitexturing, there may be multiple sets of UV's on a particular vertex,
    each with its own name.
    """

    @overload
    def __init__(self, copy: EggVertexUV) -> None: ...
    @overload
    def __init__(self, name: str, uvw: DoubleVec3Like) -> None: ...
    @overload
    def __init__(self, name: str, uv: DoubleVec2Like) -> None: ...
    @staticmethod
    def filter_name(name: str) -> str:
        """Returns the actual name that should be set for a given name string.
        Usually this is the same string that is input, but for historical reasons
        the texture coordinate name "default" is mapped to the empty string.
        """
    def get_num_dimensions(self) -> int:
        """Returns the number of components of the texture coordinate set.  This is
        either 2 (the normal case) or 3 (for a 3-d texture coordinate).
        """
    def has_w(self) -> bool:
        """Returns true if the texture coordinate has a third, w component, false if
        it is just a normal 2-d texture coordinate.
        """
    def get_uv(self) -> LTexCoordd:
        """Returns the texture coordinate pair, if get_num_dimensions() is 2."""
    def get_uvw(self) -> LTexCoord3d:
        """Returns the texture coordinate triple, if get_num_dimensions() is 3.  This
        is also legal to call if get_num_dimensions() is 2 (but the last dimension
        will be zero).
        """
    def set_uv(self, texCoord: DoubleVec2Like) -> None:
        """Sets the texture coordinate pair.  This makes the texture coordinate a 2-d
        texture coordinate, which is the usual case.
        """
    def set_uvw(self, texCoord: DoubleVec3Like) -> None:
        """Sets the texture coordinate triple.  This makes the texture coordinate a
        3-d texture coordinate.
        """
    def has_tangent(self) -> bool: ...
    def has_tangent4(self) -> bool: ...
    def get_tangent(self) -> LNormald: ...
    def get_tangent4(self) -> LVecBase4d: ...
    def set_tangent(self, tangent: DoubleVec3Like) -> None: ...
    def set_tangent4(self, tangent: DoubleVec4Like) -> None:
        """Sets the tangent vector, along with a fourth parameter that is multiplied
        with the result of cross(normal, tangent) when computing the binormal.
        """
    def clear_tangent(self) -> None: ...
    def has_binormal(self) -> bool: ...
    def get_binormal(self) -> LNormald: ...
    def set_binormal(self, binormal: DoubleVec3Like) -> None: ...
    def clear_binormal(self) -> None: ...
    @staticmethod
    def make_average(first: EggVertexUV, second: EggVertexUV) -> EggVertexUV:
        """Creates a new EggVertexUV that contains the averaged values of the two
        given objects.  It is an error if they don't have the same name.
        """
    def transform(self, mat: DoubleMat4Like) -> None:
        """Applies the indicated transformation matrix to the UV's tangent and/or
        binormal.  This does nothing if there is no tangent or binormal.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    def compare_to(self, other: EggVertexUV) -> int:
        """An ordering operator to compare two vertices for sorting order.  This
        imposes an arbitrary ordering useful to identify unique vertices.
        """
    filterName = filter_name
    getNumDimensions = get_num_dimensions
    hasW = has_w
    getUv = get_uv
    getUvw = get_uvw
    setUv = set_uv
    setUvw = set_uvw
    hasTangent = has_tangent
    hasTangent4 = has_tangent4
    getTangent = get_tangent
    getTangent4 = get_tangent4
    setTangent = set_tangent
    setTangent4 = set_tangent4
    clearTangent = clear_tangent
    hasBinormal = has_binormal
    getBinormal = get_binormal
    setBinormal = set_binormal
    clearBinormal = clear_binormal
    makeAverage = make_average
    compareTo = compare_to

class EggVertexAux(EggNamedObject):
    """The set of named auxiliary data that may or may not be assigned to a
    vertex.  Panda will import this data and create a custom column for it in
    the vertex data, but will not otherwise interpret it.  Presumably, a shader
    will process the data later.
    """

    @overload
    def __init__(self, copy: EggVertexAux) -> None: ...
    @overload
    def __init__(self, name: str, aux: DoubleVec4Like) -> None: ...
    def get_aux(self) -> LVecBase4d:
        """Returns the auxiliary data quadruple."""
    def set_aux(self, aux: DoubleVec4Like) -> None:
        """Sets the auxiliary data quadruple."""
    @staticmethod
    def make_average(first: EggVertexAux, second: EggVertexAux) -> EggVertexAux:
        """Creates a new EggVertexAux that contains the averaged values of the two
        given objects.  It is an error if they don't have the same name.
        """
    def write(self, out: ostream, indent_level: int) -> None: ...
    def compare_to(self, other: EggVertexAux) -> int:
        """An ordering operator to compare two vertices for sorting order.  This
        imposes an arbitrary ordering useful to identify unique vertices.
        """
    getAux = get_aux
    setAux = set_aux
    makeAverage = make_average
    compareTo = compare_to

class EggVertex(EggObject, EggAttributes):  # type: ignore[misc]
    """Any one-, two-, three-, or four-component vertex, possibly with attributes
    such as a normal.
    """

    def __init__(self, copy: EggVertex = ...) -> None:
        """Copies all properties of the vertex except its vertex pool, index number,
        and group membership.
        """
    def upcast_to_EggObject(self) -> EggObject: ...
    def upcast_to_EggAttributes(self) -> EggAttributes: ...
    def assign(self, copy: Self) -> Self:
        """Copies all properties of the vertex except its vertex pool, index number,
        and group membership.
        """
    def get_pool(self) -> EggVertexPool:
        """Returns the vertex pool this vertex belongs in.  This may be NULL if the
        vertex has not been added to a pool.
        """
    def is_forward_reference(self) -> bool:
        """Returns true if the vertex is a forward reference to some vertex that
        hasn't been defined yet.  In this case, the vertex may not have any
        properties filled in yet.

        This can only happen if you implicitly create a vertex via
        EggVertexPool::get_forward_vertex(). Presumably, when the vertex pool is
        later filled in, this vertex will be replaced with real data.
        """
    def set_pos(self, pos: DoubleVec2Like | DoubleVec3Like | DoubleVec4Like | float) -> None:
        """`(self, pos: LPoint2d)`:
        Sets the vertex position.  This variant sets the vertex to a two-
        dimensional value.

        `(self, pos: LPoint3d)`:
        Sets the vertex position.  This variant sets the vertex to a three-
        dimensional value.

        `(self, pos: LPoint4d)`:
        Sets the vertex position.  This variant sets the vertex to a four-
        dimensional value.

        `(self, pos: float)`:
        Sets the vertex position.  This variant sets the vertex to a one-
        dimensional value.
        """
    def set_pos4(self, pos: DoubleVec4Like) -> None:
        """This special flavor of set_pos() sets the vertex as a four-component value,
        but does not change the set number of dimensions.  It's handy for
        retrieving the vertex position via get_pos4, manipulating it, then storing
        it back again, without worrying about the number of dimensions it actually
        had.
        """
    def get_num_dimensions(self) -> int:
        """get_pos[123] return the pos as the corresponding type.  It is an error to
        call any of these without first verifying that get_num_dimensions()
        matches the desired type.  However, get_pos4() may always be called; it
        returns the pos as a four-component point in homogeneous space (with a
        1.0 in the last position if the pos has fewer than four components).
        """
    def get_pos1(self) -> float:
        """Only valid if get_num_dimensions() returns 1. Returns the position as a
        one-dimensional value.
        """
    def get_pos2(self) -> LPoint2d:
        """Only valid if get_num_dimensions() returns 2. Returns the position as a
        two-dimensional value.
        """
    def get_pos3(self) -> LVertexd:
        """Valid if get_num_dimensions() returns 3 or 4. Returns the position as a
        three-dimensional value.
        """
    def get_pos4(self) -> LPoint4d:
        """This is always valid, regardless of the value of get_num_dimensions.  It
        returns the position as a four-dimensional value.  If the pos has fewer
        than four dimensions, this value represents the pos extended into four-
        dimensional homogenous space, e.g.  by adding 1 as the fourth component.
        """
    def has_uv(self, name: str = ...) -> bool:
        """`(self)`:
        Returns true if the vertex has an unnamed UV coordinate pair, false
        otherwise.

        This is the more restrictive interface, and is generally useful only in the
        absence of multitexturing; see has_uv(name) for the interface that supports
        multitexturing.

        `(self, name: str)`:
        Returns true if the vertex has the named UV coordinate pair, and the named
        UV coordinate pair is 2-d, false otherwise.
        """
    def get_uv(self, name: str = ...) -> LTexCoordd:
        """`(self)`:
        Returns the unnamed UV coordinate pair on the vertex.  It is an error to
        call this if has_uv() has returned false.

        This is the more restrictive interface, and is generally useful only in the
        absence of multitexturing; see get_uv(name) for the interface that supports
        multitexturing.

        `(self, name: str)`:
        Returns the named UV coordinate pair on the vertex.  It is an error to call
        this if has_uv(name) returned false.
        """
    @overload
    def set_uv(self, texCoord: DoubleVec2Like) -> None:
        """`(self, texCoord: LTexCoordd)`:
        Replaces the unnamed UV coordinate pair on the vertex with the indicated
        value.

        This is the more restrictive interface, and is generally useful only in the
        absence of multitexturing; see set_uv(name, uv) for the interface that
        supports multitexturing.

        `(self, name: str, texCoord: LTexCoordd)`:
        Sets the indicated UV coordinate pair on the vertex.  This replaces any UV
        coordinate pair with the same name already on the vertex, but preserves UV
        morphs.
        """
    @overload
    def set_uv(self, name: str, texCoord: DoubleVec2Like) -> None: ...
    def clear_uv(self, name: str = ...) -> None:
        """`(self)`:
        Removes all UV coordinate pairs from the vertex.

        `(self, name: str)`:
        Removes the named UV coordinate pair from the vertex, along with any UV
        morphs.
        """
    def has_uvw(self, name: str) -> bool:
        """Returns true if the vertex has the named UV coordinate triple, and the
        named UV coordinate triple is 3-d, false otherwise.
        """
    def get_uvw(self, name: str) -> LTexCoord3d:
        """Returns the named UV coordinate triple on the vertex.  It is an error to
        call this if has_uvw(name) returned false.
        """
    def set_uvw(self, name: str, texCoord: DoubleVec3Like) -> None:
        """Sets the indicated UV coordinate triple on the vertex.  This replaces any
        UV coordinate pair or triple with the same name already on the vertex, but
        preserves UV morphs.
        """
    def get_uv_obj(self, name: str) -> EggVertexUV:
        """Returns the named EggVertexUV object, which defines both the UV coordinate
        pair for this name and the UV morphs.  This object might be shared between
        multiple vertices.  You should not attempt to modify this object; instead,
        call modify_uv_object to return a modifiable pointer.
        """
    def modify_uv_obj(self, name: str) -> EggVertexUV:
        """Returns a modifiable pointer to the named EggVertexUV object, which defines
        both the UV coordinate pair for this name and the UV morphs.  Returns NULL
        if there is no such named UV object.
        """
    def set_uv_obj(self, vertex_uv: EggVertexUV) -> None:
        """Sets the indicated EggVertexUV on the vertex.  This replaces any UV
        coordinate pair with the same name already on the vertex, including UV
        morphs.
        """
    def has_aux(self, name: str = ...) -> bool:
        """`(self)`:
        Returns true if the vertex has any auxiliary data, false otherwise.

        `(self, name: str)`:
        Returns true if the vertex has the named auxiliary data quadruple.
        """
    def clear_aux(self, name: str = ...) -> None:
        """`(self)`:
        Removes all auxiliary data from the vertex.

        `(self, name: str)`:
        Removes the named auxiliary data from the vertex.
        """
    def get_aux(self, name: str) -> LVecBase4d:
        """Returns the named auxiliary data quadruple on the vertex.  It is an error
        to call this if has_aux(name) returned false.
        """
    def set_aux(self, name: str, aux: DoubleVec4Like) -> None:
        """Sets the indicated auxiliary data quadruple on the vertex.  This replaces
        any auxiliary data with the same name already on the vertex.
        """
    def get_aux_obj(self, name: str) -> EggVertexAux:
        """Returns the named EggVertexAux object, which defines the auxiliary data for
        this name.  This object might be shared between multiple vertices.  You
        should not attempt to modify this object; instead, call modify_aux_object
        to return a modifiable pointer.
        """
    def modify_aux_obj(self, name: str) -> EggVertexAux:
        """Returns a modifiable pointer to the named EggVertexAux object, which
        defines the auxiliary data for this name.  Returns NULL if there is no such
        named UV object.
        """
    def set_aux_obj(self, vertex_aux: EggVertexAux) -> None:
        """Sets the indicated EggVertexAux on the vertex.  This replaces any auxiliary
        data with the same name already on the vertex.
        """
    @staticmethod
    def make_average(first: EggVertex, second: EggVertex) -> EggVertex:
        """Creates a new vertex that lies in between the two given vertices.  The
        attributes for the UV sets they have in common are averaged.

        Both vertices need to be either in no pool, or in the same pool.  In the
        latter case, the new vertex will be placed in that pool.
        """
    def get_index(self) -> int:
        """Returns the index number of the vertex within its pool."""
    def set_external_index(self, external_index: int) -> None:
        """Sets a special index number that is associated with the EggVertex (but is
        not written to the egg file). This number is not interpreted by any egg
        code; it is simply maintained along with the vertex.  It *is* used to
        differentiate otherwise identical vertices in
        EggVertexPool::create_unique_vertex(), however.

        The intention of this number is as an aid for file converters, to associate
        an EggVertex back to the index number of the original source vertex.
        """
    def get_external_index(self) -> int:
        """Returns the number set by set_external_index().  See set_external_index()."""
    def set_external_index2(self, external_index2: int) -> None:
        """Similar to set_external_index(), but this is a different number which may
        be used for a different purpose by the calling code.  The egg library does
        not assign any meaning to this number or use it in any way.
        """
    def get_external_index2(self) -> int:
        """Returns the number set by set_external_index2().  See
        set_external_index2().
        """
    def write(self, out: ostream, indent_level: int) -> None:
        """Writes the vertex to the indicated output stream in Egg format."""
    def sorts_less_than(self, other: EggVertex) -> bool:  # type: ignore[override]
        """An ordering operator to compare two vertices for sorting order.  This
        imposes an arbitrary ordering useful to identify unique vertices.
        """
    def compare_to(self, other: EggVertex) -> int:  # type: ignore[override]
        """An ordering operator to compare two vertices for sorting order.  This
        imposes an arbitrary ordering useful to identify unique vertices.

        Group membership is not considered in this comparison.  This is somewhat
        problematic, but cannot easily be helped, because considering group
        membership would make it difficult to add and remove groups from vertices.
        It also makes it impossible to meaningfully compare with a concrete
        EggVertex object (which cannot have group memberships).

        However, this is not altogether bad, because two vertices that are
        identical in all other properties should generally also be identical in
        group memberships, else the vertices will tend to fly apart when the joints
        animate.
        """
    def get_num_local_coord(self) -> int:
        """Returns the number of primitives that own this vertex whose vertices are
        interpreted to be in a local coordinate system.
        """
    def get_num_global_coord(self) -> int:
        """Returns the number of primitives that own this vertex whose vertices are
        interpreted in the global coordinate system.
        """
    def transform(self, mat: DoubleMat4Like) -> None:
        """Applies the indicated transformation matrix to the vertex."""
    def has_gref(self, group: EggGroup) -> bool:
        """Returns true if the indicated group references this vertex, false
        otherwise.
        """
    def copy_grefs_from(self, other: EggVertex) -> None:
        """Copies all the group references from the other vertex onto this one.  This
        assigns the current vertex to exactly the same groups, with exactly the
        same memberships, as the given one.

        Warning: only an EggVertex allocated from the free store may have groups
        assigned to it.  Do not attempt to call this on a temporary concrete
        EggVertex object; a core dump will certainly result.
        """
    def clear_grefs(self) -> None:
        """Removes all group references from the vertex, so that it is not assigned to
        any group.
        """
    def has_pref(self, prim: EggPrimitive) -> int:
        """Returns the number of times the vertex appears in the indicated primitive,
        or 0 if it does not appear.
        """
    def test_gref_integrity(self) -> None: ...
    def test_pref_integrity(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    upcastToEggObject = upcast_to_EggObject
    upcastToEggAttributes = upcast_to_EggAttributes
    getPool = get_pool
    isForwardReference = is_forward_reference
    setPos = set_pos
    setPos4 = set_pos4
    getNumDimensions = get_num_dimensions
    getPos1 = get_pos1
    getPos2 = get_pos2
    getPos3 = get_pos3
    getPos4 = get_pos4
    hasUv = has_uv
    getUv = get_uv
    setUv = set_uv
    clearUv = clear_uv
    hasUvw = has_uvw
    getUvw = get_uvw
    setUvw = set_uvw
    getUvObj = get_uv_obj
    modifyUvObj = modify_uv_obj
    setUvObj = set_uv_obj
    hasAux = has_aux
    clearAux = clear_aux
    getAux = get_aux
    setAux = set_aux
    getAuxObj = get_aux_obj
    modifyAuxObj = modify_aux_obj
    setAuxObj = set_aux_obj
    makeAverage = make_average
    getIndex = get_index
    setExternalIndex = set_external_index
    getExternalIndex = get_external_index
    setExternalIndex2 = set_external_index2
    getExternalIndex2 = get_external_index2
    sortsLessThan = sorts_less_than  # type: ignore[assignment]
    compareTo = compare_to  # type: ignore[assignment]
    getNumLocalCoord = get_num_local_coord
    getNumGlobalCoord = get_num_global_coord
    hasGref = has_gref
    copyGrefsFrom = copy_grefs_from
    clearGrefs = clear_grefs
    hasPref = has_pref
    testGrefIntegrity = test_gref_integrity
    testPrefIntegrity = test_pref_integrity

class EggVertexPool(EggNode):
    """A collection of vertices.  There may be any number of vertex pools in a
    single egg structure.  The vertices in a single pool need not necessarily
    have any connection to each other, but it is necessary that any one
    primitive (e.g.  a polygon) must pull all its vertices from the same pool.

    An EggVertexPool is an STL-style container of pointers to EggVertex's.
    Functions add_vertex() and remove_vertex() are provided to manipulate the
    list.  The list may also be operated on (read-only) via iterators and
    begin()/end().
    """

    @overload
    def __init__(self, copy: EggVertexPool) -> None:
        """Copying a vertex pool is of questionable value, since it will copy all of
        the vertices and assign new pointers to them all.  There will be no
        polygons referring to the new vertices.
        """
    @overload
    def __init__(self, name: str) -> None: ...
    def __getitem__(self, index: int) -> EggVertex:
        """Returns the vertex in the pool with the indicated index number, or NULL if
        no vertices have that index number.
        """
    def __len__(self) -> int:
        """Returns the number of vertices in the pool."""
    def __iter__(self) -> Iterator[EggVertex]: ...  # Doesn't actually exist
    def has_vertex(self, index: int) -> bool:
        """Returns true if the indicated vertex has been defined in the vertex pool,
        false otherwise.  This does not include forward references.
        """
    def has_forward_vertices(self) -> bool:
        """Returns true if any vertices in the pool are undefined forward-reference
        vertices, false if all vertices are defined.
        """
    def has_defined_vertices(self) -> bool:
        """Returns true if any vertices in the pool are fully defined vertices, false
        if all vertices are forward references.
        """
    def get_vertex(self, index: int) -> EggVertex:
        """Returns the vertex in the pool with the indicated index number, or NULL if
        no vertices have that index number.
        """
    def get_forward_vertex(self, index: int) -> EggVertex:
        """Returns the vertex in the pool with the indicated index number.  If there
        is not a vertex in the pool with the indicated index number, creates a
        special forward-reference EggVertex that has no data, on the assumption
        that the vertex pool has not yet been fully read and more data will be
        available later.
        """
    def get_highest_index(self) -> int:
        """Returns the highest index number used by any vertex in the pool (except
        forward references).  Returns -1 if the pool is empty.
        """
    def set_highest_index(self, highest_index: int) -> None:
        """Artificially changes the "highest index number", so that a newly created
        vertex will begin at this number plus 1.  This can be used to default a
        vertex pool to start counting at 1 (or any other index number), instead of
        the default of 0.  Use with caution.
        """
    def get_num_dimensions(self) -> int:
        """Returns the maximum number of dimensions used by any vertex in the pool."""
    def has_normals(self) -> bool:
        """Returns true if any vertex in the pool has a normal defined, false if none
        of them do.
        """
    def has_colors(self) -> bool:
        """Returns true if any vertex in the pool has a color defined, false if none
        of them do.
        """
    def has_nonwhite_colors(self) -> bool:
        """Returns true if any vertex in the pool has a color defined other than
        white, false if no vertices have colors, or if all colors are white.
        """
    def has_uvs(self) -> bool:
        """Returns true if any vertex in the pool has a uv defined, false if none of
        them do.
        """
    def has_aux(self) -> bool:
        """Returns true if any vertex in the pool has auxiliary data defined, false if
        none of them do.
        """
    def add_vertex(self, vertex: EggVertex, index: int = ...) -> EggVertex:
        """Adds the indicated vertex to the pool.  It is an error if the vertex is
        already a member of this or any other pool.  The vertex must have been
        allocated from the free store; its pointer will now be owned by the vertex
        pool.  If the index number is supplied, tries to assign that index number;
        it is an error if the index number is already in use.

        It is possible that a forward reference to this vertex was requested in the
        past; if so, the data from the supplied vertex is copied onto the forward
        reference, which becomes the actual vertex.  In this case, a different
        pointer is saved (and returned) than the one actually passed in.  In the
        usual case, however, the vertex pointer passed in is the one that is saved
        in the vertex pool and returned from this method.
        """
    def make_new_vertex(self, pos: DoubleVec2Like | DoubleVec3Like | DoubleVec4Like | float = ...) -> EggVertex:
        """`(self)`:
        Allocates and returns a new vertex from the pool.  This is one of three
        ways to add new vertices to a vertex pool.

        `(self, pos: LPoint2d)`; `(self, pos: LPoint3d)`; `(self, pos: LPoint4d)`; `(self, pos: float)`:
        Allocates and returns a new vertex from the pool.  This is one of three
        ways to add new vertices to a vertex pool.

        This flavor of make_new_vertex() explicitly sets the vertex position as it
        is allocated.  It does not attempt to share vertices.
        """
    def create_unique_vertex(self, copy: EggVertex) -> EggVertex:
        """Creates a new vertex in the pool that is a copy of the indicated one and
        returns it.  If there is already a vertex in the pool like the indicated
        one, simply returns that one.
        """
    def find_matching_vertex(self, copy: EggVertex) -> EggVertex:
        """If the EggVertexPool already has a vertex matching the indicated vertex,
        returns it; otherwise, returns NULL.  This is similar to
        create_unique_vertex() except that a new vertex is never created.
        """
    def remove_vertex(self, vertex: EggVertex) -> None:
        """Removes the vertex from the pool.  It is an error if the vertex is not
        already a member of the pool.
        """
    def remove_unused_vertices(self) -> int:
        """Removes all vertices from the pool that are not referenced by at least one
        primitive.  Also collapses together equivalent vertices, and renumbers all
        vertices after the operation so their indices are consecutive, beginning at
        zero.  Returns the number of vertices removed.
        """
    def add_unused_vertices_to_prim(self, prim: EggPrimitive) -> None:
        """Adds all of the unused vertices in this vertex pool to the indicated
        primitive, in ascending order.
        """
    def transform(self, mat: DoubleMat4Like) -> None:
        """Applies the indicated transformation matrix to all the vertices.  However,
        vertices that are attached to primitives that believe their vertices are in
        a local coordinate system are transformed only by the scale and rotation
        component.  If a vertex happens to be attached both to a local and a global
        primitive, and the transformation includes a translation component, the
        vertex will be split.
        """
    def sort_by_external_index(self) -> None:
        """Re-orders (and re-numbers) the vertices in this vertex pool so that they
        appear in increasing order by the optional external_index that has been
        assigned to each vertex.
        """
    hasVertex = has_vertex
    hasForwardVertices = has_forward_vertices
    hasDefinedVertices = has_defined_vertices
    getVertex = get_vertex
    getForwardVertex = get_forward_vertex
    getHighestIndex = get_highest_index
    setHighestIndex = set_highest_index
    getNumDimensions = get_num_dimensions
    hasNormals = has_normals
    hasColors = has_colors
    hasNonwhiteColors = has_nonwhite_colors
    hasUvs = has_uvs
    hasAux = has_aux
    addVertex = add_vertex
    makeNewVertex = make_new_vertex
    createUniqueVertex = create_unique_vertex
    findMatchingVertex = find_matching_vertex
    removeVertex = remove_vertex
    removeUnusedVertices = remove_unused_vertices
    addUnusedVerticesToPrim = add_unused_vertices_to_prim
    sortByExternalIndex = sort_by_external_index

class EggRenderMode:
    """This class stores miscellaneous rendering properties that is associated
    with geometry, and which may be set on the geometry primitive level, on the
    group above it, or indirectly via a texture.  It's intended to be a base
    class for egg objects that can have these properties set.

    This class cannot inherit from EggObject, because it causes problems at the
    EggPolygon level with multiple appearances of the EggObject base class.
    And making EggObject a virtual base class is just no fun.
    """

    AM_unspecified: Final = 0
    AMUnspecified: Final = 0
    AM_off: Final = 1
    AMOff: Final = 1
    AM_on: Final = 2
    AMOn: Final = 2
    AM_blend: Final = 3
    AMBlend: Final = 3
    AM_blend_no_occlude: Final = 4
    AMBlendNoOcclude: Final = 4
    AM_ms: Final = 5
    AMMs: Final = 5
    AM_ms_mask: Final = 6
    AMMsMask: Final = 6
    AM_binary: Final = 7
    AMBinary: Final = 7
    AM_dual: Final = 8
    AMDual: Final = 8
    AM_premultiplied: Final = 9
    AMPremultiplied: Final = 9
    DWM_unspecified: Final = 0
    DWMUnspecified: Final = 0
    DWM_off: Final = 1
    DWMOff: Final = 1
    DWM_on: Final = 2
    DWMOn: Final = 2
    DTM_unspecified: Final = 0
    DTMUnspecified: Final = 0
    DTM_off: Final = 1
    DTMOff: Final = 1
    DTM_on: Final = 2
    DTMOn: Final = 2
    VM_unspecified: Final = 0
    VMUnspecified: Final = 0
    VM_hidden: Final = 1
    VMHidden: Final = 1
    VM_normal: Final = 2
    VMNormal: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: EggRenderMode = ...) -> None: ...
    def __eq__(self, __other: object) -> bool:
        """Comparison operators are handy."""
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: EggRenderMode) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def write(self, out: ostream, indent_level: int) -> None:
        """Writes the attributes to the indicated output stream in Egg format."""
    def set_alpha_mode(self, mode: _EggRenderMode_AlphaMode) -> None:
        """Specifies precisely how the transparency for this geometry should be
        achieved, or if it should be used.  The default, AM_unspecified, is to use
        transparency if the geometry has a color whose alpha value is non-1, or if
        it has a four-channel texture applied; otherwise, AM_on forces transparency
        on, and AM_off forces it off.  The other flavors of transparency are
        specific ways to turn on transparency, which may or may not be supported by
        a particular rendering backend.
        """
    def get_alpha_mode(self) -> _EggRenderMode_AlphaMode:
        """Returns the alpha mode that was set, or AM_unspecified if nothing was set.
        See set_alpha_mode().
        """
    def set_depth_write_mode(self, mode: _EggRenderMode_DepthWriteMode) -> None:
        """Specifies whether writes should be made to the depth buffer (assuming the
        rendering backend provides a depth buffer) when rendering this geometry.
        """
    def get_depth_write_mode(self) -> _EggRenderMode_DepthWriteMode:
        """Returns the depth_write mode that was set, or DWM_unspecified if nothing
        was set.  See set_depth_write_mode().
        """
    def set_depth_test_mode(self, mode: _EggRenderMode_DepthTestMode) -> None:
        """Specifies whether this geometry should be tested against the depth buffer
        when it is drawn (assuming the rendering backend provides a depth buffer).
        Note that this is different, and independent from, the depth_write mode.
        """
    def get_depth_test_mode(self) -> _EggRenderMode_DepthTestMode:
        """Returns the depth_test mode that was set, or DTM_unspecified if nothing was
        set.  See set_depth_test_mode().
        """
    def set_visibility_mode(self, mode: _EggRenderMode_VisibilityMode) -> None:
        """Specifies whether this geometry is to be considered normally visible, or
        hidden.  If it is hidden, it is either not loaded into the scene graph at
        all, or loaded as a "stashed" node, according to the setting of egg-
        suppress-hidden.
        """
    def get_visibility_mode(self) -> _EggRenderMode_VisibilityMode:
        """Returns the visibility mode that was set, or VM_unspecified if nothing was
        set.  See set_visibility_mode().
        """
    def set_depth_offset(self, bias: int) -> None:
        """Sets the "depth-offset" flag associated with this object.  This adds or
        subtracts an offset bias into the depth buffer.  See also DepthOffsetAttrib
        and NodePath::set_depth_offset().
        """
    def get_depth_offset(self) -> int:
        """Returns the "depth-offset" flag as set for this particular object.  See
        set_depth_offset().
        """
    def has_depth_offset(self) -> bool:
        """Returns true if the depth-offset flag has been set for this particular
        object.  See set_depth_offset().
        """
    def clear_depth_offset(self) -> None:
        """Removes the depth-offset flag from this particular object.  See
        set_depth_offset().
        """
    def set_draw_order(self, order: int) -> None:
        """Sets the "draw-order" flag associated with this object.  This specifies a
        particular order in which objects of this type should be drawn, within the
        specified bin.  If a bin is not explicitly specified, "fixed" is used.  See
        also set_bin().
        """
    def get_draw_order(self) -> int:
        """Returns the "draw-order" flag as set for this particular object.  See
        set_draw_order().
        """
    def has_draw_order(self) -> bool:
        """Returns true if the draw-order flag has been set for this particular
        object.  See set_draw_order().
        """
    def clear_draw_order(self) -> None:
        """Removes the draw-order flag from this particular object.  See
        set_draw_order().
        """
    def set_bin(self, bin: str) -> None:
        """Sets the "bin" string for this particular object.  This names a particular
        bin in which the object should be rendered.  The exact meaning of a bin is
        implementation defined, but generally a GeomBin matching each bin name must
        also be specifically added to the rendering engine (e.g.  the
        CullTraverser) in use for this to work.  See also set_draw_order().
        """
    def get_bin(self) -> str:
        """Returns the bin name that has been set for this particular object, if any.
        See set_bin().
        """
    def has_bin(self) -> bool:
        """Returns true if a bin name has been set for this particular object.  See
        set_bin().
        """
    def clear_bin(self) -> None:
        """Removes the bin name that was set for this particular object.  See
        set_bin().
        """
    @staticmethod
    def string_alpha_mode(string: str) -> _EggRenderMode_AlphaMode:
        """Returns the AlphaMode value associated with the given string
        representation, or AM_unspecified if the string does not match any known
        AlphaMode value.
        """
    @staticmethod
    def string_depth_write_mode(string: str) -> _EggRenderMode_DepthWriteMode:
        """Returns the DepthWriteMode value associated with the given string
        representation, or DWM_unspecified if the string does not match any known
        DepthWriteMode value.
        """
    @staticmethod
    def string_depth_test_mode(string: str) -> _EggRenderMode_DepthTestMode:
        """Returns the DepthTestMode value associated with the given string
        representation, or DTM_unspecified if the string does not match any known
        DepthTestMode value.
        """
    @staticmethod
    def string_visibility_mode(string: str) -> _EggRenderMode_VisibilityMode:
        """Returns the HiddenMode value associated with the given string
        representation, or VM_unspecified if the string does not match any known
        HiddenMode value.
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setAlphaMode = set_alpha_mode
    getAlphaMode = get_alpha_mode
    setDepthWriteMode = set_depth_write_mode
    getDepthWriteMode = get_depth_write_mode
    setDepthTestMode = set_depth_test_mode
    getDepthTestMode = get_depth_test_mode
    setVisibilityMode = set_visibility_mode
    getVisibilityMode = get_visibility_mode
    setDepthOffset = set_depth_offset
    getDepthOffset = get_depth_offset
    hasDepthOffset = has_depth_offset
    clearDepthOffset = clear_depth_offset
    setDrawOrder = set_draw_order
    getDrawOrder = get_draw_order
    hasDrawOrder = has_draw_order
    clearDrawOrder = clear_draw_order
    setBin = set_bin
    getBin = get_bin
    hasBin = has_bin
    clearBin = clear_bin
    stringAlphaMode = string_alpha_mode
    stringDepthWriteMode = string_depth_write_mode
    stringDepthTestMode = string_depth_test_mode
    stringVisibilityMode = string_visibility_mode
    getClassType = get_class_type

class EggTransform:
    """This represents the <Transform> entry of a group or texture node: a list of
    component transform operations, applied in order, that describe a net
    transform matrix.

    This may be either a 3-d transform, and therefore described by a 4x4
    matrix, or a 2-d transform, described by a 3x3 matrix.
    """

    CT_invalid: Final = 0
    CTInvalid: Final = 0
    CT_translate2d: Final = 1
    CTTranslate2d: Final = 1
    CT_translate3d: Final = 2
    CTTranslate3d: Final = 2
    CT_rotate2d: Final = 3
    CTRotate2d: Final = 3
    CT_rotx: Final = 4
    CTRotx: Final = 4
    CT_roty: Final = 5
    CTRoty: Final = 5
    CT_rotz: Final = 6
    CTRotz: Final = 6
    CT_rotate3d: Final = 7
    CTRotate3d: Final = 7
    CT_scale2d: Final = 8
    CTScale2d: Final = 8
    CT_scale3d: Final = 9
    CTScale3d: Final = 9
    CT_uniform_scale: Final = 10
    CTUniformScale: Final = 10
    CT_matrix3: Final = 11
    CTMatrix3: Final = 11
    CT_matrix4: Final = 12
    CTMatrix4: Final = 12
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: EggTransform = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def clear_transform(self) -> None:
        """Resets the transform to empty, identity."""
    def add_translate2d(self, translate: DoubleVec2Like) -> None:
        """Appends a 2-d translation operation to the current transform."""
    def add_translate3d(self, translate: DoubleVec3Like) -> None:
        """Appends a 3-d translation operation to the current transform."""
    def add_rotate2d(self, angle: float) -> None:
        """Appends a 2-d rotation to the current transform.  The rotation angle is
        specified in degrees counterclockwise about the origin.
        """
    def add_rotx(self, angle: float) -> None:
        """Appends a rotation about the X axis to the current transform.  The rotation
        angle is specified in degrees counterclockwise about the axis.
        """
    def add_roty(self, angle: float) -> None:
        """Appends a rotation about the Y axis to the current transform.  The rotation
        angle is specified in degrees counterclockwise about the axis.
        """
    def add_rotz(self, angle: float) -> None:
        """Appends a rotation about the Z axis to the current transform.  The rotation
        angle is specified in degrees counterclockwise about the axis.
        """
    @overload
    def add_rotate3d(self, quat: DoubleVec4Like) -> None:
        """`(self, quat: LQuaterniond)`:
        Appends an arbitrary 3-d rotation to the current transform, expressed as a
        quaternion.  This is converted to axis-angle notation for the egg file.

        `(self, angle: float, axis: LVector3d)`:
        Appends a 3-d rotation about an arbitrary axis to the current transform.
        The rotation angle is specified in degrees counterclockwise about the axis.
        """
    @overload
    def add_rotate3d(self, angle: float, axis: DoubleVec3Like) -> None: ...
    def add_scale2d(self, scale: DoubleVec2Like) -> None:
        """Appends a possibly non-uniform scale to the current transform."""
    def add_scale3d(self, scale: DoubleVec3Like) -> None:
        """Appends a possibly non-uniform scale to the current transform."""
    def add_uniform_scale(self, scale: float) -> None:
        """Appends a uniform scale to the current transform."""
    def add_matrix3(self, mat: LMatrix3d) -> None:
        """Appends an arbitrary 3x3 matrix to the current transform."""
    def add_matrix4(self, mat: DoubleMat4Like) -> None:
        """Appends an arbitrary 4x4 matrix to the current transform."""
    def has_transform(self) -> bool:
        """Returns true if the transform is nonempty, false if it is empty (no
        transform components have been added).  This is true for either a 2-d or a
        3-d transform.
        """
    def has_transform2d(self) -> bool:
        """Returns true if the transform is specified as a 2-d transform, e.g.  with a
        3x3 matrix, or false if it is specified as a 3-d transform (with a 4x4
        matrix), or not specified at all.

        Normally, EggTextures have a 2-d matrix (but occasionally they use a 3-d
        matrix), and EggGroups always have a 3-d matrix.
        """
    def set_transform2d(self, mat: LMatrix3d) -> None:
        """Sets the overall transform as a 3x3 matrix.  This completely replaces
        whatever componentwise transform may have been defined.
        """
    def has_transform3d(self) -> bool:
        """Returns true if the transform is specified as a 3-d transform, e.g.  with a
        4x4 matrix, or false if it is specified as a 2-d transform (with a 2x2
        matrix), or not specified at all.

        Normally, EggTextures have a 3-d matrix (but occasionally they use a 3-d
        matrix), and EggGroups always have a 3-d matrix.
        """
    def set_transform3d(self, mat: DoubleMat4Like) -> None:
        """Sets the overall transform as a 4x4 matrix.  This completely replaces
        whatever componentwise transform may have been defined.
        """
    def get_transform2d(self) -> LMatrix3d:
        """Returns the overall transform as a 3x3 matrix.  It is an error to call this
        if has_transform3d() is true.
        """
    def get_transform3d(self) -> LMatrix4d:
        """Returns the overall transform as a 4x4 matrix.  It is valid to call this
        even if has_transform2d() is true; in this case, the 3x3 transform will be
        expanded to a 4x4 matrix.
        """
    def transform_is_identity(self) -> bool:
        """Returns true if the described transform is identity, false otherwise."""
    def get_num_components(self) -> int:
        """Returns the number of components that make up the transform."""
    def get_component_type(self, n: int) -> _EggTransform_ComponentType:
        """Returns the type of the nth component."""
    def get_component_number(self, n: int) -> float:
        """Returns the solitary number associated with the nth component.  In the case
        of a rotation, this is the angle in degrees to rotate; in the case of
        uniform scale, this is the amount of the scale.  Other types do not use
        this property.
        """
    def get_component_vec2(self, n: int) -> LVecBase2d:
        """Returns the 2-component vector associated with the nth component.  This may
        be the translate vector, rotate axis, or non-uniform scale.  It is an error
        to call this if the component type does not use a 2-d vector property.
        """
    def get_component_vec3(self, n: int) -> LVecBase3d:
        """Returns the 3-component vector associated with the nth component.  This may
        be the translate vector, rotate axis, or non-uniform scale.  It is an error
        to call this if the component type does not use a 3-d vector property.
        """
    def get_component_mat3(self, n: int) -> LMatrix3d:
        """Returns the 3x3 matrix associated with the nth component.  It is an error
        to call this if the component type is not CT_matrix3.
        """
    def get_component_mat4(self, n: int) -> LMatrix4d:
        """Returns the 4x4 matrix associated with the nth component.  It is an error
        to call this if the component type is not CT_matrix4.
        """
    def write(self, out: ostream, indent_level: int, label: str) -> None:
        """Writes the transform to the indicated stream in Egg format."""
    clearTransform = clear_transform
    addTranslate2d = add_translate2d
    addTranslate3d = add_translate3d
    addRotate2d = add_rotate2d
    addRotx = add_rotx
    addRoty = add_roty
    addRotz = add_rotz
    addRotate3d = add_rotate3d
    addScale2d = add_scale2d
    addScale3d = add_scale3d
    addUniformScale = add_uniform_scale
    addMatrix3 = add_matrix3
    addMatrix4 = add_matrix4
    hasTransform = has_transform
    hasTransform2d = has_transform2d
    setTransform2d = set_transform2d
    hasTransform3d = has_transform3d
    setTransform3d = set_transform3d
    getTransform2d = get_transform2d
    getTransform3d = get_transform3d
    transformIsIdentity = transform_is_identity
    getNumComponents = get_num_components
    getComponentType = get_component_type
    getComponentNumber = get_component_number
    getComponentVec2 = get_component_vec2
    getComponentVec3 = get_component_vec3
    getComponentMat3 = get_component_mat3
    getComponentMat4 = get_component_mat4

class EggSwitchCondition(EggObject):
    """This corresponds to a <SwitchCondition> entry within a group.  It indicates
    the condition at which a level-of-detail is switched in or out.  This is
    actually an abstract base class for potentially any number of specific
    different kinds of switching conditions; presently, only a <Distance> type
    is actually supported.
    """

    def make_copy(self) -> EggSwitchCondition: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def transform(self, mat: DoubleMat4Like) -> None: ...
    makeCopy = make_copy

class EggSwitchConditionDistance(EggSwitchCondition):
    """A SwitchCondition that switches the levels-of-detail based on distance from
    the camera's eyepoint.
    """

    def __init__(self, switch_in: float, switch_out: float, center: DoubleVec3Like, fade: float = ...) -> None: ...

class EggGroup(EggGroupNode, EggRenderMode, EggTransform):  # type: ignore[misc]
    """The main glue of the egg hierarchy, this corresponds to the <Group>,
    <Instance>, and <Joint> type nodes.
    """

    GT_invalid: Final = -1
    GTInvalid: Final = -1
    GT_group: Final = 0
    GTGroup: Final = 0
    GT_instance: Final = 1
    GTInstance: Final = 1
    GT_joint: Final = 2
    GTJoint: Final = 2
    DC_unspecified: Final = 0
    DCUnspecified: Final = 0
    DC_none: Final = 16
    DCNone: Final = 16
    DC_local: Final = 32
    DCLocal: Final = 32
    DC_net: Final = 48
    DCNet: Final = 48
    DC_no_touch: Final = 64
    DCNoTouch: Final = 64
    DC_default: Final = 80
    DCDefault: Final = 80
    BT_none: Final = 0
    BTNone: Final = 0
    BT_axis: Final = 32
    BTAxis: Final = 32
    BT_point_camera_relative: Final = 64
    BTPointCameraRelative: Final = 64
    BT_point_world_relative: Final = 128
    BTPointWorldRelative: Final = 128
    CST_none: Final = 0
    CSTNone: Final = 0
    CST_plane: Final = 65536
    CSTPlane: Final = 65536
    CST_polygon: Final = 131072
    CSTPolygon: Final = 131072
    CST_polyset: Final = 196608
    CSTPolyset: Final = 196608
    CST_sphere: Final = 262144
    CSTSphere: Final = 262144
    CST_tube: Final = 327680
    CSTTube: Final = 327680
    CST_inv_sphere: Final = 393216
    CSTInvSphere: Final = 393216
    CST_box: Final = 458752
    CSTBox: Final = 458752
    CST_floor_mesh: Final = 524288
    CSTFloorMesh: Final = 524288
    CF_none: Final = 0
    CFNone: Final = 0
    CF_descend: Final = 1048576
    CFDescend: Final = 1048576
    CF_event: Final = 2097152
    CFEvent: Final = 2097152
    CF_keep: Final = 4194304
    CFKeep: Final = 4194304
    CF_solid: Final = 8388608
    CFSolid: Final = 8388608
    CF_center: Final = 16777216
    CFCenter: Final = 16777216
    CF_turnstile: Final = 33554432
    CFTurnstile: Final = 33554432
    CF_level: Final = 67108864
    CFLevel: Final = 67108864
    CF_intangible: Final = 134217728
    CFIntangible: Final = 134217728
    DT_none: Final = 0
    DTNone: Final = 0
    DT_structured: Final = 268435456
    DTStructured: Final = 268435456
    DT_sync: Final = 536870912
    DTSync: Final = 536870912
    DT_nosync: Final = 805306368
    DTNosync: Final = 805306368
    DT_default: Final = 1073741824
    DTDefault: Final = 1073741824
    BM_unspecified: Final = 0
    BMUnspecified: Final = 0
    BM_none: Final = 1
    BMNone: Final = 1
    BM_add: Final = 2
    BMAdd: Final = 2
    BM_subtract: Final = 3
    BMSubtract: Final = 3
    BM_inv_subtract: Final = 4
    BMInvSubtract: Final = 4
    BM_min: Final = 5
    BMMin: Final = 5
    BM_max: Final = 6
    BMMax: Final = 6
    BO_unspecified: Final = 0
    BOUnspecified: Final = 0
    BO_zero: Final = 1
    BOZero: Final = 1
    BO_one: Final = 2
    BOOne: Final = 2
    BO_incoming_color: Final = 3
    BOIncomingColor: Final = 3
    BO_one_minus_incoming_color: Final = 4
    BOOneMinusIncomingColor: Final = 4
    BO_fbuffer_color: Final = 5
    BOFbufferColor: Final = 5
    BO_one_minus_fbuffer_color: Final = 6
    BOOneMinusFbufferColor: Final = 6
    BO_incoming_alpha: Final = 7
    BOIncomingAlpha: Final = 7
    BO_one_minus_incoming_alpha: Final = 8
    BOOneMinusIncomingAlpha: Final = 8
    BO_fbuffer_alpha: Final = 9
    BOFbufferAlpha: Final = 9
    BO_one_minus_fbuffer_alpha: Final = 10
    BOOneMinusFbufferAlpha: Final = 10
    BO_constant_color: Final = 11
    BOConstantColor: Final = 11
    BO_one_minus_constant_color: Final = 12
    BOOneMinusConstantColor: Final = 12
    BO_constant_alpha: Final = 13
    BOConstantAlpha: Final = 13
    BO_one_minus_constant_alpha: Final = 14
    BOOneMinusConstantAlpha: Final = 14
    BO_incoming_color_saturate: Final = 15
    BOIncomingColorSaturate: Final = 15
    BO_color_scale: Final = 16
    BOColorScale: Final = 16
    BO_one_minus_color_scale: Final = 17
    BOOneMinusColorScale: Final = 17
    BO_alpha_scale: Final = 18
    BOAlphaScale: Final = 18
    BO_one_minus_alpha_scale: Final = 19
    BOOneMinusAlphaScale: Final = 19
    group_type: _EggGroup_GroupType
    billboard_type: _EggGroup_BillboardType
    billboard_center: LPoint3d
    cs_type: _EggGroup_CollisionSolidType
    collide_flags: _EggGroup_CollideFlags
    collision_name: str
    dcs_type: _EggGroup_DCSType
    dart_type: _EggGroup_DartType
    switch_flag: bool
    switch_fps: float
    model_flag: bool
    texlist_flag: bool
    nofog_flag: bool
    decal_flag: bool
    direct_flag: bool
    portal_flag: bool
    occluder_flag: bool
    indexed_flag: bool
    collide_mask: CollideMask
    from_collide_mask: CollideMask
    into_collide_mask: CollideMask
    blend_mode: _EggGroup_BlendMode
    blend_operand_a: _EggGroup_BlendOperand
    blend_operand_b: _EggGroup_BlendOperand
    blend_color: LColor
    lod: EggSwitchCondition
    default_pose: EggTransform
    scroll_u: float
    scroll_v: float
    scroll_w: float
    scroll_r: float
    @property
    def object_types(self) -> Sequence[str]: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggGroup) -> None: ...
    def upcast_to_EggGroupNode(self) -> EggGroupNode: ...
    def upcast_to_EggRenderMode(self) -> EggRenderMode: ...
    def upcast_to_EggTransform(self) -> EggTransform: ...
    def write(self, out: ostream, indent_level: int) -> None:  # type: ignore[override]
        """Writes the group and all of its children to the indicated output stream in
        Egg format.
        """
    def write_billboard_flags(self, out: ostream, indent_level: int) -> None:
        """Writes just the <Billboard> entry and related fields to the indicated
        ostream.
        """
    def write_collide_flags(self, out: ostream, indent_level: int) -> None:
        """Writes just the <Collide> entry and related fields to the indicated
        ostream.
        """
    def write_model_flags(self, out: ostream, indent_level: int) -> None:
        """Writes the <Model> flag and related flags to the indicated ostream."""
    def write_switch_flags(self, out: ostream, indent_level: int) -> None:
        """Writes the <Switch> flag and related flags to the indicated ostream."""
    def write_object_types(self, out: ostream, indent_level: int) -> None:
        """Writes just the <ObjectTypes> entries, if any, to the indicated ostream."""
    def write_decal_flags(self, out: ostream, indent_level: int) -> None:
        """Writes the flags related to decaling, if any."""
    def write_tags(self, out: ostream, indent_level: int) -> None:
        """Writes just the <Tag> entries, if any, to the indicated ostream."""
    def write_render_mode(self, out: ostream, indent_level: int) -> None:
        """Writes the flags inherited from EggRenderMode and similar flags that
        control obscure render effects.
        """
    def determine_alpha_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has an alpha_mode
        other than AM_unspecified.  Returns a valid EggRenderMode pointer if one is
        found, or NULL otherwise.
        """
    def determine_depth_write_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has a
        depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_depth_test_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has a
        depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_visibility_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has a
        visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_depth_offset(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has a depth_offset
        specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
        otherwise.
        """
    def determine_draw_order(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has a draw_order
        specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
        otherwise.
        """
    def determine_bin(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this group that has a bin
        specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
        otherwise.
        """
    def set_group_type(self, type: _EggGroup_GroupType) -> None: ...
    def get_group_type(self) -> _EggGroup_GroupType: ...
    def is_instance_type(self) -> bool:
        """Returns true if this group is an instance type node; i.e.  it begins the
        root of a local coordinate space.  This is not related to instancing
        (multiple copies of a node in a scene graph).

        This also includes the case of the node including a billboard flag without
        an explicit center, which implicitly makes the node behave like an
        instance.
        """
    def set_billboard_type(self, type: _EggGroup_BillboardType) -> None: ...
    def get_billboard_type(self) -> _EggGroup_BillboardType: ...
    def set_billboard_center(self, billboard_center: DoubleVec3Like) -> None:
        """Sets the point around which the billboard will rotate, if this node
        contains a billboard specification.

        If a billboard type is given but no billboard_center is specified, then the
        group node is treated as an <Instance>, and the billboard rotates around
        the origin.  If, however, a billboard_center is specified, then the group
        node is *not* treated as an <Instance>, and the billboard rotates around
        the specified point.

        The point is in the same coordinate system as the vertices of this node:
        usually global, but possibly local if there is an <Instance> somewhere
        above.  Specifically, this is the coordinate system defined by
        get_vertex_frame().
        """
    def clear_billboard_center(self) -> None: ...
    def has_billboard_center(self) -> bool: ...
    def get_billboard_center(self) -> LPoint3d: ...
    def set_cs_type(self, type: _EggGroup_CollisionSolidType) -> None: ...
    def get_cs_type(self) -> _EggGroup_CollisionSolidType: ...
    def set_collide_flags(self, flags: int) -> None: ...
    def get_collide_flags(self) -> _EggGroup_CollideFlags: ...
    def set_collision_name(self, collision_name: str) -> None: ...
    def clear_collision_name(self) -> None: ...
    def has_collision_name(self) -> bool: ...
    def get_collision_name(self) -> str: ...
    def set_dcs_type(self, type: _EggGroup_DCSType) -> None: ...
    def get_dcs_type(self) -> _EggGroup_DCSType: ...
    def has_dcs_type(self) -> bool:
        """Returns true if the specified DCS type is not DC_none and not
        DC_unspecified.
        """
    def set_dart_type(self, type: _EggGroup_DartType) -> None: ...
    def get_dart_type(self) -> _EggGroup_DartType: ...
    def set_switch_flag(self, flag: bool) -> None: ...
    def get_switch_flag(self) -> bool: ...
    def set_switch_fps(self, fps: float) -> None: ...
    def get_switch_fps(self) -> float: ...
    def add_object_type(self, object_type: str) -> None: ...
    def clear_object_types(self) -> None: ...
    def get_num_object_types(self) -> int: ...
    def get_object_type(self, index: int) -> str: ...
    def has_object_type(self, object_type: str) -> bool:
        """Returns true if the indicated object type has been added to the group, or
        false otherwise.
        """
    def remove_object_type(self, object_type: str) -> bool:
        """Removes the first instance of the indicated object type from the group if
        it is present.  Returns true if the object type was found and removed,
        false otherwise.
        """
    def set_model_flag(self, flag: bool) -> None: ...
    def get_model_flag(self) -> bool: ...
    def set_texlist_flag(self, flag: bool) -> None: ...
    def get_texlist_flag(self) -> bool: ...
    def set_nofog_flag(self, flag: bool) -> None: ...
    def get_nofog_flag(self) -> bool: ...
    def set_decal_flag(self, flag: bool) -> None: ...
    def get_decal_flag(self) -> bool: ...
    def set_direct_flag(self, flag: bool) -> None: ...
    def get_direct_flag(self) -> bool: ...
    def set_portal_flag(self, flag: bool) -> None: ...
    def get_portal_flag(self) -> bool: ...
    def set_occluder_flag(self, flag: bool) -> None: ...
    def get_occluder_flag(self) -> bool: ...
    def set_polylight_flag(self, flag: bool) -> None: ...
    def get_polylight_flag(self) -> bool: ...
    def set_indexed_flag(self, flag: bool) -> None:
        """If this flag is true, geometry at this node and below will be generated as
        indexed geometry.
        """
    def clear_indexed_flag(self) -> None: ...
    def has_indexed_flag(self) -> bool: ...
    def get_indexed_flag(self) -> bool: ...
    def set_collide_mask(self, mask: CollideMask | int) -> None: ...
    def clear_collide_mask(self) -> None: ...
    def has_collide_mask(self) -> bool: ...
    def get_collide_mask(self) -> CollideMask: ...
    def set_from_collide_mask(self, mask: CollideMask | int) -> None: ...
    def clear_from_collide_mask(self) -> None: ...
    def has_from_collide_mask(self) -> bool: ...
    def get_from_collide_mask(self) -> CollideMask: ...
    def set_into_collide_mask(self, mask: CollideMask | int) -> None: ...
    def clear_into_collide_mask(self) -> None: ...
    def has_into_collide_mask(self) -> bool: ...
    def get_into_collide_mask(self) -> CollideMask: ...
    def set_blend_mode(self, blend_mode: _EggGroup_BlendMode) -> None: ...
    def get_blend_mode(self) -> _EggGroup_BlendMode: ...
    def set_blend_operand_a(self, blend_operand_a: _EggGroup_BlendOperand) -> None: ...
    def get_blend_operand_a(self) -> _EggGroup_BlendOperand: ...
    def set_blend_operand_b(self, blend_operand_b: _EggGroup_BlendOperand) -> None: ...
    def get_blend_operand_b(self) -> _EggGroup_BlendOperand: ...
    def set_blend_color(self, blend_color: Vec4Like) -> None: ...
    def clear_blend_color(self) -> None:
        """Removes the blend color specification."""
    def has_blend_color(self) -> bool:
        """Returns true if the blend color has been specified, false otherwise."""
    def get_blend_color(self) -> LColor:
        """Returns the blend color if one has been specified, or (0, 0, 0, 0) if one
        has not.
        """
    def set_lod(self, lod: EggSwitchCondition) -> None: ...
    def clear_lod(self) -> None: ...
    def has_lod(self) -> bool: ...
    def get_lod(self) -> EggSwitchCondition: ...
    def set_tag(self, key: str, value: str) -> None:
        """Associates a user-defined value with a user-defined key which is stored on
        the node.  This value has no meaning to Panda; but it is stored
        indefinitely on the node until it is requested again.  This value will be
        copied to the PandaNode that is created for this particular EggGroup if the
        egg file is loaded as a scene.

        Each unique key stores a different string value.  There is no effective
        limit on the number of different keys that may be stored or on the length
        of any one key's value.
        """
    def get_tag(self, key: str) -> str:
        """Retrieves the user-defined value that was previously set on this node for
        the particular key, if any.  If no value has been previously set, returns
        the empty string.
        """
    def has_tag(self, key: str) -> bool:
        """Returns true if a value has been defined on this node for the particular
        key (even if that value is the empty string), or false if no value has been
        set.
        """
    def clear_tag(self, key: str) -> None:
        """Removes the value defined for this key on this particular node.  After a
        call to clear_tag(), has_tag() will return false for the indicated key.
        """
    def get_default_pose(self) -> EggTransform:
        """Returns a read-only accessor to the initial pose transform.  This is the
        <DefaultPose> entry for a Joint, and defines only the initial transform
        pose for the unanimated joint; it has nothing to do with the group's
        <Transform> entry, which defines the (eventual) space of the group's
        vertices.
        """
    def modify_default_pose(self) -> EggTransform:
        """Returns a writable accessor to the initial pose transform.  This is the
        <DefaultPose> entry for a Joint, and defines only the initial transform
        pose for the unanimated joint; it has nothing to do with the group's
        <Transform> entry, which defines the (eventual) space of the group's
        vertices.
        """
    def set_default_pose(self, transform: EggTransform) -> None:
        """Replaces the initial pose transform.  This is the <DefaultPose> entry for a
        Joint, and defines only the initial transform pose for the unanimated
        joint; it has nothing to do with the group's <Transform> entry, which
        defines the (eventual) space of the group's vertices.
        """
    def clear_default_pose(self) -> None:
        """Removes the initial pose transform.  See set_default_pose()."""
    def set_scroll_u(self, u_speed: float) -> None: ...
    def set_scroll_v(self, v_speed: float) -> None: ...
    def set_scroll_w(self, w_speed: float) -> None: ...
    def set_scroll_r(self, r_speed: float) -> None: ...
    def get_scroll_u(self) -> float: ...
    def get_scroll_v(self) -> float: ...
    def get_scroll_w(self) -> float: ...
    def get_scroll_r(self) -> float: ...
    def has_scrolling_uvs(self) -> bool: ...
    def ref_vertex(self, vert: EggVertex, membership: float = ...) -> None:
        """Adds the vertex to the set of those referenced by the group, at the
        indicated membership level.  If the vertex is already being referenced,
        increases the membership amount by the indicated amount.
        """
    def unref_vertex(self, vert: EggVertex) -> None:
        """Removes the vertex from the set of those referenced by the group.  Does
        nothing if the vertex is not already reffed.
        """
    def unref_all_vertices(self) -> None:
        """Removes all vertices from the reference list."""
    def get_vertex_membership(self, vert: EggVertex) -> float:
        """Returns the amount of membership of the indicated vertex in this group.  If
        the vertex is not reffed by the group, returns 0.
        """
    def set_vertex_membership(self, vert: EggVertex, membership: float) -> None:
        """Explicitly sets the net membership of the indicated vertex in this group to
        the given value.
        """
    def steal_vrefs(self, other: EggGroup) -> None:
        """Moves all of the vertex references from the indicated other group into this
        one.  If a given vertex was previously shared by both groups, the relative
        memberships will be summed.
        """
    def test_vref_integrity(self) -> None: ...
    def add_group_ref(self, group: EggGroup) -> None:
        """Adds a new <Ref> entry to the group.  This declares an internal reference
        to another node, and is used to implement scene-graph instancing; it is
        only valid if the group_type is GT_instance.
        """
    def get_num_group_refs(self) -> int:
        """Returns the number of <Ref> entries within this group.  See
        add_group_ref().
        """
    def get_group_ref(self, n: int) -> EggGroup:
        """Returns the nth <Ref> entry within this group.  See add_group_ref()."""
    def remove_group_ref(self, n: int) -> None:
        """Removes the nth <Ref> entry within this group.  See add_group_ref()."""
    def clear_group_refs(self) -> None:
        """Removes all of the <Ref> entries within this group.  See add_group_ref()."""
    @staticmethod
    def string_group_type(strval: str) -> _EggGroup_GroupType:
        """Returns the GroupType value associated with the given string
        representation, or GT_invalid if the string does not match any known
        GroupType value.
        """
    @staticmethod
    def string_dart_type(strval: str) -> _EggGroup_DartType:
        """Returns the DartType value associated with the given string representation,
        or DT_none if the string does not match any known DartType value.
        """
    @staticmethod
    def string_dcs_type(strval: str) -> _EggGroup_DCSType:
        """Returns the DCSType value associated with the given string representation,
        or DC_unspecified if the string does not match any known DCSType value.
        """
    @staticmethod
    def string_billboard_type(strval: str) -> _EggGroup_BillboardType:
        """Returns the BillboardType value associated with the given string
        representation, or BT_none if the string does not match any known
        BillboardType value.
        """
    @staticmethod
    def string_cs_type(strval: str) -> _EggGroup_CollisionSolidType:
        """Returns the CollisionSolidType value associated with the given string
        representation, or CST_none if the string does not match any known
        CollisionSolidType value.
        """
    @staticmethod
    def string_collide_flags(strval: str) -> _EggGroup_CollideFlags:
        """Returns the CollideFlags value associated with the given string
        representation, or CF_none if the string does not match any known
        CollideFlags value.  This only recognizes a single keyword; it does not
        attempt to parse a string of keywords.
        """
    @staticmethod
    def string_blend_mode(strval: str) -> _EggGroup_BlendMode:
        """Returns the BlendMode value associated with the given string
        representation, or BM_none if the string does not match any known
        BlendMode.
        """
    @staticmethod
    def string_blend_operand(strval: str) -> _EggGroup_BlendOperand:
        """Returns the BlendOperand value associated with the given string
        representation, or BO_none if the string does not match any known
        BlendOperand.
        """
    def get_object_types(self) -> tuple[str, ...]: ...
    def get_group_refs(self) -> tuple[EggGroup, ...]: ...
    upcastToEggGroupNode = upcast_to_EggGroupNode
    upcastToEggRenderMode = upcast_to_EggRenderMode
    upcastToEggTransform = upcast_to_EggTransform
    writeBillboardFlags = write_billboard_flags
    writeCollideFlags = write_collide_flags
    writeModelFlags = write_model_flags
    writeSwitchFlags = write_switch_flags
    writeObjectTypes = write_object_types
    writeDecalFlags = write_decal_flags
    writeTags = write_tags
    writeRenderMode = write_render_mode
    determineAlphaMode = determine_alpha_mode
    determineDepthWriteMode = determine_depth_write_mode
    determineDepthTestMode = determine_depth_test_mode
    determineVisibilityMode = determine_visibility_mode
    determineDepthOffset = determine_depth_offset
    determineDrawOrder = determine_draw_order
    determineBin = determine_bin
    setGroupType = set_group_type
    getGroupType = get_group_type
    isInstanceType = is_instance_type
    setBillboardType = set_billboard_type
    getBillboardType = get_billboard_type
    setBillboardCenter = set_billboard_center
    clearBillboardCenter = clear_billboard_center
    hasBillboardCenter = has_billboard_center
    getBillboardCenter = get_billboard_center
    setCsType = set_cs_type
    getCsType = get_cs_type
    setCollideFlags = set_collide_flags
    getCollideFlags = get_collide_flags
    setCollisionName = set_collision_name
    clearCollisionName = clear_collision_name
    hasCollisionName = has_collision_name
    getCollisionName = get_collision_name
    setDcsType = set_dcs_type
    getDcsType = get_dcs_type
    hasDcsType = has_dcs_type
    setDartType = set_dart_type
    getDartType = get_dart_type
    setSwitchFlag = set_switch_flag
    getSwitchFlag = get_switch_flag
    setSwitchFps = set_switch_fps
    getSwitchFps = get_switch_fps
    addObjectType = add_object_type
    clearObjectTypes = clear_object_types
    getNumObjectTypes = get_num_object_types
    getObjectType = get_object_type
    hasObjectType = has_object_type
    removeObjectType = remove_object_type
    setModelFlag = set_model_flag
    getModelFlag = get_model_flag
    setTexlistFlag = set_texlist_flag
    getTexlistFlag = get_texlist_flag
    setNofogFlag = set_nofog_flag
    getNofogFlag = get_nofog_flag
    setDecalFlag = set_decal_flag
    getDecalFlag = get_decal_flag
    setDirectFlag = set_direct_flag
    getDirectFlag = get_direct_flag
    setPortalFlag = set_portal_flag
    getPortalFlag = get_portal_flag
    setOccluderFlag = set_occluder_flag
    getOccluderFlag = get_occluder_flag
    setPolylightFlag = set_polylight_flag
    getPolylightFlag = get_polylight_flag
    setIndexedFlag = set_indexed_flag
    clearIndexedFlag = clear_indexed_flag
    hasIndexedFlag = has_indexed_flag
    getIndexedFlag = get_indexed_flag
    setCollideMask = set_collide_mask
    clearCollideMask = clear_collide_mask
    hasCollideMask = has_collide_mask
    getCollideMask = get_collide_mask
    setFromCollideMask = set_from_collide_mask
    clearFromCollideMask = clear_from_collide_mask
    hasFromCollideMask = has_from_collide_mask
    getFromCollideMask = get_from_collide_mask
    setIntoCollideMask = set_into_collide_mask
    clearIntoCollideMask = clear_into_collide_mask
    hasIntoCollideMask = has_into_collide_mask
    getIntoCollideMask = get_into_collide_mask
    setBlendMode = set_blend_mode
    getBlendMode = get_blend_mode
    setBlendOperandA = set_blend_operand_a
    getBlendOperandA = get_blend_operand_a
    setBlendOperandB = set_blend_operand_b
    getBlendOperandB = get_blend_operand_b
    setBlendColor = set_blend_color
    clearBlendColor = clear_blend_color
    hasBlendColor = has_blend_color
    getBlendColor = get_blend_color
    setLod = set_lod
    clearLod = clear_lod
    hasLod = has_lod
    getLod = get_lod
    setTag = set_tag
    getTag = get_tag
    hasTag = has_tag
    clearTag = clear_tag
    getDefaultPose = get_default_pose
    modifyDefaultPose = modify_default_pose
    setDefaultPose = set_default_pose
    clearDefaultPose = clear_default_pose
    setScrollU = set_scroll_u
    setScrollV = set_scroll_v
    setScrollW = set_scroll_w
    setScrollR = set_scroll_r
    getScrollU = get_scroll_u
    getScrollV = get_scroll_v
    getScrollW = get_scroll_w
    getScrollR = get_scroll_r
    hasScrollingUvs = has_scrolling_uvs
    refVertex = ref_vertex
    unrefVertex = unref_vertex
    unrefAllVertices = unref_all_vertices
    getVertexMembership = get_vertex_membership
    setVertexMembership = set_vertex_membership
    stealVrefs = steal_vrefs
    testVrefIntegrity = test_vref_integrity
    addGroupRef = add_group_ref
    getNumGroupRefs = get_num_group_refs
    getGroupRef = get_group_ref
    removeGroupRef = remove_group_ref
    clearGroupRefs = clear_group_refs
    stringGroupType = string_group_type
    stringDartType = string_dart_type
    stringDcsType = string_dcs_type
    stringBillboardType = string_billboard_type
    stringCsType = string_cs_type
    stringCollideFlags = string_collide_flags
    stringBlendMode = string_blend_mode
    stringBlendOperand = string_blend_operand
    getObjectTypes = get_object_types
    getGroupRefs = get_group_refs

class EggBin(EggGroup):
    """A type of group node that holds related subnodes.  This is a special kind
    of node that will never be read in from an egg file, but can only exist in
    the egg scene graph if it is created via the use of an EggBinMaker.
    """

    def set_bin_number(self, bin_number: int) -> None: ...
    def get_bin_number(self) -> int: ...
    setBinNumber = set_bin_number
    getBinNumber = get_bin_number

class EggBinMaker(EggObject):
    """This is a handy class for collecting related nodes together.  It is an
    abstract class; to use it you must subclass off of it.  See the somewhat
    lengthy comment above.
    """

    def make_bins(self, root_group: EggGroupNode) -> int:
        """The main entry point to EggBinMaker.  Walks the egg scene graph beginning
        at the indicated root node, and moves all binnable nodes into EggBin
        objects.  Returns the number of EggBins created.
        """
    def prepare_node(self, node: EggNode) -> None:
        """May be overridden in derived classes to perform some setup work as each
        node is encountered.  This will be called once for each node in the egg
        hierarchy.
        """
    def get_bin_number(self, node: EggNode) -> int: ...
    def sorts_less(self, bin_number: int, a: EggNode, b: EggNode) -> bool:
        """May be overridden in derived classes to create additional bins within a
        particular bin number, based on some arbitrary property of nodes.  This
        function establishes an arbitrary but fixed ordering between nodes; if two
        nodes do not sort to the same position, different bins are created for each
        one (with the same bin number on each bin).
        """
    def collapse_group(self, group: EggGroup, bin_number: int) -> bool:
        """May be overridden in derived classes to specify whether a particular group
        node, apparently redundant, may be safely collapsed out.
        """
    def get_bin_name(self, bin_number: int, child: EggNode) -> str:
        """May be overridden in derived classes to define a name for each new bin,
        based on its bin number, and a sample child.
        """
    def make_bin(self, bin_number: int, child: EggNode, collapse_from: EggGroup) -> EggBin:
        """May be overridden in derived classes to construct a new EggBin object (or
        some derived class, if needed), and preload some initial data into as
        required.

        child is an arbitrary child of the bin, and collapse_from is the group the
        bin is being collapsed with, if any (implying collapse_group() returned
        true), or NULL if not.
        """
    makeBins = make_bins
    prepareNode = prepare_node
    getBinNumber = get_bin_number
    sortsLess = sorts_less
    collapseGroup = collapse_group
    getBinName = get_bin_name
    makeBin = make_bin

class EggComment(EggNode):
    """A comment that appears in an egg file within a <Comment> entry."""

    @overload
    def __init__(self, copy: EggComment) -> None: ...
    @overload
    def __init__(self, node_name: str, comment: str) -> None: ...
    @overload
    def assign(self, copy: EggComment) -> Self: ...
    @overload
    def assign(self, comment: str) -> Self: ...
    def set_comment(self, comment: str) -> None: ...
    def get_comment(self) -> str: ...
    setComment = set_comment
    getComment = get_comment

class EggFilenameNode(EggNode):
    """This is an egg node that contains a filename.  It references a physical
    file relative to the directory the egg file was loaded in.  It is a base
    class for EggTexture and EggExternalReference.
    """

    def get_default_extension(self) -> str:
        """Returns the default extension for this filename type."""
    def get_filename(self) -> Filename:
        """Returns a nonmodifiable reference to the filename."""
    def set_filename(self, filename: StrOrBytesPath) -> None: ...
    def get_fullpath(self) -> Filename:
        """Returns the full pathname to the file, if it is known; otherwise, returns
        the same thing as get_filename().

        This function simply returns whatever was set by the last call to
        set_fullpath().  This string is not written to the egg file; its main
        purpose is to record the full path to a filename (for instance, a texture
        filename) if it is known, for egg structures that are generated in-memory
        and then immediately converted to a scene graph.
        """
    def set_fullpath(self, fullpath: StrOrBytesPath) -> None:
        """Records the full pathname to the file, for the benefit of get_fullpath()."""
    getDefaultExtension = get_default_extension
    getFilename = get_filename
    setFilename = set_filename
    getFullpath = get_fullpath
    setFullpath = set_fullpath

class EggTexture(EggFilenameNode, EggRenderMode, EggTransform):  # type: ignore[misc]
    """Defines a texture map that may be applied to geometry."""

    E_basename: Final = 1
    EBasename: Final = 1
    E_extension: Final = 2
    EExtension: Final = 2
    E_dirname: Final = 4
    EDirname: Final = 4
    E_complete_filename: Final = 7
    ECompleteFilename: Final = 7
    E_transform: Final = 8
    ETransform: Final = 8
    E_attributes: Final = 16
    EAttributes: Final = 16
    E_tref_name: Final = 32
    ETrefName: Final = 32
    TT_unspecified: Final = 0
    TTUnspecified: Final = 0
    TT_1d_texture: Final = 1
    TT1dTexture: Final = 1
    TT_2d_texture: Final = 2
    TT2dTexture: Final = 2
    TT_3d_texture: Final = 3
    TT3dTexture: Final = 3
    TT_cube_map: Final = 4
    TTCubeMap: Final = 4
    F_unspecified: Final = 0
    FUnspecified: Final = 0
    F_rgba: Final = 1
    FRgba: Final = 1
    F_rgbm: Final = 2
    FRgbm: Final = 2
    F_rgba12: Final = 3
    FRgba12: Final = 3
    F_rgba8: Final = 4
    FRgba8: Final = 4
    F_rgba4: Final = 5
    FRgba4: Final = 5
    F_rgba5: Final = 6
    FRgba5: Final = 6
    F_rgb: Final = 7
    FRgb: Final = 7
    F_rgb12: Final = 8
    FRgb12: Final = 8
    F_rgb8: Final = 9
    FRgb8: Final = 9
    F_rgb5: Final = 10
    FRgb5: Final = 10
    F_rgb332: Final = 11
    FRgb332: Final = 11
    F_red: Final = 12
    FRed: Final = 12
    F_green: Final = 13
    FGreen: Final = 13
    F_blue: Final = 14
    FBlue: Final = 14
    F_alpha: Final = 15
    FAlpha: Final = 15
    F_luminance: Final = 16
    FLuminance: Final = 16
    F_luminance_alpha: Final = 17
    FLuminanceAlpha: Final = 17
    F_luminance_alphamask: Final = 18
    FLuminanceAlphamask: Final = 18
    F_srgb: Final = 19
    FSrgb: Final = 19
    F_srgb_alpha: Final = 20
    FSrgbAlpha: Final = 20
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
    WM_unspecified: Final = 0
    WMUnspecified: Final = 0
    WM_clamp: Final = 1
    WMClamp: Final = 1
    WM_repeat: Final = 2
    WMRepeat: Final = 2
    WM_mirror: Final = 3
    WMMirror: Final = 3
    WM_mirror_once: Final = 4
    WMMirrorOnce: Final = 4
    WM_border_color: Final = 5
    WMBorderColor: Final = 5
    FT_unspecified: Final = 0
    FTUnspecified: Final = 0
    FT_nearest: Final = 1
    FTNearest: Final = 1
    FT_linear: Final = 2
    FTLinear: Final = 2
    FT_nearest_mipmap_nearest: Final = 3
    FTNearestMipmapNearest: Final = 3
    FT_linear_mipmap_nearest: Final = 4
    FTLinearMipmapNearest: Final = 4
    FT_nearest_mipmap_linear: Final = 5
    FTNearestMipmapLinear: Final = 5
    FT_linear_mipmap_linear: Final = 6
    FTLinearMipmapLinear: Final = 6
    ET_unspecified: Final = 0
    ETUnspecified: Final = 0
    ET_modulate: Final = 1
    ETModulate: Final = 1
    ET_decal: Final = 2
    ETDecal: Final = 2
    ET_blend: Final = 3
    ETBlend: Final = 3
    ET_replace: Final = 4
    ETReplace: Final = 4
    ET_add: Final = 5
    ETAdd: Final = 5
    ET_blend_color_scale: Final = 6
    ETBlendColorScale: Final = 6
    ET_modulate_glow: Final = 7
    ETModulateGlow: Final = 7
    ET_modulate_gloss: Final = 8
    ETModulateGloss: Final = 8
    ET_normal: Final = 9
    ETNormal: Final = 9
    ET_normal_height: Final = 10
    ETNormalHeight: Final = 10
    ET_glow: Final = 11
    ETGlow: Final = 11
    ET_gloss: Final = 12
    ETGloss: Final = 12
    ET_height: Final = 13
    ETHeight: Final = 13
    ET_selector: Final = 14
    ETSelector: Final = 14
    ET_normal_gloss: Final = 15
    ETNormalGloss: Final = 15
    ET_emission: Final = 16
    ETEmission: Final = 16
    CM_unspecified: Final = 0
    CMUnspecified: Final = 0
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
    CC_rgb: Final = 0
    CCRgb: Final = 0
    CC_alpha: Final = 1
    CCAlpha: Final = 1
    CC_num_channels: Final = 2
    CCNumChannels: Final = 2
    CI_num_indices: Final = 3
    CINumIndices: Final = 3
    CS_unspecified: Final = 0
    CSUnspecified: Final = 0
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
    CO_unspecified: Final = 0
    COUnspecified: Final = 0
    CO_src_color: Final = 1
    COSrcColor: Final = 1
    CO_one_minus_src_color: Final = 2
    COOneMinusSrcColor: Final = 2
    CO_src_alpha: Final = 3
    COSrcAlpha: Final = 3
    CO_one_minus_src_alpha: Final = 4
    COOneMinusSrcAlpha: Final = 4
    TG_unspecified: Final = 0
    TGUnspecified: Final = 0
    TG_eye_sphere_map: Final = 1
    TGEyeSphereMap: Final = 1
    TG_world_cube_map: Final = 2
    TGWorldCubeMap: Final = 2
    TG_eye_cube_map: Final = 3
    TGEyeCubeMap: Final = 3
    TG_world_normal: Final = 4
    TGWorldNormal: Final = 4
    TG_eye_normal: Final = 5
    TGEyeNormal: Final = 5
    TG_world_position: Final = 6
    TGWorldPosition: Final = 6
    TG_eye_position: Final = 7
    TGEyePosition: Final = 7
    TG_point_sprite: Final = 8
    TGPointSprite: Final = 8
    QL_unspecified: Final = 0
    QLUnspecified: Final = 0
    QL_default: Final = 1
    QLDefault: Final = 1
    QL_fastest: Final = 2
    QLFastest: Final = 2
    QL_normal: Final = 3
    QLNormal: Final = 3
    QL_best: Final = 4
    QLBest: Final = 4
    texture_type: _EggTexture_TextureType
    format: _EggTexture_Format
    compression_mode: _EggTexture_CompressionMode
    wrap_mode: _EggTexture_WrapMode
    wrap_u: _EggTexture_WrapMode
    wrap_v: _EggTexture_WrapMode
    wrap_w: _EggTexture_WrapMode
    minfilter: _EggTexture_FilterType
    magfilter: _EggTexture_FilterType
    anisotropic_degree: int
    env_type: _EggTexture_EnvType
    saved_result: bool
    tex_gen: _EggTexture_TexGen
    quality_level: _EggTexture_QualityLevel
    stage_name: str
    priority: int
    color: LColor
    border_color: LColor
    uv_name: str
    rgb_scale: int
    alpha_scale: int
    alpha_filename: Filename
    alpha_fullpath: Filename
    alpha_file_channel: int
    multiview: bool
    num_views: int
    read_mipmaps: bool
    min_lod: float
    max_lod: float
    lod_bias: float
    @property
    def multitexture_sort(self) -> int: ...
    @overload
    def __init__(self, copy: EggTexture) -> None: ...
    @overload
    def __init__(self, tref_name: str, filename: StrOrBytesPath) -> None: ...
    def upcast_to_EggFilenameNode(self) -> EggFilenameNode: ...
    def upcast_to_EggRenderMode(self) -> EggRenderMode: ...
    def upcast_to_EggTransform(self) -> EggTransform: ...
    def write(self, out: ostream, indent_level: int) -> None:  # type: ignore[override]
        """Writes the texture definition to the indicated output stream in Egg format."""
    def is_equivalent_to(self, other: EggTexture, eq: int) -> bool:
        """Returns true if the two textures are equivalent in all relevant properties
        (according to eq), false otherwise.

        The Equivalence parameter, eq, should be set to the bitwise OR of the
        following properties, according to what you consider relevant:

        EggTexture::E_basename: The basename part of the texture filename, without
        the directory prefix *or* the filename extension.

        EggTexture::E_extension: The extension part of the texture filename.

        EggTexture::E_dirname: The directory prefix of the texture filename.

        EggTexture::E_complete_filename: The union of the above three; that is, the
        complete filename, with directory, basename, and extension.

        EggTexture::E_transform: The texture matrix.

        EggTexture::E_attributes: All remaining texture attributes (mode, mipmap,
        etc.) except TRef name.

        EggTexture::E_tref_name: The TRef name.
        """
    def sorts_less_than(self, other: EggTexture, eq: int) -> bool:
        """An ordering operator to compare two textures for sorting order.  This
        imposes an arbitrary ordering useful to identify unique textures, according
        to the indicated Equivalence factor.  See is_equivalent_to().
        """
    def has_alpha_channel(self, num_components: int) -> bool:
        """Given the number of color components (channels) in the image file as
        actually read from the disk, return true if this texture seems to have an
        alpha channel or not.  This depends on the EggTexture's format as well as
        the number of channels.
        """
    def set_texture_type(self, texture_type: _EggTexture_TextureType) -> None: ...
    def get_texture_type(self) -> _EggTexture_TextureType: ...
    def set_format(self, format: _EggTexture_Format) -> None: ...
    def get_format(self) -> _EggTexture_Format: ...
    def set_compression_mode(self, mode: _EggTexture_CompressionMode) -> None: ...
    def get_compression_mode(self) -> _EggTexture_CompressionMode: ...
    def set_wrap_mode(self, mode: _EggTexture_WrapMode) -> None: ...
    def get_wrap_mode(self) -> _EggTexture_WrapMode: ...
    def set_wrap_u(self, mode: _EggTexture_WrapMode) -> None: ...
    def get_wrap_u(self) -> _EggTexture_WrapMode:
        """Returns the amount specified for U wrap.  This may be unspecified, even if
        there is an overall wrap value.
        """
    def determine_wrap_u(self) -> _EggTexture_WrapMode:
        """Determines the appropriate wrap in the U direction.  This is different from
        get_wrap_u() in that if the U wrap is unspecified, it returns the overall
        wrap value.
        """
    def set_wrap_v(self, mode: _EggTexture_WrapMode) -> None: ...
    def get_wrap_v(self) -> _EggTexture_WrapMode:
        """Returns the amount specified for V wrap.  This may be unspecified, even if
        there is an overall wrap value.
        """
    def determine_wrap_v(self) -> _EggTexture_WrapMode:
        """Determines the appropriate wrap in the V direction.  This is different from
        get_wrap_v() in that if the V wrap is unspecified, it returns the overall
        wrap value.
        """
    def set_wrap_w(self, mode: _EggTexture_WrapMode) -> None: ...
    def get_wrap_w(self) -> _EggTexture_WrapMode:
        """Returns the amount specified for W wrap.  This may be unspecified, even if
        there is an overall wrap value.
        """
    def determine_wrap_w(self) -> _EggTexture_WrapMode:
        """Determines the appropriate wrap in the W direction.  This is different from
        get_wrap_w() in that if the W wrap is unspecified, it returns the overall
        wrap value.
        """
    def set_minfilter(self, type: _EggTexture_FilterType) -> None: ...
    def get_minfilter(self) -> _EggTexture_FilterType: ...
    def set_magfilter(self, type: _EggTexture_FilterType) -> None: ...
    def get_magfilter(self) -> _EggTexture_FilterType: ...
    def set_anisotropic_degree(self, anisotropic_degree: int) -> None:
        """Sets the degree of anisotropic filtering for this texture.  1 is off;
        higher levels indicate filtering in effect.
        """
    def clear_anisotropic_degree(self) -> None:
        """Removes the specification of anisotropic filtering from the texture."""
    def has_anisotropic_degree(self) -> bool:
        """Returns true if a value for the anisotropic filtering degree has been
        specified for this texture, false otherwise.
        """
    def get_anisotropic_degree(self) -> int:
        """Returns the anisotropic filtering degree that has been specified for this
        texture, or 0 if nothing has been specified.
        """
    def set_env_type(self, type: _EggTexture_EnvType) -> None: ...
    def get_env_type(self) -> _EggTexture_EnvType: ...
    def affects_polygon_alpha(self) -> bool:
        """Returns true if this texture's environment type or combine mode allows the
        texture to have an effect on the polygon's alpha values, false otherwise.
        """
    def set_combine_mode(self, channel: _EggTexture_CombineChannel, cm: _EggTexture_CombineMode) -> None: ...
    def get_combine_mode(self, channel: _EggTexture_CombineChannel) -> _EggTexture_CombineMode: ...
    def set_combine_source(self, channel: _EggTexture_CombineChannel, n: int, cs: _EggTexture_CombineSource) -> None: ...
    def get_combine_source(self, channel: _EggTexture_CombineChannel, n: int) -> _EggTexture_CombineSource: ...
    def set_combine_operand(self, channel: _EggTexture_CombineChannel, n: int, co: _EggTexture_CombineOperand) -> None: ...
    def get_combine_operand(self, channel: _EggTexture_CombineChannel, n: int) -> _EggTexture_CombineOperand: ...
    def set_saved_result(self, saved_result: bool) -> None:
        """Sets the saved_result flag.  When this is true, the output of this stage is
        not part of the normal pipeline--that is, it will not be supplied as the
        "previous" source for the next texture stage--but it will instead be
        supplied as the "last_saved_result" source for any future stages, until the
        next TextureStage with a saved_result set true is encountered.

        This can be used to reuse the results of this texture stage as input to
        more than one stage later in the pipeline.

        The last texture in the pipeline (the one with the highest sort value)
        should not have this flag set.
        """
    def get_saved_result(self) -> bool:
        """Returns the current setting of the saved_result flag.  See
        set_saved_result().
        """
    def set_tex_gen(self, tex_gen: _EggTexture_TexGen) -> None: ...
    def get_tex_gen(self) -> _EggTexture_TexGen: ...
    def set_quality_level(self, quality_level: _EggTexture_QualityLevel) -> None: ...
    def get_quality_level(self) -> _EggTexture_QualityLevel: ...
    def set_stage_name(self, stage_name: str) -> None:
        """Specifies the particular TextureStage this texture will be rendered on by
        name.  If this is omitted, the texture will be rendered on the default
        TextureStage, unless some other stage-specific property is specificied, in
        which case the texture will be rendered on a TextureStage with the same
        name as the tref.  This is in support of multitexturing.

        Each different TextureStage in the world must be uniquely named.
        """
    def clear_stage_name(self) -> None:
        """Removes the named TextureStage specification."""
    def has_stage_name(self) -> bool:
        """Returns true if a stage name has been explicitly specified for this
        texture, false otherwise.
        """
    def get_stage_name(self) -> str:
        """Returns the stage name that has been specified for this texture, or the
        tref name if no texture stage has explicitly been specified.
        """
    def set_priority(self, priority: int) -> None:
        """Sets the importance of this texture with respect to other textures also
        applied on the same geometry.  This is only meaningful in the presence of
        multitexturing.
        """
    def clear_priority(self) -> None:
        """Removes the specification of multitexture priority from the texture.  The
        default priority value is 0.
        """
    def has_priority(self) -> bool:
        """Returns true if a priority value for multitexture importance has been
        specified for the texture, false otherwise.
        """
    def get_priority(self) -> int:
        """Returns the multitexture importance value that has been specified for the
        texture, or 0 if no priority value has been specified.
        """
    def set_color(self, color: Vec4Like) -> None: ...
    def clear_color(self) -> None: ...
    def has_color(self) -> bool:
        """Returns true if a blend color has been specified for the texture."""
    def get_color(self) -> LColor:
        """Returns the blend color if one has been specified, or (0, 0, 0, 1)
        otherwise.
        """
    def set_border_color(self, border_color: Vec4Like) -> None: ...
    def clear_border_color(self) -> None: ...
    def has_border_color(self) -> bool:
        """Returns true if a border color has been specified for the texture."""
    def get_border_color(self) -> LColor:
        """Returns the border color if one has been specified, or (0, 0, 0, 1)
        otherwise.
        """
    def set_uv_name(self, uv_name: str) -> None:
        """Specifies the named set of texture coordinates that this texture will use
        when it is applied to geometry.  Geometry may have multiple sets of texture
        coordinates defined, by name.

        If this is not specified for a particular texture, the default set of
        texture coordinates will be used.
        """
    def clear_uv_name(self) -> None:
        """Removes the restriction to a particular named set of texture coordinates
        and restores the texture to using the default texture coordinates.
        """
    def has_uv_name(self) -> bool:
        """Returns true if a texcoord name has been explicitly specified for this
        texture, false otherwise.
        """
    def get_uv_name(self) -> str:
        """Returns the texcoord name that has been specified for this texture, or the
        empty string if no texcoord name has explicitly been specified.
        """
    def set_rgb_scale(self, rgb_scale: int) -> None:
        """Sets an additional factor that will scale all three r, g, b components
        after the texture has been applied.  This is used only when a combine mode
        is in effect.

        The only legal values are 1, 2, or 4.
        """
    def clear_rgb_scale(self) -> None:
        """Removes the rgb_scale from the texture and restores it to the default value
        of 1.
        """
    def has_rgb_scale(self) -> bool:
        """Returns true if an rgb_scale has been specified for the texture, false
        otherwise.
        """
    def get_rgb_scale(self) -> int:
        """Returns the rgb_scale value that has been specified for the texture, or 1
        if no rgb_scale value has been specified.
        """
    def set_alpha_scale(self, alpha_scale: int) -> None:
        """Sets an additional factor that will scale the alpha component after the
        texture has been applied.  This is used only when a combine mode is in
        effect.

        The only legal values are 1, 2, or 4.
        """
    def clear_alpha_scale(self) -> None:
        """Removes the alpha_scale from the texture and restores it to the default
        value of 1.
        """
    def has_alpha_scale(self) -> bool:
        """Returns true if an alpha_scale has been specified for the texture, false
        otherwise.
        """
    def get_alpha_scale(self) -> int:
        """Returns the alpha_scale value that has been specified for the texture, or 1
        if no alpha_scale value has been specified.
        """
    def set_alpha_filename(self, filename: StrOrBytesPath) -> None:
        """Specifies a separate file that will be loaded in with the 1- or 3-component
        texture and applied as the alpha channel.  This is useful when loading
        textures from file formats that do not support alpha, for instance jpg.
        """
    def clear_alpha_filename(self) -> None: ...
    def has_alpha_filename(self) -> bool:
        """Returns true if a separate file for the alpha component has been applied,
        false otherwise.  See set_alpha_filename().
        """
    def get_alpha_filename(self) -> Filename:
        """Returns the separate file assigned for the alpha channel.  It is an error
        to call this unless has_alpha_filename() returns true.  See
        set_alpha_filename().
        """
    def set_alpha_fullpath(self, fullpath: StrOrBytesPath) -> None:
        """Records the full pathname to the file, for the benefit of
        get_alpha_fullpath().
        """
    def get_alpha_fullpath(self) -> Filename:
        """Returns the full pathname to the alpha file, if it is known; otherwise,
        returns the same thing as get_alpha_filename().

        This function simply returns whatever was set by the last call to
        set_alpha_fullpath().  This string is not written to the egg file; its main
        purpose is to record the full path to the alpha filename if it is known,
        for egg structures that are generated in-memory and then immediately
        converted to a scene graph.
        """
    def set_alpha_file_channel(self, alpha_file_channel: int) -> None:
        """If a separate alpha-file is specified, this indicates which channel number
        should be extracted from this file to derive the alpha channel for the
        final image.  The default is 0, which means the grayscale combination of r,
        g, b.  Otherwise, this should be the 1-based channel number, for instance
        1, 2, or 3 for r, g, or b, respectively, or 4 for the alpha channel of a
        four-component image.
        """
    def clear_alpha_file_channel(self) -> None:
        """Removes the specification of a particular channel to use from the alpha-
        file image.
        """
    def has_alpha_file_channel(self) -> bool:
        """Returns true if a particular channel has been specified for the alpha-file
        image, false otherwise.
        """
    def get_alpha_file_channel(self) -> int:
        """Returns the particular channel that has been specified for the alpha-file
        image, or 0 if no channel has been specified.  See
        set_alpha_file_channel().
        """
    def set_multiview(self, multiview: bool) -> None:
        """Sets the multiview flag.

        If multiview is true, the filename should contain a hash mark ('#'), which
        will be filled in with the view number; and a multiview texture will be
        defined with a series of images, one for each view.

        A multiview texture is most often used for stereo textures, but other uses
        are also possible, such as for texture animation.
        """
    def get_multiview(self) -> bool:
        """Returns the current setting of the multiview flag.  See set_multiview()."""
    def set_num_views(self, num_views: int) -> None:
        """When loading a 3-D multiview texture, this parameter is necessary to
        specify how many views will be expected.  The z size is determined
        implicitly from the number of images loaded.
        """
    def clear_num_views(self) -> None:
        """Removes the specification of the number of views for a 3-D multiview
        texture.
        """
    def has_num_views(self) -> bool:
        """Returns true if the number of views has been specified for the 3-D
        multiview texture, false otherwise.
        """
    def get_num_views(self) -> int:
        """Returns the specified number of views specified for the 3-D multiview
        texture.  See set_num_views().
        """
    def set_read_mipmaps(self, read_mipmaps: bool) -> None:
        """Sets the read_mipmaps flag.

        If read_mipmaps is true, the filename should contain a hash mark ('#'),
        which will be filled in with the mipmap level number; and the texture will
        be defined with a series of images, one for each mipmap level.

        If the filename is of a type that already requires a hash mark, such as a
        cube map or a 3-d texture, then the filename should now require two hash
        marks, and the first one indicates the mipmap level number, while the
        second indicates the face number or 3-d level number.
        """
    def get_read_mipmaps(self) -> bool:
        """Returns the current setting of the read_mipmaps flag.  See
        set_read_mipmaps().
        """
    def set_min_lod(self, min_lod: float) -> None:
        """Sets the minimum mipmap level that may be sampled."""
    def clear_min_lod(self) -> None:
        """Removes the specification of a minimum mipmap level from the texture."""
    def has_min_lod(self) -> bool:
        """Returns true if a value for the minimum mipmap level has been specified for
        this texture, false otherwise.
        """
    def get_min_lod(self) -> float:
        """Returns the minimum mipmap level that has been specified for this texture."""
    def set_max_lod(self, max_lod: float) -> None:
        """Sets the maximum mipmap level that may be sampled."""
    def clear_max_lod(self) -> None:
        """Removes the specification of a maximum mipmap level from the texture."""
    def has_max_lod(self) -> bool:
        """Returns true if a value for the maximum mipmap level has been specified for
        this texture, false otherwise.
        """
    def get_max_lod(self) -> float:
        """Returns the maximum mipmap level that has been specified for this texture."""
    def set_lod_bias(self, lod_bias: float) -> None:
        """Sets the mipmap level bias that is added to the mipmap level to be sampled."""
    def clear_lod_bias(self) -> None:
        """Removes the specification of a maximum mipmap level from the texture."""
    def has_lod_bias(self) -> bool:
        """Returns true if a value for the maximum mipmap level has been specified for
        this texture, false otherwise.
        """
    def get_lod_bias(self) -> float:
        """Returns the maximum mipmap level that has been specified for this texture."""
    def clear_multitexture(self) -> None:
        """Resets the multitexture flags set by multitexture_over().  After this call,
        get_multitexture() will return false, and get_multitexture_sort() will
        return 0.
        """
    def multitexture_over(self, other: EggTexture) -> bool:
        """Indicates that this texture should be layered on top of the other texture.
        This will guarantee that this->get_multitexture_sort() >
        other->get_multitexture_sort(), at least until clear_multitexture() is
        called on either one.

        The return value is true if successful, or false if there is a failure
        because the other texture was already layered on top of this one (or there
        is a three- or more-way cycle).
        """
    def get_multitexture_sort(self) -> int:
        """Returns an integer that represents the depth to which this texture is
        layered on all other textures in the egg file.  In general, if texture A is
        layered over texture B, then sort(A) > sort(B).  If texture A is never
        layered over any other texture, then sort(A) == 0.  More than that is
        difficult to guarantee.
        """
    @staticmethod
    def string_texture_type(string: str) -> _EggTexture_TextureType:
        """Returns the Texture_ype value associated with the given string
        representation, or TT_unspecified if the string does not match any known
        TextureType value.
        """
    @staticmethod
    def string_format(string: str) -> _EggTexture_Format:
        """Returns the Format value associated with the given string representation,
        or F_unspecified if the string does not match any known Format value.
        """
    @staticmethod
    def string_compression_mode(string: str) -> _EggTexture_CompressionMode:
        """Returns the CompressionMode value associated with the given string
        representation, or CM_default if the string does not match any known
        CompressionMode value.
        """
    @staticmethod
    def string_wrap_mode(string: str) -> _EggTexture_WrapMode:
        """Returns the WrapMode value associated with the given string representation,
        or WM_unspecified if the string does not match any known WrapMode value.
        """
    @staticmethod
    def string_filter_type(string: str) -> _EggTexture_FilterType:
        """Returns the FilterType value associated with the given string
        representation, or FT_unspecified if the string does not match any known
        FilterType value.
        """
    @staticmethod
    def string_env_type(string: str) -> _EggTexture_EnvType:
        """Returns the EnvType value associated with the given string representation,
        or ET_unspecified if the string does not match any known EnvType value.
        """
    @staticmethod
    def string_combine_mode(string: str) -> _EggTexture_CombineMode:
        """Returns the CombineMode value associated with the given string
        representation, or CM_unspecified if the string does not match any known
        CombineMode value.
        """
    @staticmethod
    def string_combine_source(string: str) -> _EggTexture_CombineSource:
        """Returns the CombineSource value associated with the given string
        representation, or CS_unspecified if the string does not match any known
        CombineSource value.
        """
    @staticmethod
    def string_combine_operand(string: str) -> _EggTexture_CombineOperand:
        """Returns the CombineOperand value associated with the given string
        representation, or CO_unspecified if the string does not match any known
        CombineOperand value.
        """
    @staticmethod
    def string_tex_gen(string: str) -> _EggTexture_TexGen:
        """Returns the TexGen value associated with the given string representation,
        or ET_unspecified if the string does not match any known TexGen value.
        """
    @staticmethod
    def string_quality_level(string: str) -> _EggTexture_QualityLevel:
        """Returns the TexGen value associated with the given string representation,
        or ET_unspecified if the string does not match any known TexGen value.
        """
    upcastToEggFilenameNode = upcast_to_EggFilenameNode
    upcastToEggRenderMode = upcast_to_EggRenderMode
    upcastToEggTransform = upcast_to_EggTransform
    isEquivalentTo = is_equivalent_to
    sortsLessThan = sorts_less_than
    hasAlphaChannel = has_alpha_channel
    setTextureType = set_texture_type
    getTextureType = get_texture_type
    setFormat = set_format
    getFormat = get_format
    setCompressionMode = set_compression_mode
    getCompressionMode = get_compression_mode
    setWrapMode = set_wrap_mode
    getWrapMode = get_wrap_mode
    setWrapU = set_wrap_u
    getWrapU = get_wrap_u
    determineWrapU = determine_wrap_u
    setWrapV = set_wrap_v
    getWrapV = get_wrap_v
    determineWrapV = determine_wrap_v
    setWrapW = set_wrap_w
    getWrapW = get_wrap_w
    determineWrapW = determine_wrap_w
    setMinfilter = set_minfilter
    getMinfilter = get_minfilter
    setMagfilter = set_magfilter
    getMagfilter = get_magfilter
    setAnisotropicDegree = set_anisotropic_degree
    clearAnisotropicDegree = clear_anisotropic_degree
    hasAnisotropicDegree = has_anisotropic_degree
    getAnisotropicDegree = get_anisotropic_degree
    setEnvType = set_env_type
    getEnvType = get_env_type
    affectsPolygonAlpha = affects_polygon_alpha
    setCombineMode = set_combine_mode
    getCombineMode = get_combine_mode
    setCombineSource = set_combine_source
    getCombineSource = get_combine_source
    setCombineOperand = set_combine_operand
    getCombineOperand = get_combine_operand
    setSavedResult = set_saved_result
    getSavedResult = get_saved_result
    setTexGen = set_tex_gen
    getTexGen = get_tex_gen
    setQualityLevel = set_quality_level
    getQualityLevel = get_quality_level
    setStageName = set_stage_name
    clearStageName = clear_stage_name
    hasStageName = has_stage_name
    getStageName = get_stage_name
    setPriority = set_priority
    clearPriority = clear_priority
    hasPriority = has_priority
    getPriority = get_priority
    setColor = set_color
    clearColor = clear_color
    hasColor = has_color
    getColor = get_color
    setBorderColor = set_border_color
    clearBorderColor = clear_border_color
    hasBorderColor = has_border_color
    getBorderColor = get_border_color
    setUvName = set_uv_name
    clearUvName = clear_uv_name
    hasUvName = has_uv_name
    getUvName = get_uv_name
    setRgbScale = set_rgb_scale
    clearRgbScale = clear_rgb_scale
    hasRgbScale = has_rgb_scale
    getRgbScale = get_rgb_scale
    setAlphaScale = set_alpha_scale
    clearAlphaScale = clear_alpha_scale
    hasAlphaScale = has_alpha_scale
    getAlphaScale = get_alpha_scale
    setAlphaFilename = set_alpha_filename
    clearAlphaFilename = clear_alpha_filename
    hasAlphaFilename = has_alpha_filename
    getAlphaFilename = get_alpha_filename
    setAlphaFullpath = set_alpha_fullpath
    getAlphaFullpath = get_alpha_fullpath
    setAlphaFileChannel = set_alpha_file_channel
    clearAlphaFileChannel = clear_alpha_file_channel
    hasAlphaFileChannel = has_alpha_file_channel
    getAlphaFileChannel = get_alpha_file_channel
    setMultiview = set_multiview
    getMultiview = get_multiview
    setNumViews = set_num_views
    clearNumViews = clear_num_views
    hasNumViews = has_num_views
    getNumViews = get_num_views
    setReadMipmaps = set_read_mipmaps
    getReadMipmaps = get_read_mipmaps
    setMinLod = set_min_lod
    clearMinLod = clear_min_lod
    hasMinLod = has_min_lod
    getMinLod = get_min_lod
    setMaxLod = set_max_lod
    clearMaxLod = clear_max_lod
    hasMaxLod = has_max_lod
    getMaxLod = get_max_lod
    setLodBias = set_lod_bias
    clearLodBias = clear_lod_bias
    hasLodBias = has_lod_bias
    getLodBias = get_lod_bias
    clearMultitexture = clear_multitexture
    multitextureOver = multitexture_over
    getMultitextureSort = get_multitexture_sort
    stringTextureType = string_texture_type
    stringFormat = string_format
    stringCompressionMode = string_compression_mode
    stringWrapMode = string_wrap_mode
    stringFilterType = string_filter_type
    stringEnvType = string_env_type
    stringCombineMode = string_combine_mode
    stringCombineSource = string_combine_source
    stringCombineOperand = string_combine_operand
    stringTexGen = string_tex_gen
    stringQualityLevel = string_quality_level

class EggMaterial(EggNode):
    E_attributes: Final = 1
    EAttributes: Final = 1
    E_mref_name: Final = 2
    EMrefName: Final = 2
    base: LColor
    diff: LColor
    amb: LColor
    emit: LColor
    spec: LColor
    shininess: float
    roughness: float
    metallic: float
    ior: float
    local: bool
    @overload
    def __init__(self, copy: EggMaterial) -> None: ...
    @overload
    def __init__(self, mref_name: str) -> None: ...
    def is_equivalent_to(self, other: EggMaterial, eq: int) -> bool:
        """Returns true if the two materials are equivalent in all relevant properties
        (according to eq), false otherwise.

        The Equivalence parameter, eq, should be set to the bitwise OR of the
        following properties, according to what you consider relevant:

        EggMaterial::E_attributes: All material attributes (diff, spec, etc.)
        except MRef name.

        EggMaterial::E_mref_name: The MRef name.
        """
    def sorts_less_than(self, other: EggMaterial, eq: int) -> bool:
        """An ordering operator to compare two materials for sorting order.  This
        imposes an arbitrary ordering useful to identify unique materials,
        according to the indicated Equivalence factor.  See is_equivalent_to().
        """
    def set_base(self, base: Vec4Like) -> None:
        """@since 1.10.0"""
    def clear_base(self) -> None:
        """@since 1.10.0"""
    def has_base(self) -> bool:
        """@since 1.10.0"""
    def get_base(self) -> LColor:
        """It is legal to call this even if has_base() returns false.  If so, it
        simply returns the default base color.

        @since 1.10.0
        """
    def set_diff(self, diff: Vec4Like) -> None: ...
    def clear_diff(self) -> None: ...
    def has_diff(self) -> bool: ...
    def get_diff(self) -> LColor:
        """It is legal to call this even if has_diff() returns false.  If so, it
        simply returns the default diff color.
        """
    def set_amb(self, amb: Vec4Like) -> None: ...
    def clear_amb(self) -> None: ...
    def has_amb(self) -> bool: ...
    def get_amb(self) -> LColor:
        """It is legal to call this even if has_amb() returns false.  If so, it simply
        returns the default amb color.
        """
    def set_emit(self, emit: Vec4Like) -> None: ...
    def clear_emit(self) -> None: ...
    def has_emit(self) -> bool: ...
    def get_emit(self) -> LColor:
        """It is legal to call this even if has_emit() returns false.  If so, it
        simply returns the default emit color.
        """
    def set_spec(self, spec: Vec4Like) -> None: ...
    def clear_spec(self) -> None: ...
    def has_spec(self) -> bool: ...
    def get_spec(self) -> LColor:
        """It is legal to call this even if has_spec() returns false.  If so, it
        simply returns the default spec color.
        """
    def set_shininess(self, shininess: float) -> None: ...
    def clear_shininess(self) -> None: ...
    def has_shininess(self) -> bool: ...
    def get_shininess(self) -> float: ...
    def set_roughness(self, roughness: float) -> None:
        """@since 1.10.0"""
    def clear_roughness(self) -> None:
        """@since 1.10.0"""
    def has_roughness(self) -> bool:
        """@since 1.10.0"""
    def get_roughness(self) -> float:
        """@since 1.10.0"""
    def set_metallic(self, metallic: float) -> None:
        """@since 1.10.0"""
    def clear_metallic(self) -> None:
        """@since 1.10.0"""
    def has_metallic(self) -> bool:
        """@since 1.10.0"""
    def get_metallic(self) -> float:
        """@since 1.10.0"""
    def set_ior(self, ior: float) -> None:
        """@since 1.10.0"""
    def clear_ior(self) -> None:
        """@since 1.10.0"""
    def has_ior(self) -> bool:
        """@since 1.10.0"""
    def get_ior(self) -> float:
        """@since 1.10.0"""
    def set_local(self, local: bool) -> None: ...
    def clear_local(self) -> None: ...
    def has_local(self) -> bool: ...
    def get_local(self) -> bool: ...
    isEquivalentTo = is_equivalent_to
    sortsLessThan = sorts_less_than
    setBase = set_base
    clearBase = clear_base
    hasBase = has_base
    getBase = get_base
    setDiff = set_diff
    clearDiff = clear_diff
    hasDiff = has_diff
    getDiff = get_diff
    setAmb = set_amb
    clearAmb = clear_amb
    hasAmb = has_amb
    getAmb = get_amb
    setEmit = set_emit
    clearEmit = clear_emit
    hasEmit = has_emit
    getEmit = get_emit
    setSpec = set_spec
    clearSpec = clear_spec
    hasSpec = has_spec
    getSpec = get_spec
    setShininess = set_shininess
    clearShininess = clear_shininess
    hasShininess = has_shininess
    getShininess = get_shininess
    setRoughness = set_roughness
    clearRoughness = clear_roughness
    hasRoughness = has_roughness
    getRoughness = get_roughness
    setMetallic = set_metallic
    clearMetallic = clear_metallic
    hasMetallic = has_metallic
    getMetallic = get_metallic
    setIor = set_ior
    clearIor = clear_ior
    hasIor = has_ior
    getIor = get_ior
    setLocal = set_local
    clearLocal = clear_local
    hasLocal = has_local
    getLocal = get_local

class EggPrimitive(EggNode, EggAttributes, EggRenderMode):  # type: ignore[misc]
    """A base class for any of a number of kinds of geometry primitives: polygons,
    point lights, nurbs patches, parametrics curves, etc.  Things with a set of
    vertices and some rendering properties like color.

    An EggPrimitive is an STL-style container of pointers to EggVertex's.  In
    fact, it IS a vector, and can be manipulated in all the ways that vectors
    can.  However, it is necessary that all vertices belong to the same vertex
    pool.
    """

    S_unknown: Final = 0
    SUnknown: Final = 0
    S_overall: Final = 1
    SOverall: Final = 1
    S_per_face: Final = 2
    SPerFace: Final = 2
    S_per_vertex: Final = 3
    SPerVertex: Final = 3
    material: EggMaterial
    bface_flag: bool
    @property
    def sort_name(self) -> str: ...
    @property
    def shading(self) -> _EggPrimitive_Shading: ...
    @property
    def connected_shading(self) -> _EggPrimitive_Shading: ...
    @property
    def textures(self) -> Sequence[EggTexture]: ...
    @property
    def vertices(self) -> MutableSequence[EggVertex]: ...
    @property
    def pool(self) -> EggVertexPool: ...
    def upcast_to_EggNode(self) -> EggNode: ...
    def upcast_to_EggAttributes(self) -> EggAttributes: ...
    def upcast_to_EggRenderMode(self) -> EggRenderMode: ...
    def make_copy(self) -> EggPrimitive: ...
    def determine_alpha_mode(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this primitive that has an
        alpha_mode other than AM_unspecified.  Returns a valid EggRenderMode
        pointer if one is found, or NULL otherwise.
        """
    def determine_depth_offset(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this primitive that has a
        depth_offset specified.  Returns a valid EggRenderMode pointer if one is
        found, or NULL otherwise.
        """
    def determine_draw_order(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this primitive that has a
        draw_order specified.  Returns a valid EggRenderMode pointer if one is
        found, or NULL otherwise.
        """
    def determine_bin(self) -> EggRenderMode:
        """Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
        some such object at this level or above this primitive that has a bin
        specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
        otherwise.
        """
    def get_sort_name(self) -> str:
        """Returns the name of the primitive for the purposes of sorting primitives
        into different groups, if there is one.

        Presently, this is defined as the primitive name itself, unless it begins
        with a digit.
        """
    def get_shading(self) -> _EggPrimitive_Shading:
        """Returns the shading properties apparent on this particular primitive.  This
        returns S_per_vertex if the vertices have colors or normals (and they are
        not all the same values), or for a simple primitive, S_overall otherwise.
        A composite primitive may also return S_per_face if the individual
        component primitives have colors or normals that are not all the same
        values.

        To get the most accurate results, you should call clear_shading() on all
        connected primitives (or on all primitives in the egg file), followed by
        get_shading() on each primitive.  You may find it easiest to call these
        methods on the EggData root node (they are defined on EggGroupNode).
        """
    def clear_connected_shading(self) -> None:
        """Resets the connected_shading member in this primitive, so that
        get_connected_shading() will recompute a new value.
        """
    def get_connected_shading(self) -> _EggPrimitive_Shading:
        """Determines what sort of shading properties this primitive's connected
        neighbors have.

        To get the most accurate results, you should first call
        clear_connected_shading() on all connected primitives (or on all primitives
        in the egg file). It might also be a good idea to call
        remove_unused_vertices() to ensure proper connectivity.

        You may find it easiest to call these other methods on the EggData root
        node (they are defined on EggGroupNode).
        """
    def set_texture(self, texture: EggTexture) -> None:
        """Replaces the current list of textures with the indicated texture.

        @deprecated This method is used in support of single-texturing only.
        Please use the multitexture variant add_texture instead.
        """
    def has_texture(self, texture: EggTexture = ...) -> bool:
        """`(self)`:
        Returns true if the primitive has any textures specified, false otherwise.

        @deprecated This method is used in support of single-texturing only.
        New code should be written to use the multitexture variants instead.

        `(self, texture: EggTexture)`:
        Returns true if the primitive has the particular indicated texture, false
        otherwise.
        """
    def get_texture(self, n: int = ...) -> EggTexture:
        """`(self)`:
        Returns the first texture on the primitive, if any, or NULL if there are no
        textures on the primitive.

        @deprecated This method is used in support of single-texturing only.
        New code should be written to use the multitexture variants instead.

        `(self, n: int)`:
        Returns the nth texture that has been applied to the primitive.
        """
    def add_texture(self, texture: EggTexture) -> None:
        """Applies the indicated texture to the primitive.

        Note that, in the case of multiple textures being applied to a single
        primitive, the order in which the textures are applied does not affect the
        rendering order; use EggTexture::set_sort() to specify that.
        """
    def clear_texture(self) -> None:
        """Removes any texturing from the primitive."""
    def get_num_textures(self) -> int:
        """Returns the number of textures applied to the primitive."""
    def set_material(self, material: EggMaterial) -> None:
        """Applies the indicated material to the primitive."""
    def clear_material(self) -> None:
        """Removes any material from the primitive."""
    def get_material(self) -> EggMaterial:
        """Returns a pointer to the applied material, or NULL if there is no material
        applied.
        """
    def has_material(self) -> bool:
        """Returns true if the primitive is materiald (and get_material() will return
        a real pointer), false otherwise (and get_material() will return NULL).
        """
    def set_bface_flag(self, flag: bool) -> None:
        """Sets the backfacing flag of the polygon.  If this is true, the polygon will
        be rendered so that both faces are visible; if it is false, only the front
        face of the polygon will be visible.
        """
    def get_bface_flag(self) -> bool:
        """Retrieves the backfacing flag of the polygon.  See set_bface_flag()."""
    def copy_attributes(self, other: EggAttributes) -> None:
        """Copies the rendering attributes from the indicated primitive."""
    def has_vertex_normal(self) -> bool:
        """Returns true if any vertex on the primitive has a specific normal set,
        false otherwise.

        If you call unify_attributes() first, this will also return false even if
        all the vertices were set to the same value (since unify_attributes()
        removes redundant vertex properties).
        """
    def has_vertex_color(self) -> bool:
        """Returns true if any vertex on the primitive has a specific color set, false
        otherwise.

        If you call unify_attributes() first, this will also return false even if
        all the vertices were set to the same value (since unify_attributes()
        removes redundant vertex properties).
        """
    def unify_attributes(self, shading: _EggPrimitive_Shading) -> None:
        """If the shading property is S_per_vertex, ensures that all vertices have a
        normal and a color, and the overall primitive does not.

        If the shading property is S_per_face, and this is a composite primitive,
        ensures that all components have a normal and a color, and the vertices and
        overall primitive do not.  (If this is a simple primitive, S_per_face works
        the same as S_overall, below).

        If the shading property is S_overall, ensures that no vertices or
        components have a normal or a color, and the overall primitive does (if any
        exists at all).

        After this call, either the primitive will have normals or its vertices
        will, but not both.  Ditto for colors.

        This may create redundant vertices in the vertex pool.
        """
    def apply_last_attribute(self) -> None:
        """Sets the last vertex of the triangle (or each component) to the primitive
        normal and/or color, if the primitive is flat-shaded.  This reflects the
        OpenGL convention of storing flat-shaded properties on the last vertex,
        although it is not usually a convention in Egg.

        This may introduce redundant vertices to the vertex pool.
        """
    def apply_first_attribute(self) -> None:
        """Sets the first vertex of the triangle (or each component) to the primitive
        normal and/or color, if the primitive is flat-shaded.  This reflects the
        DirectX convention of storing flat-shaded properties on the first vertex,
        although it is not usually a convention in Egg.

        This may introduce redundant vertices to the vertex pool.
        """
    def post_apply_flat_attribute(self) -> None:
        """Intended as a followup to apply_last_attribute(), this also sets an
        attribute on the first vertices of the primitive, if they don't already
        have an attribute set, just so they end up with *something*.
        """
    def reverse_vertex_ordering(self) -> None:
        """Reverses the ordering of the vertices in this primitive, if appropriate, in
        order to change the direction the polygon appears to be facing.  Does not
        adjust the surface normal, if any.
        """
    def cleanup(self) -> bool:
        """Cleans up modeling errors in whatever context this makes sense.  For
        instance, for a polygon, this calls remove_doubled_verts(true).  For a
        point, it calls remove_nonunique_verts().  Returns true if the primitive is
        valid, or false if it is degenerate.
        """
    def remove_doubled_verts(self, closed: bool) -> None:
        """Certain kinds of primitives, particularly polygons, don't like to have the
        same vertex repeated consecutively.  Unfortunately, some modeling programs
        (like MultiGen) make this an easy mistake to make.

        It's handy to have a function to remove these redundant vertices.  If
        closed is true, it also checks that the first and last vertices are not the
        same.

        This function identifies repeated vertices by position only; it does not
        consider any other properties, such as color or UV, significant in
        differentiating vertices.
        """
    def remove_nonunique_verts(self) -> None:
        """Removes any multiple appearances of the same vertex from the primitive.
        This primarily makes sense for a point primitive, which is really a
        collection of points and which doesn't make sense to include the same point
        twice, in any order.
        """
    def has_primitives(self) -> bool:
        """Returns true if there are any primitives (e.g.  polygons) defined within
        this group or below, false otherwise.
        """
    def joint_has_primitives(self) -> bool:
        """Returns true if there are any primitives (e.g.  polygons) defined within
        this group or below, but the search does not include nested joints.
        """
    def has_normals(self) -> bool:
        """Returns true if any of the primitives (e.g.  polygons) defined within this
        group or below have either face or vertex normals defined, false otherwise.
        """
    def clear(self) -> None:
        """Removes all of the vertices from the primitive."""
    def add_vertex(self, vertex: EggVertex) -> EggVertex:
        """Adds the indicated vertex to the end of the primitive's list of vertices,
        and returns it.
        """
    @overload
    def remove_vertex(self, vertex: EggVertex) -> EggVertex:
        """`(self, vertex: EggVertex)`:
        Removes the indicated vertex from the primitive and returns it.  If the
        vertex was not already in the primitive, does nothing and returns NULL.

        `(self, index: int)`:
        Removes the indicated vertex from the primitive.
        """
    @overload
    def remove_vertex(self, index: int) -> None: ...
    def copy_vertices(self, other: EggPrimitive) -> None:
        """Replaces the current primitive's list of vertices with a copy of the list
        of vertices on the other primitive.
        """
    def get_num_vertices(self) -> int:
        """These are shorthands if you don't want to use the iterators."""
    def get_vertex(self, index: int) -> EggVertex:
        """Returns a particular index based on its index number."""
    def set_vertex(self, index: int, vertex: EggVertex) -> None:
        """Replaces a particular vertex based on its index number in the list of
        vertices.  This is just a convenience function for people who don't want to
        mess with the iterators.
        """
    def insert_vertex(self, index: int, vertex: EggVertex) -> None:
        """Inserts a vertex at the given position."""
    def get_pool(self) -> EggVertexPool:
        """Returns the vertex pool associated with the vertices of the primitive, or
        NULL if the primitive has no vertices.
        """
    def test_vref_integrity(self) -> None: ...
    def get_textures(self) -> tuple[EggTexture, ...]: ...
    def get_vertices(self) -> tuple[EggVertex, ...]: ...
    upcastToEggNode = upcast_to_EggNode
    upcastToEggAttributes = upcast_to_EggAttributes
    upcastToEggRenderMode = upcast_to_EggRenderMode
    makeCopy = make_copy
    determineAlphaMode = determine_alpha_mode
    determineDepthOffset = determine_depth_offset
    determineDrawOrder = determine_draw_order
    determineBin = determine_bin
    getSortName = get_sort_name
    getShading = get_shading
    clearConnectedShading = clear_connected_shading
    getConnectedShading = get_connected_shading
    setTexture = set_texture
    hasTexture = has_texture
    getTexture = get_texture
    addTexture = add_texture
    clearTexture = clear_texture
    getNumTextures = get_num_textures
    setMaterial = set_material
    clearMaterial = clear_material
    getMaterial = get_material
    hasMaterial = has_material
    setBfaceFlag = set_bface_flag
    getBfaceFlag = get_bface_flag
    copyAttributes = copy_attributes
    hasVertexNormal = has_vertex_normal
    hasVertexColor = has_vertex_color
    unifyAttributes = unify_attributes
    applyLastAttribute = apply_last_attribute
    applyFirstAttribute = apply_first_attribute
    postApplyFlatAttribute = post_apply_flat_attribute
    reverseVertexOrdering = reverse_vertex_ordering
    removeDoubledVerts = remove_doubled_verts
    removeNonuniqueVerts = remove_nonunique_verts
    hasPrimitives = has_primitives
    jointHasPrimitives = joint_has_primitives
    hasNormals = has_normals
    addVertex = add_vertex
    removeVertex = remove_vertex
    copyVertices = copy_vertices
    getNumVertices = get_num_vertices
    getVertex = get_vertex
    setVertex = set_vertex
    insertVertex = insert_vertex
    getPool = get_pool
    testVrefIntegrity = test_vref_integrity
    getTextures = get_textures
    getVertices = get_vertices

class EggCompositePrimitive(EggPrimitive):
    """The base class for primitives such as triangle strips and triangle fans,
    which include several component triangles, each of which might have its own
    color and/or normal.
    """

    @property
    def components(self) -> MutableSequence[EggAttributes]: ...
    def get_num_components(self) -> int:
        """Returns the number of individual component triangles within the composite.
        Each one of these might have a different set of attributes.
        """
    def get_component(self, i: int) -> EggAttributes:
        """Returns the attributes for the nth component triangle."""
    def set_component(self, i: int, attrib: EggAttributes) -> None:
        """Changes the attributes for the nth component triangle."""
    def triangulate_into(self, container: EggGroupNode) -> bool:
        """Subdivides the composite primitive into triangles and adds those triangles
        to the indicated container.  Does not remove the primitive from its
        existing parent or modify it in any way.

        Returns true if the triangulation is successful, or false if there was some
        error (in which case the container may contain some partial triangulation).
        """
    def triangulate_in_place(self) -> EggCompositePrimitive:
        """Subdivides the composite primitive into triangles and adds those triangles
        to the parent group node in place of the original primitive.  Returns a
        pointer to the original primitive, which is likely about to be destructed.

        If convex_also is true, both concave and convex polygons will be subdivided
        into triangles; otherwise, only concave polygons will be subdivided, and
        convex polygons will be copied unchanged into the container.
        """
    def get_components(self) -> tuple[EggAttributes, ...]: ...
    getNumComponents = get_num_components
    getComponent = get_component
    setComponent = set_component
    triangulateInto = triangulate_into
    triangulateInPlace = triangulate_in_place
    getComponents = get_components

class EggData(EggGroupNode):
    """This is the primary interface into all the egg data, and the root of the
    egg file structure.  An EggData structure corresponds exactly with an egg
    file on the disk.

    The EggData class inherits from EggGroupNode its collection of children,
    which are accessed by using the EggData itself as an STL container with
    begin() and end() calls.  The children of the EggData class are the
    toplevel nodes in the egg file.
    """

    auto_resolve_externals: bool
    coordinate_system: _CoordinateSystem
    egg_filename: Filename
    egg_timestamp: int
    def __init__(self, copy: EggData = ...) -> None: ...
    @staticmethod
    def resolve_egg_filename(egg_filename: StrOrBytesPath, searchpath: SearchPathLike = ...) -> bool:
        """Looks for the indicated filename, first along the indicated searchpath, and
        then along the model_path.  If found, updates the filename to the full path
        and returns true; otherwise, returns false.
        """
    @overload
    def read(self, _in: istream) -> bool:
        """`(self, filename: Filename, display_name: str = ...)`:
        Opens the indicated filename and reads the egg data contents from it.
        Returns true if the file was successfully opened and read, false if there
        were some errors, in which case the data may be partially read.

        error is the output stream to which to write error messages.

        `(self, _in: istream)`:
        Parses the egg syntax contained in the indicated input stream.  Returns
        true if the stream was a completely valid egg file, false if there were
        some errors, in which case the data may be partially read.

        Before you call this routine, you should probably call set_egg_filename()
        to set the name of the egg file we're processing, if at all possible.  If
        there is no such filename, you may set it to the empty string.
        """
    @overload
    def read(self, filename: StrOrBytesPath, display_name: str = ...) -> bool: ...
    def merge(self, other: EggData) -> None:
        """Appends the other egg structure to the end of this one.  The other egg
        structure is invalidated.
        """
    @overload
    def load_externals(self, searchpath: SearchPathLike = ...) -> bool:
        """Loads up all the egg files referenced by <File> entries within the egg
        structure, and inserts their contents in place of the <File> entries.
        Searches for files in the searchpath, if not found directly, and writes
        error messages to the indicated output stream.  Returns true if all
        externals were loaded successfully, false otherwise.
        """
    @overload
    def load_externals(self, searchpath: SearchPathLike, record: BamCacheRecord) -> bool: ...
    def collapse_equivalent_textures(self) -> int:
        """Removes duplicate references to the same texture image with the same
        properties.  Considers two texture references with identical properties,
        but different tref names, to be equivalent, and collapses them, choosing
        one tref name to keep arbitrarily.  Returns the number of textures removed.
        """
    def collapse_equivalent_materials(self) -> int:
        """Removes duplicate references to the same material with the same properties.
        Considers two material references with identical properties, but different
        mref names, to be equivalent, and collapses them, choosing one mref name to
        keep arbitrarily.  Returns the number of materials removed.
        """
    @overload
    def write_egg(self, filename: StrOrBytesPath) -> bool:
        """The main interface for writing complete egg files."""
    @overload
    def write_egg(self, out: ostream) -> bool: ...
    def set_auto_resolve_externals(self, resolve: bool) -> None:
        """Indicates whether the EggData object will automatically resolve any
        external references when read() is called.  The default is false.
        """
    def get_auto_resolve_externals(self) -> bool:
        """Indicates whether the EggData object will automatically resolve any
        external references when read() is called.  The default is false.
        """
    def original_had_absolute_pathnames(self) -> bool:
        """Returns true if the data processed in the last call to read() contained
        absolute pathnames, or false if those pathnames were all relative.

        This method is necessary because if auto_resolve_externals() is in effect,
        it may modify the pathnames to be absolute whether or not they were as
        loaded from disk.  This method can be used to query the state of the
        original egg file from disk.
        """
    def set_coordinate_system(self, coordsys: _CoordinateSystem) -> None:
        """Changes the coordinate system of the EggData.  If the coordinate system was
        previously different, this may result in a conversion of the data.
        """
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system in which the egg file is defined."""
    def set_egg_filename(self, egg_filename: StrOrBytesPath) -> None:
        """Sets the filename--especially the directory part--in which the egg file is
        considered to reside.  This is also implicitly set by read().
        """
    def get_egg_filename(self) -> Filename:
        """Returns the directory in which the egg file is considered to reside."""
    def set_egg_timestamp(self, egg_timestamp: int) -> None:
        """Sets the timestamp of the egg file on disk, at the time it was opened for
        reading.  This is also implicitly set by read().
        """
    def get_egg_timestamp(self) -> int:
        """Returns the timestamp of the egg file on disk, at the time it was opened
        for reading, or 0 if this information is not available.
        """
    def recompute_vertex_normals(self, threshold: float) -> None:  # type: ignore[override]
        """Recomputes all the vertex normals for polygon geometry at this group node
        and below so that they accurately reflect the vertex positions.  A shared
        edge between two polygons (even in different groups) is considered smooth
        if the angle between the two edges is less than threshold degrees.

        This function also removes degenerate polygons that do not have enough
        vertices to define a normal.  It does not affect normals for other kinds of
        primitives like Nurbs or Points.

        This function does not remove or adjust vertices in the vertex pool; it
        only adds new vertices with the correct normals.  Thus, it is a good idea
        to call remove_unused_vertices() after calling this.
        """
    def recompute_polygon_normals(self) -> None:  # type: ignore[override]
        """Recomputes all the polygon normals for polygon geometry at this group node
        and below so that they accurately reflect the vertex positions.  Normals
        are removed from the vertices and defined only on polygons, giving the
        geometry a faceted appearance.

        This function also removes degenerate polygons that do not have enough
        vertices to define a normal.  It does not affect normals for other kinds of
        primitives like Nurbs or Points.

        This function does not remove or adjust vertices in the vertex pool; it
        only adds new vertices with the normals removed.  Thus, it is a good idea
        to call remove_unused_vertices() after calling this.
        """
    resolveEggFilename = resolve_egg_filename
    loadExternals = load_externals
    collapseEquivalentTextures = collapse_equivalent_textures
    collapseEquivalentMaterials = collapse_equivalent_materials
    writeEgg = write_egg
    setAutoResolveExternals = set_auto_resolve_externals
    getAutoResolveExternals = get_auto_resolve_externals
    originalHadAbsolutePathnames = original_had_absolute_pathnames
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    setEggFilename = set_egg_filename
    getEggFilename = get_egg_filename
    setEggTimestamp = set_egg_timestamp
    getEggTimestamp = get_egg_timestamp
    recomputeVertexNormals = recompute_vertex_normals  # type: ignore[assignment]
    recomputePolygonNormals = recompute_polygon_normals  # type: ignore[assignment]

class EggCoordinateSystem(EggNode):
    """The <CoordinateSystem> entry at the top of an egg file.  Don't confuse this
    with the enum EggData::CoordinateSystem, which is the value contained by
    this entry.
    """

    @overload
    def __init__(self, value: _CoordinateSystem = ...) -> None: ...
    @overload
    def __init__(self, copy: EggCoordinateSystem) -> None: ...
    def set_value(self, value: _CoordinateSystem) -> None: ...
    def get_value(self) -> _CoordinateSystem: ...
    setValue = set_value
    getValue = get_value

class EggCurve(EggPrimitive):
    """A parametric curve of some kind.  See EggNurbsCurve."""

    CT_none: Final = 0
    CTNone: Final = 0
    CT_xyz: Final = 1
    CTXyz: Final = 1
    CT_hpr: Final = 2
    CTHpr: Final = 2
    CT_t: Final = 3
    CTT: Final = 3
    def set_subdiv(self, subdiv: int) -> None:
        """Sets the number of subdivisions that will be requested across the curve.
        (This doesn't necessary guarantee that this number of subdivisions will be
        made; it's just a hint to any curve renderer or quick tesselator.)  Set the
        number to 0 to disable the hint.
        """
    def get_subdiv(self) -> int:
        """Returns the requested number of subdivisions, or 0 if no particular
        subdivisions have been requested.
        """
    def set_curve_type(self, type: _EggCurve_CurveType) -> None:
        """Sets the type of the curve.  This is primarily used as a hint to any code
        that may need to deal with this curve.
        """
    def get_curve_type(self) -> _EggCurve_CurveType:
        """Returns the indicated type of the curve."""
    @staticmethod
    def string_curve_type(string: str) -> _EggCurve_CurveType:
        """Returns the CurveType value associated with the given string
        representation, or CT_invalid if the string does not match any known
        CurveType value.
        """
    setSubdiv = set_subdiv
    getSubdiv = get_subdiv
    setCurveType = set_curve_type
    getCurveType = get_curve_type
    stringCurveType = string_curve_type

class EggExternalReference(EggFilenameNode):
    """Defines a reference to another egg file which should be inserted at this
    point.
    """

    @overload
    def __init__(self, copy: EggExternalReference) -> None: ...
    @overload
    def __init__(self, node_name: str, filename: str) -> None: ...

class EggNameUniquifier(EggObject):
    """This is a handy class for guaranteeing unique node names in an egg
    hierarchy.  It is an abstract class; to use it you must subclass off of it.
    See the comment above.
    """

    def clear(self) -> None:
        """Empties the table of used named and prepares the Uniquifier for a new tree."""
    def uniquify(self, node: EggNode) -> None:
        """Begins the traversal from the indicated node."""
    def get_node(self, category: str, name: str) -> EggNode:
        """Returns the node associated with the given category and name, or NULL if
        the name has not been used.
        """
    def has_name(self, category: str, name: str) -> bool:
        """Returns true if the name has been used for the indicated category already,
        false otherwise.
        """
    def add_name(self, category: str, name: str, node: EggNode = ...) -> bool:
        """Adds the name to the indicated category.  This name will not be used for
        any other egg node within this category.  Returns true if the name was
        added, or false if it was already in use for the category.
        """
    def get_category(self, node: EggNode) -> str: ...
    def filter_name(self, node: EggNode) -> str:
        """Returns the name of the given node, or at least the name it should be.
        This provides a hook to adjust the name before attempting to uniquify it,
        if desired, for instance to remove invalid characters.
        """
    def generate_name(self, node: EggNode, category: str, index: int) -> str:
        """Generates a new name for the given node when its existing name clashes with
        some other node.  This function will be called repeatedly, if necessary,
        until it returns a name that actually is unique.

        The category is the string returned by get_category(), and index is a
        uniquely-generated number that may be useful for synthesizing the name.
        """
    getNode = get_node
    hasName = has_name
    addName = add_name
    getCategory = get_category
    filterName = filter_name
    generateName = generate_name

class EggGroupUniquifier(EggNameUniquifier):
    """This is a specialization of EggNameUniquifier to generate unique names for
    EggGroup nodes.  It's not called automatically; you must invoke it yourself
    if you want it.
    """

    def __init__(self, filter_names: bool = ...) -> None:
        """If filter_names is true, then the group names will be coerced into a fairly
        safe, standard convention that uses no characters other than a-z, A-Z, 0-9,
        and underscore.  If filter_names is false, the group names will be left
        unchanged.
        """

class EggLine(EggCompositePrimitive):
    """A line segment, or a series of connected line segments, defined by a <Line>
    entry.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggLine) -> None: ...
    def has_thick(self) -> bool: ...
    def get_thick(self) -> float:
        """Returns the thickness set on this particular line.  If there is no
        thickness set, returns 1.0.
        """
    def set_thick(self, thick: float) -> None: ...
    def clear_thick(self) -> None: ...
    hasThick = has_thick
    getThick = get_thick
    setThick = set_thick
    clearThick = clear_thick

class EggMaterialCollection:
    """This is a collection of materials by MRef name.  It can extract the
    materials from an egg file and sort them all together; it can also manage
    the creation of unique materials and the assignment of unique MRef names.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: EggMaterialCollection = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Removes all materials from the collection."""
    def extract_materials(self, node: EggGroupNode) -> int:
        """Walks the egg hierarchy beginning at the indicated node, and removes any
        EggMaterials encountered in the hierarchy, adding them to the collection.
        Returns the number of EggMaterials encountered.
        """
    def find_used_materials(self, node: EggNode) -> int:
        """Walks the egg hierarchy beginning at the indicated node, looking for
        materials that are referenced by primitives but are not already members of
        the collection, adding them to the collection.

        If this is called following extract_materials(), it can be used to pick up
        any additional material references that appeared in the egg hierarchy (but
        whose EggMaterial node was not actually part of the hierarchy).

        If this is called in lieu of extract_materials(), it will fill up the
        collection with all of the referenced materials (and only the referenced
        materials), without destructively removing the EggMaterials from the
        hierarchy.

        This also has the side effect of incrementing the internal usage count for
        a material in the collection each time a material reference is encountered.
        This side effect is taken advantage of by remove_unused_materials().
        """
    def remove_unused_materials(self, node: EggNode) -> None:
        """Removes any materials from the collection that aren't referenced by any
        primitives in the indicated egg hierarchy.  This also, incidentally, adds
        materials to the collection that had been referenced by primitives but had
        not previously appeared in the collection.
        """
    def collapse_equivalent_materials(self, eq: int, node: EggGroupNode) -> int:
        """Walks through the collection and collapses together any separate materials
        that are equivalent according to the indicated equivalence factor, eq (see
        EggMaterial::is_equivalent_to()).  The return value is the number of
        materials removed.

        This flavor of collapse_equivalent_materials() automatically adjusts all
        the primitives in the egg hierarchy to refer to the new material pointers.
        """
    def uniquify_mrefs(self) -> None:
        """Guarantees that each material in the collection has a unique MRef name.
        This is essential before writing an egg file.
        """
    def sort_by_mref(self) -> None:
        """Sorts all the materials into alphabetical order by MRef name.  Subsequent
        operations using begin()/end() will traverse in this sorted order.
        """
    def add_material(self, material: EggMaterial) -> bool:
        """Explicitly adds a new material to the collection.  Returns true if the
        material was added, false if it was already there or if there was some
        error.
        """
    def remove_material(self, material: EggMaterial) -> bool:
        """Explicitly removes a material from the collection.  Returns true if the
        material was removed, false if it wasn't there or if there was some error.
        """
    def create_unique_material(self, copy: EggMaterial, eq: int) -> EggMaterial:
        """create_unique_material() creates a new material if there is not already
        one equivalent (according to eq, see EggMaterial::is_equivalent_to()) to
        the indicated material, or returns the existing one if there is.
        """
    def find_mref(self, mref_name: str) -> EggMaterial:
        """Returns the material with the indicated MRef name, or NULL if no material
        matches.
        """
    extractMaterials = extract_materials
    findUsedMaterials = find_used_materials
    removeUnusedMaterials = remove_unused_materials
    collapseEquivalentMaterials = collapse_equivalent_materials
    uniquifyMrefs = uniquify_mrefs
    sortByMref = sort_by_mref
    addMaterial = add_material
    removeMaterial = remove_material
    createUniqueMaterial = create_unique_material
    findMref = find_mref

class EggPolygon(EggPrimitive):
    """A single polygon."""

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggPolygon) -> None: ...
    def calculate_normal(self, result: DoubleVec3Like, cs: _CoordinateSystem = ...) -> bool:
        """Calculates the true polygon normal--the vector pointing out of the front of
        the polygon--based on the vertices.  This does not return or change the
        polygon's normal as set via set_normal().

        The return value is true if the normal is computed correctly, or false if
        the polygon is degenerate and does not have at least three noncollinear
        vertices.
        """
    def is_planar(self) -> bool:
        """Returns true if all of the polygon's vertices lie within the same plane,
        false otherwise.
        """
    def recompute_polygon_normal(self, cs: _CoordinateSystem = ...) -> bool:
        """Recalculates the normal according to the order of the vertices, and sets
        it.  Returns true if the normal is computed correctly, or false if the
        polygon is degenerate and does not have a normal.
        """
    def triangulate_into(self, container: EggGroupNode, convex_also: bool) -> bool:
        """Subdivides the polygon into triangles and adds each one to the indicated
        container.  If the polygon is already a triangle, adds an exact copy of the
        polygon to the container.  Does not remove the polygon from its existing
        parent or modify it in any way.

        Returns true if the triangulation is successful, or false if there was some
        error (in which case the container may contain some partial triangulation).

        If convex_also is true, both concave and convex polygons will be subdivided
        into triangles; otherwise, only concave polygons will be subdivided, and
        convex polygons will be copied unchanged into the container.
        """
    def triangulate_in_place(self, convex_also: bool) -> EggPolygon:
        """Subdivides the polygon into triangles and adds those triangles to the
        parent group node in place of the original polygon.  Returns a pointer to
        the original polygon, which is likely about to be destructed.

        If convex_also is true, both concave and convex polygons will be subdivided
        into triangles; otherwise, only concave polygons will be subdivided, and
        convex polygons will be copied unchanged into the container.
        """
    calculateNormal = calculate_normal
    isPlanar = is_planar
    recomputePolygonNormal = recompute_polygon_normal
    triangulateInto = triangulate_into
    triangulateInPlace = triangulate_in_place

class EggNurbsCurve(EggCurve):
    """A parametric NURBS curve."""

    order: int
    @property
    def degree(self) -> int: ...
    @property
    def closed(self) -> bool: ...
    @property
    def knots(self) -> MutableSequence[float]: ...
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggNurbsCurve) -> None: ...
    def setup(self, order: int, num_knots: int) -> None:
        """Prepares a new curve definition with the indicated order and number of
        knots.  This also implies a particular number of vertices as well (the
        number of knots minus the order), but it is up to the user to add the
        correct number of vertices to the curve by repeatedly calling push_back().
        """
    def set_order(self, order: int) -> None:
        """Directly changes the order to the indicated value (which must be an integer
        in the range 1 <= order <= 4).  If possible, it is preferable to use the
        setup() method instead of this method, since changing the order directly
        may result in an invalid curve.
        """
    def set_num_knots(self, num: int) -> None:
        """Directly changes the number of knots.  This will either add zero-valued
        knots onto the end, or truncate knot values from the end, depending on
        whether the list is being increased or decreased.  If possible, it is
        preferable to use the setup() method instead of directly setting the number
        of knots, as this may result in an invalid curve.
        """
    def set_knot(self, k: int, value: float) -> None:
        """Resets the value of the indicated knot as indicated.  k must be in the
        range 0 <= k < get_num_knots(), and the value must be in the range
        get_knot(k - 1) <= value <= get_knot(k + 1).
        """
    def is_valid(self) -> bool:
        """Returns true if the NURBS parameters are all internally consistent (e.g.
        it has the right number of vertices to match its number of knots and order
        in each dimension), or false otherwise.
        """
    def get_order(self) -> int:
        """Returns the order of the curve.  The order is the degree of the NURBS
        equation plus 1; for a typical NURBS, the order is 4.  With this
        implementation of NURBS, the order must be in the range [1, 4].
        """
    def get_degree(self) -> int:
        """Returns the degree of the curve.  For a typical NURBS, the degree is 3."""
    def get_num_knots(self) -> int:
        """Returns the number of knots."""
    def get_num_cvs(self) -> int:
        """Returns the total number of control vertices that *should* be defined for
        the curve.  This is determined by the number of knots and the order, in
        each direction; it does not necessarily reflect the number of vertices that
        have actually been added to the curve.  (However, if the number of vertices
        in the curve are wrong, the curve is invalid.)
        """
    def is_closed(self) -> bool:
        """Returns true if the curve appears to be closed.  Since the Egg syntax does
        not provide a means for explicit indication of closure, this has to be
        guessed at by examining the curve itself.
        """
    def get_knot(self, k: int) -> float:
        """Returns the nth knot value defined."""
    def get_knots(self) -> tuple[float, ...]: ...
    setOrder = set_order
    setNumKnots = set_num_knots
    setKnot = set_knot
    isValid = is_valid
    getOrder = get_order
    getDegree = get_degree
    getNumKnots = get_num_knots
    getNumCvs = get_num_cvs
    isClosed = is_closed
    getKnot = get_knot
    getKnots = get_knots

class EggSurface(EggPrimitive):
    """A parametric surface of some kind.  See EggNurbsSurface."""

    def set_u_subdiv(self, subdiv: int) -> None:
        """Sets the number of subdivisions in the U direction that will be requested
        across the surface.  (This doesn't necessary guarantee that this number of
        subdivisions will be made; it's just a hint to any surface renderer or
        quick tesselator.)  Set the number to 0 to disable the hint.
        """
    def get_u_subdiv(self) -> int:
        """Returns the requested number of subdivisions in the U direction, or 0 if no
        particular subdivisions have been requested.
        """
    def set_v_subdiv(self, subdiv: int) -> None:
        """Sets the number of subdivisions in the U direction that will be requested
        across the surface.  (This doesn't necessary guarantee that this number of
        subdivisions will be made; it's just a hint to any surface renderer or
        quick tesselator.)  Set the number to 0 to disable the hint.
        """
    def get_v_subdiv(self) -> int:
        """Returns the requested number of subdivisions in the U direction, or 0 if no
        particular subdivisions have been requested.
        """
    setUSubdiv = set_u_subdiv
    getUSubdiv = get_u_subdiv
    setVSubdiv = set_v_subdiv
    getVSubdiv = get_v_subdiv

class EggNurbsSurface(EggSurface):
    """A parametric NURBS surface."""

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggNurbsSurface) -> None: ...
    def setup(self, u_order: int, v_order: int, num_u_knots: int, num_v_knots: int) -> None:
        """Prepares a new surface definition with the indicated order and number of
        knots in each dimension.  This also implies a particular number of vertices
        in each dimension as well (the number of knots minus the order), but it is
        up to the user to add the correct number of vertices to the surface by
        repeatedly calling push_back().
        """
    def set_u_order(self, u_order: int) -> None:
        """Directly changes the order in the U direction to the indicated value (which
        must be an integer in the range 1 <= u_order <= 4).  If possible, it is
        preferable to use the setup() method instead of this method, since changing
        the order directly may result in an invalid surface.
        """
    def set_v_order(self, v_order: int) -> None:
        """Directly changes the order in the V direction to the indicated value (which
        must be an integer in the range 1 <= v_order <= 4).  If possible, it is
        preferable to use the setup() method instead of this method, since changing
        the order directly may result in an invalid surface.
        """
    def set_num_u_knots(self, num: int) -> None:
        """Directly changes the number of knots in the U direction.  This will either
        add zero-valued knots onto the end, or truncate knot values from the end,
        depending on whether the list is being increased or decreased.  If
        possible, it is preferable to use the setup() method instead of directly
        setting the number of knots, as this may result in an invalid surface.
        """
    def set_num_v_knots(self, num: int) -> None:
        """Directly changes the number of knots in the V direction.  This will either
        add zero-valued knots onto the end, or truncate knot values from the end,
        depending on whether the list is being increased or decreased.  If
        possible, it is preferable to use the setup() method instead of directly
        setting the number of knots, as this may result in an invalid surface.
        """
    def set_u_knot(self, k: int, value: float) -> None:
        """Resets the value of the indicated knot as indicated.  k must be in the
        range 0 <= k < get_num_u_knots(), and the value must be in the range
        get_u_knot(k - 1) <= value <= get_u_knot(k + 1).
        """
    def set_v_knot(self, k: int, value: float) -> None:
        """Resets the value of the indicated knot as indicated.  k must be in the
        range 0 <= k < get_num_v_knots(), and the value must be in the range
        get_v_knot(k - 1) <= value <= get_v_knot(k + 1).
        """
    def set_cv(self, ui: int, vi: int, vertex: EggVertex) -> None:
        """Redefines the control vertex associated with a particular u, v coordinate
        pair.  This is just a shorthand to access the EggPrimitive's normal vertex
        assignment for a 2-d control vertex.
        """
    def is_valid(self) -> bool:
        """Returns true if the NURBS parameters are all internally consistent (e.g.
        it has the right number of vertices to match its number of knots and order
        in each dimension), or false otherwise.
        """
    def get_u_order(self) -> int:
        """Returns the order of the surface in the U direction.  The order is the
        degree of the NURBS equation plus 1; for a typical NURBS, the order is 4.
        With this implementation of NURBS, the order must be in the range [1, 4].
        """
    def get_v_order(self) -> int:
        """Returns the order of the surface in the V direction.  The order is the
        degree of the NURBS equation plus 1; for a typical NURBS, the order is 4.
        With this implementation of NURBS, the order must be in the range [1, 4].
        """
    def get_u_degree(self) -> int:
        """Returns the degree of the surface in the U direction.  For a typical NURBS,
        the degree is 3.
        """
    def get_v_degree(self) -> int:
        """Returns the degree of the surface in the V direction.  for a typical NURBS,
        the degree is 3.
        """
    def get_num_u_knots(self) -> int:
        """Returns the number of knots in the U direction."""
    def get_num_v_knots(self) -> int:
        """Returns the number of knots in the V direction."""
    def get_num_u_cvs(self) -> int:
        """Returns the number of control vertices that should be present in the U
        direction.  This is determined by the number of knots and the order; it
        does not necessarily reflect the number of vertices that have actually been
        added to the surface.  (However, if the number of vertices in the surface
        are wrong, the surface is invalid.)
        """
    def get_num_v_cvs(self) -> int:
        """Returns the number of control vertices that should be present in the V
        direction.  This is determined by the number of knots and the order; it
        does not necessarily reflect the number of vertices that have actually been
        added to the surface.  (However, if the number of vertices in the surface
        are wrong, the surface is invalid.)
        """
    def get_num_cvs(self) -> int:
        """Returns the total number of control vertices that *should* be defined for
        the surface.  This is determined by the number of knots and the order, in
        each direction; it does not necessarily reflect the number of vertices that
        have actually been added to the surface.  (However, if the number of
        vertices in the surface are wrong, the surface is invalid.)
        """
    def get_u_index(self, vertex_index: int) -> int:
        """Returns the U index number of the given vertex within the EggPrimitive's
        linear list of vertices.  An EggNurbsSurface maps a linear list of vertices
        to its 2-d mesh; this returns the U index number that corresponds to the
        nth vertex in the list.
        """
    def get_v_index(self, vertex_index: int) -> int:
        """Returns the V index number of the given vertex within the EggPrimitive's
        linear list of vertices.  An EggNurbsSurface maps a linear list of vertices
        to its 2-d mesh; this returns the V index number that corresponds to the
        nth vertex in the list.
        """
    def get_vertex_index(self, ui: int, vi: int) -> int:
        """Returns the index number within the EggPrimitive's list of the control
        vertex at position ui, vi.
        """
    def is_closed_u(self) -> bool:
        """Returns true if the surface appears to be closed in the U direction.  Since
        the Egg syntax does not provide a means for explicit indication of closure,
        this has to be guessed at by examining the surface itself.
        """
    def is_closed_v(self) -> bool:
        """Returns true if the surface appears to be closed in the V direction.  Since
        the Egg syntax does not provide a means for explicit indication of closure,
        this has to be guessed at by examining the surface itself.
        """
    def get_u_knot(self, k: int) -> float:
        """Returns the nth knot value defined in the U direction."""
    def get_v_knot(self, k: int) -> float:
        """Returns the nth knot value defined in the V direction."""
    def get_cv(self, ui: int, vi: int) -> EggVertex:
        """Returns the control vertex at the indicate U, V position."""
    def get_u_knots(self) -> tuple[float, ...]: ...
    def get_v_knots(self) -> tuple[float, ...]: ...
    setUOrder = set_u_order
    setVOrder = set_v_order
    setNumUKnots = set_num_u_knots
    setNumVKnots = set_num_v_knots
    setUKnot = set_u_knot
    setVKnot = set_v_knot
    setCv = set_cv
    isValid = is_valid
    getUOrder = get_u_order
    getVOrder = get_v_order
    getUDegree = get_u_degree
    getVDegree = get_v_degree
    getNumUKnots = get_num_u_knots
    getNumVKnots = get_num_v_knots
    getNumUCvs = get_num_u_cvs
    getNumVCvs = get_num_v_cvs
    getNumCvs = get_num_cvs
    getUIndex = get_u_index
    getVIndex = get_v_index
    getVertexIndex = get_vertex_index
    isClosedU = is_closed_u
    isClosedV = is_closed_v
    getUKnot = get_u_knot
    getVKnot = get_v_knot
    getCv = get_cv
    getUKnots = get_u_knots
    getVKnots = get_v_knots

class EggPatch(EggPrimitive):
    """A single "patch", a special primitive to be rendered only with a
    tessellation shader.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggPatch) -> None: ...

class EggPoint(EggPrimitive):
    """A single point, or a collection of points as defined by a single
    <PointLight> entry.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggPoint) -> None: ...
    def has_thick(self) -> bool: ...
    def get_thick(self) -> float:
        """Returns the thickness set on this particular point.  If there is no
        thickness set, returns 1.0.
        """
    def set_thick(self, thick: float) -> None: ...
    def clear_thick(self) -> None: ...
    def has_perspective(self) -> bool: ...
    def get_perspective(self) -> bool:
        """Returns the perspective flag set on this particular point.  If there is no
        perspective flag set, returns false.
        """
    def set_perspective(self, perspective: bool) -> None: ...
    def clear_perspective(self) -> None: ...
    hasThick = has_thick
    getThick = get_thick
    setThick = set_thick
    clearThick = clear_thick
    hasPerspective = has_perspective
    getPerspective = get_perspective
    setPerspective = set_perspective
    clearPerspective = clear_perspective

class EggPolysetMaker(EggBinMaker):
    """A specialization on EggBinMaker for making polysets that share the same
    basic rendering characteristic.  This really just defines the example
    functions described in the leading comment to EggBinMaker.

    It makes some common assumptions about how polysets should be grouped; if
    these are not sufficient, you can always rederive your own further
    specialization of this class.
    """

    BN_none: Final = 0
    BNNone: Final = 0
    BN_polyset: Final = 1
    BNPolyset: Final = 1
    P_has_texture: Final = 1
    PHasTexture: Final = 1
    P_texture: Final = 2
    PTexture: Final = 2
    P_has_material: Final = 4
    PHasMaterial: Final = 4
    P_material: Final = 8
    PMaterial: Final = 8
    P_has_poly_color: Final = 16
    PHasPolyColor: Final = 16
    P_poly_color: Final = 32
    PPolyColor: Final = 32
    P_has_poly_normal: Final = 64
    PHasPolyNormal: Final = 64
    P_has_vertex_normal: Final = 128
    PHasVertexNormal: Final = 128
    P_has_vertex_color: Final = 256
    PHasVertexColor: Final = 256
    P_bface: Final = 512
    PBface: Final = 512
    def __init__(self) -> None: ...
    def set_properties(self, properties: int) -> None:
        """Sets the set of properties that determines which polygons are allowed to be
        grouped together into a single polyset.  This is the bitwise 'or' of all
        the properties that matter.  If this is 0, all polygons (within a given
        group) will be lumped into a common polyset regardless of their properties.
        """
    setProperties = set_properties

class EggPoolUniquifier(EggNameUniquifier):
    """This is a specialization of EggNameUniquifier to generate unique names for
    textures, materials, and vertex pools prior to writing out an egg file.
    It's automatically called by EggData prior to writing out an egg file.
    """

    def __init__(self) -> None: ...

class EggSAnimData(EggAnimData):
    """Corresponding to an <S$Anim> entry, this stores a single column of numbers,
    for instance for a morph target, or as one column in an EggXfmSAnim.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggSAnimData) -> None: ...
    def get_num_rows(self) -> int:
        """Returns the number of rows in the table.  For an SAnim table, each row has
        one column.
        """
    def get_value(self, row: int) -> float:
        """Returns the value at the indicated row.  Row must be in the range 0 <= row
        < get_num_rows().
        """
    def set_value(self, row: int, value: float) -> None:
        """Changes the value at the indicated row.  Row must be in the range 0 <= row
        < get_num_rows().
        """
    def optimize(self) -> None:
        """Optimizes the data by collapsing a long table of duplicate values into a
        single value.
        """
    getNumRows = get_num_rows
    getValue = get_value
    setValue = set_value

class EggTable(EggGroupNode):
    """This corresponds to a <Table> or a <Bundle> entry.  As such, it doesn't
    actually contain a table of numbers, but it may be a parent to an
    EggSAnimData or an EggXfmAnimData, which do.  It may also be a parent to
    another <Table> or <Bundle>, establishing a hierarchy of tables.
    """

    TT_invalid: Final = 0
    TTInvalid: Final = 0
    TT_table: Final = 1
    TTTable: Final = 1
    TT_bundle: Final = 2
    TTBundle: Final = 2
    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggTable) -> None: ...
    def set_table_type(self, type: _EggTable_TableType) -> None: ...
    def get_table_type(self) -> _EggTable_TableType: ...
    def has_transform(self) -> bool:
        """Returns true if the table contains a transform description, false
        otherwise.
        """
    @staticmethod
    def string_table_type(string: str) -> _EggTable_TableType:
        """Returns the TableType value associated with the given string
        representation, or TT_invalid if the string does not match any known
        TableType value.
        """
    setTableType = set_table_type
    getTableType = get_table_type
    hasTransform = has_transform
    stringTableType = string_table_type

class EggTextureCollection:
    """This is a collection of textures by TRef name.  It can extract the textures
    from an egg file and sort them all together; it can also manage the
    creation of unique textures and the assignment of unique TRef names.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: EggTextureCollection = ...) -> None: ...
    def __getitem__(self, n: int) -> EggTexture:
        """Returns the nth EggTexture in the collection."""
    def __len__(self) -> int:
        """Returns the number of EggTextures in the collection."""
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[EggTexture]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Removes all textures from the collection."""
    def extract_textures(self, node: EggGroupNode) -> int:
        """Walks the egg hierarchy beginning at the indicated node, and removes any
        EggTextures encountered in the hierarchy, adding them to the collection.
        Returns the number of EggTextures encountered.
        """
    def is_empty(self) -> bool:
        """Returns true if there are no EggTexures in the collection, false otherwise."""
    def get_num_textures(self) -> int:
        """Returns the number of EggTextures in the collection."""
    def get_texture(self, index: int) -> EggTexture:
        """Returns the nth EggTexture in the collection."""
    def find_used_textures(self, node: EggNode) -> int:
        """Walks the egg hierarchy beginning at the indicated node, looking for
        textures that are referenced by primitives but are not already members of
        the collection, adding them to the collection.

        If this is called following extract_textures(), it can be used to pick up
        any additional texture references that appeared in the egg hierarchy (but
        whose EggTexture node was not actually part of the hierarchy).

        If this is called in lieu of extract_textures(), it will fill up the
        collection with all of the referenced textures (and only the referenced
        textures), without destructively removing the EggTextures from the
        hierarchy.

        This also has the side effect of incrementing the internal usage count for
        a texture in the collection each time a texture reference is encountered.
        This side effect is taken advantage of by remove_unused_textures().

        And one more side effect: this function identifies the presence of
        multitexturing in the egg file, and calls multitexture_over() on each
        texture appropriately so that, after this call, you may expect
        get_multitexture_sort() to return a reasonable value for each texture.
        """
    def remove_unused_textures(self, node: EggNode) -> None:
        """Removes any textures from the collection that aren't referenced by any
        primitives in the indicated egg hierarchy.  This also, incidentally, adds
        textures to the collection that had been referenced by primitives but had
        not previously appeared in the collection.
        """
    def collapse_equivalent_textures(self, eq: int, node: EggGroupNode) -> int:
        """Walks through the collection and collapses together any separate textures
        that are equivalent according to the indicated equivalence factor, eq (see
        EggTexture::is_equivalent_to()).  The return value is the number of
        textures removed.

        This flavor of collapse_equivalent_textures() automatically adjusts all the
        primitives in the egg hierarchy to refer to the new texture pointers.
        """
    def uniquify_trefs(self) -> None:
        """Guarantees that each texture in the collection has a unique TRef name.
        This is essential before writing an egg file.
        """
    def sort_by_tref(self) -> None:
        """Sorts all the textures into alphabetical order by TRef name.  Subsequent
        operations using begin()/end() will traverse in this sorted order.
        """
    def sort_by_basename(self) -> None:
        """Sorts all the textures into alphabetical order by the basename part
        (including extension) of the filename.  Subsequent operations using
        begin()/end() will traverse in this sorted order.
        """
    def add_texture(self, texture: EggTexture) -> bool:
        """Explicitly adds a new texture to the collection.  Returns true if the
        texture was added, false if it was already there or if there was some
        error.
        """
    def remove_texture(self, texture: EggTexture) -> bool:
        """Explicitly removes a texture from the collection.  Returns true if the
        texture was removed, false if it wasn't there or if there was some error.
        """
    def create_unique_texture(self, copy: EggTexture, eq: int) -> EggTexture:
        """create_unique_texture() creates a new texture if there is not already one
        equivalent (according to eq, see EggTexture::is_equivalent_to()) to the
        indicated texture, or returns the existing one if there is.
        """
    def find_tref(self, tref_name: str) -> EggTexture:
        """Returns the texture with the indicated TRef name, or NULL if no texture
        matches.
        """
    def find_filename(self, filename: StrOrBytesPath) -> EggTexture:
        """Returns the texture with the indicated filename, or NULL if no texture
        matches.
        """
    def get_textures(self) -> tuple[EggTexture, ...]: ...
    extractTextures = extract_textures
    isEmpty = is_empty
    getNumTextures = get_num_textures
    getTexture = get_texture
    findUsedTextures = find_used_textures
    removeUnusedTextures = remove_unused_textures
    collapseEquivalentTextures = collapse_equivalent_textures
    uniquifyTrefs = uniquify_trefs
    sortByTref = sort_by_tref
    sortByBasename = sort_by_basename
    addTexture = add_texture
    removeTexture = remove_texture
    createUniqueTexture = create_unique_texture
    findTref = find_tref
    findFilename = find_filename
    getTextures = get_textures

class EggTriangleFan(EggCompositePrimitive):
    """A connected fan of triangles.  This does not normally appear in an egg
    file; it is typically generated as a result of meshing.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggTriangleFan) -> None: ...

class EggTriangleStrip(EggCompositePrimitive):
    """A connected strip of triangles.  This does not normally appear in an egg
    file; it is typically generated as a result of meshing.
    """

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, copy: EggTriangleStrip) -> None: ...

class EggXfmSAnim(EggGroupNode):
    """This corresponds to an <Xfm$Anim_S$> entry, which is a collection of up to
    nine <S$Anim> entries that specify the nine components of a transformation.
    It's implemented as a group that can contain any number of EggSAnimData
    children.
    """

    @overload
    def __init__(self, name: str = ..., cs: _CoordinateSystem = ...) -> None:
        """Converts the older-style XfmAnim table to the newer-style XfmSAnim table."""
    @overload
    def __init__(self, convert_from: EggXfmAnimData) -> None: ...
    @overload
    def __init__(self, copy: EggXfmSAnim) -> None: ...
    def assign(self, copy: EggXfmAnimData | EggXfmSAnim) -> Self: ...
    def set_fps(self, fps: float) -> None: ...
    def clear_fps(self) -> None: ...
    def has_fps(self) -> bool: ...
    def get_fps(self) -> float:
        """This is only valid if has_fps() returns true."""
    def set_order(self, order: str) -> None: ...
    def clear_order(self) -> None: ...
    def has_order(self) -> bool: ...
    def get_order(self) -> str: ...
    @staticmethod
    def get_standard_order() -> str:
        """Returns the standard order of matrix component composition.  This is what
        the order string must be set to in order to use set_value() or add_data()
        successfully.
        """
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system this table believes it is defined within.
        This should always match the coordinate system of the EggData structure
        that owns it.  It is necessary to store it here because the meaning of the
        h, p, and r columns depends on the coordinate system.
        """
    def optimize(self) -> None:
        """Optimizes the table by collapsing redundant sub-tables."""
    def optimize_to_standard_order(self) -> None:
        """Optimizes the table by collapsing redundant sub-tables, and simultaneously
        ensures that the order string is the standard order (which is the same as
        that supported by compose_matrix() and decompose_matrix()).
        """
    def normalize(self) -> None:
        """The inverse operation of optimize(), this ensures that all the sub-tables
        have the same length by duplicating rows as necessary.  This is needed
        before doing operations like add_data() or set_value() on an existing
        table.
        """
    def get_num_rows(self) -> int:
        """Returns the effective number of rows in the table.  This is actually the
        number of rows of the smallest subtable larger than one row.  This is a
        convenience function that treats the table of tables as if it were a single
        table of matrices.
        """
    def get_value(self, row: int, mat: DoubleMat4Like) -> None:
        """Returns the value of the aggregate row of the table as a matrix.  This is a
        convenience function that treats the table of tables as if it were a single
        table of matrices.  It is an error to call this if any SAnimData children
        of this node have an improper name (e.g.  not a single letter, or not one
        of "ijkabchprxyz").
        """
    def set_value(self, row: int, mat: DoubleMat4Like) -> bool:
        """Replaces the indicated row of the table with the given matrix.

        This function can only be called if all the constraints of add_data(),
        below, are met.  Call normalize() first if you are not sure.

        The return value is true if the matrix can be decomposed and stored as
        scale, shear, rotate, and translate, or false otherwise.  The data is set
        in either case.
        """
    def clear_data(self) -> None:
        """Removes all data from the table.  It does this by removing all of its
        children.
        """
    def add_data(self, mat: DoubleMat4Like) -> bool:
        """Adds a new matrix to the table, by adding a new row to each of the
        subtables.

        This is a convenience function that treats the table of tables as if it
        were a single table of matrices.  It is an error to call this if any
        SAnimData children of this node have an improper name (e.g.  not a single
        letter, or not one of "ijkabchprxyz").

        This function has the further requirement that all nine of the subtables
        must exist and be of the same length.  Furthermore, the order string must
        be the standard order string, which matches the system compose_matrix() and
        decompose_matrix() functions.

        Thus, you probably cannot take an existing EggXfmSAnim object and start
        adding matrices to the end; you must clear out the original data first.
        (As a special exception, if no tables exist, they will be created.)  The
        method normalize() will do this for you on an existing EggXfmSAnim.

        This function may fail silently if the matrix cannot be decomposed into
        scale, shear, rotate, and translate.  In this case, the closest
        approximation is added to the table, and false is returned.
        """
    @overload
    def add_component_data(self, component: int, value: float) -> None:
        """`(self, component: int, value: float)`:
        Adds a new row to the indicated component (0-12) of the table.

        `(self, component_name: str, value: float)`:
        Adds a new row to the named component (one of matrix_component_letters) of
        the table.
        """
    @overload
    def add_component_data(self, component_name: str, value: float) -> None: ...
    @staticmethod
    def compose_with_order(
        mat: DoubleMat4Like,
        scale: DoubleVec3Like,
        shear: DoubleVec3Like,
        hpr: DoubleVec3Like,
        trans: DoubleVec3Like,
        order: str,
        cs: _CoordinateSystem,
    ) -> None:
        """Composes a matrix out of the nine individual components, respecting the
        order string.  The components will be applied in the order indicated by the
        string.
        """
    setFps = set_fps
    clearFps = clear_fps
    hasFps = has_fps
    getFps = get_fps
    setOrder = set_order
    clearOrder = clear_order
    hasOrder = has_order
    getOrder = get_order
    getStandardOrder = get_standard_order
    getCoordinateSystem = get_coordinate_system
    optimizeToStandardOrder = optimize_to_standard_order
    getNumRows = get_num_rows
    getValue = get_value
    setValue = set_value
    clearData = clear_data
    addData = add_data
    addComponentData = add_component_data
    composeWithOrder = compose_with_order

class EggXfmAnimData(EggAnimData):
    """Corresponding to an <Xfm$Anim> entry, this stores a two-dimensional table
    with up to nine columns, one for each component of a transformation.  This
    is an older syntax of egg anim table, not often used currently--it's
    replaced by EggXfmSAnim.
    """

    @overload
    def __init__(self, name: str = ..., cs: _CoordinateSystem = ...) -> None:
        """Converts the newer-style XfmSAnim table to the older-style XfmAnim table."""
    @overload
    def __init__(self, copy: EggXfmAnimData) -> None: ...
    @overload
    def __init__(self, convert_from: EggXfmSAnim) -> None: ...
    def assign(self, copy: EggXfmAnimData | EggXfmSAnim) -> Self: ...
    def set_order(self, order: str) -> None: ...
    def clear_order(self) -> None: ...
    def has_order(self) -> bool: ...
    def get_order(self) -> str: ...
    @staticmethod
    def get_standard_order() -> str:
        """Returns the standard order of matrix component composition.  This is what
        the order string must be set to in order to use set_value() or add_data()
        successfully.
        """
    def set_contents(self, contents: str) -> None: ...
    def clear_contents(self) -> None: ...
    def has_contents(self) -> bool: ...
    def get_contents(self) -> str: ...
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system this table believes it is defined within.
        This should always match the coordinate system of the EggData structure
        that owns it.  It is necessary to store it here because the meaning of the
        h, p, and r columns depends on the coordinate system.
        """
    def get_num_rows(self) -> int:
        """Returns the number of rows in the table."""
    def get_num_cols(self) -> int:
        """Returns the number of columns in the table.  This is set according to the
        "contents" string, which defines the meaning of each column.
        """
    @overload
    def get_value(self, row: int, mat: DoubleMat4Like) -> None:
        """`(self, row: int, mat: LMatrix4d)`:
        Returns the value of the aggregate row of the table as a matrix.  This is a
        convenience function that treats the 2-d table as if it were a single table
        of matrices.

        `(self, row: int, col: int)`:
        Returns the value at the indicated row.  Row must be in the range 0 <= row
        < get_num_rows(); col must be in the range 0 <= col < get_num_cols().
        """
    @overload
    def get_value(self, row: int, col: int) -> float: ...
    setOrder = set_order
    clearOrder = clear_order
    hasOrder = has_order
    getOrder = get_order
    getStandardOrder = get_standard_order
    setContents = set_contents
    clearContents = clear_contents
    hasContents = has_contents
    getContents = get_contents
    getCoordinateSystem = get_coordinate_system
    getNumRows = get_num_rows
    getNumCols = get_num_cols
    getValue = get_value

def parse_egg_data(egg_syntax: str) -> EggData:
    """Parses an EggData from the raw egg syntax."""

def parse_egg_node(egg_syntax: str) -> EggNode:
    """Parses a single egg node from the raw egg syntax."""

parseEggData = parse_egg_data
parseEggNode = parse_egg_node
