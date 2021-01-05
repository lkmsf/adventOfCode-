from collections import Counter, defaultdict
from itertools import combinations, chain 
#import numpy as np 
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read()
    f.close()
    
    part1, part2 = 0, 0 

    splitInp = re.findall(r"(.+) \(contains (.+)\)\n" , inp)
    foods = [[a.split(), b.split(", ")] for a, b in splitInp] 

    allIng = [] 

    possibles = defaultdict(list) 
    for ing, alg in foods: 
        for a in alg: 
            possibles[a].append(set(ing)) 

        for i in ing: allIng.append(i)

    allIng = Counter(allIng)

    intersected = {} 
    for key, val in possibles.items(): 
        intersected[key] = set.intersection(*val)

    possibleContainAllergen = set([i for x in intersected.values() for i in x]) 
    
    notAllergen = set(allIng.keys()) - possibleContainAllergen

    for i in notAllergen: 
        part1 += allIng[i] 

    allergens = {} 
    alreadyAdded = set()
    for key in sorted(intersected, key = lambda a: len(intersected[a])): 
            val = (intersected[key] - alreadyAdded).pop() 
            allergens[key] = (val)
            alreadyAdded.add(val) 
    
    sort = sorted(allergens.items()) 
    print(",".join([k[1] for k in sort])) 

    print(f"part1: {part1}, part2: {part2}")

if __name__ == "__main__":
    main()
