from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
from functools import cache

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

p1, p2 = 4, 8
p1, p2 = 4, 9

p1, p2 = p1 - 1, p2 - 1

def nextPlace(pos, move):
    return (pos + move) % 10
    #return ((pos + move - 1) % 10) + 1

rolls = Counter([a + b + c for a in range(1, 4) for b in range(1, 4) for c in range(1, 4)])

@cache
def game(p1, p2, s1, s2, turn1):

    if s1 >= 21:
        return 1, 0
    elif s2 >= 21:
        return 0, 1


    w1, w2 = 0, 0

    for r1, r1C in rolls.items():
        if turn1:
            np1 = nextPlace(p1, r1)
            c1, c2 = game(np1, p2, s1 + np1 + 1, s2, not turn1)
        else:
            np2 = nextPlace(p2, r1)
            c1, c2 = game(p1, np2, s1, s2 + np2 + 1, not turn1)

        w1 += c1 * r1C
        w2 += c2 * r1C

    return w1, w2 

result = game(p1, p2, 0, 0, True) 
print(result)
print(max(result))