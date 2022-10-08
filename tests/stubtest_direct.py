import subprocess
import sys
from pathlib import Path


def main() -> int:
    allowlists = [Path('allowlists', 'direct.txt')]
    version_allowlist = Path(
        'allowlists',
        f'direct-py{sys.version_info.major}{sys.version_info.minor}.txt'
    )
    platform_allowlist = Path('allowlists', f'direct-{sys.platform}.txt')
    if version_allowlist.exists():
        allowlists.append(version_allowlist)
    if platform_allowlist.exists():
        allowlists.append(platform_allowlist)
    src_dir = Path('..', 'src', 'direct-stubs')
    modules = (p.stem for p in src_dir.glob('*'))
    dont_check = {
        '__init__',
        'directbase',
        'directutil',
        'p3d',
    }
    cmd = [
        sys.executable,
        '-O',
        '-m',
        'mypy.stubtest',
        *('direct.' + m for m in modules if m not in dont_check),
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
