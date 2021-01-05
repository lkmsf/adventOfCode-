from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import numpy as np 
import math
from copy import deepcopy

TOTAL = 144 
SIDE = int(math.sqrt(TOTAL) ) 

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read()
    f.close()
    
    inp = inp.split("\n\n")
    inp = {int(re.findall(r"\d+", e)[0]):  e.splitlines()[1:] for e in inp} 
    
    tiles = {}
    for key, val in inp.items(): 
        val = [list(i) for i in val]
        curr = np.array(val)
        tiles[key] = curr

    part1, part2 = 0, 0 

    image = []

    part1 = math.prod(findCorners(tiles)) 

    #part 2
    edges = getEdgeList(tiles)
    pairs =  [val for val in edges.values() if len(val) == 2]
    adjList = getAdjList(pairs)

    puzzle = np.array([[0] * SIDE] * SIDE)
    solvePuzzle(adjList, puzzle)
    puzzle = np.rot90(np.flipud(puzzle)) 
    print(puzzle)
        

    #now need to figure out orientation - yay
    pairs =  {tuple(sorted(val)) : key for key, val in edges.items() if len(val) == 2} 
    
    for row in range(SIDE): 
        for col in range(SIDE): 
            tiles[puzzle[row, col]] = matchEdges(row, col, pairs, puzzle, tiles)[1: -1, 1: -1]

    #for row in range(SIDE): 
    #    for line in range(10): 
    #        for col in range(SIDE): 
    #            print(tiles[puzzle[row, col]][line, :], end = " ")
    #        print()
    #    print()

    
   # newImage = np.array([[""] * 10 *  SIDE] * 10 * SIDE)
   # for row in range(SIDE): 
   #     for col in range(SIDE): 
   #         for i in range(10): 
   #             for j in range(10): 
   #                 newImage[row * 10 + i, col * 10 + j] = tiles[puzzle[row, col]][i, j]


   # for i in range(10*SIDE):  
   #     for j in range(10*SIDE):  
   #         print(newImage[i, j],  end = " ")
   #     print()

   # return 

    #for row in range(SIDE): 
    #    for col in range(SIDE): 
    #        tiles[puzzle[row, col]] = tiles[puzzle[row, col]][1:-1, 1:-1]


    newImage = np.array([[""] * 8 * SIDE] * 8 * SIDE)
    for row in range(SIDE): 
        for col in range(SIDE): 
            for i in range(8): 
                for j in range(8): 
                    newImage[row * 8 + i, col * 8 + j] = tiles[puzzle[row, col]][i, j]
    
    for i in range(8*SIDE):  
        for j in range(8*SIDE):  
            print(newImage[i, j], end = " ")
        print()

     
    seaMonster =    [ 
    "                  # ",
    "#    ##    ##    ###", 
    " #  #  #  #  #  #   " ] 

    seaMonster = [[i == "#" for i in x] for x in seaMonster]

    for _ in range(4): 
        image = newImage.copy()
        part2 = countMonsters(image, seaMonster)
        if part2 != 0: break

        image = np.fliplr(newImage) 
        part2 = countMonsters(image, seaMonster)
        if part2 != 0: break

        image= np.flipud(newImage) 
        part2 = countMonsters(image, seaMonster)
        if part2 != 0: break

        newImage = np.rot90(newImage)

    numH = len([1 for x in range(SIDE * 8) for y in range(SIDE * 8) if newImage[x, y] == "#"])
    part2 = numH - part2 * 15
    print(f"part1: {part1}, part2: {part2}")


def countMonsters(image, monster): 
    count = 0
    rows, cols = image.shape 
    for x in range(rows - 3): 
        for y in range(cols - len(monster[0])): 
            count += isMonster(image, x, y, monster)
    return count 

def isMonster(image, x, y, monster): 
    for i in range(3): 
        for j in range(len(monster[0])): 
            if monster[i][j]: 
                if image[x + i, y + j] != "#": 
                    return False 

    return True 


