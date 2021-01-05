from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

def main():
    with open("input.txt") as f: 
    #f = open("ex.txt")
        inp = f.read().splitlines() 
    
    
    for dim in [3]:
        neighbors = [(0,) * (dim - 2) + (i, j) for i in range()]

        points = [(0,) * (dim - 2) + (i, j) for i, l in enumerate(inp) for j, elem in enumerate(l) if elem == "#" ]
        print(points)


        print(result)
    
    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
