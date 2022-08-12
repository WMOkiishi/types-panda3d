__all__ = ['directNotify', 'giveNotify']

from collections.abc import Callable
from typing import ClassVar
from typing_extensions import Protocol

from .DirectNotify import DirectNotify
from .Notifier import Notifier

class _SupportsNotify(Protocol):
    __name__: ClassVar[str]
    notify: ClassVar[Notifier]

directNotify: DirectNotify
giveNotify: Callable[[type[_SupportsNotify]], None]
