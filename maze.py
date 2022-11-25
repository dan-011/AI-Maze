from cell import *
from interface import *
from player import *
class Maze:
    def __init__(self, nrows = 0, ncols = 0):
        self.startCell = None
        self.finishCell = None
        self.cells = []
        self.runningumber = 0
        self.nrows = nrows
        self.ncols = ncols
    
    def getStartCell(self):
        return self.startCell

    def setRowsCols(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols

    def getRowsCols(self):
        return (self.nrows, self.ncols)
    
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
            # self[i] = Cell(cellNum=i)
            self.cells.append(Cell(cellNum=i))
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

    def buildTestMaze(self):
        cell0 = Cell(0, isStart=True)
        cell1 = Cell(1)
        cell2 = Cell(2)
        cell3 = Cell(3)
        cell4 = Cell(4)
        cell5 = Cell(5)
        cell6 = Cell(6)
        cell7 = Cell(7)
        cell8 = Cell(8, isFinish=True)
        cell0.south = cell3
        cell0.east = cell1

        cell1.south = cell4
        cell1.east = cell2
        cell1.west = cell0

        cell2.south = cell5
        cell2.west = cell1

        cell3.north = cell0
        cell3.east = cell4
        cell3.south = cell6

        #cell4.north = cell1
        #cell4.south = cell7
        #cell4.east = cell5
        cell4.west = cell3

        cell5.north = cell2
        cell5.south = cell8
        cell5.west = cell4

        cell6.north = cell3
        cell6.east = cell7

        cell7.north = cell4
        cell7.east = cell8
        cell7.west = cell6

        cell8.north = cell5
        cell8.west = cell7

        self.cells.append(cell0)
        self.cells.append(cell1)
        self.cells.append(cell2)
        self.cells.append(cell3)
        self.cells.append(cell4)
        self.cells.append(cell5)
        self.cells.append(cell6)
        self.cells.append(cell7)
        self.cells.append(cell8)

        self.startCell = cell0
        cell0.makeStart()
        self.finishCell = cell8
        cell8.makeFinish()
    
    def buildTestMaze2(self):
        cell0 = Cell(0, isStart=True)
        cell1 = Cell(1)
        cell2 = Cell(2)
        cell3 = Cell(3)
        cell4 = Cell(4)
        cell5 = Cell(5)
        cell6 = Cell(6)
        cell7 = Cell(7)
        cell8 = Cell(8)
        cell9 = Cell(9)
        cell10 = Cell(10)
        cell11 = Cell(11)
        cell12 = Cell(12)
        cell13 = Cell(13)
        cell14 = Cell(14)
        cell15 = Cell(15)
        cell16 = Cell(16)
        cell17 = Cell(17)
        cell18 = Cell(18)
        cell19 = Cell(19)
        cell20 = Cell(20)
        cell21 = Cell(21)
        cell22 = Cell(22)
        cell23 = Cell(23)
        cell24 = Cell(24, isFinish=True)

        #cell0.south = cell5
        cell0.east = cell1

        cell1.south = cell6
        cell1.east = cell2
        cell1.west = cell0

        cell2.south = cell7
        #cell2.east = cell3
        cell2.west = cell1

        cell3.south = cell8
        #cell3.east = cell4
        #cell3.west = cell2

        cell4.south = cell9
        #cell4.west = cell3

        #cell5.north = cell0
        cell5.south = cell10
        cell5.east = cell6

        cell6.north = cell1
        cell6.south = cell11
        #cell6.east = cell7
        cell6.west = cell5

        cell7.north = cell2
        #cell7.south = cell12
        cell7.east = cell8
        #cell7.west = cell6

        cell8.north = cell3
        cell8.south = cell13
        cell8.east = cell9
        cell8.west = cell7

        cell9.north = cell4
        #cell9.south = cell14
        cell9.west = cell8

        cell10.north = cell5
        cell10.south = cell15
        cell10.east = cell11

        cell11.north = cell6
        #cell11.south = cell16
        #cell11.east = cell12
        cell11.west = cell10

        #cell12.north = cell7
        #cell12.south = cell17
        cell12.east = cell13
        #cell12.west = cell11

        cell13.north = cell8
        cell13.south = cell18
        cell13.east = cell14
        cell13.west = cell12

        #cell14.north = cell9
        cell14.south = cell19
        cell14.west = cell13

        cell15.north = cell10
        cell15.south = cell20
        cell15.east = cell16

        #cell16.north = cell11
        cell16.south = cell21
        #cell16.east = cell17
        cell16.west = cell15

        #cell17.north = cell12
        cell17.south = cell22
        cell17.east = cell18
        #cell17.west = cell16

        cell18.north = cell13
        cell18.south = cell23
        #cell18.east = cell19
        cell18.west = cell17

        cell19.north = cell14
        cell19.south = cell24
        #cell19.west = cell18

        cell20.north = cell15
        #cell20.east = cell21

        cell21.north = cell16
        cell21.east = cell22
        #cell21.west = cell20

        cell22.north = cell17
        #cell22.east = cell23
        cell22.west = cell21

        cell23.north = cell18
        cell23.east = cell24
        #cell23.west = cell22

        cell24.north = cell19
        cell24.west = cell23

        self.cells.append(cell0)
        self.cells.append(cell1)
        self.cells.append(cell2)
        self.cells.append(cell3)
        self.cells.append(cell4)
        self.cells.append(cell5)
        self.cells.append(cell6)
        self.cells.append(cell7)
        self.cells.append(cell8)
        self.cells.append(cell9)
        self.cells.append(cell10)
        self.cells.append(cell11)
        self.cells.append(cell12)
        self.cells.append(cell13)
        self.cells.append(cell14)
        self.cells.append(cell15)
        self.cells.append(cell16)
        self.cells.append(cell17)
        self.cells.append(cell18)
        self.cells.append(cell19)
        self.cells.append(cell20)
        self.cells.append(cell21)
        self.cells.append(cell22)
        self.cells.append(cell23)
        self.cells.append(cell24)

        self.startCell = cell0
        cell0.makeStart()
        self.finishCell = cell24
        cell24.makeFinish()

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

    def getPerformance(self, currentCell):
        curCoords = currentCell.getCoords(self.nrows, self.ncols)
        endCoords = self.finishCell.getCoords(self.nrows, self.ncols)
        return DistanceForm(curCoords, endCoords)
    
    def testValidPath(self, path):
        cell = self.startCell
        for i in path:
            dir = Directions(i)
            match i:
                case Directions.NORTH:
                    if(cell.hasNorth()):
                        cell = cell.getNorth()
                    else:
                        return False
                case Directions.SOUTH:
                    if(cell.hasSouth()):
                        cell = cell.getSouth()
                    else:
                        return False
                case Directions.EAST:
                    if(cell.hasEast()):
                        cell = cell.getEast()
                    else:
                        return False
                case Directions.WEST:
                    if(cell.hasWest()):
                        cell = cell.getWest()
                    else:
                        return False
        if(cell.getCellNum() == self.finishCell.getCellNum()):
            return True
        else:
            return False


