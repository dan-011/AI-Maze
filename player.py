from interface import *
from cell import *
from maze import *

class Player:
    def __init__(self, startCell = Cell(isStart = True)): # this is just a placeholder
        self.current_cell = startCell
        self.inventory = {}
        self.map = None
        self.performance = 0
        self.path = []
        self.maze = None

    def enterMaze(self, maze):
        self.current_cell = maze.getStartCell()
        self.maze = maze

    def goNorth(self):
        if(self.current_cell.getNorth() is not None):
            #print("Moving North")
            self.current_cell = self.current_cell.getNorth()
        else:
            print("Cannot go North")

    def goSouth(self):
        if(self.current_cell.getSouth() is not None):
            #print("Moving South")
            self.current_cell = self.current_cell.getSouth()
        else:
            print("Cannot go South")

    def goEast(self):
        if(self.current_cell.getEast() is not None):
            #print("Moving East")
            self.current_cell = self.current_cell.getEast()
        else:
            print("Cannot go East")
    
    def goWest(self):
        if(self.current_cell.getWest() is not None):
            #print("Moving West")
            self.current_cell = self.current_cell.getWest()
        else:
            print("Cannot go West")

    def move(self, direction):
        match direction:
            case Directions.NORTH:
                self.goNorth()
            case Directions.SOUTH:
                self.goSouth()
            case Directions.EAST:
                self.goEast()
            case Directions.WEST:
                self.goWest()
            case _:
                raise ValueError

    def checkFinish(self):
        if self.current_cell.finishStatus():
            print("Reached Finish")
            return True
        else:
            return False
    
    def checkStart(self):
        if self.current_cell.startStatus():
            print("You're at the start")
            return True
        else:
            return False

    def hasNorth(self):
        return self.current_cell.hasNorth()

    def hasSouth(self):
        return self.current_cell.hasSouth()

    def hasEast(self):
        return self.current_cell.hasEast()

    def hasWest(self):
        return self.current_cell.hasWest()

    def lookAround(self):
        msg = "You can go "
        if(self.hasNorth()):
            msg += "North "
        if(self.hasSouth()):
            msg += "South "
        if(self.hasEast()):
            msg += "East "
        if(self.hasWest()):
            msg += "West"
        print(msg)

    def getCurrentCell(self):
        return self.current_cell
    
    def setPerformance(self, perf):
        self.performance = perf

    def getPerformance(self):
        return self.performance

    def setPath(self, path):
        self.path = path.copy()

    def getPath(self):
        return self.path

    def runPath(self, maze):
        # print("testing path: " + pathStr(self.path))
        for i in range(len(self.path)):
            dir = Directions(self.path[i])
            if(i > 0):
                prev = Directions(self.path[i-1])
                if(self.current_cell.atDeadEnd(prev)):
                    self.performance = .00000000001
                    return .00000000001
            if(not(self.current_cell.hasDir(dir))):
                self.performance = .00000000001
                return .00000000001
            self.move(dir)
            if(self.checkFinish()):
                self.performance = 1
                self.path = self.path[:i+1]
                current_cellnum = self.current_cell.getCellNum()
                return 1
        perf = maze.getPerformance(self.current_cell)
        if(perf == 0):
            self.performance = 1
            return 1
        self.performance = 1/perf
        return 1/perf