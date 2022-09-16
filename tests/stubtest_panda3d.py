import subprocess
import sys
from pathlib import Path


def main() -> int:
    allowlist = Path('allowlists', 'panda3d.txt')
    cmd = [
        sys.executable,
        '-m',
        'mypy.stubtest',
        'panda3d',
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
