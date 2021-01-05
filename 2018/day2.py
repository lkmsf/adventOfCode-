import collections as c
import itertools as i  

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close() 
    a2, a3 = 0, 0

    for e in inp:
       freq  = c.Counter(e).values() 
       if(2 in freq): 
           a2 += 1
       if(3 in freq):
           a3 += 1

    print(a2 * a3) 
   
    for e, f in i.combinations(inp, 2): 
        #same  = [c1 == c2 for c1, c2 in zip(e, f)]
        s = [i for i,j in zip(e,f) if i == j]
        if sum( same) == len(e) - 1: 
            print(''.join(s))
            break
    print("done" )

def differByOne(e, f): 
    diffs = 0
    di = 0
    for idx, (c1, c2) in enumerate(zip(e,f)): 
        if c2 != c1: 
            diffs += 1
            di = idx
    if  diffs == 1: 
        print(e, f, e[:di] + e[di + 1:])
        return True 
    else: 
        return False 

def ltrappear(s, i): 
    for c in s: 
        if s.count(c) == i: 
            return True 
    return False 

if __name__ == "__main__":
    main()
