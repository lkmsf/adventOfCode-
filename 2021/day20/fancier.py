from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    enhance, pic = inp.split("\n\n")

enhance = list(enhance)
pic = [list(x) for x in pic.splitlines()]

points = set()

for il, line in enumerate(pic):
    for iv, val in enumerate(line):
        if val == "#":
            points.add((il, iv))

def surrounding(li, iv):
    result =  []
    for lineI in range(li - 1, li + 2):
        for valI in range(iv - 1, iv + 2):
            result.append((lineI, valI))
    return result

def getPoints(borders):
    minL, maxL, minV, maxV = borders
    result = set()

    for li in range(minL - 1, maxL + 2):
        for vi in range(minV - 1, maxV + 2):
            result.add((li, vi))

    return result

def getBorders(points):
    li = [a for a, b in points]
    vi = [b for a, b in points]
    return min(li), max(li), min(vi), max(vi)


def withinBorders(li, vi, borders):
    minL, maxL, minV, maxV = borders
    return li in range(minL, maxL + 1) and vi in range(minV, maxV + 1)

def round(points, default, borders):
    result = set()

    for (li, iv) in getPoints(borders):
        sur = surrounding(li, iv)
        index = [int((l, v) in points or (not withinBorders(l, v, borders) and default == "#")) for l, v in sur] 
        num = int("".join(map(str, index)), 2)
        if enhance[num] == "#":
            result.add((li, iv))

    return result

for i in range(50):
    print(len(points))
    points = round(points, enhance[0] if i % 2 == 1 else enhance[-1], getBorders(points))



print(len(points))