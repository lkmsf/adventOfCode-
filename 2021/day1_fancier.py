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

    calc_increase = lambda win: sum(f > e for e, f in zip(inp, inp[win:]))
    p1 = calc_increase(1)
    p2 = calc_increase(3)

    print(f"part1: {p1}")
    print(f"part2: {p2}")


if __name__ == "__main__":
    main()