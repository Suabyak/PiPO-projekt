from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image
from Renderer.renderer import Renderer
from pygame import transform
from Utils.maths import sin, isBetween, cos


class Truck(Object):
    def __init__(self, camera, screenSize):
        super().__init__(
            "Truck", (screenSize[0]/2, screenSize[1]/2), parent=camera)
        self.addComponent(Image("Truck", (0.5, 0.5)))
        self.__rotation = 0
        self.__rotationSpeed = 0
        self.__acceleration = 0
        self.__velocity = 0

    def render(self):
        position = self.getComponent("Transform").getPosition()
        surface, origin = self.getComponent("Image").render()
        surface.set_alpha(self.getVisibility())
        surfaceSize = surface.get_size()
        surface = transform.rotate(surface, -self.__rotation)
        sizeDifference = (0.5 * (surfaceSize[0]-surface.get_size()[0]),
                          0.5 * (surfaceSize[1]-surface.get_size()[1]))
        parent = self.getParent()
        parentPos = parent.getComponent("Transform").getPosition()
        renderPosition = (sizeDifference[0]+position[0]-surfaceSize[0]*(origin.x)+parentPos[0],
                          sizeDifference[1]+position[1]-surfaceSize[1]*(origin.y)+parentPos[1])
        return surface, renderPosition

    def move(self):
        self.__rotation += self.__rotationSpeed * (self.__velocity * 0.1)
        self.__rotation %= 360

        verticalOffset = self.__velocity * sin(self.__rotation-90)
        horizontalOffset = self.__velocity * cos(self.__rotation-90)
        self.getComponent("Transform").move(
            (horizontalOffset, verticalOffset))
        self.getParent().move((-horizontalOffset, - verticalOffset))

        self.applyFriction()

    def rotate(self, angle):
        self.__rotationSpeed += angle * Renderer.getDeltaTime()

    def accelerate(self, acceleration):
        self.__acceleration = acceleration
        self.__velocity += self.__acceleration * Renderer.getDeltaTime()

    def applyFriction(self):
        self.__rotationSpeed *= 0.95
        self.__velocity *= 0.98
