from collections import Counter, defaultdict
from itertools import combinations
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close()

    data = defaultdict(lambda: defaultdict(list)) 
    currG = 0 
    currSleepStart = 0
    for e in inp:
        times, action = e.split("]")
        date, mins = times.split() 
        minPlace = int(mins.split(":")[1])
        if "Guard" in action: 
            currG = re.search("#\d+", action).group()
            currG = int(currG[1:])
        elif "falls" in action: 
            currSleepStart = minPlace
        elif "wakes" in action: 
            for i in range(currSleepStart, minPlace): 
                data[currG][i].append(date)

    #x = 1973
    #print(sum([len(data[x][i]) for i in data[x]])) 
    mostAsleep = max(data, lambda x: sum([len(data[x][i]) for i in data[x]])) 
    minMostSleep = max(data[mostAsleep], lambda x: data[mostAsleep][x])
    print(mostAsleep * minMostSleep)

            
         

    


if __name__ == "__main__":
    main()
