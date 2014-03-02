import matrixClass

def path(v, p):
        #path printing algorithm, recursively prints all intermediate nodes
        if p[v] == -1:
                print matrixClass.array.get(0,v),
                return

        path(p[v], p)
        print matrixClass.array.get(0,v),
