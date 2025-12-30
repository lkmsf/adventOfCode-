from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    ranges, food = inp.split("\n\n")

ranges = ranges.splitlines()
ranges = [x.split("-") for x in ranges]
ranges = [(int(a), int(b)) for a, b in ranges]

food = food.splitlines()
food = [int(x) for x in food]


result = 0
for x in food:
	if any( a <= x <= b for a, b in ranges): 
		result += 1


print(result)
