from typing import Any, ClassVar
from typing_extensions import Final, Literal, TypeAlias

from panda3d.core._dtoolutil import ostream
from panda3d.core._express import Namable, TypedReferenceCount

_ThreadPriority: TypeAlias = Literal[0, 1, 2, 3]

class Thread(TypedReferenceCount, Namable):
    """A thread; that is, a lightweight process.  This is an abstract base class;
    to use it, you must subclass from it and redefine thread_main().

    The thread itself will keep a reference count on the Thread object while it
    is running; when the thread returns from its root function, the Thread
    object will automatically be destructed if no other pointers are
    referencing it.
    """

    pipeline_stage: int
    @property
    def sync_name(self) -> str: ...
    @property
    def pstats_index(self) -> int: ...
    @property
    def python_index(self) -> int: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def main_thread(self) -> Thread: ...
    @property
    def external_thread(self) -> Thread: ...
    @property
    def current_thread(self) -> Thread: ...
    @property
    def current_pipeline_stage(self) -> int: ...
    @property
    def threading_supported(self) -> bool: ...
    @property
    def true_threads(self) -> bool: ...
    @property
    def simple_threads(self) -> bool: ...
    @property
    def started(self) -> bool: ...
    @property
    def joinable(self) -> bool: ...
    @property
    def current_task(self) -> TypedReferenceCount: ...
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    @staticmethod
    def bind_thread(name: str, sync_name: str) -> Thread:
        """Returns a new Panda Thread object associated with the current thread (which
        has been created externally). This can be used to bind a unique Panda
        Thread object with an external thread, such as a new Python thread.

        It is particularly useful to bind a Panda Thread object to an external
        thread for the purposes of PStats monitoring.  Without this call, each
        external thread will be assigned the same global ExternalThread object,
        which means they will all appear in the same PStats graph.

        It is the caller's responsibility to save the returned Thread pointer for
        the lifetime of the external thread.  It is an error for the Thread pointer
        to destruct while the external thread is still in the system.

        It is also an error to call this method from the main thread, or twice
        within a given thread, unless it is given the same name each time (in which
        case the same pointer will be returned each time).
        """
    def get_sync_name(self) -> str:
        """Returns the sync name of the thread.  This name collects threads into "sync
        groups", which are expected to run synchronously.  This is mainly used for
        the benefit of PStats; threads with the same sync name can be ticked all at
        once via the thread_tick() call.
        """
    def get_pstats_index(self) -> int:
        """Returns the PStats index associated with this thread, or -1 if no index has
        yet been associated with this thread.  This is used internally by the
        PStatClient; you should not need to call this directly.
        """
    def get_python_index(self) -> int:
        """Returns the Python index associated with this thread, or -1 if no index has
        yet been associated with this thread.  This is used internally by the
        direct.stdpy.thread module; you should not need to call this directly.
        """
    def get_unique_id(self) -> str:
        """Returns a string that is guaranteed to be unique to this thread, across all
        processes on the machine, during at least the lifetime of this process.
        """
    def get_pipeline_stage(self) -> int:
        """Returns the Pipeline stage number associated with this thread.  The default
        stage is 0 if no stage is specified otherwise.  See set_pipeline_stage().
        """
    def set_pipeline_stage(self, pipeline_stage: int) -> None:
        """Specifies the Pipeline stage number associated with this thread.  The
        default stage is 0 if no stage is specified otherwise.

        This must be a value in the range [0 .. pipeline->get_num_stages() - 1].
        It specifies the values that this thread observes for all pipelined data.
        Typically, an application thread will leave this at 0, but a render thread
        may set it to 1 or 2 (to operate on the previous frame's data, or the
        second previous frame's data).
        """
    def set_min_pipeline_stage(self, min_pipeline_stage: int) -> None:
        """Sets this thread's pipeline stage number to at least the indicated value,
        unless it is already larger.  See set_pipeline_stage().
        """
    @staticmethod
    def get_main_thread() -> Thread:
        """Returns a pointer to the "main" Thread object--this is the Thread that
        started the whole process.
        """
    @staticmethod
    def get_external_thread() -> Thread:
        """Returns a pointer to the "external" Thread object--this is a special Thread
        object that corresponds to any thread spawned outside of Panda's threading
        interface.  Note that multiple different threads may share this same
        pointer.
        """
    @staticmethod
    def get_current_thread() -> Thread:
        """Returns a pointer to the currently-executing Thread object.  If this is
        called from the main thread, this will return the same value as
        get_main_thread().

        This will always return some valid Thread pointer.  It will never return
        NULL, even if the current thread was spawned outside of Panda's threading
        system, although all non-Panda threads will return the exact same Thread
        pointer.
        """
    @staticmethod
    def get_current_pipeline_stage() -> int:
        """Returns the integer pipeline stage associated with the current thread.
        This is the same thing as get_current_thread()->get_pipeline_stage(), but
        it may be faster to retrieve in some contexts.
        """
    @staticmethod
    def is_threading_supported() -> bool:
        """Returns true if threading support has been compiled in and enabled, or
        false if no threading is available (and Thread::start() will always fail).
        """
    @staticmethod
    def is_true_threads() -> bool:
        """Returns true if a real threading library is available that supports actual
        OS-implemented threads, or false if the only threading we can provide is
        simulated user-space threading.
        """
    @staticmethod
    def is_simple_threads() -> bool:
        """Returns true if Panda is currently compiled for "simple threads", which is
        to say, cooperative context switching only, reducing the need for quite so
        many critical section protections.  This is not necessarily the opposite of
        "true threads", since one possible implementation of simple threads is via
        true threads with mutex protection to ensure only one runs at a time.
        """
    @staticmethod
    def sleep(seconds: float) -> None:
        """Suspends the current thread for at least the indicated amount of time.  It
        might be suspended for longer.
        """
    @staticmethod
    def force_yield() -> None:
        """Suspends the current thread for the rest of the current epoch."""
    @staticmethod
    def consider_yield() -> None:
        """Possibly suspends the current thread for the rest of the current epoch, if
        it has run for enough this epoch.  This is especially important for the
        simple thread implementation, which relies on cooperative yields like this.
        """
    def output_blocker(self, out: ostream) -> None:
        """Writes a description of the mutex or condition variable that this thread is
        blocked on.  Writes nothing if there is no blocker, or if we are not in
        DEBUG_THREADS mode.
        """
    @staticmethod
    def write_status(out: ostream) -> None: ...
    def is_started(self) -> bool:
        """Returns true if the thread has been started, false if it has not, or if
        join() has already been called.
        """
    def is_joinable(self) -> bool:
        """Returns the value of joinable that was passed to the start() call."""
    def start(self, priority: _ThreadPriority, joinable: bool) -> bool:
        """Starts the thread executing.  It is only valid to call this once.

        The thread will begin executing its thread_main() function, and will
        terminate when thread_main() returns.

        priority is intended as a hint to the relative importance of this thread.
        This may be ignored by the thread implementation.

        joinable should be set true if you intend to call join() to wait for the
        thread to terminate, or false if you don't care and you will never call
        join(). Note that the reference count on the Thread object is incremented
        while the thread itself is running, so if you just want to fire and forget
        a thread, you may pass joinable = false, and never store the Thread object.
        It will automatically destruct itself when it finishes.

        The return value is true if the thread is successfully started, false
        otherwise.
        """
    def join(self) -> None:
        """Blocks the calling process until the thread terminates.  If the thread has
        already terminated, this returns immediately.
        """
    def preempt(self) -> None:
        """Indicates that this thread should run as soon as possible, preemptying any
        other threads that may be scheduled to run.  This may not be implemented on
        every platform.
        """
    def get_current_task(self) -> TypedReferenceCount:
        """Returns the task currently executing on this thread (via the
        AsyncTaskManager), if any, or NULL if the thread is not currently servicing
        a task.
        """
    def set_python_index(self, index: int) -> None:
        """Stores a Python index to be associated with this thread.  This is used
        internally by the thread module; you should not need to call this directly.
        """
    @staticmethod
    def prepare_for_exit() -> None:
        """Should be called by the main thread just before exiting the program, this
        blocks until any remaining thread cleanup has finished.
        """
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToNamable = upcast_to_Namable
    bindThread = bind_thread
    getSyncName = get_sync_name
    getPstatsIndex = get_pstats_index
    getPythonIndex = get_python_index
    getUniqueId = get_unique_id
    getPipelineStage = get_pipeline_stage
    setPipelineStage = set_pipeline_stage
    setMinPipelineStage = set_min_pipeline_stage
    getMainThread = get_main_thread
    getExternalThread = get_external_thread
    getCurrentThread = get_current_thread
    getCurrentPipelineStage = get_current_pipeline_stage
    isThreadingSupported = is_threading_supported
    isTrueThreads = is_true_threads
    isSimpleThreads = is_simple_threads
    forceYield = force_yield
    considerYield = consider_yield
    outputBlocker = output_blocker
    writeStatus = write_status
    isStarted = is_started
    isJoinable = is_joinable
    getCurrentTask = get_current_task
    setPythonIndex = set_python_index
    prepareForExit = prepare_for_exit

