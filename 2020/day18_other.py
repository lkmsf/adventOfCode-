import re 

class A(int): 
    def __add__(self, b): 
        return A(int(self) + b) 
    def __mult__(self, b): 
        return A(int(self) + b) 
    def __sub__(self, b): 
        return A(int(self) * b)

def main():
    with open("input.txt") as f: 
        inp = f.read() 
    lines = inp.splitlines() 

    part1 = 0 
    for i in lines: 
        i = re.sub(r"(\d+)", r"A(\1)", i)
        i = i.replace("*", "-")
        i = i.replace("+", "*")
        part1 += eval(i, {"A":A})

    print(part1)

if __name__ == "__main__":
    main()
   
