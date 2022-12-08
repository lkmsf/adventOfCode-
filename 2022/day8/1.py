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

def treeVis(i, j, val):
    left = i == 0 or all([inp[i][x] < val for x in range(0, j)]) 
    if left: return True
    right = i == len(inp) - 1 or all([inp[i][x] < val for x in range(j + 1, len(inp[0]))]) 
    if right: return True
    top = j == 0 or all([inp[x][j] < val for x in range(0, i)]) 
    if top: return True
    bot = j == len(inp) - 1 or all([inp[x][j] < val for x in range(i + 1, len(inp[0]))]) 
    if bot: return True
    return False

n = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        vis = treeVis(i, j, inp[i][j])
        # print(inp[i][j], int(vis), end = "  ")
        n += vis
  #   print()

print(n)

