__all__ = ['PackageMerger', 'PackageMergerError']

from _typeshed import StrOrBytesPath
from collections.abc import Container
from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from panda3d.core import TiXmlDocument, TiXmlElement, TiXmlNode

from .FileSpec import FileSpec
from .SeqValue import SeqValue

class PackageMergerError(Exception): ...

class PackageMerger:
    class PackageEntry:
        sourceDir: StrOrBytesPath
        packageName: str
        platform: str
        version: str
        solo: bool
        perPlatform: bool
        descFile: FileSpec
        packageSeq: SeqValue
        packageSetVer: SeqValue
        importDescFile = ...
        def __init__(self, xpackage: TiXmlElement, sourceDir: StrOrBytesPath) -> None: ...
        def getKey(self) -> tuple[str, str, str]: ...
        def isNewer(self, other: PackageMerger.PackageEntry) -> bool: ...
        def loadXml(self, xpackage: TiXmlElement) -> None: ...
        def makeXml(self) -> TiXmlElement: ...
        def validatePackageContents(self) -> None: ...

    notify: ClassVar[Notifier]
    installDir: StrOrBytesPath
    xhost: TiXmlNode | None
    contents: dict[tuple[str, str, str], PackageMerger.PackageEntry]
    maxAge: int | None
    contentsSeq: SeqValue
    contentsDoc: TiXmlDocument
    def __init__(self, installDir: StrOrBytesPath) -> None: ...
    def merge(self, sourceDir: StrOrBytesPath, packageNames: Container[str] | None = ...) -> None: ...
    def close(self) -> None: ...
