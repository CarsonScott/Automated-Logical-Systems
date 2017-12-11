from Factories import Proposition

class System:

	def __init__(self, values):
		self.values = []
		self.inputs = []
		self.rate = 0.1
		self.threshold = 0.5

		for i in range(values):
			self.inputs.append(0)
			self.values.append([])
			for j in range(values):
				self.values[i].append(0)

	def C(self, p, q):
		return self.values[p][q] >= self.threshold
	def N(self, p, q):
		return self.values[p][q] <= -self.threshold
	def B(self, p, q):
		return self.C(p, q) and self.C(q, p)
	def E(self, p, q):
		return self.N(p, q) and self.N(q, p)

	def get(self, i, j):
		return self.values[i][j]
	def set(self, i, j, v):
		self.values[i][j] = v

	def update(self, inputs):
		self.inputs = inputs
		for i in range(len(self.values)):
			for j in range(len(self.values)):
				xi = self.inputs[i]
				xj = self.inputs[j]
				v = self.get(i,j)
				if xi:
					if xj:
						v += self.rate
					else:
						v -= self.rate
				if abs(v) > 1:
					v /= abs(v)
				self.set(i,j,v)

	def compute(self, p):
		o = p['o']
		i = p['i']
		j = p['j']
		if o == 'c':
			return self.C(i, j)
		if o == 'n':
			return self.N(i, j)
		if o == 'b':
			return self.B(i, j)
		if o == 'e':
			return self.E(i, j)
		return None

	def convert(self, i, j):
		if self.B(i, j):
			return Proposition('b', i, j)
		elif self.C(i, j):
			return Proposition('c', i, j)
		elif self.C(j, i):
			return Proposition('c', j, i)
		elif self.E(i, j):
			return Proposition('e', i, j)
		elif self.N(i, j):
			return Proposition('n', i, j)
		elif self.N(j, i):
			return Proposition('n', j, i)

