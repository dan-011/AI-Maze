import os
import sys
import random
try:
    os.remove("maze_file1.txt")
except Exception:
    1 == 1

def build100x100Soln():
    visited = set()
    visited.add(0)
    path = []
    directions = []
    cellNum = 0
    while(cellNum != 9999):
        l = []
        if cellNum - 100 > -1 and cellNum-100 not in visited:
            l.append('N')
        if cellNum < 9900 and cellNum + 100 not in visited:
            l.append('S')
        if cellNum % 100 < 99 and cellNum+1 not in visited:
            l.append('E')
        if cellNum % 100 != 0 and cellNum-1 not in visited:
            l.append('W')
        if(len(l) == 0):
            print("run again")
            return
        dir = random.choice(l)
        directions.append(dir)
        visited.add(cellNum)
        path.append(cellNum)
        match dir:
            case 'N':
                cellNum -= 100
            case 'S':
                cellNum += 100
            case 'E':
                cellNum += 1
            case 'W':
                cellNum -= 1
    string = ""
    for direction in directions:
        string += direction
    print(string)
    string = ""
    for cell in path:
        string += str(cell)

build100x100Soln()
sys.exit()

def createCellStr(cellNum):
    cellStr = "(" + str(cellNum)
    l = ['N','S','E','W']
    for dir in l:
        hasDir = bool(random.getrandbits(1))
        if(hasDir):
            cellStr += "," + dir
    cellStr += ")"
    #return cellStr
    return str(cellNum)

print("Enter Maze Dimensions:")
output = open("maze_file1.txt", "w")
input = sys.stdin.readline().strip().split()
n1 = int(input[0])
n2 = int(input[1])
output.write(str(n1) + '\t' + str(n2) + '\n')
cellNum = 0
for i in range(n1):
    for j in range(n2):
        output.write(createCellStr(cellNum) + '\t')
        cellNum += 1
    output.write('\n')
output.close()