from _typeshed import StrOrBytesPath
from collections.abc import Callable, Container, Iterable
from typing import ClassVar, overload
from typing_extensions import Final, TypeAlias

from direct._typing import Incomplete
from direct.p3d.DeploymentTools import Icon
from setuptools import Command  # type: ignore[import]

_FileHandler: TypeAlias = Callable[[build_apps, Incomplete, Incomplete], StrOrBytesPath]
_OpenFile: TypeAlias = StrOrBytesPath | int

def egg2bam(_build_cmd: object, srcpath: str, dstpath: str) -> str: ...

macosx_binary_magics: Final[tuple[bytes, ...]]
PACKAGE_DATA_DIRS: Final[dict[str, list[tuple[str, str, set[str]]]]]
PACKAGE_LIB_DIRS: Final[dict[str, list[tuple[str, str | None]]]]
SITE_PY2: Final[str]
SITE_PY3: Final[str]
SITE_PY_TKINTER_ADDENDUM: Final[str]
SITE_PY: Final[str]

class build_apps(Command):
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    default_file_handlers: ClassVar[dict[str, _FileHandler]]
    build_base: str
    gui_apps: dict[str, str]
    console_apps: dict[str, str]
    macos_main_app: str | None
    rename_paths: dict[str, str]
    include_patterns: list[str]
    exclude_patterns: list[str]
    include_modules: dict[str, list[str]]
    exclude_modules: dict[str, list[str]]
    icons: dict[str, list[str] | tuple[str, ...]]
    platforms: list[str]
    plugins: list[str]
    embed_prc_data: bool
    extra_prc_files: list[str]
    extra_prc_data: str
    default_prc_dir: str | None
    log_filename: str | None
    log_filename_strftime: bool
    log_append: bool
    requirements_path: str
    use_optimized_wheels: bool
    optimized_wheel_index: str
    pypi_extra_indexes: list[str]
    file_handlers: dict[str, _FileHandler]
    exclude_dependencies: list[str]
    package_data_dirs: dict[str, Iterable[tuple[str, str, Container[str]]]]
    icon_object: dict[str, Icon]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def download_wheels(self, platform: str) -> list[str]: ...
    def update_pe_resources(self, appname: str, runtime: _OpenFile) -> None: ...
    def bundle_macos_app(self, builddir: str) -> None: ...
    def build_runtimes(self, platform: str, use_wheels: bool) -> None: ...
    def add_dependency(self, name: str, target_dir: str, search_path: Iterable[str], referenced_by: object) -> None: ...
    def copy(self, source_path: str, target_path: str) -> None: ...
    def copy_with_dependencies(self, source_path: str, target_path: str, search_path: Iterable[str]) -> None: ...
    def copy_dependencies(self, target_path: str, target_dir: str, search_path: Iterable[str], referenced_by: object) -> None: ...
    @overload
    def expand_path(self, path: str, platform: str) -> str: ...
    @overload
    def expand_path(self, path: None, platform: str) -> None: ...

class bdist_apps(Command):
    DEFAULT_INSTALLERS: ClassVar[dict[str, list[str]]]
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    installers: dict[str, list[str]]
    dist_dir: str
    skip_build: bool
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def create_zip(self, basename: str, build_dir: str) -> None: ...
    def create_tarball(self, basename: str, build_dir: str, tar_compression: str) -> None: ...
    def create_nsis(self, basename: object, build_dir: str, is_64bit: bool) -> None: ...
    def run(self) -> None: ...

def finalize_distribution_options(dist) -> None: ...
