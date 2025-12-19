__all__ = ['verify']

from panda3d.core import ConfigVariableBool

wantVerifyPdb: ConfigVariableBool

def verify(assertion: object) -> None: ...
