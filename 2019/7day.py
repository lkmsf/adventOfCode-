import numpy as np
from collections import namedtuple
from intCodeFunctions import readInFile, runProgram, getArray_op
import itertools 

instruction = namedtuple("instruction", ["opCode", "mode1", "mode2", "mode3"])

def main(): 
	inputs = [9,8,7,6,5]
	#getArray_op("1101")
	#puzzle = readInFile("7input.txt")
	puzzle = np.fromstring("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5", sep = ",", dtype = int)

	#possiblilites = list(itertools.permutations([9,8,7,6,5]))
	currHighest = 0
	#currPos = []
	#for pos in possiblilites:
		#currPuzzle = puzzle.copy()
		#thruster = 0
		#inputs = pos
	inp2 = 0
		#startIndex = 0
		#thruster = 0


	while(True):
		#run A
		[]
		#run B

		#run C

		#run D

		#run E
	for i in inputs:
		thruster = runProgram(puzzle, [i,inp2])
		#thruster = thruster + output
		inp2 = thruster
		if i == 5: i = 9
		# if thruster > currHighest: 
		# 	currHighest = thruster
			#currPos = pos

	# print(currHighest)
	
	

# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()