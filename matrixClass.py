class Matrix(object):
	def __init__(self):
		initmat = []
		initmat.append(["*"])
		self._adjmatrix = initmat
		self._matsize = 1
	def get(self, posx, posy):
		if posx < 0 or posy < 0:
			return "get must be non negative"
		else:
			return self._adjmatrix[posx][posy]
	def set(self, posx, posy, value):
		self._adjmatrix[posx][posy] = value
	def size(self):
		return self._matsize
	def add(self, nodelist, nodetype):
                for i in xrange(0,len(nodelist),1):
			if self._adjmatrix[0].count(nodetype + nodelist[i]) == 0:
				self._adjmatrix.append([])
				self._adjmatrix[len(self._adjmatrix) - 1].append(nodetype + nodelist[i])
			else:
				print nodetype + " " + nodelist[i] + " already exists"

		self._matsize = len(self._adjmatrix)

		for j in xrange(1,len(nodelist)+ 1,1):
			if self._adjmatrix[0].count(nodetype + nodelist[j - 1]) == 0:
				self._adjmatrix[0].append(nodetype + nodelist[j - 1])
			else:
				pass

		self._matsize = len(self._adjmatrix)

		#populates the list with 0's
		for k in xrange(1, self._matsize,1):
			for m in xrange(0,self._matsize,1):
				if len(self._adjmatrix[k]) < len(self._adjmatrix[0]):
					self._adjmatrix[k].append(0)
	def delete(self, nodelist, nodetype):
		for i in xrange(0, len(nodelist),1):
			try:
				l = self._adjmatrix[0].index(nodetype + nodelist[i])
				del self._adjmatrix[l]
				for m in xrange(0, len(self._adjmatrix),1):
					del self._adjmatrix[m][l]
			except:
				print nodetype + nodelist[i] + " was not there"
		self._matsize = len(self._adjmatrix)
	def findIndex(self, value):
		return self._adjmatrix[0].index(value)

array = Matrix()
