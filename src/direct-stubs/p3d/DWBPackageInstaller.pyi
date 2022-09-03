__all__ = ['DWBPackageInstaller']

from panda3d.core import NodePath
from ..gui.DirectWaitBar import DirectWaitBar
from .AppRunner import AppRunner
from .PackageInstaller import PackageInstaller

class DWBPackageInstaller(DirectWaitBar, PackageInstaller):
    def __init__(self, appRunner: AppRunner, parent: NodePath | None = None, **kw) -> None: ...
