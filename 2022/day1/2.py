from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split("\n\n")

inp = [[int(a) for a in x.split()] for x in inp]

sums = [sum(x) for x in inp]

vals = sorted(sums)[-3:]
print(sum(vals))
