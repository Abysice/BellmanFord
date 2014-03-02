import matrixClass

def display():

	#prints the adjacency matrix
	temp = matrixClass.array.size()			
	for x in range(0, temp):
		for y in range(0, temp):
			print matrixClass.array.get(x, y),
			print " ",
		print " "
