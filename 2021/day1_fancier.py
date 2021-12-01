from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("1.in") as f:
    # with open("test1.in") as f:
        inp = f.read().strip()
        inp = inp.splitlines() 

    inp = [int(x) for x in inp]

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")


def part1(inp):
    return sum(1 for e, f in zip(inp, inp[1:]) if f > e)

def part2(inp):
    windows = [sum((a, b, c)) for a, b, c in zip(inp, inp[1:], inp[2:])]
    return sum(1 for e, f in zip(windows, windows[1:]) if f > e)
    
if __name__ == "__main__":
    main()