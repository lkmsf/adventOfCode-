from collections import Counter, defaultdict
from itertools import combinations, chain, accumulate
import numpy as np
import re
import statistics
import math
import sys
from copy import deepcopy

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [x.split(": ") for x in inp]
expr = {a: b for a,b in inp}


prevRoot = expr["root"].split()
expr["root"] = prevRoot[0] + ' - ' + prevRoot[2]

def calc(key):
    if expr[key].isdigit():
        return int(expr[key])
    op1, op, op2 = expr[key].split()
    op1 = calc(op1)
    op2 = calc(op2)
    return eval(f"{op1} {op} {op2}")


def binarySearch(low, high):
    if low >= high:
        return low

    mid = (high + low) // 2
    expr["humn"] = str(mid)
    result = calc("root")

    if result == 0: 
        return binarySearch(mid, mid)
    elif result < 0: 
        # too high
        return binarySearch(low, mid)
    else:
        return binarySearch(mid, high)

print(binarySearch(0, 10000000000000000))