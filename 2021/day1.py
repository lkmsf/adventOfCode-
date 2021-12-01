from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

def main():
    with open("1.in") as f:
    # with open("test1.in") as f:
        inp = f.read()
        inp = inp.strip()
        inp = inp.splitlines() 

    inp = [int(x) for x in inp]

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")


def part1(inp):
    c = 0
    prev = inp[0] 
    for i in range(1, len(inp)):
        curr = inp[i]
        if curr > prev:
            c += 1
        prev = curr
    return c

def part2(inp):
    c = 0
    prev = sum(inp[0:3])
    for i in range(3, len(inp)):
        curr = prev - inp[i - 3] + inp[i]
        if curr > prev:
            c += 1
        prev = curr
    return c
    
if __name__ == "__main__":
    main()