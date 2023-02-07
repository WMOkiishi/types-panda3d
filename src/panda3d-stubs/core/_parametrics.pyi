from _typeshed import StrOrBytesPath
from array import array
from collections.abc import MutableSequence, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Mat4Like, Vec3Like, Vec4Like
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import ostream
from panda3d.core._express import ReferenceCount
from panda3d.core._linmath import LMatrix4, LPoint3, LVecBase3, LVecBase4, LVector3
from panda3d.core._pgraph import NodePath, PandaNode

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_RopeNode_RenderMode: TypeAlias = Literal[0, 1, 2, 3]
_RopeNode_UVMode: TypeAlias = Literal[0, 1, 2, 3]
_RopeNode_NormalMode: TypeAlias = Literal[0, 1]

class ParametricCurve(PandaNode):
    """A virtual base class for parametric curves.  This encapsulates all curves
    in 3-d space defined for a single parameter t in the range [0,get_max_t()].
    """

    def is_valid(self) -> bool:
        """Returns true if the curve is defined.  This base class function always
        returns true; derived classes might override this to sometimes return
        false.
        """
    def get_max_t(self) -> float:
        """Returns the upper bound of t for the entire curve.  The curve is defined in
        the range 0.0f <= t <= get_max_t().  This base class function always
        returns 1.0f; derived classes might override this to return something else.
        """
    def set_curve_type(self, type: int) -> None:
        """Sets the flag indicating the use to which the curve is intended to be put.
        This flag is optional and only serves to provide a hint to the egg reader
        and writer code; it has no effect on the curve's behavior.

        Setting the curve type also sets the num_dimensions to 3 or 1 according to
        the type.

        THis flag may have one of the values PCT_XYZ, PCT_HPR, or PCT_T.
        """
    def get_curve_type(self) -> int:
        """Returns the flag indicating the use to which the curve is intended to be
        put.
        """
    def set_num_dimensions(self, num: int) -> None:
        """Specifies the number of significant dimensions in the curve's vertices.
        This should be one of 1, 2, or 3. Normally, XYZ and HPR curves have three
        dimensions; time curves should always have one dimension.  This only serves
        as a hint to the mopath editor, and also controls how the curve is written
        out.
        """
    def get_num_dimensions(self) -> int:
        """Returns the number of significant dimensions in the curve's vertices, as
        set by a previous call to set_num_dimensions().  This is only a hint as to
        how the curve is intended to be used; the actual number of dimensions of
        any curve is always three.
        """
    @overload
    def calc_length(self) -> float:
        """`(self)`:
        Approximates the length of the entire curve to within a few decimal places.

        `(self, _from: float, to: float)`:
        Approximates the length of the curve segment from parametric time 'from' to
        time 'to'.
        """
    @overload
    def calc_length(self, _from: float, to: float) -> float: ...
    def find_length(self, start_t: float, length_offset: float) -> float:
        """Returns the parametric value corresponding to the indicated distance along
        the curve from the starting parametric value.

        This is the inverse of calc_length(): rather than determining the length
        along the curve between two parametric points, it determines the position
        in parametric time of a point n units along the curve.

        The search distance must not be negative.
        """
    def get_point(self, t: float, point: Vec3Like) -> bool: ...
    def get_tangent(self, t: float, tangent: Vec3Like) -> bool: ...
    def get_pt(self, t: float, point: Vec3Like, tangent: Vec3Like) -> bool: ...
    def get_2ndtangent(self, t: float, tangent2: Vec3Like) -> bool: ...
    def adjust_point(self, t: float, px: float, py: float, pz: float) -> bool:
        """Recomputes the curve such that it passes through the point (px, py, pz) at
        time t, but keeps the same tangent value at that point.
        """
    def adjust_tangent(self, t: float, tx: float, ty: float, tz: float) -> bool:
        """Recomputes the curve such that it has the tangent (tx, ty, tz) at time t,
        but keeps the same position at the point.
        """
    def adjust_pt(self, t: float, px: float, py: float, pz: float, tx: float, ty: float, tz: float) -> bool:
        """Recomputes the curve such that it passes through the point (px, py, pz)
        with the tangent (tx, ty, tz).
        """
    def recompute(self) -> bool:
        """Recalculates the curve, if necessary.  Returns true if the resulting curve
        is valid, false otherwise.
        """
    def stitch(self, a: ParametricCurve, b: ParametricCurve) -> bool:
        """Regenerates this curve as one long curve: the first curve connected end-to-
        end with the second one.  Either a or b may be the same as 'this'.

        Returns true if successful, false on failure or if the curve type does not
        support stitching.
        """
    @overload
    def write_egg(self, filename: StrOrBytesPath, cs: _CoordinateSystem = ...) -> bool:
        """`(self, filename: Filename, cs: _CoordinateSystem = ...)`:
        Writes an egg description of the nurbs curve to the specified output file.
        Returns true if the file is successfully written.

        `(self, out: ostream, filename: Filename, cs: _CoordinateSystem)`:
        Writes an egg description of the nurbs curve to the specified output
        stream.  Returns true if the file is successfully written.
        """
    @overload
    def write_egg(self, out: ostream, filename: StrOrBytesPath, cs: _CoordinateSystem) -> bool: ...
    isValid = is_valid
    getMaxT = get_max_t
    setCurveType = set_curve_type
    getCurveType = get_curve_type
    setNumDimensions = set_num_dimensions
    getNumDimensions = get_num_dimensions
    calcLength = calc_length
    findLength = find_length
    getPoint = get_point
    getTangent = get_tangent
    getPt = get_pt
    get2ndtangent = get_2ndtangent
    adjustPoint = adjust_point
    adjustTangent = adjust_tangent
    adjustPt = adjust_pt
    writeEgg = write_egg

class CubicCurveseg(ParametricCurve):
    """A CubicCurveseg is any curve that can be completely described by four
    4-valued basis vectors, one for each dimension in three-space, and one for
    the homogeneous coordinate.  This includes Beziers, Hermites, and NURBS.

    This class encapsulates a single curve segment of the cubic curve.
    Normally, when we think of Bezier and Hermite curves, we think of a
    piecewise collection of such segments.

    Although this class includes methods such as hermite_basis() and
    nurbs_basis(), to generate a Hermite and NURBS curve segment, respectively,
    only the final basis vectors are stored: the product of the basis matrix of
    the corresponding curve type, and its geometry vectors.  This is the
    minimum information needed to evaluate the curve.  However, the individual
    CV's that were used to compute these basis vectors are not retained; this
    might be handled in a subclass (for instance, HermiteCurve).
    """

