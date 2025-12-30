from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
sys.path.append("../")
from utils import clean_ranges

input_file = "data.in" if len(sys.argv) == 1 else "test.in" if len(sys.argv[1]) == 1 else sys.argv[1]

with open(input_file) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 
    inp = inp.split("\n\n")

inp = [int(x) for x in inp]
inp = [x.split() for x in inp]


