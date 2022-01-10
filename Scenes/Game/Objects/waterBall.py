from Renderer.Objects.object import Object
from Renderer.Objects.Components.gif import Gif
from Utils.maths import sin, cos, acos
from math import sqrt


class WaterBall(Object):
    __count = 0
    __VELOCITY = 5

    def __init__(self, rotation, position, cannonLength):
        super().__init__(f"WaterBall_{WaterBall.__count}", position=position)
        WaterBall.__count += 1
        self.__rotation = rotation
        self.__damage = 10
        self.addComponent(Gif("water", 0.25, self.destroy))
        surface, _ = self.getComponent("Gif").render()
        self.surfaceSize = surface.get_size()
        self.move(cannonLength)

    def destroy(self):
        Object.get("WaterCannon").getWaterBalls().remove(self)

    def move(self, dist=__VELOCITY):
        verticalOffset = dist * sin(self.__rotation-90)
        horizontalOffset = dist * cos(self.__rotation-90)
        self.getComponent("Transform").move(
            (horizontalOffset, verticalOffset))
        if self.isOnFire():
            self.damageFire()

    def render(self):
        surface, _ = self.getComponent("Gif").render()
        position = self.getComponent("Transform").getPosition()
        cameraPosition = Object.get("Camera").getComponent(
            "Transform").getPosition()
        renderPosition = (cameraPosition[0]+position[0]-self.surfaceSize[0]/2,
                          cameraPosition[1]+position[1]-self.surfaceSize[1]/2)
        return surface, renderPosition

    def tick(self):
        self.getComponent("Gif").tick()
        self.move()

    def isRenderable(self):
        return True

    def isOnFire(self):
        fire = Object.get("Fire")
        if not fire.isActive():
            return
        fireCollider = fire.getComponent("Collider")
        firePos = fire.getComponent("Transform").getPosition()
        position = self.getComponent("Transform").getPosition()
        x = firePos[0] - position[0]
        y = firePos[1] - position[1]
        z = sqrt(x**2 + y**2)
        if z != 0:
            _cos = x/z
            rotation = (1-2*int(y < 0))*acos(_cos)
        verticalOffset = self.surfaceSize[1]/2 * sin(rotation)
        horizontalOffset = self.surfaceSize[0]/2 * cos(rotation)

        return fireCollider.isOver(firePos, (position[0]+horizontalOffset, position[1]+verticalOffset))

    def damageFire(self):
        Object.get("Fire").getHit(self.__damage
                                  - self.getComponent("Gif").getActiveImage())
        self.destroy()
