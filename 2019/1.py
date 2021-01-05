from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    f = sys.stdin.read() 
    inp = f.splitlines() 
    inp = [int(x) for x in inp]
    
    part1, part2 = 0, 0 
    
    for e in inp:
        part1 += e//3 - 2
        part2 += fuel(e) 
    
    
    print(f"part1: {part1}, part2: {part2}")

def fuel(e): 
    if e <= 0: 
        return 0
    part = e//3 - 2
    return part + fuel(part)

if __name__ == "__main__":
    main()
