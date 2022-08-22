from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .NonPhysicsWalker import NonPhysicsWalker

class GhostWalker(NonPhysicsWalker):
    notify: ClassVar[Notifier]
    slideName: ClassVar[str]
