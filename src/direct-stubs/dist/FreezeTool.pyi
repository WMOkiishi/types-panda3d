from _typeshed import StrOrBytesPath, SupportsRead
from collections.abc import Container, Iterable, Mapping, Sequence
from modulefinder import Module, ModuleFinder
from typing import Any, TypeVar
from typing_extensions import Final, TypeAlias

from direct._typing import Unused
from panda3d.core import Filename, Multifile

_File = TypeVar('_File', bound=_OpenFile)
_OpenFile: TypeAlias = StrOrBytesPath | int

p3extend_frozen: Any | None
def pytest_imports() -> list[str]: ...

python: Final[str]
isDebugBuild: Final[bool]
startupModules: list[str]
builtinInitFuncs: dict[str, str | None]
hiddenImports: dict[str, list[str]]
ignoreImports: dict[str, list[str]]
overrideModules: dict[str, str]
reportedMissing: dict[str, bool]

class CompilationEnvironment:
    platform: str
    compileObj: str
    linkExe: str
    linkDll: str
    Python: str | None
    PythonIPath: str
    PythonVersion: int | str | None
    MSVC: str | None
    PSDK: str | None
    MD: str | None
    suffix64: str
    dllext: str
    arch: str
    def __init__(self, platform: str) -> None: ...
    def determineStandardSetup(self) -> None: ...
    def compileExe(self, filename: object, basename: object, extraLink: Iterable[str] = ...) -> None: ...
    def compileDll(self, filename: object, basename: object, extraLink: Iterable[str] = ...) -> None: ...

frozenMainCode: str
frozenDllMainCode: str
mainInitCode: str
dllInitCode: str
programFile: str
okMissing: list[str]

class Freezer:

    class ModuleDef:
        moduleName: str
        filename: Filename | None
        implicit: bool
        guess: bool
        exclude: bool
        forbid: bool
        allowChildren: bool
        fromSource: Any
        text: str | None
        def __init__(
            self,
            moduleName: str,
            filename: StrOrBytesPath | None = None,
            implicit: bool = False,
            guess: bool = False,
            exclude: bool = False,
            forbid: bool = False,
            allowChildren: bool = False,
            fromSource: Any = None,
            text: str | None = None,
        ) -> None: ...

    platform: str
    cenv: CompilationEnvironment | None
    path: list[str] | None
    sourceExtension: str
    objectExtension: str
    keepTemporaryFiles: bool
    frozenMainCode: str
    frozenDllMainCode: str
    mainInitCode: str
    storePythonSource: bool
    extras: list
    linkExtensionModules: bool
    previousModules: dict[str, Freezer.ModuleDef]
    modules: dict[str, Freezer.ModuleDef]
    mf: PandaModuleFinder | None
    moduleSuffixes: list[tuple[str, str, int]]
    def __init__(
        self,
        previous: Freezer | None = None,
        debugLevel: Unused = ...,
        platform: str | None = None,
        path: list[str] | None = None,
    ) -> None: ...
    def excludeFrom(self, freezer: Freezer) -> None: ...
    def excludeModule(
        self,
        moduleName: str,
        forbid: bool = False,
        allowChildren: bool = False,
        fromSource: Any = None,
    ) -> None: ...
    def handleCustomPath(self, moduleName: str) -> None: ...
    def getModulePath(self, moduleName: str) -> list[str] | None: ...
    def getModuleStar(self, moduleName: str) -> list[str] | None: ...
    def addModule(
        self,
        moduleName: str,
        implicit: bool = False,
        newName: str | None = None,
        filename: StrOrBytesPath | None = None,
        guess: bool = False,
        fromSource: Any = None,
        text: str | None = None,
    ) -> None: ...
    def done(self, addStartupModules: bool = False) -> None: ...
    def reset(self) -> None: ...
    def mangleName(self, moduleName: str) -> str: ...
    def getAllModuleNames(self) -> list[str]: ...
    def getModuleDefs(self) -> list[tuple[str, Freezer.ModuleDef]]: ...
    def addToMultifile(self, multifile: Multifile, compressionLevel: int = ...) -> None: ...
    def writeMultifile(self, mfname: StrOrBytesPath) -> None: ...
    def writeCode(self, filename: _OpenFile | None, initCode: str = ...) -> None: ...
    def generateCode(self, basename: str, compileToExe: bool = False) -> str: ...
    def generateRuntimeFromStub(
        self,
        target: _File,
        stub_file: SupportsRead[bytes],
        use_console: bool,
        fields: Mapping[str, str | None] = ...,
        log_append: bool = False,
        log_filename_strftime: bool = False,
    ) -> _File: ...
    def makeModuleDef(self, mangledName: str, code: bytes) -> str: ...
    def makeModuleListEntry(self, mangledName: str, code: bytes, moduleName: str, module: object) -> str: ...
    def makeForbiddenModuleListEntry(self, moduleName: str) -> str: ...

class PandaModuleFinder(ModuleFinder):
    def __init__(
        self,
        path: list[str] | None = ...,
        debug: int = ...,
        excludes: Container[str] | None = ...,
        replace_paths: Sequence[tuple[str, str]] | None = ...,
        *,
        suffixes: Iterable[tuple[str, str, int]] = ...,
    ) -> None: ...
    def find_module(self, name: str, path: str | None = None, parent: Module | None = None): ...
