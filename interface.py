from enum import IntEnum

class Directions(IntEnum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

direction = {'n': Directions.NORTH, 's': Directions.SOUTH, 'e': Directions.EAST, 'w': Directions.WEST}
directionsSet = (Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST)