import matrixClass
import parseModule

def con(inputs):

        #parses the input and connects the nodes on the adjacency matrix
        vals = parseModule.parse_con(inputs)

        
        try:
                if vals[0] == "$":
                        matrixClass.array.set(0,0,vals[20])
                else:
                        x = matrixClass.array.findIndex(vals[0])
                        y = matrixClass.array.findIndex(vals[1])
                        vec = int(vals[2])
                        matrixClass.array.set(y,x,vec)
        except:
                print "Invalid Input"
