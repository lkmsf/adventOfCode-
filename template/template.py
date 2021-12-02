from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("%%DAY%%.in") as f:
    # with open("test%%DAY%%.in") as f:
        inp = f.read().strip()
        inp = inp.splitlines() 
        inp = inp.split("\n\n")

    inp = [int(x) for x in inp]
    inp = [x.split() for x in inp]

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")

    for i, part in enumerate([p1, p2]):
        print(f'bash submit.sh {i+1} {part}')


def part1(inp):
    for e in inp:
        return None

def part2(inp):
    return None
    
if __name__ == "__main__":
    main()