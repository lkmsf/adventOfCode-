
with open("data.in") as f:
    inp = f.read().strip()
    inp = inp.splitlines()

inp = [a.split() for a in inp]

for i, line in enumerate(inp):
    if line[0] == "mod":
        print(inp[i+12][2], end = ", ")
        assert(inp[i + 12][0] == "add")


