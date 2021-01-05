from collections import Counter, defaultdict
from itertools import combinations

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().splitlines() 
    f.close()

    currMask = 0  
    currMem = {}

    for e in inp:
        if "mask" in e: 
            currMask = e.split("=")[1].strip() 
            continue 

        first, sec = e.split("=")
        addr = int(first.strip()[4:-1]) 
        val = int(sec.strip()) 
        
        binary = str(bin(val))[2:]
        binary = binary.zfill(len(currMask))
        strMask = str(currMask)
    
        result = "" 
        for i, n in enumerate(strMask): 
            o = binary[i]
            result += o if n == "X" else n
            print("   ", i, o, n, result)

        currMem[addr] = int(result, 2) 


    print(sum(currMem.values())) 

    #part 2
    currMask = 0  
    currMem = {}

    for e in inp:
        if "mask" in e: 
            currMask = e.split("=")[1].strip() 
            continue 

        first, sec = e.split("=")
        addr = int(first.strip()[4:-1]) 
        val = int(sec.strip()) 
        
        binary = str(bin(addr))[2:]
        binary = binary.zfill(len(currMask))
        strMask = str(currMask)
    
        result = "" 
        for i, n in enumerate(strMask): 
            o = binary[i]
            result += o if n == "0" else n
            #print("   ", i, o, n, result)

        addAllPossibilites(currMem, result, val)


    print(sum(currMem.values())) 

def addAllPossibilites(d, key, value): 
    if key.isnumeric(): 
        d[int(key, 2)] = value 
    else: 
        i = key.find("X")
        key = key[:i] + "0"  + key[i+1:]
        addAllPossibilites(d, key, value)
        key = key[:i] + "1"  + key[i+1:]
        addAllPossibilites(d, key, value)

       # for i, c in enumerate(key):  original method 
       #     if c != "X": continue
       #     key = key[:i] + "0"  + key[i+1:]
       #     addAllPossibilites(d, key, value)
       #     key = key[:i] + "1"  + key[i+1:]
       #     addAllPossibilites(d, key, value)
       #     return 


if __name__ == "__main__":
    main()
