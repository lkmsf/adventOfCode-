from collections import Counter, defaultdict
from itertools import combinations
import math 

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    earliestTime = int(inp[0]) 
    print(earliestTime)
    buses  = [x.split(",") for x in inp[1:]]
    f.close()

    busNums = [int(x) for x in buses[0] if x.isnumeric()] 

    busesInOrder = buses[0]

    buses = busNums

    time = buses.copy() 
    
    largestTimes = time.copy() 
    for i in range(len(time)): 
        while largestTimes[i] < earliestTime: 
            largestTimes[i] += time[i]

    
    bestIndex = min(range(len(time)), key = lambda i: largestTimes[i]) 

    print(busNums[bestIndex], largestTimes[bestIndex]- earliestTime)
    print(busNums[bestIndex] * (largestTimes[bestIndex]- earliestTime)) 

    i = max(buses) 

    inc = 1
    while True: 
        result, inc = isValid(i, busesInOrder, inc)
        if result: break 
        i += inc

    print(i)

def isValid(time, buses, oldInc): 
    for i in range(len(buses)): 
        if buses[i] == "x": continue 
        
        if ((time + i) % int(buses[i]) == 0) : 
            oldInc = lcm(oldInc, int(buses[i]))
            print(oldInc, buses[i])
        else: 
            return False, oldInc

    return True, None 

def lcm(a, b): 
    return abs(a*b) //math.gcd(a,b)

if __name__ == "__main__":
    main()
