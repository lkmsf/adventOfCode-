from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

AMBER = 1
BRONZE = 10
COPPER = 100
DESERT = 1000

test = [["A", "B"], ["D", "C"], ["C", "B"], ["A", "D"]]

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 
    inp = inp.split("\n\n")

inp = [int(x) for x in inp]
inp = [x.split() for x in inp]


