from typing import ClassVar, Final

from direct.directnotify.Notifier import Notifier

class FrameProfiler:
    notify: ClassVar[Notifier]
    Minute: Final = 60
    Hour: Final = 3600
    Day: Final = 86400
    def __init__(self) -> None: ...
    def destroy(self) -> None: ...
