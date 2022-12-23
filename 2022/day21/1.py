from collections import Counter, defaultdict
from itertools import combinations, chain, accumulate
import numpy as np
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [x.split(":") for x in inp]

leftOver = []
vals = {}
for line in inp:
    name, args = line
    args = args.strip().split()
    if len(args) == 1:
        vals[name] = int(args[0])
    else:
        op1, op, op2 = args
        leftOver.append((name, [op1, op2], f'vals["{op1}"] {op} vals["{op2}"]'))

while "root" not in vals: 
    for name, ops, expr in leftOver: 
        if all([x in vals for x in ops]):
            vals[name] = eval(expr)
        else:
            leftOver.append([name, ops, expr])

print(int(vals["root"]))