class MutexDirect:
    """This class implements a standard mutex by making direct calls to the
    underlying implementation layer.  It doesn't perform any debugging
    operations.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def acquire(self) -> None:
        """Grabs the mutex if it is available.  If it is not available, blocks until
        it becomes available, then grabs it.  In either case, the function does not
        return until the mutex is held; you should then call unlock().

        This method is considered const so that you can lock and unlock const
        mutexes, mainly to allow thread-safe access to otherwise const data.

        Also see MutexHolder.
        """
    def try_acquire(self) -> bool:
        """Returns immediately, with a true value indicating the mutex has been
        acquired, and false indicating it has not.
        """
    def release(self) -> None:
        """Releases the mutex.  It is an error to call this if the mutex was not
        already locked.

        This method is considered const so that you can lock and unlock const
        mutexes, mainly to allow thread-safe access to otherwise const data.
        """
    def debug_is_locked(self) -> bool:
        """Returns true if the current thread has locked the Mutex, false otherwise.
        This method is only intended for use in debugging, hence the method name;
        in the MutexDirect case, it always returns true, since there's not a
        reliable way to determine this otherwise.
        """
    def set_name(self, name: str) -> None:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def clear_name(self) -> None:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def has_name(self) -> bool:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def get_name(self) -> str:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def output(self, out: ostream) -> None:
        """This method is declared virtual in MutexDebug, but non-virtual in
        MutexDirect.
        """
    tryAcquire = try_acquire
    debugIsLocked = debug_is_locked
    setName = set_name
    clearName = clear_name
    hasName = has_name
    getName = get_name

class Mutex(MutexDirect):
    def __init__(self, name: str = ...) -> None: ...

class ConditionVarDirect:
    """A condition variable, usually used to communicate information about
    changing state to a thread that is waiting for something to happen.  A
    condition variable can be used to "wake up" a thread when some arbitrary
    condition has changed.

    A condition variable is associated with a single mutex, and several
    condition variables may share the same mutex.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_mutex(self) -> MutexDirect:
        """Returns the mutex associated with this condition variable."""
    def wait(self, timeout: float = ...) -> None:
        """`(self)`:
        Waits on the condition.  The caller must already be holding the lock
        associated with the condition variable before calling this function.

        wait() will release the lock, then go to sleep until some other thread
        calls notify() on this condition variable.  At that time at least one
        thread waiting on the same ConditionVarDirect will grab the lock again, and
        then return from wait().

        It is possible that wait() will return even if no one has called notify().
        It is the responsibility of the calling process to verify the condition on
        return from wait, and possibly loop back to wait again if necessary.

        Note the semantics of a condition variable: the mutex must be held before
        wait() is called, and it will still be held when wait() returns.  However,
        it will be temporarily released during the wait() call itself.

        `(self, timeout: float)`:
        Waits on the condition, with a timeout.  The function will return when the
        condition variable is notified, or the timeout occurs.  There is no way to
        directly tell which happened, and it is possible that neither in fact
        happened (spurious wakeups are possible).

        See wait() with no parameters for more.
        """
    def notify(self) -> None:
        """Informs one of the other threads who are currently blocked on wait() that
        the relevant condition has changed.  If multiple threads are currently
        waiting, at least one of them will be woken up, although there is no way to
        predict which one.  It is possible that more than one thread will be woken
        up.

        The caller must be holding the mutex associated with the condition variable
        before making this call, which will not release the mutex.

        If no threads are waiting, this is a no-op: the notify event is lost.
        """
    def output(self, out: ostream) -> None:
        """This method is declared virtual in ConditionVarDebug, but non-virtual in
        ConditionVarDirect.
        """
    getMutex = get_mutex

