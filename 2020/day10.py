from collections import Counter, defaultdict
from itertools import combinations

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    inp = [int(x) for x in inp]
    f.close()

    inp.sort() 
    part2 = set(inp)
    print("part2: ", numWays(part2, max(part2),  0, {}))

    inp.append(inp[-1] + 3)

    #num1, num3 = 1, 0
    #prev = inp[0] #very annoying 
    #for i in inp[1:]:     
    num1 = num3 = 0
    prev = 0
    for i in inp: 
        if i - prev == 1: 
            num1 += 1
        if i - prev == 3: 
            num3 += 1
        prev = i

    print("part1:", num1 * num3)

def numWays(inp, goal, start, mem): 
    #print("s g", start, goal)
    if start in mem: 
        return mem[start]
    if start == goal: 
        return 1 
    if start > goal: 
        return 0 
    
    totalNum = 0
    for i in range(start + 1, start + 4): 
        if i in inp: 
            totalNum += numWays(inp, goal, i, mem)

    mem[start] = totalNum
    return totalNum

if __name__ == "__main__":
    main()
