from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image
from Scenes.Game.Objects.waterBall import WaterBall
from pygame import transform
from Utils.maths import sin, cos, acos
from math import sqrt


class WaterCannon(Object):
    def __init__(self, screenSize):
        super().__init__("WaterCannon")
        self.addComponent(Image("water_cannon"))
        self.__screenSize = screenSize
        self.__pivot = 31
        self.__rotation = 0
        self.__waterBalls = list()
        self.__reloadTime = 0.3
        self.__timer = 0

    def isRenderable(self):
        return True

    def tick(self, dTime):
        self.__timer -= dTime

    def render(self):
        surface, _ = self.getComponent("Image").render()
        surfaceSize = surface.get_size()
        surface = transform.rotate(surface, -self.__rotation)
        sizeDifference = (0.5 * (surfaceSize[0]-surface.get_size()[0]),
                          0.5 * (surfaceSize[1]-surface.get_size()[1]))
        verticalOffset = (
            -self.__pivot+surfaceSize[1]/2) * sin(self.__rotation+90)
        horizontalOffset = (
            -self.__pivot+surfaceSize[1]/2) * cos(self.__rotation+90)

        truck = Object.get("Truck")
        truckPosition = truck.getRenderPosition()

        truckSurface, origin = truck.getComponent("Image").render()
        surface.set_alpha(truck.getVisibility())
        truckSurfaceSize = truckSurface.get_size()
        truckSurface = transform.rotate(truckSurface, -truck.getRotation())
        truckSizeDifference = (0.5 * (truckSurfaceSize[0]-truckSurface.get_size()[0]),
                               0.5 * (truckSurfaceSize[1]-truckSurface.get_size()[1]))

        self.__renderPosition = (horizontalOffset+sizeDifference[0]+truckPosition[0]-truckSizeDifference[0]+(truckSurfaceSize[0]-surfaceSize[0])/2,
                                 verticalOffset+sizeDifference[1]+truckPosition[1]-truckSizeDifference[1]+(truckSurfaceSize[1]-surfaceSize[1])/2)
        return (surface, self.__renderPosition)

    def calcRotation(self, x, y):
        z = sqrt(x**2 + y**2)
        if z != 0:
            _cos = x/z
            self.__rotation = (1-2*int(y < 0))*acos(_cos)
            self.__rotation += 90

    def fire(self):
        if self.__timer > 0:
            return
        self.__timer = self.__reloadTime
        x, y = self.getComponent("Transform").getPosition()
        truckPosition = Object.get("Truck").getComponent(
            "Transform").getPosition()
        waterBall = WaterBall(
            self.__rotation, (x+truckPosition[0], y+truckPosition[1]), self.__pivot)
        self.__waterBalls.append(waterBall)

    def getWaterBalls(self):
        return self.__waterBalls

    def tickWaterBalls(self):
        for waterBall in self.__waterBalls:
            waterBall.tick()
