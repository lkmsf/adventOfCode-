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

beams = set([inp[0].index("S")])

num_splits = 0

for row in inp[1:]:
	next_beams = set()
	
	def add_beam(x):
		if 0 <= x < len(inp[0]): next_beams.add(x)

	for b in beams: 
		if row[b] == "^":
			num_splits += 1
			add_beam(b-1)
			add_beam(b+1)	
		else:
			add_beam(b)
	beams = next_beams

print(num_splits) 
