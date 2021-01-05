def main():
    inp  = open('input.txt').read().splitlines() 
  
    result = 1
    for m in [1, 3, 5, 7, 0.5]: 
        numTrees = 0 
        currX = 0 
        for e in inp: 
            if currX % 1 == 0: 
                if e[int(currX)] == "#": 
                    numTrees += 1
            currX += m 
            currX %= len(e)  

        print(numTrees) 
        result *= numTrees

    print(result) 


if __name__ == "__main__":
    main()
