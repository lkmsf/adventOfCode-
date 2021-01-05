
def main():
    pswds = open('day2_input.txt').read().splitlines() 
    validCount = 0
    for p in pswds: 
        curr = p.split('-') 
        minLtr = int(curr[0]) 
        curr = curr[1].split() 
        maxLtr = int(curr[0]) 
        ltr = curr[1][0]
        wd = curr[2].strip() 

        #isValid? 
        firstContains = wd[minLtr - 1] == ltr 
        secondContains = wd[maxLtr - 1] == ltr 
        if(firstContains + secondContains == 1): 
            validCount += 1

    print(validCount) 



if __name__ == "__main__":
    main()
