
import math 

def main():
	input = open("1input.txt", 'r')
	totalFuel = 0
	for fuel  in input:
		#totalFuel = totalFuel + getFuel(int(fuel))
		totalFuel = totalFuel + getFuelRec(int(fuel))
	print(totalFuel)

def getFuel(mass):
	mass = math.floor(mass/3) - 2
	return mass

def getFuelRec(mass):
	currAdd  = getFuel(mass) 
	if(currAdd <= 0):
		return 0
	return currAdd + getFuelRec(currAdd)

# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()