class ConditionVar(ConditionVarDirect):
    def __init__(self, mutex: Mutex) -> None:
        """You must pass in a Mutex to the condition variable constructor.  This mutex
        may be shared by other condition variables, if desired.  It is the caller's
        responsibility to ensure the Mutex object does not destruct during the
        lifetime of the condition variable.
        """
    def get_mutex(self) -> Mutex:
        """Returns the mutex associated with this condition variable."""
    getMutex = get_mutex

class ConditionVarFullDirect:
    """A condition variable, usually used to communicate information about
    changing state to a thread that is waiting for something to happen.  A
    condition variable can be used to "wake up" a thread when some arbitrary
    condition has changed.

    A condition variable is associated with a single mutex, and several
    condition variables may share the same mutex.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_mutex(self) -> MutexDirect:
        """Returns the mutex associated with this condition variable."""
    def wait(self, timeout: float = ...) -> None:
        """`(self)`:
        Waits on the condition.  The caller must already be holding the lock
        associated with the condition variable before calling this function.

        wait() will release the lock, then go to sleep until some other thread
        calls notify() on this condition variable.  At that time at least one
        thread waiting on the same ConditionVarFullDirect will grab the lock again,
        and then return from wait().

        It is possible that wait() will return even if no one has called notify().
        It is the responsibility of the calling process to verify the condition on
        return from wait, and possibly loop back to wait again if necessary.

        Note the semantics of a condition variable: the mutex must be held before
        wait() is called, and it will still be held when wait() returns.  However,
        it will be temporarily released during the wait() call itself.

        `(self, timeout: float)`:
        Waits on the condition, with a timeout.  The function will return when the
        condition variable is notified, or the timeout occurs.  There is no way to
        directly tell which happened, and it is possible that neither in fact
        happened (spurious wakeups are possible).

        See wait() with no parameters for more.
        """
    def notify(self) -> None:
        """Informs one of the other threads who are currently blocked on wait() that
        the relevant condition has changed.  If multiple threads are currently
        waiting, at least one of them will be woken up, although there is no way to
        predict which one.  It is possible that more than one thread will be woken
        up.

        The caller must be holding the mutex associated with the condition variable
        before making this call, which will not release the mutex.

        If no threads are waiting, this is a no-op: the notify is lost.
        """
    def notify_all(self) -> None:
        """Informs all of the other threads who are currently blocked on wait() that
        the relevant condition has changed.

        The caller must be holding the mutex associated with the condition variable
        before making this call, which will not release the mutex.

        If no threads are waiting, this is a no-op: the notify event is lost.
        """
    def output(self, out: ostream) -> None:
        """This method is declared virtual in ConditionVarFullDebug, but non-virtual
        in ConditionVarFullDirect.
        """
    getMutex = get_mutex
    notifyAll = notify_all

class ConditionVarFull(ConditionVarFullDirect):
    def __init__(self, mutex: Mutex) -> None:
        """You must pass in a Mutex to the condition variable constructor.  This mutex
        may be shared by other condition variables, if desired.  It is the caller's
        responsibility to ensure the Mutex object does not destruct during the
        lifetime of the condition variable.
        """
    def get_mutex(self) -> Mutex:
        """Returns the mutex associated with this condition variable."""
    getMutex = get_mutex

class ReMutexDirect:
    """This class implements a standard reMutex by making direct calls to the
    underlying implementation layer.  It doesn't perform any debugging
    operations.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def acquire(self, current_thread: Thread = ...) -> None:
        """`(self)`:
        Grabs the reMutex if it is available.  If it is not available, blocks until
        it becomes available, then grabs it.  In either case, the function does not
        return until the reMutex is held; you should then call unlock().

        This method is considered const so that you can lock and unlock const
        reMutexes, mainly to allow thread-safe access to otherwise const data.

        Also see ReMutexHolder.

        `(self, current_thread: Thread)`:
        This variant on acquire() accepts the current thread as a parameter, if it
        is already known, as an optimization.
        """
    def try_acquire(self, current_thread: Thread = ...) -> bool:
        """Returns immediately, with a true value indicating the mutex has been
        acquired, and false indicating it has not.
        """
    def elevate_lock(self) -> None:
        """This method increments the lock count, assuming the calling thread already
        holds the lock.  After this call, release() will need to be called one
        additional time to release the lock.

        This method really performs the same function as acquire(), but it offers a
        potential (slight) performance benefit when the calling thread knows that
        it already holds the lock.  It is an error to call this when the calling
        thread does not hold the lock.
        """
    def release(self) -> None:
        """Releases the reMutex.  It is an error to call this if the reMutex was not
        already locked.

        This method is considered const so that you can lock and unlock const
        reMutexes, mainly to allow thread-safe access to otherwise const data.
        """
    def debug_is_locked(self) -> bool:
        """Returns true if the current thread has locked the ReMutex, false otherwise.
        This method is only intended for use in debugging, hence the method name;
        in the ReMutexDirect case, it always returns true, since there's not a
        reliable way to determine this otherwise.
        """
    def set_name(self, name: str) -> None:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def clear_name(self) -> None:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def has_name(self) -> bool:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def get_name(self) -> str:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def output(self, out: ostream) -> None:
        """This method is declared virtual in MutexDebug, but non-virtual in
        ReMutexDirect.
        """
    tryAcquire = try_acquire
    elevateLock = elevate_lock
    debugIsLocked = debug_is_locked
    setName = set_name
    clearName = clear_name
    hasName = has_name
    getName = get_name

