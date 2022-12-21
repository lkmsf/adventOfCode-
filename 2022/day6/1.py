from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()

amt = 4
critical = 0
for i in range(len(inp)):
    curr = inp[i:i+amt]
    if len(curr) == len(set(curr)):
        critical = i + amt
        break

print(critical)
