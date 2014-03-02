import parseModule
import matrixClass

def del_rt(inputs):

        if inputs == "":
                print "Invalid Input"
        else:
                if inputs[0] == " ":
                        #parses the input
                        routers = parseModule.parse(inputs)

                        matrixClass.array.delete(routers, "rt")
                else:
                        print "Invalid Input"

def del_nt(inputs):

        if inputs == "":
                print "Invalid Input"
        else:
                if inputs[0] == " ":
                        #parses the input
                        networks = parseModule.parse(inputs)

                        matrixClass.array.delete(networks, "nt")
                else:
                        print "Invalid Input"

       

        
