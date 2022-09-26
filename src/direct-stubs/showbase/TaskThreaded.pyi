__all__ = ['TaskThread', 'TaskThreaded']

from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from typing import ClassVar

from direct.directnotify.Notifier import Notifier

class TaskThreaded:
    notify: ClassVar[Notifier]
    def __init__(
        self,
        name: str,
        threaded: bool = True,
        timeslice: float | None = None,
        callback: Callable[[], object] | None = None,
    ) -> None: ...
    def finished(self) -> None: ...
    def destroy(self) -> None: ...
    def getTimeslice(self) -> float: ...
    def setTimeslice(self, timeslice: float) -> None: ...
    def scheduleCallback(self, callback: Callable[[], object]) -> None: ...
    def scheduleThread(self, thread: TaskThread) -> None: ...
    def taskTimeLeft(self) -> bool: ...

class TaskThread(metaclass=ABCMeta):
    @abstractmethod
    def setUp(self) -> None: ...
    @abstractmethod
    def run(self) -> None: ...
    @abstractmethod
    def tearDown(self) -> None: ...
    @abstractmethod
    def done(self) -> None: ...
    def finished(self) -> None: ...
    def isFinished(self) -> bool: ...
    def timeLeft(self) -> float: ...
