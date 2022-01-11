from Renderer.Objects.object import Object
from pygame import transform, Surface, Rect


class MiniMap(Object):
    def __init__(self, screenSize):
        super().__init__("MiniMap")
        self.__screenSize = screenSize

    def isRenderable(self):
        return True

    def render(self):
        map = Object.get("Map")
        truckPosition = Object.get("Truck").getComponent(
            "Transform").getPosition()
        fire = Object.get("Fire")
        firePosition = fire.getPosition()
        truckPosition = (truckPosition[0]+map.TILE_SIZE*map.MAP_SIZE[0]/2,
                         truckPosition[1]+map.TILE_SIZE*map.MAP_SIZE[1]/2)
        firePosition = (firePosition[0]+map.TILE_SIZE*map.MAP_SIZE[0]/2,
                        firePosition[1]+map.TILE_SIZE*map.MAP_SIZE[1]/2)
        mapSurface = map.getSurface()
        mapSize = mapSurface.get_size()
        truckPosition = (truckPosition[0]/mapSize[0],
                         truckPosition[1]/mapSize[0])
        firePosition = (firePosition[0]/mapSize[0],
                        firePosition[1]/mapSize[0])
        mapSurface = transform.scale(mapSurface, (12*map.MAP_SIZE[0],
                                                  12*map.MAP_SIZE[1]))
        mapSize = mapSurface.get_size()
        if fire.isActive():
            mapSurface.fill((240, 55, 5), Rect(int(firePosition[0]*mapSize[0])-2,
                                               int(firePosition[1]
                                                   * mapSize[1])-2,
                                               4, 4))
        mapSlicedSurface = Surface((144, 144))
        mapSlicedSurface.fill((50, 115, 35))
        mapSlicedSurface.blit(mapSurface, (72-int(truckPosition[0]*mapSize[0]),
                                           72-int(truckPosition[1]*mapSize[1])))
        mapSlicedSurface.fill((255, 255, 255), Rect(70, 70, 4, 4))
        surface = Surface((150, 150))
        surface.blit(mapSlicedSurface, (3, 3))
        surfaceSize = surface.get_size()
        origin = (1, 0)
        position = (20, 20)
        renderPosition = (self.__screenSize[0] - position[0]-surfaceSize[0]*(origin[0]),
                          position[1]-surfaceSize[1]*(origin[1]))
        return surface, renderPosition
