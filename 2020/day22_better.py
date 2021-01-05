from collections import Counter, defaultdict
from itertools import combinations, chain 
#import numpy as np 
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().split("\n\n")
    f.close()

    p1, p2 = inp
    p1 = p1.splitlines()[1:]
    p2 = p2.splitlines()[1:]

    p1 = [int(x) for x in p1]
    p2 = [int(x) for x in p2]
    
    part1, part2 = 0, 0 

    p1_2, p2_2 = p1.copy(), p2.copy()

    while len(p1) > 0 and len(p2) > 0: 
        p1C = p1.pop(0)
        p2C = p2.pop(0)
        if p1C > p2C: 
            p1.extend([p1C, p2C]) 
        else:  
            p2.extend([p2C, p1C]) 

    if len(p1) == 0: 
        p1 = p2
    part1 = sum([x * m for x, m in enumerate(reversed(p1), 1)])  

    #part 2
    part2 = recursiveCombat(p1_2, p2_2, set()) 
    part2 = p1_2 if len(p1_2) != 0 else p2_2
    part2 = sum([x * m for x, m in enumerate(reversed(part2), 1)])  
    
    print(f"part1: {part1}, part2: {part2}")

def recursiveCombat(p1, p2, currRound):  
    while len(p1) > 0 and len(p2) > 0: 
        if (tuple(p1), tuple(p2)) in currRound: 
            return 1 
        currRound.add((tuple(p1), tuple(p2)))

        p1C = p1.pop(0) 
        p2C = p2.pop(0) 

        if len(p1) >= p1C and len(p2) >= p2C: 
            winner = recursiveCombat(p1[:p1C], p2[:p2C], set())
        else: 
            winner = 1 if p1C > p2C else 2
        
        if winner == 1: 
            p1 += [p1C, p2C]
        else: 
            p2 += [p2C, p1C]

    return 1 if len(p1) != 0 else 2 
    
#def recursiveCombat(p1, p2, currRound): #, mem): 
#    while len(p1) > 0 and len(p2) > 0: 
#        if (tuple(p1), tuple(p2)) in currRound: 
#            return p1, p2, 1 
#        currRound.add((tuple(p1), tuple(p2)))
#
#        p1C = p1[0]
#        p2C = p2[0]
#
#        p1 = p1[1:]
#        p2 = p2[1:]
#
#        if len(p1) >= p1C and len(p2) >= p2C: 
#            _, _,  winner = recursiveCombat(p1[:p1C], p2[:p2C], set())
#        else: 
#            winner = 1 if p1C > p2C else 2
#        
#        if winner == 1: 
#            p1.extend([p1C, p2C])
#        else: 
#            p2.extend([p2C, p1C]) 
#
#    result = p1, p2, (1 if len(p1) != 0 else 2) 
#    return result

if __name__ == "__main__":
    main()
