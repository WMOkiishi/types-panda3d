from typing_extensions import Unpack

from panda3d.core import NodePath

from ._typing import ButtonKeywords, MaybeImageOrSequence
from .DirectButton import DirectButton

class DirectCheckBox(DirectButton):
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        uncheckedImage: MaybeImageOrSequence = None,
        checkedImage: MaybeImageOrSequence = None,
        isChecked: bool = False,
        **kw: Unpack[ButtonKeywords],
    ) -> None: ...
