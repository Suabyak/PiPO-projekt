from Renderer.scene import Scene
from Scenes.Game.Objects.camera import Camera
from Scenes.Game.Objects.map import Map


class Game(Scene):
    def __init__(self, main):
        super().__init__("Game", main)

        camera = Camera()
        self.addObject(camera)
        self.addObject(Map(camera))

    def start(self):
        pass
