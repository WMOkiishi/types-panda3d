from collections.abc import Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d.core._dtoolutil import ostream
from panda3d.core._express import PStatCollectorForwardBase
from panda3d.core._pipeline import Thread

class PStatClient:
    DtoolClassDict: ClassVar[dict[str, Any]]
    client_name: str
    max_rate: float
    @property
    def collectors(self) -> Sequence[PStatCollector]: ...
    @property
    def threads(self) -> Sequence[PStatThread]: ...
    @property
    def main_thread(self) -> PStatThread: ...
    @property
    def current_thread(self) -> PStatThread: ...
    @property
    def real_time(self) -> float: ...
    def set_client_name(self, name: str) -> None:
        """Sets the name of the client.  This is reported to the PStatsServer, and
        will presumably be written in the title bar or something.
        """
    def get_client_name(self) -> str:
        """Retrieves the name of the client as set."""
    def set_max_rate(self, rate: float) -> None:
        """Controls the number of packets that will be sent to the server.  Normally,
        one packet is sent per frame, but this can flood the server with more
        packets than it can handle if the frame rate is especially good (e.g.  if
        nothing is onscreen at the moment).  Set this parameter to a reasonable
        number to prevent this from happening.

        This number specifies the maximum number of packets that will be sent to
        the server per second, per thread.
        """
    def get_max_rate(self) -> float:
        """Returns the maximum number of packets that will be sent to the server per
        second, per thread.  See set_max_rate().
        """
    def get_num_collectors(self) -> int:
        """Returns the total number of collectors the Client knows about."""
    def get_collector(self, index: int) -> PStatCollector:
        """Returns the nth collector."""
    def get_collector_name(self, index: int) -> str:
        """Returns the name of the indicated collector."""
    def get_collector_fullname(self, index: int) -> str:
        """Returns the "full name" of the indicated collector.  This will be the
        concatenation of all of the collector's parents' names (except Frame) and
        the collector's own name.
        """
    def get_num_threads(self) -> int:
        """Returns the total number of threads the Client knows about."""
    def get_thread(self, index: int) -> PStatThread:
        """Returns the nth thread."""
    def get_thread_name(self, index: int) -> str:
        """Returns the name of the indicated thread."""
    def get_thread_sync_name(self, index: int) -> str:
        """Returns the sync_name of the indicated thread."""
    def get_thread_object(self, index: int) -> Thread:
        """Returns the Panda Thread object associated with the indicated PStatThread."""
    def get_main_thread(self) -> PStatThread:
        """Returns a handle to the client's Main thread.  This is the thread that
        started the application.
        """
    def get_current_thread(self) -> PStatThread:
        """Returns a handle to the currently-executing thread.  This is the thread
        that PStatCollectors will be counted in if they do not specify otherwise.
        """
    def get_real_time(self) -> float:
        """Returns the time according to to the PStatClient's clock object.  It keeps
        its own clock, instead of using the global clock object, so the stats won't
        get mucked up if you put the global clock in non-real-time mode or
        something.
        """
    @staticmethod
    def connect(hostname: str = ..., port: int = ...) -> bool:
        """Attempts to establish a connection to the indicated PStatServer.  Returns
        true if successful, false on failure.
        """
    @staticmethod
    def disconnect() -> None:
        """Closes the connection previously established."""
    @staticmethod
    def is_connected() -> bool:
        """Returns true if the client believes it is connected to a working
        PStatServer, false otherwise.
        """
    @staticmethod
    def resume_after_pause() -> None:
        """Resumes the PStatClient after the simulation has been paused for a while.
        This allows the stats to continue exactly where it left off, instead of
        leaving a big gap that would represent a chug.
        """
    @staticmethod
    def main_tick() -> None:
        """A convenience function to call new_frame() on the global PStatClient's main
        thread, and any other threads with a sync_name of "Main".
        """
    @staticmethod
    def thread_tick(sync_name: str) -> None:
        """A convenience function to call new_frame() on any threads with the
        indicated sync_name
        """
    def client_main_tick(self) -> None:
        """A convenience function to call new_frame() on the given PStatClient's main
        thread, and any other threads with a sync_name of "Main".
        """
    def client_thread_tick(self, sync_name: str) -> None:
        """A convenience function to call new_frame() on all of the threads with the
        indicated sync name.
        """
    def client_connect(self, hostname: str, port: int) -> bool:
        """The nonstatic implementation of connect()."""
    def client_disconnect(self) -> None:
        """The nonstatic implementation of disconnect()."""
    def client_is_connected(self) -> bool:
        """The nonstatic implementation of is_connected()."""
    def client_resume_after_pause(self) -> None:
        """Resumes the PStatClient after the simulation has been paused for a while.
        This allows the stats to continue exactly where it left off, instead of
        leaving a big gap that would represent a chug.
        """
    @staticmethod
    def get_global_pstats() -> PStatClient:
        """Returns a pointer to the global PStatClient object.  It's legal to declare
        your own PStatClient locally, but it's also convenient to have a global one
        that everyone can register with.  This is the global one.
        """
    def get_collectors(self) -> tuple[PStatCollector, ...]: ...
    def get_threads(self) -> tuple[PStatThread, ...]: ...
    setClientName = set_client_name
    getClientName = get_client_name
    setMaxRate = set_max_rate
    getMaxRate = get_max_rate
    getNumCollectors = get_num_collectors
    getCollector = get_collector
    getCollectorName = get_collector_name
    getCollectorFullname = get_collector_fullname
    getNumThreads = get_num_threads
    getThread = get_thread
    getThreadName = get_thread_name
    getThreadSyncName = get_thread_sync_name
    getThreadObject = get_thread_object
    getMainThread = get_main_thread
    getCurrentThread = get_current_thread
    getRealTime = get_real_time
    isConnected = is_connected
    resumeAfterPause = resume_after_pause
    mainTick = main_tick
    threadTick = thread_tick
    clientMainTick = client_main_tick
    clientThreadTick = client_thread_tick
    clientConnect = client_connect
    clientDisconnect = client_disconnect
    clientIsConnected = client_is_connected
    clientResumeAfterPause = client_resume_after_pause
    getGlobalPstats = get_global_pstats
    getCollectors = get_collectors
    getThreads = get_threads

