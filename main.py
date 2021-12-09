import pygame
from eventOperator import EventOperator
from renderer import Renderer


class Main:
    def __init__(self):
        pygame.init()  # Inicjalizacja pygame
        self.__eventOperator = EventOperator(self)
        self.__renderer = Renderer((800, 640))
        self.__running = True
        self.__gameLoop()

    def __gameLoop(self):
        """Pętla która będzie się wykonywała cały czas dopóki użytkownik
        nie zechce wyjść z aplikacji, obsługuje ona renderowanie i eventy."""
        while self.__running:
            self.__eventOperator.operateEvents()
            self.__renderer.render()

    def quit(self, event):
        """Chyba nie muszę tłumaczyć :|"""
        self.__running = False


if __name__ == "__main__":
    Main()
