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

    for i, part in enumerate([p1, p2]):
        print(f'bash submit.sh {i+1} {part}')


def part1(inp):
    h = 0
    d = 0
    for dir, val in inp:
        if dir == "forward":
            h += int(val)
        elif dir == "up":
            d -= int(val)
        elif dir == "down":
            d += int(val)
    return h * d


def part2(inp):
    h = 0
    d = 0
    a = 0
    for dir, val in inp:
        if dir == "forward":
            h += int(val)
            d += a * int(val)
        elif dir == "up":
            a -= int(val)
        elif dir == "down":
            a += int(val)
    return h * d
    
if __name__ == "__main__":
    main()