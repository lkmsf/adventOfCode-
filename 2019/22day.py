import numpy as np
from collections import namedtuple

NUM_CARDS = 10#119315717514047
def main(): 
	file = open("22input.txt", "r")
	instructions = file.readlines()
	file.close()

	cards = [x for x in range(NUM_CARDS)]
	breakpoint()
	for i in range(NUM_CARDS):
		for i in instructions:
			if i[:4] == "deal":
				if i[5:9] == "into": cards = dealIntoNewStack(cards)
				elif i[5:9] == "with": cards = dealWInc(int(i[20:]), cards)
				else: print("problem")
			else: cards = cut(int(i[4:]), cards)

		if 1% 1000 == 0: print(i)
		#print(cards)

	#print(cards[2020])

def dealIntoNewStack(cards):
	#print("deal into new stack")
	return cards[-1::-1]#

def dealWInc(inc, cards):
	#print("deal w inc", inc)
	temp = [0 for __ in range(NUM_CARDS)]

	j = 0
	for i in cards: 
		#print("j =", j, "i =", i)
		temp[j] = i
		j = j + inc 
		while j >= NUM_CARDS:
			j = j % NUM_CARDS

	return temp 

	

def cut(amt, cards):
	#print("cut", amt)
	return cards[amt:] + cards[:amt]
	# if amt > 0: 
		
	# elif amt < 0:
	# 	return cards[amt:] + cards[:amt] 
	


# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()