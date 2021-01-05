import numpy as np
from AOCfunctions import readInFile

HIGH_NUM = 99999

HEIGHT = 0
WIDTH =  0 
def main(): 
	#get Data 
	file = open("20input.txt", "r")
	#file = open("test.txt", "r")
	result = file.read() 
	lenOfFile = len(result)
	result = result.splitlines()
	#print(result[0])
	WIDTH = len(result[0])
	HEIGHT = int(lenOfFile/WIDTH) - 1
	#print(WIDTH,HEIGHT)
	file.close()

	inp = np.chararray([HEIGHT, WIDTH], unicode = True)

	keysToFind = []
	for i in range(HEIGHT):
		for j in range(WIDTH):
			#print(i,j)
			inp[i,j] = result[i][j]

	result = findPortal("MJ", inp)
	print(result)

	#shortestPath = getShortestPath('@', keysToFind, 99999, inp, mem, hMem)

def findPortal(portal, maze):
	possiblitiesA = np.where(maze == portal[0])
	possiblitiesB = np.where(maze == portal[1])
	#print(np.concatenate([possiblitiesA,possiblitiesB]))
	results = np.sort(np.concatenate([possiblitiesA,possiblitiesB]))
	print("A:", possiblitiesA,"B:", possiblitiesB, "both",results)
	return results[:2]


def getShortestPath(curr, goal, seen, currShortest, maze):
	#print()
	#print("gdtl", "curr:", curr, maze[curr],"goal: ", goal)
	#print("currPath: ", pathSoFar)
	if curr == goal:  
		#print("got here")
		return 0

	#don't include the last letter because we're still trying to go there
	possiblePaths = getPossiblePaths(curr, pathSoFar[:-1], maze) 

	#print("gdtl", "full poss paths ", possiblePaths)
	#for i in possiblePaths: print(maze[i])

	for path in possiblePaths:
		#print("34 path:", path)
		if path in seen: continue

		newSeen = seen.copy()
		newSeen.append(path)
		#try going here 
		partialPath = getShortestToLtr(path, goal, pathSoFar, newSeen, currShortest, maze)

		if(partialPath == HIGH_NUM): continue 

		fullPath = partialPath + 1

		if fullPath < currShortest: currShortest = fullPath

	#hMem[sortString(pathSoFar)] = currShortest
	return currShortest

def getPossiblePaths(curr, pathSoFar, matrix):  #we need coordinates
	[xCurr, yCurr] = curr
	possibleCoords = [(xCurr + 1, yCurr), (xCurr - 1, yCurr), (xCurr, yCurr + 1), (xCurr, yCurr - 1)]
	#print("possible coor:", possibleCoords)

	validCoors = []
	for i in possibleCoords:

		if i[0] >= HEIGHT or i[0] < 0: continue 
		elif i[1] >= WIDTH or i[1] < 0: continue

		currVal = matrix[tuple(i)][0]
		#print(currVal)

		if currVal == '#': 
			#print("can't go here- #")
			continue 

		elif currVal.isupper():
			#print(currVal, "is upper")
			if currVal.lower() in pathSoFar: #we have the key
				validCoors.append(i)
			else: 
				#print("can't go here- no key")
				continue   #we don't have the key for that door

		
		validCoors.append(i)


	#print("valid coordinates:", validCoors)
	return validCoors
	

# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()