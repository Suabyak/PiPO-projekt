from Renderer.Scenes.scene import Scene
from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image
from Renderer.Objects.Components.label import Label
from Utils import maths


class MainMenu(Scene):
    """Scene widoczna po włączeniu gry.s"""

    def __init__(self):
        super().__init__()
        self.addObject(Object("Placeholder1", components=[
                       Image("placeholder", origin=maths.Vector2(100, 100))]))
        self.addObject(Object("tekst", components=[Label(
            "Siema", 40, origin=maths.Vector2(-100, -200))]))
