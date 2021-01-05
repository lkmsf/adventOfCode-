from itertools import combinations, chain 
from copy import deepcopy 
import re

from collections import Counter, defaultdict

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close()
    
    part1, part2 = 0, 0 
    
    points = defaultdict(lambda: ".") 
    
    #initialize list 
    for i in range(len(inp)): 
        for j in range(len(inp[0])): 
            points[(0, i, j)] = inp[i][j]

    for layer in range(-1, 2): 
        for i in range(-1, len(inp) + 1): 
            for j in range(-1, len(inp[0]) + 1): 
                points[layer, i, j] #lazy way of adding values to defaultdict 

    for i in range(6): 
        points = doRound(points)
        #printWell(points)

    part1 = sum(e == "#" for e in points.values())


    #part2 
    points = defaultdict(lambda: ".") 
    
    for i in range(len(inp)): 
        for j in range(len(inp[0])): 
            points[(0, 0, i, j)] = inp[i][j]

    for dim in range(-1, 2): 
        for layer in range(-1, 2): 
            for i in range(-1, len(inp) + 1): 
                for j in range(-1, len(inp[0]) + 1): 
                    points[dim, layer, i, j] #lazy way of adding values to defaultdict 

    for i in range(6): 
        points = doRound4d(points)
        #printWell(points)

    part2 = sum(e == "#" for e in points.values())


    print(f"part1: {part1}, part2: {part2}")

def doRound(points): 
    newDict = deepcopy(points) 

    for p, val in points.items(): 
        neighbors = getNeighbors(newDict, points, *p) 
        count = sum(x == "#" for x in neighbors) 

        if isActive(val) and not (2 <= count <= 3): 
            newDict[p] = "."
        elif not isActive(val) and count == 3:  
            newDict[p] = "#" 
    return newDict

def getNeighbors(newDict, points, layer, row, col): 
    neighbors = []

    for dLayer in range(-1, 2): 
        for dRow in range(-1, 2): 
            for dCol in range(-1, 2): 
                if dLayer == dRow == dCol == 0: continue 

                neighbor = (dLayer + layer, dRow + row, dCol + col) 

                if neighbor in points: 
                    neighbors.append(points[neighbor]) 
                else:
                    newDict[neighbor]

    return neighbors 


def isActive(e): 
    return e == "#" 

def printWell(d): 
    items = sorted(d.items())
    maxVal, minVal = items[-1][0], items[0][0]
    for layer in range(minVal[0], maxVal[0] + 1): 
        print(f"{layer}")
        for row in range(minVal[1], maxVal[1] + 1): 
            for col in range(minVal[2], maxVal[2] + 1): 
                print(d[(layer, row, col)], end = "")
            print() 

    print("--------------------")

#part 2

def doRound4d(points): 
    newDict = deepcopy(points) 

    for p, val in points.items(): 
        neighbors = getNeighbors4d(newDict, points, *p) 
        count = sum(x == "#" for x in neighbors) 

        if isActive(val) and not (2 <= count <= 3): 
            newDict[p] = "."
        elif not isActive(val) and count == 3:  
            newDict[p] = "#" 
    return newDict

def getNeighbors4d(newDict, points, dim, layer, row, col): 
    neighbors = []

    for dDim in range(-1, 2): 
        for dLayer in range(-1, 2): 
            for dRow in range(-1, 2): 
                for dCol in range(-1, 2): 
                    if dDim == dLayer == dRow == dCol == 0: continue 

                    neighbor = (dDim + dim, dLayer + layer, dRow + row, dCol + col) 

                    if neighbor in points: 
                        neighbors.append(points[neighbor]) 
                    else:
                        newDict[neighbor]

    return neighbors 



#    result = [[[[i for i in s] for s in inp]]] 
#    result = addBorders4d(result)
#    
#
#    for i in range(1): 
#        print(f"4d: {i}")
#        result = doCycle4d(result)
#
#    part2 = len([j for x in result for y in x for i in y for j in i if i == "#"])
#

#original part 1
#def main(): 
    #result = [[[i for i in s] for s in inp]]

    #for i in range(6): 
    #    result = doCycle(result)
    #    #printWell(result)
   
    #
    #part1 = len([i for x in result for y in x for i in y if i == "#"])


