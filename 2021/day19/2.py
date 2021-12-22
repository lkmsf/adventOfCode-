from collections import Counter, defaultdict
from itertools import combinations, chain, permutations 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split("\n\n")

scanners = [set([tuple(map(int, a.split(","))) for a in x.splitlines()[1:]]) for x in inp]
scanners = {i: val for i, val in enumerate(scanners)}

def optionsForScanner(scanner):
    result = []
    for xi, yi, zi in permutations([0, 1, 2]):
        for xs in (1, -1):
            for ys in (1, -1):
                for zs in (1, -1):
                    curr = set()
                    for s in scanner:
                        x, y, z = xs * s[xi], ys * s[yi], zs * s[zi]
                        curr.add((x, y, z))
                    result.append(curr)
    return result

def findOffset(option, placedBeacons):
    offsets = defaultdict(int)
    for opt in option:
        for placed in placedBeacons:  # placed = (0, 0, 0), opt = (1, 5, 4) -> (-1, -5, -4)
            curr = tuple(a - b for a, b in zip(placed, opt))
            offsets[curr] += 1
            if offsets[curr] >= 12:
                return curr
    # print(offsets)

def findBeacons(scannerToPlace, beacons):
    for option in optionsForScanner(scannerToPlace):
        offset = findOffset(option, beacons)
        if offset:
            dx, dy, dz = offset
            shiftedVals = set([(x + dx, y + dy, z + dz) for x,y,z in option])
            return shiftedVals, offset
    return None, None


foundBeacons = scanners[0]

scannersPlaced = set()
scannersPlaced.add(0)

scannersPlacements = []

totalToPlace = len(scanners)
while len(scannersPlaced) != totalToPlace:
    for i, otherScanner in scanners.items():
        if i in scannersPlaced: continue
        match, offset = findBeacons(otherScanner, foundBeacons)
        if match:
            scannersPlacements.append(offset)
            print("beacons so far:", len(match))
            foundBeacons = foundBeacons.union(match)
            scannersPlaced.add(i)
            break
    
print(scannersPlacements)

dist = []
for a, b in combinations(scannersPlacements, 2):
    d = sum(abs(e - r) for e,r in zip(a, b))
    dist.append(d)

print(max(dist))


        # xs = [x[0] for x in option]
        # for dx in range(max(xs) - 1000, min(xs) + 1001):
        #     ys = [y[1] for y in option]
        #     for dy in range(max(ys) - 1000, min(ys) + 1001):
        #         zs = [z[2] for z in option]
        #         for dz in range(max(zs) - 1000, min(zs) + 1001):