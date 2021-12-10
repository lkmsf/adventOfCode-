from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math

with open("10.in") as f:
#with open("test10.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

CLOSE = "{(<["

def findFirstIll(s):
    prev = ""
    while prev != s:
        prev = s
        for v in ["()", "[]", "{}", "<>"]:
            s = s.replace(v, "")
    result = [c for c in s if c not in CLOSE]
    return "" if not result else result[0]

def findOpens(s):
    prev = ""
    while prev != s:
        prev = s
        for v in ["()", "[]", "{}", "<>"]:
            s = s.replace(v, "")
    return s

pts = {"(": 1, "[":2, "{":3, "<":4}

total = 0
complete = [v for v in inp if not findFirstIll(v)]
opens = [findOpens(v) for v in complete]

scores = []
for s in opens:
    print(s)
    total = 0
    while s:
        total *= 5
        total += pts[s[-1]]
        s = s[:-1]
    scores.append(total)

scores = sorted(scores)
print(scores[len(scores) // 2])