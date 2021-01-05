from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    f = sys.stdin.read() 
    inp = f.split(",")
    inp = [int(x) for x in inp]
    
    part1, part2 = 0, 0 
    part1 = runProgram(inp.copy(), 12, 2)

    for i in range(100): 
        for j in range(100): 
            if runProgram(inp.copy(), i, j) == GOAL: 
                part2 = 100 * i + j 
                break 

    print(f"part1: {part1}, part2: {part2}")

def runProgram(inp, i, j): 
    inp[1] = i 
    inp[2] = j

    i = 0
    while True: 
        if inp[i] == 99: break 
        elif inp[i] == 1: i = op1(inp, i)
        elif inp[i] == 2: i = op2(inp, i)

    return  inp[0] 

def op1(inp, i):
    n1, n2, n3 = inp[i + 1: i + 4]
    inp[n3] = inp[n1] + inp[n2]
    return i + 4

def op2(inp, i):
    n1, n2, n3 = inp[i + 1: i + 4]
    inp[n3] = inp[n1] * inp[n2]
    return i + 4

def op3(inp, i, val):
    n1 = inp[i + 1]
    inp[n1] = val 
    return i + 1

def op4(inp, i):
    n1 = inp[i + 1]
    return i + 1, inp[n1]


if __name__ == "__main__":
    main()
