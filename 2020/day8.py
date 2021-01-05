def main():
   f = open("input.txt")
   inp = f.read().splitlines()
   inp = [x.split() for x in inp]
   f.close()

   for e in inp: 
       if e[0] == "nop": 
           e[0] = "jmp"
           if(tryInp(inp)): 
               return 
           e[0] = "nop" 
       elif e[0] == "jmp": 
           e[0] = "nop"
           if(tryInp(inp)): 
               return 
           e[0] = "jmp" 
   print("end" )


def tryInp(inp): 
   acc = 0
   alreadyRan = set()  
   i = 0
   while True: 
       if i >= len(inp): 
          break  
       if i in alreadyRan: 
          return False 
       alreadyRan.add(i)
       ins, num  = inp[i]
       if ins == "nop": 
           i += 1
       elif ins == "acc": 
            acc += int(num)
            i += 1
       elif ins  == "jmp": 
            i += int(num)
       else: 
            print("askjldfakjsgd" )

   print(acc)
   return True 

if __name__ == "__main__":
    main()


