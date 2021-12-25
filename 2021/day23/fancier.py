from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

energyCosts = {"A": 1, "B": 10, "C": 100, "D": 1000}

#slots = [["A", "B"], ["D", "C"], ["C", "B"], ["A", "D"]]
#slots = [["A", "A"], ["B", "C"], ["C", "B"], ["D", "D"]]
slots = [["D", "D"], ["A", "A"], ["B", "C"], ["B", "C"]]

addIn = [["D", "D"], ["B", "C"], ["A", "B"], ["C", "A"]]

slots = [[a[0], b[0], b[1], a[1]] for a, b in zip(slots, addIn)]
NUM_IN_SLOT = 4

# .   basically the one close to surface is in last index (stack)
# slots = [["A", "D", "D", "B"], ["D", "B", "C", "C"], ....]
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

# these are loc along top - lowercase letters mark slot location
hallway = ["", "", "a", "", "b", "", "c", "", "d", "", ""]

# we're done - we returned everyone to their slot
def everyoneHome(slots):
    for line, shouldBe in zip(slots, "ABCD"):
        if not len(line) == NUM_IN_SLOT or not all(x == shouldBe for x in line):
            return False
    return True

# Can I get from hi index in hallway to my goalI index - nothing is in my way
def canMoveThroughHallway(hi, goalI, hallway):
    startI, endI = min(hi, goalI), max(hi, goalI)

    hallwayBetween = hallway[startI + 1: endI]
    return not any([x and x in "ABCD" for x in hallwayBetween])

# Can the char at index i in the hallway get to it's home slot?
def canMoveHome(i, slots, hallway):
    c = hallway[i]

    # 1) do we have a slot to go to?
    moveTo =  slots["ABCD".index(c)]
    if not all(x == c or x == "" for x in moveTo):
        return False

    # 2) can we get to that slot?
    return canMoveThroughHallway(i, hallway.index(c.lower()), hallway)

# what is the cost from our slot (given by slot index si) to the hi (hallway index) location
#     assumes it is possible
def slotToHallwayLocCost(c, hi, si, slots, hallway):
    hallwayMoves = abs(hi - hallway.index("abcd"[si]))
    toSlotMove = abs(NUM_IN_SLOT - len(slots[si]))
    return (hallwayMoves + toSlotMove) * energyCosts[c]

# return the minimum energy cost to return everyone home
# .  Recursive insight - every element has two moves 
#       (1) to some hallway location
#       (2) to their home slot
def solve(slots, hallway, mem):
    key = (tuple(tuple(x) for x in slots), tuple(hallway))
    if everyoneHome(slots):
        return 0
    if key in mem:
        return mem[key]

    # see if anyone in the hallway can move home
    # .  if they can - there is never a time we don't want to do that
    for i, c in enumerate(hallway):
        if c and c in "ABCD" and canMoveHome(i, slots, hallway):
            cost = slotToHallwayLocCost(c, i, "ABCD".index(c), slots, hallway)
            hallway[i] = ""
            slots["ABCD".index(c)].append(c)
            result = solve(slots, hallway, mem)

            if result is not None:
                result = cost + result
                mem[key] = result
                slots["ABCD".index(c)].pop()
                hallway[i] = c
                return result

            slots["ABCD".index(c)].pop()
            hallway[i] = c

    possibleCosts = []

    # now try moving top of each slot somewhere in hallway
    for si, currSlotVals in enumerate(slots):

        # get the top value if it exists
        if not currSlotVals: continue 
        c = currSlotVals[-1]

        # Don't remove an element already in its correct location
        if si == "ABCD".index(c) and all(x == c or x == "" for x in slots[si]): continue

        # now try moving that element to every possible in the hallway
        for hi,v in enumerate(hallway):
            if v: continue #location is full

            if not canMoveThroughHallway(hallway.index("abcd"[si]), hi, hallway): continue

            slots[si].pop()
            hallway[hi] = c

            cost = slotToHallwayLocCost(c, hi, si, slots, hallway)

            if not possibleCosts or cost < min(possibleCosts):  #this could still be a good option
                result = solve(slots, hallway, mem)
                if result is not None:
                    possibleCosts.append(cost + result)

            slots[si].append(c)
            hallway[hi] = ""

    result = min(possibleCosts) if possibleCosts else None
    mem[key] = result
    return result


print(solve(slots, hallway, dict()))