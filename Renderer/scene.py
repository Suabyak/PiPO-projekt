from abc import (ABC, abstractmethod)
from Renderer.Objects.object import Object
from log import Log


class Scene(ABC):
    @abstractmethod
    def __init__(self, id, main):
        self.__id = id
        self.__main = main
        self.__objects = dict()
        Log.executionLog(f"Scene \"{self.__id}\" created.")

    def addObject(self, obj):
        if not issubclass(obj.__class__, Object):
            raise Exception("Nie da się dodać do sceny "
                            "obiektu nie dziedziczącego z Object.")
            Log.executionLog(
                f"\n[!] {obj.__class__} cannot be added to Scene \"{self.getId()}\".\n")
            exit(1)
        self.__objects[obj.getId()] = obj
        Log.executionLog(
            f"Object \"{obj.getId()}\" added to \"{self.getId()}\" Scene")

    def getId(self):
        return self.__id

    def getObjects(self):
        return self.__objects.values()

    def getObject(self, id):
        return self.__objects[id]

    def getMain(self):
        return self.__main

    def getScreenSize(self):
        return self.__main.getScreenSize()
