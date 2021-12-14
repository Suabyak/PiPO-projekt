from Renderer.Objects.Components.component import Component
import Utils.maths as maths


class Transform(Component):
    def __init__(self, *position):
        self.__position = maths.Vector2(position)

    def move(self, offset):
        self.__position += offset

    def getPosition(self):
        return (self.__position.x, self.__position.y)
