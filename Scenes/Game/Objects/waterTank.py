from Renderer.Objects.object import Object
from Renderer.Objects.Components.rect import Rect
from pygame import Surface


class WaterTank(Object):
    def __init__(self, screenSize):
        super().__init__("WaterTank", (30, screenSize[1]-30))
        self.__size = (50, 150)
        self.addComponent(Rect(self.__size, (31, 31, 31), (0, 1)))

    def isRenderable(self):
        return True

    def render(self):
        surface, origin = self.getComponent("Rect").render()
        surfaceSize = surface.get_size()
        position = self.getComponent("Transform").getPosition()
        renderPosition = (position[0]-surfaceSize[0]*(origin.x),
                          position[1]-surfaceSize[1]*(origin.y))
        waterLevel = int((1-Object.get(
            "WaterCannon").getWaterLevel())*self.__size[1])
        if waterLevel > self.__size[1]:
            waterLevel = self.__size[1]
        waterSurface = Surface((self.__size[0]-10, waterLevel-10))
        waterSurface.fill((5, 160, 250))
        surface.blit(waterSurface, (5, 5+self.__size[1]-waterLevel))
        return surface, renderPosition
