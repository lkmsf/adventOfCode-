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

inp = [x.split() for x in inp]
inp = [(x[0], int(x[1])) for x in inp]

dir = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

head = [0, 0]
tail = [0, 0]
locs = []
locs.append(tail)

def updateTail(h, t):
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1: 
        return t
    xDiff = 0 if h[0] == t[0] else 1 if h[0] > t[0] else -1
    yDiff = 0 if h[1] == t[1] else 1 if h[1] > t[1] else -1
    return [tail[0] + xDiff, tail[1] + yDiff]

for d, a in inp:
    xD, yD = dir[d]
    print(d, a)
    for i in range(a):
        head = [head[0] + xD, head[1] + yD]
        tail = updateTail(head, tail)
        locs.append(tail)
        print(tail)
    print()

print(len(set(map(tuple, locs))))