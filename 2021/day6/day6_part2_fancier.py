from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

p2 = None 

with open("6.in") as f:
# with open("test6.in") as f:
    inp = f.read().strip()

inp = [int(x) for x in inp.split(",")]
fish = [inp.count(i) for i in range(9)]

for i in range(256):
    n = fish.pop(0)
    fish[6] += n
    fish.append(n)

p2 = sum(fish)
print(f"part2: {p2}")