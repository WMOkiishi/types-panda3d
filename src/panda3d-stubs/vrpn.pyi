from typing import Any, ClassVar
from panda3d.core import ClientBase, TypeHandle, ostream

class VrpnClient(ClientBase):
    """A specific ClientBase that connects to a VRPN server and records
    information on the connected VRPN devices.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, server_name: str) -> None: ...
    def get_server_name(self) -> str:
        """Returns the name of the server as passed to the VrpnClient constructor."""
        ...
    def is_valid(self) -> bool:
        """Returns true if everything seems to be kosher with the server (even if
        there is no connection), or false otherwise.
        """
        ...
    def is_connected(self) -> bool:
        """Returns true if the connection is established successfully, false
        otherwise.
        """
        ...
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a list of the active devices that the VrpnClient is currently
        polling each frame.
        """
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getServerName = get_server_name
    isValid = is_valid
    isConnected = is_connected
    getClassType = get_class_type
