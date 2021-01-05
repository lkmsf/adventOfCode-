
from collections import namedtuple
import operator

point = namedtuple("point", ["x", "y"])

def main():
	input = open("3input.txt", "r")
	[wire1, wire2] = input.readlines() 
	#[wire1, wire2] = ["R8,U5,L5,D3", "U7,R6,D4,L4"]

	coors1 = getCoors(wire1)
	coors2 = getCoors(wire2)

	#get intersections 
	intersections = [k for k in coors1 if k in coors2]

	#get step distances 
	dist = []
	for i in intersections:
		dist.append(coors1[i] + coors2[i])

	dist.sort()

	print(dist)

	#getDistances 
	# dist = []
	# for i in intersections:
	# 	dist.append(abs(i.x) + abs(i.y))
	# dist.sort()


	#print(dist)
	#closestInt = dist[0]
	#print("manhattan dist: ", closestInt)



	#input.close()


def getCoors(input):
	coors = {}
	currCoor = point(x = 0, y = 0)
	coors[currCoor] = 0
	input = input.split(",")
	for i in input:
		[direction, amt] = [i[0], int(i[1:])]

		if direction == "R":
			for i in range(1, amt + 1):
				nextPoint = point(x = currCoor.x + i, y = currCoor.y)
				coors[nextPoint] = coors[currCoor] + i
			currCoor = nextPoint
		elif direction == "L":
			for i in range(1, amt + 1):
				nextPoint = point(x = currCoor.x - i, y = currCoor.y)
				coors[nextPoint] = coors[currCoor] + i
			currCoor = nextPoint
		elif direction == "U": 
			for i in range(1, amt + 1):
				nextPoint = point(x = currCoor.x, y = currCoor.y + i)
				coors[nextPoint] = coors[currCoor] + i
			currCoor = nextPoint
		else: 
			for i in range(1, amt + 1):
				nextPoint = point(x = currCoor.x , y = currCoor.y - i)
				coors[nextPoint] = coors[currCoor] + i
			currCoor = nextPoint
	return coors








# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()