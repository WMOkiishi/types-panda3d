from collections.abc import Sequence
from typing import Any
from typing_extensions import Final, Literal, TypedDict

from direct.showbase.Messenger import Messenger

from .ClientRepository import ClientRepository

MESSAGE_TYPES: Final[
    tuple[
        Literal['avatarOnline'], Literal['avatarOffline'], Literal['create'], Literal['needUberdogCreates'], Literal['transferDo']
    ]
]

class _message_strings(TypedDict):
    avatarOnline: Literal[1]
    avatarOffline: Literal[2]
    create: Literal[3]
    needUberdogCreates: Literal[4]
    transferDo: Literal[5]

MESSAGE_STRINGS: Final[_message_strings]

class NetMessenger(Messenger):
    air: ClientRepository
    channels: Sequence[int]
    def __init__(self, air: ClientRepository, channels: Sequence[int]) -> None: ...
    def send(self, message: str, sentArgs: Any = ...) -> None: ...  # type: ignore[override]
    def handle(self, pickleData: bytes) -> None: ...
