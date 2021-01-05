from collections import Counter, defaultdict
from itertools import combinations

def main():
   f = open("input.txt")
   #f = open("ex.txt")
   inp = f.read().splitlines() 
   f.close()

   claims = []
   for i in inp: 
       iD, _,loc , dim = i.split() 
       w, h = dim.split("x")
       fL, fT = loc.split(",")
       claims.append([ iD, int(fL), int(fT[:-1]) , int(w), int(h)]) 

   lookedAt = defaultdict(set) 
   ids = defaultdict(set)
   for e in claims:
       idN, fL, fT, w, h = e
       for wi  in range(w): 
           for hi  in range(h): 
               curr = (fL + wi, fT + hi)
               lookedAt[curr].add(idN)
               ids[idN].add(curr)


   print(sum([1 for i in lookedAt if len(lookedAt[i]) >= 2]))
   onlyOnce = set(([i for i in lookedAt if len(lookedAt[i]) ==  1])) 
   for i in ids: 
       if all([e in onlyOnce for e in ids[i]]): 
           print(i)




if __name__ == "__main__":
    main()