def matchEdges(row, col, pairs, puzzle, tiles): 
    tileN = puzzle[row, col]
    tile = tiles[tileN]

    n = [puzzle[c] if c != "X" else "X" for c in getNeighbors(row, col)]
    matchingRows = [pairs[tuple(sorted([tileN, c]))] if c != "X" else "X" for c in n]

    for _ in range(4): 
        newTile = tile.copy() 
        if(isValid(newTile, matchingRows)): return newTile 

        newTile = np.fliplr(tile) 
        if(isValid(newTile, matchingRows)): return newTile 

        newTile = np.flipud(tile) 
        if(isValid(newTile, matchingRows)): return newTile 

        tile = np.rot90(tile)

    assert False 

def isValid(tile, matchingRows): 
    for i in range(4): 
        if matchingRows[i] == "X": continue 
        row = matchingRows[i]
        if i == 0: #top
            if not (all(getTopEdge(tile) == row) or all(getTopEdge(tile) == row[::-1])): 
                return False 
        elif i == 1: #right
            if not (all(getRightEdge(tile) == row) or all(getRightEdge(tile) == row[::-1])): 
                return False 
        elif i == 2: #bottom
            if not (all(getBotEdge(tile) == row) or all(getBotEdge(tile) == row[::-1])): 
                return False 
        elif i == 3: #left
            if not (all(getLeftEdge(tile) == row) or all(getLeftEdge(tile) == row[::-1])): 
                return False 

    return True 
         


def getNeighbors(row, col): 
    n = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
    n = [(r, c) if (0 <= r < SIDE) and (0 <= c < SIDE) else "X" for r, c in n ] 
    return n

def getTopEdge(tile): 
    return tile[0, :]

def getBotEdge(tile): 
    return tile[-1, :]

def getLeftEdge(tile): 
    return tile[:, 0]

def getRightEdge(tile): 
    return tile[:, -1]



def solvePuzzle(adjList, puzzle): 
    #probably don't need to solve the entire border first, it's just cuter 
    solveBorder(adjList, puzzle)
    for i in range(1, SIDE - 1): 
        solveRowAcross(i, adjList, puzzle)

def solveBorder(adjList, puzzle): 
    #since orientation doesn't matter yet, we can place corner and the start of the 
    #two directions (let's assume we place top left)
    corners = set([x for x, val in adjList.items() if len(val) == 2]) 
    c = corners.pop();  

    puzzle[0, 0] = c          
    start1, start2 = adjList[c]

    puzzle[0, 1] = start1;      removeEntry(adjList, c, start1)
    puzzle[1, 0] = start2;      removeEntry(adjList, c, start2)
    
    outerEdge = set([x for x, val in adjList.items() if len(val) == 3]) 

    solveRowAcross(0, adjList, puzzle, outerEdge)
    solveColAcross(0, adjList, puzzle, outerEdge)
    
    #fill in other corners 
    blC = getPointAdjTo([puzzle[SIDE - 2, 0]], adjList, corners);    corners.remove(blC) 
    trC = getPointAdjTo([puzzle[0, SIDE - 2] ], adjList, corners);   corners.remove(trC) 
    brA =  corners.pop() 
    
    puzzle[SIDE - 1,        0] = blC;    removeEntry(adjList, puzzle[SIDE - 2, 0], blC)
    puzzle[0,        SIDE - 1] = trC;    removeEntry(adjList, puzzle[0, SIDE - 2], trC) 
    puzzle[SIDE - 1, SIDE - 1] = brA
    
    #Finish Border 
    solveRowAcross(-1, adjList, puzzle, outerEdge)
    solveColAcross(-1, adjList, puzzle, outerEdge)


