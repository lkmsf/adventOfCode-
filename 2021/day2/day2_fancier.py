from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("2.in") as f:
    # with open("test2.in") as f:
        inp = f.read().strip()
        inp = inp.splitlines() 

    inp = [x.split() for x in inp]

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")

def part1(inp):
    h = d = 0
    for dir, val in inp:
        val = int(val)
        if dir == "forward":
            h += val
        elif dir == "up":
            d -= val
        elif dir == "down":
            d += val
    return h * d


def part2(inp):
    h = d = a = 0
    for dir, val in inp:
        val = int(val)
        if dir == "forward":
            h += val
            d += a * val
        elif dir == "up":
            a -= val
        elif dir == "down":
            a += val
    return h * d
    
if __name__ == "__main__":
    main()