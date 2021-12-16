from Renderer.Scenes.scene import Scene
from Renderer.Objects.button import Button
from Renderer.Objects.label import Label
from Renderer.Objects.Components.rect import Rect


class MainMenu(Scene):
    """Scene widoczna po włączeniu gry."""

    def __init__(self, main):
        super().__init__()
        self.__main = main
        self.addObject(Button("nawiekszyszef", Rect(
            (100, 100), (51, 51, 255)), self.test, position=(500, 500)))
        self.addObject(Label("napisek", "Co tam?", 12, (0, 200), (255, 0, 0)))

    def test(self):
        print(self.__main)
