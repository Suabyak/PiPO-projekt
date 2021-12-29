import pygame
from Utils.eventOperator import EventOperator
from Renderer.renderer import Renderer
from Renderer.Objects.Components.animation import Animation
from Renderer.Objects.Components.animationSequence import AnimationSequence
from log import Log
from os import listdir, system
import traceback


class Main:
    def __init__(self):
        pygame.init()  # Inicjalizacja pygame
        self.__TITLE = "Strażak Bam-Bam"
        self.__SCREEN_SIZE = (800, 640)
        Log.executionLog(f"\n{'-'*50}")
        Log.executionLog(f"{self.__TITLE} started.")

        self.__eventOperator = EventOperator(self)
        self.__renderer = Renderer(self.__SCREEN_SIZE)
        pygame.display.set_caption(self.__TITLE)
        self.__scenes = self.loadScenes()
        self.__activeScene = None
        self.__running = True

        self.setActiveScene("MainMenu")
        self.__gameLoop()

    def __gameLoop(self):
        """Pętla która będzie się wykonywała cały czas dopóki użytkownik
        nie zechce wyjść z aplikacji, obsługuje ona renderowanie i eventy."""
        while self.__running:
            self.__eventOperator.operateEvents()
            self.__renderer.render(self.getActiveScene())
            self.tickAnimations(self.getActiveScene())

    def loadScenes(self):
        scenes = dict()

        for dictionary in listdir("Scenes"):
            for scene in listdir(f"Scenes\\{dictionary}"):
                if ".py" in scene:
                    scene = scene.replace(".py", "")
                    exec(
                        f"from Scenes.{dictionary}.{scene} import {dictionary}")
                    exec(
                        f"scenes[{dictionary}.__name__] = {dictionary}(self)")

        return scenes

    def setActiveScene(self, scene):
        self.__activeScene = scene
        Log.executionLog(f"Scene set to \"{scene}\".")

    def getActiveScene(self):
        return self.__scenes[self.__activeScene]

    def getScreenSize(self):
        return self.__SCREEN_SIZE

    def mouseClick(self, event):
        # pętla od tyłu (jak michael jackson i jego moonwalk)
        for obj in reversed(self.getActiveScene().getObjects()):
            if not obj.hasComponent("Collider"):
                continue
            collider = obj.getComponent("Collider")
            if collider.isOver(obj.getComponent(
                    "Transform").getPosition(), event.dict["pos"]):
                obj.getComponent("Event").run("Click", event)

    def tickAnimations(self, scene):
        for obj in scene.getObjects():
            for component in obj.getComponents().values():
                if ((issubclass(component.__class__, Animation) and component.isActive())
                        or (isinstance(component, AnimationSequence) and component.isRunning())):
                    component.tick()

    def quit(self, event):
        """Zakończenie działania programu."""
        self.__running = False
        Log.executionLog(f"{self.__TITLE} shat down.")


if __name__ == "__main__":
    try:
        Main()
    except Exception as e:
        Log.executionLog(e)
        Log.executionLog(traceback.format_exc())
        system("Logs\\execution_log.txt")
