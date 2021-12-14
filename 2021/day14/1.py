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


def doRound(poly, rules):
    newS = ""
    newS += poly[0]
    for i in range(0, len(poly)):
        chars = poly[i:i+2]
        if chars in rules:
            newS += rules[chars] + poly[i+1]
    poly = newS  

    return poly

for i in range(40):
    poly = doRound(poly, rules)

counts = Counter(poly)

print(counts.most_common()[0][1] - counts.most_common()[-1][1])