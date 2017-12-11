from Functions import *

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

def AND(o, x):
	x = getinputs(o, x)
	return x[0] and x[1]

def OR(o, x):
	x = getinputs(o, x)
	return x[0] or x[1]

def NOT(o, x):
	x = getinputs(o, x)
	return not x[0]

def EQUAL(o, x):
	x = getinputs(o, x)
	return x[0] == x[1]

def MORE(o, x):
	x = getinputs(o, x)
	return x[0] > x[1]

def LESS(o, x):
	x = getinputs(o, x)
	return x[0] < x[1]

def MOE(o, x):
	x = getinputs(o, x)
	return x[0] >= x[1]

def LOE(o, x):
	x = getinputs(o, x)
	return x[0] <= x[1]

def ADD(o, x):
	x = getinputs(o, x)
	return x[0] + x[1]

def SUB(o, x):
	x = getinputs(o, x)
	return x[0] - x[1]

def MULT(o, x):
	x = getinputs(o, x)
	return x[0] * x[1]

def DIV(o, x):
	x = getinputs(o, x)
	return x[0] / x[1]

def SQR(o, x):
	x = getinputs(o, x)
	return x[0] ** 2

def ABS(o, x):
	x = getinputs(o, x)
	return abs(x[0])