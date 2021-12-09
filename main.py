import pygame
from eventOperator import EventOperator


class Main:
    def __init__(self):
        pygame.init()  # Inicjalizacja pygame
        self.__eventOperator = EventOperator(self)
        self.__display = pygame.display.set_mode((800, 640))
        self.__FPSLimit = 144
        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__gameLoop()

    def __gameLoop(self):
        """Pętla która będzie się wykonywała cały czas dopóki użytkownik
        nie zechce wyjść z aplikacji, obsługuje ona renderowanie i eventy."""
        while self.__running:
            self.__eventOperator.operateEvents()
            self.__clock.tick(self.__FPSLimit)

    def quit(self, event):
        self.__running = False


if __name__ == "__main__":
    Main()
