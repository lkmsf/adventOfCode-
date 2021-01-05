import numpy as np
from collections import namedtuple
from intCodeFunctions import readInFile, runProgram, getArray_op

instruction = namedtuple("instruction", ["opCode", "mode1", "mode2", "mode3"])

def main(): 
	input = 5
	#getArray_op("1101")
	#puzzle = np.fromstring("1101, 1, 1, 0, 99", sep = ",", dtype = int)
	puzzle = readInFile("5input.txt")
	runProgram(puzzle, input)

# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()