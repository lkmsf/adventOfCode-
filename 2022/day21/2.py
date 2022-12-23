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
    return int(eval(f"{op1} {op} {op2}"))


# def binarySearch(low, high):
#     if low >= high:
#         return low

# by hand
expr["humn"] = "3441198826073"
print(calc("root"))