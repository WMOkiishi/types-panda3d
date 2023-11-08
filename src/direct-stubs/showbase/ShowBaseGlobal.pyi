__all__: list[str] = []

from typing import TypeVar
from typing_extensions import deprecated

from direct.tkpanels.Inspector import InspectorWindow
from panda3d.core import (
    ClockObject,
    ConfigPageManager,
    ConfigVariableManager,
    NodePath,
    PandaNode,
    PandaSystem,
    PGTop,
    VirtualFileSystem,
    ostream as ostream_type,
)

from .ShowBase import ShowBase

_T = TypeVar('_T')

__dev__: bool
vfs: VirtualFileSystem
ostream: ostream_type
globalClock: ClockObject
cpMgr: ConfigPageManager
cvMgr: ConfigVariableManager
pandaSystem: PandaSystem
render2d: NodePath[PandaNode]
aspect2d: NodePath[PGTop]
hidden: NodePath[PandaNode]
base: ShowBase  # only exists once an instance of ShowBase is created

@deprecated('run() is deprecated, use base.run() instead')
def run() -> None: ...
def inspect(anObject: _T) -> InspectorWindow[_T]: ...
