from collections import Counter, defaultdict
from itertools import combinations, chain
from os import posix_spawn 
import re
import statistics
import math
import sys
import heapq

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

orig = [list(map(int, list(x))) for x in inp]
inp = [[None] * len(orig) * 5 for _ in range(len(orig) * 5)]

for i in range(5):
    for j in range(5):
        for x in range(len(orig)):
            for y in range(len(orig)):
                inp[x + (i * len(orig))][y + (j * len(orig))]  = ((orig[x][y] + i + j - 1) % 9) + 1

LEN = len(inp)

def neighbors(pt):
    x, y = pt
    result = [(x + dx, y + dy) for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]]
    return [(a, b) for a,b in result if a in range(LEN) and b in range(LEN)]

curr = (0, 0)

nextPossibles = []
heapq.heappush(nextPossibles, (0, curr))

alreadySet = set()
costs = {curr: 0}

while nextPossibles: 
    cost, curr = heapq.heappop(nextPossibles) 
    alreadySet.add(curr)

    x, y = curr 
    costsFromPath = cost + inp[x][y]

    ns = neighbors(curr)# - alreadySet
    for a, b in ns:
        if (a, b) not in costs or costs[(a, b)] > costsFromPath:
            costs[(a, b)] = cost + inp[a][b]
            heapq.heappush(nextPossibles, (costs[(a, b)],(a, b)))


print(costs[(LEN - 1, LEN - 1)])