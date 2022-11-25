from interface import Directions


class Cell:
    def __init__(self, cellNum = 0, isStart = False, isFinish = False):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.isStart = isStart
        self.isFinish = isFinish
        self.cellNum = cellNum
    
    def setDirections(self, north = None, south = None, east = None, west = None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def getCellNum(self):
        return self.cellNum

    def finishStatus(self):
        return self.isFinish
    
    def startStatus(self):
        return self.isStart

    def makeStart(self):
        self.isStart = True

    def makeFinish(self):
        self.isFinish = True

    def getNorth(self):
        return self.north

    def getSouth(self):
        return self.south

    def getEast(self):
        return self.east

    def getWest(self):
        return self.west
    
    def setNorth(self, cell):
        self.north = cell

    def setSouth(self, cell):
        self.south = cell

    def setEast(self, cell):
        self.east = cell

    def setWest(self, cell):
        self.west = cell

    def connectCells(self, other, direction):
        match direction:
            case Directions.NORTH:
                self.setNorth(other)
                other.setSouth(self)
            case Directions.SOUTH:
                self.setSouth(other)
                other.setNorth(self)
            case Directions.EAST:
                self.setEast(other)
                other.setWest(self)
            case Directions.WEST:
                self.setWest(other)
                other.setEast(self)

    def hasNorth(self):
        return self.north is not None

    def hasSouth(self):
        return self.south is not None

    def hasEast(self):
        return self.east is not None

    def hasWest(self):
        return self.west is not None

    def getCoords(self, nrows, ncols):
        row = self.cellNum % nrows
        col = ncols - (self.cellNum // ncols)
        return (row, col)

    def hasDir(self, direction):
        match direction:
            case Directions.NORTH:
                return self.hasNorth()
            case Directions.SOUTH:
                return self.hasSouth()
            case Directions.EAST:
                return self.hasEast()
            case Directions.WEST:
                return self.hasWest()
            case _:
                raise ValueError
    
    def atDeadEnd(self, prevDir):
        match prevDir:
            case Directions.NORTH:
                return not(self.hasSouth()) and not(self.hasEast()) and not(self.hasWest())
            case Directions.SOUTH:
                return not(self.hasNorth()) and not(self.hasEast()) and not(self.hasWest())
            case Directions.EAST:
                return not(self.hasNorth()) and not(self.hasSouth()) and not(self.hasWest())
            case Directions.WEST:
                return not(self.hasNorth()) and not(self.hasSouth()) and not(self.hasEast())
            case _:
                raise ValueError