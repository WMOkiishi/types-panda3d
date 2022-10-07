__all__ = ['FileSpec']

from os import stat_result

from direct.directnotify.Notifier import Notifier
from panda3d._typing import Filepath
from panda3d.core import Filename, TiXmlElement

class FileSpec:
    actualFile: FileSpec | None
    filename: str | None
    basename: str
    size: int
    timestamp: int
    hash: str | None
    def __init__(self) -> None: ...
    def fromFile(
        self, packageDir: Filepath, filename: Filepath, pathname: Filename | None = None, st: stat_result | None = None
    ) -> None: ...
    def readHash(self, pathname: Filepath) -> None: ...
    def loadXml(self, xelement: TiXmlElement) -> None: ...
    def storeXml(self, xelement: TiXmlElement) -> None: ...
    def storeMiniXml(self, xelement: TiXmlElement) -> None: ...
    def quickVerify(
        self,
        packageDir: Filepath | None = None,
        pathname: Filename | None = None,
        notify: Notifier | None = None,
        correctSelf: bool = False,
    ) -> bool: ...
    def fullVerify(
        self, packageDir: Filepath | None = None, pathname: Filename | None = None, notify: Notifier | None = None
    ) -> bool: ...
    def checkHash(self, packageDir: Filepath, pathname: Filename | None, st: stat_result | None) -> bool: ...
