from collections import Counter, defaultdict
from itertools import combinations
import copy 

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    inp = [[c for c in x] for x in inp]
    f.close()

    while True: 
        inp, stable = applyRule(inp)
        #for i in inp: 
        #    print ("".join(i))
        #print ()
        if stable: break 

    numOcp = 0
    for i in range(len(inp)): 
        for j in range(len(inp[0])):
            if inp[i][j] == "#": 
                numOcp += 1
    print (numOcp)

def applyRule(inp): 
    nxt  = copy.deepcopy(inp) 
    numChanges = 0
    for i in range(len(inp)): 
        for j in range(len(inp[0])): 
            if inp[i][j] == "L": 
                if numAdj(inp, i, j) == 0: 
                    nxt[i][j] = "#" 
                    numChanges += 1
            elif inp[i][j] == "#": 
                if numAdj(inp, i, j) >= 5:#4: 
                    nxt[i][j] = "L"
                    numChanges += 1

    return nxt, numChanges == 0

def numAdj(inp, r, c): 
    count = 0
    for i in range(r - 1, r + 2): 
        for j in range(c - 1, c + 2): 
            if not inBounds(inp,i, j): continue 
            if i == r and j == c: continue 
            #if inp[i][j] == "#": 
            if adjOcp(inp, r,c, i, j): 
                count += 1
    return count

def adjOcp(inp, r0, c0, r1, c1): 
    r, c = r1, c1
    while True:  
        if inp[r][c] == "#": return True 
        if inp[r][c] == "L": break   
        r += (r1 - r0) 
        c += (c1 - c0)
        if not inBounds(inp, r, c): break 
    return False 

def inBounds(inp, r, c):
    if r < 0 or r >= len(inp): return False  
    if c < 0 or c >= len(inp[0]): return False    
    return True 

if __name__ == "__main__":
    main()
