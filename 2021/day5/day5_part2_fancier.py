from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

with open("5.in") as f:
# with open("test5.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [[tuple(map(int, z.split(","))) for z in x.split(" -> ")] for x in inp]

p1 = None 
p2 = None 

lines = inp 

points = [] 

for a, b in lines:
    xAdd = (1 if a[0] < b[0] else -1) if a[0] != b[0] else 0
    yAdd = (1 if a[1] < b[1] else -1) if a[1] != b[1] else 0
    curr = a
    points.append(a)
    while curr != b:
        curr = (curr[0] + xAdd, curr[1] + yAdd)
        points.append(curr)

p2 = len([x for x, n in Counter(points).items() if n > 1]) 


print(f"part1: {p1}")
print(f"part2: {p2}")

for i, part in enumerate([p1, p2]):
    print(f'bash submit.sh {i+1} {part}')