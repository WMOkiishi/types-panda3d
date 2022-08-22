from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .NonPhysicsWalker import NonPhysicsWalker

class SwimWalker(NonPhysicsWalker):
    notify: ClassVar[Notifier]
