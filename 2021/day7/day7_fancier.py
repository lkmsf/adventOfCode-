from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math

with open("7.in") as f:
# with open("test7.in") as f:
    inp = f.read().strip()
    inp = inp.split(",")

inp = [int(x) for x in inp]

# part 1
bestI = statistics.median(inp)
print(math.trunc(sum(abs(val - bestI) for val in inp)))

# part 2
fuels = []
for i in range(max(inp) + 1):
    findCost = lambda x: (x * (x+1)) / 2
    fuels.append(sum(findCost(abs(val - i)) for val in inp))

print(math.trunc(min(fuels)))