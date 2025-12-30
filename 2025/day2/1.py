from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split(",")

inp = [x.split("-") for x in inp]
inp = [(int(x), int(y)) for x,y in inp]

result = 0

for a, b in inp: 
	for i in range(a, b + 1):
		s = str(i)
		if len(s) % 2 != 0:
			continue
		half = int(len(s) / 2)
		if s[:half] == s[half:]:
			result += i

print(result)


