from collections import Counter, defaultdict
from itertools import combinations
from math import cos, sin, radians, sqrt, tan

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    inp = [(x[:1], int(x[1:])) for x in inp]
    f.close()

    l = v = 0
    facing = 90 
    
    wl = 10 
    wv = 1

    for dr, amt in inp:
        if dr == "N": 
            v += amt 
        if dr == "S": 
            v += -amt 
        if dr == "E": 
            l += amt 
        if dr == "W": 
            l += -amt 
        
        if dr == "L": 
            facing += -amt 
        if dr == "R": 
            facing += amt 
            
        if dr == "F": 
            l += sin(radians(facing)) * amt
            v += cos(radians(facing)) * amt


    print(l,v)
    print(abs(l) + abs(v)) 

    l = v = 0
    facing = 90 
    
    wl = 10 
    wv = 1

    for dr, amt in inp:
        if dr == "N": 
            wv += amt 
        if dr == "S": 
            wv += -amt 
        if dr == "E": 
            wl += amt 
        if dr == "W": 
            wl += -amt 
        
        if dr in  "LR": 
            if dr == "R": amt *= -1
            ol, ov = wl, wv
            wl = cos(radians(amt)) * ol - sin(radians(amt)) * ov 
            wv = sin(radians(amt)) * ol + cos(radians(amt)) * ov 

        if dr == "F": 
            l += (wl * amt )
            v += (wv * amt )

        print(dr, amt, l, v, wl, wv)

    print(l,v)
    print(abs(l) + abs(v)) 

if __name__ == "__main__":
    main()
