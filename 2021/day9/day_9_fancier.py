from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import math

with open("9.in") as f:
#with open("test9.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [list(map(int, list(x))) for x in inp]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

low = []

def inBounds(li, vi):
    return (li in range(len(inp))) and (vi in range(len(inp[0])))

def getNeighbors(li, vi):
    return [inp[li + dx][vi + dy] for dx, dy in dirs if inBounds(li + dx, vi + dy)]

for li, line in enumerate(inp):
    for vi, val in enumerate(line):
        if all(val < x for x in getNeighbors(li, vi)):
            low.append((li, vi))

scores = [inp[li][vi] + 1 for li, vi in low]
print(sum(scores))


# part 2

def countBasin(li, vi, seen):
    if (li, vi) in seen or not inBounds(li, vi) or inp[li][vi] == 9:
        return 0
    seen.add((li, vi))

    return 1 + sum(countBasin(li + dx, vi + dy, seen) for dx, dy in dirs)

basins = [countBasin(li, vi, set()) for li, vi in low]
result = sorted(basins)
print(math.prod(result[-3:]))

