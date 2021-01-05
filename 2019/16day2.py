import numpy as np

def main():
	file = open("16input.txt", mode = "r")
	inp = file.read().strip()
	#inp = [1,2,3,4,5,6,7,8]

	inp = list("03036732577212944063491565474664")

	inp = list(map(int, inp))

	messageOffset = inp[:7]

	inp = np.tile(inp, 10000)

	base = np.asarray([0, 1, 0, -1])

	numPhases = 1


	lenOfInp = len(inp)
	#get tiledBases 
	bases = np.zeros([lenOfInp, lenOfInp])

	for j in range(lenOfInp):
		if j == 0 or j%1000 == 0: print("starting", j)
		newBase = tiledBase(base, lenOfInp)
		#if j == 0 or j%1000 == 0: print("done with tiled Base", j)
		bases[:,j] = newBase
		#if j == 0 or j%1000 == 0: print("done with bases",j)
		base = getNewBase(base, lenOfInp)
		#if j == 0 or j%1000 == 0: print("done with getNewBase",j)

	print(bases)

	result = inp
	for i in range(numPhases):
		result = doAPhase(result, bases)
		print("phase ", i, "done")


	print(result[messageOffset: messageOffset + 8])



def doAPhase(inp, bases):

	result = np.matmul(inp, bases)

	# for j in range(lenOfInp):
		

	# 	currVal = 
	# 	#print(currVal)

	# 	toAppend = int(str(currVal)[-1])
	# 	result.append(toAppend)   #only ones digit
	# 	#print("base: ", base)

	# 	if j == 1 or j%1000 == 0: print("j is: ", j)


	return result 



def getNewBase(base, maxLength):
	result = []
	prevA = base[0]
	for i in range(len(base)):
		result.append(prevA)
		if base[i] != prevA:
			result.append(base[i])
		prevA = base[i]
		if i > maxLength - 1: return result 
	result.append(base[i])
	return result 



def tiledBase(base, size):
	if size < len(base): return base[1:size+1]
	result = base[1:]
	resultSize = len(result)
	[rep, remainder] = divmod(size - resultSize, len(base))
	bit1 = result
	bit2 = np.tile(base, rep)
	bit3 = base[:remainder]
	result = np.concatenate([bit1, bit2, bit3])
	return result








# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()