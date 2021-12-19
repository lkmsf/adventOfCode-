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
        if dx < 0 and x < minX: return False
        if y > 2278: return False
        x, y, dx, dy = doStep(x, y, dx, dy)

num = 0
for dx in range(0, 500):
    print(dx)
    for dy in range(-100, 100):
        if getSteps(0, 0, dx, dy):
            num += 1
            print("      ", dx, dy)


print(num)