import os
def writeConnectedMaze(nrows, ncols):
    k = nrows * ncols
    try:
        os.remove(str(k) + "_length_maze.txt")
    except Exception:
        1 == 1
    output = open(str(k) + "_length_maze.txt", 'w')
    output.write("cell0 = Cell(0, isStart=True)\n")
    for i in range(1, k-1):
        output.write("cell" + str(i) + " = Cell(" + str(i) + ")\n")
    output.write("cell" + str(k-1) + " = Cell(" + str(k-1) + ", isFinish=True)\n")
    output.write('\n')
    # modulo ncols
    for i in range(k):
        if(i >= ncols): # can go north
            northCell = i - ncols
            output.write("cell" + str(i) + ".north = cell" + str(northCell) + '\n')
        if(i < k - ncols): # can go south
            southCell = i + ncols
            output.write("cell" + str(i) + ".south = cell" + str(southCell) + '\n')
        if((i + 1) % ncols != 0): # can go east
            eastCell = i + 1
            output.write("cell" + str(i) + ".east = cell" + str(eastCell) + '\n')
        if(i % ncols != 0): # can go west
            westCell = i - 1
            output.write("cell" + str(i) + ".west = cell" + str(westCell) + '\n')        
        output.write('\n')

    for i in range(k):
        output.write("self.cells.append(cell" + str(i) + ")\n")
    output.write('\n')
    output.write("self.startCell = cell0\n")
    output.write("cell0.makeStart()\n")
    output.write("self.finishCell = cell" + str(k-1) + "\n")
    output.write("cell" + str(k-1) + ".makeFinish()")
    output.close()

writeConnectedMaze(5, 5)