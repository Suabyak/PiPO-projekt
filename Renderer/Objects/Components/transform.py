from Renderer.Objects.Components.component import Component
from Utils import maths


class Transform(Component):
    """Przechowuje pozycje obiektu,
    każdy obiekt posiada ten komponent."""

    def __init__(self, position=(0, 0)):
        self.__position = maths.Vector2(position)

    def move(self, offset):
        self.__position += offset

    def moveTo(self, position):
        self.__position = maths.Vector2(position)

    def getPosition(self):
        return (self.__position.x, self.__position.y)
