from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys


p1 = None 
p2 = None 

with open("6.in") as f:
# with open("test6.in") as f:
    inp = f.read().strip()

inp = inp.split(",")
inp =[int(x) for x in inp]

def day(fish):
    newFish = []
    for v in fish:
        if v == 0:
            newFish.append(6)
            newFish.append(8)
        else:
            newFish.append(v - 1)
    return newFish


for i in range(80):
    inp = day(inp)

p1 = len(inp)


print(f"part1: {p1}")
print(f"part2: {p2}")

for i, part in enumerate([p1, p2]):
    print(f'bash submit.sh {i+1} {part}')