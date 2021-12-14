from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    poly, rules= inp.split("\n\n")

rules = dict(x.split(" -> ") for x in rules.splitlines())

pairs = Counter(a + b for a,b in zip(poly, poly[1:])) 
chars = Counter(poly)

for i in range(40):
    for (a, b), count in pairs.copy().items():
        newChar = rules[a + b]

        pairs[a + b] -= count
        pairs[a + newChar] += count
        pairs[newChar + b] += count

        chars[newChar] += count


print(max(chars.values()) - min(chars.values()))
