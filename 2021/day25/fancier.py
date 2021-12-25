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

rightCucumbers = set()
downCucumbers = set()

for li, line in enumerate(inp):
    for vi, v in enumerate(line):
        if v == ".": continue
        elif v == ">": rightCucumbers.add((vi, li))
        elif v == "v": downCucumbers.add((vi, li))
        else: assert(False)

Y_LEN = len(inp)
X_LEN = len(inp[0])

def newLoc(x, y, dx, dy):
    return (x + dx) % X_LEN, (y + dy) % Y_LEN

def round(right, down):
    newRight, newDown = set(), set() 

    for (x, y) in right:
        dx, dy = 1, 0
        loc = newLoc(x, y, dx, dy)
        if loc in right or loc in down:
            loc = (x, y)
        newRight.add(loc)

    for (x, y) in down:
        dx, dy = 0, 1
        loc = newLoc(x, y, dx, dy)
        if loc in newRight or loc in down: 
            loc = (x, y)

        newDown.add(loc) 

    return newRight, newDown

def printCuc(right, down):
    for y in range(Y_LEN):
        for x in range(X_LEN):
            print("." if (x, y) not in right and (x, y) not in down else (">" if (x, y) in right else "v" ), end = "")
        print()
i = 0

pRight, pDown = set(), set()
right, down = rightCucumbers, downCucumbers

while pRight != right or pDown != down:
    i += 1
    pRight, pDown = right, down
    right, down = round(right, down)

print(i)


