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

nums = set() 

for a, b in inp: 
	for i in range(a, b + 1):
		s = str(i)
		s_len = len(s)
		for seq_len in range(1, s_len): 
			if s_len % seq_len != 0: 
				continue
			
			seq = s[:seq_len]
			chunks = [s[new_i:new_i+seq_len] for new_i in range(seq_len, s_len, seq_len)] 
			if all(x == seq for x in chunks): 
				nums.add(i)

print()
print(sum(nums))

