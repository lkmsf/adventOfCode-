import numpy as np
from AOCfunctions import readInFile


PIX_WIDE =  25
PIX_TALL = 6

def main():

	file = open("8input.txt", mode = "r")
	inp = list(file.read().strip())
	lenOfInp = len(inp)
	inp = np.array(inp, dtype = int)

	
	numLayers = int(lenOfInp / (PIX_TALL * PIX_WIDE))


	image = inp.reshape(numLayers, (PIX_TALL * PIX_WIDE))


	finalImage = np.zeros([PIX_TALL,PIX_WIDE])


	newImage = inp.reshape(numLayers * PIX_TALL, int((PIX_TALL * PIX_WIDE)/PIX_TALL))



	for i in range(PIX_TALL):
		for j in range(PIX_WIDE):
			currVal = 2
			depth = 0
			while(currVal == 2):
				currVal = newImage[i + depth, j]
				depth = depth + PIX_TALL
			finalImage[i,j] = currVal


	print(finalImage)




	# print(image, len(image))

	# numOfZeros = np.count_nonzero(image == 0, axis = 1)
	# print(numOfZeros)
	# maxRowIndex = np.argmin(numOfZeros)
	# print(maxRowIndex)

	# maxRow = image[maxRowIndex,:]
	# print(maxRow)
 
	# result = sum(maxRow == 1) * sum(maxRow == 2)


	# print(result)

	





# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()