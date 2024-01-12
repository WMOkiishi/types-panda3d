from __future__ import annotations

import sys
from collections.abc import Container, Sequence
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from importlib.util import spec_from_loader
from pathlib import Path
from types import ModuleType

import attrs
import mypy.stubtest


@attrs.define
class NonExecutingLoader(Loader):
    """This `Loader` skips execution of the module's contents."""

    def exec_module(self, module: ModuleType) -> None:
        pass


@attrs.define
class PathFilter(MetaPathFinder):
    """This `MetaPathFinder` can be used to prevent
    certain scripts from running when loaded.
    """
    modules: Container[str]

    def find_spec(
            self,
            fullname: str,
            path: Sequence[str] | None,
            target: ModuleType | None = None) -> ModuleSpec | None:
        if fullname in self.modules:
            return spec_from_loader(fullname, NonExecutingLoader())
        else:
            return None


def main() -> int:
    root = Path(__file__).parent.parent
    allowlist_names = [
        'common',
        f'py{sys.version_info.major}{sys.version_info.minor}',
        sys.platform,
        f'{sys.platform}-py{sys.version_info.major}{sys.version_info.minor}',
    ]
    args = [
        'panda3d', 'direct',
        '--mypy-config-file',
        str(root / 'pyproject.toml'),
    ]
    for name in allowlist_names:
        path = root / 'tests' / 'allowlists' / f'{name}.txt'
        if path.exists():
            args += ['--allowlist', str(path)]
            print('Using allowlist', repr(str(path)), file=sys.stderr)
    # These scripts run on import, interfering with the tests
    sys.meta_path.insert(2, PathFilter({
        'direct.directbase.ThreeUpStart',
        'direct.directbase.TestStart',
        'direct.directutil.MemoryLeakHelpers',
    }))
    sys.argv += args
    return mypy.stubtest.main()


if __name__ == '__main__':
    sys.exit(main())
