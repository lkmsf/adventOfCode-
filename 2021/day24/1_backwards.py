from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" #if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [x.split() for x in inp]


def setVar(vars, var, val):
    vars[varNames.index(var)] = val

def getVal(vars, var):
    return vars[varNames.index(var)]

varNames = "wxyz"

def runProgram(s):
    vars = ["0"] * 4
    vars[-1] = "z"
    i = 0

    for j, instr in enumerate(inp):
        if instr[0] == "inp":
            setVar(vars, instr[1], s[i])
            i += 1
            continue

        op, a, b = instr
        b = getVal(vars, b) if b in varNames else b

        if op == "add":
            if b == '0': continue
            setVar(vars, a, "(" + getVal(vars, a) + ")+" + b)
        elif op == "mul":
            if b == '0':
                setVar(vars, a, '0')
            else:
                setVar(vars, a, "(" + getVal(vars, a) + ")*" + b)
        elif op == "div":
            setVar(vars, a,  "(" + getVal(vars, a) + ")/" + b)
        elif op == "mod":
            setVar(vars, a, "(" + getVal(vars, a) + ")%" + b)
        elif op == "eql":
            setVar(vars, a, "(" + getVal(vars, a) + ")==" + b)

        # try: 
        #     result = eval(getVal(vars, a))
        #     setVar(vars, a, str(int(result)))
        # except:
        #     continue

    return vars

# print(runProgram("11"))

vars = runProgram("ab")

for v in vars:
    print(v)


