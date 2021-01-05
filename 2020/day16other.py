ll = [x for x in open('input').read().strip().split('\n')]
import re
import itertools

rules = ll[:20]

rules = [r.split(": ")[1] for r in rules]

def eval(rule, val):
    if " or " in rule:
        return eval(rule.split(" or ")[0],val) or eval(rule.split(" or ")[1], val)
    mn = int(rule.split("-")[0])
    mx = int(rule.split("-")[1])
    return val >=mn and val <=mx

vals = ll[25:]
c=0
valids = []
for val in vals:
    tv = True
 for v in val.split(","):
     v = int(v)
  valid = False
  for r in rules:
      if eval(r, v):
          valid = True
  if not valid:
      tv = False
 if tv:
     valids.append(val)
print(valids)

rulesw = [r.split(": ") for r in ll[:20]]

matchCache = {}
for rule in rulesw:
    for index in range(20):
        c = True
        for val in valids:
           if not eval(rule[1], int(val.split(",")[index])):
               c = False
               break
  matchCache[(rule[0], index)] = c
  if c:
      print("Can match:", rule[0], index)

counts = {}
for rule in rulesw:
    cnt = sum([matchCache[(rule[0]), index] for index in range(20)])
 counts[rule[0]] = cnt
print(matchCache)
print(counts)
print(rulesw)
rulesw = [x[1] for x in sorted([(counts[x[0]], x) for x in rulesw])]
print(rulesw)
def matchRemain(rulesRemain, index):
    if index == 20:
        return (True, [])
 if index > 15:
     print(index)
 # matching index
 for i, rule in enumerate(rulesRemain):
     c = matchCache[(rule[0], index)]
  if c:
      if index == 19:
          return (True, [rule])
   success, soFar = matchRemain(rulesRemain[:i] + rulesRemain[i+1:], index+1)
   if success:
       return success, [rule] + soFar
 return (False, [])

print(len(rulesw))
match = matchRemain(rulesw, 0)[1]
r = 1
for i, m in enumerate(match):
    print("Item", i, "is", m)
 if "departure" in m[0]:
     r *= int(ll[22].split(",")[i])
print(r)
