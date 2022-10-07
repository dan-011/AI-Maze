from cell import *
from interface import *
class Maze:
    def __init__(self):
        self.startCell = None
        self.finishCell = None
        self.cells = {}
        self.runningumber = 0
    
    def getStartCell(self):
        return self.startCell
    
    def __len__(self):
        return len(self.cells)
    
    def __getitem__(self, index):
        return self.cells[index]

    def __setitem__(self, index, value):
        self.cells[index] = value

    def __contains__(self, index):
        return index in self.cells
    
    def __iter__(self):
        return self.cells.__iter__()

    def buildMaze(self):
        for i in range(100):
            self[i] = Cell(cellNum=i)
        with open("maze_file.txt", "r+") as f:
            for line in f:
                l = line.strip().split()
                for c in l:
                    cleaned = c[1:-1] # remove parenthesis
                    contents = cleaned.split(",")
                    cellNum = int(contents[0])
                    dirs = contents[1:]
                    for dir in dirs:
                        match dir:
                            case 'N':
                                self[cellNum].connectCells(self[cellNum-10], Directions.NORTH)
                            case 'S':
                                self[cellNum].connectCells(self[cellNum+10], Directions.SOUTH)
                            case 'E':
                                self[cellNum].connectCells(self[cellNum+1], Directions.EAST)
                            case 'W':
                                self[cellNum].connectCells(self[cellNum-1], Directions.WEST)
                            case _:
                                raise KeyError
        self[0].makeStart()
        self.startCell = self[0]
        self[99].makeFinish()
        self.finishCell = self[99]

    def defineCellNum(self):
        self.runningumber += 1
        self.cellNumbers.add(self.runningumber)
        return self.runningumber

    def buildMazeCell(self, cell, directions):
        north = None
        south = None
        east = None
        west = None
        for dir in directions:
            cellNum = self.defineCellNum()
            match dir:
                case Directions.NORTH:
                    north = Cell(cellNum)
                    cell.connectCells(north, Directions.NORTH)
                case Directions.SOUTH:
                    south = Cell(cellNum)
                    cell.connectCells(south, Directions.SOUTH)
                case Directions.EAST:
                    east = Cell(cellNum)
                    cell.connectCells(east, Directions.EAST)
                case Directions.WEST:
                    west = Cell(cellNum)
                    cell.connectCells(west, Directions.WEST)
        cell.setDirections(north, south, east, west)

    def enterMaze(self):
        return self.startCell