class ReMutex(ReMutexDirect):
    def __init__(self, name: str = ...) -> None: ...

class ExternalThread(Thread):
    """The special "external thread" class.  There is one instance of these in the
    world, and it is returned by Thread::get_external_thread().
    """

class LightMutexDirect:
    """This class implements a lightweight Mutex by making direct calls to the
    underlying implementation layer.  It doesn't perform any debugging
    operations.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def acquire(self) -> None:
        """Grabs the lightMutex if it is available.  If it is not available, blocks
        until it becomes available, then grabs it.  In either case, the function
        does not return until the lightMutex is held; you should then call
        unlock().

        This method is considered const so that you can lock and unlock const
        lightMutexes, mainly to allow thread-safe access to otherwise const data.

        Also see LightMutexHolder.
        """
    def release(self) -> None:
        """Releases the lightMutex.  It is an error to call this if the lightMutex was
        not already locked.

        This method is considered const so that you can lock and unlock const
        lightMutexes, mainly to allow thread-safe access to otherwise const data.
        """
    def debug_is_locked(self) -> bool:
        """Returns true if the current thread has locked the LightMutex, false
        otherwise.  This method is only intended for use in debugging, hence the
        method name; in the LightMutexDirect case, it always returns true, since
        there's not a reliable way to determine this otherwise.
        """
    def set_name(self, name: str) -> None:
        """The lightMutex name is only defined when compiling in DEBUG_THREADS mode."""
    def clear_name(self) -> None:
        """The lightMutex name is only defined when compiling in DEBUG_THREADS mode."""
    def has_name(self) -> bool:
        """The lightMutex name is only defined when compiling in DEBUG_THREADS mode."""
    def get_name(self) -> str:
        """The lightMutex name is only defined when compiling in DEBUG_THREADS mode."""
    def output(self, out: ostream) -> None:
        """This method is declared virtual in LightMutexDebug, but non-virtual in
        LightMutexDirect.
        """
    debugIsLocked = debug_is_locked
    setName = set_name
    clearName = clear_name
    hasName = has_name
    getName = get_name

class LightMutex(LightMutexDirect):
    def __init__(self, name: str = ...) -> None: ...

class LightReMutexDirect:
    """This class implements a standard lightReMutex by making direct calls to the
    underlying implementation layer.  It doesn't perform any debugging
    operations.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def acquire(self, current_thread: Thread = ...) -> None:
        """`(self)`:
        Grabs the lightReMutex if it is available.  If it is not available, blocks
        until it becomes available, then grabs it.  In either case, the function
        does not return until the lightReMutex is held; you should then call
        unlock().

        This method is considered const so that you can lock and unlock const
        lightReMutexes, mainly to allow thread-safe access to otherwise const data.

        Also see LightReMutexHolder.

        `(self, current_thread: Thread)`:
        This variant on acquire() accepts the current thread as a parameter, if it
        is already known, as an optimization.
        """
    def elevate_lock(self) -> None:
        """This method increments the lock count, assuming the calling thread already
        holds the lock.  After this call, release() will need to be called one
        additional time to release the lock.

        This method really performs the same function as acquire(), but it offers a
        potential (slight) performance benefit when the calling thread knows that
        it already holds the lock.  It is an error to call this when the calling
        thread does not hold the lock.
        """
    def release(self) -> None:
        """Releases the lightReMutex.  It is an error to call this if the lightReMutex
        was not already locked.

        This method is considered const so that you can lock and unlock const
        lightReMutexes, mainly to allow thread-safe access to otherwise const data.
        """
    def debug_is_locked(self) -> bool:
        """Returns true if the current thread has locked the LightReMutex, false
        otherwise.  This method is only intended for use in debugging, hence the
        method name; in the LightReMutexDirect case, it always returns true, since
        there's not a reliable way to determine this otherwise.
        """
    def set_name(self, name: str) -> None:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def clear_name(self) -> None:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def has_name(self) -> bool:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def get_name(self) -> str:
        """The mutex name is only defined when compiling in DEBUG_THREADS mode."""
    def output(self, out: ostream) -> None:
        """This method is declared virtual in MutexDebug, but non-virtual in
        LightReMutexDirect.
        """
    elevateLock = elevate_lock
    debugIsLocked = debug_is_locked
    setName = set_name
    clearName = clear_name
    hasName = has_name
    getName = get_name

