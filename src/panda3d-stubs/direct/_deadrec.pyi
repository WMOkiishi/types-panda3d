from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Vec3Like
from panda3d.core._dtoolutil import ostream
from panda3d.core._linmath import LPoint3, LVecBase3
from panda3d.core._pgraph import NodePath

_SmoothMover_SmoothMode: TypeAlias = Literal[0, 1]
_SmoothMover_PredictionMode: TypeAlias = Literal[0, 1]

class SmoothMover:
    """This class handles smoothing of sampled motion points over time, e.g.  for
    smoothing the apparent movement of remote avatars, whose positions are sent
    via occasional telemetry updates.

    It can operate in any of three modes: off, in which it does not smooth any
    motion but provides the last position it was told; smoothing only, in which
    it smooths motion information but never tries to anticipate where the
    avatar might be going; or full prediction, in which it smooths motion as
    well as tries to predict the avatar's position in lead of the last position
    update.  The assumption is that all SmoothMovers in the world will be
    operating in the same mode together.
    """

    SM_off: Final = 0
    SMOff: Final = 0
    SM_on: Final = 1
    SMOn: Final = 1
    PM_off: Final = 0
    PMOff: Final = 0
    PM_on: Final = 1
    PMOn: Final = 1
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: SmoothMover = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def set_pos(self, pos: Vec3Like) -> bool:
        """Specifies the position of the SmoothMover at a particular time in the past.
        When mark_position() is called, this will be recorded (along with hpr and
        timestamp) in a position report, which will then be used along with all
        other position reports to determine the smooth position at any particular
        instant.

        The return value is true if any parameter has changed since the last call
        to set_pos(), or false if they are the same.
        """
    @overload
    def set_pos(self, x: float, y: float, z: float) -> bool: ...
    def set_x(self, x: float) -> bool:
        """Sets the X position only.  See set_pos()."""
    def set_y(self, y: float) -> bool:
        """Sets the Y position only.  See set_pos()."""
    def set_z(self, z: float) -> bool:
        """Sets the Z position only.  See set_pos()."""
    @overload
    def set_hpr(self, hpr: Vec3Like) -> bool:
        """Specifies the orientation of the SmoothMover at a particular time in the
        past.  When mark_position() is called, this will be recorded (along with
        hpr and timestamp) in a position report, which will then be used along with
        all other position reports to determine the smooth position at any
        particular instant.

        The return value is true if any parameter has changed since the last call
        to set_hpr(), or false if they are the same.
        """
    @overload
    def set_hpr(self, h: float, p: float, r: float) -> bool: ...
    def set_h(self, h: float) -> bool:
        """Sets the heading only.  See set_hpr()."""
    def set_p(self, p: float) -> bool:
        """Sets the pitch only.  See set_hpr()."""
    def set_r(self, r: float) -> bool:
        """Sets the roll only.  See set_hpr()."""
    @overload
    def set_pos_hpr(self, pos: Vec3Like, hpr: Vec3Like) -> bool:
        """`(self, pos: LVecBase3, hpr: LVecBase3)`:
        Specifies the position and orientation of the SmoothMover at a particular
        time in the past.  When mark_position() is called, this will be recorded
        (along with timestamp) in a position report, which will then be used along
        with all other position reports to determine the smooth position at any
        particular instant.

        The return value is true if any parameter has changed since the last call
        to set_pos_hpr(), or false if they are the same.

        `(self, x: float, y: float, z: float, h: float, p: float, r: float)`:
        Specifies the position of the SmoothMover at a particular time in the past.
        When mark_position() is called, this will be recorded (along with
        timestamp) in a position report, which will then be used along with all
        other position reports to determine the smooth position at any particular
        instant.

        The return value is true if any parameter has changed since the last call
        to set_pos_hpr(), or false if they are the same.
        """
    @overload
    def set_pos_hpr(self, x: float, y: float, z: float, h: float, p: float, r: float) -> bool: ...
    def get_sample_pos(self) -> LPoint3:
        """Returns the current position of the working sample point.  This position is
        updated periodically by set_x(), set_y(), etc., and its current value is
        copied to the sample point table when mark_position() is called.
        """
    def get_sample_hpr(self) -> LVecBase3:
        """Returns the current orientation of the working sample point.  This
        orientation is updated periodically by set_h(), set_p(), etc., and its
        current value is copied to the sample point table when mark_position() is
        called.
        """
    def set_phony_timestamp(self, timestamp: float = ..., period_adjust: bool = ...) -> None:
        """Lies and specifies that the current position report was received now.  This
        is usually used for very old position reports for which we're not sure of
        the actual receipt time.
        """
    def set_timestamp(self, timestamp: float) -> None:
        """Specifies the time that the current position report applies.  This should
        be called, along with set_pos() and set_hpr(), before a call to
        mark_position().
        """
    def has_most_recent_timestamp(self) -> bool:
        """Returns true if we have most recently recorded timestamp"""
    def get_most_recent_timestamp(self) -> float:
        """Returns most recently recorded timestamp"""
    def mark_position(self) -> None:
        """Stores the position, orientation, and timestamp (if relevant) indicated by
        previous calls to set_pos(), set_hpr(), and set_timestamp() in a new
        position report.

        When compute_smooth_position() is called, it uses these stored position
        reports to base its computation of the known position.
        """
    def clear_positions(self, reset_velocity: bool) -> None:
        """Erases all the old position reports.  This should be done, for instance,
        prior to teleporting the avatar to a new position; otherwise, the smoother
        might try to lerp the avatar there.  If reset_velocity is true, the
        velocity is also reset to 0.
        """
    def compute_smooth_position(self, timestamp: float = ...) -> bool:
        """`(self)`:
        Computes the smoothed position (and orientation) of the mover at the
        indicated point in time, based on the previous position reports.  After
        this call has been made, get_smooth_pos() etc.  may be called to retrieve
        the smoothed position.

        With no parameter, the function uses ClockObject::get_frame_time() as the
        default time.

        `(self, timestamp: float)`:
        Computes the smoothed position (and orientation) of the mover at the
        indicated point in time, based on the previous position reports.  After
        this call has been made, get_smooth_pos() etc.  may be called to retrieve
        the smoothed position.

        The return value is true if the value has changed (or might have changed)
        since the last call to compute_smooth_position(), or false if it remains
        the same.
        """
    def get_latest_position(self) -> bool:
        """Updates the smooth_pos (and smooth_hpr, etc.) members to reflect the
        absolute latest position known for this avatar.  This may result in a pop
        to the most recent position.

        Returns true if the latest position is known, false otherwise.
        """
    def get_smooth_pos(self) -> LPoint3:
        """Returns the smoothed position as computed by a previous call to
        compute_smooth_position().
        """
    def get_smooth_hpr(self) -> LVecBase3:
        """Returns the smoothed orientation as computed by a previous call to
        compute_smooth_position().
        """
    def apply_smooth_pos(self, node: NodePath) -> None:
        """Applies the smoothed position to the indicated NodePath.  This is
        equivalent to calling node.set_pos(smooth_mover->get_smooth_pos()).  It
        exists as an optimization only, to avoid the overhead of passing the return
        value through Python.
        """
    def apply_smooth_pos_hpr(self, pos_node: NodePath, hpr_node: NodePath) -> None:
        """Applies the smoothed position and orientation to the indicated NodePath.
        This is equivalent to calling
        node.set_pos_hpr(smooth_mover->get_smooth_pos(),
        smooth_mover->get_smooth_hpr()).  It exists as an optimization only, to
        avoid the overhead of passing the return value through Python.
        """
    def apply_smooth_hpr(self, node: NodePath) -> None:
        """Applies the smoothed orientation to the indicated NodePath.  This is
        equivalent to calling node.set_hpr(smooth_mover->get_smooth_hpr()).  It
        exists as an optimization only, to avoid the overhead of passing the return
        value through Python.
        """
    def compute_and_apply_smooth_pos(self, node: NodePath) -> None:
        """A further optimization to reduce Python calls.  This computes the smooth
        position and applies it to the indicated node in one call.
        """
    def compute_and_apply_smooth_pos_hpr(self, pos_node: NodePath, hpr_node: NodePath) -> None:
        """A further optimization to reduce Python calls.  This computes the smooth
        position and applies it to the indicated node or nodes in one call.  The
        pos_node and hpr_node might be the same NodePath.
        """
    def compute_and_apply_smooth_hpr(self, hpr_node: NodePath) -> None:
        """A further optimization to reduce Python calls.  This computes the smooth
        position and applies it to the indicated node or nodes in one call.  The
        pos_node and hpr_node might be the same NodePath.
        """
    def get_smooth_forward_velocity(self) -> float:
        """Returns the speed at which the avatar is moving, in feet per second, along
        its own forward axis (after applying the avatar's hpr).  This will be a
        positive number if the avatar is moving forward, and a negative number if
        it is moving backward.
        """
    def get_smooth_lateral_velocity(self) -> float:
        """Returns the speed at which the avatar is moving, in feet per second, along
        its own lateral axis (after applying the avatar's hpr).  This will be a
        positive number if the avatar is moving right, and a negative number if it
        is moving left.
        """
    def get_smooth_rotational_velocity(self) -> float:
        """Returns the speed at which the avatar is rotating in the horizontal plane
        (i.e.  heading), in degrees per second.  This may be positive or negative,
        according to the direction of rotation.
        """
    def get_forward_axis(self) -> LVecBase3:
        """Returns the smoothed position as computed by a previous call to
        compute_smooth_position().
        """
    def handle_wrt_reparent(self, old_parent: NodePath, new_parent: NodePath) -> None:
        """Node is being wrtReparented, update recorded sample positions to reflect
        new parent
        """
    def set_smooth_mode(self, mode: _SmoothMover_SmoothMode) -> None:
        """Sets the smoothing mode of all SmoothMovers in the world.  If this is
        SM_off, no smoothing or prediction will be performed, and get_smooth_pos()
        will simply return the position last set by mark_position().
        """
    def get_smooth_mode(self) -> _SmoothMover_SmoothMode:
        """Returns the smoothing mode of all SmoothMovers in the world.  See
        set_smooth_mode().
        """
    def set_prediction_mode(self, mode: _SmoothMover_PredictionMode) -> None:
        """Sets the predictioning mode of all SmoothMovers in the world.  If this is
        PM_off, no prediction will be performed, but smoothing might still be
        performed.
        """
    def get_prediction_mode(self) -> _SmoothMover_PredictionMode:
        """Returns the predictioning mode of all SmoothMovers in the world.  See
        set_prediction_mode().
        """
    def set_delay(self, delay: float) -> None:
        """Sets the amount of time, in seconds, to delay the computed position of a
        SmoothMover.  This is particularly useful when the prediction mode is off,
        because it can allow the apparent motion of an avatar to appear smooth
        without relying on prediction, at the cost of introducing additional lag in
        the avatar's apparent position.
        """
    def get_delay(self) -> float:
        """Returns the amount of time, in seconds, to delay the computed position of a
        SmoothMover.  See set_delay().
        """
    def set_accept_clock_skew(self, flag: bool) -> None:
        """Sets the 'accept clock skew' flag.  When this flag is true, clock skew from
        the other clients will be tolerated by delaying each smooth mover's
        position an additional amount, on top of that specified by set_delay(),
        based on the measured average latency for timestamp messages received by
        the client.

        In this way, if the other client has significant clock skew with respect to
        our clock, it will be evident as a large positive or negative average
        latency for timestamps.  By subtracting out this average latency, we
        compensate for poor clock sync.
        """
    def get_accept_clock_skew(self) -> bool:
        """Returns the current state of the 'accept clock skew' flag.  See
        set_accept_clock_skew().
        """
    def set_max_position_age(self, age: float) -> None:
        """Sets the maximum amount of time a position is allowed to remain unchanged
        before assuming it represents the avatar actually standing still.
        """
    def get_max_position_age(self) -> float:
        """Returns the maximum amount of time a position is allowed to remain
        unchanged before assuming it represents the avatar actually standing still.
        """
    def set_expected_broadcast_period(self, period: float) -> None:
        """Sets the interval at which we expect the SmoothNodes to broadcast their
        position, in elapsed seconds.  This controls the length of time we assume
        the object has truly stopped, when we receive a long sequence of no
        updates.
        """
    def get_expected_broadcast_period(self) -> float:
        """Returns the interval at which we expect the SmoothNodes to broadcast their
        position, in elapsed seconds.  See set_expected_broadcast_period().
        """
    def set_reset_velocity_age(self, age: float) -> None:
        """Sets the amount of time that should elapse after the last position report
        before the velocity is reset to 0.  This is similar to max_position_age,
        but it is only used to determine the resetting of the reported velocity.
        It should always be greater than or equal to max_position_age.
        """
    def get_reset_velocity_age(self) -> float:
        """Returns the amount of time that should elapse after the last position
        report before the velocity is reset to 0.  See set_reset_velocity_age().
        """
    def set_directional_velocity(self, flag: bool) -> None:
        """Sets the flag that indicates whether the avatar's direction is considered
        in computing the velocity.  When this is true, velocity is automatically
        decomposed into a forward and a lateral velocity (and both may be positive
        or negative); when it is false, all velocity is always returned as forward
        velocity (and it is always positive).
        """
    def get_directional_velocity(self) -> bool:
        """Returns the current state of the 'directional velocity' flag.  See
        set_directional_velocity().
        """
    def set_default_to_standing_still(self, flag: bool) -> None:
        """Sets the flag that indicates whether to assume that the node stopped moving
        during periods when we don't get enough position updates.  If true, the
        object will stand still momentarily.  If false, the object will
        continuously lerp between the position updates that we did get.
        """
    def get_default_to_standing_still(self) -> bool:
        """Returns the current state of the 'default to standing still' flag.  See
        set_default_to_standing_still().
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    setPos = set_pos
    setX = set_x
    setY = set_y
    setZ = set_z
    setHpr = set_hpr
    setH = set_h
    setP = set_p
    setR = set_r
    setPosHpr = set_pos_hpr
    getSamplePos = get_sample_pos
    getSampleHpr = get_sample_hpr
    setPhonyTimestamp = set_phony_timestamp
    setTimestamp = set_timestamp
    hasMostRecentTimestamp = has_most_recent_timestamp
    getMostRecentTimestamp = get_most_recent_timestamp
    markPosition = mark_position
    clearPositions = clear_positions
    computeSmoothPosition = compute_smooth_position
    getLatestPosition = get_latest_position
    getSmoothPos = get_smooth_pos
    getSmoothHpr = get_smooth_hpr
    applySmoothPos = apply_smooth_pos
    applySmoothPosHpr = apply_smooth_pos_hpr
    applySmoothHpr = apply_smooth_hpr
    computeAndApplySmoothPos = compute_and_apply_smooth_pos
    computeAndApplySmoothPosHpr = compute_and_apply_smooth_pos_hpr
    computeAndApplySmoothHpr = compute_and_apply_smooth_hpr
    getSmoothForwardVelocity = get_smooth_forward_velocity
    getSmoothLateralVelocity = get_smooth_lateral_velocity
    getSmoothRotationalVelocity = get_smooth_rotational_velocity
    getForwardAxis = get_forward_axis
    handleWrtReparent = handle_wrt_reparent
    setSmoothMode = set_smooth_mode
    getSmoothMode = get_smooth_mode
    setPredictionMode = set_prediction_mode
    getPredictionMode = get_prediction_mode
    setDelay = set_delay
    getDelay = get_delay
    setAcceptClockSkew = set_accept_clock_skew
    getAcceptClockSkew = get_accept_clock_skew
    setMaxPositionAge = set_max_position_age
    getMaxPositionAge = get_max_position_age
    setExpectedBroadcastPeriod = set_expected_broadcast_period
    getExpectedBroadcastPeriod = get_expected_broadcast_period
    setResetVelocityAge = set_reset_velocity_age
    getResetVelocityAge = get_reset_velocity_age
    setDirectionalVelocity = set_directional_velocity
    getDirectionalVelocity = get_directional_velocity
    setDefaultToStandingStill = set_default_to_standing_still
    getDefaultToStandingStill = get_default_to_standing_still
