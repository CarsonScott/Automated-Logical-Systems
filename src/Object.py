class Object(dict):
	def __init__(self, T):
		self['T'] = T
	def values(self):
		return list(super().values())
	def keys(self):
		return list(super().keys())
	def typeof(self, T):
		return self['T'] == T
	def get(self, K):
		return self[K]
	def set(self, K, V):
		self[K] = V


