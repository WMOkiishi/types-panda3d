from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from .Job import Job

class JobManager:
    notify: ClassVar[Notifier]
    TaskName: ClassVar[str]
    def __init__(self, timeslice: float | None = None) -> None: ...
    def destroy(self) -> None: ...
    def add(self, job: Job) -> None: ...
    def remove(self, job: Job) -> None: ...
    def finish(self, job: Job) -> None: ...
    @staticmethod
    def getDefaultTimeslice() -> float: ...
    def getTimeslice(self) -> float: ...
    def setTimeslice(self, timeslice: float | None) -> None: ...
