from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
from functools import cache

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

#p1, p2 = 4, 8  #test data
p1, p2 = 4, 9

p1, p2 = p1 - 1, p2 - 1

rolls = Counter([a + b + c for a in range(1, 4) for b in range(1, 4) for c in range(1, 4)])

@cache
def game(p1, p2, s1, s2):
    if s2 >= 21:
        return 0, 1

    w1, w2 = 0, 0
    for r, rC in rolls.items():
        np1 =  (p1 + r) % 10
        c1, c2 = game(p2, np1, s2, s1 + np1 + 1)

        w1 += c2 * rC
        w2 += c1 * rC

    return w1, w2 

result = game(p1, p2, 0, 0) 
print(result)
print(max(result))