#import functools as f 
def main():
    inp  = open('i').read().split('\n\n')
    count = 0 

    for g in inp:  
        total = set(g) 
        for i in g.split():  
            q = set(i)
            total &= q
        count += len(total) 

    print(count) 

def betterMain(): 
    inp  = open('i').read().split('\n\n')
    count = 0 

    for g in inp:  
        p = 
        for i in g.split():  
            q = set(i)
            total &= q
        count += len(total) 
    print(count) 


if __name__ == "__main__":
    main()

    print(sum(len(__import__('functools').reduce(lambda a,b:a&set(b),g.split(),set(g))) for g in open('i').read().split('\n\n'))) 

    print(sum(len(set.intersection(*[set(x) for x in l.split()])) for l in open('i').read().split('\n\n')))
    #print(sum(len(__import__('functools').reduce(lambda a,b:a&set(b),g.split(),set(g))) for g in open('i').read().split('\n\n'))) 
    #print(sum(f.reduce(lambda a,b: a&b, i, set(i)) for i in (g.split() for g in open("input.txt").read().split('\n\n'))))
