from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
from copy import deepcopy 
import matplotlib.pyplot as plt

dr = {"e": (0, -1), "se" : (1, -1), "sw": (1, 0), "w": (0, 1),  "nw":(-1, 1), "ne":(-1, 0)}

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close()

    ins = [re.findall(r"(se|sw|nw|ne|e|w)", x) for x in inp]

    part1, part2 = 0, 0 
    
    #true -> black, false->white 
    tiles = defaultdict(lambda: False)
    
    for l in ins: 
        currLoc = (0, 0)
    
        for step in l: 
            delta = dr[step]
            currLoc = tuple(sum(x) for x in zip(currLoc, delta)) #][currLoc[0] + delta[0], currLoc[1] + delta[1]) 
        tiles[currLoc] = not tiles[currLoc]
    part1 = sum(tiles.values())


    maxX = max([a for a, b in tiles]) 
    minX = min([a for a, b in tiles]) 
    maxY = max([b for a, b in tiles]) 
    minY = min([b for a, b in tiles]) 

    for i in range(minX, maxX + 2): 
        for j in range(minY, maxY + 2): 
            tiles[i, j]

    #tiles = [x for x in tiles if x[1]]] 
    for i in range(100): 
        tiles = doRound(tiles)
        print(i + 1, sum(tiles.values()))

    part2 = sum(tiles.values())
    print(f"part1: {part1}, part2: {part2}")


def doRound(tiles): 
    newTiles = defaultdict(lambda: False)
    surroundingTiles = set() 
    for key, val in tiles.items(): 
        diff, neighbors = getNeighbors(key, tiles)
        surroundingTiles |= diff
        n = sum(neighbors)
        if val: #black 
            newTiles[key] = not (n == 0 or n > 2) 
        else:  #white 
            newTiles[key] =  n == 2 

    for i in surroundingTiles: newTiles[i] 

    return newTiles 

def getNeighbors(key, t): 
    diff = set()  
    neighbors = list() 
    for idx in dr.values(): 
        newKey = tuple(sum(x) for x in zip(key, idx)) #(idx[0] + key[0], idx[1] + key[1])
        if newKey not in t:    
            diff.add(newKey) 
        else: 
            neighbors.append(t[newKey])
    return diff, neighbors 

if __name__ == "__main__":
    main()
