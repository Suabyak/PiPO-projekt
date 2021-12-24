from Renderer.scene import Scene
from Renderer.Objects.button import Button
from Renderer.Objects.Components.text import Text
from functools import partial


class MainMenu(Scene):
    """Scena widoczna po włączeniu gry."""

    def __init__(self, main):
        super().__init__("MainMenu", main)
        self.addObject(Button("Play", Text("Graj", 64, origin=(0.5, 0)),
                              partial(MainMenu.play, self.getMain()), position=(self.getScreenSize()[0]/2, 100)))
        self.addObject(Button("Quit", Text("Wyjdź z Gry", 64, origin=(0.5, 0)),
                              self.getMain().quit, position=(self.getScreenSize()[0]/2, 300)))

    def play(game, event):
        game.setActiveScene("Game")
