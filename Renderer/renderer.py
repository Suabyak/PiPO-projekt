from pygame import display as Display, time as Time
from log import Log


class Renderer:
    def __init__(self, resolution):
        self.__display = Display.set_mode(resolution)
        self.__clock = Time.Clock()
        self.__FPSLimit = 144
        Log.executionLog("Renderer created.")

    def render(self, scene):
        """Wyświetlanie wszystkich elementów na ekranie."""
        self.__clock.tick(self.__FPSLimit)
        self.__display.fill((0, 0, 0))
        for obj in scene.getObjects():
            if (obj.isActive() and obj.isRenderable()):
                try:
                    surface, position = obj.render()
                    self.__display.blit(surface, position)
                except Exception:
                    position = obj.getComponent("Transform").getPosition()
                    for componentType, component in obj.getComponents().items():
                        if not component.isRenderable():
                            continue
                        surface, origin = component.render()
                        surface.set_alpha(obj.getVisibility())
                        surfaceSize = surface.get_size()
                        renderPosition = (position[0]-surfaceSize[0]*(origin.x),
                                          position[1]-surfaceSize[1]*(origin.y))
                        self.__display.blit(surface, renderPosition)
        Display.flip()
