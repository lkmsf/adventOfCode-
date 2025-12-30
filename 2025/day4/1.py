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
	

inp = [list(x) for x in inp]
num_rows = len(inp)
num_cols = len(inp[0])

print(inp)

rolls = set()
for r, row in enumerate(inp):
	for c, val in enumerate(row): 
		if val == "@":
			rolls.add((r, c)) 

print(rolls)

def get_neighbors(r, c): 
	ns = [(-1, 0), (1, 0), (0, 1), (0, -1), (1,1), (-1,-1), (-1, 1), (1,-1)] 
	points = []
	for dr, dc in ns:
		if (0 <= (r + dr) < num_rows) and (0 <= (c + dc) < num_cols): 
			points.append((r + dr, c + dc)) 
	return points
			

result = 0
for r, c in rolls:
	print(r,c) 
	print(get_neighbors(r,c))
	adj_rolls = [x for x in get_neighbors(r, c) if x in rolls]
	if len(adj_rolls) < 4:
		print(	"FREE NEIHGBOR") 
		result += 1

print(result)
