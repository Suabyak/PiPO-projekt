from Renderer.Objects.Components.component import Component
from pygame import font as Font
from Utils import maths


class Label(Component):
    """Odpowiada za renderowanie tekstu na ekranie,
    oraz przechowuje utworzone czcionki."""
    __font = dict()

    def __init__(self, text, size, color=(255, 255, 255), origin=maths.Vector2(0, 0)):
        self.__text = text
        self.__size = size
        self.__color = color
        self.__origin = origin
        if self.__size not in Label.__font.keys():
            """Ten mały trik sprawia że kilka komponentów Label może
            korzystać z tej samej czcionki,
            zamiast tworzyć kilka obiektów czcionki."""
            Label.__font[self.__size] = Font.Font(
                "Data\\Poppins-Light.ttf", size)

    def render(self):
        return Label.__font[self.__size].render(self.__text, 0, self.__color), self.__origin

    def isRenderable(self):
        return True
