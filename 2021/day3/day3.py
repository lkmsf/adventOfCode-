from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("3.in") as f:
    #with open("test3.in") as f:
        inp = f.read().strip()
        inp = inp.splitlines() 

    p1 = part1(inp)
    p2 = part2(inp)

    print(f"part1: {p1}")
    print(f"part2: {p2}")

    for i, part in enumerate([p1, p2]):
        print(f'bash submit.sh {i+1} {part}')


def part1(inp):
    gamma = epsilon = ""

    for i in range(len(inp[0])):
        n_one = n_zero = 0
        for val in inp:
            curr = val[i]
            if curr == "0":
                n_zero += 1
            else:
                n_one += 1
        if n_one > n_zero:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    g_num = int(gamma, 2)
    e_num = int(epsilon, 2)

    return g_num * e_num
    

def findMostCommon(inp, i):
    n_one = n_zero = 0
    for val in inp:
        curr = val[i]
        if curr == "0":
            n_zero += 1
        else:
            n_one += 1

    return "0" if n_zero > n_one else "1"

def part2(inp):
    return getOx(inp) * getCom(inp)


def getOx(inp):
    vals = inp

    for i in range(len(inp[0])):
        if len(vals) == 1:
            break
        mostCom = findMostCommon(vals, i)
        vals = [v for v in vals if v[i] == mostCom]

    return int(vals[0], 2)

def getCom(inp):
    vals = inp

    for i in range(len(inp[0])):
        if len(vals) == 1:
            break
        mostCom = findMostCommon(vals, i)
        vals = [v for v in vals if v[i] != mostCom]

    return int(vals[0], 2)

if __name__ == "__main__":
    main()