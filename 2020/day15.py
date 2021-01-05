from collections import Counter, defaultdict
from itertools import combinations
import copy 


def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().split(",")
    inp = [int(x) for x in inp]
    f.close()

    turnNum = 1 
    spokenLast = {} 

    n = inp[0] 
    nextNum = inp[1]
    while turnNum <= 2020: #30000000: 

        if turnNum <= len(inp): 
            nextNum = inp[turnNum - 1]
        elif n in spokenLast: 
            nextNum = turnNum - spokenLast[n] 
        else: 
            nextNum  = 0 

        spokenLast[n] = turnNum
        turnNum += 1
        n = nextNum 

    print(n)
    
    turnNum = 1 
    spokenLast = {} 

    n = inp[0] 
    while turnNum <= 2020: 
        spokenLast[n] = turnNum

        if turnNum <= len(inp): 
            n = inp[turnNum - 1]
        elif n in spokenLast: 
            n = turnNum - spokenLast[n] 
        else: 
            n  = 0 

        turnNum += 1

    print(n)

if __name__ == "__main__":
    main()
