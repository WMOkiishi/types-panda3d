__all__ = ['PatchMaker']

from _typeshed import Self
from collections.abc import MutableSequence
from typing_extensions import TypeAlias

from panda3d._typing import Filepath
from panda3d.core import Filename, TiXmlDocument, TiXmlElement
from .FileSpec import FileSpec

_Key: TypeAlias = tuple[str | None, str | None, str | None, str | None, FileSpec | None]
_Plan: TypeAlias = list[tuple[PatchMaker.Patchfile, PatchMaker.PackageVersion]]

class PatchMaker:
    class PackageVersion:
        packageName: str | None
        platform: str | None
        version: str | None
        hostUrl: str | None
        file: FileSpec | None
        printName: str | None
        packageCurrent: PatchMaker.Package | None
        packageBase: PatchMaker.Package | None
        packageTop: PatchMaker.Package | None
        fromPatches: list[PatchMaker.Patchfile]
        toPatches: list[PatchMaker.Patchfile]
        tempFile: Filename | None
        def __init__(
            self,
            packageName: str | None,
            platform: str | None,
            version: str | None,
            hostUrl: str | None,
            file: FileSpec | None,
        ) -> None: ...
        def cleanup(self) -> None: ...
        def getPatchChain(
            self: Self,
            startPv: Self,
            alreadyVisited: MutableSequence[Self] = ...,
        ) -> list[PatchMaker.Patchfile] | None: ...
        def getRecreateFilePlan(
            self: Self,
            alreadyVisited: MutableSequence[Self] = ...,
        ) -> tuple[Filename, PatchMaker.PackageVersion, _Plan] | tuple[None, None, None]: ...
        def getFile(self) -> Filename | None: ...
        def applyPatch(self, origFile: Filepath, patchFilename: Filepath) -> Filename | None: ...
        def getNext(self, package: PatchMaker.Package) -> PatchMaker.Patchfile: ...
    class Patchfile:
        package: PatchMaker.Package
        packageName: str | None
        platform: str | None
        version: str | None
        hostUrl: str | None
        file: FileSpec | None
        sourceFile: FileSpec | None
        targetFile: FileSpec | None
        fromPv: PatchMaker.PackageVersion | None
        toPv: PatchMaker.PackageVersion | None
        def __init__(self, package: PatchMaker.Package) -> None: ...
        def getSourceKey(self) -> _Key: ...
        def getTargetKey(self) -> _Key: ...
        def fromFile(
            self,
            packageDir: Filepath,
            patchFilename: Filepath,
            sourceFile: FileSpec | None,
            targetFile: FileSpec | None,
        ) -> None: ...
        def loadXml(self, xpatch: TiXmlElement) -> None: ...
        def makeXml(self, package: PatchMaker.Package) -> TiXmlElement: ...
    class Package:
        packageDir: Filename
        packageDesc: Filepath
        patchMaker: PatchMaker
        contentsDocPackage: TiXmlElement | None
        patchVersion: int
        currentPv: PatchMaker.PackageVersion | None
        basePv: PatchMaker.PackageVersion | None
        topPv: PatchMaker.PackageVersion | None
        packageName: str | None
        platform: str | None
        version: str | None
        hostUrl: str | None
        currentFile: FileSpec | None
        baseFile: FileSpec | None
        doc: TiXmlDocument | None
        anyChanges: bool
        patches: list[PatchMaker.Patchfile]
        def __init__(self, packageDesc: Filepath, patchMaker: PatchMaker, xpackage: TiXmlElement | None = None) -> None: ...
        def getCurrentKey(self) -> _Key: ...
        def getBaseKey(self) -> _Key: ...
        def getTopKey(self) -> _Key: ...
        def getGenericKey(self, fileSpec: FileSpec | None) -> _Key: ...
        def readDescFile(self, doProcessing: bool = False) -> bool: ...
        def writeDescFile(self) -> None: ...
    installDir: Filepath
    packageVersions: dict[_Key, PatchMaker.PackageVersion]
    packages: list[PatchMaker.Package]
    patchFilenames: dict[str, PatchMaker.Patchfile]
    def __init__(self, installDir: Filepath) -> None: ...
    def buildPatches(self, packageNames: MutableSequence[PatchMaker.Patchfile] | None = None) -> bool: ...
    def cleanup(self) -> None: ...
    def getPatchChainToCurrent(self, descFilename: Filepath, fileSpec: FileSpec | None) -> list[PatchMaker.Patchfile] | None: ...
    def readPackageDescFile(self, descFilename: Filepath) -> PatchMaker.Package | None: ...
    def readContentsFile(self) -> bool: ...
    def writeContentsFile(self) -> None: ...
    def getPackageVersion(self, key: _Key) -> PatchMaker.PackageVersion: ...
    def buildPatchChains(self) -> None: ...
    def recordPatchfile(self, patchfile: PatchMaker.Patchfile) -> None: ...
    def processSomePackages(self, packageNames: MutableSequence[PatchMaker.Package]) -> None: ...
    def processAllPackages(self) -> None: ...
    def processPackage(self, package: PatchMaker.Package) -> None: ...
    def buildPatch(
        self,
        v1: PatchMaker.PackageVersion,
        v2: PatchMaker.PackageVersion,
        package: PatchMaker.Package,
        patchFilename: Filename | str,
    ) -> bool: ...
    def buildPatchFile(
        self,
        origFilename: Filename,
        newFilename: Filepath,
        patchFilename: Filename,
        printOrigName: object,
        printNewName: object,
    ) -> bool: ...
