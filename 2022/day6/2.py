from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()

critical = 0
for i in range(len(inp)):
    curr = inp[i:i+14]
    if len(curr) == len(set(curr)):
        critical = i + 14 
        break

print(critical)
