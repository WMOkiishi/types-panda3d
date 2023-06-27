from typing import Final

from ._dcparser import *
from ._deadrec import *
from ._distributed import *
from ._interval import *
from ._motiontrail import *
from ._showbase import *

Dtool_PyNativeInterface: Final = 1
def Dtool_BorrowThisReference(from_in, to_in) -> None: ...
