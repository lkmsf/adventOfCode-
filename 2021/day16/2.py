from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

# first three bits are header
# 4 - literal value  -> single binary number

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
    r = r.copy()
    num = []
    ind = 1
    while ind:
        ind, data = getInt(popValues(s, 1, r), 2), popValues(s, 4, r)
        num += data

    r["D"] = getInt(num, 2)

    return s, r

def parseOperator(s, r):
    r = r.copy()
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
    # else: raise ValueError("parse packet: don't know this type")

    return s, r


def countVersion(packets):
    if "values" not in packets:
        return packets["V"]
    else:
        return packets["V"] + sum(countVersion(X) for X in packets["values"])

def sumUp(packets):
    if "values" not in packets:
        return packets["D"]
    # if len(packets["values"]) == 1:
    #     return packets["values"][0]["D"]
    if packets["T"] == 4: raise ValueError("type 4 should fall under 2nd base case")
    
    vals = list(map(sumUp, packets["values"])) 

    if packets["T"] == 0: return sum(vals)
    elif packets["T"] == 1: return math.prod(vals)
    elif packets["T"] == 2: return min(vals) 
    elif packets["T"] == 3: return max(vals) 
    elif packets["T"] == 5: 
        if len(vals) != 2: raise ValueError("5 packet not 2 elements")
        return vals[0] > vals[1]
    elif packets["T"] == 6: 
        if len(vals) != 2: raise ValueError("6 packet not 2 elements")
        return vals[0] < vals[1]
    elif packets["T"] == 7: 
        if len(vals) != 2: raise ValueError("7 packet not 2 elements")
        return vals[0] == vals[1]
    else: raise ValueError("packet type that we don't expect")


# exampleLiteral = list("11010001010")
# s2021 = list("110100101111111000101000")
# packW2literals = list("00111000000000000110111101000101001010010001001000000000")
# threePackets = list("11101110000000001101010000001100100000100011000001100000")
# print(parsePacket(threePackets))
#inp = "8A004A801A8002F478"
#inp = "620080001611562C8802118E34"
# inp = "C0015000016115A2E0802F182340"
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
print(toBin)

s, packets = parsePacket(list(toBin))

print(sumUp(packets))