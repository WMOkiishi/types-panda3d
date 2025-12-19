from _typeshed import FileDescriptorOrPath, Incomplete, StrOrBytesPath, StrPath, SupportsRead
from collections.abc import Callable, Container, Iterable
from typing import ClassVar, Final, overload
from typing_extensions import TypeAlias

from direct.dist.icon import Icon
from setuptools import Command  # type: ignore[import-untyped]

_FileHandler: TypeAlias = Callable[[build_apps, Incomplete, Incomplete], StrOrBytesPath]
_FileRead: TypeAlias = FileDescriptorOrPath | SupportsRead[bytes] | SupportsRead[str]
_OpenFile: TypeAlias = StrOrBytesPath | int

macosx_binary_magics: Final[tuple[bytes, ...]]
PACKAGE_DATA_DIRS: Final[dict[str, list[tuple[str, str, set[str]]]]]
PACKAGE_LIB_DIRS: Final[dict[str, list[tuple[str, str | None]]]]
SITE_PY: Final[str]
SITE_PY_ANDROID: Final[str]

class build_apps(Command):
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str, str]] | list[tuple[str, str | None, str]]]
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
    def generate_android_manifest(self, path: FileDescriptorOrPath) -> None: ...
    def check_android_manifest(self, path: _FileRead) -> None: ...
    def build_binaries(
        self, platform: str, binary_dir: StrPath, data_dir: StrPath | None = None, blob_dir: StrPath | None = None
    ) -> None: ...
    def build_assets(self, platform: str, data_dir: StrPath) -> None: ...
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
    DEFAULT_INSTALLER_FUNCS: ClassVar[dict[str, Callable]]
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str, str]] | list[tuple[str, str | None, str]]]
    installers: dict[str, list[str]]
    dist_dir: str
    skip_build: bool
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def get_archive_basedir(self) -> str: ...
    def get_current_platform(self) -> str | None: ...
    def run(self) -> None: ...

def finalize_distribution_options(dist) -> None: ...
