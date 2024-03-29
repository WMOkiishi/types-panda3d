from collections.abc import Callable
from typing import Any, ClassVar, SupportsFloat

from panda3d.core import DatagramIterator

class PyDatagramIterator(DatagramIterator):
    FuncDict: ClassVar[dict[int, Callable[[], Any]]]
    def getChannel(self) -> int: ...
    def getArg(self, subatomicType: int, divisor: SupportsFloat = 1) -> list[Any]: ...
