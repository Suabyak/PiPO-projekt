from Renderer.scene import Scene
from Renderer.Objects.button import Button
from Renderer.Objects.object import Object
from Renderer.Objects.colouredLabel import ColouredLabel
from Renderer.Objects.Components.text import Text
from Scenes.MainMenu.Objects.mainMenuOperator import MainMenuOperator
from Scenes.MainMenu.Objects.title import Title
from functools import partial


class MainMenu(Scene):
    """Scena widoczna po włączeniu gry."""

    def __init__(self, main):
        super().__init__("MainMenu", main)
        operator = MainMenuOperator(self.getMain().startGame)
        self.addObject(operator)
        self.addObject(Title(self.getScreenSize(),
                             operator.getComponent("Appear").activate))

        self.addObject(ColouredLabel("Title2", "Strażak /bBam/-/rBam/",
                                     32, parent=operator, origin=(0.5, 0), position=(self.getScreenSize()[0]/2, 50)))
        self.addObject(Button("Play", Text("Graj", 48, origin=(0.5, 0)),
                              partial(MainMenu.fade, self.getMain()), parent=operator, position=(self.getScreenSize()[0]/2, 200)))
        self.addObject(Button("Quit", Text("Wyjdź z Gry", 48, origin=(0.5, 0)),
                              self.getMain().quit, parent=operator, position=(self.getScreenSize()[0]/2, 400)))

    def fade(game, event):
        operator = Object.get("MainMenuOperator")
        operator.getComponent("Fade").activate()
