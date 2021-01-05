from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().split("\n\n")
    f.close()
    
    part1, part2 = 0, 1 

    rules, my, nearby = inp 

    rules = re.findall(r"(.+): (.+)-(.+) or (.+)-(.+)", rules)    
    rules = {name: set(chain(range(int(a), int(b)  + 1), range(int(c), int(d)+ 1))) for name, a, b, c, d in rules }

    my = list(map(int, my.splitlines()[1].split(',')))
    
    nearby = [list(map(int, x.split(","))) for x in nearby.splitlines()[1:]]
    
    part1 = sum(n for t in nearby for n in t if not any(n in l for l in rules.values())) 

    
    #part2 
    valids = [v for v in nearby if all( any(n in l for l in rules.values()) for n in v)]
    possibleFields = { name: {i for i in range(20) if all(n[i] in nums for n in valids) } 
                for name, nums in rules.items() }    
    
    used = set() 

    for name in sorted(possibleFields, key = lambda x: possibleFields[x]): 
        if name.startswith("departure"): 
            part2 *= my[(possibleFields[name] - used).pop()] 
        used.update(possibleFields[name])



    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
