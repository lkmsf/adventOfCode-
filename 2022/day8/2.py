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

inp = [list(map(int, list(x))) for x in inp]

def count(l, val):
    n = 0
    for i in l:
        if i < val:
            n += 1
        else:
            return n + 1
    return n

def treeVis(i, j, val):
    left = count([inp[i][x] for x in range(0, j)][::-1], val)
    right = count([inp[i][x]  for x in range(j + 1, len(inp[0]))], val) 
    top = count([inp[x][j] for x in range(0, i)][::-1], val) 
    bot = count([inp[x][j] for x in range(i + 1, len(inp[0]))], val) 
    # print(left, right, top, bot)
    return left * right * top * bot

n = -1
for i in range(len(inp)):
    for j in range(len(inp[0])):
        vis = treeVis(i, j, inp[i][j])
       #  print(inp[i][j], int(vis))
        n = max(n, vis)
   #  print()

print(n)

