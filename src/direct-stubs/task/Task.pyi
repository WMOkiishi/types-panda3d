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
from typing_extensions import Literal, Protocol

from panda3d.core import (
    AsyncTask, AsyncTaskPause, AsyncTaskSequence,
    ClockObject, ConfigVariableBool,
    GlobPattern, PythonTask,
    AsyncTaskManager,
)
from panda3d.core import AsyncTaskPause as pause
from ..directnotify.Notifier import Notifier
from ..fsm.StatePush import StateVar

def print_exc_plus() -> None: ...

done: Literal[0]
cont: Literal[1]
again: Literal[2]
pickup: Literal[3]
exit: Literal[4]

class Task(PythonTask):
    cont: ClassVar[Literal[1]]
    again: ClassVar[Literal[2]]
    pickup: ClassVar[Literal[3]]
    exit: ClassVar[Literal[4]]
    @staticmethod
    @overload
    def pause(__param0: AsyncTaskPause) -> AsyncTaskPause: ...
    @staticmethod
    @overload
    def pause(delay: float) -> AsyncTaskPause: ...
    @staticmethod
    def gather(args): ...
    @staticmethod
    def sequence(*taskList: AsyncTask) -> AsyncTaskSequence: ...
    @staticmethod
    def loop(*taskList: AsyncTask) -> AsyncTaskSequence: ...

gather = ...
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
    def __init__(self) -> None: ...
    def finalInit(self) -> None: ...
    def destroy(self) -> None: ...
    def setClock(self, clockObject: ClockObject) -> None: ...
    @property
    def clock(self) -> ClockObject: ...
    def invokeDefaultHandler(self, signalNumber: object, stackFrame: object) -> NoReturn: ...
    def keyboardInterruptHandler(self, signalNumber: object, stackFrame: object) -> None: ...
    def getCurrentTask(self): ...
    def hasTaskChain(self, chainName: str) -> bool: ...
    def setupTaskChain(
        self,
        chainName: str,
        numThreads: int | None = None,
        tickClock: bool = False,
        threadPriority = None,
        frameBudget = None,
        frameSync: bool = False,
        timeslicePriority: bool = False,
    ): ...
    def hasTaskNamed(self, taskName: str) -> bool: ...
    def getTasksNamed(self, taskName: str): ...
    def getTasksMatching(self, taskPattern: str | GlobPattern): ...
    def getAllTasks(self): ...
    def getTasks(self): ...
    def getDoLaters(self): ...
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
        name: str | None,
        sort: int | None = None,
        extraArgs: Sequence[Any] | None = None,
        priority: int | None = None,
        appendTask: bool = False,
        uponDeath: Callable[..., object] | None = None,
        taskChain: str | None = None,
        owner: _TaskOwner | None = None,
        delay: float | None = None,
    ) -> AsyncTask: ...
    @overload
    def add(
        self,
        funcOrTask: Callable,
        name: str | None,
        sort: int | None = None,
        extraArgs: Sequence[Any] | None = None,
        priority: int | None = None,
        appendTask: bool = False,
        uponDeath: Callable[..., object] | None = None,
        taskChain: str | None = None,
        owner: _TaskOwner | None = None,
        delay: float | None = None,
    ) -> PythonTask: ...
    def remove(self, taskOrName): ...
    def removeTasksMatching(self, taskPattern: str | GlobPattern) -> int: ...
    def step(self) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def replaceMethod(self, oldMethod, newFunction): ...
    def popupControls(self): ...
    def getProfileSession(self, name = None): ...
    def profileFrames(self, num = None, session = None, callback = None): ...
    def getProfileFrames(self): ...
    def getProfileFramesSV(self): ...
    def setProfileFrames(self, profileFrames) -> None: ...
    def getProfileTasks(self) -> StateVar: ...
    def getProfileTasksSV(self): ...
    def setProfileTasks(self, profileTasks) -> None: ...
    def logTaskProfiles(self, name = None) -> None: ...
    def flushTaskProfiles(self, name = None) -> None: ...
    def doYield(self, frameStartTime: object, nextScheduledTaskTime: object) -> None: ...
