

def main(): 
	low = 264793
	high = 803935

	currNum = 0
	for i in range(low, high + 1):
		if  not valid(i):
			continue
		print(i)
		currNum = currNum + 1

	print(currNum)


def valid(num):

	digits = [int(x) for x in str(num)] 

	validDouble = False
	prevNum = digits[0]
	for i in range(1, len(digits)):
		currNum = digits[i]

		if currNum < prevNum:
			#print("line ", 26, currNum, "is less than ", prevNum)
			return False  

		if not validDouble and currNum == prevNum:
			if checkborders(digits, i):
				validDouble = True 
		prevNum = currNum


	if(not validDouble): 
		#print("invalid double")
		return False 

	return True


def checkborders(digits, rInd):
	leftBorder = rInd - 2
	rightBorder = rInd + 1
	dig = digits[rInd]

	if (leftBorder < 0 or digits[leftBorder] != dig) and (rightBorder > 5 or digits[rightBorder] != dig) : 
		return True 

	return False 








# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()