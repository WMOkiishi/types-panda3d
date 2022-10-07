from typing_extensions import Literal

USE_DISK: Literal[0x01]
ChunkSize: Literal[100]
FilePattern: Literal['largeBlob.%s']

def getLargeBlobPath() -> str: ...
