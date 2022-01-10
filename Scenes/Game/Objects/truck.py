from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image
from Renderer.renderer import Renderer
from pygame import transform
from Utils.maths import sin, cos, isBetween


class Truck(Object):
    def __init__(self, camera, screenSize):
        super().__init__(
            "Truck", (screenSize[0]/2, screenSize[1]/2), parent=camera)
        self.addComponent(Image("Truck", (0.5, 0.5)))
        self.__rotation = 0
        self.__rotationSpeed = 0
        self.__acceleration = 0
        self.__velocity = 0
        self.__handleBrake = 0
        self.__onGrass = 0
        self.__tile = 0

        map = Object.get("Map")
        mainRoad = map.getRoads()[0]
        tile = ((1+mainRoad[0][0]+mainRoad[1][0]-map.MAP_SIZE[0])/2.0,
                (1+mainRoad[0][1]+mainRoad[1][1]-map.MAP_SIZE[1])/2.0)
        horizontalOffset = tile[0]*map.TILE_SIZE-screenSize[0]/2
        verticalOffset = tile[1]*map.TILE_SIZE-screenSize[1]/2
        self.getComponent("Transform").move(
            (horizontalOffset, verticalOffset))
        self.getParent().move((-horizontalOffset, - verticalOffset))

        if map.determineRoadOrientation(mainRoad) == "X":
            self.__rotation = 90

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
        self.__renderPosition = renderPosition
        return surface, renderPosition

    def move(self):
        self.__rotation += self.__rotationSpeed * (self.__velocity * 0.1)
        self.__rotation %= 360

        verticalOffset = self.__velocity * sin(self.__rotation-90)
        horizontalOffset = self.__velocity * cos(self.__rotation-90)
        self.getComponent("Transform").move(
            (horizontalOffset, verticalOffset))
        map = Object.get("Map")
        self.__tile = self.getComponent("Transform").getPosition()
        self.__tile = (self.__tile[0]//map.TILE_SIZE+map.MAP_SIZE[0]/2,
                       self.__tile[1]//map.TILE_SIZE+map.MAP_SIZE[1]/2)
        self.isOnGrass()
        self.getParent().move((-horizontalOffset, - verticalOffset))
        self.keepOnMap()
        self.applyFriction()

    def rotate(self, angle):
        self.__rotationSpeed += angle * Renderer.getDeltaTime() * (1+0.3*self.__onGrass)

    def accelerate(self, acceleration):
        self.__acceleration = acceleration
        self.__velocity += self.__acceleration * \
            Renderer.getDeltaTime() * (1-self.__onGrass*0.5)

    def applyFriction(self):
        self.__rotationSpeed *= (0.96 + self.__handleBrake * 0.025)
        self.__velocity *= (0.98 - self.__handleBrake * 0.05)

    def setHandleBrake(self, value):
        self.__handleBrake = value

    def isOnGrass(self):
        map = Object.get("Map")
        for road in map.getRoads():
            if (isBetween(road[0][0], road[1][0], self.__tile[0])
                    and isBetween(road[0][1], road[1][1], self.__tile[1])):
                self.__onGrass = 0
                return
        self.__onGrass = 1

    def keepOnMap(self):
        map = Object.get("Map")
        xSize, ySize = (map.TILE_SIZE*map.MAP_SIZE[0]/2,
                        map.TILE_SIZE*map.MAP_SIZE[1]/2)
        xPos, yPos = self.getComponent("Transform").getPosition()
        if abs(xPos) > abs(xSize):
            xOffset = (abs(xPos) - abs(xSize)) * -(abs(xPos) / xPos)
        else:
            xOffset = 0
        if abs(yPos) > abs(ySize):
            yOffset = (abs(yPos) - abs(ySize)) * -(abs(yPos) / yPos)
        else:
            yOffset = 0
        self.getComponent("Transform").move(
            (xOffset, yOffset))
        self.getParent().move((-xOffset, -yOffset))

    def getRenderPosition(self):
        return self.__renderPosition

    def getRotation(self):
        return self.__rotation
