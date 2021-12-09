from collections import Counter, defaultdict
from itertools import combinations, chain 
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
            print(val, n)
            low.append(val)

print(low)
scores = [x + 1 for x in low]
print(sum(scores))

