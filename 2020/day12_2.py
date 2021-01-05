from collections import Counter, defaultdict
from itertools import combinations
from math import cos, sin, radians, sqrt, tan

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    inp = [(x[:1], int(x[1:])) for x in inp]
    f.close()

    d = {'N': complex(0,1),  'S': complex(0,-1),  'E': complex(1,0),  'W': complex(-1,0)}
    drev = {value:key for key,value in d.items()}

    pos = complex(0, 0)
    heading  = complex(1, 0)

    for dr, amt in inp:
        if dr == "F": 
           dr = drev[heading]
        if dr in "NSEW": 
            pos += d[dr] * amt
        
        elif dr in  "LR": 
            mult = 1 if dr == "L" else -1
            heading *= (mult * 1j) ** (amt//90) 

    print(abs(pos.real) + abs(pos.imag)) 

 
    pos = complex(0, 0)
    wp  = complex(10, 1)

    for dr, amt in inp:
        if dr == "F": 
           pos += wp * amt   

        elif dr in "NSEW": 
            wp += d[dr] * amt
        
        elif dr in  "LR": 
            mult = 1 if dr == "L" else -1
            wp *= (mult * 1j) ** (amt//90) 
                  
    print(pos)
    print(abs(pos.real) + abs(pos.imag)) 

 

if __name__ == "__main__":
    main()