#def doCycle(start): 
#    result = [] 
#
#    addBorders(start) 
#
#    for i, l in enumerate(start): 
#
#        layer = deepcopy(l) 
#        newLayer = []
#
#        
#        for j, row in enumerate(layer): 
#            newRow = []
#
#            for k, elem in enumerate(row): 
#                neighbors = getNeighbors(start, i, j, k)
#                numActive = neighbors.count("#")
#                newElem = "."
#                if elem == "#" and (numActive == 2 or numActive == 3): 
#                    newElem = "#" 
#                elif elem == "." and numActive == 3: 
#                    newElem = "#" 
#                newRow.append(newElem) 
#
#            newLayer.append(newRow)
#        result.append(newLayer)
#
#    return result 
#
#def addBorders(s): 
#    height, width = len(s[0]), len(s[0][0])
#    newLayer = [["."] * width ] * height
#    s.insert(0, deepcopy(newLayer))
#    s.append(deepcopy(newLayer)) 
#
#
#    for layer in s: 
#        l = ['.'] * width 
#        layer.insert(0, deepcopy(l)) 
#        layer.append(deepcopy(l))
#
#        for i, row in enumerate(layer): 
#            newRow = row.copy() #still not sure why I have to copy the row here 
#            newRow.insert(0, '.' )
#            newRow.append('.' )
#            layer[i] = newRow
#
#
#def getNeighbors(start, i, j, k): 
#    neighbors = []
#    for di in range(-1, 2): 
#        if not (0 <= (i + di) < len(start)): continue 
#
#        for dj in range(-1, 2): 
#            if not (0 <= (j + dj) < len(start[0])): continue 
#
#            for dk in range(-1, 2): 
#                if not (0 <= (k + dk) < len(start[0][0])): continue 
#                if di == dj == dk == 0: continue 
#               
#                elem = start[i + di][j + dj][k + dk]
#
#                neighbors.append(elem) 
#
#    return neighbors
#
#def printWell(d): 
#    for i, l in enumerate(d): 
#        print(f"z = {i}")
#        for j in l: 
#            print(j)
#        print() 
#    print("----------")
#
#
##part 2 functions 
#
#def doCycle4d(start): 
#    result = [] 
#
#    start = addBorders4d(start) 
#
#
#    for x, outer in enumerate(start): 
#        newOuter = []
#        for i, layer in enumerate(outer): 
#            newLayer = []
#            for j, row in enumerate(layer): 
#                newRow = []
#                for k, elem in enumerate(row): 
#                    neighbors = getNeighbors4d(start, x, i, j, k)
#                    numActive = neighbors.count("#")
#                    newElem = "."
#                    if elem == "#" and (numActive == 2 or numActive == 3): 
#                        newElem = "#" 
#                    elif elem == "." and numActive == 3: 
#                        newElem = "#" 
#                    newRow.append(newElem) 
#
#                newLayer.append(newRow)
#            newOuter.append(newLayer)
#        result.append(newOuter)
#
#    return result 
#
#def addBorders4d(s): 
#    depth, layers, height, width = len(s), len(s[0]), len(s[0][0]), len(s[0][0][0])
#    
#    result = []
#    for d in range(depth + 2):  
#        currOuter = []
#        allInactiveD = (d == 0 or d == depth + 1) 
#
#        for h in range(layers + 2): 
#            currLayer = []
#            allInactiveH = allInactiveD or (h == 0 or h == layers + 1) 
#
#            for w in range(height + 2): 
#                currRow = []
#                allInactiveW = allInactiveH or (w == 0 or w == height + 1) 
#
#                for i in range(width + 2):  
#                    allInactiveI = allInactiveW or (i == 0 or i == width + 1) 
#                    currRow.append("." if allInactiveI else s[d - 1][h - 1][w - 1][i - 1]) 
#
#                currLayer.append(currRow)
#            currOuter.append(currLayer)
#        result.append(currOuter)
#
#    return result 
#
#    
#
#
#
#def getNeighbors4d(start, x, i, j, k): 
#    neighbors = []
#    for dx in range(-1, 2): 
#        if not (0 <= (x + dx) < len(start)): continue 
#
#        for di in range(-1, 2): 
#            if not (0 <= (i + di) < len(start[0])): continue 
#
#            for dj in range(-1, 2): 
#                if not (0 <= (j + dj) < len(start[0][0])): continue 
#
#                for dk in range(-1, 2): 
#                    if not (0 <= (k + dk) < len(start[0][0][0])): continue 
#                    if di == dj == dk == dx == 0: continue 
#                    
#                    elem = start[x + dx][i + di][j + dj][k + dk]
#
#                    neighbors.append(elem) 
#
#    return neighbors

if __name__ == "__main__":
    main()
