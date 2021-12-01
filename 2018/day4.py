from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("4.in") as f:
    #with open("test4.in") as f:
        inp = f.read()
        inp = inp.splitlines() 
    
    # org input
    inp = sorted(inp)
    shifts = [] 
    for e in inp:
        if "#" in e:
            num = re.findall(r"#(\d+)", e)
            shifts.append(num)
        else: 
            min = int(re.findall(r":(\d\d)", e)[0])
            shifts[-1].append(min)


    p1 = part1(shifts)
    p2 = part2(shifts)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
 

def part1(inp):
    guards = defaultdict(int)
    for e in inp:
        times = [e[i + 1] - e[i] for i in range(1, len(e), 2)]
        guards[e[0]] += sum(times)

    guardMostAsleep = max(guards, key= guards.get)

    timesAsleep = [0] * 60   
    for e in inp:
        if e[0] != guardMostAsleep:
            continue
        for i in range(1, len(e), 2):
            for m in range(e[i], e[i+1]):
                timesAsleep[m] += 1

    timeMostAsleep =  max(range(len(timesAsleep)), key = lambda a: timesAsleep[a])
    return int(guardMostAsleep) * timeMostAsleep

def part2(inp):
    guards = {}
    for e in inp:
        if e[0] not in guards:
            guards[e[0]] = [0] * 60

        for i in range(1, len(e), 2):
            for m in range(e[i], e[i+1]):
                guards[e[0]][m] += 1

    mostAsleepVal = -1
    mostAsleepID = -1
    mostAsleepMin = -1

    for g, times in guards.items():
        tmA =  max(range(len(times)), key = lambda a: times[a])
        if times[tmA] > mostAsleepVal:
            mostAsleepMin = tmA
            mostAsleepID = g
            mostAsleepVal = times[tmA]
    
    return int(mostAsleepID) * mostAsleepMin

    
if __name__ == "__main__":
    main()