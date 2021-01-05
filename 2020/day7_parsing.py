from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    f = sys.stdin.read() 
    inp = f.splitlines() 
    
    inp = [re.split(r" bags? contain ", x)  for x in inp]
    d = [(key, re.split(r"bags?,|.", val)) for key, val in inp]
    print(d.pop())

    #part1, part2 = 0, 0 

    #for e in inp:
    
    
    #print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
