import parseModule
import matrixClass

def add_rt(inputs):

        if inputs == "":
                print "Invalid Input"
        else:
                if inputs[0] == " ":
                        # parses the input
                        routers = parseModule.parse(inputs)
                        
                        matrixClass.array.add(routers, "rt")
                else:
                        print "Invalid Input"

def add_nt(inputs):
	
        if inputs == "":
                print "Invalid Input"
        else:
                if inputs[0] == " ":
                        #parses the input
                        networks = parseModule.parse(inputs)

                        matrixClass.array.add(networks, "nt")
                else:
                        print "Invalid Input"

