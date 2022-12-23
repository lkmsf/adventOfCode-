from collections import Counter, defaultdict, deque
from itertools import combinations, chain, accumulate
import numpy as np
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines()

inp = np.asarray([list(x) for x in inp])

start, end = None, None
starts = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i, j] == "S":
            start = (i, j)
            inp[start] = "a"
        if inp[i, j] == "E":
            end = (i, j)
            print(end)
            inp[end] = "z"
        if inp[i, j]  == "a":
            starts.append((i, j))

print(start, end)
print(starts)

a, b = start

def getNeighbors(i, j):
    ns = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    possibles = [(i + dx, j + dy) for dx, dy in ns]
    possibles = [x for x in possibles if x[0] in range(len(inp)) and x[1] in range(len(inp[0]))] 
    possibles = [x for x in possibles if ord(inp[i, j]) + 1 >= ord(inp[x])]
    return possibles

def bfs(startHere):
    visted = set([startHere])
    paths = deque([[startHere]])
    while True:
        if not paths: return None
        currPath = paths.popleft()
        currLast = currPath[-1]

        for neighbor in getNeighbors(*currLast): 
            if neighbor in visted: continue
            visted.add(neighbor)

            nextPath = currPath.copy()
            nextPath.append(neighbor)
            paths.append(nextPath)
            if neighbor == end:
                return nextPath

best = 99999999999999
for start in starts:
    l = bfs(start)
    if l == None: continue
    best = min(len(l) -1, best)

print(best)