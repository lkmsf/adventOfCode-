from collections import Counter, defaultdict
from itertools import combinations, chain 
#import numpy as np
import re


def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read() 
    f.close()
    
    cups = [int(i) for i in inp.strip()]
    currVal = cups[0]
    part1, part2 = 0, 0 

    for i in range(100): 
        curr = cups.index(currVal)
        nextVal = cups[(curr + 4) % len(cups)]
        pickCups = cups[curr + 1:curr + 4]
        dest = cups[curr] - 1
        del cups[curr + 1: curr + 4]

        while len(pickCups) < 3: 
            pickCups.append(cups.pop(0))

        while True: 
            if dest in pickCups: 
                dest -= 1
            elif dest < 1: 
                dest = 9
            else: break 
        destIndex = cups.index(dest) 
        cups = cups[:destIndex + 1] + pickCups + cups[destIndex + 1:] 

        currVal = nextVal 

    
    cups = [str(x) for x in cups]
    part1 = "".join(cups[cups.index("1")+1:] + cups[:cups.index("1")])

    part2 = solvePart2(inp.strip())
    print(f"part1: {part1}, part2: {part2}")

class Node: 
    def __init__(self, val, next = None): 
        self.val = val 
        self.next = next 

def solvePart2(inp): 
    #inp = "389125467" 
    cups = [int(i) for i in inp]

    nodes = dict()# [0] * 1000001 

    head = Node(cups[0]) 
    nodes[cups[0]] = head
    prev = head 
    for e in list(cups[1:]) + list(range(10, 1000001)): 
        curr = Node(e) 
        nodes[e] = curr 
        prev.next = curr
        prev = curr 

    prev.next = head  #make circular 

    currNode = head 

    for i in range(10000000): 
        #pick cups 
        curr = currNode 
        pickedCups = set()
        pickedCupsNode = curr.next 
        for i in range(3): 
            curr = curr.next
            pickedCups.add(curr.val)
        nextRoundStart = curr.next 

        currNode.next = nextRoundStart  #remove picked cups 

        #get destination node 
        destVal = currNode.val - 1

        while True: 
            if destVal in pickedCups: 
                destVal  -= 1
            elif destVal  < 1: 
                destVal  = 1000000 
            else: break 

        destNode = nodes[destVal] 

        #rewire in picked cups 
        afterDest = destNode.next
        destNode.next = pickedCupsNode
        pickedCupsNode.next.next.next = afterDest

        currNode = nextRoundStart

    n1 = nodes[1]
    return n1.next.val * n1.next.next.val  


if __name__ == "__main__":
    main()
