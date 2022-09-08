__all__ = ['FileSpec']

from os import PathLike, stat_result
from typing_extensions import TypeAlias

from panda3d.core import ConfigVariableFilename, Filename, TiXmlElement
from ..directnotify.Notifier import Notifier

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike

class FileSpec:
    actualFile: FileSpec | None
    filename: str | None
    basename: str
    size: int
    timestamp: int
    hash: str | None
    def __init__(self) -> None: ...
    def fromFile(
        self,
        packageDir: _Filename,
        filename: _Filename,
        pathname: Filename | None = None,
        st: stat_result | None = None,
    ) -> None: ...
    def readHash(self, pathname: _Filename) -> None: ...
    def loadXml(self, xelement: TiXmlElement) -> None: ...
    def storeXml(self, xelement: TiXmlElement) -> None: ...
    def storeMiniXml(self, xelement: TiXmlElement) -> None: ...
    def quickVerify(
        self,
        packageDir: _Filename | None = None,
        pathname: Filename | None = None,
        notify: Notifier | None = None,
        correctSelf: bool = False,
    ) -> bool: ...
    def fullVerify(
        self,
        packageDir: _Filename | None = None,
        pathname: Filename | None = None,
        notify: Notifier | None = None,
    ) -> bool: ...
    def checkHash(self, packageDir: _Filename, pathname: Filename | None, st: stat_result | None) -> bool: ...
