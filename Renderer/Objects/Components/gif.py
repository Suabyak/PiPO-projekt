from Renderer.Objects.Components.component import Component
from Renderer.Objects.Components.image import Image
from Renderer.renderer import Renderer
from log import Log


class Gif(Component):

    def __init__(self, path, timeToChange, action=None):
        self.__activeImage = 0
        self.__timeToChange = timeToChange
        self.__timer = timeToChange
        self.__images = dict()
        self.__action = action
        i = 0
        while 1:
            try:
                self.__images[i] = Image(f"{path}_{i+1}", (0.5, 0.5))
                i += 1
            except Exception as e:
                Log.executionLog(f"Loaded gif {path} with {i} images.")
                break

    def isRenderable(self):
        return True

    def nextImage(self):
        self.__activeImage += 1
        if self.__activeImage == len(self.__images):
            self.__activeImage = 0
            if self.__action:
                self.__action()

    def render(self):
        return self.__images[self.__activeImage].render()

    def tick(self):
        self.__timer -= Renderer.getDeltaTime()
        if self.__timer < 0:
            self.__timer += self.__timeToChange
            self.nextImage()

    def getActiveImage(self):
        return self.__activeImage
