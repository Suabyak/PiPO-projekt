from Renderer.scene import Scene
from Scenes.Game.Objects.camera import Camera
from Scenes.Game.Objects.map import Map
from Scenes.Game.Objects.miniMap import MiniMap
from Scenes.Game.Objects.truck import Truck
from Scenes.Game.Objects.fire import Fire
from Scenes.Game.Objects.waterCannon import WaterCannon
from Scenes.Game.Objects.fireAppearedLabel import FireAppearedLabel
from Scenes.Game.Objects.firePointer import FirePointer
from Scenes.Game.Objects.scoreLabel import ScoreLabel
from Scenes.Game.Objects.waterTank import WaterTank


class Game(Scene):
    def __init__(self, main):
        super().__init__("Game", main)
        screenSize = main.getScreenSize()
        camera = Camera()
        self.addObject(camera)
        self.addObject(Map(camera))
        self.addObject(Fire(camera, screenSize))
        self.addObject(MiniMap(screenSize))
        self.addObject(FirePointer(screenSize))
        self.addObject(Truck(camera, screenSize))
        self.addObject(WaterCannon(screenSize))
        self.addObject(FireAppearedLabel(screenSize))
        self.addObject(WaterTank(screenSize))
        self.addObject(ScoreLabel())
