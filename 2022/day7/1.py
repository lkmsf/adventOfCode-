from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [x.split() for x in inp]

dir = {}

sizes = {}
curr = ["/"]

i = 0
while i < len(inp):
    line = inp[i]
    cmd = line[1]
    if line[0] == "$" and cmd == "cd":
        dir = line[2]
        if dir == "/":
            curr = ["/"]
        elif dir == "..":
            del curr[-1]
        else:
            curr.append(line[2])
    elif line[0] != "$":
        currPath = ""
        for path in curr:
            if line[0] == "dir": continue
            currPath += path
            sizes[currPath] = sizes.get(currPath, 0) + int(line[0])
    i += 1

upper = 100000
result = sum(val for key, val in sizes.items() if val < upper)
print(result)