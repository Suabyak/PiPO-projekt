from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image
from pygame import transform
from Utils.maths import sin, isBetween


class Truck(Object):
    def __init__(self, camera, screenSize):
        super().__init__(
            "Truck", (screenSize[0]/2, screenSize[1]/2), parent=camera)
        self.addComponent(Image("Truck", (0, 0)))
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
        parent = self.getParent()
        parentPos = parent.getComponent("Transform").getPosition()
        renderPosition = (position[0]-surfaceSize[0]*(origin.x)+parentPos[0],
                          position[1]-surfaceSize[1]*(origin.y)+parentPos[1])
        return surface, renderPosition

    def move(self):
        self.__rotation += self.__rotationSpeed
        self.__rotation %= 360

        vertMultiplier = int(str(bin(isBetween(90, 270, self.__rotation))), 2)
        vertMultiplier *= 2
        vertMultiplier -= 1
        sinRotation = sin(self.__rotation)
        verticalOffset = self.__velocity * \
            (vertMultiplier * (1 - abs(sinRotation)))
        horizontalOffset = self.__velocity * sinRotation
        self.getComponent("Transform").move((horizontalOffset, verticalOffset))
        self.getParent().move((-horizontalOffset, -verticalOffset))

        self.applyFriction()

    def rotate(self, angle):
        self.__rotationSpeed += angle

    def accelerate(self, acceleration):
        self.__acceleration = acceleration
        self.__velocity += self.__acceleration

    def applyFriction(self):
        self.__rotationSpeed *= 0.95
        self.__velocity *= 0.99
