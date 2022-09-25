import subprocess
import sys
from pathlib import Path


def main() -> int:
    allowlists = [Path('allowlists', 'panda3d.txt')]
    if sys.platform != 'win32':
        allowlists.append(Path('allowlists', 'panda3d-unix.txt'))
    cmd = [
        sys.executable,
        '-m',
        'mypy.stubtest',
        'panda3d',
    ]
    for allowlist in allowlists:
        cmd += [
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
