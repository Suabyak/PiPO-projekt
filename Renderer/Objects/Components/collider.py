from Renderer.Objects.Components.component import Component
from Utils import maths


class Collider(Component):
    """Komponent do sprawdzania kolizji obiektu."""

    def __init__(self, size, origin):
        self.__size = maths.Vector2(size)
        self.__origin = maths.Vector2(origin)

    def isOver(self, objPos, pos):
        boundaries = ((objPos[0]-self.__size.x*self.__origin.x,
                       objPos[1]-self.__size.y*self.__origin.y),
                      (objPos[0]+self.__size.x*(1-self.__origin.x),
                       objPos[1]+self.__size.y*(1-self.__origin.y)))
        xMin, xMax = maths.getMinAndMax(boundaries[0][0], boundaries[1][0])
        yMin, yMax = maths.getMinAndMax(boundaries[0][1], boundaries[1][1])
        return (maths.isBetween(xMin, xMax, pos[0])
                and maths.isBetween(yMin, yMax, pos[1]))

    def setSize(self, size):
        self.__size = maths.Vector2(size)
