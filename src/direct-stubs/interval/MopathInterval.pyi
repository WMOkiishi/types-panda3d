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
        fromT: float = ...,
        toT: float | None = ...,
        duration: float | None = ...,
        blendType: Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend'] = ...,
        name: str | None = ...,
    ) -> None: ...
    def destroy(self) -> None: ...
