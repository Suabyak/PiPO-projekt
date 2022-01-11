from Renderer.Objects.Components.component import Component
from Renderer.colors import colors
from pygame import font as Font
from Utils import maths


class Text(Component):
    """Odpowiada za renderowanie tekstu na ekranie,
    oraz przechowuje utworzone czcionki."""
    __font = dict()

    def __init__(self, text, size, color=(255, 255, 255),
                 origin=(0, 0)):
        self.__text = text
        self.__size = size
        if isinstance(color, str):
            color = colors[color]
        self.__color = color
        self.__origin = maths.Vector2(origin)
        if self.__size not in Text.__font.keys():
            """Ten mały trik sprawia że kilka komponentów Text może
            korzystać z tej samej czcionki,
            zamiast tworzyć kilka obiektów czcionki."""
            Text.__font[self.__size] = Font.Font(
                "Data\\Poppins-Light.ttf", size)

    def render(self, text=None, color=None):
        if not color:
            color = self.__color
        if not text:
            text = self.__text
        return (Text.getFont(self.__size).render(text, 0, color),
                self.__origin)

    def isRenderable(self):
        return True

    def getSize(self):
        return self.render()[0].get_size()

    def getFontSize(self):
        return self.__size

    def getOrigin(self):
        return self.__origin

    def getText(self):
        return self.__text

    def getColor(self):
        return self.__color

    def getFont(size):
        if size in Text.__font.keys():
            return Text.__font[size]
        raise Exception(f"Nie ma czcionki o wielkości {size}")

    def setText(self, text):
        self.__text = text
