from collections.abc import Generator
from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from .DirectObject import DirectObject
from .Job import Job

class MessengerLeakObject(DirectObject): ...

class MessengerLeakDetector(Job):
    notify: ClassVar[Notifier]
    def run(self) -> Generator[None, None, None]: ...
