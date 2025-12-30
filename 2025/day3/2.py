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
	curr = 0
	left_i = 0	
	for i in range(12):
		start_i = len(x) - (12 - i) + 1
		n_m = max(x[left_i:start_i])
		left_i = x.index(n_m, left_i, start_i) + 1
				
		curr = (curr * 10) + n_m		

	print(curr)
	result += curr


print(result)


