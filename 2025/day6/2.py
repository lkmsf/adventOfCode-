from collections import Counter, defaultdict
import math
from itertools import combinations, chain 
import re
import statistics
import math
import sys
sys.path.append("../")
from utils import clean_ranges

input_file = "data.in" if len(sys.argv) == 1 else "test.in" if len(sys.argv[1]) == 1 else sys.argv[1]

with open(input_file) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

ops = re.split(r"\s+", inp[-1])
inp = inp[:-1]

cols = [[row[i] for row in inp] for i in range(len(inp[0]))]
vals = ["".join(col).strip(" ") for col in cols]

problems = []
curr = []
for val in vals: 
	if val == "":
		problems.append(curr)
		curr = []
	else:
		curr.append(int(val))
problems.append(curr) 

total = 0
for op, vals in zip(ops, problems):
	print(op, vals)
	if op == "+": 
		total += sum(vals) 
	elif op == "*": 
		total += math.prod(vals)
	print(total)

print(total)