class ParametricCurveCollection(ReferenceCount):
    """This is a set of zero or more ParametricCurves, which may or may not be
    related.  If they are related, the set should contain no more than one XYZ
    curve, no more than one HPR curve, and zero or more Timewarp curves, which
    can then be evaluated as a unit to return a single transformation matrix
    for a given unit of time.
    """

    @property
    def curves(self) -> MutableSequence[ParametricCurve]: ...
    @property
    def xyz_curve(self) -> ParametricCurve: ...
    @property
    def hpr_curve(self) -> ParametricCurve: ...
    @property
    def default_curve(self) -> ParametricCurve: ...
    @property
    def timewarp_curves(self) -> Sequence[ParametricCurve]: ...
    @property
    def max_t(self) -> float: ...
    def __init__(self, __param0: ParametricCurveCollection = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_curve(self, curve: ParametricCurve, index: int = ...) -> None:
        """`(self, curve: ParametricCurve)`:
        Adds a new ParametricCurve to the collection.

        `(self, curve: ParametricCurve, index: int)`:
        Adds a new ParametricCurve to the collection at the indicated index.
        @deprecated Use insert_curve(index, curve) instead.
        """
    def insert_curve(self, index: int, curve: ParametricCurve) -> None:
        """Adds a new ParametricCurve to the collection at the indicated index."""
    def add_curves(self, node: PandaNode) -> int:
        """Adds all the curves found in the scene graph rooted at the given node.
        Returns the number of curves found.
        """
    @overload
    def remove_curve(self, curve: ParametricCurve) -> bool:
        """`(self, curve: ParametricCurve)`:
        Removes the indicated ParametricCurve from the collection.  Returns true if
        the curve was removed, false if it was not a member of the collection.

        `(self, index: int)`:
        Removes the indicated ParametricCurve from the collection, by its index
        number.
        """
    @overload
    def remove_curve(self, index: int) -> None: ...
    def set_curve(self, index: int, curve: ParametricCurve) -> None:
        """Replaces the indicated ParametricCurve from the collection, by its index
        number.
        """
    def has_curve(self, curve: ParametricCurve) -> bool:
        """Returns true if the indicated ParametricCurve appears in this collection,
        false otherwise.
        """
    def clear(self) -> None:
        """Removes all ParametricCurves from the collection."""
    def clear_timewarps(self) -> None:
        """Removes all the timewarp curves from the collection."""
    def get_num_curves(self) -> int:
        """Returns the number of ParametricCurves in the collection."""
    def get_curve(self, index: int) -> ParametricCurve:
        """Returns the nth ParametricCurve in the collection."""
    def get_xyz_curve(self) -> ParametricCurve:
        """Returns the first XYZ curve in the collection, if any, or NULL if there are
        none.
        """
    def get_hpr_curve(self) -> ParametricCurve:
        """Returns the first HPR curve in the collection, if any, or NULL if there are
        none.
        """
    def get_default_curve(self) -> ParametricCurve:
        """If there is an XYZ curve in the collection, returns it; otherwise, returns
        the first curve whose type is unspecified.  Returns NULL if no curve meets
        the criteria.
        """
    def get_num_timewarps(self) -> int:
        """Returns the number of timewarp curves in the collection."""
    def get_timewarp_curve(self, n: int) -> ParametricCurve:
        """Returns the nth timewarp curve in the collection."""
    def get_max_t(self) -> float:
        """Returns the maximum T value associated with the *last* curve in the
        collection.  Normally, this will be either the XYZ or HPR curve, or a
        timewarp curve.
        """
    def make_even(self, max_t: float, segments_per_unit: float) -> None:
        """Discards all existing timewarp curves and recomputes a new timewarp curve
        that maps distance along the curve to parametric time, so that the distance
        between any two points in parametric time is proportional to the
        approximate distance of those same two points along the XYZ curve.

        segments_per_unit represents the number of segments to take per each unit
        of parametric time of the original XYZ curve.

        The new timewarp curve (and thus, the apparent range of the collection)
        will range from 0 to max_t.
        """
    def face_forward(self, segments_per_unit: float) -> None:
        """Discards the existing HPR curve and generates a new one that looks in the
        direction of travel along the XYZ curve, based on the XYZ curve's tangent
        at each point.
        """
    def reset_max_t(self, max_t: float) -> None:
        """Adjusts the apparent length of the curve by applying a new timewarp that
        maps the range [0..max_t] to the range [0..get_max_t()].  After this call,
        the curve collection will contain one more timewarp curve, and get_max_t()
        will return the given max_t value.
        """
    @overload
    def evaluate(self, t: float, result: Mat4Like, cs: _CoordinateSystem = ...) -> bool:
        """`(self, t: float, result: LMatrix4, cs: _CoordinateSystem = ...)`:
        Computes the transform matrix representing translation to the position
        indicated by the first XYZ curve in the collection and the rotation
        indicated by the first HPR curve in the collection, after t has been
        modified by all the timewarp curves in the collection applied in sequence,
        from back to front.

        Returns true if the point is valid (i.e.  t is within the bounds indicated
        by all the timewarp curves and within the bounds of the curves themselves),
        or false otherwise.

        `(self, t: float, xyz: LVecBase3, hpr: LVecBase3)`:
        Computes the position and rotation represented by the first XYZ and HPR
        curves in the collection at the given point t, after t has been modified by
        all the timewarp curves in the collection applied in sequence, from back to
        front.

        Returns true if the point is valid (i.e.  t is within the bounds indicated
        by all the timewarp curves and within the bounds of the curves themselves),
        or false otherwise.
        """
    @overload
    def evaluate(self, t: float, xyz: Vec3Like, hpr: Vec3Like) -> bool: ...
    def evaluate_t(self, t: float) -> float:
        """Determines the value of t that should be passed to the XYZ and HPR curves,
        after applying the given value of t to all the timewarps.  Return -1.0f if
        the value of t exceeds one of the timewarps' ranges.
        """
    def evaluate_xyz(self, t: float, xyz: Vec3Like) -> bool:
        """Computes only the XYZ part of the curves.  See evaluate()."""
    def evaluate_hpr(self, t: float, hpr: Vec3Like) -> bool:
        """Computes only the HPR part of the curves.  See evaluate()."""
    @overload
    def adjust_xyz(self, t: float, xyz: Vec3Like) -> bool:
        """Adjust the XYZ curve at the indicated time to the new value.  The curve
        shape will change correspondingly.  Returns true if successful, false if
        unable to make the adjustment for some reason.
        """
    @overload
    def adjust_xyz(self, t: float, x: float, y: float, z: float) -> bool: ...
    @overload
    def adjust_hpr(self, t: float, xyz: Vec3Like) -> bool:
        """Adjust the HPR curve at the indicated time to the new value.  The curve
        shape will change correspondingly.  Returns true if successful, false if
        unable to make the adjustment for some reason.
        """
    @overload
    def adjust_hpr(self, t: float, h: float, p: float, r: float) -> bool: ...
    def recompute(self) -> bool:
        """Ensures all the curves are freshly computed and up-to-date.  Returns true
        if everything is valid, false if at least one curve is incorrect.
        """
    def stitch(self, a: ParametricCurveCollection, b: ParametricCurveCollection) -> bool:
        """Regenerates this curve as one long curve: the first curve connected end-to-
        end with the second one.  Either a or b may be the same as 'this'.  This
        will lose any timewarps on the input curves.

        Returns true if successful, false on failure.
        """
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the ParametricCurveCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the ParametricCurveCollection
        to the indicated output stream.
        """
    @overload
    def write_egg(self, filename: StrOrBytesPath, cs: _CoordinateSystem = ...) -> bool:
        """`(self, filename: Filename, cs: _CoordinateSystem = ...)`:
        Writes an egg description of all the nurbs curves in the collection to the
        specified output file.  Returns true if the file is successfully written.

        `(self, out: ostream, filename: Filename, cs: _CoordinateSystem)`:
        Writes an egg description of all the nurbs curves in the collection to the
        specified output stream.  Returns true if the file is successfully written.
        """
    @overload
    def write_egg(self, out: ostream, filename: StrOrBytesPath, cs: _CoordinateSystem) -> bool: ...
    def get_curves(self) -> tuple[ParametricCurve, ...]: ...
    def get_timewarp_curves(self) -> tuple[ParametricCurve, ...]: ...
    addCurve = add_curve
    insertCurve = insert_curve
    addCurves = add_curves
    removeCurve = remove_curve
    setCurve = set_curve
    hasCurve = has_curve
    clearTimewarps = clear_timewarps
    getNumCurves = get_num_curves
    getCurve = get_curve
    getXyzCurve = get_xyz_curve
    getHprCurve = get_hpr_curve
    getDefaultCurve = get_default_curve
    getNumTimewarps = get_num_timewarps
    getTimewarpCurve = get_timewarp_curve
    getMaxT = get_max_t
    makeEven = make_even
    faceForward = face_forward
    resetMaxT = reset_max_t
    evaluateT = evaluate_t
    evaluateXyz = evaluate_xyz
    evaluateHpr = evaluate_hpr
    adjustXyz = adjust_xyz
    adjustHpr = adjust_hpr
    writeEgg = write_egg
    getCurves = get_curves
    getTimewarpCurves = get_timewarp_curves

class CurveFitter:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: CurveFitter = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def reset(self) -> None:
        """Removes all the data points previously added to the CurveFitter, and
        initializes it for a new curve.
        """
    def add_xyz(self, t: float, xyz: Vec3Like) -> None:
        """Adds a single sample xyz."""
    def add_hpr(self, t: float, hpr: Vec3Like) -> None:
        """Adds a single sample hpr."""
    def add_xyz_hpr(self, t: float, xyz: Vec3Like, hpr: Vec3Like) -> None:
        """Adds a single sample xyz & hpr simultaneously."""
    def get_num_samples(self) -> int:
        """Returns the number of sample points that have been added."""
    def get_sample_t(self, n: int) -> float:
        """Returns the parametric value of the nth sample added."""
    def get_sample_xyz(self, n: int) -> LVecBase3:
        """Returns the point in space of the nth sample added."""
    def get_sample_hpr(self, n: int) -> LVecBase3:
        """Returns the orientation of the nth sample added."""
    def get_sample_tangent(self, n: int) -> LVecBase3:
        """Returns the tangent associated with the nth sample added.  This is only
        meaningful if compute_tangents() has already been called.
        """
    def remove_samples(self, begin: int, end: int) -> None:
        """Eliminates all samples from index begin, up to but not including index end,
        from the database.
        """
    def sample(self, curves: ParametricCurveCollection, count: int) -> None:
        """Generates a series of data points by sampling the given curve (or xyz/hpr
        curves) the indicated number of times.  The sampling is made evenly in
        parametric time, and then the timewarps, if any, are applied.
        """
    def wrap_hpr(self) -> None:
        """Resets each HPR data point so that the maximum delta between any two
        consecutive points is 180 degrees, which should prevent incorrect HPR
        wrapping.
        """
    def sort_points(self) -> None:
        """Sorts all the data points in order by parametric time, in case they were
        added in an incorrect order.
        """
    def desample(self, factor: float) -> None:
        """Removes sample points in order to reduce the complexity of a sampled curve.
        Keeps one out of every factor samples.  Also keeps the first and the last
        samples.
        """
    def compute_tangents(self, scale: float) -> None:
        """Once a set of points has been built, and prior to calling MakeHermite() or
        MakeNurbs(), ComputeTangents() must be called to set up the tangents
        correctly (unless the tangents were defined as the points were added).
        """
    def make_hermite(self) -> ParametricCurveCollection:
        """Converts the current set of data points into a Hermite curve."""
    def make_nurbs(self) -> ParametricCurveCollection:
        """Converts the current set of data points into a NURBS curve.  This gives a
        smoother curve than produced by MakeHermite().
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    addXyz = add_xyz
    addHpr = add_hpr
    addXyzHpr = add_xyz_hpr
    getNumSamples = get_num_samples
    getSampleT = get_sample_t
    getSampleXyz = get_sample_xyz
    getSampleHpr = get_sample_hpr
    getSampleTangent = get_sample_tangent
    removeSamples = remove_samples
    wrapHpr = wrap_hpr
    sortPoints = sort_points
    computeTangents = compute_tangents
    makeHermite = make_hermite
    makeNurbs = make_nurbs
    getClassType = get_class_type

class PiecewiseCurve(ParametricCurve):
    """A PiecewiseCurve is a curve made up of several curve segments, connected in
    a head-to-tail fashion.  The length of each curve segment in parametric
    space is definable.
    """

    def __init__(self) -> None: ...

class HermiteCurve(PiecewiseCurve):
    """A parametric curve defined by a sequence of control vertices, each with an
    in and out tangent.

    This class is actually implemented as a PiecewiseCurve made up of several
    CubicCurvesegs, each of which is created using the hermite_basis() method.
    The HermiteCurve class itself keeps its own list of the CV's that are used
    to define the curve (since the CubicCurveseg class doesn't retain these).
    """

    def __init__(self, pc: ParametricCurve = ...) -> None:
        """Constructs a Hermite from the indicated (possibly non-hermite) curve."""
    def get_num_cvs(self) -> int:
        """Returns the number of CV's in the curve."""
    def insert_cv(self, t: float) -> int:
        """Inserts a new CV at the given parametric point along the curve.  If this
        parametric point is already on the curve, the CV is assigned an index
        between its two neighbors and the indices of all following CV's are
        incremented by 1; its in and out tangents are chosen to keep the curve
        consistent.  If the new parametric point is beyond the end of the existing
        curve, the curve is extended to meet it and the new CV's position, in
        tangent, and out tangent are set to zero.

        The index number of the new CV is returned.
        """
    @overload
    def append_cv(self, type: int, v: Vec3Like) -> int:
        """Adds a new CV to the end of the curve.  The new CV is given initial in/out
        tangents of 0.  The return value is the index of the new CV.
        """
    @overload
    def append_cv(self, type: int, x: float, y: float, z: float) -> int: ...
    def remove_cv(self, n: int) -> bool:
        """Removes the given CV from the curve.  Returns true if the CV existed, false
        otherwise.
        """
    def remove_all_cvs(self) -> None:
        """Removes all CV's from the curve."""
    def set_cv_type(self, n: int, type: int) -> bool:
        """Changes the given CV's continuity type.  Legal values are HC_CUT, HC_FREE,
        HC_G1, or HC_SMOOTH.

        Other than HC_CUT, these have no effect on the actual curve; it remains up
        to user software to impose the constraints these imply.

        HC_CUT implies a disconnection of the curve; HC_FREE imposes no constraints
        on the tangents; HC_G1 forces the tangents to be collinear, and HC_SMOOTH
        forces the tangents to be identical.  Setting type type to HC_G1 or
        HC_SMOOTH may adjust the out tangent to match the in tangent.
        """
    @overload
    def set_cv_point(self, n: int, v: Vec3Like) -> bool:
        """Changes the given CV's position."""
    @overload
    def set_cv_point(self, n: int, x: float, y: float, z: float) -> bool: ...
    @overload
    def set_cv_in(self, n: int, v: Vec3Like) -> bool:
        """Changes the given CV's in tangent.  Depending on the continuity type, this
        may also adjust the out tangent.
        """
    @overload
    def set_cv_in(self, n: int, x: float, y: float, z: float) -> bool: ...
    @overload
    def set_cv_out(self, n: int, v: Vec3Like) -> bool:
        """Changes the given CV's out tangent.  Depending on the continuity type, this
        may also adjust the in tangent.
        """
    @overload
    def set_cv_out(self, n: int, x: float, y: float, z: float) -> bool: ...
    def set_cv_tstart(self, n: int, tstart: float) -> bool:
        """Changes the given CV's parametric starting time.  This may affect the shape
        of the curve.
        """
    def set_cv_name(self, n: int, name: str) -> bool:
        """Changes the name associated with a particular CV."""
    def get_cv_type(self, n: int) -> int:
        """Returns the given CV's continuity type, HC_CUT, HC_FREE, HC_G1, or
        HC_SMOOTH, or 0 if there is no such CV.
        """
    @overload
    def get_cv_point(self, n: int) -> LVecBase3:
        """Returns the position of the given CV."""
    @overload
    def get_cv_point(self, n: int, v: Vec3Like) -> None: ...
    @overload
    def get_cv_in(self, n: int) -> LVecBase3:
        """Returns the in tangent of the given CV."""
    @overload
    def get_cv_in(self, n: int, v: Vec3Like) -> None: ...
    @overload
    def get_cv_out(self, n: int) -> LVecBase3:
        """Returns the out tangent of the given CV."""
    @overload
    def get_cv_out(self, n: int, v: Vec3Like) -> None: ...
    def get_cv_tstart(self, n: int) -> float:
        """Returns the starting point in parametric space of the given CV."""
    def get_cv_name(self, n: int) -> str:
        """Returns the name of the given CV, or NULL."""
    def write_cv(self, out: ostream, n: int) -> None: ...
    getNumCvs = get_num_cvs
    insertCv = insert_cv
    appendCv = append_cv
    removeCv = remove_cv
    removeAllCvs = remove_all_cvs
    setCvType = set_cv_type
    setCvPoint = set_cv_point
    setCvIn = set_cv_in
    setCvOut = set_cv_out
    setCvTstart = set_cv_tstart
    setCvName = set_cv_name
    getCvType = get_cv_type
    getCvPoint = get_cv_point
    getCvIn = get_cv_in
    getCvOut = get_cv_out
    getCvTstart = get_cv_tstart
    getCvName = get_cv_name
    writeCv = write_cv

class NurbsCurveInterface:
    """This abstract class defines the interface only for a Nurbs-style curve,
    with knots and coordinates in homogeneous space.

    The NurbsCurve class inherits both from this and from ParametricCurve.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_order(self, order: int) -> None: ...
    def get_order(self) -> int: ...
    def get_num_cvs(self) -> int: ...
    def get_num_knots(self) -> int: ...
    def insert_cv(self, t: float) -> bool: ...
    @overload
    def append_cv(self, v: Vec3Like | Vec4Like) -> int: ...
    @overload
    def append_cv(self, x: float, y: float, z: float) -> int: ...
    def remove_cv(self, n: int) -> bool: ...
    def remove_all_cvs(self) -> None: ...
    @overload
    def set_cv_point(self, n: int, v: Vec3Like) -> bool:
        """Repositions the indicated CV.  Returns true if successful, false otherwise."""
    @overload
    def set_cv_point(self, n: int, x: float, y: float, z: float) -> bool: ...
    def get_cv_point(self, n: int) -> LVecBase3:
        """Returns the position of the indicated CV."""
    def set_cv_weight(self, n: int, w: float) -> bool:
        """Sets the weight of the indicated CV without affecting its position in 3-d
        space.
        """
    def get_cv_weight(self, n: int) -> float:
        """Returns the weight of the indicated CV."""
    def set_cv(self, n: int, v: Vec4Like) -> bool: ...
    def get_cv(self, n: int) -> LVecBase4: ...
    def set_knot(self, n: int, t: float) -> bool: ...
    def get_knot(self, n: int) -> float: ...
    def write_cv(self, out: ostream, n: int) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_cvs(self) -> tuple[LVecBase4, ...]: ...
    def get_knots(self) -> tuple[float, ...]: ...
    setOrder = set_order
    getOrder = get_order
    getNumCvs = get_num_cvs
    getNumKnots = get_num_knots
    insertCv = insert_cv
    appendCv = append_cv
    removeCv = remove_cv
    removeAllCvs = remove_all_cvs
    setCvPoint = set_cv_point
    getCvPoint = get_cv_point
    setCvWeight = set_cv_weight
    getCvWeight = get_cv_weight
    setCv = set_cv
    getCv = get_cv
    setKnot = set_knot
    getKnot = get_knot
    writeCv = write_cv
    getClassType = get_class_type
    getCvs = get_cvs
    getKnots = get_knots

class NurbsCurve(PiecewiseCurve, NurbsCurveInterface):
    """A Nonuniform Rational B-Spline.

    This class is actually implemented as a PiecewiseCurve made up of several
    CubicCurvesegs, each of which is created using the nurbs_basis() method.
    The list of CV's and knots is kept here, within the NurbsCurve class.

    This class is the original Panda-native implementation of a NURBS curve.
    It is typedeffed as "NurbsCurve" and performs all NURBS curve functions if
    we do not have the NURBS++ library available.

    However, if we *do* have the NURBS++ library, another class exists, the
    NurbsPPCurve, which is a wrapper around that library and provides some
    additional functionality.  In that case, the other class is typedeffed to
    "NurbsCurve" instead of this one, and performs most of the NURBS curve
    functions.  This class then becomes vestigial.
    """

    def __init__(self, pc: ParametricCurve = ...) -> None:
        """Constructs a NURBS curve equivalent to the indicated (possibly non-NURBS)
        curve.
        """
    def upcast_to_PiecewiseCurve(self) -> PiecewiseCurve: ...
    def upcast_to_NurbsCurveInterface(self) -> NurbsCurveInterface: ...
    upcastToPiecewiseCurve = upcast_to_PiecewiseCurve
    upcastToNurbsCurveInterface = upcast_to_NurbsCurveInterface

class NurbsCurveResult(ReferenceCount):
    """The result of a NurbsCurveEvaluator.  This object represents a curve in a
    particular coordinate space.  It can return the point and/or tangent to the
    curve at any point.

    This is not related to NurbsCurve, CubicCurveseg or any of the
    ParametricCurve-derived objects in this module.  It is a completely
    parallel implementation of NURBS curves, and will probably eventually
    replace the whole ParametricCurve class hierarchy.
    """

    def __init__(self, __param0: NurbsCurveResult) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_start_t(self) -> float:
        """Returns the first legal value of t on the curve.  Usually this is 0.0."""
    def get_end_t(self) -> float:
        """Returns the last legal value of t on the curve."""
    def eval_point(self, t: float, point: Vec3Like) -> bool:
        """Computes the point on the curve corresponding to the indicated value in
        parametric time.  Returns true if the t value is valid, false otherwise.
        """
    def eval_tangent(self, t: float, tangent: Vec3Like) -> bool:
        """Computes the tangent to the curve at the indicated point in parametric
        time.  This tangent vector will not necessarily be normalized, and could be
        zero.  See also eval_point().
        """
    def eval_extended_point(self, t: float, d: int) -> float:
        """Evaluates the curve in n-dimensional space according to the extended
        vertices associated with the curve in the indicated dimension.
        """
    def eval_extended_points(self, t: float, d: int, result: array[float], num_values: int) -> bool:
        """Simultaneously performs eval_extended_point on a contiguous sequence of
        dimensions.  The dimensions evaluated are d through (d + num_values - 1);
        the results are filled into the num_values elements in the indicated result
        array.
        """
    def get_num_segments(self) -> int:
        """Returns the number of piecewise continuous segments within the curve.  This
        number is usually not important unless you plan to call
        eval_segment_point().
        """
    def eval_segment_point(self, segment: int, t: float, point: Vec3Like) -> None:
        """Evaluates the point on the curve corresponding to the indicated value in
        parametric time within the indicated curve segment.  t should be in the
        range [0, 1].

        The curve is internally represented as a number of connected (or possibly
        unconnected) piecewise continuous segments.  The exact number of segments
        for a particular curve depends on the knot vector, and is returned by
        get_num_segments().  Normally, eval_point() is used to evaluate a point
        along the continuous curve, but when you care more about local continuity,
        you can use eval_segment_point() to evaluate the points along each segment.
        """
    def eval_segment_tangent(self, segment: int, t: float, tangent: Vec3Like) -> None:
        """As eval_segment_point, but computes the tangent to the curve at the
        indicated point.  The tangent vector will not necessarily be normalized,
        and could be zero, particularly at the endpoints.
        """
    def eval_segment_extended_point(self, segment: int, t: float, d: int) -> float:
        """Evaluates the curve in n-dimensional space according to the extended
        vertices associated with the curve in the indicated dimension.
        """
    def eval_segment_extended_points(self, segment: int, t: float, d: int, result: array[float], num_values: int) -> None:
        """Simultaneously performs eval_extended_point on a contiguous sequence of
        dimensions.  The dimensions evaluated are d through (d + num_values - 1);
        the results are filled into the num_values elements in the indicated result
        array.
        """
    def get_segment_t(self, segment: int, t: float) -> float:
        """Accepts a t value in the range [0, 1], and assumed to be relative to the
        indicated segment (as in eval_segment_point()), and returns the
        corresponding t value in the entire curve (as in eval_point()).
        """
    def adaptive_sample(self, tolerance: float) -> None:
        """Determines the set of subdivisions necessary to approximate the curve with
        a set of linear segments, no point of which is farther than tolerance units
        from the actual curve.

        After this call, you may walk through the resulting set of samples with
        get_num_samples(), get_sample_t(), and get_sample_point().
        """
    def get_num_samples(self) -> int:
        """Returns the number of sample points generated by the previous call to
        adaptive_sample().
        """
    def get_sample_t(self, n: int) -> float:
        """Returns the t value of the nth sample point generated by the previous call
        to adaptive_sample().
        """
    def get_sample_point(self, n: int) -> LPoint3:
        """Returns the point on the curve of the nth sample point generated by the
        previous call to adaptive_sample().

        For tangents, or extended points, you should use get_sample_t() and pass it
        into eval_tangent() or eval_extended_point().
        """
    def get_sample_ts(self) -> tuple[float, ...]: ...
    def get_sample_points(self) -> tuple[LPoint3, ...]: ...
    getStartT = get_start_t
    getEndT = get_end_t
    evalPoint = eval_point
    evalTangent = eval_tangent
    evalExtendedPoint = eval_extended_point
    evalExtendedPoints = eval_extended_points
    getNumSegments = get_num_segments
    evalSegmentPoint = eval_segment_point
    evalSegmentTangent = eval_segment_tangent
    evalSegmentExtendedPoint = eval_segment_extended_point
    evalSegmentExtendedPoints = eval_segment_extended_points
    getSegmentT = get_segment_t
    adaptiveSample = adaptive_sample
    getNumSamples = get_num_samples
    getSampleT = get_sample_t
    getSamplePoint = get_sample_point
    getSampleTs = get_sample_ts
    getSamplePoints = get_sample_points

class NurbsCurveEvaluator(ReferenceCount):
    """This class is an abstraction for evaluating NURBS curves.  It accepts an
    array of vertices, each of which may be in a different coordinate space (as
    defined by a NodePath), as well as an optional knot vector.

    This is not related to NurbsCurve, CubicCurveseg or any of the
    ParametricCurve-derived objects in this module.  It is a completely
    parallel implementation of NURBS curves, and will probably eventually
    replace the whole ParametricCurve class hierarchy.
    """

    def __init__(self, __param0: NurbsCurveEvaluator = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_order(self, order: int) -> None:
        """Sets the order of the curve.  This resets the knot vector to the default
        knot vector for the number of vertices.

        The order must be 1, 2, 3, or 4, and the value is one more than the degree
        of the curve.
        """
    def get_order(self) -> int:
        """Returns the order of the curve as set by a previous call to set_order()."""
    def reset(self, num_vertices: int) -> None:
        """Resets all the vertices and knots to their default values, and sets the
        curve up with the indicated number of vertices.  You must then call
        set_vertex() repeatedly to fill in all of the vertex values appropriately.
        """
    def get_num_vertices(self) -> int:
        """Returns the number of control vertices in the curve.  This is the number
        passed to the last call to reset().
        """
    @overload
    def set_vertex(self, i: int, vertex: Vec4Like) -> None:
        """`(self, i: int, vertex: LVecBase3, weight: float = ...)`:
        Sets the nth control vertex of the curve.  This flavor sets the vertex as a
        3-d coordinate and a weight; the 3-d coordinate values are implicitly
        scaled up by the weight factor.

        `(self, i: int, vertex: LVecBase4)`:
        Sets the nth control vertex of the curve, as a vertex in 4-d homogeneous
        space.  In this form, the first three components of the vertex should
        already have been scaled by the fourth component, which is the homogeneous
        weight.
        """
    @overload
    def set_vertex(self, i: int, vertex: Vec3Like, weight: float = ...) -> None: ...
    def get_vertex(self, i: int, rel_to: NodePath = ...) -> LVecBase4:
        """`(self, i: int)`:
        Returns the nth control vertex of the curve, relative to its indicated
        coordinate space.

        `(self, i: int, rel_to: NodePath)`:
        Returns the nth control vertex of the curve, relative to the given
        coordinate space.
        """
    def set_vertex_space(self, i: int, space: NodePath | str) -> None:
        """`(self, i: int, space: NodePath)`:
        Sets the coordinate space of the nth control vertex.  If this is not
        specified, or is set to an empty NodePath, the nth control vertex is deemed
        to be in the coordinate space passed to evaluate().

        This specifies the space as a fixed NodePath, which is always the same
        NodePath.  Also see setting the space as a path string, which can specify a
        different NodePath for different instances of the curve.

        `(self, i: int, space: str)`:
        Sets the coordinate space of the nth control vertex.  If this is not
        specified, or is set to an empty string, the nth control vertex is deemed
        to be in the coordinate space passed to evaluate().

        This specifies the space as a string, which describes the path to find the
        node relative to the rel_to NodePath when the curve is evaluated.
        """
    def get_vertex_space(self, i: int, rel_to: NodePath) -> NodePath:
        """Returns the coordinate space of the nth control vertex of the curve,
        expressed as a NodePath.
        """
    def set_extended_vertex(self, i: int, d: int, value: float) -> None:
        """Sets an n-dimensional vertex value.  This allows definition of a NURBS
        surface or curve in a sparse n-dimensional space, typically used for
        associating additional properties (like color or joint membership) with
        each vertex of a surface.

        The value d is an arbitrary integer value and specifies the dimension of
        question for this particular vertex.  Any number of dimensions may be
        specified, and they need not be consecutive.  If a value for a given
        dimension is not specified, is it implicitly 0.0.

        The value is implicitly scaled by the homogenous weight value--that is, the
        fourth component of the value passed to set_vertex().  This means the
        ordinary vertex must be set first, before the extended vertices can be set.
        """
    def get_extended_vertex(self, i: int, d: int) -> float:
        """Returns an n-dimensional vertex value.  See set_extended_vertex().  This
        returns the value set for the indicated dimension, or 0.0 if nothing has
        been set.
        """
    def set_extended_vertices(self, i: int, d: int, values: array[float], num_values: int) -> None:
        """Simultaneously sets several extended values in the slots d through (d +
        num_values - 1) from the num_values elements of the indicated array.  This
        is equivalent to calling set_extended_vertex() num_values times.  See
        set_extended_vertex().
        """
    def get_num_knots(self) -> int:
        """Returns the number of knot values in the curve.  This is based on the
        number of vertices and the order.
        """
    def set_knot(self, i: int, knot: float) -> None:
        """Sets the value of the nth knot.  Each knot value should be greater than or
        equal to the preceding value.  If no knot values are set, a default knot
        vector is supplied.
        """
    def get_knot(self, i: int) -> float:
        """Returns the value of the nth knot."""
    def normalize_knots(self) -> None:
        """Normalizes the knot sequence so that the parametric range of the curve is 0
        .. 1.
        """
    def get_num_segments(self) -> int:
        """Returns the number of piecewise continuous segments in the curve.  This is
        based on the knot vector.
        """
    @overload
    def evaluate(self, rel_to: NodePath = ...) -> NurbsCurveResult:
        """`(self, rel_to: NodePath = ...)`:
        Returns a NurbsCurveResult object that represents the result of applying
        the knots to all of the current values of the vertices, transformed into
        the indicated coordinate space.

        `(self, rel_to: NodePath, mat: LMatrix4)`:
        Returns a NurbsCurveResult object that represents the result of applying
        the knots to all of the current values of the vertices, transformed into
        the indicated coordinate space, and then further transformed by the
        indicated matrix.
        """
    @overload
    def evaluate(self, rel_to: NodePath, mat: Mat4Like) -> NurbsCurveResult: ...
    def output(self, out: ostream) -> None: ...
    def get_vertices(self) -> tuple[LVecBase4, ...]: ...
    def get_knots(self) -> tuple[float, ...]: ...
    setOrder = set_order
    getOrder = get_order
    getNumVertices = get_num_vertices
    setVertex = set_vertex
    getVertex = get_vertex
    setVertexSpace = set_vertex_space
    getVertexSpace = get_vertex_space
    setExtendedVertex = set_extended_vertex
    getExtendedVertex = get_extended_vertex
    setExtendedVertices = set_extended_vertices
    getNumKnots = get_num_knots
    setKnot = set_knot
    getKnot = get_knot
    normalizeKnots = normalize_knots
    getNumSegments = get_num_segments
    getVertices = get_vertices
    getKnots = get_knots

class NurbsSurfaceResult(ReferenceCount):
    """The result of a NurbsSurfaceEvaluator.  This object represents a surface in
    a particular coordinate space.  It can return the point and/or normal to
    the surface at any point.
    """

    def __init__(self, __param0: NurbsSurfaceResult) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_start_u(self) -> float:
        """Returns the first legal value of u on the surface.  Usually this is 0.0."""
    def get_end_u(self) -> float:
        """Returns the last legal value of u on the surface."""
    def get_start_v(self) -> float:
        """Returns the first legal value of v on the surface.  Usually this is 0.0."""
    def get_end_v(self) -> float:
        """Returns the last legal value of v on the surface."""
    def eval_point(self, u: float, v: float, point: Vec3Like) -> bool:
        """Computes the point on the surface corresponding to the indicated value in
        parametric time.  Returns true if the u, v values are valid, false
        otherwise.
        """
    def eval_normal(self, u: float, v: float, normal: Vec3Like) -> bool:
        """Computes the normal to the surface at the indicated point in parametric
        time.  This normal vector will not necessarily be normalized, and could be
        zero.  See also eval_point().
        """
    def eval_extended_point(self, u: float, v: float, d: int) -> float:
        """Evaluates the surface in n-dimensional space according to the extended
        vertices associated with the surface in the indicated dimension.
        """
    def eval_extended_points(self, u: float, v: float, d: int, result: array[float], num_values: int) -> bool:
        """Simultaneously performs eval_extended_point on a contiguous sequence of
        dimensions.  The dimensions evaluated are d through (d + num_values - 1);
        the results are filled into the num_values elements in the indicated result
        array.
        """
    def get_num_u_segments(self) -> int:
        """Returns the number of piecewise continuous segments within the surface in
        the U direction.  This number is usually not important unless you plan to
        call eval_segment_point().
        """
    def get_num_v_segments(self) -> int:
        """Returns the number of piecewise continuous segments within the surface in
        the V direction.  This number is usually not important unless you plan to
        call eval_segment_point().
        """
    def eval_segment_point(self, ui: int, vi: int, u: float, v: float, point: Vec3Like) -> None:
        """Evaluates the point on the surface corresponding to the indicated value in
        parametric time within the indicated surface segment.  u and v should be in
        the range [0, 1].

        The surface is internally represented as a number of connected (or possibly
        unconnected) piecewise continuous segments.  The exact number of segments
        for a particular surface depends on the knot vector, and is returned by
        get_num_segments().  Normally, eval_point() is used to evaluate a point
        along the continuous surface, but when you care more about local
        continuity, you can use eval_segment_point() to evaluate the points along
        each segment.
        """
    def eval_segment_normal(self, ui: int, vi: int, u: float, v: float, normal: Vec3Like) -> None:
        """As eval_segment_point, but computes the normal to the surface at the
        indicated point.  The normal vector will not necessarily be normalized, and
        could be zero.
        """
    def eval_segment_extended_point(self, ui: int, vi: int, u: float, v: float, d: int) -> float:
        """Evaluates the surface in n-dimensional space according to the extended
        vertices associated with the surface in the indicated dimension.
        """
    def eval_segment_extended_points(
        self, ui: int, vi: int, u: float, v: float, d: int, result: array[float], num_values: int
    ) -> None:
        """Simultaneously performs eval_extended_point on a contiguous sequence of
        dimensions.  The dimensions evaluated are d through (d + num_values - 1);
        the results are filled into the num_values elements in the indicated result
        array.
        """
    def get_segment_u(self, ui: int, u: float) -> float:
        """Accepts a u value in the range [0, 1], and assumed to be relative to the
        indicated segment (as in eval_segment_point()), and returns the
        corresponding u value in the entire surface (as in eval_point()).
        """
    def get_segment_v(self, vi: int, v: float) -> float:
        """Accepts a v value in the range [0, 1], and assumed to be relative to the
        indicated segment (as in eval_segment_point()), and returns the
        corresponding v value in the entire surface (as in eval_point()).
        """
    getStartU = get_start_u
    getEndU = get_end_u
    getStartV = get_start_v
    getEndV = get_end_v
    evalPoint = eval_point
    evalNormal = eval_normal
    evalExtendedPoint = eval_extended_point
    evalExtendedPoints = eval_extended_points
    getNumUSegments = get_num_u_segments
    getNumVSegments = get_num_v_segments
    evalSegmentPoint = eval_segment_point
    evalSegmentNormal = eval_segment_normal
    evalSegmentExtendedPoint = eval_segment_extended_point
    evalSegmentExtendedPoints = eval_segment_extended_points
    getSegmentU = get_segment_u
    getSegmentV = get_segment_v

class NurbsSurfaceEvaluator(ReferenceCount):
    """This class is an abstraction for evaluating NURBS surfaces.  It accepts an
    array of vertices, each of which may be in a different coordinate space (as
    defined by a NodePath), as well as an optional knot vector.
    """

    u_order: int
    v_order: int
    @property
    def u_knots(self) -> MutableSequence[float]: ...
    @property
    def v_knots(self) -> MutableSequence[float]: ...
    def __init__(self, __param0: NurbsSurfaceEvaluator = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_u_order(self, u_order: int) -> None:
        """Sets the order of the surface in the U direction.  This resets the knot
        vector to the default knot vector for the number of vertices.

        The order must be 1, 2, 3, or 4, and the value is one more than the degree
        of the surface.
        """
    def get_u_order(self) -> int:
        """Returns the order of the surface in the U direction as set by a previous
        call to set_u_order().
        """
    def set_v_order(self, v_order: int) -> None:
        """Sets the order of the surface in the V direction.  This resets the knot
        vector to the default knot vector for the number of vertices.

        The order must be 1, 2, 3, or 4, and the value is one more than the degree
        of the surface.
        """
    def get_v_order(self) -> int:
        """Returns the order of the surface in the V direction as set by a previous
        call to set_v_order().
        """
    def reset(self, num_u_vertices: int, num_v_vertices: int) -> None:
        """Resets all the vertices and knots to their default values, and sets the
        surface up with the indicated number of vertices.  You must then call
        set_vertex() repeatedly to fill in all of the vertex values appropriately.
        """
    def get_num_u_vertices(self) -> int:
        """Returns the number of control vertices in the U direction on the surface.
        This is the number passed to the last call to reset().
        """
    def get_num_v_vertices(self) -> int:
        """Returns the number of control vertices in the V direction on the surface.
        This is the number passed to the last call to reset().
        """
    @overload
    def set_vertex(self, ui: int, vi: int, vertex: Vec4Like) -> None:
        """`(self, ui: int, vi: int, vertex: LVecBase3, weight: float = ...)`:
        Sets the nth control vertex of the surface.  This flavor sets the vertex as
        a 3-d coordinate and a weight; the 3-d coordinate values are implicitly
        scaled up by the weight factor.

        `(self, ui: int, vi: int, vertex: LVecBase4)`:
        Sets the nth control vertex of the surface, as a vertex in 4-d homogeneous
        space.  In this form, the first three components of the vertex should
        already have been scaled by the fourth component, which is the homogeneous
        weight.
        """
    @overload
    def set_vertex(self, ui: int, vi: int, vertex: Vec3Like, weight: float = ...) -> None: ...
    def get_vertex(self, ui: int, vi: int, rel_to: NodePath = ...) -> LVecBase4:
        """`(self, ui: int, vi: int)`:
        Returns the nth control vertex of the surface, relative to its indicated
        coordinate space.

        `(self, ui: int, vi: int, rel_to: NodePath)`:
        Returns the nth control vertex of the surface, relative to the given
        coordinate space.
        """
    def set_vertex_space(self, ui: int, vi: int, space: NodePath | str) -> None:
        """`(self, ui: int, vi: int, space: NodePath)`:
        Sets the coordinate space of the nth control vertex.  If this is not
        specified, or is set to an empty NodePath, the nth control vertex is deemed
        to be in the coordinate space passed to evaluate().

        This specifies the space as a fixed NodePath, which is always the same
        NodePath.  Also see setting the space as a path string, which can specify a
        different NodePath for different instances of the surface.

        `(self, ui: int, vi: int, space: str)`:
        Sets the coordinate space of the nth control vertex.  If this is not
        specified, or is set to an empty string, the nth control vertex is deemed
        to be in the coordinate space passed to evaluate().

        This specifies the space as a string, which describes the path to find the
        node relative to the rel_to NodePath when the surface is evaluated.
        """
    def get_vertex_space(self, ui: int, vi: int, rel_to: NodePath) -> NodePath:
        """Returns the coordinate space of the nth control vertex of the surface,
        expressed as a NodePath.
        """
    def set_extended_vertex(self, ui: int, vi: int, d: int, value: float) -> None:
        """Sets an n-dimensional vertex value.  This allows definition of a NURBS
        surface or surface in a sparse n-dimensional space, typically used for
        associating additional properties (like color or joint membership) with
        each vertex of a surface.

        The value d is an arbitrary integer value and specifies the dimension of
        question for this particular vertex.  Any number of dimensions may be
        specified, and they need not be consecutive.  If a value for a given
        dimension is not specified, is it implicitly 0.0.

        The value is implicitly scaled by the homogenous weight value--that is, the
        fourth component of the value passed to set_vertex().  This means the
        ordinary vertex must be set first, before the extended vertices can be set.
        """
    def get_extended_vertex(self, ui: int, vi: int, d: int) -> float:
        """Returns an n-dimensional vertex value.  See set_extended_vertex().  This
        returns the value set for the indicated dimension, or 0.0 if nothing has
        been set.
        """
    def set_extended_vertices(self, ui: int, vi: int, d: int, values: array[float], num_values: int) -> None:
        """Simultaneously sets several extended values in the slots d through (d +
        num_values - 1) from the num_values elements of the indicated array.  This
        is equivalent to calling set_extended_vertex() num_values times.  See
        set_extended_vertex().
        """
    def get_num_u_knots(self) -> int:
        """Returns the number of knot values in the surface in the U direction.  This
        is based on the number of vertices and the order.
        """
    def set_u_knot(self, i: int, knot: float) -> None:
        """Sets the value of the nth knot.  Each knot value should be greater than or
        equal to the preceding value.  If no knot values are set, a default knot
        vector is supplied.
        """
    def get_u_knot(self, i: int) -> float:
        """Returns the value of the nth knot."""
    def normalize_u_knots(self) -> None:
        """Normalizes the knot sequence so that the parametric range of the surface in
        the U direction is 0 .. 1.
        """
    def get_num_v_knots(self) -> int:
        """Returns the number of knot values in the surface in the V direction.  This
        is based on the number of vertices and the order.
        """
    def set_v_knot(self, i: int, knot: float) -> None:
        """Sets the value of the nth knot.  Each knot value should be greater than or
        equal to the preceding value.  If no knot values are set, a default knot
        vector is supplied.
        """
    def get_v_knot(self, i: int) -> float:
        """Returns the value of the nth knot."""
    def normalize_v_knots(self) -> None:
        """Normalizes the knot sequence so that the parametric range of the surface in
        the U direction is 0 .. 1.
        """
    def get_num_u_segments(self) -> int:
        """Returns the number of piecewise continuous segments in the surface in the U
        direction.  This is based on the knot vector.
        """
    def get_num_v_segments(self) -> int:
        """Returns the number of piecewise continuous segments in the surface in the V
        direction.  This is based on the knot vector.
        """
    def evaluate(self, rel_to: NodePath = ...) -> NurbsSurfaceResult:
        """Returns a NurbsSurfaceResult object that represents the result of applying
        the knots to all of the current values of the vertices, transformed into
        the indicated coordinate space.
        """
    def output(self, out: ostream) -> None: ...
    def get_u_knots(self) -> tuple[float, ...]: ...
    def get_v_knots(self) -> tuple[float, ...]: ...
    setUOrder = set_u_order
    getUOrder = get_u_order
    setVOrder = set_v_order
    getVOrder = get_v_order
    getNumUVertices = get_num_u_vertices
    getNumVVertices = get_num_v_vertices
    setVertex = set_vertex
    getVertex = get_vertex
    setVertexSpace = set_vertex_space
    getVertexSpace = get_vertex_space
    setExtendedVertex = set_extended_vertex
    getExtendedVertex = get_extended_vertex
    setExtendedVertices = set_extended_vertices
    getNumUKnots = get_num_u_knots
    setUKnot = set_u_knot
    getUKnot = get_u_knot
    normalizeUKnots = normalize_u_knots
    getNumVKnots = get_num_v_knots
    setVKnot = set_v_knot
    getVKnot = get_v_knot
    normalizeVKnots = normalize_v_knots
    getNumUSegments = get_num_u_segments
    getNumVSegments = get_num_v_segments
    getUKnots = get_u_knots
    getVKnots = get_v_knots

class RopeNode(PandaNode):
    """This class draws a visible representation of the NURBS curve stored in its
    NurbsCurveEvaluator.  It automatically recomputes the curve every frame.

    This is not related to NurbsCurve, CubicCurveseg or any of the
    ParametricCurve-derived objects in this module.  It is a completely
    parallel implementation of NURBS curves, and will probably eventually
    replace the whole ParametricCurve class hierarchy.
    """

    RM_thread: Final = 0
    RMThread: Final = 0
    RM_tape: Final = 1
    RMTape: Final = 1
    RM_billboard: Final = 2
    RMBillboard: Final = 2
    RM_tube: Final = 3
    RMTube: Final = 3
    UV_none: Final = 0
    UVNone: Final = 0
    UV_parametric: Final = 1
    UVParametric: Final = 1
    UV_distance: Final = 2
    UVDistance: Final = 2
    UV_distance2: Final = 3
    UVDistance2: Final = 3
    NM_none: Final = 0
    NMNone: Final = 0
    NM_vertex: Final = 1
    NMVertex: Final = 1
    curve: NurbsCurveEvaluator
    render_mode: _RopeNode_RenderMode
    uv_mode: _RopeNode_UVMode
    uv_direction: bool
    uv_scale: float
    normal_mode: _RopeNode_NormalMode
    tube_up: LVector3
    use_vertex_color: bool
    num_subdiv: int
    num_slices: int
    use_vertex_thickness: bool
    thickness: float
    matrix: LMatrix4
    @property
    def vertex_color_dimension(self) -> int: ...
    @property
    def vertex_thickness_dimension(self) -> int: ...
    def set_curve(self, curve: NurbsCurveEvaluator) -> None:
        """Sets the particular curve represented by the RopeNode."""
    def get_curve(self) -> NurbsCurveEvaluator:
        """Returns the curve represented by the RopeNode."""
    def set_render_mode(self, render_mode: _RopeNode_RenderMode) -> None:
        """Specifies the method used to render the rope.  The simplest is RM_thread,
        which just draws a one-pixel line segment.
        """
    def get_render_mode(self) -> _RopeNode_RenderMode:
        """Returns the method used to render the rope.  See set_render_mode()."""
    def set_uv_mode(self, uv_mode: _RopeNode_UVMode) -> None:
        """Specifies the algorithm to use to generate UV's for the rope."""
    def get_uv_mode(self) -> _RopeNode_UVMode:
        """Returns the algorithm to use to generate UV's for the rope."""
    def set_uv_direction(self, u_dominant: bool) -> None:
        """Specify true to vary the U coordinate down the length of the rope, or false
        to vary the V coordinate.
        """
    def get_uv_direction(self) -> bool:
        """Returns true if the rope runs down the U coordinate of the texture, or
        false if it runs down the V coordinate.
        """
    def set_uv_scale(self, scale: float) -> None:
        """Specifies an additional scaling factor to apply to generated UV's along the
        rope.  This scale factor is applied in whichever direction is along the
        rope, as specified by set_uv_direction().
        """
    def get_uv_scale(self) -> float:
        """Returns the scaling factor to apply to generated UV's for the rope."""
    def set_normal_mode(self, normal_mode: _RopeNode_NormalMode) -> None:
        """Specifies the kind of normals to generate for the rope.  This is only
        applicable when the RenderMode is set to RM_tube; in the other render
        modes, normals are never generated.
        """
    def get_normal_mode(self) -> _RopeNode_NormalMode:
        """Returns the kind of normals to generate for the rope.  This is only
        applicable when the RenderMode is set to RM_tube.
        """
    def set_tube_up(self, tube_up: Vec3Like) -> None:
        """Specifies a normal vector, generally perpendicular to the main axis of the
        starting point of the curve, that controls the "top" of the curve, when
        RenderMode is RM_tube.  This is used to orient the vertices that make up
        the tube.  If this vector is too nearly parallel with the starting
        direction of the curve, there may be a tendency for the whole tube to
        gimble-lock around its primary axis.
        """
    def get_tube_up(self) -> LVector3:
        """Returns the normal vector used to control the "top" of the curve, when
        RenderMode is RM_tube.  See set_tube_up().
        """
    def set_use_vertex_color(self, flag: bool) -> None:
        """Sets the "use vertex color" flag.  When this is true, the R, G, B, A vertex
        color is assumed to be stored as the dimensions n + 0, n + 1, n + 2, n + 3,
        respectively, of the extended vertex values, where n is the value returned
        by get_vertex_color_dimension().  Use
        NurbsCurveEvaluator::set_extended_vertex() to set these values.
        """
    def get_use_vertex_color(self) -> bool:
        """Returns the "use vertex color" flag.  See set_use_vertex_color()."""
    @staticmethod
    def get_vertex_color_dimension() -> int:
        """Returns the numeric extended dimension in which the color components should
        be found.  See NurbsCurveEvaluator::set_extended_vertex().

        The color components will be expected at (n, n + 1, n + 2, n + 3).
        """
    def set_num_subdiv(self, num_subdiv: int) -> None:
        """Specifies the number of subdivisions per cubic segment (that is, per unique
        knot value) to draw in a fixed uniform tesselation of the curve.
        """
    def get_num_subdiv(self) -> int:
        """Returns the number of subdivisions per cubic segment to draw.  See
        set_num_subdiv().
        """
    def set_num_slices(self, num_slices: int) -> None:
        """Specifies the number of radial subdivisions to make if RenderMode is
        RM_tube.  It is ignored in the other render modes.

        Increasing this number increases the roundness of a cross-section of the
        tube.  The minimum value for a dimensional tube is 3; setting it to 2 will
        get you a thin piece of tape (which is similar to RM_billboard, except it
        won't rotate to face the camera).
        """
    def get_num_slices(self) -> int:
        """Returns the number of radial subdivisions to make if RenderMode is RM_tube.
        It is ignored in the other render modes.  See set_num_slices().
        """
    def set_use_vertex_thickness(self, flag: bool) -> None:
        """Sets the "use vertex thickness" flag.  When this is true, the vertex
        thickness is assumed to be stored as the dimension
        get_vertex_thickness_dimension(), of the extended vertex values.  Use
        NurbsCurveEvaluator::set_extended_vertex() to set these values.

        In this mode, the overall thickness is also applied as a scale to the
        vertex thickness.  Not all render modes support vertex thickness.
        """
    def get_use_vertex_thickness(self) -> bool:
        """Returns the "use vertex thickness" flag.  See set_use_vertex_thickness()."""
    @staticmethod
    def get_vertex_thickness_dimension() -> int:
        """Returns the numeric extended dimension in which the thickness component
        should be found.  See NurbsCurveEvaluator::set_extended_vertex().
        """
    def set_thickness(self, thickness: float) -> None:
        """Specifies the thickness of the rope, in pixels or in spatial units,
        depending on the render mode.  See set_render_mode().

        The thickness may also be specified on a per-vertex basis.  See
        set_use_vertex_thickness().
        """
    def get_thickness(self) -> float:
        """Returns the thickness of the rope.  See set_thickness()."""
    def set_matrix(self, matrix: Mat4Like) -> None:
        """Specifies an optional matrix which is used to transform each control vertex
        after it has been transformed into the RopeNode's coordinate space, but
        before the polygon vertices are generated.
        """
    def clear_matrix(self) -> None:
        """Resets the node's matrix to identity.  See set_matrix()."""
    def has_matrix(self) -> bool:
        """Returns true if the node has a matrix set, false otherwise.  See
        set_matrix().
        """
    def get_matrix(self) -> LMatrix4:
        """Returns the optional matrix which is used to transform each control vertex
        after it has been transformed into the RopeNode's coordinate space, but
        before the polygon vertices are generated.
        """
    def reset_bound(self, rel_to: NodePath) -> None:
        """Recomputes the bounding volume.  This is normally called automatically, but
        it must occasionally be called explicitly when the curve has changed
        properties outside of this node's knowledge.
        """
    setCurve = set_curve
    getCurve = get_curve
    setRenderMode = set_render_mode
    getRenderMode = get_render_mode
    setUvMode = set_uv_mode
    getUvMode = get_uv_mode
    setUvDirection = set_uv_direction
    getUvDirection = get_uv_direction
    setUvScale = set_uv_scale
    getUvScale = get_uv_scale
    setNormalMode = set_normal_mode
    getNormalMode = get_normal_mode
    setTubeUp = set_tube_up
    getTubeUp = get_tube_up
    setUseVertexColor = set_use_vertex_color
    getUseVertexColor = get_use_vertex_color
    getVertexColorDimension = get_vertex_color_dimension
    setNumSubdiv = set_num_subdiv
    getNumSubdiv = get_num_subdiv
    setNumSlices = set_num_slices
    getNumSlices = get_num_slices
    setUseVertexThickness = set_use_vertex_thickness
    getUseVertexThickness = get_use_vertex_thickness
    getVertexThicknessDimension = get_vertex_thickness_dimension
    setThickness = set_thickness
    getThickness = get_thickness
    setMatrix = set_matrix
    clearMatrix = clear_matrix
    hasMatrix = has_matrix
    getMatrix = get_matrix
    resetBound = reset_bound

class SheetNode(PandaNode):
    """This class draws a visible representation of the NURBS surface stored in
    its NurbsSurfaceEvaluator.  It automatically recomputes the surface every
    frame.

    This is not related to NurbsSurface, CubicSurfaceseg or any of the
    ParametricSurface-derived objects in this module.  It is a completely
    parallel implementation of NURBS surfaces, and will probably eventually
    replace the whole ParametricSurface class hierarchy.
    """

    def set_surface(self, surface: NurbsSurfaceEvaluator) -> None:
        """Sets the particular surface represented by the SheetNode."""
    def get_surface(self) -> NurbsSurfaceEvaluator:
        """Returns the surface represented by the SheetNode."""
    def set_use_vertex_color(self, flag: bool) -> None:
        """Sets the "use vertex color" flag.  When this is true, the R, G, B, A vertex
        color is assumed to be stored as the dimensions 0, 1, 2, 3, respectively,
        of the extended vertex values.  Use
        NurbsCurveEvaluator::set_extended_vertex() to set these values.
        """
    def get_use_vertex_color(self) -> bool:
        """Returns the "use vertex color" flag.  See set_use_vertex_color()."""
    def set_num_u_subdiv(self, num_u_subdiv: int) -> None:
        """Specifies the number of subdivisions per cubic segment (that is, per unique
        knot value) to draw in a fixed uniform tesselation of the surface in the U
        direction.
        """
    def get_num_u_subdiv(self) -> int:
        """Returns the number of subdivisions per cubic segment to draw in the U
        direction.  See set_num_u_subdiv().
        """
    def set_num_v_subdiv(self, num_v_subdiv: int) -> None:
        """Specifies the number of subdivisions per cubic segment (that is, per unique
        knot value) to draw in a fixed uniform tesselation of the surface in the V
        direction.
        """
    def get_num_v_subdiv(self) -> int:
        """Returns the number of subdivisions per cubic segment to draw in the V
        direction.  See set_num_v_subdiv().
        """
    def reset_bound(self, rel_to: NodePath) -> None:
        """Recomputes the bounding volume.  This is normally called automatically, but
        it must occasionally be called explicitly when the surface has changed
        properties outside of this node's knowledge.
        """
    setSurface = set_surface
    getSurface = get_surface
    setUseVertexColor = set_use_vertex_color
    getUseVertexColor = get_use_vertex_color
    setNumUSubdiv = set_num_u_subdiv
    getNumUSubdiv = get_num_u_subdiv
    setNumVSubdiv = set_num_v_subdiv
    getNumVSubdiv = get_num_v_subdiv
    resetBound = reset_bound
