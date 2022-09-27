__all__ = [
    'Task',
    'TaskManager',
    'again',
    'cont',
    'done',
    'exit',
    'loop',
    'pause',
    'pickup',
    'sequence',
]

from collections.abc import Callable, Sequence
from typing import Any, ClassVar, NoReturn, overload
from typing_extensions import Final, Literal, Protocol

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from direct.fsm.StatePush import StateVar
from direct.showbase.ProfileSession import ProfileSession
from direct.tkpanels.TaskManagerPanel import TaskManagerPanel
from panda3d.core import (
    AsyncFuture,
    AsyncTask,
    AsyncTaskManager,
    AsyncTaskPause,
    AsyncTaskPause as pause,
    AsyncTaskSequence,
    ClockObject,
    ConfigVariableBool,
    GlobPattern,
    PythonTask,
)

def print_exc_plus() -> None: ...

done: Final[Literal[0]]
cont: Final[Literal[1]]
again: Final[Literal[2]]
pickup: Final[Literal[3]]
exit: Final[Literal[4]]

class Task(PythonTask):  # type: ignore[misc]
    cont: ClassVar[Literal[1]]
    again: ClassVar[Literal[2]]
    pickup: ClassVar[Literal[3]]
    exit: ClassVar[Literal[4]]
    pause: type[AsyncTaskPause]
    @staticmethod
    def sequence(*taskList: AsyncTask) -> AsyncTaskSequence: ...
    @staticmethod
    def loop(*taskList: AsyncTask) -> AsyncTaskSequence: ...

def gather(*taskList: AsyncFuture) -> AsyncFuture: ...
def sequence(*taskList: AsyncTask) -> AsyncTaskSequence: ...
def loop(*taskList: AsyncTask) -> AsyncTaskSequence: ...

class _TaskOwner(Protocol):
    def _addTask(self, task: Task) -> None: ...
    def _clearTask(self, task: Task) -> None: ...

class TaskManager:
    notify: ClassVar[Notifier]
    taskTimerVerbose: ClassVar[ConfigVariableBool]
    extendedExceptions: ClassVar[ConfigVariableBool]
    pStatsTasks: ClassVar[ConfigVariableBool]
    MaxEpochSpeed: ClassVar[float]
    mgr: AsyncTaskManager
    globalClock: ClockObject
    stepping: bool
    running: bool
    destroyed: bool
    fKeyboardInterrupt: bool
    interruptCount: int
    clock: ClockObject
    def __init__(self) -> None: ...
    def finalInit(self) -> None: ...
    def destroy(self) -> None: ...
    def setClock(self, clockObject: ClockObject) -> None: ...
    def invokeDefaultHandler(self, signalNumber: Unused, stackFrame: Unused) -> NoReturn: ...
    def keyboardInterruptHandler(self, signalNumber: Unused, stackFrame: Unused) -> None: ...
    def getCurrentTask(self) -> Task | None: ...
    def hasTaskChain(self, chainName: str) -> bool: ...
    def setupTaskChain(
        self,
        chainName: str,
        numThreads: int | None = None,
        tickClock: bool | None = None,
        threadPriority: Literal[0, 1, 2, 3, None] = None,
        frameBudget: float | None = None,
        frameSync: bool | None = None,
        timeslicePriority: bool | None = None,
    ) -> None: ...
    def hasTaskNamed(self, taskName: str) -> bool: ...
    def getTasksNamed(self, taskName: str) -> list[Task]: ...
    def getTasksMatching(self, taskPattern: str | GlobPattern) -> list[Task]: ...
    def getAllTasks(self) -> list[Task]: ...
    def getTasks(self) -> list[Task]: ...
    def getDoLaters(self) -> list[Task]: ...
    @overload
    def do_method_later(
        self,
        delayTime: float,
        funcOrTask: AsyncTask,
        name: str | None,
        extraArgs: Sequence[Any] | None = None,
        sort: int | None = None,
        priority: int | None = None,
        taskChain: str | None = None,
        uponDeath: Callable[..., object] | None = None,
        appendTask: bool = False,
        owner: _TaskOwner | None = None,
    ) -> AsyncTask: ...
    @overload
    def do_method_later(
        self,
        delayTime: float,
        funcOrTask: Callable,
        name: str | None,
        extraArgs: Sequence[Any] | None = None,
        sort: int | None = None,
        priority: int | None = None,
        taskChain: str | None = None,
        uponDeath: Callable[..., object] | None = None,
        appendTask: bool = False,
        owner: _TaskOwner | None = None,
    ) -> PythonTask: ...
    doMethodLater = do_method_later
    @overload
    def add(
        self,
        funcOrTask: AsyncTask,
        name: str | None = None,
        sort: int | None = None,
        extraArgs: Sequence[Any] | None = None,
        priority: int | None = None,
        uponDeath: Callable[..., object] | None = None,
        appendTask: bool = False,
        taskChain: str | None = None,
        owner: _TaskOwner | None = None,
        delay: float | None = None,
    ) -> AsyncTask: ...
    @overload
    def add(
        self,
        funcOrTask: Callable,
        name: str | None = None,
        sort: int | None = None,
        extraArgs: Sequence[Any] | None = None,
        priority: int | None = None,
        uponDeath: Callable[..., object] | None = None,
        appendTask: bool = False,
        taskChain: str | None = None,
        owner: _TaskOwner | None = None,
        delay: float | None = None,
    ) -> PythonTask: ...
    @overload
    def remove(self, taskOrName: str | AsyncTask) -> bool: ...
    @overload
    def remove(self, taskOrName: list[str | AsyncTask]) -> None: ...
    def removeTasksMatching(self, taskPattern: str | GlobPattern) -> int: ...
    def step(self) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def replaceMethod(self, oldMethod: Callable[..., Any], newFunction: Callable[..., Any]) -> int: ...
    def popupControls(self) -> TaskManagerPanel: ...
    def getProfileSession(self, name: str | None = None) -> ProfileSession: ...
    def profileFrames(
        self,
        num: int | None = None,
        session: ProfileSession | None = None,
        callback: Callable[[], object] | None = None,
    ) -> None: ...
    def getProfileFrames(self) -> bool: ...
    def getProfileFramesSV(self) -> StateVar: ...
    def setProfileFrames(self, profileFrames: bool) -> None: ...
    def getProfileTasks(self) -> bool: ...
    def getProfileTasksSV(self) -> StateVar: ...
    def setProfileTasks(self, profileTasks: bool) -> None: ...
    def logTaskProfiles(self, name: str | None = None) -> None: ...
    def flushTaskProfiles(self, name: str | None = None) -> None: ...
    def doYield(self, frameStartTime: Unused, nextScheduledTaskTime: Unused) -> None: ...
