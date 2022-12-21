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

class Node: 
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

def printL(start):
    print(start.val, end = ", ")
    curr = start.next
    while start != curr:
        print(curr.val, end = ", ")
        curr = curr.next
    print("")


start = None
nodes = [Node(x * 811589153) for x in inp]
for a, b in zip(nodes, nodes[1:]):
    if a.val == 0:
        start = a
    a.next = b
    b.prev = a

nodes[0].prev = nodes[-1]
nodes[-1].next = nodes[0]

#printL(start)
for i in range(10):
    for node in nodes: 
       # printL(start)
        if node.val == 0: continue
        #remove node
        # if node == start:
        #     start = node.next
        node.prev.next = node.next
        node.next.prev = node.prev

        amt = abs(node.val) % (len(nodes) - 1)
        insertAfterMe = node
        if node.val < 0:
            insertAfterMe = insertAfterMe.prev
            for i in range(amt):
                insertAfterMe = insertAfterMe.prev
        else: 
            for i in range(amt):
                insertAfterMe = insertAfterMe.next

        # insert node
        insertBeforeMe = insertAfterMe.next
        insertBeforeMe.prev = node
        node.next = insertBeforeMe
        insertAfterMe.next = node
        node.prev = insertAfterMe

    #printL(start)
    #break

vals = []
for i in [1000, 2000, 3000]:
    i = i % len(nodes)
    curr = start
    for _ in range(i):
        curr = curr.next
    vals.append(curr.val)

print(vals)
print(sum(vals))

#     Initial arrangement:
# 1, 2, -3, 3, -2, 0, 4
#1, 2, -3, 3, -2, 0, 4, 


# 1 moves between 2 and -3:
# 2, 1, -3, 3, -2, 0, 4
 
# 2 moves between -3 and 3:
# 1, -3, 2, 3, -2, 0, 4

# -3 moves between -2 and 0:
# 1, 2, 3, -2, -3, 0, 4

# 3 moves between 0 and 4:
# 1, 2, -2, -3, 0, 3, 4
# 1, 2, -2, -3, 0, 3, 4, 

# -2 moves between 4 and 1:
# 1, 2, -3, 0, 3, 4, -2
# -2, 1, 2, -3, 0, 3, 4, 

# 0 does not move:
# 1, 2, -3, 0, 3, 4, -2
# -2, 1, 2, -3, 0, 3, 4,
# 4 moves between -3 and 0:
# 1, 2, -3, 4, 0, 3, -2

