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

# rock: A, X, paper: B, Y, scissors: C, Z
# 

scores = {"X":["B", "A", "C"], "Y": ["C", "B", "A"], "Z":["A", "C", "B"]}

total = 0
for them, us in inp:
    #print(them, us)
    score = 1 if us == "X" else 2 if us == "Y" else 3
    score += scores[us].index(them) * 3
    #print("  ", score)

    total += score


print(total)

# 1 + JK