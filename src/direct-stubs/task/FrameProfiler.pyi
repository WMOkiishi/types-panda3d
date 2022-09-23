from typing import ClassVar
from typing_extensions import Final, Literal

from ..directnotify.Notifier import Notifier

class FrameProfiler:
    notify: ClassVar[Notifier]
    Minute: Final[Literal[60]]
    Hour: Final[Literal[3600]]
    Day: Final[Literal[86400]]
    def __init__(self) -> None: ...
    def destroy(self) -> None: ...
