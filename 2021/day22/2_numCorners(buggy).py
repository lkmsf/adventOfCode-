from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" #if len(sys.argv) > 1 else "data.in"

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
    result.append((state, points))

def withinRange(val, minV, maxV):
    return val >= minV and val <= maxV

def coordWithin(minA, maxA, minB, maxB):
    return withinRange(minB, minA, maxA) and withinRange(maxB, minA, maxA)


def volume(box):
    minX, maxX, minY, maxY, minZ, maxZ = box
    return abs((maxX - minX) * (maxY - minY) * (maxZ - minZ))

def pointWithinBox(x, y, z, box):
    minX, maxX, minY, maxY, minZ, maxZ = box
    return withinRange(x, minX, maxX) and withinRange(y, minY, maxY) and withinRange(z, minZ, maxZ)

def getCorners(box):
    minX, maxX, minY, maxY, minZ, maxZ = box

    lowerLeft = [minX, minY, minZ]

    sides = maxX - minX, maxY - minY, maxZ - minZ

    coords = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]

    result = [] 

    for ds in coords:
        ds = [a * b for a,b in zip(ds, sides)] 
        result.append([a + b for a, b in zip(lowerLeft, ds)])

    return result


def overlappingCorners(box, otherBox):
    corners = getCorners(box)

    result = []
    for x, y, z in corners:
        if pointWithinBox(x, y, z, otherBox):
            result.append((x, y, z))

    return result


def overlap(box, otherBox):
    minXa, maxXa, minYa, maxYa, minZa, maxZa = box
    minXb, maxXb, minYb, maxYb, minZb, maxZb = otherBox

    boxCornersOverlapping = overlappingCorners(box, otherBox)
    otherBoxOverlapping = overlappingCorners(otherBox, box)

    #not touching
    if not boxCornersOverlapping: return 0

    #completely within
    if len(boxCornersOverlapping) == 8: return volume(box)
    if len(otherBoxOverlapping) == 8: return volume(otherBox)

    if len(boxCornersOverlapping) == 1:
        assert(len(otherBoxOverlapping) == 1)

        lower = boxCornersOverlapping[0]
        upper = otherBoxOverlapping[0]
        return volume(*lower, *upper)

    if len(boxCornersOverlapping) == 2:
        assert(False)

    if len(boxCornersOverlapping) == 4:
        assert(False)

    assert(False)




ons = [pts for state, pts in result if state]
offs = [pts for state, pts in result if not state]


areas = []
total = 0

for box in ons:
    minX, maxX, minY, maxY, minZ, maxZ = box
    total += volume(box)

    for otherBox in areas:
        total -= overlap(box, otherBox)

    areas.append(box)

for box in offs:
    for otherBox in areas:
        total -= overlap(box, otherBox)

print(total)


# vals = []
# for state, vals in result:
#     minX, maxX, minY, maxY, minZ, maxZ = vals

#     currStart = (minX, minY, maxZ)
#     currEnd = (maxX, maxY, maxZ)

#     for start, end in vals:




# print(len(area))