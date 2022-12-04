from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split("\n")

inp = [x.split(",") for x in inp]

isContainedBy = lambda a, b: a[0] >= b[0] and a[1] <= b[1]

n = 0
for pairing in inp:
    a,b = [x.split("-") for x in pairing]
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    if isContainedBy(a, b) or isContainedBy(b, a):
        n += 1

print(n)