class PStatCollector:
    """A lightweight class that represents a single element that may be timed
    and/or counted via stats.

    Collectors can be used to measure two different kinds of values: elapsed
    time, and "other".

    To measure elapsed time, call start() and stop() as appropriate to bracket
    the section of code you want to time (or use a PStatTimer to do this
    automatically).

    To measure anything else, call set_level() and/or add_level() to set the
    "level" value associated with this collector.  The meaning of the value set
    for the "level" is entirely up to the user; it may represent the number of
    triangles rendered or the kilobytes of texture memory consumed, for
    instance.  The level set will remain fixed across multiple frames until it
    is reset via another set_level() or adjusted via a call to add_level().  It
    may also be completely removed via clear_level().
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: PStatCollector) -> None:
        """`(self, parent: PStatCollector, name: str)`:
        Creates a new PStatCollector, ready to start accumulating data.  The name
        of the collector uniquely identifies it among the other collectors; if two
        collectors share the same name then they are really the same collector.

        The parent is the collector that conceptually includes all of the time
        measured for this collector.  For instance, a particular character's
        animation time is owned by the "Animation" collector, which is in turn
        owned by the "Frame" collector.  It is not strictly necessary that all of
        the time spent in a particular collector is completely nested within time
        spent in its parent's collector.  If parent is the empty string, the
        collector is owned by "Frame".

        This constructor does not take a client pointer; it always creates the new
        collector on the same client as its parent.

        `(self, name: str, client: PStatClient = ...)`:
        Creates a new PStatCollector, ready to start accumulating data.  The name
        of the collector uniquely identifies it among the other collectors; if two
        collectors share the same name then they are really the same collector.

        The name may also be a compound name, something like "Cull:Sort", which
        indicates that this is a collector named "Sort", a child of the collector
        named "Cull". The parent may also be named explicitly by reference in the
        other flavor of the constructor; see further comments on this for that
        constructor.

        If the client pointer is non-null, it specifies a particular client to
        register the collector with; otherwise, the global client is used.
        """
    @overload
    def __init__(self, name: str, client: PStatClient = ...) -> None: ...
    @overload
    def __init__(self, parent: PStatCollector, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def is_valid(self) -> bool:
        """Returns true if collector is valid and may be used, or false if it was
        constructed with the default constructor (in which case any attempt to use
        it will crash).
        """
    def get_name(self) -> str:
        """Returns the local name of this collector.  This is the rightmost part of
        the fullname, after the rightmost colon.
        """
    def get_fullname(self) -> str:
        """Returns the full name of this collector.  This includes the names of all
        the collector's parents, concatenated together with colons.
        """
    def output(self, out: ostream) -> None: ...
    def is_active(self, thread: PStatThread | Thread = ...) -> bool:
        """`(self)`:
        Returns true if this particular collector is active on the default thread,
        and we are currently transmitting PStats data.

        `(self, thread: PStatThread)`:
        Returns true if this particular collector is active on the indicated
        thread, and we are currently transmitting PStats data.
        """
    def is_started(self, thread: PStatThread | Thread = ...) -> bool:
        """`(self)`:
        Returns true if this particular collector has been started on the default
        thread, or false otherwise.

        `(self, thread: PStatThread)`:
        Returns true if this particular collector has been started on the indicated
        thread, or false otherwise.
        """
    @overload
    def start(self, thread: PStatThread | Thread = ...) -> None:
        """`(self)`:
        Starts this particular timer ticking.  This should be called before the
        code you want to measure.

        `(self, thread: PStatThread)`:
        Starts this timer ticking within a particular thread.

        `(self, thread: PStatThread, as_of: float)`:
        Marks that the timer should have been started as of the indicated time.
        This must be a time based on the PStatClient's clock (see
        PStatClient::get_clock()), and care should be taken that all such calls
        exhibit a monotonically increasing series of time values.
        """
    @overload
    def start(self, thread: PStatThread | Thread, as_of: float) -> None: ...
    @overload
    def stop(self, thread: PStatThread | Thread = ...) -> None:
        """`(self)`:
        Stops this timer.  This should be called after the code you want to
        measure.

        `(self, thread: PStatThread)`:
        Stops this timer within a particular thread.

        `(self, thread: PStatThread, as_of: float)`:
        Marks that the timer should have been stopped as of the indicated time.
        This must be a time based on the PStatClient's clock (see
        PStatClient::get_clock()), and care should be taken that all such calls
        exhibit a monotonically increasing series of time values.
        """
    @overload
    def stop(self, thread: PStatThread | Thread, as_of: float) -> None: ...
    def clear_level(self, thread: PStatThread | Thread = ...) -> None:
        """`(self)`:
        Removes the level setting associated with this collector for the main
        thread.  The collector will no longer show up on any level graphs in the
        main thread.  This implicitly calls flush_level().

        `(self, thread: PStatThread)`:
        Removes the level setting associated with this collector for the indicated
        thread.  The collector will no longer show up on any level graphs in this
        thread.
        """
    @overload
    def set_level(self, level: float) -> None:
        """`(self, thread: PStatThread, level: float)`:
        Sets the level setting associated with this collector for the indicated
        thread to the indicated value.

        `(self, level: float)`:
        Sets the level setting associated with this collector for the main thread
        to the indicated value.  This implicitly calls flush_level().
        """
    @overload
    def set_level(self, thread: PStatThread | Thread, level: float) -> None: ...
    @overload
    def add_level(self, increment: float) -> None:
        """`(self, thread: PStatThread, increment: float)`:
        Adds the indicated increment (which may be negative) to the level setting
        associated with this collector for the indicated thread.  If the collector
        did not already have a level setting for this thread, it is initialized to
        0.

        `(self, increment: float)`:
        Adds the indicated increment (which may be negative) to the level setting
        associated with this collector for the main thread.  If the collector did
        not already have a level setting for the main thread, it is initialized to
        0.

        As an optimization, the data is not immediately set to the PStatClient.  It
        will be sent the next time flush_level() is called.
        """
    @overload
    def add_level(self, thread: PStatThread | Thread, increment: float) -> None: ...
    @overload
    def sub_level(self, decrement: float) -> None:
        """`(self, thread: PStatThread, decrement: float)`:
        Subtracts the indicated decrement (which may be negative) to the level
        setting associated with this collector for the indicated thread.  If the
        collector did not already have a level setting for this thread, it is
        initialized to 0.

        `(self, decrement: float)`:
        Subtracts the indicated decrement (which may be negative) to the level
        setting associated with this collector for the main thread.  If the
        collector did not already have a level setting for the main thread, it is
        initialized to 0.

        As an optimization, the data is not immediately set to the PStatClient.  It
        will be sent the next time flush_level() is called.
        """
    @overload
    def sub_level(self, thread: PStatThread | Thread, decrement: float) -> None: ...
    def add_level_now(self, increment: float) -> None:
        """Calls add_level() and immediately calls flush_level()."""
    def sub_level_now(self, decrement: float) -> None:
        """Calls sub_level() and immediately calls flush_level()."""
    def flush_level(self) -> None:
        """Updates the PStatClient with the recent results from add_level() and
        sub_level().
        """
    def get_level(self, thread: PStatThread | Thread = ...) -> float:
        """`(self)`:
        Returns the current level value of the given collector in the main thread.
        This implicitly calls flush_level().

        `(self, thread: PStatThread)`:
        Returns the current level value of the given collector.
        """
    def clear_thread_level(self) -> None:
        """Removes the level setting associated with this collector for the current
        thread.  The collector will no longer show up on any level graphs in the
        current thread.
        """
    def set_thread_level(self, level: float) -> None:
        """Sets the level setting associated with this collector for the current
        thread to the indicated value.
        """
    def add_thread_level(self, increment: float) -> None:
        """Adds the indicated increment (which may be negative) to the level setting
        associated with this collector for the current thread.  If the collector
        did not already have a level setting for the current thread, it is
        initialized to 0.
        """
    def sub_thread_level(self, decrement: float) -> None:
        """Subtracts the indicated decrement (which may be negative) to the level
        setting associated with this collector for the current thread.  If the
        collector did not already have a level setting for the current thread, it
        is initialized to 0.
        """
    def get_thread_level(self) -> float:
        """Returns the current level value of the given collector in the current
        thread.
        """
    def get_index(self) -> int:
        """Returns the index number of this particular collector within the
        PStatClient.
        """
    isValid = is_valid
    getName = get_name
    getFullname = get_fullname
    isActive = is_active
    isStarted = is_started
    clearLevel = clear_level
    setLevel = set_level
    addLevel = add_level
    subLevel = sub_level
    addLevelNow = add_level_now
    subLevelNow = sub_level_now
    flushLevel = flush_level
    getLevel = get_level
    clearThreadLevel = clear_thread_level
    setThreadLevel = set_thread_level
    addThreadLevel = add_thread_level
    subThreadLevel = sub_thread_level
    getThreadLevel = get_thread_level
    getIndex = get_index

class PStatThread:
    """A lightweight class that represents a single thread of execution to PStats.
    It corresponds one-to-one with Panda's Thread instance.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def thread(self) -> Thread: ...
    @property
    def index(self) -> int: ...
    @overload
    def __init__(self, copy: PStatThread) -> None:
        """`(self, client: PStatClient, index: int)`:
        Normally, this constructor is called only from PStatClient.  Use one of the
        constructors below to create your own Thread.

        `(self, thread: Thread, client: PStatClient = ...)`:
        Creates a new named thread.  This will be used to unify tasks that share a
        common thread, and differentiate tasks that occur in different threads.
        """
    @overload
    def __init__(self, thread: Thread, client: PStatClient = ...) -> None: ...
    @overload
    def __init__(self, client: PStatClient, index: int) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: PStatThread | Thread) -> Self: ...
    def new_frame(self) -> None:
        """This must be called at the start of every "frame", whatever a frame may be
        deemed to be, to accumulate all the stats that have collected so far for
        the thread and ship them off to the server.

        Calling PStatClient::thread_tick() will automatically call this for any
        threads with the indicated sync name.
        """
    def get_thread(self) -> Thread:
        """Returns the Panda Thread object associated with this particular
        PStatThread.
        """
    def get_index(self) -> int:
        """Returns the index number of this particular thread within the PStatClient."""
    newFrame = new_frame
    getThread = get_thread
    getIndex = get_index

class PStatCollectorForward(PStatCollectorForwardBase):
    """This class serves as a cheap forward reference to a PStatCollector, so that
    classes that are defined before the pstats module may access the
    PStatCollector.
    """

    def __init__(self, col: PStatCollector) -> None: ...
