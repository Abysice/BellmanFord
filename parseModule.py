def parse(inputs):
        #takes a string and returns a list of all the numbers in it

	index = 0
	inputs = inputs + "EOS"
	outputs = list()
	flag = True

	#overly complicated parsing code
	while flag == True:
		size = ""
		while inputs[index] == " ":
			index = index + 1
		
		while inputs[index] == "1" or inputs[index] == "2" or inputs[index] == "3" or inputs[index] == "4"  or inputs[index] == "5" or inputs[index] == "6" or inputs[index] == "7" or inputs[index] == "8" or inputs[index] == "9" or inputs[index] == "0":
			size = size + inputs[index]
			index = index + 1
			
		if inputs[index] == "-":
			first = int(size)
			size = ""
			index = index + 1

			while inputs[index] == "1" or inputs[index] == "2" or inputs[index] == "3" or inputs[index] == "4"  or inputs[index] == "5" or inputs[index] == "6" or inputs[index] == "7" or inputs[index] == "8" or inputs[index] == "9" or inputs[index] == "0":
				size = size + inputs[index]
				index = index + 1
			second = int(size)

			for i in range(first,second + 1,1):
				outputs.append(str(i))				        
		else:
			outputs.append(size)

		if inputs[index] == ",":
			flag = True
			index = index + 1
		else:
			flag = False

	return outputs

def parse_con(inputs):

        #break up the input string
	i = 0
	inputs = inputs + "EOF"
	flag = False
	connections = list()
	#overly complicated parsing code
	while i < len(inputs):
		if inputs[i] == "n" and inputs[i+1] == "t":
			if flag == False:
				i = i + 2
				first = ""
				first = first + "nt"
				flag = True
				while inputs[i] == "1" or inputs[i] == "2" or inputs[i] == "3" or inputs[i] == "4"  or inputs[i] == "5" or inputs[i] == "6" or inputs[i] == "7" or inputs[i] == "8" or inputs[i] == "9" or inputs[i] == "0":
					first = first + inputs[i]
					i = i + 1
				connections.append(first)
			else:
				print "Cannot connect two networks"
				break
		if inputs[i] == "r" and inputs[i+1] == "t":
			i = i + 2
			first = ""
			first = first + "rt"
			while inputs[i] == "1" or inputs[i] == "2" or inputs[i] == "3" or inputs[i] == "4"  or inputs[i] == "5" or inputs[i] == "6" or inputs[i] == "7" or inputs[i] == "8" or inputs[i] == "9" or inputs[i] == "0":
				first = first + inputs[i]
				i = i + 1
			connections.append(first)
		if inputs[i] == "1" or inputs[i] == "2" or inputs[i] == "3" or inputs[i] == "4"  or inputs[i] == "5" or inputs[i] == "6" or inputs[i] == "7" or inputs[i] == "8" or inputs[i] == "9" or inputs[i] == "0":
			first = ""
			while inputs[i] == "1" or inputs[i] == "2" or inputs[i] == "3" or inputs[i] == "4"  or inputs[i] == "5" or inputs[i] == "6" or inputs[i] == "7" or inputs[i] == "8" or inputs[i] == "9" or inputs[i] == "0":
				first = first + inputs[i]
				i = i + 1
			connections.append(first)
		i = i + 1

	if len(connections) == 3:
		return connections
	else:
		print "Invalid Input"
		a = ["$", "$", "$"]
		return a

