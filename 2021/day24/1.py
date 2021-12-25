from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split("inp w\n")

inp = [[a.split() for a in x.splitlines()] for x in inp][1:]


def runProgram(s):
    z = 0
    nums = []
    for i, c in enumerate(s):

        xAdd = int(inp[i][4][2])
        assert(inp[i][4][0] == "add")

        zDiv = int(inp[i][3][2])
        assert(inp[i][3][0] == "div")

        yAdd = int(inp[i][-3][2])
        assert(inp[i][-3][0] == "add")

        w = int(c)

        if zDiv == 1:
            if ((z % 26) + xAdd) != w:
                z = ((z / zDiv) * (26)) + (w + yAdd)
            else:
                z //= zDiv 
        elif zDiv == 26:
            # xAdd < 0
            if ((z % 26) + xAdd) != w:
                z = ((z / zDiv) * (26)) + (w + yAdd)
            else:
                z //= zDiv 
        else: assert(False)


    return len(nums) == 0

# a 
# z = a + 14
# # b
# z = [(a + 14), (b + 6)]
# #c
# z = [(a + 14), (b + 6), (c + 6)]
# #d
# z = [(a + 14), (b + 6), (c + 6), (d + 13)]
# #e
# z = [(a + 14), (b + 6), (c + 6)]
#     we need ((c + 6) -12) == e
# #f
# z = [(a + 14), (b + 6), (c + 6), (f + 8)]
# #g 
# z = [(a + 14), (b + 6), (c + 6)]
#     we need (c + 6) - 15 == g
# #h 
# z = [(a + 14), (b + 6), (c + 6), (c + )]


# (c + 6) - 12 = e
# (c + 6) - 15 = g
# (h + 10) - 13 = j
# (c + 6) - 13 = k
# (b + 6) - 14 = l
# (a + 14-  2   = m
# (  )  -   9  = n



                   X   X    x   X    x   X   X   x   x     X
# #       a    b   c   d    e   f    g   h   i   j   k     l    m   n        
# zDiv = [1,   1,  1,  1,  26,  1,  26,  1,  1,  26, 26,   26, 26, 26]
# yAdd = [14,  6,  6, 13,   8,  8,   7, 10,  8,  12,  10,   8,   8, 7]
# xAdd = [11, 14, 15, 13, -12, 10, -15, 13, 10, -13, -13, -14, -2, -9]

# first char doesn't matter
# second char doesn't matter
# 
def answer():
    result = 0
    i = 0
    for a in range(9, 1, -1):
        for b in range(9, 1, -1):
            for c in range(9, 1, -1):
                for d in range(9, 1, -1):
                    for e in range(9, 1, -1):
                        for f in range(9, 1, -1):
                            for g in range(9, 1, -1):
                                l = list(map(str, [a, b, c, d, e, f, g]))
                                #num = "".join(l)
                                num = "".join("9999" + str(a) + "9" + str(f) + str(g) + "99999"

                                if i % 100000 == 0: print(num)
                                i += 1

                                result = runProgram(num)
                                if result:
                                    print("result: ", num)
                                    return 


answer()