from typing import ClassVar, TypeVar
from typing_extensions import Literal, Protocol, TypeAlias

from panda3d.core import NodePath
from panda3d.physics import BaseForce, ForceNode
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

_T_contra = TypeVar("_T_contra", contravariant=True)

_OldBool: TypeAlias = Literal[0, 1]

class _SupportsWrite(Protocol[_T_contra]):
    def write(self, s: _T_contra, /) -> object: ...

class ForceGroup(DirectObject):
    notify: ClassVar[Notifier]
    id: ClassVar[int]
    node: ForceGroup
    nodePath: NodePath[ForceNode]
    fEnabled: bool | _OldBool
    particleEffect = ...
    def __init__(self, name: str | None = None) -> None: ...
    def cleanup(self) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def is_enabled(self) -> bool | _OldBool: ...
    def addForce(self, force: BaseForce) -> None: ...
    def removeForce(self, force: BaseForce | int) -> None: ...
    def get_name(self) -> str: ...
    def get_node(self) -> ForceGroup: ...
    def get_node_path(self) -> NodePath[ForceNode]: ...
    def __getitem__(self, index: int) -> BaseForce: ...
    def __len__(self) -> int: ...
    def as_list(self) -> list[BaseForce]: ...
    def print_params(self, file: _SupportsWrite[str] = ..., targ: str = 'self') -> None: ...
    isEnabled = is_enabled
    getNode = get_node
    getNodePath = get_node_path
    asList = as_list
    printParams = print_params
