__all__ = ['directNotify', 'giveNotify']

from typing import ClassVar, Final, Protocol

from .DirectNotify import DirectNotify
from .Notifier import Notifier

class _SupportsNotify(Protocol):
    notify: ClassVar[Notifier]

directNotify: Final[DirectNotify]

def giveNotify(cls: type[_SupportsNotify]) -> None: ...
