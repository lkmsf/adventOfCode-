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

def fuelCost(goal, pos):
    r = 0
    diff = abs(goal - pos)
    return sum(range(1, diff + 1)) 

for i in range(max(inp) + 1):
    fuel = 0
    print(i)
    for val in inp:
        fuel += fuelCost(i, val) 

    if bestFuel == -1 or fuel < bestFuel:
        bestFuel = fuel
        bestPos = i

print(bestFuel)