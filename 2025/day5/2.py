from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    ranges, food = inp.split("\n\n")

ranges = ranges.splitlines()
ranges = [x.split("-") for x in ranges]
ranges = [(int(a), int(b)) for a, b in ranges]

food = food.splitlines()
food = [int(x) for x in food]

#parse 
ranges.sort()

cleaned_ranges = []
ignore_ranges = []

for i, (a,b) in enumerate(ranges): 
	print(f"looking at ({a}, {b})") 
	
	if (a,b) in ignore_ranges: 
		continue
		
	for c,d in ranges[i+1:]:
		if not ( (a <= c <= b)  or (a <= d <= b)): 
			continue

		if c <= a:
			# c a d b
			if d <= b:
				a = d+1

			# c a  b d
			if d > b:
				a = -1
				break

		elif c > a:
			#  a c d b 
			if d <= b:
				ignore_ranges.append((c,d)) 		

			#  a c  b d
			if d > b:
				b = c-1

		print(f" 	from {c}, {d}, ->  ({a}, {b})") 

	
	print(f" Changed to ({a}, {b})") 
	if a != -1:
		cleaned_ranges.append((a,b)) 


counts = 0
for a, b in cleaned_ranges: 
	counts += b - a + 1	

print(counts)
