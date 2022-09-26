from collections.abc import Callable
from typing import Any, ClassVar

from panda3d.core import Datagram

class PyDatagram(Datagram):
    FuncDict: ClassVar[dict[int, tuple[Callable[[Datagram, Any], None], Callable[[Any], Any] | None]]]
    def addChannel(self, value: int) -> None: ...
    def addServerHeader(self, channel, sender, code) -> None: ...
    def addOldServerHeader(self, channel, sender, code) -> None: ...
    def addServerControlHeader(self, code) -> None: ...
    def putArg(self, arg: Any, subatomicType: int, divisor: float = 1) -> None: ...
