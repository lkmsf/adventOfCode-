from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys
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

def canBuildRobot(name, req, robots, resources):
    for key, val in req[name].items():
        if resources[key] < val: return False
    return True

def buildRobot(name, req, rob, res):
    for key, val in req[name].items():
        res[key] -= val
        if res[key] < 0: assert(False)
    rob[name] += 1
    return res, rob

def recBuild(name, req, rob, res, curr):
    for key, val in req[name]:
        if rob[key] == 0:
            curr += recBuild(key, req, rob, res)

def update(resources, robots): 
    for key, val in resources.items():
        resources[key] = val + robots[key]

def findNumGeode(line):
    resources = {"ore": 0, "cla": 0, "obs":0, "geo": 0}
    robots = {"ore": 1, "cla": 0, "obs":0, "geo":0}
    _ , ore, clay, obsOre, obsClay, geodeOre, geodeObs = line
    req = {}
    req["ore"] =  {"ore": ore}
    req["cla"] = {"ore": clay}
    req["obs"] =  {"ore": obsOre, "cla": obsClay}
    req["geo"] =  {"ore": geodeOre, "obs": geodeObs}

    print(req)

    # for i in range(TIME):
    #     print(i, resources, robots)
    #     if robots["cla"] == 0:
    #     if canBuildRobot("geo", req, robots, resources):
    #         buildRobot("geo", req, robots, resources)
    #     elif canBuildRobot("obs", req, robots, resources):
    #         buildRobot("obs", req, robots, resources)
    #     elif canBuildRobot("cla", req, robots, resources):
    #         buildRobot("cla", req, robots, resources)
    #     elif canBuildRobot("geo", req, robots, resources):
    #         buildRobot("geo", req, robots, resources)
    #     update(resources, robots)

    return resources["geo"]

qualities = []
for line in data:
    numGeodes = findNumGeode(line)
    qualities.append(numGeodes * line[0])
    break 

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
# def geode(req, resources, robots, curr):
#     if curr >= TIME:
#         return resources["geo"]
#     print(resources, " | ", robots, curr)
#     opt = []
#     for name in NAMES:
#         #print(name)
#         res, rob = buildRobot(name, req, robots, resources)
#         #print(res, rob)
#         if res == None: continue
#         res = update(res, robots)
#         geodes = geode(req, res, rob, curr + 1)
#         opt.append(geodes)

#     res = update(resources, robots)
#     geodes = geode(req, res, robots, curr + 1)
#     opt.append(geodes)

#     return max(opt)