from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
import numpy as np
from functools import lru_cache

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

data = []
for line in inp:
    numbers = re.findall("\d+", line)
    #  num, ore, clay, obsOre, obsClay, geodeOre, geodeObs 
    numbers = [int(x) for x in numbers]
    data.append(numbers)

TIME = 24
NAMES = ["ore", "cla", "obs", "geo"]

def buildRobot(name, req, robots, resources):
    currRequirements = req[NAMES.index(name)]

    if not all(robots[i] > 0 for i in range(len(robots)) if currRequirements[i]): 
        #print(f"    no robots to make requirements for {name} - {currRequirements}")
        return None, None, None

    daysPerRes = [math.ceil((currRequirements[i] - resources[i]) / robots[i]) for i in range(len(robots)) if currRequirements[i]]
    #print(f"    days needed: {daysPerRes}")
    days = max(max(daysPerRes),0) + 1 
    #print(f"    we need {days} to build {name}")

    robs = robots.copy()
    robs[NAMES.index(name)] += 1

    #print(f"    {resources} + ({days} * {robs}) - {currRequirements}")
    res = resources + (days * robots) - currRequirements

    return np.array(res), np.array(robs), days

#order = ["cla", "cla", "cla", "obs", "cla", "obs", "geo", "geo"]
def geode(mem, req, resources, robots, curr, maxs, i):
    # key = ",".join(map(str, resources)) + "|" + ",".join(map(str, robots)) + str(curr)
    # if key in mem:
    #     return mem[key]
    #print(f"----------{curr}----------")
    # print(i * "     ", robots, " | ", resources, curr)
    if curr == TIME:
        return resources[NAMES.index("geo")]
    opt = []
    for name in NAMES:
        if robots[NAMES.index(name)] == maxs[NAMES.index(name)]: 
            #print(f"took many robots for {name}")
            continue
        if resources[NAMES.index(name)] >= ((TIME - curr) * maxs[NAMES.index(name)]): 
            #print(f"too many resources for {name}")
            continue
        #print(name)
        res, rob, days = buildRobot(name, req, robots, resources)
        #print("   ", rob, " | ", res, curr + days)
        if days == None: continue
        if curr + days > TIME: continue
        geodes = geode(mem, req, res, rob, curr + days, maxs, i + 1)
        opt.append(geodes)

    if not opt:
        #print("no options")
        return (TIME - curr) * robots[NAMES.index("geo")]
    result = max(opt)
    # mem[key] = result
    return result

def findNumGeode(line):
    resources = np.array([0, 0, 0, 0])
    robots = np.array([1, 0, 0, 0])
    _ , ore, clay, obsOre, obsClay, geodeOre, geodeObs = line
    req = [np.array(x) for x in [[ore, 0, 0, 0], [clay, 0, 0, 0], [obsOre, obsClay, 0, 0], [geodeOre, 0, geodeObs, 0]]]
   #print(req)
    mem = {}
    maxs = [max([x[i] for x in req]) for i in range(len(NAMES))]
    maxs[-1] = TIME
    #print(maxs)
    return geode(mem, req, resources, robots, 1, maxs, 0)

qualities = []
for line in data:
    numGeodes = findNumGeode(line)
    qualities.append(numGeodes * line[0])

print(qualities)
print(sum(qualities))

# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.

# Blueprint 2:
#   Each ore robot costs 2 ore.
#   Each clay robot costs 3 ore.
#   Each obsidian robot costs 3 ore and 8 clay.
#   Each geode robot costs 3 ore and 12 obsidian.