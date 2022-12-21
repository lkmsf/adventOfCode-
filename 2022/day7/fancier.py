# from collections import Counter, defaultdict
# from itertools import combinations, chain, accumulate
# import re
# import statistics
# import math
# import sys

# inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

# with open(inputFile) as f:
#     inp = f.read().strip()
#     inp = inp.splitlines() 

# inp = [x.split() for x in inp]

# dir = {}

# sizes = {}
# curr = ["/"]

# i = 0
# while i < len(inp):
#     line = inp[i]
#     match line:
#         case '$', 'cd', x:
#             curr.append(x)
#         case '$', 'cd', '/':
#             curr = ["/"]
#         case '$', 'cd', '..':
#             del curr[-1]
#         case '$', 'ls' | 'dir', _:
#             pass
#         case size, _:
#             currPath = ""
#             for path in accumulate(curr):
#                 sizes[currPath] = sizes.get(currPath, 0) + int(size)
#     i += 1

# leftOver = 30000000 - (70000000 - sizes["/"])

# bigEnough = {key:val for key,val in sizes.items() if val >= leftOver}

# print(min(bigEnough.values()))