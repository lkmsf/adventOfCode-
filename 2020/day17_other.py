from collections import Counter

def main(dims):

    neighbors = [()]
    for x in range(dims):
        neighbors = [x + (i,) for i in [-1, 0, 1] for x in neighbors]
    neighbors.remove(dims * (0,))

    state = set((dims - 2) * (0,) + (i, j) for i, v in enumerate(open('input.txt').read().splitlines()) for j, v in enumerate(v) if v == '#')

    for i in range(6):
        state = set(pos for pos, cnt in Counter(tuple(map(sum, zip(pos, n))) for pos in state for n in neighbors).items() if cnt == 3 or pos in state and cnt == 2)
    
                

    print(len(state))

main(dims=3)
#main(dims=4)
