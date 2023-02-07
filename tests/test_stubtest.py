from __future__ import annotations

import sys
from collections.abc import Container, Sequence
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from importlib.util import spec_from_loader
from pathlib import Path
from types import ModuleType

import mypy.stubtest


class NonExecutingLoader(Loader):
    """This `Loader` skips execution of the module's contents."""
    __slots__ = ()

    def exec_module(self, module: ModuleType) -> None:
        pass


class PathFilter(MetaPathFinder):
    """This `MetaPathFinder` can be used to prevent
    certain scripts from running when loaded.
    """
    __slots__ = 'modules'
    modules: Container[str]

    def __init__(self, modules: Container[str]) -> None:
        self.modules = modules

    def find_spec(
            self,
            fullname: str,
            path: Sequence[str | bytes] | None,
            target: ModuleType | None = None) -> ModuleSpec | None:
        if fullname in self.modules:
            return spec_from_loader(fullname, NonExecutingLoader())
        else:
            return None


def prevent_running(names: Container[str], *, index: int = 2) -> None:
    """Prevent scripts with names in `names` from running when imported."""
    sys.meta_path.insert(index, PathFilter(names))


def main() -> int:
    allowlists = [Path('allowlists', 'common.txt')]
    version_allowlist = Path(
        'allowlists',
        f'py{sys.version_info.major}{sys.version_info.minor}.txt'
    )
    platform_allowlist = Path('allowlists', f'{sys.platform}.txt')
    if version_allowlist.exists():
        allowlists.append(version_allowlist)
    if platform_allowlist.exists():
        allowlists.append(platform_allowlist)
    args = ['panda3d', 'direct']
    for allowlist in allowlists:
        args += [
            '--allowlist',
            str(allowlist),
        ]
    print('Stubtest arguments:', ' '.join(args), file=sys.stderr)
    # These scripts run on import, interfering with the tests
    prevent_running({
        'direct.directbase.ThreeUpStart',
        'direct.directbase.TestStart',
        'direct.directutil.MemoryLeakHelpers',
    })
    sys.argv += args
    return mypy.stubtest.main()


if __name__ == '__main__':
    sys.exit(main())
