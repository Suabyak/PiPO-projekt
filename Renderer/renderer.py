from pygame import display as Display, time as Time


class Renderer:
    def __init__(self, resolution):
        self.__display = Display.set_mode(resolution)
        self.__clock = Time.Clock()
        self.__FPSLimit = 144

    def render(self, scene):
        """Wyświetlanie wszystkich elementów na ekranie."""
        self.__clock.tick(self.__FPSLimit)
        for obj in scene.getObjects():
            if (obj.isActive() and obj.isRenderable()):
                self.__display.blit(obj.getComponent("Image").getSurface(),
                                    obj.getComponent("Transform").getPosition())
        Display.flip()
