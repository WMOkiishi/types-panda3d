import logging
from os import PathLike
from pathlib import Path
from typing import Final

from .checks import check_module
from .construction import get_all_manifests, make_package_rep, with_alias
from .idbutil import load_interrogate_database
from .processors import process_dependencies
from .reps import Module, StubRep
from .typedata import load_data
from .util import flatten

_logger: Final = logging.getLogger(__name__)


def main(
        input_dir: PathLike[str] | str | None = None,
        output_dir: PathLike[str] | str = '.',
        *, package_name: str = 'panda3d',
        infer_optional: bool = True,
        ignore_coercion: bool = False) -> None:
    load_interrogate_database(input_dir)
    _logger.debug('Gathering type information')
    load_data()
    package = make_package_rep(
        package_name,
        infer_opt_params=infer_optional,
        ignore_coercion=ignore_coercion
    )
    for module in package:
        _logger.info(f'Writing stubs for {module}')
        if len(module.nested) > 1:
            init_nested: list[StubRep] = []
            if module.name == 'core':
                init_nested += flatten(with_alias(m) for m in get_all_manifests())
            module.nested['__init__'] = init_nested
        check_module(module)
        write_module_stubs(module, output_dir)
    (Path(output_dir) / f'{package.name}-stubs' / '__init__.pyi').write_text('')


def write_module_stubs(
        module: Module,
        output_dir: PathLike[str] | str = '.') -> None:
    for file in module:
        path = output_dir / file.stub_path().with_suffix('.pyi')
        _logger.debug(f'Writing file {path.resolve()}')
        if file.name == '__init__':
            file.imports |= {
                other: ['*']
                for other in module.nested
                if other != '__init__'
            }
        process_dependencies(file)
        file.sort_items()
        for parent in reversed(path.parents):
            if not parent.exists():
                parent.mkdir()
        with path.open('w') as f:
            for line in file.lines():
                print(line, file=f)
