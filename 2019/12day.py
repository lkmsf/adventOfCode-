import numpy as np
from collections import namedtuple


def main(): 
	#writeFile("test.txt")
	#read in moons 
	coors = readInCoors("12input.txt")
	origCoors = coors.copy()
	vel = np.zeros([4,3])
	origVel = np.zeros([4,3])

	loops = [0,0,0]
	i = 1
	while True:
		#print("\ncoors\n", coors,"\norigCoors\n", origCoors, "\nvel\n", vel, "\norigVel\n", origVel)
		[coors, vel] = runStep(coors, vel)

		loops = checkIfSame(loops, i, coors, origCoors, vel, origVel)

		#print(loops)
		if np.all([loops[j] != 0 for j in range(3)]): break

		#if sameStates(coors, origCoors, vel, origVel): break 
		i += 1

	print(loops)
	

def checkIfSame(loops, trial, coors, origCoors, vel, origVel):
	for i in range(3):
		if loops[i]  != 0: continue 
		if np.array_equal(coors[:,i],origCoors[:,i]) and np.array_equal(vel[:,i], origVel[:,i]): 
			loops[i] = trial 
	return loops


def runStep(coors, vel):
	addVel = getGravity(coors)
	vel = vel + addVel
	coors = coors + vel
	return [coors, vel]

def getGravity(coors):
	diff = np.concatenate([getDiff(0, coors), getDiff(1, coors), getDiff(2, coors), getDiff(3, coors)])
	diff = np.reshape(diff, [4,3])
	return diff


def getDiff(index, coors):
	diff = np.zeros([4,3])
	diff[coors[index] > coors] = -1
	diff[coors[index] < coors] = 1
	sumDiff = sum(diff)
	return sumDiff 

def sameStates(coors, origCoors, vel, origVel):
	if not np.array_equal(coors, origCoors): return False 
	if not np.array_equal(vel, origVel): return False 
	return True



def writeFile(fileName):
	file = open(fileName, "r")
	data = file.read()
	data = data.translate({ord(i): None for i in '<>xyz='})
	file = open(fileName, "w")
	file.write(data)
	file.close()


def readInCoors(fileName):
	return np.loadtxt(fileName, delimiter= ",")


# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()