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

rules = rules.splitlines()

rules = [r.split(" -> ") for r in rules]
rules = {a:b for a,b in rules}

patterns = {}

for key, value in rules.items():
    patterns[key] = [key[0] + value, value + key[1]]

def countChars(chars, iterations, mem):
    if iterations == 0:
        return Counter(chars) 
    if (chars, iterations) in mem:
        return mem[chars, iterations]

    total = Counter()

    for nexts in patterns[chars]:
        total += countChars(nexts, iterations - 1, mem)

    doubleCounted = patterns[chars][0][1]
    total[doubleCounted] -= 1

    mem[(chars, iterations)] = total
    return total

result = Counter()
mem = {}
for i in range(len(poly) - 1):
    print(poly[i:i+2])
    result += countChars(poly[i:i+2], 40, mem)


print(poly, result.most_common())
print(result.most_common()[0][1] - result.most_common()[-1][1]) # one too low :/