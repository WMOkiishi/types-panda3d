import argparse
import logging
import os.path
from typing import cast

from .main import main


def cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='src',
                        help='the output directory for the stubs')
    parser.add_argument('-d', '--database',
                        help='the directory containing the database files')
    parser.add_argument('-p', '--package_name', default='panda3d',
                        help='the name of the package being examined')
    parser.add_argument('-l', '--log', default=os.path.join('idbstubs', 'log.log'),
                        help='the file to write the log to')
    parser.add_argument('-v', '--verbosity', action='count', default=0,
                        help='increase verbosity (up to 4)')
    args = parser.parse_args()

    package_name = cast(str, args.package_name)
    output_dir = cast(str, args.output)
    database_dir = cast(str | None, args.database)
    log_path = cast(str, args.log)
    log_level = 10 * (5 - cast(int, args.verbosity))

    logger = logging.getLogger('idbstubs')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_path, mode='w')
    file_handler.setFormatter(
        logging.Formatter('%(levelname)s - %(name)s - %(message)s')
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter('%(levelname)s: %(message)s')
    )
    stream_handler.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    main(database_dir, output_dir,
         package_name=package_name)


if __name__ == '__main__':
    cli()
