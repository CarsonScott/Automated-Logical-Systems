from Operators import *

def isobject(X):
	return isinstance(X, Object)

# def compute(O, X):
# 	if O.typeof('rule'):
# 		O['X'] = X
# 		O['S'] = IN(O['X'], O['V'])
	
# 	elif O.typeof('ruleset'):
# 		O['X'] = X
# 		for i in range(len(O['X'])):
# 			O['I'] = i
# 			compute(O['R'][O['I']], O['X'][O['I']])
# 			O['S'] = O['R'][O['I']]['S']
# 			if O['S'] == 0: break

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
	# def compute(self, O):
	# 	keys = O.keys()
	# 	for i in range(len(keys)):
	# 		if isobject(O[keys[i]]):
	# 			self.compute(O[keys[i]])
	# 			O.set(keys[i], O[keys[i]].get('V'))

	# 	if O.typeof('getter'):
	# 		O.set('V', self.get(O['K']))
	# 	elif O.typeof('setter'):
	# 		self.set(O['K'], O['V'])

def Model(F):
	o = Object('model')
	o['F'] = F
	o['X'] = []
	return o

def Rule(V, X):
	O = Object('rule')
	O['V'] = V
	O['X'] = X
	O['S'] = None
	return O

def RuleSet(V):
	O = Object('ruleset')
	O['X'] = None
	O['S'] = None
	O['I'] = 0
	O['R'] = []
	for i in range(len(V)):
		C = Rule(V[i])
		O['R'].append(C)
	return O