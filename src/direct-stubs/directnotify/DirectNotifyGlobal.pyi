__all__ = ['directNotify', 'giveNotify']

from typing import ClassVar
from typing_extensions import Final, Protocol

from .DirectNotify import DirectNotify
from .Notifier import Notifier

class _SupportsNotify(Protocol):
    __name__: ClassVar[str]
    notify: ClassVar[Notifier]

directNotify: Final[DirectNotify]
def giveNotify(cls: type[_SupportsNotify]) -> None: ...
