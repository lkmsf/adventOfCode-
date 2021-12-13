from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math

with open("12.in") as f:
#with open("test12.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [x.split("-") for x in inp]

paths = defaultdict(list)
for s, e in inp:
    paths[s].append(e)
    paths[e].append(s)

def numPaths(curr, visited, path):
    if curr == "end": 
        print(path)
        return 1

    total = 0
    for e in paths[curr]:
        if e in visited:
            continue
        newVisted = visited.copy()
        if curr[0].islower():
            newVisted.add(curr)
        total += numPaths(e, newVisted, path + "," + e)

    return total


print(numPaths("start", {"start"}, "start"))
