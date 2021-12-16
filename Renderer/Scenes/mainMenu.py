from Renderer.Scenes.scene import Scene
from Renderer.Objects.button import Button
from Renderer.Objects.Components.text import Text


class MainMenu(Scene):
    """Scene widoczna po włączeniu gry."""

    def __init__(self, main):
        super().__init__()
        self.__main = main
        self.__screenSize = main.getScreenSize()
        self.addObject(Button("Play", Text("Graj", 64, origin=(0.5, 0)),
                              self.play, position=(self.__screenSize[0]/2, 100)))
        self.addObject(Button("Quit", Text("Wyjdź z Gry", 64, origin=(0.5, 0)),
                              self.__main.quit, position=(self.__screenSize[0]/2, 300)))

    def play(self):
        print("Come back later.")
        exit(0)
