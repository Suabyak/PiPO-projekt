from Renderer.Objects.object import Object
from Renderer.Objects.Components.gif import Gif
from Renderer.renderer import Renderer
from random import randint, choice
from Utils.eventOperator import EventOperator
from Utils.maths import getMinAndMax


class Fire(Object):
    def __init__(self, parent):
        super().__init__("Fire", parent=parent, active=False)
        self.addComponent(Gif("fire", 0.15))
        self.setTimeToFire()

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
        self.getComponent("Transform").moveTo((x, y))
        self.setActive(True)
        self.__hp = 100
        EventOperator.createEvent(EventOperator.STOP, {"name": "peaceful"})
        Object.get("FireAppearedLabel").setActive(True)
        Object.get("FireAppearedLabel").getComponent("Fade").activate()
        #play evil sound

    def getHit(self, waterDamage):
        self.__hp -= waterDamage
        if self.__hp <= 0:
            self.stopFire()

    def stopFire(self):
        EventOperator.createEvent(EventOperator.PLAY, {"name": "peaceful"})
        self.setTimeToFire()
        self.setActive(False)
