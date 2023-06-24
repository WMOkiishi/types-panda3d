from collections.abc import Callable, Generator, Iterator, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias, final

from panda3d._typing import TaskCoroutine, TaskFunction
from panda3d.core._dtoolbase import TypedObject
from panda3d.core._dtoolutil import GlobPattern, ostream
from panda3d.core._express import Namable, TypedReferenceCount
from panda3d.core._putil import (
    ButtonHandle,
    ClockObject,
    ModifierButtons,
    ParamValueBase,
    PointerData,
    TypedWritableReferenceCount,
)

_AsyncTask_State: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
_ClockObject_Mode: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_ThreadPriority: TypeAlias = Literal[0, 1, 2, 3]
_ButtonEvent_Type: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]

class EventParameter:
    """An optional parameter associated with an event.  Each event may have zero
    or more of these.  Each parameter stores a pointer to a
    TypedWritableReferenceCount object, which of course could be pretty much
    anything.  To store a simple value like a double or a string, the
    EventParameter constructors transparently use the ParamValue template class
    from paramValue.h.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: EventParameter | None = ...) -> None:
        """`(self, ptr: TypedReferenceCount)`:
        Defines an EventParameter that stores a pointer to a TypedReferenceCount
        object.  Note that a TypedReferenceCount is not the same kind of pointer as
        a TypedWritableReferenceCount, hence we require both constructors.

        This accepts a const pointer, even though it stores (and eventually
        returns) a non-const pointer.  This is just the simplest way to allow both
        const and non-const pointers to be stored, but it does lose the constness.
        Be careful.

        `(self, ptr: TypedWritableReferenceCount)`:
        Defines an EventParameter that stores a pointer to any kind of
        TypedWritableReferenceCount object.  This is the most general constructor.

        This accepts a const pointer, even though it stores (and eventually
        returns) a non-const pointer.  This is just the simplest way to allow both
        const and non-const pointers to be stored, but it does lose the constness.
        Be careful.

        `(self, value: float)`:
        Defines an EventParameter that stores a floating-point value.

        `(self, value: int)`:
        Defines an EventParameter that stores an integer value.

        `(self, value: str)`:
        Defines an EventParameter that stores a string value.

        `(self, value: str)`:
        Defines an EventParameter that stores a wstring value.
        """
    @overload
    def __init__(self, ptr: TypedReferenceCount | TypedWritableReferenceCount) -> None: ...
    @overload
    def __init__(self, value: float | str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: EventParameter | TypedReferenceCount | TypedWritableReferenceCount | float | str | None) -> Self: ...
    def is_empty(self) -> bool:
        """These functions are conveniences to easily determine if the
        EventParameter is one of the predefined parameter types, and retrieve the
        corresponding value.  Of course, it is possible that the EventParameter
        is some user-defined type, and is none of these.
        """
    def is_int(self) -> bool:
        """Returns true if the EventParameter stores an integer value, false
        otherwise.
        """
    def get_int_value(self) -> int:
        """Retrieves the value stored in the EventParameter.  It is only valid to call
        this if is_int() has already returned true.
        """
    def is_double(self) -> bool:
        """Returns true if the EventParameter stores a double floating-point value,
        false otherwise.
        """
    def get_double_value(self) -> float:
        """Retrieves the value stored in the EventParameter.  It is only valid to call
        this if is_double() has already returned true.
        """
    def is_string(self) -> bool:
        """Returns true if the EventParameter stores a string value, false otherwise."""
    def get_string_value(self) -> str:
        """Retrieves the value stored in the EventParameter.  It is only valid to call
        this if is_string() has already returned true.
        """
    def is_wstring(self) -> bool:
        """Returns true if the EventParameter stores a wstring value, false otherwise."""
    def get_wstring_value(self) -> str:
        """Retrieves the value stored in the EventParameter.  It is only valid to call
        this if is_wstring() has already returned true.
        """
    def is_typed_ref_count(self) -> bool:
        """Returns true if the EventParameter stores a TypedReferenceCount pointer,
        false otherwise.  Note that a TypedReferenceCount is not exactly the same
        kind of pointer as a TypedWritableReferenceCount, hence the need for this
        separate call.
        """
    def get_typed_ref_count_value(self) -> TypedReferenceCount:
        """Retrieves the value stored in the EventParameter.  It is only valid to call
        this if is_typed_ref_count() has already returned true.
        """
    def get_ptr(self) -> TypedWritableReferenceCount:
        """Retrieves a pointer to the actual value stored in the parameter.  The
        TypeHandle of this pointer may be examined to determine the actual type of
        parameter it contains.  This is the only way to retrieve the value when it
        is not one of the above predefined types.
        """
    def output(self, out: ostream) -> None: ...
    isEmpty = is_empty
    isInt = is_int
    getIntValue = get_int_value
    isDouble = is_double
    getDoubleValue = get_double_value
    isString = is_string
    getStringValue = get_string_value
    isWstring = is_wstring
    getWstringValue = get_wstring_value
    isTypedRefCount = is_typed_ref_count
    getTypedRefCountValue = get_typed_ref_count_value
    getPtr = get_ptr

class AsyncFuture(TypedReferenceCount):
    """This class represents a thread-safe handle to a promised future result of
    an asynchronous operation, providing methods to query its status and result
    as well as register callbacks for this future's completion.

    An AsyncFuture can be awaited from within a coroutine or task.  It keeps
    track of tasks waiting for this future and automatically reactivates them
    upon this future's completion.

    A task itself is also a subclass of AsyncFuture.  Other subclasses are
    not generally necessary, except to override the function of `cancel()`.

    Until the future is done, it is "owned" by the resolver thread, though it's
    still legal for other threads to query its state.  When the resolver thread
    resolves this future using `set_result()`, or any thread calls `cancel()`,
    it instantly enters the "done" state, after which the result becomes a
    read-only field that all threads can access.

    When the future returns true for done(), a thread can use cancelled() to
    determine whether the future was cancelled or get_result() to access the
    result of the operation.  Not all operations define a meaningful result
    value, so some will always return nullptr.

    In Python, the `cancelled()`, `wait()` and `get_result()` methods are
    wrapped up into a single `result()` method which waits for the future to
    complete before either returning the result or throwing an exception if the
    future was cancelled.
    However, it is preferable to use the `await` keyword when running from a
    coroutine, which only suspends the current task and not the entire thread.

    This API aims to mirror and be compatible with Python's Future class.

    @since 1.10.0
    """

    done_event: str
    def __init__(self, __param0: AsyncFuture = ...) -> None:
        """Initializes the future in the pending state."""
    def __await__(self) -> Generator[Any, None, Any]: ...
    def __iter__(self) -> Iterator: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def done(self) -> bool:
        """Returns true if the future is done or has been cancelled.  It is always
        safe to call this.
        """
    def cancelled(self) -> bool:
        """Returns true if the future was cancelled.  It is always safe to call this."""
    def result(self, timeout=...): ...
    def cancel(self) -> bool:
        """Cancels the future.  Returns true if it was cancelled, or false if the
        future was already done.  Either way, done() will return true after this
        call returns.

        In the case of a task, this is equivalent to remove().
        """
    def set_done_event(self, done_event: str) -> None:
        """Sets the event name that will be triggered when the future finishes.  Will
        not be triggered if the future is cancelled, but it will be triggered for
        a coroutine task that exits with an exception.
        """
    def get_done_event(self) -> str:
        """Returns the event name that will be triggered when the future finishes.
        See set_done_event().
        """
    def add_done_callback(self, fn): ...
    @staticmethod
    def gather(*args: AsyncFuture) -> AsyncFuture: ...
    def output(self, out: ostream) -> None: ...
    def wait(self, timeout: float = ...) -> None:
        """`(self)`:
        Waits until the future is done.

        `(self, timeout: float)`:
        Waits until the future is done, or until the timeout is reached.
        """
    def set_result(self, __param0) -> None: ...
    setDoneEvent = set_done_event
    getDoneEvent = get_done_event
    addDoneCallback = add_done_callback
    setResult = set_result

class AsyncTask(AsyncFuture, Namable):  # type: ignore[misc]
    """This class represents a concrete task performed by an AsyncManager.
    Normally, you would subclass from this class, and override do_task(), to
    define the functionality you wish to have the task perform.
    """

    DS_done: Final = 0
    DSDone: Final = 0
    DS_cont: Final = 1
    DSCont: Final = 1
    DS_again: Final = 2
    DSAgain: Final = 2
    DS_pickup: Final = 3
    DSPickup: Final = 3
    DS_exit: Final = 4
    DSExit: Final = 4
    DS_pause: Final = 5
    DSPause: Final = 5
    DS_interrupt: Final = 6
    DSInterrupt: Final = 6
    DS_await: Final = 7
    DSAwait: Final = 7
    S_inactive: Final = 0
    SInactive: Final = 0
    S_active: Final = 1
    SActive: Final = 1
    S_servicing: Final = 2
    SServicing: Final = 2
    S_servicing_removed: Final = 3
    SServicingRemoved: Final = 3
    S_sleeping: Final = 4
    SSleeping: Final = 4
    S_active_nested: Final = 5
    SActiveNested: Final = 5
    S_awaiting: Final = 6
    SAwaiting: Final = 6
    name: str
    """The name of this task."""
    task_chain: str
    sort: int
    priority: int
    done_event: str
    """Returns the event name that will be triggered when the future finishes.
    See set_done_event().
    """
    @property
    def state(self) -> _AsyncTask_State: ...
    @property
    def alive(self) -> bool: ...
    @property
    def manager(self) -> AsyncTaskManager: ...
    @property
    def id(self) -> int:
        """This is a number guaranteed to be unique for each different AsyncTask
        object in the universe.
        """
    @property
    def dt(self) -> float: ...
    @property
    def max_dt(self) -> float: ...
    @property
    def average_dt(self) -> float: ...
    def __init__(self, __param0: AsyncTask) -> None: ...
    def upcast_to_AsyncFuture(self) -> AsyncFuture: ...
    def upcast_to_Namable(self) -> Namable: ...
    def get_state(self) -> _AsyncTask_State:
        """Returns the current state of the task."""
    def is_alive(self) -> bool:
        """Returns true if the task is currently active or sleeping on some task
        chain, meaning that it will be executed in its turn, or false if it is not
        active.  If the task has recently been removed while it is in the middle of
        execution, this will return false, because the task will not run again once
        it finishes.
        """
    def get_manager(self) -> AsyncTaskManager:
        """Returns the AsyncTaskManager that this task is active on.  This will be
        NULL if the state is S_inactive.
        """
    def remove(self) -> bool:
        """Removes the task from its active manager, if any, and makes the state
        S_inactive (or possible S_servicing_removed).  This is a no-op if the state
        is already S_inactive.
        """
    def set_delay(self, delay: float) -> None:
        """Specifies the amount of time, in seconds, by which this task will be
        delayed after it has been added to the AsyncTaskManager.  At least the
        specified amount of time (and possibly more) will elapse before the task
        begins.

        You may specify a delay of 0.0 to guarantee that the task will run in the
        next epoch following the one in which it is added.

        Setting this value after the task has already been added will not affect
        the task's wake time; it will only affect the task if it is re-added to the
        queue in the future, for instance if the task returns DS_again.  However,
        see recalc_wake_time() if you wish to apply the delay effect immediately.
        """
    def clear_delay(self) -> None:
        """Removes any delay specified for the task.  The next time the task is added
        to the queue, it will run immediately.  This does not affect the task's
        wake time if it has already been added to the queue.
        """
    def has_delay(self) -> bool:
        """Returns true if a delay has been set for this task via set_delay(), or
        false otherwise.
        """
    def get_delay(self) -> float:
        """Returns the delay value that has been set via set_delay, if any."""
    def get_wake_time(self) -> float:
        """If this task has been added to an AsyncTaskManager with a delay in effect,
        this returns the time at which the task is expected to awaken.  It has no
        meaning if the task has not yet been added to a queue, or if there was no
        delay in effect at the time the task was added.

        If the task's status is not S_sleeping, this returns 0.0.
        """
    def recalc_wake_time(self) -> None:
        """If the task is currently sleeping on a task chain, this resets its wake
        time to the current time + get_delay().  It is as if the task had suddenly
        returned DS_again.  The task will sleep for its current delay seconds
        before running again.  This method may therefore be used to make the task
        wake up sooner or later than it would have otherwise.

        If the task is not already sleeping, this method has no effect.
        """
    def get_start_time(self) -> float:
        """Returns the time at which the task was started, according to the task
        manager's clock.

        It is only valid to call this if the task's status is not S_inactive.
        """
    def get_elapsed_time(self) -> float:
        """Returns the amount of time that has elapsed since the task was started,
        according to the task manager's clock.

        It is only valid to call this if the task's status is not S_inactive.
        """
    def get_start_frame(self) -> int:
        """Returns the frame number at which the task was started, according to the
        task manager's clock.

        It is only valid to call this if the task's status is not S_inactive.
        """
    def get_elapsed_frames(self) -> int:
        """Returns the number of frames that have elapsed since the task was started,
        according to the task manager's clock.

        It is only valid to call this if the task's status is not S_inactive.
        """
    def clear_name(self) -> None:
        """Resets the task's name to empty."""
    def get_name_prefix(self) -> str:
        """Returns the initial part of the name, up to but not including any trailing
        digits following a hyphen or underscore.
        """
    def get_task_id(self) -> int:
        """Returns a number guaranteed to be unique for each different AsyncTask
        object in the universe.
        """
    def set_task_chain(self, chain_name: str) -> None:
        """Specifies the AsyncTaskChain on which this task will be running.  Each task
        chain runs tasks independently of the others.
        """
    def get_task_chain(self) -> str:
        """Returns the AsyncTaskChain on which this task will be running.  Each task
        chain runs tasks independently of the others.
        """
    def set_sort(self, sort: int) -> None:
        """Specifies a sort value for this task.  Within a given AsyncTaskManager, all
        of the tasks with a given sort value are guaranteed to be completed before
        any tasks with a higher sort value are begun.

        To put it another way, two tasks might execute in parallel with each other
        only if they both have the same sort value.  Tasks with a lower sort value
        are executed first.

        This is different from the priority, which makes no such exclusion
        guarantees.
        """
    def get_sort(self) -> int:
        """Returns the task's current sort value.  See set_sort()."""
    def set_priority(self, priority: int) -> None:
        """Specifies a priority value for this task.  In general, tasks with a higher
        priority value are executed before tasks with a lower priority value (but
        only for tasks with the same sort value).

        Unlike the sort value, tasks with different priorities may execute at the
        same time, if the AsyncTaskManager has more than one thread servicing
        tasks.

        Also see AsyncTaskChain::set_timeslice_priority(), which changes the
        meaning of this value.  In the default mode, when the timeslice_priority
        flag is false, all tasks always run once per epoch, regardless of their
        priority values (that is, the priority controls the order of the task
        execution only, not the number of times it runs).  On the other hand, if
        you set the timeslice_priority flag to true, then changing a task's
        priority has an effect on the number of times it runs.
        """
    def get_priority(self) -> int:
        """Returns the task's current priority value.  See set_priority()."""
    def set_done_event(self, done_event: str) -> None:
        """Sets the event name that will be triggered when the task finishes.  This
        should only be called before the task has been started, or after it has
        finished and before it is about to be restarted (i.e.  when get_state()
        returns S_inactive).
        """
    def get_dt(self) -> float:
        """Returns the amount of time elapsed during the task's previous run cycle, in
        seconds.
        """
    def get_max_dt(self) -> float:
        """Returns the maximum amount of time elapsed during any one of the task's
        previous run cycles, in seconds.
        """
    def get_average_dt(self) -> float:
        """Returns the average amount of time elapsed during each of the task's
        previous run cycles, in seconds.
        """
    upcastToAsyncFuture = upcast_to_AsyncFuture
    upcastToNamable = upcast_to_Namable
    getState = get_state
    isAlive = is_alive
    getManager = get_manager
    setDelay = set_delay
    clearDelay = clear_delay
    hasDelay = has_delay
    getDelay = get_delay
    getWakeTime = get_wake_time
    recalcWakeTime = recalc_wake_time
    getStartTime = get_start_time
    getElapsedTime = get_elapsed_time
    getStartFrame = get_start_frame
    getElapsedFrames = get_elapsed_frames
    clearName = clear_name
    getNamePrefix = get_name_prefix
    getTaskId = get_task_id
    setTaskChain = set_task_chain
    getTaskChain = get_task_chain
    setSort = set_sort
    getSort = get_sort
    setPriority = set_priority
    getPriority = get_priority
    setDoneEvent = set_done_event
    getDt = get_dt
    getMaxDt = get_max_dt
    getAverageDt = get_average_dt

