from pygame import Surface
from Renderer.Objects.Components.component import Component
from Utils import maths


class Rect(Component):
    def __init__(self, size, color, origin=(0, 0)):
        self.__size = size
        self.__surface = Surface(self.__size)
        self.__surface.fill(color)
        self.__origin = maths.Vector2(origin)

    def getOrigin(self):
        return self.__origin

    def getSize(self):
        return self.__size

    def render(self):
        return self.__surface, self.__origin

    def isRenderable(self):
        return True