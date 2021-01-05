
import numpy as np

def main():
	origInput = np.loadtxt("2input.txt", delimiter = "," , dtype = int)
	#input = np.fromstring("1,0,0,0,99", dtype = int, sep=",")

	#restore program
	for i in range(100):
		for j in range(100):
			input = origInput.copy() 
			input[1] = i
			input[2] = j
			result = runProgram(0, input)

			if(result[0] == 19690720):
				print("noun = ", i)
				print("verb = ", j)
				print("answer = ", (100 * i) + j)
				return 
	


	#run program 
	# input[1] = 76  
	# input[2] = 50

	# result = runProgram(0, input)
	# print(result[0])

def runProgram(index, puzzle):
	while(True):
		currVal = puzzle[index]
		if currVal == 99: #end program 
			return puzzle 
		elif ((index + 3) > np.size(puzzle) or (puzzle[index + 1] > np.size(puzzle)) or 
			  (puzzle[index + 2] > np.size(puzzle)) or (puzzle[index + 3] > np.size(puzzle))):
			return "nope" 
		elif currVal == 1: #add
			replaceVal = puzzle[puzzle[index + 1]] + puzzle[puzzle[index + 2]]
			puzzle[puzzle[index + 3]] = replaceVal
		elif currVal == 2: #multiply 
			replaceVal = puzzle[puzzle[index + 1]] * puzzle[puzzle[index + 2]]
			puzzle[puzzle[index + 3]] = replaceVal
		else:
			return "nope" 
		index = index + 4


	





# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()