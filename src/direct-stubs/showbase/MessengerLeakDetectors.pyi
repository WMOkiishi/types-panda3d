from collections.abc import Generator
from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .DirectObject import DirectObject
from .Job import Job

class MessengerLeakObject(DirectObject):
    def __init__(self) -> None: ...

class MessengerLeakDetector(Job):
    notify: ClassVar[Notifier]
    def run(self) -> Generator[None, None, None]: ...
