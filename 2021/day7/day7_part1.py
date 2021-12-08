from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

with open("7.in") as f:
# with open("test7.in") as f:
    inp = f.read().strip()
    inp = inp.split(",")

inp = [int(x) for x in inp]

bestPos = -1
bestFuel = -1

for i in range(max(inp) + 1):
    print(i)
    fuel = 0
    for val in inp:
        fuel += abs(val - i)

    if bestFuel == -1 or fuel < bestFuel:
        bestFuel = fuel
        bestPos = i

print(bestFuel)