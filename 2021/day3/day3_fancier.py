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
    result = ""
    for i in range(len(inp[0])):
        count = Counter(val[i] for val in inp)
        result += "1" if count["1"] > count["0"] else "0"

    num = int(result, 2)
    return num * (num ^ ((2**len(inp[0])) - 1))


# still gotta be a better way to do this:
def part2(inp):
    init = inp
    for i in range(len(inp[0])):
        count = Counter(val[i] for val in inp)
        curr = "1" if count["0"] <= count["1"] else "0"
        inp = [x for x in inp if x[i] == curr]
        if len(inp) == 1:
            break

    num1 = int(inp[0], 2)

    inp = init
    for i in range(len(inp[0])):
        count = Counter(val[i] for val in inp)
        curr = "0" if count["0"] <= count["1"] else "1"
        inp = [x for x in inp if x[i] == curr]
        if len(inp) == 1:
            break

    num2 = int(inp[0], 2)
    
    return num1 * num2


if __name__ == "__main__":
    main()