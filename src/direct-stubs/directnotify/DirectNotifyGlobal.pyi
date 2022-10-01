__all__ = ['directNotify', 'giveNotify']

from typing import ClassVar, Protocol
from typing_extensions import Final

from .DirectNotify import DirectNotify
from .Notifier import Notifier

class _SupportsNotify(Protocol):
    __name__: ClassVar[str]
    notify: ClassVar[Notifier]

directNotify: Final[DirectNotify]
def giveNotify(cls: type[_SupportsNotify]) -> None: ...
