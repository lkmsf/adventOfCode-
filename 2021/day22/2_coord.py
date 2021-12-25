from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
from bisect import bisect_left

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()

p1 = inp

points = p1.splitlines()

result = []
for x in points:
    state, points = x.split()
    state = True if state == "on" else False
    points = re.findall(r"x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", points)[0]
    points = list(map(int, points))
    minX, maxX, minY, maxY, minZ, maxZ = points
    points[1] += 1
    points[3] += 1
    points[5] += 1
    result.append((state, tuple(points)))

# new axess
xs = sorted(list(set([x[0] for _, x in result] + [x[1] for _, x in result])))
ys = sorted(list(set([x[2] for _, x in result] + [x[3] for _, x in result])))
zs = sorted(list(set([x[4] for _, x in result] + [x[5] for _, x in result])))

points = set()

i = 0
for state, vals in result:
    print(i, len(result))
    i += 1

    minX, maxX, minY, maxY, minZ, maxZ = vals

    nX, xX = bisect_left(xs, minX), bisect_left(xs, maxX)
    nY, xY = bisect_left(ys, minY), bisect_left(ys, maxY)
    nZ, xZ = bisect_left(zs, minZ), bisect_left(zs, maxZ)

    for x in range(nX, xX):
        for y in range(nY, xY):
            for z in range(nZ, xZ):
                if state:
                    points.add((x, y, z))
                else: 
                    if (x, y, z) in points: points.remove((x, y, z))


totalVolume = 0

sideLen = lambda i, l: l[i + 1] - l[i]

for x, y, z in points:
    totalVolume += sideLen(x, xs) * sideLen(y, ys) * sideLen(z, zs)

print(totalVolume)

