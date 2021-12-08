from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

with open("8.in") as f:
#with open("test8.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [[a.split() for a in x.split(" | ")] for x in inp]


output = [b for a,b in inp]

count = 0
for line in output:
    for word in line:
        if len(word) == 3 or len(word) == 2 or len(word) == 7 or len(word) == 4:
            count += 1
            print(word)

print(count)