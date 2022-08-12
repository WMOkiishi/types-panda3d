from typing import ClassVar
from typing_extensions import Literal

from ..directnotify.Notifier import Notifier

class FrameProfiler:
    notify: ClassVar[Notifier]
    Minute: ClassVar[Literal[60]]
    Hour: ClassVar[Literal[3600]]
    Day: ClassVar[Literal[86400]]
    def __init__(self) -> None: ...
    def destroy(self) -> None: ...
