class Constraint:
	def __init__(self, possible=[]):
		self.values = possible
		self.utilities = [0 for i in range(len(possible))]
		self.threshold = 0.5
		self.rate = 0.1

	def update(self, value, validity):
		if value not in self.values:
			self.values.append(value)
			self.utilities.append(0)
		
		index = self.values.index(value)
		utility = self.utilities[index]
		delta = validity-utility
		self.utilities[index] += self.rate*delta

	def predict(self, value):
		if value not in self.values:
			return -1
		else:
			index = self.values.index(value)
			utility = self.utilities[index]
			delta = utility - self.threshold
			return delta


