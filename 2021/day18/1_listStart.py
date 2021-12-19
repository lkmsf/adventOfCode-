from collections import Counter, defaultdict
import enum
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

# inp = ["[[1,2],[[3,4],5]]"]

result = []
for line in inp:
    curr = []
    nestingLevel = 0
    for c in line:
        if c == "[": nestingLevel += 1
        elif c == "]": nestingLevel -= 1
        elif c == ",": continue
        else:
            curr.append([int(c), nestingLevel])
    result.append(curr)


def explode(val):
    for i1, (c1, lev1) in enumerate(val[:-1]):
        c2, lev2 = val[i1 + 1]
        if lev1 == lev2 and lev1 >= 5:
            # now we want to reduce
            if i1 > 0:
                val[i1 - 1][0] += c1
            if i1 < len(val):
                val[i1 + 2][0] += c2
            val[i1] = [0, lev1 - 1]
            del val[i1 + 1]
            break
    return val

def split(val):
    for i, (c, l) in enumerate(val):
        if c >= 10:
            num1, num2 = c // 2, c - (c // 2)
            val[i] = [num1, l + 1]
            val.insert(i + 1, [num2, l + 1])
            break
    return val

def reduce(val):
    prev = ""
    while prev != val:
        prev = val.copy()

        val = explode(val) 
        val = split(val)

    return val


def add(a, b):
    result = [[c, l + 1] for c, l in a]
    result.extend([[c, 1 + 1] for c, l in b])
    reduce(result)
    return result

def toList(val):
    s = ""
    currLevel = 0
    for v, l in val:
        while currLevel < l:
            s += "["
            currLevel += 1
        while currLevel > l:
            s += "]"
            currLevel -= 1
        s += str(v) + ","
    
    while currLevel > 0:
        s += "]"
        currLevel -= 1

    return eval(s)
    

def mag(l):
    if isinstance(l, int):
        return l
    return (3 * mag(l[0])) + (2 * mag(l[1]))

total = add(result[0], result[1])
for e in result[2:]:
    print(e)
    total = add(total, e) 

print(mag(toList(total)))

# result = toList(result[0])
# print(mag(result))
