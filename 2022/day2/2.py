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

scoresRev = {"A":["Z", "X", "Y"], "B": ["X", "Y", "Z"], "C":["Y", "Z", "X"]}

total = 0
for them, us in inp:
    print(them, us)
    index = 0 if us == "X" else 1 if us == "Y" else 2
    wePlay = scoresRev[them][index]

    print("we play ", wePlay)
    score = 1 if wePlay == "X" else 2 if wePlay == "Y" else 3

    score += index * 3
    print("  ", score)

    total += score


print(total)

# 1 + JK