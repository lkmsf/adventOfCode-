from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

with open("%%DAY%%.in") as f:
# with open("test%%DAY%%.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 
    inp = inp.split("\n\n")

inp = [int(x) for x in inp]
inp = [x.split() for x in inp]


