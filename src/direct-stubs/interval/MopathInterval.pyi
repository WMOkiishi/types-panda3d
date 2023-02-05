__all__ = ['MopathInterval']

from typing import ClassVar
from typing_extensions import Literal

from direct.directutil.Mopath import Mopath
from panda3d.core import NodePath

from .LerpInterval import LerpFunctionInterval

class MopathInterval(LerpFunctionInterval):
    mopathNum: ClassVar[int]
    mopath: Mopath
    node: NodePath
    def __init__(
        self,
        mopath: Mopath,
        node: NodePath,
        fromT: float = 0,
        toT: float | None = None,
        duration: float | None = None,
        blendType: Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend'] = 'noBlend',
        name: str | None = None,
    ) -> None: ...
    def destroy(self) -> None: ...
