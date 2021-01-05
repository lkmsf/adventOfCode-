import numpy as np


HIGH_NUM = 999999
def main():
	file = open("6input.txt", mode = "r")
	inp = file.read().splitlines()

	relationMap = getOrbits(inp)

	#totalOrbits = countTotal(relationMap)

	numOfOrbits = getShortestPath("YOU", "SAN", [],  HIGH_NUM, relationMap)
	numOfOrbits = numOfOrbits - 2
	print(numOfOrbits)
	#print(min(numOfOrbits))

	#print(totalOrbits)

	file.close()


def getShortestPath(curr, goal, seen, currShortest, relationMap):
	#print()
	#print("curr:", curr, "goal: ", goal)
	if curr == goal:  return 0

	possiblePaths = []
	sun = getSun(curr, relationMap)
	if sun != None: possiblePaths = possiblePaths + [sun]
	if curr in relationMap: possiblePaths = possiblePaths + relationMap[curr].copy()

	#print("full poss paths ", possiblePaths)

	for path in possiblePaths:
		#print("34 path:", path)
		if path in seen: continue

		newSeen = seen.copy()
		newSeen.append(path)
		#try going here 
		partialPath = getShortestPath(path, goal, newSeen, currShortest, relationMap)

		if(partialPath == HIGH_NUM): continue 

		fullPath = partialPath + 1

		if fullPath < currShortest: currShortest = fullPath
		#print(currShortest)


	return currShortest




def getSun(curr, relationMap):
	#print("curr is:", curr)
	for i in relationMap:
		#print(i , relationMap[i])
		if curr in relationMap[i]: return i
	return None






def getOrbits(inp):
	result = dict()
	#print(type(result))
	for line in inp:
		#print(line)
		[sun, earth] = line.strip().split(")")
		#print(sun, earth)
		if sun in result: result[sun].append(earth)
		else:             result[sun] = [earth]
	return result

def countTotal(realtionMap):
	count = 0
	for key in realtionMap:
		count = count + numIndirect(key, realtionMap)

	return count 

def numIndirect(key, relationMap):
	if not key in relationMap: return 0
	vals = relationMap[key]
	count = 0
	for i in vals:
		count = count + 1 + numIndirect(i, relationMap)

	return count 





# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()