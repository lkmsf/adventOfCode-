
def main():
    inputFile = "input-day1.txt" 
    with open(inputFile) as f: 
        nums = f.read().splitlines() 
        nums = [int(n) for n in nums]

        for i, num1 in enumerate(nums): 
            for j, num2 in enumerate(nums): 
                for k, num3 in enumerate(nums): 
                    if (i == j or j == k or i == k): continue 
                    if num1 + num2 + num3 == 2020: 
                        print(num1, num2, num3 ) 
                        print(num1 * num2 * num3) 
                        return  

if __name__ == "__main__":
    main()
