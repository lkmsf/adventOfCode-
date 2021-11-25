from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("%%FILE_NAME_HERE%%") as f:
        inp = f.read()
        inp = tmp.splitlines() 
        inp = tmp.split("\n\n")

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
 

def part1(inp):
    inp = [int(x) for x in inp]
    inp = [x.split() for x in inp]
    for e in inp:

def part2(inp):
    return None
    
if __name__ == "__main__":
    main()