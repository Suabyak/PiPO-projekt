from abc import (ABC, abstractmethod)
from object import Object


class Scene(ABC):
    @abstractmethod
    def __init__(self):
        self.__objects = dict()

    def addObject(self, obj):
        if not issubclass(obj.__class__, Object):
            print("Nie da się dodać do sceny "
                  "obiektu nie dziedziczącego z Object.")
            exit(1)
        self.__objects[obj.getId()] = obj

    def getObjects(self):
        return self.__objects.values()
