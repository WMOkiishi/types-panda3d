__all__ = ['PEFile']

from _typeshed import ReadableBuffer, StrOrBytesPath, SupportsRead, SupportsWrite, WriteableBuffer
from collections.abc import Generator, Iterator, Sequence
from typing import ClassVar, IO, NamedTuple, overload
from typing_extensions import Literal, TypeAlias

from ..p3d.DeploymentTools import Icon

_OpenFile: TypeAlias = StrOrBytesPath | int

class RVASize(NamedTuple):
    addr: int
    size: int

class impdirtab(NamedTuple):
    lookup: int
    timdat : int
    forward: int
    name: int
    impaddr: int

class expdirtab(NamedTuple):
    flags: int
    timdat: int
    majver: int
    minver: int
    name: int
    ordinal_base: int
    nentries: int
    nnames: int
    entries: int
    names: int
    ordinals: int

class Section:
    name: bytes
    vaddr: int
    vsize: int
    offset: int
    size: int
    flags: int
    modified: bool
    def read_header(self, fp: SupportsRead[bytes]) -> None: ...
    def write_header(self, fp: SupportsWrite[bytes]) -> None: ...
    def __gt__(self, other: Section) -> bool: ...
    def __lt__(self, other: Section) -> bool: ...

class DataResource:
    cursor: ClassVar[int]
    bitmap: ClassVar[int]
    icon: ClassVar[int]
    menu: ClassVar[int]
    dialog: ClassVar[int]
    string: ClassVar[int]
    font_directory: ClassVar[int]
    font: ClassVar[int]
    accelerator: ClassVar[int]
    rcdata: ClassVar[int]
    message_table: ClassVar[int]
    cursor_group: ClassVar[int]
    icon_group: ClassVar[int]
    version: ClassVar[int]
    dlg_include: ClassVar[int]
    plug_play: ClassVar[int]
    vxd: ClassVar[int]
    animated_cursor: ClassVar[int]
    animated_icon: ClassVar[int]
    html: ClassVar[int]
    manifest: ClassVar[int]
    data: bytes | None
    code_page: int
    def __init__(self) -> None: ...
    @property
    def encoding(self) -> str: ...
    def get_data(self) -> bytes | None: ...
    def get_text(self, errors: str = ...) -> str: ...

class IconGroupResource:
    class Icon(NamedTuple):
        width: int
        height: int
        planes: int
        bpp: int
        size: int
        id: int
    code_page: ClassVar[int]
    type: ClassVar[int]
    icons: list[IconGroupResource.Icon]
    def __init__(self) -> None: ...
    def add_icon(self, width: int, height: int, planes: int, bpp: int, size: int, id: int) -> None: ...
    def get_data(self) -> bytearray: ...
    def unpack_from(self, data: ReadableBuffer, offs: int = ...) -> None: ...

class VersionInfoResource:
    code_page: ClassVar[int]
    type: ClassVar[int]
    string_info: dict[str, dict[str, str]]
    var_info: dict[str, bytearray]
    signature: int
    struct_version: int
    file_version: tuple[int, int, int, int]
    product_version: tuple[int, int, int, int]
    file_flags_mask: int
    file_flags: int
    file_os: int
    file_type: int
    file_subtype: int
    file_data: tuple[int, int]
    def __init__(self) -> None: ...
    def get_data(self) -> bytearray: ...
    def unpack_from(self, data: ReadableBuffer) -> None: ...
    @overload
    def __getitem__(self, key: Literal['StringFileInfo']) -> dict[str, dict[str, str]]: ...
    @overload
    def __getitem__(self, key: Literal['VarFileInfo']) -> dict[str, bytearray]: ...
    def __contains__(self, key: object) -> bool: ...

class ResourceTable:
    flags: int
    timdat: int
    version: tuple[int, int]
    def __init__(self, ident: tuple[int | str, ...] = ...) -> None: ...
    def __getitem__(self, key: int | str) -> ResourceTable: ...
    def __setitem__(self, key: int | str, value: ResourceTable) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int | str]: ...
    def items(self) -> list[tuple[int | str, ResourceTable | None]]: ...
    def count_resources(self) -> int: ...
    def get_nested_tables(self) -> Generator[ResourceTable, None, None]: ...
    def pack_header(self, data: WriteableBuffer, offs: int) -> None: ...
    def unpack_from(self, mem: ReadableBuffer, addr: int = ..., offs: int = ...) -> None: ...

class PEFile:
    machine: int
    code_size: int
    initialized_size: int
    uninitialized_size: int
    section_alignment: int
    file_alignment: int
    image_size: int
    header_size: int
    rva_offset: int
    exp_rva: RVASize
    imp_rva: RVASize
    res_rva: RVASize
    sections: list[Section]
    vmem: bytearray
    imports: tuple[str, ...]
    resources: ResourceTable
    def open(self, fn: _OpenFile, mode: str = ...) -> None: ...
    def close(self) -> None: ...
    def read(self, fp: IO[bytes]) -> None: ...
    def get_export_address(self, symbol_name: str | bytes) -> int | None: ...
    def get_address_offset(self, addr: int) -> int | None: ...
    def get_address_section(self, addr: int) -> Section | None: ...
    def add_icon(self, icon: Icon, ordinal: int = ...) -> None: ...
    def add_section(self, name: bytes | str, flags: int, data: Sequence[int]) -> Section: ...
    def add_version_info(
        self,
        file_ver: tuple[int, int, int, int],
        product_ver: tuple[int, int, int, int],
        data: dict[str, str],
        lang: int = ...,
        codepage: int = ...,
    ) -> None: ...
    def add_resource_section(self) -> None: ...
    def write_changes(self) -> None: ...
