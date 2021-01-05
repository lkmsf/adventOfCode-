from collections import Counter, defaultdict
from itertools import combinations

def main():
    f = open("input.txt")
    #f = open("ex.txt")
    inp = f.read().split("\n\n")
    f.close()
    
    rules, my, nearby = inp
    fieldsInOrder = [] 
    rulesD =  {}
    for i in rules.splitlines(): 
        key, value = i.split(":") 
        values = [ x.strip() for x in value.split("or")]
        final  = [[int(v) for v in x.split("-")] for x in values] 
        rulesD[key] = final
        fieldsInOrder.append(key)
    
    nearby = nearby.splitlines()[1:]

    errorRate = 0

    newTickets = []

    for i in nearby: 
        tickets = [int(x) for x in i.split(",")] 
        result = [valid(rulesD, x) for x in tickets]
        if all(result): 
            newTickets.append(tickets) 
        else: 
            errorRate += sum([t for i, t in enumerate(tickets) if not result[i]])


    print(errorRate)
    
    #part 2 

    fields = []
    for i in range(len(newTickets[0])):
        validFieldsForI= []
        for ticket in newTickets: 

            n = ticket[i]
            currValids = set() 

            for key, val in rulesD.items(): 
                rule1, rule2 = val 
                if withinRange(*rule1, n) or withinRange(*rule2, n): 
                    currValids.add(key)

            #print(n, currValids)
            validFieldsForI.append(currValids)

        fields.append(set.intersection(*validFieldsForI))

     
    while True:
        oneElems = [x for x in fields if len(x) == 1]
        if len(oneElems) == len(newTickets[0]) : break 
        toRemove = set([next(iter(x)) for x in oneElems]) 
        for elem in fields: 
            if len(elem) == 1: continue 
            elem -= toRemove

    #print(fields) 

    result = 1 
    myTicket = my.split(",")
    for i, elem in enumerate(fields): 
        elem = next(iter(elem))
        if elem.startswith("departure"): 
            result *= int(myTicket[i]) 


    print(result)

def valid(rules, t): 
    return len(getAllValidRules(rules, t)) >  1

def getAllValidRules(rules, t): 
    validRules = []
    for field, rule in rules.items(): 
        rule1, rule2 = rule
        if withinRange(*rule1, t) or withinRange(*rule2, t): 
            validRules.append(field)
    return validRules 

def withinRange(low, high,  n): 
    return   low <= n  <= high

if __name__ == "__main__":
    main()
