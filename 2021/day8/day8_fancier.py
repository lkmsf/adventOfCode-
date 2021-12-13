from collections import Counter, defaultdict
from itertools import combinations, chain, permutations 
import re
import sys

with open("8.in") as f:
#with open("test8.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines() 

inp = [[a.split() for a in x.split(" | ")] for x in inp]

letters = "abcdefg"
nums = {0: "abcefg", 1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}

def findMapping(sig):
    for opt in permutations(letters):
        opt = "".join(opt)
        currMapping = {oldC: newC for oldC, newC in zip(letters, opt)}
        mapping = {}
        for i in range(10):
            wouldBe = "".join(sorted(currMapping[x] for x in nums[i]))
            if wouldBe not in sig:
                break
            mapping[wouldBe] = i
        if len(mapping) == 10: 
            return mapping

total = 0
for signals, out in inp:
    signals = ["".join(sorted(x)) for x in signals]
    mapping = findMapping(signals)
    output = "".join([str(mapping["".join(sorted(x))]) for x in out]) 
    total += int(output)


print(total)