from _typeshed import StrOrBytesPath
from typing_extensions import Literal, TypeAlias
from panda3d.core import BamCacheRecord, ConfigVariableFilename, Filename, PandaNode
from panda3d.egg import EggData

_Filename: TypeAlias = Filename | ConfigVariableFilename | StrOrBytesPath
_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
def load_egg_file(filename: _Filename, cs: _CoordinateSystem = ..., record: BamCacheRecord = ...) -> PandaNode: ...
def load_egg_data(data: EggData, cs: _CoordinateSystem = ...) -> PandaNode: ...
def save_egg_file(filename: _Filename, node: PandaNode, cs: _CoordinateSystem = ...) -> bool: ...
def save_egg_data(data: EggData, node: PandaNode) -> bool: ...
loadEggFile = load_egg_file
loadEggData = load_egg_data
saveEggFile = save_egg_file
saveEggData = save_egg_data
