import subprocess
import sys
from pathlib import Path


def main() -> int:
    allowlist = Path('allowlists', 'direct.txt')
    src_dir = Path('..', 'src', 'direct-stubs')
    modules = (p.stem for p in src_dir.glob('*'))
    dont_check = {
        '__init__',
        'directbase',
        'directutil',
        'leveleditor',
        'p3d',
        'tkpanels',
        'tkwidgets',
        'wxwidgets',
    }
    cmd = [
        sys.executable,
        '-O',
        '-m',
        'mypy.stubtest',
        *('direct.' + m for m in modules if m not in dont_check),
        '--allowlist',
        str(allowlist),
    ]
    try:
        print(' '.join(cmd), file=sys.stderr)
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        return e.returncode
    return 0


if __name__ == '__main__':
    sys.exit(main())
