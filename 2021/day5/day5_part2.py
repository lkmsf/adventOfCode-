from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

with open("5.in") as f:
# with open("test5.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [[list(map(int, z.split(","))) for z in x.split(" -> ")] for x in inp]

p1 = None 
p2 = None 


lines = inp 

points = defaultdict(int)

for a, b in lines:
    xs = [a[0], b[0]]
    ys = [a[1], b[1]]

    if a[0] == b[0]:
        for y in range(min(ys), max(ys) + 1):
            points[(a[0], y)] += 1
    elif a[1] == b[1]:
        for x in range(min(xs), max(xs) + 1):
            points[(x, a[1])] += 1
    else:
        xAdd = 1 if a[0] < b[0] else -1
        yAdd = 1 if a[1] < b[1] else -1
        curr = a
        while curr != b:
            points[(curr[0], curr[1])] += 1
            curr[0] += xAdd
            curr[1] += yAdd
        points[(b[0], b[1])] += 1


p2 = sum(points[key] > 1 for key in points)


print(f"part1: {p1}")
print(f"part2: {p2}")

for i, part in enumerate([p1, p2]):
    print(f'bash submit.sh {i+1} {part}')