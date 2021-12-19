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

scanners = [[list(map(int, a.split(","))) for a in x.splitlines()[1:]] for x in inp]

s = scanners[0]

s = s[0]
for xi, yi, zi in permutations([0, 1, 2]):
    for xs in (1, -1):
        for ys in (1, -1):
            for zs in (1, -1):
                x, y, z = xs * s[xi], ys * s[yi], zs * s[zi]
                print(x,y, z)

