#import functools as f 

#l = [__import__('functools').reduce(lambda a,b: a<<1 | (b in "BR"),  e[:-1], 0) for e in open('input.txt').readlines()]
#
#x, n = max(l), min(l) 
#print((x * (x + 1) / 2 - n * (n - 1) / 2) - sum(l))

#l = [f.reduce(lambda a,b:a<<1|(b in"BR"),e,0) for e in open('input.txt').read().split('\n')[:-1]]           
#l=[__import__('functools').reduce(lambda a,b:a<<1|(b in"BR"),e[:-1],0)for e in open('input.txt').readlines()]
#x,n=max(l),min(l) 
#print((x*(x + 1) /2-n*(n-1)/2)-sum(l))


#x,*l,n= [__import__('functools').reduce(lambda a,b:a<<1|(b in"BR"),e[:-1],0)for e in open('input.txt').readlines()])
##x,n=max(l),min(l) 
#print((x*(x + 1) /2-n*(n-1)/2)-sum(l))

#s=set([__import__('functools').reduce(lambda a,b:a<<1|(b in'BR'),e[:-1],0)for e in open('input.txt').readlines()]);print(s-set(range(min(s),max(s)))) 

        
#s=set([int('0b'+e.maketrans('FBLR', '0101'))for e in open('input.txt').readlines()])
#print(s-set(range(min(s),max(s)))) 

