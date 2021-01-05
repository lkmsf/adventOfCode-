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
            currLoc = tuple(sum(x) for x in zip(currLoc, delta)) 
        tiles[currLoc] = not tiles[currLoc]
    part1 = sum(tiles.values())

    tiles = {key for key, val in tiles.items() if val} 

    for i in range(100): 
        tiles = doRound(tiles)
        print(i + 1, len(tiles))

    part2 = len(tiles) 
    print(f"part1: {part1}, part2: {part2}")


def doRound(tiles): 
    newTiles = set()  
    surroundingTiles = set() 
    for key in tiles: 
        diff, n= getNeighbors(key, tiles)
        surroundingTiles |= diff
        if not(n == 0 or n > 2) : #black 
            newTiles.add(key)

    for key in surroundingTiles: 
        _, n= getNeighbors(key, tiles)
        if n == 2:  #white 
            newTiles.add(key)

    return newTiles 

def getNeighbors(key, t): 
    diff = set()  
    n = 0 
    for idx in dr.values(): 
        newKey = tuple(sum(x) for x in zip(key, idx)) 
        if newKey not in t:    
            diff.add(newKey) 
        else: 
            n += 1
    return diff, n 

if __name__ == "__main__":
    main()