class LightReMutex(LightReMutexDirect):
    def __init__(self, name: str = ...) -> None: ...

class MainThread(Thread):
    """The special "main thread" class.  There is one instance of these in the
    world, and it is returned by Thread::get_main_thread().
    """

class Semaphore:
    """A classic semaphore synchronization primitive.

    A semaphore manages an internal counter which is decremented by each
    acquire() call and incremented by each release() call.  The counter can
    never go below zero; when acquire() finds that it is zero, it blocks,
    waiting until some other thread calls release().
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, initial_count: int = ...) -> None: ...
    def acquire(self) -> None:
        """Decrements the internal count.  If the count was already at zero, blocks
        until the count is nonzero, then decrements it.
        """
    def try_acquire(self) -> bool:
        """If the semaphore can be acquired without blocking, does so and returns
        true.  Otherwise, returns false.
        """
    def release(self) -> int:
        """Increments the semaphore's internal count.  This may wake up another thread
        blocked on acquire().

        Returns the count of the semaphore upon release.
        """
    def get_count(self) -> int:
        """Returns the current semaphore count.  Note that this call is not thread-
        safe (the count may change at any time).
        """
    def output(self, out: ostream) -> None: ...
    tryAcquire = try_acquire
    getCount = get_count

class PythonThread(Thread):
    """This class is exposed to Python to allow creation of a Panda thread from
    the Python level.  It will spawn a thread that executes an arbitrary Python
    functor.
    """

    args = ...
    def __init__(self, function, args, name: str, sync_name: str) -> None: ...
    def join(self): ...

TP_low: Final = 0
TPLow: Final = 0
TP_normal: Final = 1
TPNormal: Final = 1
TP_high: Final = 2
TPHigh: Final = 2
TP_urgent: Final = 3
TPUrgent: Final = 3
