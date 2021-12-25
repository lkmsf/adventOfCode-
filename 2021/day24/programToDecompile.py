with open("test.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines()

inp = [a.split() for a in inp]

instr = []

s = "abc"
i = 0

# def setVar(vars, var, val):
#     vars[varNames.index(var)] = val

# def getVal(vars, var):
#     return vars[varNames.index(var)]

# varNames = "wxyz"
# vars = [0] * 4

for l in inp:  
    if l[0] == "inp":
        instr.append(l[1] + " = " + s[i]) 
        i += 1
        continue
        
    ops = {"add": "+", "sub": "-", "mod": "%", "div": "/", "eql": "==", "mul": "*"}
    op = ops[l[0]]

    instr.append(l[1] + " " + op + "= " + l[2])


for i in instr:
    print(i)

