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

inp = [[a for a in re.split(r'\s+', x) if a != ""] for x in inp]

problems = [[int(row[i]) if row[i] not in ("+", "*") else row[i] for row in inp] for i in range(len(inp[0]))] 

print(problems) 

total = 0

print(len(problems)) 
for curr in problems:
	op = curr[-1]
	vals = curr[:-1]
	print(op, vals) 
	if op == "+": 
		total += sum(vals) 
	elif op == "*": 
		total += math.prod(vals)
	print(total)

print(total)