class AsyncTaskManager(TypedReferenceCount, Namable):
    """A class to manage a loose queue of isolated tasks, which can be performed
    either synchronously (in the foreground thread) or asynchronously (by a
    background thread).

    The AsyncTaskManager is actually a collection of AsyncTaskChains, each of
    which maintains a list of tasks.  Each chain can be either foreground or
    background (it may run only in the main thread, or it may be serviced by
    one or more background threads). See AsyncTaskChain for more information.

    If you do not require background processing, it is perfectly acceptable to
    create only one AsyncTaskChain, which runs in the main thread.  This is a
    common configuration.
    """

    clock: ClockObject
    @property
    def tasks(self) -> AsyncTaskCollection: ...
    @property
    def active_tasks(self) -> AsyncTaskCollection: ...
    @property
    def sleeping_tasks(self) -> AsyncTaskCollection: ...
    @property
    def next_wake_time(self) -> float: ...
    def __init__(self, name: str) -> None: ...
    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def cleanup(self) -> None:
        """Stops all threads and messily empties the task list.  This is intended to
        be called on destruction only.
        """
    def set_clock(self, clock: ClockObject | _ClockObject_Mode) -> None:
        """Replaces the clock pointer used within the AsyncTaskManager.  This is used
        to control when tasks with a set_delay() specified will be scheduled.  It
        can also be ticked automatically each epoch, if set_tick_clock() is true.

        The default is the global clock pointer.
        """
    def get_clock(self) -> ClockObject:
        """Returns the clock pointer used within the AsyncTaskManager.  See
        set_clock().
        """
    def get_num_task_chains(self) -> int:
        """Returns the number of different task chains."""
    def get_task_chain(self, n: int) -> AsyncTaskChain:
        """Returns the nth task chain."""
    def make_task_chain(self, name: str) -> AsyncTaskChain:
        """Creates a new AsyncTaskChain of the indicated name and stores it within the
        AsyncTaskManager.  If a task chain with this name already exists, returns
        it instead.
        """
    def find_task_chain(self, name: str) -> AsyncTaskChain:
        """Searches a new AsyncTaskChain of the indicated name and returns it if it
        exists, or NULL otherwise.
        """
    def remove_task_chain(self, name: str) -> bool:
        """Removes the AsyncTaskChain of the indicated name.  If the chain still has
        tasks, this will block until all tasks are finished.

        Returns true if successful, or false if the chain did not exist.
        """
    def add(self, task: AsyncTask) -> None:
        """Adds the indicated task to the active queue.  It is an error if the task is
        already added to this or any other active queue.
        """
    def has_task(self, task: AsyncTask) -> bool:
        """Returns true if the indicated task has been added to this AsyncTaskManager,
        false otherwise.
        """
    def find_task(self, name: str) -> AsyncTask:
        """Returns the first task found with the indicated name, or NULL if there is
        no task with the indicated name.

        If there are multiple tasks with the same name, returns one of them
        arbitrarily.
        """
    def find_tasks(self, name: str) -> AsyncTaskCollection:
        """Returns the list of tasks found with the indicated name."""
    def find_tasks_matching(self, pattern: GlobPattern | str) -> AsyncTaskCollection:
        """Returns the list of tasks found whose name matches the indicated glob
        pattern, e.g.  "my_task_*".
        """
    @overload
    def remove(self, task: AsyncTask) -> bool:
        """`(self, task: AsyncTask)`:
        Removes the indicated task from the active queue.  Returns true if the task
        is successfully removed, or false if it wasn't there.

        `(self, tasks: AsyncTaskCollection)`:
        Removes all of the tasks in the AsyncTaskCollection.  Returns the number of
        tasks removed.
        """
    @overload
    def remove(self, tasks: AsyncTaskCollection) -> int: ...
    def wait_for_tasks(self) -> None:
        """Blocks until the task list is empty."""
    def stop_threads(self) -> None:
        """Stops any threads that are currently running.  If any tasks are still
        pending and have not yet been picked up by a thread, they will not be
        serviced unless poll() or start_threads() is later called.
        """
    def start_threads(self) -> None:
        """Starts any requested threads to service the tasks on the queue.  This is
        normally not necessary, since adding a task will start the threads
        automatically.
        """
    def get_num_tasks(self) -> int:
        """Returns the number of tasks that are currently active or sleeping within
        the task manager.
        """
    def get_tasks(self) -> AsyncTaskCollection:
        """Returns the set of tasks that are active or sleeping on the task manager,
        at the time of the call.
        """
    def get_active_tasks(self) -> AsyncTaskCollection:
        """Returns the set of tasks that are active (and not sleeping) on the task
        manager, at the time of the call.
        """
    def get_sleeping_tasks(self) -> AsyncTaskCollection:
        """Returns the set of tasks that are sleeping (and not active) on the task
        manager, at the time of the call.
        """
    def poll(self) -> None:
        """Runs through all the tasks in the task list, once, if the task manager is
        running in single-threaded mode (no threads available).  This method does
        nothing in threaded mode, so it may safely be called in either case.
        """
    def get_next_wake_time(self) -> float:
        """Returns the scheduled time (on the manager's clock) of the next sleeping
        task, on any task chain, to awaken.  Returns -1 if there are no sleeping
        tasks.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    @staticmethod
    def get_global_ptr() -> AsyncTaskManager:
        """Returns a pointer to the global AsyncTaskManager.  This is the
        AsyncTaskManager that most code should use for queueing tasks and suchlike.
        """
    def get_task_chains(self) -> tuple[AsyncTaskChain, ...]: ...
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToNamable = upcast_to_Namable
    setClock = set_clock
    getClock = get_clock
    getNumTaskChains = get_num_task_chains
    getTaskChain = get_task_chain
    makeTaskChain = make_task_chain
    findTaskChain = find_task_chain
    removeTaskChain = remove_task_chain
    hasTask = has_task
    findTask = find_task
    findTasks = find_tasks
    findTasksMatching = find_tasks_matching
    waitForTasks = wait_for_tasks
    stopThreads = stop_threads
    startThreads = start_threads
    getNumTasks = get_num_tasks
    getTasks = get_tasks
    getActiveTasks = get_active_tasks
    getSleepingTasks = get_sleeping_tasks
    getNextWakeTime = get_next_wake_time
    getGlobalPtr = get_global_ptr
    getTaskChains = get_task_chains

class AsyncTaskCollection:
    """A list of tasks, for instance as returned by some of the AsyncTaskManager
    query functions.  This also serves to define an AsyncTaskSequence.

    TODO: None of this is thread-safe yet.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: AsyncTaskCollection = ...) -> None: ...
    def __getitem__(self, index: int) -> AsyncTask:
        """Returns the nth AsyncTask in the collection.  This is the same as
        get_task(), but it may be a more convenient way to access it.
        """
    def __len__(self) -> int:
        """Returns the number of tasks in the collection.  This is the same thing as
        get_num_tasks().
        """
    def __iadd__(self, other: AsyncTaskCollection) -> Self: ...
    def __add__(self, other: AsyncTaskCollection) -> AsyncTaskCollection: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[AsyncTask]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def add_task(self, task: AsyncTask) -> None:
        """Adds a new AsyncTask to the collection."""
    @overload
    def remove_task(self, task: AsyncTask) -> bool:
        """`(self, task: AsyncTask)`:
        Removes the indicated AsyncTask from the collection.  Returns true if the
        task was removed, false if it was not a member of the collection.

        `(self, index: int)`:
        Removes the nth AsyncTask from the collection.
        """
    @overload
    def remove_task(self, index: int) -> None: ...
    def add_tasks_from(self, other: AsyncTaskCollection) -> None:
        """Adds all the AsyncTasks indicated in the other collection to this task.
        The other tasks are simply appended to the end of the tasks in this list;
        duplicates are not automatically removed.
        """
    def remove_tasks_from(self, other: AsyncTaskCollection) -> None:
        """Removes from this collection all of the AsyncTasks listed in the other
        collection.
        """
    def remove_duplicate_tasks(self) -> None:
        """Removes any duplicate entries of the same AsyncTasks on this collection.
        If a AsyncTask appears multiple times, the first appearance is retained;
        subsequent appearances are removed.
        """
    def has_task(self, task: AsyncTask) -> bool:
        """Returns true if the indicated AsyncTask appears in this collection, false
        otherwise.
        """
    def clear(self) -> None:
        """Removes all AsyncTasks from the collection."""
    def find_task(self, name: str) -> AsyncTask:
        """Returns the task in the collection with the indicated name, if any, or NULL
        if no task has that name.
        """
    def get_num_tasks(self) -> int:
        """Returns the number of AsyncTasks in the collection."""
    def get_task(self, index: int) -> AsyncTask:
        """Returns the nth AsyncTask in the collection."""
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the AsyncTaskCollection to the
        indicated output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the AsyncTaskCollection to the
        indicated output stream.
        """
    def get_tasks(self) -> tuple[AsyncTask, ...]: ...
    addTask = add_task
    removeTask = remove_task
    addTasksFrom = add_tasks_from
    removeTasksFrom = remove_tasks_from
    removeDuplicateTasks = remove_duplicate_tasks
    hasTask = has_task
    findTask = find_task
    getNumTasks = get_num_tasks
    getTask = get_task
    getTasks = get_tasks

class AsyncTaskChain(TypedReferenceCount, Namable):
    """The AsyncTaskChain is a subset of the AsyncTaskManager.  Each chain
    maintains a separate list of tasks, and will execute them with its own set
    of threads.  Each chain may thereby operate independently of the other
    chains.

    The AsyncTaskChain will spawn a specified number of threads (possibly 0) to
    serve the tasks.  If there are no threads, you must call poll() from time
    to time to serve the tasks in the main thread.  Normally this is done by
    calling AsyncTaskManager::poll().

    Each task will run exactly once each epoch.  Beyond that, the tasks' sort
    and priority values control the order in which they are run: tasks are run
    in increasing order by sort value, and within the same sort value, they are
    run roughly in decreasing order by priority value, with some exceptions for
    parallelism.  Tasks with different sort values are never run in parallel
    together, but tasks with different priority values might be (if there is
    more than one thread).
    """

    def upcast_to_TypedReferenceCount(self) -> TypedReferenceCount: ...
    def upcast_to_Namable(self) -> Namable: ...
    def set_tick_clock(self, tick_clock: bool) -> None:
        """Sets the tick_clock flag.  When this is true, get_clock()->tick() will be
        called automatically at each task epoch.  This is false by default.
        """
    def get_tick_clock(self) -> bool:
        """Returns the tick_clock flag.  See set_tick_clock()."""
    def set_num_threads(self, num_threads: int) -> None:
        """Changes the number of threads for this task chain.  This may require
        stopping the threads if they are already running.
        """
    def get_num_threads(self) -> int:
        """Returns the number of threads that will be servicing tasks for this chain.
        Also see get_num_running_threads().
        """
    def get_num_running_threads(self) -> int:
        """Returns the number of threads that have been created and are actively
        running.  This will return 0 before the threads have been started; it will
        also return 0 if thread support is not available.
        """
    def set_thread_priority(self, priority: _ThreadPriority) -> None:
        """Changes the priority associated with threads that serve this task chain.
        This may require stopping the threads if they are already running.
        """
    def get_thread_priority(self) -> _ThreadPriority:
        """Returns the priority associated with threads that serve this task chain."""
    def set_frame_budget(self, frame_budget: float) -> None:
        """Sets the maximum amount of time per frame the tasks on this chain are
        granted for execution.  If this is less than zero, there is no limit; if it
        is >= 0, it represents a maximum amount of time (in seconds) that will be
        used to execute tasks.  If this time is exceeded in any one frame, the task
        chain will stop executing tasks until the next frame, as defined by the
        TaskManager's clock.
        """
    def get_frame_budget(self) -> float:
        """Returns the maximum amount of time per frame the tasks on this chain are
        granted for execution.  See set_frame_budget().
        """
    def set_frame_sync(self, frame_sync: bool) -> None:
        """Sets the frame_sync flag.  When this flag is true, this task chain will be
        forced to sync with the TaskManager's clock.  It will run no faster than
        one epoch per clock frame.

        When this flag is false, the default, the task chain will finish all of its
        tasks and then immediately start from the first task again, regardless of
        the clock frame.  When it is true, the task chain will finish all of its
        tasks and then wait for the clock to tick to the next frame before resuming
        the first task.

        This only makes sense for threaded task chains.  Non-threaded task chains
        are automatically synchronous.
        """
    def get_frame_sync(self) -> bool:
        """Returns the frame_sync flag.  See set_frame_sync()."""
    def set_timeslice_priority(self, timeslice_priority: bool) -> None:
        """Sets the timeslice_priority flag.  This changes the interpretation of
        priority, and the number of times per epoch each task will run.

        When this flag is true, some tasks might not run in any given epoch.
        Instead, tasks with priority higher than 1 will be given precedence, in
        proportion to the amount of time they have already used.  This gives
        higher-priority tasks more runtime than lower-priority tasks.  Each task
        gets the amount of time proportional to its priority value, so a task with
        priority 100 will get five times as much processing time as a task with
        priority 20.  For these purposes, priority values less than 1 are deemed to
        be equal to 1.

        When this flag is false (the default), all tasks are run exactly once each
        epoch, round-robin style.  Priority is only used to determine which task
        runs first within tasks of the same sort value.
        """
    def get_timeslice_priority(self) -> bool:
        """Returns the timeslice_priority flag.  This changes the interpretation of
        priority, and the number of times per epoch each task will run.  See
        set_timeslice_priority().
        """
    def stop_threads(self) -> None:
        """Stops any threads that are currently running.  If any tasks are still
        pending and have not yet been picked up by a thread, they will not be
        serviced unless poll() or start_threads() is later called.
        """
    def start_threads(self) -> None:
        """Starts any requested threads to service the tasks on the queue.  This is
        normally not necessary, since adding a task will start the threads
        automatically.
        """
    def is_started(self) -> bool:
        """Returns true if the thread(s) have been started and are ready to service
        requests, false otherwise.  If this is false, the next call to add() or
        add_and_do() will automatically start the threads.
        """
    def has_task(self, task: AsyncTask) -> bool:
        """Returns true if the indicated task has been added to this AsyncTaskChain,
        false otherwise.
        """
    def wait_for_tasks(self) -> None:
        """Blocks until the task list is empty."""
    def get_num_tasks(self) -> int:
        """Returns the number of tasks that are currently active or sleeping within
        the task chain.
        """
    def get_tasks(self) -> AsyncTaskCollection:
        """Returns the set of tasks that are active or sleeping on the task chain, at
        the time of the call.
        """
    def get_active_tasks(self) -> AsyncTaskCollection:
        """Returns the set of tasks that are active (and not sleeping) on the task
        chain, at the time of the call.
        """
    def get_sleeping_tasks(self) -> AsyncTaskCollection:
        """Returns the set of tasks that are sleeping (and not active) on the task
        chain, at the time of the call.
        """
    def poll(self) -> None:
        """Runs through all the tasks in the task list, once, if the task chain is
        running in single-threaded mode (no threads available).  This method does
        nothing in threaded mode, so it may safely be called in either case.

        Normally, you would not call this function directly; instead, call
        AsyncTaskManager::poll(), which polls all of the task chains in sequence.
        """
    def get_next_wake_time(self) -> float:
        """Returns the scheduled time (on the manager's clock) of the next sleeping
        task, on any task chain, to awaken.  Returns -1 if there are no sleeping
        tasks.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    upcastToTypedReferenceCount = upcast_to_TypedReferenceCount
    upcastToNamable = upcast_to_Namable
    setTickClock = set_tick_clock
    getTickClock = get_tick_clock
    setNumThreads = set_num_threads
    getNumThreads = get_num_threads
    getNumRunningThreads = get_num_running_threads
    setThreadPriority = set_thread_priority
    getThreadPriority = get_thread_priority
    setFrameBudget = set_frame_budget
    getFrameBudget = get_frame_budget
    setFrameSync = set_frame_sync
    getFrameSync = get_frame_sync
    setTimeslicePriority = set_timeslice_priority
    getTimeslicePriority = get_timeslice_priority
    stopThreads = stop_threads
    startThreads = start_threads
    isStarted = is_started
    hasTask = has_task
    waitForTasks = wait_for_tasks
    getNumTasks = get_num_tasks
    getTasks = get_tasks
    getActiveTasks = get_active_tasks
    getSleepingTasks = get_sleeping_tasks
    getNextWakeTime = get_next_wake_time

class AsyncTaskPause(AsyncTask):
    """A special kind of task that simple returns DS_pause, to pause for a
    specified number of seconds and then finish.  It's intended to be used
    within an AsyncTaskSequence.
    """

    @overload
    def __init__(self, __param0: AsyncTaskPause) -> None: ...
    @overload
    def __init__(self, delay: float) -> None: ...

class AsyncTaskSequence(AsyncTask, AsyncTaskCollection):  # type: ignore[misc]
    """A special kind of task that serves as a list of tasks internally.  Each
    task on the list is executed in sequence, one per epoch.

    This is similar to a Sequence interval, though it has some slightly
    different abilities.  For instance, although you can't start at any
    arbitrary point in the sequence, you can construct a task sequence whose
    duration changes during playback.
    """

    @overload
    def __init__(self, __param0: AsyncTaskSequence) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def upcast_to_AsyncTask(self) -> AsyncTask: ...
    def upcast_to_AsyncTaskCollection(self) -> AsyncTaskCollection: ...
    def set_repeat_count(self, repeat_count: int) -> None:
        """Sets the repeat count of the sequence.  If the count is 0 or 1, the
        sequence will run exactly once.  If it is greater than 0, it will run that
        number of times.  If it is negative, it will run forever until it is
        explicitly removed.
        """
    def get_repeat_count(self) -> int:
        """Returns the repeat count of the sequence.  See set_repeat_count()."""
    def get_current_task_index(self) -> int:
        """Returns the index of the task within the sequence that is currently being
        executed (or that will be executed at the next epoch).
        """
    upcastToAsyncTask = upcast_to_AsyncTask
    upcastToAsyncTaskCollection = upcast_to_AsyncTaskCollection
    setRepeatCount = set_repeat_count
    getRepeatCount = get_repeat_count
    getCurrentTaskIndex = get_current_task_index

class ButtonEvent:
    """Records a button event of some kind.  This is either a keyboard or mouse
    button (or some other kind of button) changing state from up to down, or
    vice-versa, or it is a single "keystroke".

    A keystroke is different than a button event in that (a) it does not
    necessarily correspond to a physical button on a keyboard, but might be the
    result of a combination of buttons (e.g.  "A" is the result of shift +
    "a"); and (b) it does not manage separate "up" and "down" events, but is
    itself an instantaneous event.

    Normal up/down button events can be used to track the state of a particular
    button on the keyboard, while keystroke events are best used to monitor
    what a user is attempting to type.

    Button up/down events are defined across all the physical keys on the
    keyboard (and other buttons for which there is a corresponding ButtonHandle
    object), while keystroke events are defined across the entire Unicode
    character set.

    This API should not be considered stable and may change in a future version
    of Panda3D.
    """

    T_down: Final = 0
    TDown: Final = 0
    T_resume_down: Final = 1
    TResumeDown: Final = 1
    T_up: Final = 2
    TUp: Final = 2
    T_repeat: Final = 3
    TRepeat: Final = 3
    T_keystroke: Final = 4
    TKeystroke: Final = 4
    T_candidate: Final = 5
    TCandidate: Final = 5
    T_move: Final = 6
    TMove: Final = 6
    T_raw_down: Final = 7
    TRawDown: Final = 7
    T_raw_up: Final = 8
    TRawUp: Final = 8
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def button(self) -> ButtonHandle: ...
    @property
    def keycode(self) -> int: ...
    @property
    def type(self) -> _ButtonEvent_Type: ...
    @property
    def time(self) -> float: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: ButtonEvent) -> bool: ...

