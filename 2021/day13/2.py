from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split("\n\n")
    inp = [x.splitlines() for x in inp]

points, folds= inp

points = [[int(a) for a in x.split(",")] for x in points]
folds = [y.split()[2].split("=") for y in folds]
folds = [(x, int(y)) for x,y in folds]

maxX = max([a for a,b in points]) + 1
maxY = max([b for a,b in points]) + 1

grid = [[" "] * maxX for i in range(maxY)] 

for x, y in points:
    grid[y][x] = "X"


def foldAlongX(val, grid):
    afterFold = [[" "] * val for i in range(len(grid))]

    cols = len(grid[0])
    for y, line in enumerate(afterFold):
        for i in range(len(line)):
            afterFold[y][i] = "X" if (grid[y][i] == "X" or grid[y][cols - i - 1] == "X") else " "

    return afterFold


def foldAlongY(val, grid):
    afterFold = [[" "] * len(grid[0]) for i in range(val)]

    rows = len(grid)
    for y, line in enumerate(afterFold):
        for i in range(len(line)):
            afterFold[y][i] = "X" if (grid[y][i] =="X" or grid[rows - y - 1][i] == "X") else " "

    return afterFold

result = grid
for dir, val in folds:
    if dir == "x":
        result = foldAlongX(val, result)
    else:
        result = foldAlongY(val, result)

for line in result:
    print("".join(line))