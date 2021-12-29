from Renderer.Objects.Components.component import Component
from log import Log


class AnimationSequence(Component):
    def __init__(self, sequence=list(), running=False):
        self.__activeAnimation = 0
        self.__running = running
        self.__sequence = sequence

    def start(self):
        self.__running = True
        self.__activeAnimation = 0
        Log.executionLog(
            f"AnimationSequence of Object \"{self.getParent().getId()}\" started.")
        self.getActiveAnimation().activate()

    def isRunning(self):
        return self.__running

    def getActiveAnimation(self):
        return self.__sequence[self.__activeAnimation]

    def tick(self):
        self.getActiveAnimation().tick()
        if not self.getActiveAnimation().isActive():
            self.__activeAnimation += 1
            if self.__activeAnimation == len(self.__sequence):
                self.__running = False
                self.__activeAnimation = 0
                Log.executionLog(
                    f"AnimationSequence of object {self.getParent().getId()} finished.")
                return
            self.getActiveAnimation().activate()

    def add(self, animation):
        animation.getParent = self.getParent
        self.__sequence.append(animation)
