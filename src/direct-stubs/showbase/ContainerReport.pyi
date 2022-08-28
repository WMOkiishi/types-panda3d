from collections.abc import Generator
from typing import Any, ClassVar

from ..directnotify.Notifier import Notifier
from .Job import Job

class ContainerReport(Job):
    notify: ClassVar[Notifier]
    PrivateIds: ClassVar[set[int]]
    def __init__(self, name: str, log: bool = False, limit: int | None = None, threaded: bool = False) -> None: ...
    def run(self) -> Generator[Any | None, None, None]: ...
    def log(self, *, limit: int | None = None) -> None: ...
