import numpy as np
from AOCfunctions import readInFile

import itertools 


HIGH_NUM = 99999

HEIGHT = 9 #81 #9
WIDTH =  17 #81 #17
def main(): 
	#get Data 
	#file = open("18input.txt", "r")
	file = open("test.txt", "r")
	result = file.read().splitlines()
	file.close()

	inp = np.chararray([HEIGHT, WIDTH], unicode = True)

	keysToFind = []
	for i in range(HEIGHT):
		for j in range(WIDTH):
			inp[i,j] = result[i][j]
			if inp[i,j].islower(): keysToFind.append(inp[i,j]) 

	#start = np.where(inp == '@')

	#print(start)

	mem = dict()
	hMem = dict()
	shortestPath = getShortestPath('@', keysToFind, 99999, inp, mem, hMem)

	# shortestPath = 0
	# path = "@cebfkgahjdmonipl"
	# for i in range(len(path)-1):
	# 	l1 = path[i]
	# 	l2 = path[i+1]
	# 	shortestPath = shortestPath + getShortestToLtr(np.where(inp == l1), np.where(inp == l2), path[:i + 2], [], HIGH_NUM, inp)

	print(shortestPath)


def getShortestPath(pathSoFar, keysToFind, currShortest, maze, mem, hMem):
	#print()
	currVal = pathSoFar[-1]
	#print("started gSP", pathSoFar)
	#base case 
	if len(keysToFind) == 0: 
		#print(pathSoFar)
		return 0

	#memoization
	sortedPath = sortString(pathSoFar)
	
	if sortedPath in mem: 
		#print("sortedPath: ", sortedPath,  mem[sortedPath])
		return mem[sortedPath]

	#recursive case 
	
	#print("keysToFind", keysToFind)
	for key in keysToFind:
		#print("currVal:", currVal)
		#print("curr key:", key)

		#get ready for next recursive call
		newKeysToFind = keysToFind.copy()
		newKeysToFind.remove(key)
		newPathSoFar = pathSoFar + key

		#find distance to ltr
		sortedNewPath = sortString(newPathSoFar[:-2]) + sortString(newPathSoFar[-2:])
		shortCut = sortString(newPathSoFar[-2:])
		if sortedNewPath in hMem:   
			sToLtr = hMem[sortedNewPath]
		elif shortCut in hMem and hMem[shortCut] != HIGH_NUM:
			sToLtr = hMem[shortCut]
		else:
			#print("parameters:", np.where(maze == currVal), np.where(maze == key), newPathSoFar, [], HIGH_NUM)
			sToLtr = getShortestToLtr(np.where(maze == currVal), np.where(maze == key), newPathSoFar, [], HIGH_NUM, maze)
			hMem[sortedNewPath] = sToLtr

		#print(currVal, "to", key, "is", sToLtr)
		if sToLtr == HIGH_NUM: continue 
		
		#print(newKeysToFind)
		trySdist = getShortestPath(newPathSoFar, newKeysToFind, currShortest, maze, mem, hMem)
		trySdist = trySdist + sToLtr
		#print("try distance: ", trySdist)
		#print(trySdist)
		#compare result to prev shortest
		if trySdist < currShortest: currShortest = trySdist

	#return and update mem
	#print(len(newPathSoFar))
	mem[sortString(newPathSoFar)] = currShortest
	return currShortest




def sortString(a):
	return ''.join(sorted(a))


def getShortestToLtr(curr, goal, pathSoFar, seen, currShortest, maze):
	#print()
	#print("gdtl", "curr:", curr, maze[curr],"goal: ", goal)
	#print("currPath: ", pathSoFar)
	ltr1 = maze[curr]
	ltr2 = maze[goal]
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


# def getShortestToLtr(curr, keysToFind, seen, currShortest, matrix):
# 	#print()
# 	#print()

# 	#print("curr:", matrix[curr],curr) #, "keysToFind: ", keysToFind)

# 	if len(keysToFind) == 0:  
# 		#print("found everything")
# 		return 0

# 	possiblePaths = getPossiblePaths(curr, keysToFind, matrix)

# 	pathVals = []
# 	for i in possiblePaths:
# 		pathVals.append(matrix[i])
# 	#print("possiblePath Values: ", pathVals)

# 	#print("full poss paths ", possiblePaths)
# 	for path in possiblePaths:

# 		if path in seen: continue

# 		currVal = matrix[path]
# 		#print("val:", currVal, "curr path:", path)

# 		newSeen = seen.copy()
# 		newKeysToFind = keysToFind.copy()

# 		newSeen.append(path)

# 		if currVal.islower() and currVal in newKeysToFind: 
# 			#print("choose a letter")
# 			newKeysToFind.remove(currVal)
# 			newSeen.clear()
# 		#print("keys to find:", newKeysToFind)

# 		#try going here 
# 		fullPath = getShortestPath(path,newKeysToFind, newSeen, currShortest, matrix) + 1

# 		#if(partialPath == HIGH_NUM): continue 

# 		#fullPath = partialPath + 1

# 		if fullPath < currShortest: currShortest = fullPath
# 		#print("currShortest", currShortest)

# 	return currShortest

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