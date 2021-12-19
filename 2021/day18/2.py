from collections import Counter, defaultdict
import enum
from itertools import combinations, chain 
import re
import statistics
import math
import sys
from copy import deepcopy
inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [eval(x) for x in inp]

def convert(l):
    if isinstance(l, int):
        return [l]
    return [convert(x) for x in l] 


def split(val):
    if len(val) == 1 and isinstance(val[0], int):
        if val[0] < 10: return
        num1, num2 = val[0] // 2, val[0] - (val[0] // 2)
        del val[0]
        val.extend([[num1], [num2]])
        return
    for x in val:
        prev = deepcopy(val)
        split(x) 
        if val != prev:
            return

singlePair = lambda x: all(len(e) == 1 and isinstance(e[0], int) for e in x)

def getFarRight(val):
    if len(val) == 1 and isinstance(val[0], int):
        return val
    return getFarRight(val[-1])

def getFarLeft(val):
    if len(val) == 1 and isinstance(val[0], int):
        return val
    return getFarLeft(val[0])

def explode(vals, level = 0, left = None, right = None):
    if len(vals) == 1:
        return

    if level >= 4 and singlePair(vals):
        n1, n2 = vals

        if left: 
            left = getFarRight(left)
            left[0] = n1[0] + left[0]
        if right: 
            right = getFarLeft(right)
            right[0] = n2[0] + right[0]
        vals[0] = 0
        del vals[1]

    elif not singlePair(vals):
        prev = deepcopy(vals)
        explode(vals[0], level + 1, left, vals[1])
        if prev != vals: return
        explode(vals[1], level + 1, vals[0], right) 

def reduce(vals):
    prev = ""
    while prev != vals:
        prev = deepcopy(vals)
        explode(vals)
        if vals != prev: continue
        split(vals)

def mag(l):
    if len(l) == 1 and isinstance(l[0], int):
        return l[0]
    return (3 * mag(l[0])) + (2 * mag(l[1]))


def unconvert(vals):
    if len(vals) == 1 and isinstance(vals[0], int):
        return vals[0]
    return [unconvert(x) for x in vals]


inp = convert(inp)
totals = []
for a in inp:
    for b in inp:
        if a == b: continue
        curr = deepcopy([a, b])
        reduce(curr)
        totals.append(mag(curr))

print(max(totals))
