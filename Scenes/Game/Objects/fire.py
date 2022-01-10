from Renderer.Objects.object import Object
from Renderer.Objects.Components.gif import Gif
from Renderer.renderer import Renderer
from random import randint
from Utils.eventOperator import EventOperator


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
        self.setActive(True)
        self.__hp = 100
        EventOperator.createEvent(EventOperator.STOP, {"name": "peaceful"})
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
