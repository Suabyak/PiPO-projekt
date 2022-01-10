from Renderer.scene import Scene
from Scenes.Game.Objects.camera import Camera
from Scenes.Game.Objects.map import Map
from Scenes.Game.Objects.truck import Truck
from Scenes.Game.Objects.fire import Fire


class Game(Scene):
    def __init__(self, main):
        super().__init__("Game", main)

        camera = Camera()
        self.addObject(camera)
        self.addObject(Map(camera))
        self.addObject(Fire(camera))
        self.addObject(Truck(camera, main.getScreenSize()))
