from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.readlines() 
inp = [x.strip() for x in inp]

inp = [(inp[i], inp[i+1], inp[i+2]) for i in range(0, len(inp), 3)]

inp = [(set(a), set(b), set(c)) for a, b, c in inp]

repeated = [list(a.intersection(b).intersection(c))[0] for a, b, c in inp]

print(repeated)

score = 0

for elem in repeated:
    if elem.islower():
        curr = ord(elem) - ord('a') + 1
    else:
        print("is upper")
        curr = ord(elem) - ord('A') + 27
    score += curr
    print(elem, curr)

print(score)
