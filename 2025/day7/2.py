from collections import Counter, defaultdict
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

inp = [list(x) for x in inp]

beam = inp[0].index("S")


def num_worlds(beam, row_i, mem):
	if (beam, row_i) in mem: 
		return mem[(beam, row_i)] 

	if not 0 <= beam < len(inp[0]):
		return 0 
	if row_i == len(inp) -1:
		return 1

	row_i += 1	
	if inp[row_i][beam] == "^":
		result = num_worlds(beam + 1, row_i, mem) + num_worlds(beam - 1, row_i, mem)
	else: 
		result = num_worlds(beam, row_i, mem) 

	mem[(beam, row_i)] = result

	return result

mem = {}
print(num_worlds(beam, 0, mem)) 
