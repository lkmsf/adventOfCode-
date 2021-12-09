from collections import Counter, defaultdict
from itertools import combinations, chain, count 
import re
import sys

with open("9.in") as f:
#with open("test9.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [list(map(int, list(x))) for x in inp]


low = []

def getNeighbors(inp, li, vi):
    pts = []

    if li >= 1:
        pts.append(inp[li - 1][vi])
    # below 
    if li < len(inp) - 1:
        pts.append(inp[li + 1][vi])

    # to left
    if vi >= 1:
        pts.append(inp[li][vi-1])
    # right
    if vi < len(inp[0]) - 1:
        pts.append(inp[li][vi + 1])

    return pts

for i, line in enumerate(inp):
    for iV, val in enumerate(line):
        n = getNeighbors(inp, i, iV)
        if all(val < x for x in n):
            low.append((i, iV))

basins = []


def countBasin(li, vi, seen):
    if (li, vi) in seen:
        return 0
    seen.add((li, vi))
    if li < 0 or li >= len(inp):
        return 0
    if vi < 0 or vi >= len(inp[0]):
        return 0
    if inp[li][vi] == 9:
        return 0
    return 1 + countBasin(li - 1, vi, seen) + countBasin(li + 1, vi, seen) + countBasin(li, vi - 1, seen) + countBasin(li, vi + 1, seen)

for l in low:
    il, iv = l
    print(inp[il][iv])
    curr = 0
    row = inp[l[0]]
    col = [x[l[1]] for x in inp] 
    
    #count rows
    seen = set()
    basins.append(countBasin(il, iv, seen))

result = sorted(basins)
print(basins)
print(result[-1] * result[-2] * result[-3])