class ButtonEventList(ParamValueBase):
    """Records a set of button events that happened recently.  This class is
    usually used only in the data graph, to transmit the recent button presses,
    but it may be used anywhere a list of ButtonEvents is desired.
    """

    @property
    def events(self) -> Sequence[ButtonEvent]: ...
    def __init__(self, copy: ButtonEventList = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def add_event(self, event: ButtonEvent) -> None:
        """Adds a new event to the end of the list."""
    def get_num_events(self) -> int:
        """Returns the number of events in the list."""
    def get_event(self, n: int) -> ButtonEvent:
        """Returns the nth event in the list.  This does not remove the event from the
        list; the only way to remove events is to empty the whole list with
        clear().
        """
    def clear(self) -> None:
        """Empties all the events from the list."""
    def add_events(self, other: ButtonEventList) -> None:
        """Appends the events from the other list onto the end of this one."""
    def update_mods(self, mods: ModifierButtons) -> None:
        """Updates the indicated ModifierButtons object with all of the button up/down
        transitions indicated in the list.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    addEvent = add_event
    getNumEvents = get_num_events
    getEvent = get_event
    addEvents = add_events
    updateMods = update_mods

class Event(TypedReferenceCount):
    """A named event, possibly with parameters.  Anyone in any thread may throw an
    event at any time; there will be one process responsible for reading and
    dispacting on the events (but not necessarily immediately).

    This function use to inherit from Namable, but that makes it too expensive
    to get its name the Python code.  Now it just copies the Namable interface
    in.
    """

    name: str
    @property
    def parameters(self) -> Sequence[EventParameter]: ...
    def __init__(self, copy: Event | str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Event | str) -> Self: ...
    def set_name(self, name: str) -> None: ...
    def clear_name(self) -> None:
        """Resets the Event's name to empty."""
    def has_name(self) -> bool:
        """Returns true if the Event has a nonempty name set, false if the name is
        empty.
        """
    def get_name(self) -> str: ...
    def add_parameter(
        self, obj: EventParameter | TypedReferenceCount | TypedWritableReferenceCount | float | str | None
    ) -> None: ...
    def get_num_parameters(self) -> int: ...
    def get_parameter(self, n: int) -> EventParameter: ...
    def has_receiver(self) -> bool: ...
    def clear_receiver(self) -> None: ...
    def output(self, out: ostream) -> None: ...
    def get_parameters(self) -> tuple[EventParameter, ...]: ...
    setName = set_name
    clearName = clear_name
    hasName = has_name
    getName = get_name
    addParameter = add_parameter
    getNumParameters = get_num_parameters
    getParameter = get_parameter
    hasReceiver = has_receiver
    clearReceiver = clear_receiver
    getParameters = get_parameters

class EventHandler(TypedObject):
    """A class to monitor events from the C++ side of things.  It maintains a set
    of "hooks", function pointers assigned to event names, and calls the
    appropriate hooks when the matching event is detected.

    This class is not necessary when the hooks are detected and processed
    entirely by the scripting language, e.g.  via Scheme hooks or the messenger
    in Python.
    """

    def __init__(self, ev_queue: EventQueue) -> None: ...
    def get_future(self, event_name: str) -> AsyncFuture:
        """Returns a pending future that will be marked as done when the event is next
        fired.
        """
    def process_events(self) -> None:
        """The main processing loop of the EventHandler.  This function must be called
        periodically to service events.  Walks through each pending event and calls
        its assigned hooks.
        """
    def dispatch_event(self, event: Event | str) -> None:
        """Calls the hooks assigned to the indicated single event."""
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_event_handler(queue: EventQueue = ...) -> EventHandler:
        """Returns a pointer to the one global EventHandler object.  If the global
        object has not yet been created, this will create it.
        """
    getFuture = get_future
    processEvents = process_events
    dispatchEvent = dispatch_event
    getGlobalEventHandler = get_global_event_handler

class EventQueue:
    """A queue of pending events.  As events are thrown, they are added to this
    queue; eventually, they will be extracted out again by an EventHandler and
    processed.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def queue_event(self, event: Event | str) -> None: ...
    def clear(self) -> None:
        """Empties all events on the queue, throwing them on the floor."""
    def is_queue_empty(self) -> bool: ...
    def is_queue_full(self) -> Literal[False]:
        """@deprecated Always returns false; the queue can never be full."""
    def dequeue_event(self) -> Event: ...
    @staticmethod
    def get_global_event_queue() -> EventQueue:
        """Returns a pointer to the one global EventQueue object.  If the global
        object has not yet been created, this will create it.
        """
    queueEvent = queue_event
    isQueueEmpty = is_queue_empty
    isQueueFull = is_queue_full
    dequeueEvent = dequeue_event
    getGlobalEventQueue = get_global_event_queue

class PointerEventList(ParamValueBase):
    """Records a set of pointer events that happened recently.  This class is
    usually used only in the data graph, to transmit the recent pointer
    presses, but it may be used anywhere a list of PointerEvents is desired.
    """

    def __init__(self) -> None: ...
    def get_num_events(self) -> int:
        """Returns the number of events in the list."""
    def get_in_window(self, n: int) -> bool:
        """Get the in-window flag of the nth event."""
    def get_xpos(self, n: int) -> int:
        """Get the x-coordinate of the nth event."""
    def get_ypos(self, n: int) -> int:
        """Get the y-coordinate of the nth event."""
    def get_dx(self, n: int) -> float:
        """Get the x-delta of the nth event."""
    def get_dy(self, n: int) -> float:
        """Get the y-delta of the nth event."""
    def get_sequence(self, n: int) -> int:
        """Get the sequence number of the nth event."""
    def get_length(self, n: int) -> float:
        """Get the length of the nth event."""
    def get_direction(self, n: int) -> float:
        """Get the direction of the nth event."""
    def get_rotation(self, n: int) -> float:
        """Get the rotation of the nth event."""
    def get_time(self, n: int) -> float:
        """Get the timestamp of the nth event."""
    def clear(self) -> None:
        """Empties all the events from the list."""
    def pop_front(self) -> None:
        """Discards the first event on the list."""
    @overload
    def add_event(self, data: PointerData, seq: int, time: float) -> None:
        """`(self, data: PointerData, seq: int, time: float)`:
        Adds a new event from the given PointerData object.

        `(self, in_win: bool, xpos: int, ypos: int, xdelta: float, ydelta: float, seq: int, time: float)`:
        Adds a new event to the end of the list based on the given mouse movement.

        `(self, in_win: bool, xpos: int, ypos: int, seq: int, time: float)`:
        Adds a new event to the end of the list.  Automatically calculates the dx,
        dy, length, direction, and rotation for all but the first event.
        """
    @overload
    def add_event(self, in_win: bool, xpos: int, ypos: int, seq: int, time: float) -> None: ...
    @overload
    def add_event(self, in_win: bool, xpos: int, ypos: int, xdelta: float, ydelta: float, seq: int, time: float) -> None: ...
    def encircles(self, x: int, y: int) -> bool:
        """Returns true if the trail loops around the specified point."""
    def total_turns(self, sec: float) -> float:
        """returns the total angular deviation that the trail has made in the
        specified time period.  A small number means that the trail is moving in a
        relatively straight line, a large number means that the trail is zig-
        zagging or spinning.  The result is in degrees.
        """
    def match_pattern(self, pattern: str, rot: float, seglen: float) -> float:
        """This function is not implemented yet.  It is a work in progress.  The
        intent is as follows:

        Returns a nonzero value if the mouse movements match the specified pattern.
        The higher the value, the better the match.  The pattern is a sequence of
        compass directions (ie, "E", "NE", etc) separated by spaces.  If rot is
        nonzero, then the pattern is rotated counterclockwise by the specified
        amount before testing.  Seglen is the minimum length a mouse movement needs
        to be in order to be considered significant.
        """
    getNumEvents = get_num_events
    getInWindow = get_in_window
    getXpos = get_xpos
    getYpos = get_ypos
    getDx = get_dx
    getDy = get_dy
    getSequence = get_sequence
    getLength = get_length
    getDirection = get_direction
    getRotation = get_rotation
    getTime = get_time
    popFront = pop_front
    addEvent = add_event
    totalTurns = total_turns
    matchPattern = match_pattern

@final
class PythonTask(AsyncTask):
    """This class exists to allow association of a Python function or coroutine
    with the AsyncTaskManager.
    """

    delay_time: float
    """The delay value that has been set on this task, if any, or None."""
    delayTime: float
    """Alias of delay_time."""
    @property
    def time(self) -> float:
        """The amount of seconds that have elapsed since the task was started,
        according to the task manager's clock.
        """
    @property
    def wake_time(self) -> float:
        """If this task has been added to an AsyncTaskManager with a delay in
        effect, this contains the time at which the task is expected to awaken.
        It has no meaning of the task has not yet been added to a queue, or if
        there was no delay in effect at the time the task was added.  If the
        task's status is not S_sleeping, this contains 0.0.
        """
    @property
    def wakeTime(self) -> float:
        """Alias of wake_time."""
    @property
    def frame(self) -> int:
        """The number of frames that have elapsed since the task was started,
        according to the task manager's clock.
        """
    @overload
    def __init__(self, function: TaskCoroutine[Any] | TaskFunction | None = ..., name: str = ...) -> None: ...
    @overload
    def __init__(self, __param0: PythonTask) -> None: ...
    def set_function(self, function: TaskFunction | None) -> None: ...
    def get_function(self) -> TaskFunction | None:
        """Returns the function that is called when the task runs."""
    def set_args(self, args: Sequence[Any] | None, append_task: bool) -> None: ...
    def get_args(self) -> tuple[Any, ...]: ...
    def set_upon_death(self, upon_death: Callable[[], object] | None) -> None: ...
    def get_upon_death(self) -> Callable[[], object] | None:
        """Returns the function that is called when the task finishes."""
    def set_owner(self, owner) -> None: ...
    def get_owner(self):
        """Returns the "owner" object.  See set_owner()."""
    def set_result(self, result) -> None:
        """Sets the "result" of this task.  This is the value returned from an "await"
        expression on this task.
        This can only be called while the task is still alive.
        """
    setFunction = set_function
    getFunction = get_function
    setArgs = set_args
    getArgs = get_args
    setUponDeath = set_upon_death
    getUponDeath = get_upon_death
    setOwner = set_owner
    getOwner = get_owner
    setResult = set_result
