from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    rules, messages = f.read().split("\n\n")
    f.close()


    part1, part2 = 0, 0 

    rulesD = dict() 

    for r in rules.splitlines(): 
        if r.startswith("8:"):   #only change for part 2
            r = "8: 42 | 42 8" 
        elif r.startswith("11:"): 
            r = "11: 42 31 | 42 11 31" 

        key, value = r.split(":")
        values = [i.split() for i in value.split("|")] 
        if not values[0][0].isnumeric(): 
            values = values[0][0][1:-1]
        rulesD[key.strip()] = values
    

    mem = {}
    c = 0 
    for i in messages.splitlines(): 
        if follow(rulesD, '0', i, mem): 
            print("*", end = "", flush = True)
            part2 += 1

        else: 
            print("-", end = "", flush = True)
        c += 1
    
    print()
    print(f"part1: {part1}, part2: {part2}")

def follow(rules, rn, s, mem): 
    if (rn, s) in mem: 
        return mem[(rn, s)] 

    if isinstance(rules[rn], str): 
        return s == rules[rn]
        
    result = any(followsRuleSet(rules, n, s, mem) for n in rules[rn])

    mem[(rn, s)] = result 
    return result 

def followsRuleSet(rules, ruleList, s, mem): 
    key = (tuple(ruleList), s)
    if key in mem: 
        return mem[key] 

    if not ruleList: 
        return s == ""  

    for i in range(len(s)): 
        if follow(rules, ruleList[0], s[:i + 1], mem): 
            if followsRuleSet(rules, ruleList[1:], s[i+1:], mem): 
                mem[key] = True 
                return True 

    mem[key] = False  
    return False  


if __name__ == "__main__":
    main()
