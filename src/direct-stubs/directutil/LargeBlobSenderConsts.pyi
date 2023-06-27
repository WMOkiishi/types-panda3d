from typing import Final

USE_DISK: Final = 0x01
ChunkSize: Final = 100
FilePattern: Final = 'largeBlob.%s'

def getLargeBlobPath() -> str: ...
