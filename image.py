from pygame import image
from component import Component


class Image(Component):
    """Służy do wczytywania obrazów."""

    def __init__(self, path):
        """Wczytanie zdjęcia w konstruktorze.
        Wystarczy wpisać nazwę pliku, bez rozszerzenia
        oraz bez folderu."""
        self.__surface = image.load(f"data\\{path}.png")

    def getSurface(self):
        return self.__surface

    def getDimensions(self):
        return self.__surface.get_size()
