from pygame import display as Display, time as Time
from log import Log


class Renderer:
    __deltaTime = 0

    def __init__(self, resolution):
        self.__display = Display.set_mode(resolution)
        self.__FPSLimit = 144
        self.__clock = Time.Clock()
        Log.executionLog("Renderer created.")

    def render(self, scene):
        """Wyświetlanie wszystkich elementów na ekranie."""
        Renderer.__deltaTime = self.__clock.tick(self.__FPSLimit) / 1000.0
        self.__display.fill((50, 115, 35))
        for obj in scene.getObjects():
            if (obj.isActive() and obj.isRenderable()):
                try:
                    surface, position = obj.render()
                    self.__display.blit(surface, position)
                    if obj.getId() == "WaterCannon":
                        for waterBall in obj.getWaterBalls():
                            surface, position = waterBall.render()
                            self.__display.blit(surface, position)
                except Exception:
                    position = obj.getComponent("Transform").getPosition()
                    parent = obj.getParent()
                    if parent:
                        parentPos = parent.getComponent(
                            "Transform").getPosition()
                    else:
                        parentPos = (0, 0)
                    for componentType, component in obj.getComponents().items():
                        if not component.isRenderable():
                            continue
                        surface, origin = component.render()
                        surface.set_alpha(obj.getVisibility())
                        surfaceSize = surface.get_size()
                        renderPosition = (position[0]-surfaceSize[0]*(origin.x)+parentPos[0],
                                          position[1]-surfaceSize[1]*(origin.y)+parentPos[1])
                        self.__display.blit(surface, renderPosition)
        Display.flip()

    def getDeltaTime():
        return Renderer.__deltaTime
