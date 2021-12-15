from Renderer.Scenes.scene import Scene
from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image


class MainMenu(Scene):
    """Scene widoczna po włączeniu gry.s"""

    def __init__(self):
        super().__init__()
        self.addObject(
            Object("Placeholder1", components=[Image("placeholder")]))
