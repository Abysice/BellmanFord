import edgeClass
import parseModule
import matrixClass
import pathFunc

def tree(node):
     
	#bad input catching
	if len(node) < 3:
		print "Syntax Error"
		return False
	else:
	      tree = parseModule.parse(node[2:])
	      prefix = node[:2]
	      if len(tree) > 1:
		      print "Syntax Error"
		      return False
	      else:
		      pass

	#sort all edges into a list of edges called line
	lines = list()
	d = []
	p = []
	for i in range(1,matrixClass.array.size(),1):
		for j in range(1, matrixClass.array.size(),1):
			if matrixClass.array.get(i, j) > 0:
				bob = edgeClass.edge(j,i,matrixClass.array.get(i, j))
				lines.append(bob)
			else:
				pass
			
	for i in range(0, matrixClass.array.size(), 1):
		d.append([])
		p.append([])
		d[i] = 99999
		p[i] = -1
			
	d[matrixClass.array.findIndex(prefix + tree[0])] = 0
				
	#Bellman Ford Algorithm
	for i in range(0, matrixClass.array.size() - 1, 1):
		for j in range(0, len(lines),1):
			if (d[lines[j].u] + lines[j].w) < d[lines[j].v]:
				d[lines[j].v] = d[lines[j].u] + lines[j].w
				p[lines[j].v] = lines[j].u

			
					
	#prints the tree and all connected or not connected paths
	for i in range(1, len(d),1):
		if d[i] == 99999:
			print "no connection",
		else:
			print d[i],
			print "--",
			pathFunc.path(i, p)
			print "--",
		print " to",
		print matrixClass.array.get(0,i)
