import pygame
from Utils.eventOperator import EventOperator
from Renderer.renderer import Renderer
from os import listdir


class Main:
    def __init__(self):
        pygame.init()  # Inicjalizacja pygame
        self.__TITLE = "Strażak Bam-Bam"
        self.__SCREEN_SIZE = (800, 640)

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

    def loadScenes(self):
        scenes = dict()

        for dictionary in listdir("Data\\Scenes"):
            for scene in listdir(f"Data\\Scenes\\{dictionary}"):
                if ".py" in scene:
                    scene = scene.replace(".py", "")
                    exec(
                        f"from Data.Scenes.{dictionary}.{scene} import {dictionary}")
                    exec(
                        f"scenes[{dictionary}.__name__] = {dictionary}(self)")

        return scenes

    def setActiveScene(self, scene):
        self.__activeScene = scene

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
                obj.getComponent("Event").run("Click")

    def quit(self, event):
        """Zakończenie działania programu."""
        self.__running = False


if __name__ == "__main__":
    Main()
