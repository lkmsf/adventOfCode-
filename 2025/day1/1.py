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
	dial = ((dial + x) % 100)
	if dial == 0:
		result += 1

print(result)
