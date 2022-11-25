from enum import IntEnum
import random

class Directions(IntEnum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

direction = {'n': Directions.NORTH, 's': Directions.SOUTH, 'e': Directions.EAST, 'w': Directions.WEST}
directionsSet = (Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST)
directionChar = {Directions.NORTH : 'N', Directions.SOUTH : 'S', Directions.EAST : 'E', Directions.WEST : 'W'}

def DistanceForm(p1, p2):
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    return (((x2 - x1)**2) + ((y2 - y1)**2))**.5

def pathStr(path):
    res = ""
    res += directionChar[Directions(path[0])]
    for i in range(1, len(path)):
        res += " "
        res += directionChar[Directions(path[i])]
    return res