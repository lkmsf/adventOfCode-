from collections import Counter, defaultdict
from itertools import combinations, chain, accumulate
import numpy as np
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read()
    inpM, instructions = inp.split("\n\n")

maze = [] 
for line in inpM.splitlines():
    print(line)
    maze.append(line)
print(maze)

steps = re.findall(r"R|L|(?:\d+)", instructions)
print(steps)

def rowBeg(y): 
    for i, x in enumerate(maze[y]):
        if x != " ":
            return i
    return None

def rowEnd(y): 
    for i in reversed(range(len(maze[y]))):
        x = maze[y][i]
        if x != ' ':
            return i
    return None

def colBeg(x): 
    for y in range(len(maze)):
        vals = maze[y]
        if x in range(len(vals)) and vals[x] != ' ':
            return y
    return None

def colEnd(x): 
    for y in range(len(maze) - 1, -1, -1):
        vals = maze[y]
        if x in range(len(vals)) and vals[x] != ' ':
            return y
    return None

facing = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
def nextLoc(ix, iy, face):
    dx, dy = facing[face]
    x, y = ix + dx, iy + dy
    #wrap around
    if dx == 0: 
        if y > colEnd(x):
            y = colBeg(x)
        elif y < colBeg(x): 
            y = colEnd(x)
    else:
        if x > rowEnd(y):
            x = rowBeg(y) 
        elif x < rowBeg(y): 
            x = rowEnd(y) 
    if maze[y][x] == " ": 
        print(ix, iy, "->", x, y, dx, dy)
        assert(False)
    return x, y 

def move(x, y, steps, face): 
    for i in range(steps):
        nx, ny = nextLoc(x, y, face)
        # print("next : ", nx, ny)
        if maze[ny][nx] == "#":
            return x, y
        x, y = nx, ny
    return x, y

face = 0
x, y = rowBeg(0), 0
print(x, y, face)
for instr in steps: 
    print(instr)
    if instr == 'R': 
        face += 1
        if face == 4:
            face = 0
    elif instr == 'L':
        face -= 1
        if face < 0: 
            face = 3
    else:
        x, y = move(x, y, int(instr), face)
    print(x, y, face)
    print()

vals = [y+ 1, x + 1, face]
print(vals)
print(sum(a * b for a, b in zip(vals, [1000, 4, 1])))
