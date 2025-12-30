from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "1.in"
#inputFile = "test.in"

with open(inputFile) as f:
	inp = f.read().strip()
	inp = inp.replace("R", "") 
	inp = inp.replace("L", "-") 
	inp = inp.splitlines()

inp = [int(x) for x in inp]

result = 0
dial = 50
for x in inp:
	print(f"start: {dial} + {x}")

	num_full_rotations = int(x / 100)
	x = x - (num_full_rotations * 100)
	num_full_rotations = abs(num_full_rotations)
	
	start = dial
	mid = dial + x
	dial = ((dial + x) % 100)
			
	addition = num_full_rotations
	if start != 0: 
		addition += ((mid != dial) | (dial == 0))

	result += addition

	print(f"	{addition}")
	print()


print(result)
