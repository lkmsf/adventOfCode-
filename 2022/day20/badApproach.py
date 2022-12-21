from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()
    inp = inp.splitlines() 
    
inp = [int(x) for x in inp]

order = inp.copy()

nums = {i: i for i in range(len(order))}


def printList(m):
    for i in range(len(m)):
        print(order[m[i]], end =", ")
    print()

for idx in range(len(order)):
    printList(nums)
    val = nums[idx]
    if order[val] == 0: continue

    origI = [key for key, val in nums.items() if val == idx][0]
    newPos = (order[idx] + origI) 
    if newPos < 0:
        newPos += len(nums)
    elif newPos >= len(nums):
        newPos = newPos % len(nums)

    newNums = {i: i for i in range(len(order))}
    if newPos == origI:
        print(f"newPod == origI - {newPos}, {origI}")
        pass
    elif newPos < origI:
        print(f"newPod < origI - {newPos}, {origI}")
        # 1,     -3, -1, -2, -2, 0, 4,
        # 1, -2, -3, -1,     j-2, 0, 4,
        for i in range(newPos):
            newNums[i] = nums[i]
        newNums[newPos] = order[val]
        for i in range(newPos + 1, origI): 
            newNums[i] = nums[i - 1 if i - 1 >= 0 else len(order) - 1]
        for i in range(origI, len(order)):
            newNums[i] = nums[i]
    else:     # origI < newPos
        print(f"origI < newPos - {origI}, {newPos}")
        # 1, 2, -1,    -2, -2, 0, 4,
        # 1,    -1, 2, -2, -2, 0, 4,
        for i in range(origI):
            newNums[i] = nums[i]
        for i in range(origI, newPos): 
            if i == 0: newNums[i] = nums[i - 1 if i - 1 >= 0 else len(order) - 1]
            else: newNums[i] = nums[i + 1 % len(order)]
        newNums[newPos] = order[origI]
        for i in range(newPos + 1, len(order)):
            newNums[i] = nums[i - 1 if i - 1 >= 0 else len(order) - 1]
    nums = newNums

result = 0
for val in [1000, 2000, 3000]:
    result += order[nums[val % len(order)]]
print(result)
# 1, 2, -3, 3, -2, 0, 4, 
# 0, 1