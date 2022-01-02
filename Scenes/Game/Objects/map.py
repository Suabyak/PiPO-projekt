from Renderer.Objects.object import Object
from random import choice
from pygame import Surface


class Map(Object):
    def __init__(self, camera):
        self.TILE_SIZE = 350
        self.TILE_DIMENSIONS = (self.TILE_SIZE, self.TILE_SIZE)
        self.STREET_COLOUR = (81, 81, 81)
        self.GRASS_COLOUR = (60, 125, 45)
        self.MAP_SIZE = (48, 48)
        self.STREET_COUNT = 10
        super().__init__("Map", parent=camera)
        self.createSurface()

    def createSurface(self):
        self.surface = Surface((self.MAP_SIZE[0] * self.TILE_SIZE,
                                self.MAP_SIZE[1] * self.TILE_SIZE))
        self.surfaceSize = self.surface.get_size()
        for i in range(self.MAP_SIZE[0] * self.MAP_SIZE[1]):
            tile = Surface(self.TILE_DIMENSIONS)
            tile.fill(self.GRASS_COLOUR)
            destination = (self.TILE_SIZE * (i % self.MAP_SIZE[0]),
                           self.TILE_SIZE * int(i / self.MAP_SIZE[0]))
            print(i, destination)
            self.surface.blit(tile, destination)

    def render(self):
        parent = self.getParent()
        parentPos = parent.getComponent("Transform").getPosition()
        return self.surface, (-self.surfaceSize[0]/2+parentPos[0], -self.surfaceSize[1]/2+parentPos[1])

    def isRenderable(self):
        return True
