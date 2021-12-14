import pygame
from Utils.eventOperator import EventOperator
from Renderer.renderer import Renderer
from Renderer.Scenes.mainMenu import MainMenu


class Main:
    def __init__(self):
        pygame.init()  # Inicjalizacja pygame
        self.__eventOperator = EventOperator(self)
        self.__renderer = Renderer((800, 640))
        self.__scenes = [MainMenu()]
        self.__activeScene = 0
        self.__running = True
        self.__gameLoop()

    def __gameLoop(self):
        """Pętla która będzie się wykonywała cały czas dopóki użytkownik
        nie zechce wyjść z aplikacji, obsługuje ona renderowanie i eventy."""
        while self.__running:
            self.__eventOperator.operateEvents()
            self.__renderer.render(self.getActiveScene())

    def getActiveScene(self):
        return self.__scenes[self.__activeScene]

    def quit(self, event):
        """Zakończenie działania programu."""
        self.__running = False


if __name__ == "__main__":
    Main()
