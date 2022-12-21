from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [x.split() for x in inp]

r = 1
vals = [r]
for curr in inp:
    if len(curr) == 1:
        vals.append(r)
    else:
        num = int(curr[1])
        vals.append(r)
        vals.append(r)
        r += num


for j in range(1, len(vals), 40):
    for i in range(40):
        if i in range(vals[j + i] - 1, vals[j + i] + 2):
            print("#", end = "")
        else:
            print(".", end = "")
    print("")
print()