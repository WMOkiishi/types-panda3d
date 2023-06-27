from _typeshed import StrOrBytesPath
from collections.abc import Collection, Iterable, Sequence
from typing import Any, ClassVar, Literal

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from panda3d.core import (
    Connection,
    ConnectionWriter,
    DatagramIterator,
    NetAddress,
    NetDatagram,
    QueuedConnectionListener,
    QueuedConnectionManager,
    QueuedConnectionReader,
    UniqueIdAllocator,
)
from panda3d.direct import DCClass, DCFile

from .DistributedObjectBase import DistributedObjectBase

class ServerRepository:
    notify: ClassVar[Notifier]

    class Client:
        connection: Connection
        netAddress: NetAddress
        doIdBase: int
        explicitInterestZoneIds: set[int]
        currentInterestZoneIds: set[int]
        objectsByDoId: dict[int, DistributedObjectBase]
        objectsByZoneId: dict[int, DistributedObjectBase]
        def __init__(self, connection: Connection, netAddress: NetDatagram, doIdBase: int) -> None: ...

    class Object:
        doId: int
        zoneId: int
        dclass: DCClass
        def __init__(self, doId: int, zoneId: int, dclass: DCClass) -> None: ...

    qcm: QueuedConnectionManager
    qcl: QueuedConnectionListener
    qcr: QueuedConnectionReader
    cw: ConnectionWriter
    tcpRendezvous: Connection
    needsFlush: set[ServerRepository.Client]
    clientsByConnection: dict[Connection, ServerRepository.Client]
    clientsByDoIdBase: dict[int, ServerRepository.Client]
    zonesToClients: dict[int, set[ServerRepository.Client]]
    objectsByZoneId: dict[int, set[DistributedObjectBase]]
    doIdRange: int
    idAllocator: UniqueIdAllocator
    dcFile: DCFile
    dcSuffix: str
    def __init__(
        self,
        tcpPort: int,
        serverAddress: str | None = None,
        udpPort: Unused = None,
        dcFileNames: Iterable[StrOrBytesPath] | None = None,
        threadedNet: bool | None = None,
    ) -> None: ...
    def flushTask(self, task: Unused) -> Literal[2]: ...
    def setTcpHeaderSize(self, headerSize: int) -> None: ...
    def getTcpHeaderSize(self) -> int: ...
    def importModule(self, dcImports: dict[str, Any], moduleName: str, importSymbols: Sequence[str]) -> None: ...
    def readDCFile(self, dcFileNames: Iterable[StrOrBytesPath] | None = None) -> None: ...
    def listenerPoll(self, task: Unused) -> Literal[1]: ...
    def readerPollUntilEmpty(self, task: Unused) -> Literal[1]: ...
    def readerPollOnce(self) -> bool: ...
    def handleDatagram(self, datagram: NetDatagram) -> None: ...
    def handleMessageType(self, msgType: object, di: Unused) -> None: ...
    def handleClientCreateObject(self, datagram: NetDatagram, dgi: DatagramIterator) -> None: ...
    def handleClientObjectUpdateField(self, datagram: NetDatagram, dgi: DatagramIterator, targeted: bool = False) -> None: ...
    def getDoIdBase(self, doId: int) -> int: ...
    def handleClientDeleteObject(self, datagram: NetDatagram, doId: int) -> None: ...
    def handleClientObjectSetZone(self, datagram: NetDatagram, dgi: DatagramIterator) -> None: ...
    def setObjectZone(self, owner: ServerRepository, object: DistributedObjectBase, zoneId: int) -> None: ...
    def sendDoIdRange(self, client: ServerRepository.Client) -> None: ...
    def handleClientDisconnect(self, client: ServerRepository.Client) -> None: ...
    def handleClientSetInterest(self, client: ServerRepository.Client, dgi: DatagramIterator) -> None: ...
    def updateClientInterestZones(self, client: ServerRepository.Client) -> None: ...
    def clientHardDisconnectTask(self, task: Unused) -> Literal[1]: ...
    def sendToZoneExcept(
        self, zoneId: int, datagram: NetDatagram, exceptionList: Collection[ServerRepository.Client]
    ) -> None: ...
    def sendToAllExcept(self, datagram: NetDatagram, exceptionList: Collection[ServerRepository.Client]) -> None: ...
