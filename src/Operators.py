from Functions import *

def AND(o, x):
	x = getinputs(o, x)
	for i in range(len(x)):
		if x[i] == 0:
			return 0
	return 1

def OR(o, x):
	x = getinputs(o, x)
	for i in range(len(x)):
		if x[i] == 1:
			return 1
	return 0

def GET(o, x):
	return o[x[0]]

def SET(o, x):
	k = x[0]
	x = x[1]
	if isnum(x):
		if isint(x):
			x = int(x)
		else:
			x = float(x)
	else:
		x = o[x]
	o[k] = x

def ADD(o, x):
	x = getinputs(o, x)
	return sum(x)

