from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    inp = sys.stdin.read()
    inp = inp.splitlines() 
    inp = [int(x) for x in inp]
    door, card = inp 

    part1, part2 = 0, 0 

    #get card loop size 
    val = 1 
    i = 0 
    subjectNum = 7
    while True: 
        i += 1
        val *= subjectNum
        val %= 20201227
        if val == card: 
            break 

    val = 1
    subjectNum = door 
    for _ in range(i): 
        val *= subjectNum
        val %= 20201227
        if val == card: 
            break 
    part1 = val
    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
