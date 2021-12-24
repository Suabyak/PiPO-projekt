from pygame import image
from Renderer.Objects.Components.component import Component
from Utils import maths


class Image(Component):
    """Służy do wczytywania obrazów."""
    __images = dict()

    def __init__(self, path, origin=(0, 0)):
        """Wczytanie zdjęcia w konstruktorze.
        Wystarczy wpisać nazwę pliku, bez rozszerzenia
        oraz bez folderu."""
        self.__path = path
        self.__origin = maths.Vector2(origin)
        if self.__path not in Image.__images.keys():
            Image.__images[self.__path] = image.load(
                f"Data\\{self.__path}.png")

    def render(self):
        surf = Image.__images[self.__path]
        return surf, self.__origin

    def isRenderable(self):
        return True

    def getSize(self):
        return self.render().get_size()

    def getOrigin(self):
        return self.__origin
