from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()

nums = re.findall(r"-?\d+", inp)
nums = map(int, nums)
minX, maxX, minY, maxY = nums

startX = 0
startY = 0

def reachesTarget(x, y):
    return x in range(minX, maxX + 1) and y in range(minY, maxY + 1)

def doStep(x, y, dx, dy):
    x += dx
    y += dy
    if dx < 0:
        dx += 1
    elif dx > 0: 
        dx -= 1
    dy -= 1
    return x, y, dx, dy

# keeps going until we're past the target
def getSteps(x, y, dx, dy):
    while True:
        if reachesTarget(x, y): return True
        if dy < 0 and y < minY: return False
        #if dx < 0 and x < minX: return False
        #if x > (maxY - minY) + maxX + 5: return False
        if y > 2278: return False
        x, y, dx, dy = doStep(x, y, dx, dy)

num = 0
for dx in range(0, 1000):
    print(dx)
    for dy in range(-10000, 10000):
        if getSteps(0, 0, dx, dy):
            num += 1
            print("      ", dx, dy)


print(num)


# def backStep(x, y, dx, dy):
#     x -= dx
#     y -= dy
#     x -= -1 if x > 0 else 1
#     y += 1
#     return x, y

# def findHeight(x, y, dx, dy):
#     currHeight = y
#     while True:
#         x, y = backStep(x, y, dx, dy)
#         if y < currHeight:
#             return currHeight
#         currHeight = y 

# def mightMakeIt(x, y, dx, dy, xMin, xMax, yMin, yMax):
#     if x + 1 < xMin and dx < 0:
#         return False
#     if x - 1 > xMax and dx > 0:
#         return False
#     if y + 1 < yMin and dy < 0:
#         return False
#     if y - 1 > yMax and dy > 0:
#         return False
#     return True

# def canGetToZero(x, y, dx, dy):
#     while True:
#         if x == 0 and y == 0:
#             return True
#         if not mightMakeIt(x, y, dx, dy, -1, 1, -1, 1):
#             break
#         x, y = backStep(x, y, dx, dy)
#     return False

# heights = []
# for x in range(minX, maxX + 1):
#     for y in range(minY, maxY + 1):
#         # what is the max height we can make it from here back to 0, 0

#         for dx in range(-10, 11):
#             for dy in range(-10, 11):
#                 if not canGetToZero(x, y, dx, dy): continue
#                 heights.append(x, y, dx, dy)

# print(max(heights))