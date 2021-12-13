from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math

with open("11.in") as f:
#with open("test11.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [[int(y) for y in list(x)] for x in inp]

def getNeighbors(x, y):
    n = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0: continue
            if x + dx in range(len(inp)) and y + dy in range(len(inp[0])):
                n.append((x + dx, y + dy))
    return n

def addEnergyToNeighbors(x, y, flashes):
    global totalFlashes
    if inp[x][y] <= 9:
        return
    elif (x,y) in flashes:
        return
    else:
        flashes.add((x,y))

    for nx, ny in getNeighbors(x, y):
        inp[nx][ny] += 1
    for nx, ny in getNeighbors(x, y):
        addEnergyToNeighbors(nx, ny, flashes)

totalFlashes = 0
for i in range(100):
    flashes = set()

    # add one to each
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            inp[x][y] += 1

    #now flash if needed
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            addEnergyToNeighbors(x, y, flashes)

    # now set those to 0 
    for x, y in flashes:
        inp[x][y] = 0

    totalFlashes += len(flashes)

print(totalFlashes)