def solveRowAcross(n, adjList, puzzle, possibles = {}): 
    start = 1 if puzzle[n, 1] == 0 else 2

    for i in range(start, SIDE - 1): 
        prev = puzzle[n, i-1]
        mustBeAdjTo = [prev]
        if n != 0 and n != -1: mustBeAdjTo.append(puzzle[n - 1, i])
        nextPiece = getPointAdjTo(mustBeAdjTo, adjList, possibles)
        puzzle[n, i] = nextPiece;   removeEntry(adjList, prev, nextPiece)


def solveColAcross(n, adjList, puzzle, possibles = {}): 
    start = 1 if puzzle[1, n] == 0 else 2

    for i in range(start, SIDE - 1): 
        prev = puzzle[i-1, n]
        mustBeAdjTo = [prev]
        if n != 0 and n != -1: mustBeAdjTo.append(puzzle[i - 1])
        nextPiece = getPointAdjTo(mustBeAdjTo, adjList, possibles)
        puzzle[i, n] = nextPiece;   removeEntry(adjList, prev, nextPiece)

def getPointAdjTo(adjcentTo, adjList, possibles = set()): 
    result = set.intersection(*[adjList[p] for p in adjcentTo])
    if possibles: result &= possibles
    assert len(result) == 1
    return result.pop() 

def removeEntry(adjList, a, b): 
    adjList[a].remove(b)
    if not adjList[a]: adjList.pop(a)

    adjList[b].remove(a)
    if not adjList[b]: adjList.pop(b)


def getAdjList(pairs): 
    d = defaultdict(set)

    for a, b in pairs: 
        d[a].add(b)
        d[b].add(a)

    return d


def getEdgeList(tiles): 
    edges = defaultdict(list)
    for key, val in tiles.items(): 
        for i in [val[0,:], val[-1,:], val[:,0], val[:,-1]]: 
            edges[tuple(i)].append(key) 
            edges[tuple(i[::-1])].append(key) 
    return edges 
    
    
def findCorners(tiles): 
    edges = getEdgeList(tiles)
    result =  [val[0] for val in edges.values() if len(val) == 1]

    #we check for both directions so each edge is counted twice 
    result = [key for key, c in Counter(result).items() if c == 4 ] 
    return(result)
    

def arrangeTiles(td, image, depth): 
    print(" " * depth, f"current state; {image}")
    if depth == 10: 
        print(" " * depth, "returning")
        return True 

    #if len(image) > 0 and not isValid(td, image): 
     #   return False 
    
    if len(image) > 1 and image[1] == 1951: 
        print(" " * depth, "Nope invalid")
        return False 

    if len(image) == TOTAL: 
        print(" " * depth, "Yay that worked!")
        return True 
    
    for key, val in td.items(): 
        print(" " * depth, f"{key}?")
        if key in image: 
            print(" " * depth, "Already used")
            continue

        d = deepcopy(td)
        original = val.copy()
        image.append(key) 

        #try every rotation 
        for j in range(4): 
            print(f"On my {j}th rotation") 

            #no flip 
            if arrangeTiles(d, image, depth + 1): 
                print(" " * depth, "No flip worked!!")
                return True 

            #flip horizontal 
            td[key] = np.fliplr(val) 
            if arrangeTiles(td, image, depth + 1): 
                print(" " * depth, "lr flip worked!!")
                return True 

            #flip vertical 
            td[key] = np.flipud(val) 
            if arrangeTiles(td, image, depth + 1): 
                print(" " * depth, "ud flip worked!!")
                return True 

            original =  np.rot90(original.copy()) 

            image = image[:-1]

    print(" " * depth, "Nothing worked??")
    return False 

#def isValid(tileD, image):  
#    i = len(image) - 1
#    o = tileD[image[i]]
#
#    #check left
#    if i > 0: 
#        n = tileD[image[i - 1]]
#        if not all(n[:, -1] == o[:, 0]): 
#            return False 
#
#    #check above 
#    if i > SIDE: 
#        n = tileD[image[i - SIDE]]
#        if not all(n[-1, :] == o[0,:]):
#            return False 
#
#    return True 

if __name__ == "__main__":
    main()
