__all__ = ['SeqValue']

from panda3d.core import TiXmlElement

class SeqValue:
    value: tuple[int, ...]
    def __init__(self, value: tuple[int, ...] | str | None = None) -> None: ...
    def set(self, value: tuple[int, ...] | str) -> None: ...
    def setFromTuple(self, value: tuple[int, ...]) -> None: ...
    def setFromString(self, value: str) -> None: ...
    def loadXml(self, xelement: TiXmlElement, attribute: str = 'seq') -> bool: ...
    def storeXml(self, xelement: TiXmlElement, attribute: str = 'seq') -> None: ...
    def __add__(self, inc: int) -> SeqValue: ...
    def __cmp__(self, other): ...
    def __lt__(self, other: SeqValue) -> bool: ...
    def __gt__(self, other: SeqValue) -> bool: ...
    def __bool__(self) -> bool: ...
