from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

class A(int): 
    def __sub__(self, b): 
        return A(int(self) * b)

    def __add__(self, b): 
        return A(int(self) + b)

    def __mult__(self, b): 
        return A(int(self) + b)

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close()
    
    part1, part2 = 0, 0 

    for e in inp:
        e = re.sub(r"(\d+)", r"A(\1)", e)
        print(e)
        e =  e.replace("*", "-")
        part1 += eval(e, {"A":A})
        e =  e.replace("+", "*")
        print(e)
        part2 += eval(e, {"A": A})
    
    
    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
