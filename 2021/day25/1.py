from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [list(x) for x in inp]

cucumbers = {}

for li, line in enumerate(inp):
    for vi, v in enumerate(line):
        if v == ".": continue
        dir = (1, 0) if v == ">" else (0, 1)
        cucumbers[(vi, li)] = dir

Y_LEN = len(inp)
X_LEN = len(inp[0])


def newLoc(x, y, dx, dy):
    return (x + dx) % X_LEN, (y + dy) % Y_LEN

def round(fish):
    newPlaces = dict()

    for (x, y), (dx, dy) in fish.items():
        if (dx, dy) == (0, 1): continue

        loc = newLoc(x, y, dx, dy)
        if loc in fish:
            loc = (x, y)

        newPlaces[loc] = (dx, dy)

    for (x, y), (dx, dy) in fish.items():
        if (dx, dy) == (1, 0): continue

        loc = newLoc(x, y, dx, dy)
        if loc in newPlaces or (loc in fish and fish[loc] == (0, 1)):
            loc = (x, y)

        newPlaces[loc] = (dx, dy)

    return newPlaces


def printCuc(cuc):
    for y in range(Y_LEN):
        for x in range(X_LEN):
            print("." if (x, y) not in cuc else (">" if cuc[(x, y)] == (1, 0) else "v" ), end = "")
        print()


curr = cucumbers
prev = {}
i = 0
printCuc(curr)
while prev != curr:
    print(i)
    i += 1
    prev = curr
    curr = round(curr)
    #printCuc(curr)

print(i)


