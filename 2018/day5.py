from collections import Counter, defaultdict
import enum
from itertools import combinations, chain
import re
import string
import sys
from string import ascii_letters, ascii_lowercase, ascii_uppercase

def main():
    with open("5.in") as f:
    # with open("test5.in") as f:
        inp = f.read()
        inp = inp.strip()

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")

def shouldReact(c, d):
    if c.islower() == d.islower():
        return False
    return c.lower() == d.lower()

def part1(inp:string):
    i = 0
    while i < len(inp) - 1:
        c = inp[i]
        nextC = inp[i + 1]
        if shouldReact(c, nextC):
            inp = inp[:i] + inp[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
    return len(inp)

def part2(inp):
    shortestLen = len(inp)
    for c in ascii_lowercase:
        s = inp.replace(c, "")
        s = s.replace(c.upper(), "")
        curr = part1(s)
        shortestLen = min(shortestLen,  curr)
    return shortestLen

if __name__ == "__main__":
    main()