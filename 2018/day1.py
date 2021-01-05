def main():
    inp = open("i").read().splitlines() 
    s = 0
    reached = set()
    ind = 0
    print(sum(int(n) for n in inp)) 
    
    while(True): 
        i = inp[ind]
        if s in reached:
            break 
        reached.add(s) 
        s += int(i[1:]) if i[0] == "+" else -int(i[1:]) 
        ind += 1
        ind %= len(inp)
    print(s)

if __name__ == "__main__":
    main()
