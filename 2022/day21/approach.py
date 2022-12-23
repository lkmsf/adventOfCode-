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

inp = [x.split(":") for x in inp]

opposites = {"+":"-", "-":"+", "/":"*", "*": "/"}

vals = {}
expr = []
for line in inp:
    name, args = line
    args = args.strip().split()
    if len(args) == 1:
        if name == "humn":
            continue
        vals[name] = int(args[0])        
    elif name == "root": 
        v1 = args[0]
        v2 = args[2]
    else:
        expr.append([name, args])

def addinOps(vals, newExpr, key, op1, op, op2):        
    # key = op1 / op2 -> op1 = key * op2
    if not type(op1) == int:
        newExpr.append([op1, [key, opposites[op], op2]])
    # key = op1 / op2 -> op1 = key * op2 -> op2 = op1 / key
    elif not type(op2) == int:
        newExpr.append([op2, [op1, op, key]])
    else:
        assert(False)

    print('adding in new ops - ' + key)
    print(vals)
    print(newExpr)
    print()


def simplifyAll(vals, exprs):
    while True:
        newExpr = []
        print(vals)
        print(exprs)
        print()

        for key, val in exprs:
            op1, op, op2 = val
            op1 = vals.get(op1, op1)
            op2 = vals.get(op2, op2)
            val = [op1, op, op2]
            if type(op1) == int and type(op2) == int:
                newVal = eval(" ".join(map(str, val)))
                vals[key] = newVal
            elif key == v1 and v2 in vals:
                vals[key] = vals[v2]
                addinOps(vals, newExpr, key, op1, op, op2) 
            elif key == v2 and v1 in vals:    
                vals[key] = vals[v1]
                addinOps(vals, newExpr, key, op1, op, op2)
            else:
                newExpr.append([key, val])
        if len(newExpr) == len(exprs): 
            exprs = deepcopy(newExpr)
            break
        exprs = deepcopy(newExpr)
    return vals, exprs

i = 0
while True:
    vals, expr = simplifyAll(vals, expr)
    if not expr: break
    currKey, currVal = expr[0]
    del expr[0]
    addinOps(vals, expr, currKey, *currVal)
    if i == 3: break
    i += 1        
    print("reshuffle")
    print(vals)
    print(expr)
    print()

print(vals)
print(vals["humn"])