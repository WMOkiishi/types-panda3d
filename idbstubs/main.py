import logging
from os import PathLike
from typing import Final

from .construction import make_file_reps
from .idbutil import load_interrogate_database
from .processors import process_dependencies, process_files
from .reps import File
from .typedata import load_data

_logger: Final = logging.getLogger(__name__)


def main(
        input_dir: PathLike[str] | str | None = None,
        output_dir: PathLike[str] | str = '.',
        *, package_name: str = 'panda3d') -> None:
    load_interrogate_database(input_dir)
    _logger.debug('Gathering type information')
    load_data()
    files = make_file_reps(package_name)
    process_files(files)
    for file in files:
        write_file_stubs(file, output_dir)


def write_file_stubs(file: File, output_dir: PathLike[str] | str = '.') -> None:
    path = output_dir / file.stub_path().with_suffix('.pyi')
    _logger.debug(f'Writing file {path.resolve()}')
    process_dependencies(file)
    file.sort_items()
    for parent in reversed(path.parents):
        if not parent.exists():
            parent.mkdir()
    with path.open('w') as f:
        for line in file.lines():
            print(line, file=f)
