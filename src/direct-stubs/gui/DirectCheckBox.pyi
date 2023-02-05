from typing import Any

from panda3d.core import NodePath

from .DirectButton import DirectButton

class DirectCheckBox(DirectButton):
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
