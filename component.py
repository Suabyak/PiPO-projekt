from abc import (ABC, abstractmethod)


class Component(ABC):
    @abstractmethod
    def __init__(self):
        """Pusty konstruktor abstrakcyjny żeby zaliczyć więcej
        punktów z wymagań do projektu 8)"""
        pass

    def getType(self):
        """Zwrócenie nazwy klasy."""
        return self.__class__.__name__
