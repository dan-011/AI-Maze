import player as pl
import maze as mz
import sys
from interface import *

maze = mz.Maze()
#maze.buildMaze()
maze.buildTestMaze()


player1 = pl.Player()

player1.enterMaze(maze)
print("Entering the maze...")

while(True):
    input = sys.stdin.readline()
    input = input.strip().lower()
    if(len(input) == 0):
        continue
    dir = -1
    try:
        dir = direction[input[0]]
    except KeyError:
        1 == 1
    
    if(dir < 0):
        if(input == "check finish"):
            if(player1.checkFinish()):
                print("Finished")
                sys.exit()
            else:
                print("Not finished")
        elif(input == "check start"):
            player1.checkStart()
        elif(input == "look"):
            player1.lookAround()
        elif(input == "die"):
            print("dies")
            break
        else:
            print("'" + input + "' is not a valid command")
    else:
        player1.move(dir)
