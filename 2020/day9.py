from collections import Counter 
from itertools import combinations

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    inp = [int(x) for x in inp]
    f.close()

    for i, e in enumerate(inp):
        if i < 25: continue 
        if not sumOfPrev(i, inp): 
            num = e  

    for i in range(len(inp)): 
        for j in range(i + 1, len(inp) - 1):
            #if(i == 2 and j == 5 ): 
            s =  inp[i: j + 1]
            if sum(s) == num: 
                print(min(s) + max(s))
                return  

def sumOfPrev(idx, inp): 
    for i, j in combinations(range(idx - 25, idx), 2): 
        if i == j : continue 
        if inp[i] + inp[j] == inp[idx]:
            return True 
    return False 


if __name__ == "__main__":
    main()


