from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

with open("8.in") as f:
#with open("test8.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [[a.split() for a in x.split(" | ")] for x in inp]

# 0 - 6, 1 - 2, 2- 5, 3 - 5, 4 - 4, 5 - 5, 6 - 6, 7 - 3, 8 - 7, 9 - 6
possibleVals = {6: [0, 6, 9], 2:[1], 5:[2, 3, 5], 4:[4], 3:[7], 7:[8]}

def isWithin (sub, s):
    for c in sub:
        if c not in s:
            return False
    return True


def findMapping(sig):
    result = {}
    # find 1, 4, 7, 8
    result[1] = [x for x in sig if len(x) == 2][0]
    result[4] = [x for x in sig if len(x) == 4][0]
    result[7] = [x for x in sig if len(x) == 3][0]
    result[8] = [x for x in sig if len(x) == 7][0]

    zeroSixNine = [x for x in sig if len(x) == 6]

    # 6 doesn't contains both of 1's vals
    result[6] = [x for x in zeroSixNine if not (isWithin(result[1], x))][0]
    zeroSixNine.remove(result[6])

    # 9 contains the letter in 7
    result[9]  = [x for x in zeroSixNine if isWithin(result[4], x)][0]

    zeroSixNine.remove(result[9])
    result[0] = zeroSixNine[0]

    twoThreeFive = [x for x in sig if len(x) == 5]

    # three contains all of 1
    result[3] = [x for x in twoThreeFive if isWithin(result[1], x)][0]
    twoThreeFive.remove(result[3])

    # one six common is F
    possibleFs = [x for x in result[1] if x in result[6]]
    valForF = possibleFs[0]


    result[5] = [x for x in twoThreeFive if valForF in x][0]
    twoThreeFive.remove(result[5])

    result[2] = twoThreeFive[0]

    return {"".join(sorted(val)): key for key, val in result.items()}

total = 0
for signals, out in inp:
    mapping = findMapping(signals)

    output = "".join([str(mapping["".join(sorted(x))]) for x in out]) 
    print(output)
    num = int(output)
    total += num


print(total)