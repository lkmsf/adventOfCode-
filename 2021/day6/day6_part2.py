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
    newFish = defaultdict(int)

    for v, n in fish.items():
        if v == 0:
            newFish[6] += n
            newFish[8] += n
        else:
            newFish[v-1] += n
    return newFish


numFish = defaultdict(int)
for f in inp:
    numFish[f] += 1

for i in range(256):
    print(i)
    numFish = day(numFish)

p2 = sum(numFish.values()) 


print(f"part1: {p1}")
print(f"part2: {p2}")

for i, part in enumerate([p1, p2]):
    print(f'bash submit.sh {i+1} {part}')