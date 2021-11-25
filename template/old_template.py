from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    f = sys.stdin.read() 
    inp = f.splitlines() 
    inp = f.split("\n\n")
    inp = [int(x) for x in inp]
    inp = [x.split() for x in inp]
    
    part1, part2 = 0, 0 

    for e in inp:
    
    
    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
