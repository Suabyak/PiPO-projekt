from Renderer.scene import Scene
from Scenes.TitleScreen.Objects.title import Title
from functools import partial


class TitleScreen(Scene):
    def __init__(self, main):
        super().__init__("TitleScreen", main)
        self.addObject(Title(self.getScreenSize(), partial(
            main.setActiveScene, "MainMenu")))
