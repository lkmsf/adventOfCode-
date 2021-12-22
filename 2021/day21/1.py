from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

#p1, p2 = 4, 8
p1, p2 = 4, 9
s1, s2 = 0, 0 

totalRolls = 0
dice = 1

def roll():
    global dice, totalRolls
    result = dice
    dice = (dice + 1)
    if dice > 100: dice = 1
    totalRolls += 1
    return result

def turn(player):
    move = roll() + roll() + roll() 
    return ((player + move - 1) % 10) + 1

while s1 < 1000 and s2 < 1000:
    p1 = turn(p1) 
    s1 += p1
    if s1 >= 1000: break

    p2 = turn(p2) 
    s2 += p2

print(s1, s2)
loser = s1 if s1 < 1000 else s2
print(loser, totalRolls)
print(loser * totalRolls)
