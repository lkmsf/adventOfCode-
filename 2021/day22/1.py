from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" #if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    #inp = inp.split("\n\n")

#p1, p2 = inp

p1 = inp

points = p1.splitlines()

result = []
for x in points:
    state, points = x.split()
    state = True if state == "on" else False
    points = re.findall(r"x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", points)[0]
    points = list(map(int, points))
    result.append((state, points))

area = defaultdict(bool)

for state, vals in result:
    minX, maxX, minY, maxY, minZ, maxZ = vals

    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            for z in range(minZ, maxZ + 1):
                area[(x, y, z)] = state


print(sum(area.values()))