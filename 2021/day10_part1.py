from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math

with open("10.in") as f:
# with open("test10.in") as f:
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

pts = {")": 3, "]":57, "}":1197, ">":25137}

total = 0

for v in inp:
    r = findFirstIll(v)
    if r:
        total += pts[r]
print(total)