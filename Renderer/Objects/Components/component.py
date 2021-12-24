from abc import (ABC, abstractmethod)


class Component(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getType(self):
        """Zwrócenie nazwy klasy."""
        return self.__class__.__name__

    def getParent(self):
        return self.__parent

    def setParent(self, parent):
        self.__parent = parent

    def isRenderable(self):
        return False
