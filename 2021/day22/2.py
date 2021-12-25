from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

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

def withinRange(val, minV, maxV):
    return val >= minV and val <= maxV

def coordWithin(minA, maxA, minB, maxB):
    return withinRange(minB, minA, maxA) and withinRange(maxB, minA, maxA)

def volume(box):
    minX, maxX, minY, maxY, minZ, maxZ = box
    if maxX < minX or maxY < minY or maxZ < minZ: return 0 
    return (maxX - minX) * (maxY - minY) * (maxZ - minZ)

def pointWithinBox(x, y, z, box):
    minX, maxX, minY, maxY, minZ, maxZ = box
    return withinRange(x, minX, maxX) and withinRange(y, minY, maxY) and withinRange(z, minZ, maxZ)

def boxCornerInside(boxWithin, surroundingBox):
    minX, maxX, minY, maxY, minZ, maxZ = boxWithin
    if pointWithinBox(minX, minY, minZ, surroundingBox): return True
    if pointWithinBox(maxX, maxY, maxZ, surroundingBox): return True
    return False

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

def boxesIntersect(box, otherBox):
    corners = getCorners(box), getCorners(otherBox)

    for b in corners[0]:
        if pointWithinBox(*b, otherBox): return True
    for b in corners[1]:
        if pointWithinBox(*b, box): return True

    return False

def splitBoxByX(box, x):
    minX, maxX, minY, maxY, minZ, maxZ = box

    if not (minX < x and x < maxX): return [box]

    b1 = minX, x, minY, maxY, minZ, maxZ 
    b2 = x, maxX, minY, maxY, minZ, maxZ 

    result = [x for x in [b1, b2] if volume(x) > 0]
    return result

def splitBoxByY(box, y):
    minX, maxX, minY, maxY, minZ, maxZ = box

    if not (minY < y and y < maxY): return [box]

    b1 = minX, maxX, minY, y, minZ, maxZ 
    b2 = minX, maxX, y, maxY, minZ, maxZ 

    result = [x for x in [b1, b2] if volume(x) > 0]
    return result

def splitBoxByZ(box, z):
    minX, maxX, minY, maxY, minZ, maxZ = box

    if not (minZ < z and z < maxZ): return [box]

    b1 = minX, maxX, minY, maxY, minZ, z 
    b2 = minX, maxX, minY, maxY, z, maxZ 

    result = [x for x in [b1, b2] if volume(x) > 0]
    return result

def splitBoxByCoord(box, x, y, z):
    byY = []
    byZ = []

    byX = splitBoxByX(box, x)
    for b in byX:
        byY += splitBoxByY(b, y)
    for b in byY:
        byZ += splitBoxByZ(b, z)

    return byZ

def splitBoxByBox(box, splitBy):

    minX, maxX, minY, maxY, minZ, maxZ = splitBy
    boxes = splitBoxByCoord(box, minX, minY, minZ)
    result = [] 
    for b in boxes:
        result += splitBoxByCoord(b, maxX, maxY, maxZ)
    return result

def breakIntoSets(box, otherBox):
    if not box or not otherBox or not boxesIntersect(box, otherBox): return set([box])

    return set(tuple(x) for x in splitBoxByBox(box, otherBox))

def breakListBoxIntoSet(box, otherBox):
    curr = set()

    for b in box:
        curr = curr | breakIntoSets(b, otherBox)

    return curr

def breakBoxByListBoxIntoSet(box, otherBoxes):
    if not otherBoxes: return set([box])

    curr = set([box])

    for b in otherBoxes:
        curr = breakListBoxIntoSet(curr, b) 

    return curr

currVolumes = set()

i = 0
for state, box in result:
    print(i, "out of", len(result), len(currVolumes))
    i += 1

    prevBoxes = breakListBoxIntoSet(currVolumes, box)
    box = breakBoxByListBoxIntoSet(box, currVolumes)

    if state:
        currVolumes = prevBoxes | box 
    else: 
        currVolumes = prevBoxes - box 

# print(result)
# print(len(result))

vols = [volume(x) for x in currVolumes]

# print(vols)
print(sum(vols))




# # on x=10..12,y=10..12,z=10..12
# # on x=11..13,y=11..13,z=11..13

# # (10, 12, 10, 12, 10, 12)
# # (11, 13, 5, 7, 7, 13)

# #  (10, 11, 10, 12, 10, 12), (11, 12, 10, 12, 10, 12)
# # 


# # turn every box into more boxes (intersection of every other)
# intersectedBoxes = []
# boxes = {}
# i = 0
# for state, box in result:
#     print(i, len(result))
#     i += 1
#     splitBox = set()
#     splitBox.add(box)

#     # now split box by every other box
#     for _, otherBox in result:
#         if boxesIntersect(box, otherBox):
#             splitBox = breakListBoxIntoSet(splitBox, otherBox)
#     boxes[box] = splitBox

#     assert(volume(box) == sum(volume(x) for x in splitBox))
#     intersectedBoxes.append((state, splitBox))


# print("finished splitting boxes")

# # Now we can treat the boxes as sets
# result = set()
# for state, boxes in intersectedBoxes:
#     if state:
#         result = result | boxes
#     else: 
#         result = result - boxes

# # print(result)
# # print(len(result))

# vols = [volume(x) for x in result]

# # print(vols)
# print(sum(vols))