__all__ = ['DWBPackageInstaller']

from direct.gui.DirectWaitBar import DirectWaitBar
from panda3d.core import NodePath

from .AppRunner import AppRunner
from .PackageInstaller import PackageInstaller

class DWBPackageInstaller(DirectWaitBar, PackageInstaller):
    def __init__(self, appRunner: AppRunner, parent: NodePath | None = ..., **kw) -> None: ...
