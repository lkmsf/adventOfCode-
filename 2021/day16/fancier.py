from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()

def popValues(s, length, r):
    r["len"] += length
    result = s[:length]
    for i in range(length): s.pop(0)
    return result

def getInt(l, base):
    return int("".join(l), base)

def parseLiteral(s, r):
    num = []
    ind = 1
    while ind:
        ind, data = getInt(popValues(s, 1, r), 2), popValues(s, 4, r)
        num += data
    r["D"] = getInt(num, 2)

    return s, r

def parseOperator(s, r):
    lenTypeID = getInt(popValues(s, 1, r), 2)

    if lenTypeID == 0:
        # length is a 15 bit number
        lenInside = getInt(popValues(s, 15, r), 2) 

        r["values"] = []
        len = lenInside 
        while len:
            if len < 0: raise ValueError("ParseOp: len is negative")
            s, currR = parsePacket(s)
            r["len"] += currR["len"]
            r["values"].append(currR)
            len -= currR["len"]

    elif lenTypeID == 1:
        numPackets = getInt(popValues(s, 11, r), 2)

        r["values"] = []
        for i in range(numPackets):
            s, currR = parsePacket(s) 
            r["len"] += currR["len"]
            r["values"].append(currR)

    else: raise ValueError("ParseOp - lenTypeId unexpected value")

    return s, r


def parsePacket(s):
    r = {"len": 0}
    r["V"] = getInt(popValues(s, 3, r), 2) 
    r["T"] = getInt(popValues(s, 3, r), 2)

    if r["T"] == 4:
        s, r = parseLiteral(s, r)
    else:
        s, r = parseOperator(s, r)

    return s, r


def countVersion(packets):
    if "values" not in packets:
        return packets["V"]
    else:
        return packets["V"] + sum(countVersion(X) for X in packets["values"])

def evalPackets(packets):
    if "values" not in packets:
        return packets["D"]

    vals = list(map(evalPackets, packets["values"])) 

    operations = [sum, math.prod, min, max, 4 , lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1]]

    return operations[packets["T"]](vals)


hexToBin = {
    "0" : "0000", 
    "1" : "0001", 
    "2" : "0010", 
    "3" : "0011", 
    "4" : "0100", 
    "5" : "0101", 
    "6" : "0110", 
    "7" : "0111", 
    "8" : "1000", 
    "9" : "1001", 
    "A" : "1010", 
    "B" : "1011", 
    "C" : "1100", 
    "D" : "1101", 
    "E" : "1110", 
    "F" : "1111", 
}
toBin = list("".join(hexToBin[x] for x in inp))

s, packets = parsePacket(list(toBin))
print(countVersion(packets))
print(evalPackets(packets))