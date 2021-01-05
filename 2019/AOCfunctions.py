import numpy as np


def readInFile(day, result, test = False, dlim = "" ):
	fileName = "{}input.txt".format(day)
	if test: fileName = "test.txt"

	if   result == "string":    toReturn = readInString(fileName)
	elif result == "list":      toReturn = readInList(fileName)
	elif result == "np array":  toReturn = readin_NParray(fileName, dlim)

	return toReturn

 

def readInString(fileName):
	file = open(fileName, "r")
	result = file.read()
	file.close()
	return result

def readInList(fileName):
	file = open(fileName, "r")
	result = file.read().splitlines()
	file.close()
	return result

def readin_NParray(fileName, dlim):
	return np.loadtxt(fileName, delimiter = dlim , dtype = int)
	

