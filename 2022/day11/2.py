from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import numpy as np
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.split("\n\n")


data = {}
for i, elem in enumerate(inp):
    _, starting, op, test, true, false = elem.splitlines()
    starting = [int(x) for x in re.findall("\d+", starting)]
    op = " ".join(op.split()[-3:])
    test = int(test.split()[-1])
    true = int(true.split()[-1])
    false = int(false.split()[-1])
    curr = [starting, op, test, true, false]
    data[i] = curr

inspections = [0 for i in range(len(data))]

prod = [x[2] for x in data.values()]
div = np.prod(prod)

def monkey(monkeys, i):
    starting, op, test, true, false = monkeys[i]
    for item in starting:
        inspections[i] += 1
        old = item
        curr = eval(op) % div
        if curr % test == 0:
            monkeys[true][0].append(curr)
        else:
            monkeys[false][0].append(curr)
    monkeys[i][0] = []


def doRound(monkeys):
    for i in range(len(data)):
        monkey(monkeys, i)

for i in range(10000):
    prev = inspections.copy()
    doRound(data)

inspections = sorted(inspections)
print(inspections)
print(inspections[-1] * inspections[-2])
