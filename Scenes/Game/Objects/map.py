from Renderer.Objects.object import Object
from pygame import Surface
from random import randint, choice, choices, uniform
from Utils.maths import getMinAndMax, getLesser


class Map(Object):
    def __init__(self, camera):
        self.TILE_SIZE = 350
        self.TILE_DIMENSIONS = (self.TILE_SIZE, self.TILE_SIZE)
        self.ROAD_COLOUR = (81, 81, 81)
        self.GRASS_COLOUR = (60, 125, 45)
        self.MAP_SIZE = (48, 48)
        self.ROAD_COUNT = 25
        self.MAIN_ROAD_COUNT = 3
        self.ROAD_MIN_LEN = 0.3
        self.ROAD_MAX_LEN = 0.6
        super().__init__("Map", parent=camera)
        self.createSurface()

    def createSurface(self):
        self.__surface = Surface((self.MAP_SIZE[0] * self.TILE_SIZE,
                                  self.MAP_SIZE[1] * self.TILE_SIZE))
        self.surfaceSize = self.__surface.get_size()
        for i in range(self.MAP_SIZE[0] * self.MAP_SIZE[1]):
            tile = Surface(self.TILE_DIMENSIONS)
            tile.fill(self.GRASS_COLOUR)
            destination = (self.TILE_SIZE * (i % self.MAP_SIZE[0]),
                           self.TILE_SIZE * int(i / self.MAP_SIZE[0]))
            self.__surface.blit(tile, destination)
        self.__createRoads()
        for road in self.__roads:
            pos = (getLesser(road[0][0], road[1][0])*self.TILE_SIZE,
                   getLesser(road[0][1], road[1][1])*self.TILE_SIZE)
            roadSurface = Surface((self.TILE_SIZE * (abs(road[0][0]-road[1][0])+1),
                                   self.TILE_SIZE * (abs(road[0][1]-road[1][1])+1)))
            roadSurface.fill(self.ROAD_COLOUR)
            self.__surface.blit(roadSurface, pos)

    def render(self):
        parent = self.getParent()
        parentPos = parent.getComponent("Transform").getPosition()
        return self.__surface, (-self.surfaceSize[0]/2+parentPos[0],
                                -self.surfaceSize[1]/2+parentPos[1])

    def isRenderable(self):
        return True

    def __createRoads(self):
        self.__roads = list()

        for i in range(self.MAIN_ROAD_COUNT):
            startToBorderDist = randint(1, 4)
            endToBorderDist = randint(1, 4)
            orientation = choice(["N", "E", "S", "W"])
            if orientation in ["E", "W"]:
                x1 = startToBorderDist
                x2 = self.MAP_SIZE[0] - endToBorderDist
                y1 = y2 = randint(1, self.MAP_SIZE[1]-1)
            if orientation in ["N", "S"]:
                y1 = startToBorderDist
                y2 = self.MAP_SIZE[1] - endToBorderDist
                x1 = x2 = randint(1, self.MAP_SIZE[0]-1)
            self.__roads.append(((x1, y1), (x2, y2)))

        for i in range(self.ROAD_COUNT-self.MAIN_ROAD_COUNT):
            connectedRoad = choice(self.__roads)
            if i < self.MAIN_ROAD_COUNT * 3:
                connectedRoad = self.__roads[i % self.MAIN_ROAD_COUNT]
            orientation = self.determineRoadOrientation(connectedRoad)
            if orientation == "X":
                distToTop = connectedRoad[0][1] - 1
                distToBottom = self.MAP_SIZE[1] - distToTop - 2
                orientation = choices(["N", "S"], [distToTop, distToBottom])
                x1, x2 = getMinAndMax(connectedRoad[0][0], connectedRoad[1][0])
                start = (randint(x1, x2),
                         connectedRoad[0][1])
                roadLen = self.__calcRoadLength(start, orientation)
                if orientation[0] == "N":
                    roadLen *= -1
                end = (start[0], start[1]+roadLen)
            else:
                distToLeft = connectedRoad[0][0] - 1
                distToRight = self.MAP_SIZE[0] - distToLeft - 2
                orientation = choices(["W", "E"], [distToLeft, distToRight])
                y1, y2 = getMinAndMax(connectedRoad[0][1], connectedRoad[1][1])
                start = (connectedRoad[0][0],
                         randint(y1, y2))
                roadLen = self.__calcRoadLength(start, orientation)
                if orientation[0] == "W":
                    roadLen *= -1
                end = (start[0]+roadLen, start[1])
            self.__roads.append((start, end))

    def __calcRoadLength(self, pos, orientation):
        orientation = orientation[0]
        if orientation in ["W", "E"]:
            pos = pos[0]
            if orientation == "W":
                distToEnd = pos
            else:
                distToEnd = self.MAP_SIZE[0] - pos
        else:
            pos = pos[1]
            if orientation == "N":
                distToEnd = pos
            else:
                distToEnd = self.MAP_SIZE[0] - pos
        return int(distToEnd * uniform(self.ROAD_MIN_LEN, self.ROAD_MAX_LEN))

    def determineRoadOrientation(self, road):
        start, end = road
        x1, _ = start
        x2, _ = end
        return "Y" if x1 == x2 else "X"

    def getRoads(self):
        return self.__roads

    def getSurface(self):
        return self.__surface
