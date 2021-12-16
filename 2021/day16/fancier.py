from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import statistics
import math
import sys

inputFile = "test.in" if len(sys.argv) > 1 else "data.in"

with open(inputFile) as f:
    inp = f.read().strip()

# simulate pass by ref by putting it into a one element list
def popValues(s, length, r):
    r["len"] += length
    result = s[0][:length]
    s[0] = s[0][length:]
    return result

def parseLiteral(s, r):
    num = ""
    ind = 1
    while ind:
        ind, data = int(popValues(s, 1, r), 2), popValues(s, 4, r)
        num += data
    r["D"] = int(num, 2)

    return r

def parseOperator(s, r):
    lenTypeID = int(popValues(s, 1, r), 2)

    if lenTypeID == 0:
        # length is a 15 bit number
        lenInside = int(popValues(s, 15, r), 2) 

        r["values"] = []
        len = lenInside 
        while len:
            currR = parsePacket(s)
            r["len"] += currR["len"]
            r["values"].append(currR)
            len -= currR["len"]

    elif lenTypeID == 1:
        numPackets = int(popValues(s, 11, r), 2)

        r["values"] = []
        for i in range(numPackets):
            currR = parsePacket(s) 
            r["len"] += currR["len"]
            r["values"].append(currR)

    return r

def parsePacket(s):
    r = {"len": 0}
    r["V"] = int(popValues(s, 3, r), 2) 
    r["T"] = int(popValues(s, 3, r), 2)

    r = parseLiteral(s, r) if r["T"] == 4 else parseOperator(s, r)

    return r

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

# convert from hex to bin
start = bin(int(inp, 16))[2:]
toBin = start.zfill(math.ceil(len(start) / 4) * 4)

# get all the packets then analyze
packets = parsePacket([toBin])
print(countVersion(packets))
print(evalPackets(packets))