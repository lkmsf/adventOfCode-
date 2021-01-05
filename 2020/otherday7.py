ll = [x for x in open('input').read().strip().split('\n')]
import re

ctc = {}
for line in ll:
    #print(line)
     color = line.split(" contain ")[0]
     contains = line.split(" contain ")[1].split(".")[0].split(", ")
 #print(color, contains)
 if contains == ["no other bags"]:
     ctc[color] = []
 else:
     c = []
  for contain in contains:
      quantity = contain.split(" ")[0]
   contain = contain[len(quantity)+1:]
   if contain[-1]!='s':
       #print(contain)
    contain+='s'
   quantity = int(quantity)
   c.append((contain, quantity))
  ctc[color] = c


def even(color):
    if color == "shiny gold bags":
        return True
 for contain in ctc[color]:
     if even(contain[0]):
         return True
 return False

cnt=0
for color in ctc.keys():
    if even(color):
        cnt+=1
print(cnt-1)

def cnt(color):
    s=0
 for contain in ctc[color]:
     s+=contain[1]*(1+cnt(contain[0]))
 return s
print(cnt("shiny gold bags"))

#andrew 
def main():
    st_rules  = open('7_input.txt').read().split('\n')
 #print(st_rules)
 rules = {}
 nums = {}
 for st_rule in st_rules:
     bagin = st_rule.split(' contain ')[0][:-5]
  bagsoutfull = st_rule.split(' contain ')[1].split(", ")
  bagsout = [' '.join(bagout.split(' ')[1:-1]) for bagout in bagsoutfull]
  lookup = [[' '.join(bagout.split(' ')[1:-1]), hack(bagout.split(' ')[0])] for bagout in bagsoutfull]
#  print(str(bagin) + " " + str(bagsout))
  rules[bagin] = bagsout
  nums[bagin] = lookup
 #print(rules)
 #print(nums)
 count = 0
 for st_rule in st_rules:
     testbag = ' '.join(st_rule.split(' ')[0:2])
  if fitinbag(testbag, rules):
      count += 1
 #print(count)
 print(bagsinbag('shiny gold', nums) - 1)


def fitinbag(bag, rules):
    dbag = 'shiny gold'
 if dbag in rules[bag]:
     return True
 else:
     if 'other' in rules[bag]:
         return False
  for newbag in rules[bag]:
      if fitinbag(newbag, rules):
          return True
  return False
def hack(num):
    if(num == 'no'):
        return 0
 else:
     return int(num)

def bagsinbag(bag, nums):
    bagcount = 1

 if "other" in str(nums[bag]):
     print(str(nums[bag]) + " " + str(bagcount))
  return 1

 for newbag in nums[bag]:
     bagcount += newbag[1] * bagsinbag(newbag[0], nums)
 print(str(nums[bag]) + " " + str(bagcount))
 return bagcount

if __name__ == "__main__":
    main())

print((lambda r: r(r, "shiny gold bags"))(lambda selfRef, color: sum(contain[1]*(1+selfRef(selfRef, contain[0])) for contain in ctc[color])))

