from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math

with open("10.in") as f:
#with open("test10.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

# part 1
pts = {")": 3, "]":57, "}":1197, ">":25137}
OPEN =  "{(<["

def findFirstIll(s):
    prev = ""
    while prev != s:
        prev = s
        for v in ["()", "[]", "{}", "<>"]:
            s = s.replace(v, "")
    result = [c for c in s if c not in OPEN]
    return "" if not result else result[0]

illegalChars = map(findFirstIll, inp)
print(sum(pts[c] for c in illegalChars if c))

#part 2
pts = {"(": 1, "[":2, "{":3, "<":4}

def findOpens(s):
    prev = ""
    while prev != s:
        prev = s
        for v in ["()", "[]", "{}", "<>"]:
            s = s.replace(v, "")
    return s

total = 0
opens = [v for v in map(findOpens, inp) if all(c in OPEN for c in v)]

scores = []
for s in opens:
    total = 0
    while s:
        total *= 5
        total += pts[s[-1]]
        s = s[:-1]
    scores.append(total)

scores = sorted(scores)
print(scores[len(scores) // 2])