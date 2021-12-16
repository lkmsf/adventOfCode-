from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
from functools import cache

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    poly, rules= inp.split("\n\n")

rules = dict(x.split(" -> ") for x in rules.splitlines())

pairs = Counter(a + b for a,b in zip(poly, poly[1:])) 
chars = Counter(poly)

@cache
def polymerize(curr, rounds) -> Counter():
    if rounds == 0:
        return Counter()
    rule = rules[curr]
    return Counter(rule) + polymerize(curr[0] + rule, rounds - 1) + polymerize(rule + curr[1], rounds - 1)

chars = sum([polymerize(a + b, 40) for a, b in zip(poly, poly[1:])], Counter(poly))
print(max(chars.values()) - min(chars.values()))
