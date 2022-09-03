__all__ = ['PackageMerger', 'PackageMergerError']

from collections.abc import Container
from os import PathLike
from typing import ClassVar
from typing_extensions import TypeAlias

from panda3d.core import ConfigVariableFilename, Filename, TiXmlDocument, TiXmlElement, TiXmlNode
from ..directnotify.Notifier import Notifier
from .FileSpec import FileSpec
from .SeqValue import SeqValue

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike

class PackageMergerError(Exception): ...

class PackageMerger:
    class PackageEntry:
        sourceDir: _Filename
        packageName: str
        platform: str
        version: str
        solo: bool
        perPlatform: bool
        descFile: FileSpec
        packageSeq: SeqValue
        packageSetVer: SeqValue
        importDescFile = ...
        def __init__(self, xpackage: TiXmlElement, sourceDir: _Filename) -> None: ...
        def getKey(self) -> tuple[str, str, str]: ...
        def isNewer(self, other: PackageMerger.PackageEntry) -> bool: ...
        def loadXml(self, xpackage: TiXmlElement) -> None: ...
        def makeXml(self) -> TiXmlElement: ...
        def validatePackageContents(self) -> None: ...
    notify: ClassVar[Notifier]
    installDir: _Filename
    xhost: TiXmlNode | None
    contents: dict[tuple[str, str, str], PackageMerger.PackageEntry]
    maxAge: int | None
    contentsSeq: SeqValue
    contentsDoc: TiXmlDocument
    def __init__(self, installDir: _Filename) -> None: ...
    def merge(self, sourceDir: _Filename, packageNames: Container[str] | None = None) -> None: ...
    def close(self) -> None: ...
