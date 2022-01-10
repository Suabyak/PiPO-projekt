from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image
from Utils.maths import acos, sin, cos
from math import sqrt
from pygame import transform


class FirePointer(Object):
    def __init__(self, screenSize):
        super().__init__("FirePointer", active=False)
        self.addComponent(Image("arrow", (0.5, 0.5)))
        self.screenSize = screenSize
        self.__pivot = 200

    def isRenderable(self):
        return True

    def render(self):
        surface, _ = self.getComponent("Image").render()
        surfaceSize = surface.get_size()
        surface = transform.rotate(surface, -self.__rotation+180)
        sizeDifference = (0.5 * (surfaceSize[0]-surface.get_size()[0]),
                          0.5 * (surfaceSize[1]-surface.get_size()[1]))
        verticalOffset = (
            self.__pivot+surfaceSize[1]/2) * sin(self.__rotation+90)
        horizontalOffset = (
            self.__pivot+surfaceSize[1]/2) * cos(self.__rotation+90)
        return (surface, (self.screenSize[0]/2+horizontalOffset+sizeDifference[0],
                          self.screenSize[1]/2+verticalOffset+sizeDifference[1]))

    def calcRotation(self, x=None, y=None):
        if not self.isActive():
            return
        if not (x and y):
            x, y = Object.get("Fire").getComponent("Transform").getPosition()
        truckPosition = Object.get("Truck").getComponent(
            "Transform").getPosition()
        x = truckPosition[0] - x
        y = truckPosition[1] - y
        if abs(x) < self.screenSize[0]/2 and abs(y) < self.screenSize[1]/2:
            self.setActive(False)
        z = sqrt(x**2 + y**2)
        if z != 0:
            _cos = x/z
            self.__rotation = (1-2*int(y < 0))*acos(_cos)
            self.__rotation += 90
