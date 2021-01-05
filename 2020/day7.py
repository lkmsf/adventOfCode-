def main():
    inp  = open('input.txt').read().splitlines() 

    rules = dict() 
    for e in inp: 
        color = e.split(" bags ")[0]
        rest = e.split("contain ")[1][:-1].split(",")
        bags = [(x.split()[0], x.strip()[1:-4].strip()) for x in rest]
        
        if e.find("no other bags") != -1:  
            bags = []
        rules[color] = bags 

    result = 0
#    for i in rules.keys(): 
#        if canHold(i, rules): 
#            result += 1
#
    #print(result)

    print(numBagsIn(("1", "shiny gold"), rules)) 

def numBagsIn(c, d): 
    print(c, d[c[1]])
    if d[c[1]] == []:
        return 0
    s = 0 
    for i in d[c[1]]: 
        s +=  int(i[0]) * (numBagsIn(i, d) +1) 
    return s 

def canHold(i, d ): 
    #if i not in d: return False 
    if "shiny gold" in d[i[1]]:
        return True 
    for j in d[i[1]]: 
        if canHold(j, d): 
            return True 

    return False 
        



if __name__ == "__main__":
    main()
