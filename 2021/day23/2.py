from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

energyCosts = {"A": 1, "B": 10, "C": 100, "D": 1000}

#loc = [["A", "B"], ["D", "C"], ["C", "B"], ["A", "D"]]
#loc = [["A", "A"], ["B", "C"], ["C", "B"], ["D", "D"]]
loc = [["D", "D"], ["A", "A"], ["B", "C"], ["B", "C"]]

addIn = [["D", "D"], ["B", "C"], ["A", "B"], ["C", "A"]]

loc = [[a[0], b[0], b[1], a[1]] for a, b in zip(loc, addIn)]

NUM_IN_SLOT = 4

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

hallway = ["", "", "a", "", "b", "", "c", "", "d", "", ""]

def everyoneHome(slots):
    for line, shouldBe in zip(slots, "ABCD"):
        if not len(line) == NUM_IN_SLOT or not all(x == shouldBe for x in line):
            return False
    return True

def canMoveThroughHallway(hi, goalI, hallway):
    startI, endI = min(hi, goalI), max(hi, goalI)

    hallwayBetween = hallway[startI + 1: endI]
    return not any([x and x in "ABCD" for x in hallwayBetween])


def canMoveHome(i, slots, hallway):
    """
    >>> slots = [['AB'], ['DD'], ['C'], []]
    >>> hallway = ["", "A", "a", "", "b", "", "c", "", "d", "", ""] 
    >>> canMoveHome(1, slots, hallway)
    False
    >>> hallway = ["", "C", "a", "", "b", "", "c", "", "d", "", ""] 
    >>> canMoveHome(1, slots, hallway)
    True
    >>> hallway = ["", "", "a", "", "b", "", "c", "", "d", "", "D"] 
    >>> canMoveHome(10, slots, hallway)
    True
    >>> hallway = ["", "", "a", "C", "b", "C", "c", "", "d", "", "D"] 
    >>> canMoveHome(3, slots, hallway)
    False
    """
    c = hallway[i]

    # 1) do we have a slot to go to?
    moveTo =  slots["ABCD".index(c)]
    if not all(x == c or x == "" for x in moveTo):
        return False

    # 2) can we get to that slot?
    return canMoveThroughHallway(i, hallway.index(c.lower()), hallway)

def getCostSlotHallway(c, hi, si, slots, hallway):
    """
    >>> slots = [['A'], [], ['C'], []]
    >>> hallway = ["B", "A", "a", "", "b", "D", "c", "", "d", "C", "C"] 
    >>> getCostSlotHallway("A", 1, 0, slots, hallway)
    2
    >>> getCostSlotHallway("D", 5, 3, slots, hallway)
    5000
    >>> getCostSlotHallway("B", 0, 1, slots, hallway)
    60
    >>> getCostSlotHallway("C", 10, 2, slots, hallway)
    500
    """
    hallwayMoves = abs(hi - hallway.index("abcd"[si]))
    toSlotMove = abs(NUM_IN_SLOT - len(slots[si]))
    return (hallwayMoves + toSlotMove) * energyCosts[c]

def solve(slots, hallway, mem):
    """
    >>> slots = [["A", "A"], ["B", "C"], ["C", "B"], ["D", "D"]]
    >>> hallway = ["", "", "a", "", "b", "", "c", "", "d", "", ""] 
    >>> solve(slots, hallway, {})
    460
    >>> slots = [["A", "A"], ["B"], ["C", "C"], ["D", "D"]]
    >>> hallway = ["", "", "a", "", "b", "B", "c", "", "d", "", ""] 
    >>> solve(slots, hallway, {})
    20
    >>> slots = [["A", "A"], ["B"], ["C", "C"], ["D", "D"]]
    >>> hallway = ["", "", "a", "B", "b", "", "c", "", "d", "", ""] 
    >>> solve(slots, hallway, {})
    20
    """
    key = (tuple(tuple(x) for x in slots), tuple(hallway))
    if everyoneHome(slots):
        return 0
    if key in mem:
        return mem[key]

    # see if anyone in the hallway can move home
    # .  if they can - there is never a time we don't want to do that
    for i, c in enumerate(hallway):
        if c and c in "ABCD" and canMoveHome(i, slots, hallway):
            cost = getCostSlotHallway(c, i, "ABCD".index(c), slots, hallway)
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

    # if hallway is full after trying to return everyone -> return false
    if all(x != "" for x in hallway):
        return None

    possibleCosts = []

    # now try moving top of each slot somewhere in hallway
    for si, c in enumerate(slots):
        if not c: continue 
        c = c[-1]
        if si == "ABCD".index(c) and all(x == c or x == "" for x in slots[si]): continue
        for hi,v in enumerate(hallway):
            if v: continue #location is full

            if not canMoveThroughHallway(hallway.index("abcd"[si]), hi, hallway): continue

            slots[si].pop()
            hallway[hi] = c

            cost = getCostSlotHallway(c, hi, si, slots, hallway)

            if not possibleCosts or cost < min(possibleCosts): 
                result = solve(slots, hallway, mem)
                if result is not None:
                    possibleCosts.append(cost + result)

            slots[si].append(c)
            hallway[hi] = ""

    result = min(possibleCosts) if possibleCosts else None
    mem[key] = result
    return result


print(solve(loc, hallway, dict()))
# import doctest
# doctest.testmod()