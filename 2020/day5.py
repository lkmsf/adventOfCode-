def main():
    inp  = open('input.txt').read().splitlines() 
    
    highestId = 0 
    seats = set() 
    for e in inp: 
        #e = "FBFBBFFRLR" 
        row = calcR(e[:7]) 
        col = calcC(e[-3:]) 
        #if (((row * 8) + col) > highestId): 
        seatId  = (row * 8) + col

        seats.add(seatId) 

    print(seats)

    
def calcR(s): 
    print(s) 
    start = 0 
    end = 127
    for i in s: 
        if i == 'F': 
            end = ((end - start) // 2 ) + start 
        elif i == 'B': 
            start  = end - ((end - start) // 2 )  

        else: print("problem with rows") 

    print(start, end) 
    return start 

def calcC(s): 
    print(s) 
    start = 0 
    end = 8 
    for i in s: 
        if i == 'L': 
            end = ((end - start) // 2 ) + start 
        elif i == 'R': 
            start  = end - ((-start +  end) // 2 )  

        else: print("problem with col") 

    return start 


if __name__ == "__main__":
    main()
