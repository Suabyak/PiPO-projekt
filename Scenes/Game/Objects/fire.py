from Renderer.Objects.object import Object
from Renderer.Objects.Components.gif import Gif
from Renderer.Objects.Components.collider import Collider
from Renderer.renderer import Renderer
from random import randint, choice
from Utils.eventOperator import EventOperator
from Utils.maths import getMinAndMax
from log import Log
from pygame import transform


class Fire(Object):
    __maxHP = 55

    def __init__(self, parent, screenSize):
        super().__init__("Fire", parent=parent, active=False)
        self.addComponent(Gif("fire", 0.15))
        surface, _ = self.getComponent("Gif").render()
        self.addComponent(Collider(surface.get_size(), (0.5, 0.5)))
        self.setTimeToFire()
        self.screenSize = screenSize
        self.__timesExtinguished = 0

    def tick(self):
        if self.isActive():
            self.getComponent("Gif").tick()
        else:
            self.__timeToFire -= Renderer.getDeltaTime()
            if self.__timeToFire <= 0:
                self.startFire()

    def isRenderable(self):
        return True

    def getTimeToFire(self):
        return self.__timeToFire

    def setTimeToFire(self):
        self.__timeToFire = randint(3, 7)

    def startFire(self):
        truckPosition = Object.get("Truck").getRenderPosition()
        x, y = truckPosition
        while (abs(x - truckPosition[0]) < self.screenSize[0]
               and abs(y - truckPosition[1]) < self.screenSize[1]):
            x, y = self.__getRandomPosition()
        self.getComponent("Transform").moveTo((x, y))
        Log.executionLog(f"Fire started at ({x}, {y})")
        self.setActive(True)
        self.__hp = self.__maxHP
        self.scale = 1
        EventOperator.createEvent(EventOperator.STOP, {"name": "peaceful"})
        EventOperator.createEvent(EventOperator.PLAY, {"name": "evil"})
        EventOperator.createEvent(EventOperator.PLAY,
                                  {"name": "sygnal", "loops": 0})

        Object.get("FirePointer").setActive(True)
        Object.get("FirePointer").calcRotation(x, y)
        Object.get("FireAppearedLabel").setActive(True)
        Object.get("FireAppearedLabel").getComponent("Fade").activate()

    def __getRandomPosition(self):
        map = Object.get("Map")
        road = choice(map.getRoads())
        xMin, xMax = getMinAndMax(road[0][0], road[1][0])
        yMin, yMax = getMinAndMax(road[0][1], road[1][1])
        x, y = (randint(xMin, xMax),
                randint(yMin, yMax))
        x *= map.TILE_SIZE
        y *= map.TILE_SIZE
        x += randint(0, map.TILE_SIZE) - map.TILE_SIZE*map.MAP_SIZE[0]/2
        y += randint(0, map.TILE_SIZE) - map.TILE_SIZE*map.MAP_SIZE[1]/2
        return x, y

    def getHit(self, waterDamage):
        self.__hp -= waterDamage
        self.scale = 0.3 + 0.7 * (self.__hp / self.__maxHP)
        surface, _ = self.getComponent("Gif").render()
        surfaceSize = surface.get_size()
        self.getComponent("Collider").setSize((surfaceSize[0]*self.scale,
                                               surfaceSize[1]*self.scale))
        Log.executionLog(f"Fire hit for {waterDamage} damage.")
        if self.__hp <= 0:
            self.stopFire()

    def stopFire(self):
        EventOperator.createEvent(EventOperator.STOP, {"name": "evil"})
        EventOperator.createEvent(EventOperator.STOP, {"name": "sygnal"})
        EventOperator.createEvent(EventOperator.PLAY, {"name": "peaceful"})
        self.setTimeToFire()
        self.setActive(False)
        self.__timesExtinguished += 1
        Object.get("ScoreLabel").setScore(self.__timesExtinguished)

    def render(self):
        position = self.getComponent("Transform").getPosition()
        surface, origin = self.getComponent("Gif").render()
        surfaceSize = surface.get_size()
        surface = transform.scale(
            surface, (int(surfaceSize[0]*self.scale), int(surfaceSize[1]*self.scale)))
        sizeDifference = (0.5 * (surfaceSize[0]-surface.get_size()[0]),
                          0.5 * (surfaceSize[1]-surface.get_size()[1]))
        parentPos = self.getParent().getComponent("Transform").getPosition()
        renderPosition = (sizeDifference[0]+position[0]-surfaceSize[0]*(origin.x)+parentPos[0],
                          sizeDifference[1]+position[1]-surfaceSize[1]*(origin.y)+parentPos[1])
        return surface, renderPosition

    def getPosition(self):
        return self.getComponent("Transform").getPosition()
