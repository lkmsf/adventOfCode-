from collections import Counter, defaultdict
from itertools import combinations, chain 
import re

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close()
    
    part1, part2 = 0, 0 

    for e in inp:
        part1 += eval(addOrderParens(e))
        e = eval(addOrderParens(addAdditionParens(e)) ) 
        part2 += e
         
    print(f"part1: {part1}, part2: {part2}")

def addAdditionParens(e): 
    if "+" not in e: return e
    elems = []

    if "(" in e: 
        elems = splitByParen(e)
        for i in range(len(elems)): 
            if elems[i][0] == "(" : 
                elems[i] =  "(" + addAdditionParens(elems[i][1:-1]) + ")" 

    else: elems = e.split()

    i = 0
    while(i < len(elems) - 1): 
        if elems[i + 1] == "+": 
            elems[i] = "("+ " ".join(elems[i:i+3]) + ")" 
            del elems[i+1:i+3]
        else: 
            i += 2

    return " ".join(elems)

def addOrderParens(e): 
    if len(e.split()) <= 3: return e
    elems = []
    if "(" in e: 
        elems = splitByParen(e)
        for i in range(len(elems)): 
            if "(" in elems[i]: 
                elems[i] = "(" + addOrderParens(elems[i][1:-1]) + ")"   

    else: elems = e.split()
    i = 0
    while(i < len(elems)): 
        elems.insert(0, "(")
        i += 2
        elems.insert(i, ")")
        i += 2

    return "".join(elems)


def splitByParen(l): 
    result = []
    i = 0
    while(i < len(l)): 
        start = l.find("(", i)

        if start == -1:  #end doesn't have ()
            result += l[i:].split() 
            break 

        end = start + getEndingParan(l[start:])
        if start > i: 
            result += l[i:start].split() 
    
        result.append(l[start: end + 1])

        i = end + 1

    return result 

def getEndingParan(l): 
    brackets = []
    for i, e in enumerate(l): 
        if e not in "()": continue 
        elif e == ")" and brackets[-1] == "(": 
            brackets = brackets[:-1]
        else: 
            brackets.append(e)
        if not brackets: 
            return i

    return len(l) - 1 



if __name__ == "__main__":
    main()
