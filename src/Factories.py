from Object import *

def Model(F):
	o = Object('model')
	o['F'] = F
	o['X'] = []
	return o

def Proposition(o, i, j):
	p = Object('proposition')
	p['o'] = o
	p['i'] = i
	p['j'] = j
	return p 