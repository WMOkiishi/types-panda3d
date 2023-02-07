from collections.abc import Generator
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import Vec2Like, Vec3Like, Vec4Like
from panda3d.core._chan import AnimControl
from panda3d.core._dtoolbase import TypeHandle
from panda3d.core._dtoolutil import ostream
from panda3d.core._event import EventQueue
from panda3d.core._express import TypedReferenceCount
from panda3d.core._gobj import TextureStage
from panda3d.core._pgraph import NodePath

_CInterval_State: TypeAlias = Literal[0, 1, 2, 3]
_CInterval_EventType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_CLerpInterval_BlendType: TypeAlias = Literal[0, 1, 2, 3, 4]
_CMetaInterval_RelativeStart: TypeAlias = Literal[0, 1, 2]
_CMetaInterval_DefType: TypeAlias = Literal[0, 1, 2, 3]

class CInterval(TypedReferenceCount):
    """The base class for timeline components.  A CInterval represents a single
    action, event, or collection of nested intervals that will be performed at
    some specific time or over a period of time.

    This is essentially similar to the Python "Interval" class, but it is
    implemented in C++ (hence the name). Intervals that may be implemented in
    C++ will inherit from this class; Intervals that must be implemented in
    Python will inherit from the similar Python class.
    """

    ET_initialize: Final = 0
    ETInitialize: Final = 0
    ET_instant: Final = 1
    ETInstant: Final = 1
    ET_step: Final = 2
    ETStep: Final = 2
    ET_finalize: Final = 3
    ETFinalize: Final = 3
    ET_reverse_initialize: Final = 4
    ETReverseInitialize: Final = 4
    ET_reverse_instant: Final = 5
    ETReverseInstant: Final = 5
    ET_reverse_finalize: Final = 6
    ETReverseFinalize: Final = 6
    ET_interrupt: Final = 7
    ETInterrupt: Final = 7
    S_initial: Final = 0
    SInitial: Final = 0
    S_started: Final = 1
    SStarted: Final = 1
    S_paused: Final = 2
    SPaused: Final = 2
    S_final: Final = 3
    SFinal: Final = 3
    done_event: str
    t: float
    auto_pause: bool
    auto_finish: bool
    manager: CIntervalManager
    play_rate: float
    @property
    def name(self) -> str: ...
    @property
    def duration(self) -> float: ...
    @property
    def open_ended(self) -> bool: ...
    @property
    def state(self) -> _CInterval_State: ...
    @property
    def stopped(self) -> bool: ...
    @property
    def playing(self) -> bool: ...
    def __init__(self, __param0: CInterval) -> None: ...
    def __await__(self) -> Generator[Any, None, Any]: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_name(self) -> str:
        """Returns the interval's name."""
    def get_duration(self) -> float:
        """Returns the duration of the interval in seconds."""
    def get_open_ended(self) -> bool:
        """Returns the state of the "open_ended" flag.  This is primarily intended for
        instantaneous intervals like FunctionIntervals; it indicates true if the
        interval has some lasting effect that should be applied even if the
        interval doesn't get started until after its finish time, or false if the
        interval is a transitive thing that doesn't need to be called late.
        """
    def get_state(self) -> _CInterval_State:
        """Indicates the state the interval believes it is in: whether it has been
        started, is currently in the middle, or has been finalized.
        """
    def is_stopped(self) -> bool:
        """Returns true if the interval is in either its initial or final states (but
        not in a running or paused state).
        """
    def set_done_event(self, event: str) -> None:
        """Sets the event that is generated whenever the interval reaches its final
        state, whether it is explicitly finished or whether it gets there on its
        own.
        """
    def get_done_event(self) -> str:
        """Returns the event that is generated whenever the interval reaches its final
        state, whether it is explicitly finished or whether it gets there on its
        own.
        """
    def set_t(self, t: float) -> None:
        """Explicitly sets the time within the interval.  Normally, you would use
        start() .. finish() to let the time play normally, but this may be used to
        set the time to some particular value.
        """
    def get_t(self) -> float:
        """Returns the current time of the interval: the last value of t passed to
        priv_initialize(), priv_step(), or priv_finalize().
        """
    def set_auto_pause(self, auto_pause: bool) -> None:
        """Changes the state of the 'auto_pause' flag.  If this is true, the interval
        may be arbitrarily interrupted when the system needs to reset due to some
        external event by calling CIntervalManager::interrupt().  If this is false
        (the default), the interval must always be explicitly finished or paused.
        """
    def get_auto_pause(self) -> bool:
        """Returns the state of the 'auto_pause' flag.  See set_auto_pause()."""
    def set_auto_finish(self, auto_finish: bool) -> None:
        """Changes the state of the 'auto_finish' flag.  If this is true, the interval
        may be arbitrarily finished when the system needs to reset due to some
        external event by calling CIntervalManager::interrupt().  If this is false
        (the default), the interval must always be explicitly finished or paused.
        """
    def get_auto_finish(self) -> bool:
        """Returns the state of the 'auto_finish' flag.  See set_auto_finish()."""
    def set_wants_t_callback(self, wants_t_callback: bool) -> None:
        """Changes the state of the 'wants_t_callback' flag.  If this is true, the
        interval will be returned by CIntervalManager::get_event() each time the
        interval's time value has been changed, regardless of whether it has any
        external events.
        """
    def get_wants_t_callback(self) -> bool:
        """Returns the state of the 'wants_t_callback' flag.  See
        set_wants_t_callback().
        """
    def set_manager(self, manager: CIntervalManager) -> None:
        """Indicates the CIntervalManager object which will be responsible for playing
        this interval.  This defaults to the global CIntervalManager; you should
        need to change this only if you have special requirements for playing this
        interval.
        """
    def get_manager(self) -> CIntervalManager:
        """Returns the CIntervalManager object which will be responsible for playing
        this interval.  Note that this can only return a C++ object; if the
        particular CIntervalManager object has been extended in the scripting
        language, this will return the encapsulated C++ object, not the full
        extended object.
        """
    def start(self, start_t: float = ..., end_t: float = ..., play_rate: float = ...) -> None:
        """Starts the interval playing by registering it with the current
        CIntervalManager.  The interval will play to the end and stop.

        If end_t is less than zero, it indicates the end of the interval.
        """
    def loop(self, start_t: float = ..., end_t: float = ..., play_rate: float = ...) -> None:
        """Starts the interval playing by registering it with the current
        CIntervalManager.  The interval will play until it is interrupted with
        finish() or pause(), looping back to start_t when it reaches end_t.

        If end_t is less than zero, it indicates the end of the interval.
        """
    def pause(self) -> float:
        """Stops the interval from playing but leaves it in its current state.  It may
        later be resumed from this point by calling resume().
        """
    def resume(self, start_t: float = ...) -> None:
        """`(self)`:
        Restarts the interval from its current point after a previous call to
        pause().

        `(self, start_t: float)`:
        Restarts the interval from the indicated point after a previous call to
        pause().
        """
    def resume_until(self, end_t: float) -> None:
        """Restarts the interval from the current point after a previous call to
        pause() (or a previous play-to-point-and-stop), to play until the indicated
        point and then stop.
        """
    def finish(self) -> None:
        """Stops the interval from playing and sets it to its final state."""
    def clear_to_initial(self) -> None:
        """Pauses the interval, if it is playing, and resets its state to its initial
        state, abandoning any state changes already in progress in the middle of
        the interval.  Calling this is like pausing the interval and discarding it,
        creating a new one in its place.
        """
    def is_playing(self) -> bool:
        """Returns true if the interval is currently playing, false otherwise."""
    def get_play_rate(self) -> float:
        """Returns the play rate as set by the last call to start(), loop(), or
        set_play_rate().
        """
    def set_play_rate(self, play_rate: float) -> None:
        """Changes the play rate of the interval.  If the interval is already started,
        this changes its speed on-the-fly.  Note that since play_rate is a
        parameter to start() and loop(), the next call to start() or loop() will
        reset this parameter.
        """
    def priv_do_event(self, t: float, event: _CInterval_EventType) -> None:
        """These cannot be declared private because they must be accessible to
        Python, but the method names are prefixed with priv_ to remind you that
        you probably don't want to be using them directly.
        """
    def priv_initialize(self, t: float) -> None:
        """This replaces the first call to priv_step(), and indicates that the
        interval has just begun.  This may be overridden by derived classes that
        need to do some explicit initialization on the first call.
        """
    def priv_instant(self) -> None:
        """This is called in lieu of priv_initialize() .. priv_step() ..
        priv_finalize(), when everything is to happen within one frame.  The
        interval should initialize itself, then leave itself in the final state.
        """
    def priv_step(self, t: float) -> None:
        """Advances the time on the interval.  The time may either increase (the
        normal case) or decrease (e.g.  if the interval is being played by a
        slider).
        """
    def priv_finalize(self) -> None:
        """This is called to stop an interval, forcing it to whatever state it would
        be after it played all the way through.  It's generally invoked by
        set_final_t().
        """
    def priv_reverse_initialize(self, t: float) -> None:
        """Similar to priv_initialize(), but this is called when the interval is being
        played backwards; it indicates that the interval should start at the
        finishing state and undo any intervening intervals.
        """
    def priv_reverse_instant(self) -> None:
        """This is called in lieu of priv_reverse_initialize() .. priv_step() ..
        priv_reverse_finalize(), when everything is to happen within one frame.
        The interval should initialize itself, then leave itself in the initial
        state.
        """
    def priv_reverse_finalize(self) -> None:
        """Called generally following a priv_reverse_initialize(), this indicates the
        interval should set itself to the initial state.
        """
    def priv_interrupt(self) -> None:
        """This is called while the interval is playing to indicate that it is about
        to be interrupted; that is, priv_step() will not be called for a length of
        time.  But the interval should remain in its current state in anticipation
        of being eventually restarted when the calls to priv_step() eventually
        resume.

        The purpose of this function is to allow self-running intervals like sound
        intervals to stop the actual sound playback during the pause.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int) -> None: ...
    def setup_play(self, start_time: float, end_time: float, play_rate: float, do_loop: bool) -> None:
        """Called to prepare the interval for automatic timed playback, e.g.  via a
        Python task.  The interval will be played from start_t to end_t, at a time
        factor specified by play_rate.  start_t must always be less than end_t
        (except for the exception for end_t == -1, below), but if play_rate is
        negative the interval will be played backwards.

        Specify end_t of -1 to play the entire interval from start_t.

        Call step_play() repeatedly to execute the interval.
        """
    def setup_resume(self) -> None:
        """Called to prepare the interval for restarting at the current point within
        the interval after an interruption.
        """
    def setup_resume_until(self, end_t: float) -> None:
        """Called to prepare the interval for restarting from the current point after
        a previous call to pause() (or a previous play-to-point-and-stop), to play
        until the indicated point and then stop.
        """
    def step_play(self) -> bool:
        """Should be called once per frame to execute the automatic timed playback
        begun with setup_play().

        Returns true if the interval should continue, false if it is done and
        should stop.
        """
    getName = get_name
    getDuration = get_duration
    getOpenEnded = get_open_ended
    getState = get_state
    isStopped = is_stopped
    setDoneEvent = set_done_event
    getDoneEvent = get_done_event
    setT = set_t
    getT = get_t
    setAutoPause = set_auto_pause
    getAutoPause = get_auto_pause
    setAutoFinish = set_auto_finish
    getAutoFinish = get_auto_finish
    setWantsTCallback = set_wants_t_callback
    getWantsTCallback = get_wants_t_callback
    setManager = set_manager
    getManager = get_manager
    resumeUntil = resume_until
    clearToInitial = clear_to_initial
    isPlaying = is_playing
    getPlayRate = get_play_rate
    setPlayRate = set_play_rate
    privDoEvent = priv_do_event
    privInitialize = priv_initialize
    privInstant = priv_instant
    privStep = priv_step
    privFinalize = priv_finalize
    privReverseInitialize = priv_reverse_initialize
    privReverseInstant = priv_reverse_instant
    privReverseFinalize = priv_reverse_finalize
    privInterrupt = priv_interrupt
    setupPlay = setup_play
    setupResume = setup_resume
    setupResumeUntil = setup_resume_until
    stepPlay = step_play

class CIntervalManager:
    """This object holds a number of currently-playing intervals and is
    responsible for advancing them each frame as needed.

    There is normally only one IntervalManager object in the world, and it is
    the responsibility of the scripting language to call step() on this object
    once each frame, and to then process the events indicated by
    get_next_event().

    It is also possible to create multiple IntervalManager objects for special
    needs.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def set_event_queue(self, event_queue: EventQueue) -> None:
        """Specifies a custom event queue to be used for throwing done events from
        intervals as they finish.  If this is not specified, the global event queue
        is used.

        The caller maintains ownership of the EventQueue object; it is the caller's
        responsibility to ensure that the supplied EventQueue does not destruct
        during the lifetime of the CIntervalManager.
        """
    def get_event_queue(self) -> EventQueue:
        """Returns the custom event queue to be used for throwing done events from
        intervals as they finish.
        """
    def add_c_interval(self, interval: CInterval, external: bool) -> int:
        """Adds the interval to the manager, and returns a unique index for the
        interval.  This index will be unique among all the currently added
        intervals, but not unique across all intervals ever added to the manager.
        The maximum index value will never exceed the maximum number of intervals
        added at any given time.

        If the external flag is true, the interval is understood to also be stored
        in the scripting language data structures.  In this case, it will be
        available for information returned by get_next_event() and
        get_next_removal().  If external is false, the interval's index will never
        be returned by these two functions.
        """
    def find_c_interval(self, name: str) -> int:
        """Returns the index associated with the named interval, if there is such an
        interval, or -1 if there is not.
        """
    def get_c_interval(self, index: int) -> CInterval:
        """Returns the interval associated with the given index."""
    def remove_c_interval(self, index: int) -> None:
        """Removes the indicated interval from the queue immediately.  It will not be
        returned from get_next_removal(), and none of its pending events, if any,
        will be returned by get_next_event().
        """
    def interrupt(self) -> int:
        """Pauses or finishes (removes from the active queue) all intervals tagged
        with auto_pause or auto_finish set to true.  These are intervals that
        someone fired up but won't necessarily expect to clean up; they can be
        interrupted at will when necessary.

        Returns the number of intervals affected.
        """
    def get_num_intervals(self) -> int:
        """Returns the number of currently active intervals."""
    def get_max_index(self) -> int:
        """Returns one more than the largest interval index number in the manager.  If
        you walk through all the values between (0, get_max_index()] and call
        get_c_interval() on each number, you will retrieve all of the managed
        intervals (and possibly a number of NULL pointers as well).
        """
    def step(self) -> None:
        """This should be called every frame to do the processing for all the active
        intervals.  It will call step_play() for each interval that has been added
        and that has not yet been removed.

        After each call to step(), the scripting language should call
        get_next_event() and get_next_removal() repeatedly to process all the high-
        level (e.g.  Python-interval-based) events and to manage the high-level
        list of intervals.
        """
    def get_next_event(self) -> int:
        """This should be called by the scripting language after each call to step().
        It returns the index number of the next interval that has events requiring
        servicing by the scripting language, or -1 if no more intervals have any
        events pending.

        If this function returns something other than -1, it is the scripting
        language's responsibility to query the indicated interval for its next
        event via get_event_index(), and eventually pop_event().

        Then get_next_event() should be called again until it returns -1.
        """
    def get_next_removal(self) -> int:
        """This should be called by the scripting language after each call to step().
        It returns the index number of an interval that was recently removed, or -1
        if no intervals were removed.

        If this returns something other than -1, the scripting language should
        clean up its own data structures accordingly, and then call
        get_next_removal() again.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_ptr() -> CIntervalManager:
        """Returns the pointer to the one global CIntervalManager object."""
    setEventQueue = set_event_queue
    getEventQueue = get_event_queue
    addCInterval = add_c_interval
    findCInterval = find_c_interval
    getCInterval = get_c_interval
    removeCInterval = remove_c_interval
    getNumIntervals = get_num_intervals
    getMaxIndex = get_max_index
    getNextEvent = get_next_event
    getNextRemoval = get_next_removal
    getGlobalPtr = get_global_ptr

class CConstraintInterval(CInterval):
    """The base class for a family of intervals that constrain some property to a
    value over time.
    """

    bogus_variable: bool
    def __init__(self, __param0: CConstraintInterval) -> None: ...

class CConstrainHprInterval(CConstraintInterval):
    """A constraint interval that will constrain the orientation of one node to
    the orientation of another.
    """

    @overload
    def __init__(self, __param0: CConstrainHprInterval) -> None:
        """Constructs a constraint interval that will constrain the orientation of one
        node to the orientation of another, possibly with an added rotation.

        If wrt is true, the node's orientation will be transformed into the target
        node's parent's  space before being copied.  If wrt is false, the target
        node's local orientation will be copied unaltered.
        """
    @overload
    def __init__(
        self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool, hprOffset: Vec3Like = ...
    ) -> None: ...
    def get_node(self) -> NodePath:
        """Returns the "source" node."""
    def get_target(self) -> NodePath:
        """Returns the "target" node."""
    getNode = get_node
    getTarget = get_target

class CConstrainPosHprInterval(CConstraintInterval):
    """A constraint interval that will constrain the position and orientation of
    one node to the position and orientation of another.
    """

    @overload
    def __init__(self, __param0: CConstrainPosHprInterval) -> None:
        """Constructs a constraint interval that will constrain the position and
        orientation of one node to the position and orientation of another.

        If wrt is true, the node's position and orientation will be transformed
        into the target node's parent's space before being copied.  If wrt is
        false, the target node's local position and orientation will be copied
        unaltered.
        """
    @overload
    def __init__(
        self,
        name: str,
        duration: float,
        node: NodePath,
        target: NodePath,
        wrt: bool,
        posOffset: Vec3Like = ...,
        hprOffset: Vec3Like = ...,
    ) -> None: ...
    def get_node(self) -> NodePath:
        """Returns the "source" node."""
    def get_target(self) -> NodePath:
        """Returns the "target" node."""
    getNode = get_node
    getTarget = get_target

class CConstrainPosInterval(CConstraintInterval):
    """A constraint interval that will constrain the position of one node to the
    position of another.
    """

    @overload
    def __init__(self, __param0: CConstrainPosInterval) -> None:
        """Constructs a constraint interval that will constrain the position of one
        node to the position of another.

        If wrt is true, the node's position will be transformed into the target
        node's parent's  space before being copied.  If wrt is false, the target
        node's local position will be copied unaltered.
        """
    @overload
    def __init__(
        self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool, posOffset: Vec3Like = ...
    ) -> None: ...
    def get_node(self) -> NodePath:
        """Returns the "source" node."""
    def get_target(self) -> NodePath:
        """Returns the "target" node."""
    getNode = get_node
    getTarget = get_target

class CConstrainTransformInterval(CConstraintInterval):
    """A constraint interval that will constrain the transform of one node to the
    transform of another.
    """

    @overload
    def __init__(self, __param0: CConstrainTransformInterval) -> None:
        """Constructs a constraint interval that will constrain the transform of one
        node to the transform of another.  To clarify, the transform of node will
        be copied to target.

        If wrt is true, the node's transform will be transformed into the target
        node's parent's  space before being copied.  If wrt is false, the node's
        local transform will be copied unaltered.
        """
    @overload
    def __init__(self, name: str, duration: float, node: NodePath, target: NodePath, wrt: bool) -> None: ...
    def get_node(self) -> NodePath:
        """Returns the "source" node."""
    def get_target(self) -> NodePath:
        """Returns the "target" node."""
    getNode = get_node
    getTarget = get_target

class CLerpInterval(CInterval):
    """The base class for a family of intervals that linearly interpolate one or
    more numeric values over time.
    """

    BT_no_blend: Final = 0
    BTNoBlend: Final = 0
    BT_ease_in: Final = 1
    BTEaseIn: Final = 1
    BT_ease_out: Final = 2
    BTEaseOut: Final = 2
    BT_ease_in_out: Final = 3
    BTEaseInOut: Final = 3
    BT_invalid: Final = 4
    BTInvalid: Final = 4
    def __init__(self, __param0: CLerpInterval) -> None: ...
    def get_blend_type(self) -> _CLerpInterval_BlendType:
        """Returns the blend type specified for the interval.  This controls how the
        linear interpolation behaves near the beginning and end of the lerp period.
        """
    @staticmethod
    def string_blend_type(blend_type: str) -> _CLerpInterval_BlendType:
        """Returns the BlendType enumerated value corresponding to the indicated
        string, or BT_invalid if the string doesn't match anything.
        """
    getBlendType = get_blend_type
    stringBlendType = string_blend_type

class CLerpAnimEffectInterval(CLerpInterval):
    """This interval lerps between different amounts of control effects for
    various AnimControls that might be playing on an actor.  It's used to
    change the blending amount between multiple animations.

    The idea is to start all the animations playing first, then use a
    CLerpAnimEffectInterval to adjust the degree to which each animation
    affects the actor.
    """

    @overload
    def __init__(self, __param0: CLerpAnimEffectInterval) -> None: ...
    @overload
    def __init__(self, name: str, duration: float, blend_type: _CLerpInterval_BlendType) -> None: ...
    def add_control(self, control: AnimControl, name: str, begin_effect: float, end_effect: float) -> None:
        """Adds another AnimControl to the list of AnimControls affected by the lerp.
        This control will be lerped from begin_effect to end_effect over the period
        of the lerp.

        The AnimControl name parameter is only used when formatting the interval
        for output.
        """
    addControl = add_control

class CLerpNodePathInterval(CLerpInterval):
    """An interval that lerps one or more properties (like pos, hpr, etc.) on a
    NodePath over time.
    """

    @overload
    def __init__(self, __param0: CLerpNodePathInterval) -> None:
        """Constructs a lerp interval that will lerp some properties on the indicated
        node, possibly relative to the indicated other node (if other is nonempty).

        You must call set_end_pos(), etc.  for the various properties you wish to
        lerp before the first call to priv_initialize().  If you want to set a
        starting value for any of the properties, you may call set_start_pos(),
        etc.; otherwise, the starting value is taken from the actual node's value
        at the time the lerp is performed.

        The starting values may be explicitly specified or omitted.  The value of
        bake_in_start determines the behavior if the starting values are omitted.
        If bake_in_start is true, the values are obtained the first time the lerp
        runs, and thenceforth are stored within the interval.  If bake_in_start is
        false, the starting value is computed each frame, based on assuming the
        current value represents the value set from the last time the interval was
        run.  This "smart" behavior allows code to manipulate the object event
        while it is being lerped, and the lerp continues to apply in a sensible
        way.

        If fluid is true, the prev_transform is not adjusted by the lerp;
        otherwise, it is reset.
        """
    @overload
    def __init__(
        self,
        name: str,
        duration: float,
        blend_type: _CLerpInterval_BlendType,
        bake_in_start: bool,
        fluid: bool,
        node: NodePath,
        other: NodePath,
    ) -> None: ...
    def get_node(self) -> NodePath:
        """Returns the node being lerped."""
    def get_other(self) -> NodePath:
        """Returns the "other" node, which the lerped node is being moved relative to.
        If this is an empty node path, the lerped node is being moved in its own
        coordinate system.
        """
    def set_start_pos(self, pos: Vec3Like) -> None:
        """Indicates the initial position of the lerped node.  This is meaningful only
        if set_end_pos() is also called.  This parameter is optional; if
        unspecified, the value will be taken from the node's actual position at the
        time the lerp is performed.
        """
    def set_end_pos(self, pos: Vec3Like) -> None:
        """Indicates that the position of the node should be lerped, and specifies the
        final position of the node.  This should be called before
        priv_initialize().  If this is not called, the node's position will not be
        affected by the lerp.
        """
    def set_start_hpr(self, hpr: Vec3Like) -> None:
        """Indicates the initial rotation of the lerped node.  This is meaningful only
        if either set_end_hpr() or set_end_quat() is also called.  This parameter
        is optional; if unspecified, the value will be taken from the node's actual
        rotation at the time the lerp is performed.
        """
    @overload
    def set_end_hpr(self, quat: Vec4Like) -> None:
        """`(self, quat: LQuaternion)`:
        Indicates that the rotation of the node should be lerped, and specifies the
        final rotation of the node.  This should be called before
        priv_initialize().

        This special function is overloaded to accept a quaternion, even though the
        function name is set_end_hpr().  The quaternion will be implicitly
        converted to a HPR trio, and the lerp will be performed in HPR space,
        componentwise.

        `(self, hpr: LVecBase3)`:
        Indicates that the rotation of the node should be lerped, and specifies the
        final rotation of the node.  This should be called before
        priv_initialize().

        This replaces a previous call to set_end_quat().  If neither set_end_hpr()
        nor set_end_quat() is called, the node's rotation will not be affected by
        the lerp.
        """
    @overload
    def set_end_hpr(self, hpr: Vec3Like) -> None: ...
    def set_start_quat(self, quat: Vec4Like) -> None:
        """Indicates the initial rotation of the lerped node.  This is meaningful only
        if either set_end_quat() or set_end_hpr() is also called.  This parameter
        is optional; if unspecified, the value will be taken from the node's actual
        rotation at the time the lerp is performed.

        The given quaternion needs to be normalized.
        """
    @overload
    def set_end_quat(self, quat: Vec4Like) -> None:
        """`(self, quat: LQuaternion)`:
        Indicates that the rotation of the node should be lerped, and specifies the
        final rotation of the node.  This should be called before
        priv_initialize().

        This replaces a previous call to set_end_hpr().  If neither set_end_quat()
        nor set_end_hpr() is called, the node's rotation will not be affected by
        the lerp.

        The given quaternion needs to be normalized.

        `(self, hpr: LVecBase3)`:
        Indicates that the rotation of the node should be lerped, and specifies the
        final rotation of the node.  This should be called before
        priv_initialize().

        This replaces a previous call to set_end_hpr().  If neither set_end_quat()
        nor set_end_hpr() is called, the node's rotation will not be affected by
        the lerp.

        This special function is overloaded to accept a HPR trio, even though the
        function name is set_end_quat().  The HPR will be implicitly converted to a
        quaternion, and the lerp will be performed in quaternion space, as a
        spherical lerp.
        """
    @overload
    def set_end_quat(self, hpr: Vec3Like) -> None: ...
    def set_start_scale(self, scale: Vec3Like | float) -> None:
        """Indicates the initial scale of the lerped node.  This is meaningful only if
        set_end_scale() is also called.  This parameter is optional; if
        unspecified, the value will be taken from the node's actual scale at the
        time the lerp is performed.
        """
    def set_end_scale(self, scale: Vec3Like | float) -> None:
        """Indicates that the scale of the node should be lerped, and specifies the
        final scale of the node.  This should be called before priv_initialize().
        If this is not called, the node's scale will not be affected by the lerp.
        """
    def set_start_shear(self, shear: Vec3Like) -> None:
        """Indicates the initial shear of the lerped node.  This is meaningful only if
        set_end_shear() is also called.  This parameter is optional; if
        unspecified, the value will be taken from the node's actual shear at the
        time the lerp is performed.
        """
    def set_end_shear(self, shear: Vec3Like) -> None:
        """Indicates that the shear of the node should be lerped, and specifies the
        final shear of the node.  This should be called before priv_initialize().
        If this is not called, the node's shear will not be affected by the lerp.
        """
    def set_start_color(self, color: Vec4Like) -> None:
        """Indicates the initial color of the lerped node.  This is meaningful only if
        set_end_color() is also called.  This parameter is optional; if
        unspecified, the value will be taken from the node's actual color at the
        time the lerp is performed.
        """
    def set_end_color(self, color: Vec4Like) -> None:
        """Indicates that the color of the node should be lerped, and specifies the
        final color of the node.  This should be called before priv_initialize().
        If this is not called, the node's color will not be affected by the lerp.
        """
    def set_start_color_scale(self, color_scale: Vec4Like) -> None:
        """Indicates the initial color scale of the lerped node.  This is meaningful
        only if set_end_color_scale() is also called.  This parameter is optional;
        if unspecified, the value will be taken from the node's actual color scale
        at the time the lerp is performed.
        """
    def set_end_color_scale(self, color_scale: Vec4Like) -> None:
        """Indicates that the color scale of the node should be lerped, and specifies
        the final color scale of the node.  This should be called before
        priv_initialize().  If this is not called, the node's color scale will not
        be affected by the lerp.
        """
    def set_texture_stage(self, stage: TextureStage) -> None:
        """Indicates the texture stage that is adjusted by tex_offset, tex_rotate,
        and/or tex_scale.  If this is not set, the default is the default texture
        stage.
        """
    def set_start_tex_offset(self, tex_offset: Vec2Like) -> None:
        """Indicates the initial UV offset of the lerped node.  This is meaningful
        only if set_end_tex_offset() is also called.  This parameter is optional;
        if unspecified, the value will be taken from the node's actual UV offset at
        the time the lerp is performed.
        """
    def set_end_tex_offset(self, tex_offset: Vec2Like) -> None:
        """Indicates that the UV offset of the node should be lerped, and specifies
        the final UV offset of the node.  This should be called before
        priv_initialize().  If this is not called, the node's UV offset will not be
        affected by the lerp.
        """
    def set_start_tex_rotate(self, tex_rotate: float) -> None:
        """Indicates the initial UV rotate of the lerped node.  This is meaningful
        only if set_end_tex_rotate() is also called.  This parameter is optional;
        if unspecified, the value will be taken from the node's actual UV rotate at
        the time the lerp is performed.
        """
    def set_end_tex_rotate(self, tex_rotate: float) -> None:
        """Indicates that the UV rotate of the node should be lerped, and specifies
        the final UV rotate of the node.  This should be called before
        priv_initialize().  If this is not called, the node's UV rotate will not be
        affected by the lerp.
        """
    def set_start_tex_scale(self, tex_scale: Vec2Like) -> None:
        """Indicates the initial UV scale of the lerped node.  This is meaningful only
        if set_end_tex_scale() is also called.  This parameter is optional; if
        unspecified, the value will be taken from the node's actual UV scale at the
        time the lerp is performed.
        """
    def set_end_tex_scale(self, tex_scale: Vec2Like) -> None:
        """Indicates that the UV scale of the node should be lerped, and specifies the
        final UV scale of the node.  This should be called before
        priv_initialize().  If this is not called, the node's UV scale will not be
        affected by the lerp.
        """
    def set_override(self, override: int) -> None:
        """Changes the override value that will be associated with any state changes
        applied by the lerp.  If this lerp is changing state (for instance, a color
        lerp or a tex matrix lerp), then the new attributes created by this lerp
        will be assigned the indicated override value when they are applied to the
        node.
        """
    def get_override(self) -> int:
        """Returns the override value that will be associated with any state changes
        applied by the lerp.  See set_override().
        """
    getNode = get_node
    getOther = get_other
    setStartPos = set_start_pos
    setEndPos = set_end_pos
    setStartHpr = set_start_hpr
    setEndHpr = set_end_hpr
    setStartQuat = set_start_quat
    setEndQuat = set_end_quat
    setStartScale = set_start_scale
    setEndScale = set_end_scale
    setStartShear = set_start_shear
    setEndShear = set_end_shear
    setStartColor = set_start_color
    setEndColor = set_end_color
    setStartColorScale = set_start_color_scale
    setEndColorScale = set_end_color_scale
    setTextureStage = set_texture_stage
    setStartTexOffset = set_start_tex_offset
    setEndTexOffset = set_end_tex_offset
    setStartTexRotate = set_start_tex_rotate
    setEndTexRotate = set_end_tex_rotate
    setStartTexScale = set_start_tex_scale
    setEndTexScale = set_end_tex_scale
    setOverride = set_override
    getOverride = get_override

class CMetaInterval(CInterval):
    """This interval contains a list of nested intervals, each of which has its
    own begin and end times.  Some of them may overlap and some of them may
    not.
    """

    RS_previous_end: Final = 0
    RSPreviousEnd: Final = 0
    RS_previous_begin: Final = 1
    RSPreviousBegin: Final = 1
    RS_level_begin: Final = 2
    RSLevelBegin: Final = 2
    DT_c_interval: Final = 0
    DTCInterval: Final = 0
    DT_ext_index: Final = 1
    DTExtIndex: Final = 1
    DT_push_level: Final = 2
    DTPushLevel: Final = 2
    DT_pop_level: Final = 3
    DTPopLevel: Final = 3
    @overload
    def __init__(self, __param0: CMetaInterval) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def set_precision(self, precision: float) -> None:
        """Indicates the precision with which time measurements are compared.  For
        numerical accuracy, all floating-point time values are converted to integer
        values internally by scaling by the precision factor.  The larger the
        number given here, the smaller the delta of time that can be
        differentiated; the limit is the maximum integer that can be represented in
        the system.
        """
    def get_precision(self) -> float:
        """Returns the precision with which time measurements are compared.  See
        set_precision().
        """
    def clear_intervals(self) -> None:
        """Resets the list of intervals and prepares for receiving a new list."""
    def push_level(self, name: str, rel_time: float, rel_to: _CMetaInterval_RelativeStart) -> int:
        """Marks the beginning of a nested level of child intervals.  Within the
        nested level, a RelativeStart time of RS_level_begin refers to the start of
        the level, and the first interval added within the level is always relative
        to the start of the level.

        The return value is the index of the def entry created by this push.
        """
    def add_c_interval(self, c_interval: CInterval, rel_time: float = ..., rel_to: _CMetaInterval_RelativeStart = ...) -> int:
        """Adds a new CInterval to the list.  The interval will be played when the
        indicated time (relative to the given point) has been reached.

        The return value is the index of the def entry representing the new
        interval.
        """
    def add_ext_index(
        self, ext_index: int, name: str, duration: float, open_ended: bool, rel_time: float, rel_to: _CMetaInterval_RelativeStart
    ) -> int:
        """Adds a new external interval to the list.  This represents some object in
        the external scripting language that has properties similar to a CInterval
        (for instance, a Python Interval object).

        The CMetaInterval object cannot play this external interval directly, but
        it records a placeholder for it and will ask the scripting language to play
        it when it is time, via is_event_ready() and related methods.

        The ext_index number itself is simply a handle that the scripting language
        makes up and associates with its interval object somehow.  The
        CMetaInterval object does not attempt to interpret this value.

        The return value is the index of the def entry representing the new
        interval.
        """
    def pop_level(self, duration: float = ...) -> int:
        """Finishes a level marked by a previous call to push_level(), and returns to
        the previous level.

        If the duration is not negative, it represents a phony duration to assign
        to the level, for the purposes of sequencing later intervals.  Otherwise,
        the level's duration is computed based on the intervals within the level.
        """
    def set_interval_start_time(self, name: str, rel_time: float, rel_to: _CMetaInterval_RelativeStart = ...) -> bool:
        """Adjusts the start time of the child interval with the given name, if found.
        This may be either a C++ interval added via add_c_interval(), or an
        external interval added via add_ext_index(); the name must match exactly.

        If the interval is found, its start time is adjusted, and all subsequent
        intervals are adjusting accordingly, and true is returned.  If a matching
        interval is not found, nothing is changed and false is returned.
        """
    def get_interval_start_time(self, name: str) -> float:
        """Returns the actual start time, relative to the beginning of the interval,
        of the child interval with the given name, if found, or -1 if the interval
        is not found.
        """
    def get_interval_end_time(self, name: str) -> float:
        """Returns the actual end time, relative to the beginning of the interval, of
        the child interval with the given name, if found, or -1 if the interval is
        not found.
        """
    def get_num_defs(self) -> int:
        """Returns the number of interval and push/pop definitions that have been
        added to the meta interval.
        """
    def get_def_type(self, n: int) -> _CMetaInterval_DefType:
        """Returns the type of the nth interval definition that has been added."""
    def get_c_interval(self, n: int) -> CInterval:
        """Return the CInterval pointer associated with the nth interval definition.
        It is only valid to call this if get_def_type(n) returns DT_c_interval.
        """
    def get_ext_index(self, n: int) -> int:
        """Return the external interval index number associated with the nth interval
        definition.  It is only valid to call this if get_def_type(n) returns
        DT_ext_index.
        """
    def is_event_ready(self) -> bool:
        """Returns true if a recent call to priv_initialize(), priv_step(), or
        priv_finalize() has left some external intervals ready to play.  If this
        returns true, call get_event_index(), get_event_t(), and pop_event() to
        retrieve the relevant information.
        """
    def get_event_index(self) -> int:
        """If a previous call to is_event_ready() returned true, this returns the
        index number (added via add_event_index()) of the external interval that
        needs to be played.
        """
    def get_event_t(self) -> float:
        """If a previous call to is_event_ready() returned true, this returns the t
        value that should be fed to the given interval.
        """
    def get_event_type(self) -> _CInterval_EventType:
        """If a previous call to is_event_ready() returned true, this returns the type
        of the event (initialize, step, finalize, etc.) for the given interval.
        """
    def pop_event(self) -> None:
        """Acknowledges that the external interval on the top of the queue has been
        extracted, and is about to be serviced by the scripting language.  This
        prepares the interval so the next call to is_event_ready() will return
        information about the next external interval on the queue, if any.
        """
    def timeline(self, out: ostream) -> None:
        """Outputs a list of all events in the order in which they occur."""
    setPrecision = set_precision
    getPrecision = get_precision
    clearIntervals = clear_intervals
    pushLevel = push_level
    addCInterval = add_c_interval
    addExtIndex = add_ext_index
    popLevel = pop_level
    setIntervalStartTime = set_interval_start_time
    getIntervalStartTime = get_interval_start_time
    getIntervalEndTime = get_interval_end_time
    getNumDefs = get_num_defs
    getDefType = get_def_type
    getCInterval = get_c_interval
    getExtIndex = get_ext_index
    isEventReady = is_event_ready
    getEventIndex = get_event_index
    getEventT = get_event_t
    getEventType = get_event_type
    popEvent = pop_event

class HideInterval(CInterval):
    """An interval that calls NodePath::hide()."""

    @overload
    def __init__(self, __param0: HideInterval) -> None: ...
    @overload
    def __init__(self, node: NodePath, name: str = ...) -> None: ...

class LerpBlendType(TypedReferenceCount):
    def __call__(self, __param0: float) -> float: ...
    @staticmethod
    def get_class_type() -> TypeHandle:
        """now for typehandle stuff"""
    getClassType = get_class_type

class EaseInBlendType(LerpBlendType):
    def __init__(self) -> None: ...

class EaseOutBlendType(LerpBlendType):
    def __init__(self) -> None: ...

class EaseInOutBlendType(LerpBlendType):
    def __init__(self) -> None: ...

class NoBlendType(LerpBlendType):
    def __init__(self) -> None: ...

class ShowInterval(CInterval):
    """An interval that calls NodePath::show()."""

    @overload
    def __init__(self, __param0: ShowInterval) -> None: ...
    @overload
    def __init__(self, node: NodePath, name: str = ...) -> None: ...

class WaitInterval(CInterval):
    """This interval does absolutely nothing, and is mainly useful for marking
    time between other intervals within a sequence.
    """

    @overload
    def __init__(self, __param0: WaitInterval) -> None:
        """All Wait intervals have the same name.  No one really cares if their names
        are unique, after all.
        """
    @overload
    def __init__(self, duration: float) -> None: ...
