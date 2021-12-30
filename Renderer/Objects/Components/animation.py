from Renderer.Objects.Components.component import Component
from abc import ABC, abstractmethod
from log import Log


class Animation(Component, ABC):
    def __init__(self, time, active=False):
        self.__time = time
        self.__clock = 0
        if not isinstance(active, bool):
            raise Exception(
                "Value of action has to be of "
                f"boolean type not {active.__class__.__name__}.")
        self.__active = active

    def tick(self):
        self.__clock += 1
        self.takeEffect()
        if self.__clock >= self.__time:
            self.finish()

    def getClock(self):
        return float(self.__clock)

    def getTime(self):
        return float(self.__time)

    def activate(self):
        self.reset()
        self.__active = True
        Log.executionLog(f"Animation \"{self.getType()}\" of "
                         f"Object \"{self.getParent().getId()}\" activated.")

    def isActive(self):
        return self.__active

    def reset(self):
        self.__clock = 0
        self.__active = False

    def finish(self):
        self.reset()

    @abstractmethod
    def takeEffect(self):
        pass
