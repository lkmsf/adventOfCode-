
import numpy as np
from collections import namedtuple


instruction = namedtuple("instruction", "opCode modes params")

class puzzleInfo:
	def __init__(self, arrayInput, inputVal, instruction, index):
		self.arrayInput = arrayInput
		self.inputVal = inputVal
		self.instruction = instruction
		self.index = index



def readInFile(fileName):
	origInput = np.loadtxt(fileName, delimiter = "," , dtype = int)
	return origInput


def runProgram(puzzle, inp):
	currProgram = puzzleInfo( arrayInput  = puzzle, 
		                      inputVal    = inp, 
		                      instruction = instruction(0,[],[]), 
		                      index       = 0)
	i = 0
	#print("current index: ", 0)
	while(not currProgram.instruction.opCode == 99):
		debuggingPrint(currProgram)
		runStep(currProgram)
		
		#i = i + 1

		#print(currProgram.instruction.opCode)
	return currProgram.inputVal[0]

def debuggingPrint(currProgram):
	print("input = ", currProgram.inputVal)
	print("instruction =  ", currProgram.instruction)
	print(currProgram.arrayInput[:currProgram.index + 5])
	print()
	print("current index: ", currProgram.index)
	print("currVal = ", currProgram.arrayInput[currProgram.index])
	

def runStep(currProgram):

	if currProgram.arrayInput[currProgram.index] == 99: 
		currProgram.instruction = instruction(99, [], [])
		print("Done!")
		return

	updateInstruction(currProgram)

	currVal = currProgram.instruction.opCode

	if   currVal == 99: return 
	elif currVal == 1 : opCodeOne(currProgram)
	elif currVal == 2 : opCodeTwo(currProgram)
	elif currVal == 3 : opCodeThree(currProgram)
	elif currVal == 4 : opCodeFour(currProgram)
	elif currVal == 5 : opCodeFive(currProgram)
	elif currVal == 6 : opCodeSix(currProgram)
	elif currVal == 7 : opCodeSeven(currProgram)
	elif currVal == 8 : opCodeEight(currProgram)
	else: raise Exception("invalid opcode:")



def opCodeOne(currProgram):
	params = currProgram.instruction.params
	replaceVal = params[0] + params[1]
	currProgram.arrayInput[params[2]] = replaceVal
	currProgram.index = currProgram.index + 4

def opCodeTwo(currProgram):
	params = currProgram.instruction.params
	replaceVal = params[0] * params[1]
	currProgram.arrayInput[params[2]] = replaceVal
	currProgram.index = currProgram.index + 4

def opCodeThree(currProgram): 
	param = currProgram.instruction.params
	puzzle = currProgram.arrayInput
	if len(currProgram.inputVal) == 0: raise Exception("no input val")
	puzzle[param] = currProgram.inputVal.pop(0)
	currProgram.index = currProgram.index + 2

def opCodeFour(currProgram): 
	param = currProgram.instruction.params
	currProgram.inputVal = [currProgram.arrayInput[param]]
	currProgram.index = currProgram.index + 2
	print("output:", currProgram.inputVal)

def opCodeFive(currProgram):
	[param1,param2] = currProgram.instruction.params[0:2]
	if param1 != 0:
		currProgram.index = param2
	else:
		currProgram.index = currProgram.index + 3

def opCodeSix(currProgram):
	[param1,param2] = currProgram.instruction.params[0:2]
	if param1 == 0:
		currProgram.index = param2
	else:
		currProgram.index = currProgram.index + 3

def opCodeSeven(currProgram):
	[param1,param2, param3] = currProgram.instruction.params
	if param1 < param2:
		currProgram.arrayInput[param3] = 1
	else:
		currProgram.arrayInput[param3] = 0
	currProgram.index = currProgram.index + 4

def opCodeEight(currProgram):
	[param1,param2, param3] = currProgram.instruction.params
	if param1 == param2:
		currProgram.arrayInput[param3] = 1
	else:
		currProgram.arrayInput[param3] = 0
	currProgram.index = currProgram.index + 4





def getParams(currProgram):
	params = [0, 0, 0]

	puzzle = currProgram.arrayInput

	index = currProgram.index
	modes = currProgram.instruction.modes

	for i in range(2):
		mode = modes[i]
		if mode == 0: #postion mode
			params[i] = puzzle[puzzle[index + i + 1]]
		elif mode == 1:
			params[i] = puzzle[index + i + 1]
		else: raise Exception("invalid mode: ", mode)

	params[2] = puzzle[index + 3]

	return params

def updateInstruction(currProgram):
	instructionInt = currProgram.arrayInput[currProgram.index]

	[opCode, modes] = getArray_op(instructionInt)

	currProgram.instruction = instruction(opCode = opCode, 
	 									   modes = modes, 
	 									  params = [0,0,0]) #update opcode and modes

	if opCode == 3 or opCode == 4:
		modes = "n/a"
		params = currProgram.arrayInput[currProgram.index + 1]
	else:  
		params = getParams(currProgram)

	currProgram.instruction = instruction(opCode, modes, params)  #final full instruction
	

def getArray_op(instructionInt):
	instructionInt = [int(x) for x in str(instructionInt)]
	while(len(instructionInt)) < 5:
		instructionInt.insert(0,0)
	currOpCode = int(str( instructionInt[-2]) + str( instructionInt[-1]))
	modes = instructionInt[:-2]
	modes = [modes[x] for x in range(2,-1,-1)]
	return [currOpCode, modes]



