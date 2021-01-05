from collections import Counter, defaultdict
from itertools import combinations, chain 
#import numpy as np
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read() 
    f.close()
    
    cups = [int(i) for i in inp.strip()]
    currVal = cups[0]
    part1, part2 = 0, 0 

    for i in range(100): 
        curr = cups.index(currVal)
        nextVal = cups[(curr + 4) % len(cups)]
        print(i + 1, cups, cups[curr])
        pickCups = cups[curr + 1:curr + 4]
        dest = cups[curr] - 1
        del cups[curr + 1: curr + 4]

        while len(pickCups) < 3: 
            pickCups.append(cups.pop(0))

        while True: 
            if dest in pickCups: 
                dest -= 1
            elif dest < 1: 
                dest = 9
            else: break 
        destIndex = cups.index(dest) 
    
        #if destIndex != 0: 
        cups = cups[:destIndex + 1] + pickCups + cups[destIndex + 1:] 
        #jelse: 
         #   cups = pickCups[-1:] + cups[1:] + cups[destIndex:destIndex + 1] + pickCups[:-1] 

        currVal = nextVal 

    
    cups = [str(x) for x in cups]
    part1 = "".join(cups[cups.index("1")+1:] + cups[:cups.index("1")])

    #part 2 
    cups = [int(i) for i in inp.strip()]
    #cups.extend(range(max(cups), 1000000))
    currVal = cups[0]


 #   for i in range(10000000): 
 #       curr = cups.index(currVal)
 #       nextVal = cups[(curr + 4) % len(cups)]
 #       pickCups = cups[curr + 1:curr + 4]
 #       dest = cups[curr] - 1
 #       del cups[curr + 1: curr + 4]

 #       while len(pickCups) < 3: 
 #           pickCups.append(cups.pop(0))

 #       while True: 
 #           if dest in pickCups: 
 #               dest -= 1
 #           elif dest < 1: 
 #               dest = 9
 #           else: break 
 #       destIndex = cups.index(dest) 
 #   
 #       #if destIndex != 0: 
 #       cups = cups[:destIndex + 1] + pickCups + cups[destIndex + 1:] 
 #       #jelse: 
 #        #   cups = pickCups[-1:] + cups[1:] + cups[destIndex:destIndex + 1] + pickCups[:-1] 

 #       currVal = nextVal 

    index1 = cups.index(1) 
    part2 = cups[index1 + 1] * cups[index1 + 2] 

    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
