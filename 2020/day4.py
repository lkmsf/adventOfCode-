def main():
    inp  = open('input.txt').read().split('\n\n') 
    
    valid = 0

    for i in inp: 
        #fill in dict 
        curr = dict() 
        for l in i.splitlines(): 
            for pair in l.split(): 
                key, val = pair.split(':')
                curr[key] = val 
        
        if(validP(curr)): 
            valid += 1 

    print(valid) 

def withinRange(d, key, low, high): 
    if key not in d: 
        return False 
    c = int(d[key] ) 
    return withinRangeNoB(c, low, high) 

def withinRangeNoB(c, low, high): 
    return not ( c < low or c > high) 

    
def validP(d): 
    if not withinRange(d, 'byr', 1920, 2002): 
        return False 
    if not withinRange(d, 'iyr', 2010, 2020): 
        return False 
    if not withinRange(d, 'eyr', 2020, 2030): 
        return False 
    if not withinRange(d, 'iyr', 2010, 2020): 
        return False 

    if not 'hgt' in d: 
        return False 
    curr  = d['hgt']  
    c = curr[:-2]
    t = curr[-2:]
    
    c = int(c) 
    if t == 'cm': 
        if not withinRangeNoB(c, 150, 193): 
            return False 
    elif t == 'in': 
        if not withinRangeNoB(c, 59, 76): 
            return False 
    else: 
        return False  

    if not 'hcl' in d: 
        return False 
    c = d['hcl'] 
    if c[0] != '#': 
        return False 
    for ch in c[1:]: 
        if not ch.isalnum(): 
            return False 

    if not 'ecl' in d: 
        return False 
    c = d['ecl'] 
    if c not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: 
        return False 

    if not 'pid' in d: 
        return False 
    c = (d['pid'] ) 
    if len(c) != 9: 
        return False 
    c = int(c) 

    return True 





if __name__ == "__main__":
    main()
