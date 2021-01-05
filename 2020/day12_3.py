from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read()
    f.close()
        
    inp = re.findall(r"(.)(\d+)", inp)
    
    part1, part2 = 0, 0 


    d2i = {"N": 1j, "S": -1j, "E": 1, "W": -1}

    pos = 0 
    facing = 1

    for d, amt in inp: 
        print(d, amt)
        amt = int(amt)
        
        if d == "F": 
            pos += amt * facing
        elif d in "LR": 
            if d == "R": amt *= -1 
            facing *= 1j ** (amt//90)
        else: 
            pos += d2i[d] * amt 

    part1 = abs(pos.real) + abs(pos.imag)

    pos = 0  
    wp = 10 + 1j 

    for d, amt in inp: 
        print(d, amt)
        amt = int(amt)
        
        if d == "F": 
            pos += amt * wp
        elif d in "LR": 
            if d == "R": amt *= -1 
            wp *= 1j ** (amt//90)
        else: 
            wp += d2i[d] * amt 
    


    part2 = abs(pos.real) + abs(pos.imag)
    
    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
