from pygame import display as Display, time as Time


class Renderer:
    def __init__(self, resolution):
        self.__display = Display.set_mode(resolution)
        self.__clock = Time.Clock()
        self.__FPSLimit = 144

    def render(self, scene):
        """Wyświetlanie wszystkich elementów na ekranie."""
        self.__clock.tick(self.__FPSLimit)
        self.__display.fill((0, 0, 0))
        for obj in scene.getObjects():
            if (obj.isActive() and obj.isRenderable()):
                position = obj.getComponent("Transform").getPosition()
                for componentType, component in obj.getComponents().items():
                    if not component.isRenderable():
                        continue
                    surface, origin = component.render()
                    self.__display.blit(
                        surface, (position[0]-origin.x, position[1]-origin.y))
        Display.flip()
