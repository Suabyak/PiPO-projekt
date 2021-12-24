from Renderer.scene import Scene
from Renderer.Objects.button import Button
from Renderer.Objects.colouredLabel import ColouredLabel
from Renderer.Objects.Components.text import Text
from functools import partial


class MainMenu(Scene):
    """Scena widoczna po włączeniu gry."""

    def __init__(self, main):
        super().__init__("MainMenu", main)
        self.addObject(ColouredLabel("Title", "Strażak /bBam/-/rBam/",
                                     32, origin=(0.5, 0), position=(self.getScreenSize()[0]/2, 50)))
        self.addObject(Button("Play", Text("Graj", 48, origin=(0.5, 0)),
                              partial(MainMenu.play, self.getMain()), position=(self.getScreenSize()[0]/2, 200)))
        self.addObject(Button("Quit", Text("Wyjdź z Gry", 48, origin=(0.5, 0)),
                              self.getMain().quit, position=(self.getScreenSize()[0]/2, 400)))

    def play(game, event):
        game.setActiveScene("Game")
