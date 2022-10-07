__all__ = ['ArgumentError', 'OutsideOfPackageError', 'Packager', 'PackagerError']

from collections.abc import Container, Iterable, Sequence
from typing import Any, ClassVar
from typing_extensions import Literal

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from direct.dist.FreezeTool import Freezer
from direct.showbase.Loader import Loader
from panda3d._typing import Filepath
from panda3d.core import (
    DSearchPath,
    Filename,
    GlobPattern,
    HTTPClient,
    LoaderOptions,
    Multifile,
    PandaNode,
    TiXmlElement,
    TiXmlNode,
)
from .FileSpec import FileSpec
from .SeqValue import SeqValue

class PackagerError(Exception): ...
class OutsideOfPackageError(PackagerError): ...
class ArgumentError(PackagerError): ...

class Packager:
    class PackFile:
        filename: Filename
        newName: str
        deleteTemp: bool
        explicit: bool
        compress: bool
        extract: bool
        text: str | None
        unprocessed: bool
        executable: bool
        dependencyDir: str | None
        platformSpecific: bool
        required: bool
        def __init__(
            self,
            package,
            filename: Filename,
            newName: str | None = None,
            deleteTemp: bool = False,
            explicit: bool = False,
            compress: bool | None = None,
            extract: bool | None = None,
            text: str | None = None,
            unprocessed: bool | None = None,
            executable: bool | None = None,
            dependencyDir: str | None = None,
            platformSpecific: bool | None = None,
            required: bool = False,
        ) -> None: ...
        def isExcluded(self, package: Packager.Package) -> bool: ...

    class ExcludeFilename:
        packager: Packager
        localOnly: bool
        glob: GlobPattern
        def __init__(self, packager: Packager, filename: Filename, caseSensitive: Unused) -> None: ...
        def matches(self, filename: Filename) -> None: ...

    class PackageEntry:
        packageSeq: SeqValue
        packageSetVer: SeqValue
        packageName: str
        platform: str
        version: str
        solo: bool
        perPlatform: bool
        descFile: FileSpec
        importDescFile: FileSpec | None
        def __init__(self) -> None: ...
        def getKey(self) -> tuple[SeqValue, str, str]: ...
        def fromFile(
            self,
            packageName: str,
            platform: str,
            version: str,
            solo: bool,
            perPlatform: bool,
            installDir: Filepath,
            descFilename: Filepath,
            importDescFilename: Filepath | None,
        ) -> None: ...
        def loadXml(self, xpackage: TiXmlElement) -> None: ...
        def makeXml(self) -> TiXmlElement: ...

    class HostEntry:
        url: str | None
        downloadUrl: str | None
        descriptiveName: str | None
        hostDir: str | None
        mirrors: list[str]
        altHosts: dict[str, str]
        def __init__(
            self,
            url: str | None = None,
            downloadUrl: str | None = None,
            descriptiveName: str | None = None,
            hostDir: str | None = None,
            mirrors: list[str] | None = None,
        ) -> None: ...
        def loadXml(self, xhost: TiXmlElement, packager: Packager) -> None: ...
        def makeXml(self, packager: Packager | None = None) -> TiXmlElement: ...

    class Package:
        packageName: str
        packager: Packager
        notify: Notifier
        platform: str | None
        perPlatform: bool
        arch: str | None
        version: str | None
        host: str | None
        p3dApplication: bool
        solo: bool
        compressionLevel: int
        importedMapsDir: str
        mainModule: tuple[str, str] | None
        signParams: list
        requires: list[Packager.Package]
        packageSetVer: SeqValue
        configs: dict[str, Any]
        skipFilenames: dict[str, Literal[True]]
        skipModules: dict[str, Freezer.ModuleDef]
        excludedFilenames: list[Packager.ExcludeFilename]
        files: list[Packager.PackFile]
        sourceFilenames: dict[Filename, Packager.PackFile]
        targetFilenames: dict[str, Packager.PackFile]
        requiredFilenames: list[Packager.PackFile]
        requiredModules: list[str]
        missingPackages: list[tuple[str, str | None]]
        freezer: Freezer
        ignoredDirFiles: dict[str, int]
        multifile: Multifile
        extracts: list[tuple[str, TiXmlElement]]
        components: list[tuple[str, str, TiXmlElement]]
        packageSeq: SeqValue
        patchVersion: str | None
        patches: list[TiXmlNode]
        oldCompressedBasename: Filepath
        moduleNames: dict[str, Freezer.ModuleDef]
        text: str | None
        deleteTemp: bool
        def __init__(self, packageName: str, packager: Packager) -> None: ...
        def close(self) -> bool | None: ...
        def considerPlatform(self) -> None: ...
        def installMultifile(self) -> bool: ...
        def installSolo(self) -> Literal[True, None]: ...
        def cleanup(self) -> None: ...
        def addFile(
            self,
            filename: Filename,
            newName: str | None = None,
            delteTemp: bool = False,
            explicit: bool = False,
            compress: bool | None = None,
            extract: bool | None = None,
            text: str | None = None,
            unprocessed: bool | None = None,
            executable: bool | None = None,
            dependencyDir: str | None = None,
            platformSpecific: bool | None = None,
            required: bool = False,
        ) -> Packager.PackFile: ...
        def excludeFile(self, filename: Filename) -> None: ...
        def addExtensionModules(self) -> None: ...
        def makeP3dInfo(self) -> None: ...
        def compressMultifile(self) -> None: ...
        def readDescFile(self) -> None: ...
        def writeDescFile(self) -> None: ...
        def writeImportDescFile(self) -> None: ...
        def readImportDescFile(self, filename: Filename) -> bool: ...
        def getFileSpec(self, element: str | TiXmlElement, pathname: Filename, newName: str) -> TiXmlElement: ...
        def addPyFile(self, file: Packager.PackFile) -> None: ...
        def addEggFile(self, file: Packager.PackFile) -> None: ...
        def addBamFile(self, file: Packager.PackFile) -> None: ...
        def addNode(self, node: PandaNode, filename: Unused, newName: str) -> None: ...
        def addFoundTexture(self, filename: Filepath) -> str: ...
        def addDcFile(self, file: Packager.PackFile) -> None: ...
        def addDcImports(self, file: Packager.PackFile) -> None: ...
        def addPrcFile(self, file: Packager.PackFile) -> None: ...
        def addComponent(self, file: Packager.PackFile) -> None: ...
        def requirePackage(self, package: Packager.Package) -> None: ...

    notify: ClassVar[Notifier]
    platform: str
    arch: str | None
    installDir: Filepath | None
    systemRoot: Filepath | None
    ignoreSetHost: bool
    verbosePrint: bool
    p3dSuffix: str
    hosts: dict[str, Packager.HostEntry]
    host: str
    http: HTTPClient
    maxAge: int
    contentsSeq: SeqValue
    installSearch: list[Filename]
    libraryCache: dict[str, Filename]
    executablePath: DSearchPath
    allowPythonDev: bool
    storePythonSource: bool
    signParams: list[tuple[Any, Any | None, Any | None, Any | None]]
    encryptionKey = ...
    prcEncryptionKey: str | None
    prcSignCommand = ...
    dcClientSuffixes: list[str]
    caseSensitive: bool
    imageExtensions: list[str]
    modelExtensions: list[str]
    textExtensions: list[str]
    binaryExtensions: list[str]
    nonuniqueExtensions: list[str]
    executableExtensions: list[str]
    manifestExtensions: list[str]
    remapExtensions: dict[str, str]
    extractExtensinos: list[str]
    platformSpecificExtensions: list[str]
    uncompressibleExtensions: list[str]
    unprocessedExtensions: list[str]
    suppressWarningForExtensions: list[str]
    excludeSystemFiles: list[str]
    excludeSystemGlobs: list[GlobPattern]
    loader: Loader
    sfxManagerList = ...
    musicManager = ...
    loaderOpts: LoaderOptions
    packageList: list[Packager.Package]
    packages: dict[tuple[str, str | None, str | None], Packager.Package]
    contents: dict[str, Packager.PackageEntry]
    currentPackage: Packager.Package | None
    p3dInstallDir: str
    allowPackages: bool
    def __init__(self, platform: str | None = None) -> None: ...
    def loadLdconfigCache(self) -> bool: ...
    def resolveLibrary(self, filename: Filename) -> bool: ...
    def setPlatform(self, platform: str | None = None) -> None: ...
    def setHost(
        self,
        host: str,
        downloadUrl: str | None = None,
        descriptiveName: str | None = None,
        hostDir: str | None = None,
        mirrors: list[str] | None = None,
    ) -> None: ...
    def addHost(
        self,
        host: str,
        downloadUrl: str | None = None,
        descriptiveName: str | None = None,
        hostDir: str | None = None,
        mirrors: list[str] | None = None,
    ) -> HostEntry: ...
    def addAltHost(
        self,
        keyword: str,
        altHost: str,
        origHost: str | None = None,
        downloadUrl: str | None = None,
        descriptiveName: str | None = None,
        hostDir: str | None = None,
        mirrors: list[str] | None = None,
    ) -> None: ...
    def addWindowsSearchPath(self, searchPath, varname: str) -> None: ...
    def addPosixSearchPath(self, searchPath, varname: str) -> None: ...
    def setup(self) -> None: ...
    def close(self) -> None: ...
    def buildPatches(self, packages: Iterable[Packager.Package]) -> None: ...
    def readPackageDef(self, packageDef, packageNames: Container[str] | None = None) -> list[Packager.Package]: ...
    def beginPackage(self, packageName: str, p3dApplication: bool = False, solo: bool = False) -> None: ...
    def endPackage(self) -> None: ...
    def findPackage(
        self,
        packageName: str,
        platform: str | None = None,
        version: str | None = None,
        host: str | None = None,
        requires: Iterable[Packager.Package] | None = None,
    ) -> Packager.Package | None: ...
    def do_setVer(self, value: tuple[int, ...] | str) -> None: ...
    def do_config(self, **kw: Any) -> None: ...
    def requirePackagesNamed(self, names: Iterable[str], version: str | None = None, host: str | None = None) -> None: ...
    do_require = requirePackagesNamed
    def requirePackage(self, package: Packager.Package) -> None: ...
    def addModule(
        self, moduleNames: Sequence[str], newName: str | None = None, filename: Filepath | None = None, required: bool = False
    ) -> None: ...
    do_module = addModule
    def do_excludeModule(self, *args: str) -> None: ...
    def do_main(self, filename: Filepath | None) -> None: ...
    def do_mainModule(self, moduleName: str, newName: str | None = None, filename: Filepath | None = None) -> None: ...
    def do_sign(self, certificate, chain=None, pkey=None, password=None) -> None: ...
    def do_setupPanda3D(self, p3dpythonName: str | None = None, p3dpythonwName: str | None = None) -> None: ...
    def do_freeze(self, filename: str, compileToExe: bool = False) -> None: ...
    def do_makeBundle(
        self,
        bundleName: str,
        plist: str,
        executable: Filepath | None = None,
        resources: Sequence[Filepath] | None = None,
        dependencyDir: str | None = None,
    ) -> None: ...
    def addFiles(
        self,
        filenames: Sequence[Filepath],
        text: str | None = None,
        newName: str | None = None,
        newDir: Filepath | None = None,
        extract: bool | None = None,
        executable: bool | None = None,
        deleteTemp: bool = False,
        literal: bool = False,
        dependencyDir: str | None = None,
        required: bool = False,
    ) -> None: ...
    do_file = addFiles
    def do_exclude(self, filename: Filepath) -> None: ...
    def do_includeExtensions(
        self,
        executableExtensions: Iterable[str] | None = None,
        extractExtensions: Iterable[str] | None = None,
        imageExtensions: Iterable[str] | None = None,
        textExtensions: Iterable[str] | None = None,
        uncompressibleExtensions: Iterable[str] | None = None,
        unprocessedExtensions: Iterable[str] | None = None,
        suppressWarningForExtensions: Iterable[str] | None = None,
    ) -> None: ...
    def do_dir(self, dirname: Filepath, newDir: str | None = None, unprocessed: bool | None = None) -> None: ...
    def readContentsFile(self) -> None: ...
    def writeContentsFile(self) -> None: ...

class metaclass_def(type): ...
class class_p3d(metaclass=metaclass_def): ...
class class_package(metaclass=metaclass_def): ...
class class_solo(metaclass=metaclass_def): ...

class func_closure:
    name: str
    def __init__(self, name: str) -> None: ...
    def generic_func(self, *args, **kw) -> None: ...
