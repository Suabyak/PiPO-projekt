from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image


class Map(Object):
    def __init__(self, camera):
        super().__init__("Map", parent=camera)
        self.addComponent(Image("Zrzut ekranu 2021-12-30 093435"))
