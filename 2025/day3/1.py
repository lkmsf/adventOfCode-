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

inp = [list(map(int, list(x))) for x in inp]

result = 0

for x in inp: 
	n_m = max(x[:-1])
	idx = x.index(n_m)
	n_2m = max(x[idx + 1:])
	val = (n_m * 10) + n_2m
	print(val)

	result += val

print(result)


