from collections.abc import Callable
from typing import ClassVar, overload
from setuptools import Command

def egg2bam(_build_cmd: object, srcpath: str, dstpath: str) -> str: ...
macosx_binary_magics: tuple[bytes, ...]
PACKAGE_DATA_DIRS: dict[str, list[tuple[str, str, set[str]]]]
PACKAGE_LIB_DIRS: dict[str, list[tuple[str, str | None]]]
SITE_PY2: str
SITE_PY3: str
SITE_PY_TKINTER_ADDENDUM: str
SITE_PY: str

class build_apps(Command):
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    default_file_handlers: ClassVar[dict[str, Callable]]
    build_base: str
    gui_apps: dict
    console_apps: dict
    macos_main_app = ...
    rename_paths: dict
    include_patterns: list
    exclude_patterns: list
    include_modules: dict
    exclude_modules: dict
    icons: dict
    platforms: list[str]
    plugins: list[str]
    embed_prc_data: bool
    extra_prc_files: list
    extra_prc_data: str
    default_prc_dir: str | None
    log_filename: str | None
    log_filename_strftime: bool
    log_append: bool
    requirements_path: str
    use_optimized_wheels: bool
    optimized_wheel_index: str
    pypi_extra_indexes: list[str]
    file_handlers: dict
    excule_dependencies: list[str]
    package_data_dirs: dict
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def download_wheels(self, platform: str) -> list[str]: ...
    def update_pe_resources(self, appname, runtime) -> None: ...
    def bundle_macos_app(self, bulddir: str) -> None: ...
    def build_runtimes(self, platform: str, use_wheels: bool) -> None: ...
    def add_dependency(self, name: str, target_dir: str, search_path, referenced_by: object) -> None: ...
    def copy(self, source_path: str, target_path: str) -> None: ...
    def copy_with_dependencies(self, source_path: str, target_path: str, search_path) -> None: ...
    def copy_dependencies(self, target_path, target_dir, search_path, referenced_by: object) -> None: ...
    @overload
    def expand_path(self, path: str, platform: str) -> str: ...
    @overload
    def expand_path(self, path: None, platform: str) -> None: ...

class bdist_apps(Command):
    DEFAULT_INSTALLERS: ClassVar[dict[str, list[str]]]
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    installers: dict
    dist_dir: str
    skip_build: bool
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def create_zip(self, basename: str, build_dir: str) -> None: ...
    def create_tarball(self, basename: str, build_dir: str, tar_compression: str) -> None: ...
    def create_nsis(self, basename: object, build_dir: str, is_64bit: bool) -> None: ...
    def run(self) -> None: ...
