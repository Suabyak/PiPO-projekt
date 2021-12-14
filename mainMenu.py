from scene import Scene
from object import Object
from image import Image


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.addObject(
            Object("Placeholder1", components=[Image("placeholder")]))
