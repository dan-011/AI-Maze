from interface import *
from player import *
from maze import *

def generatePlayers(k, _maze):
    players = []
    for i in range(k):
        newPlayer = Player()
        newPlayer.enterMaze(maze=_maze)
        players.append(newPlayer)
    return players


def generateStarts(_players, lengthOfPath):
    k = len(_players)
    for org in range(k):
        path = []
        for i in range(lengthOfPath):
            path.append(random.randint(0,3))
        _players[org].setPath(path)

def runGeneration(_players, maze):
    performances = []
    for player in _players:
        #print("Testing path: " + pathStr(player.getPath()))
        player.enterMaze(maze)
        player.runPath(maze)
        performances.append(player.getPerformance())
        if(performances[-1] == 1):
            break
    string = ""
    string += str(performances[0])
    '''for i in range(1, len(performances)):
        string += ' '
        string += str(performances[i])
    print(string)'''
    return performances

def selectParents(_players, perfs):
    performances = perfs.copy()
    indices = [i for i in range(len(_players))]
    ip1 = random.choices(indices, weights=performances)[0]
    ip2 = random.choices(indices, weights=performances)[0]
    while(ip1 == ip2):
        index = indices.index(ip2)
        del indices[index]
        del performances[index]
        ip2 = random.choices(indices, weights=performances)[0]
    p1 = _players[ip1]
    p2 = _players[ip2]

    assert(len(p1.getPath()) == len(p2.getPath()))
    slicePoint = random.randint(0, len(p1.getPath()) - 1)

    childPath1 = p1.getPath()[:slicePoint] + p2.getPath()[slicePoint:]
    childPath2 = p2.getPath()[:slicePoint] + p1.getPath()[slicePoint:]

    return (childPath1, childPath2)

def mutate(numMutations, player):
    muts = set()
    while(len(muts) < numMutations):
        muts.add(random.randint(0, len(player.getPath()) - 1))
    for mut in muts:
        player.getPath()[mut] = random.randint(0, 3)

def generateChildren(_players, performances, numberOfMutations):
    k = len(_players)
    children = []
    while(len(children) < k):
        children_i = selectParents(_players, performances)
        children.append(children_i[0])
        children.append(children_i[1])
    for i in range(len(_players)):
        player = _players[i]
        child = children[i]
        player.setPath(child)
    for chld in _players:
        mutate(numberOfMutations, chld)

def geneticAlgorithm(maze, numPlayers, numberOfMutations, lengthOfPath):
    players = generatePlayers(numPlayers, maze)
    generateStarts(players, lengthOfPath)
    i = 0
    while(True):
    #for i in range(numGenerations):    
        performances = runGeneration(players, maze)
        if(1 in performances):
            ind = performances.index(1)
            solnPath = players[ind].getPath()
            if(len(solnPath) == 1):
                print("stop here")
            print("Found solution with path: " + pathStr(solnPath) + "\nAfter " + str(i) + " generations")
            break
        generateChildren(players, performances, numberOfMutations)
        i += 1
    

def main():
    maze = Maze(10, 10)
    maze.buildMaze()
    numberOfAgents = 10
    numberOfMutations = 10
    lengthOfPath = 100
    geneticAlgorithm(maze, numberOfAgents, numberOfMutations, lengthOfPath)

main()
