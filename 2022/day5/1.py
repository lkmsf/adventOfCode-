from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"
 
with open(inputFile) as f:
    inp = f.read()
    inp = inp.split("\n\n")

puzzle = inp[0]
puzzle = puzzle.splitlines()
n = len(puzzle[0])
puzzle = [[x[i] for i in range(1, n, 4)] for x in puzzle][:-1]
puzzle = [[x[i] for x in puzzle if x[i] != " "][::-1] for i in range((n // 4) + 1)]
puzzle.insert(0, [])

print(puzzle)
instr = [list(map(int, re.findall("\d+", x))) for x in inp[1].splitlines()]

for num, src, dst in instr:
    for _ in range(num):
        #print(puzzle)
        puzzle[dst].append(puzzle[src][-1])
        del puzzle[src][-1]

print(''.join(x[-1] for x in puzzle[1:]))
