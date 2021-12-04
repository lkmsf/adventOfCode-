from collections import Counter, defaultdict
from itertools import combinations, chain 
import re
import sys

def main():
    with open("4.in") as f:
    #with open("test4.in") as f:
        inp = f.read().strip()
        inp = inp.split("\n\n")
        print(len(inp))

    numbers = inp[0].split(",")

    inBoards = [x.splitlines() for x in inp[1:]]

    boards = []
    for val in inBoards:
        boards.append([v.split() for v in val])

    p1 = part1(numbers, boards)
    p2 = part2(numbers, boards)

    print(f"part1: {p1}")
    print(f"part2: {p2}")

    for i, part in enumerate([p1, p2]):
        print(f'bash submit.sh {i+1} {part}')

def markNumbers(boards, num):
    for iB, board in enumerate(boards):
        for iR, row in enumerate(board):
            for iV, val in enumerate(row):
                if val == num:
                    boards[iB][iR][iV] = "X"



def checkForWin(board):
    for row in board:
        numInRow = sum(v == "X" for v in row)
        if numInRow == len(row):
            return True

    for i in range(len(board[0])):
        numInCol = sum(row[i] == "X" for row in board)
        if numInCol == len(board[0]):
            return True

    return False


def checkAllBoards(boards):
    winners = [] 
    for i, b in enumerate(boards):
        if checkForWin(b):
            winners.append(i)

    return winners


def playGame(numbers, boards):
    for n in numbers:
        markNumbers(boards, n)
        winner = checkAllBoards(boards)

        if winner != []:
            return winner[0], n

def part1(numbers, boards):
    winnerIndex, winningNum = playGame(numbers, boards)

    winner = boards[winnerIndex]
    winnnerSum = 0
    for row in winner:
        for val in row:
            if val != "X":
                winnnerSum += int(val)

    return winnnerSum * int(winningNum)

def part2(numbers, boards):
    winner, winningNum = playGameLast(numbers, boards)

    winnnerSum = 0
    for row in winner:
        for val in row:
            if val != "X":
                winnnerSum += int(val)

    return winnnerSum * int(winningNum)
    
    
def playGameLast(numbers, boards):
    for i, n in enumerate(numbers):
        print(len(boards), n)
        markNumbers(boards, n)

        winners = checkAllBoards(boards)
        
        if len(boards) == 1 and winners == [0]:
            return boards[0], int(n)

        boards = [b for i, b in enumerate(boards) if i not in winners]





if __name__ == "__main__":
    main()