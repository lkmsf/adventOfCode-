import re, numpy

V = lambda *a: numpy.array(a)
key = lambda a: tuple(a[0]+a[1]) + tuple(a[1])
prune = lambda x: sorted({key(x):x for x in x}.values(), key=key)[-1000:]

def parse(line):
    i,a,b,c,d,e,f = map(int, re.findall(r'\d+',line))
    return (i, (V(0,0,0,a), V(0,0,0,1)),    # Cost and production
               (V(0,0,0,b), V(0,0,1,0)),    # of each robot type,
               (V(0,0,d,c), V(0,1,0,0)),    # in the order geode,
               (V(0,f,0,e), V(1,0,0,0)),    # obs, clay, and ore.
               (V(0,0,0,0), V(0,0,0,0)))    # Construct no robot.

def run(blueprint, t):
    todo = [(V(0,0,0,0), V(0,0,0,1))]       # What we have and make.
    for t_ in range(t,0,-1):
        todo_ = list()                      # Queue for the next minute.
        for have, make in todo:
            for cost, more in blueprint:
                if all(cost <= have):       # We can afford this robot.
                    todo_.append((have+make-cost, make+more))
        todo = prune(todo_)                 # Prune the search queue.
    return max(have[0] for have, _ in todo)

vals = []
for i, *blueprint in map(parse, open("data.in")):
    curr = run(blueprint, 24) 
    vals.append(curr * i)

print(vals)