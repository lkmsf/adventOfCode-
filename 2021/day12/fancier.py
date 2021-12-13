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

def numPaths(curr, visited, path, useTwice):
    if curr == "end": 
        return 1
    total = 0
    for e in paths[curr]:

        newUseTwice = useTwice

        if e in visited:
            if (e == "start" or not useTwice):
                continue
            newUseTwice = False

        newVisted = visited.copy()
        if e[0].islower():
            newVisted.add(e)

        total += numPaths(e, newVisted, path + "," + e, newUseTwice)

    return total

print(numPaths("start", {"start"}, "start", True))
