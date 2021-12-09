from pygame import display as Display, time as Time


class Renderer:
    def __init__(self, resolution):
        self.__display = Display.set_mode(resolution)
        self.__clock = Time.Clock()
        self.__FPSLimit = 144

    def render(self):
        """Wyświetlanie wszystkich elementów na ekranie."""
        self.__clock.tick(self.__FPSLimit)
