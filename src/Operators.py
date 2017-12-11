def IN(x, V):
	return x in V
def INDEX(x, V):
	if IN(x, V): 
		return V.index(x)

def isnum(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

def isint(x):
	return x == int(x)

def getinputs(o, x):
	for i in range(len(x)):
		if isnum(x[i]):
			x[i] = float(x[i])
		else:
			x[i] = o[x[i]]
	return x

def ADD(o, x):
	x = getinputs(o, x)
	return sum(x)

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

def GET(o, x):
	return o[x[0]]
# def I(x,i):
# 	return x[i]
# def NOT(x,i):
# 	return not I(x,i)
# def AND(x,g,i):
# 	return I(x,i) and I(g,i)
# def OR(x,g,i):
# 	return I(x,i) or I(g,i)
# def IS(x,g,i):
# 	return I(x,i) is I(g,i)
# def GT(x,g,i):
# 	return I(x,i) > I(g,i)
# def LT(x,g,i):
# 	return I(x,i) < I(g,i)
# def GTET(x,g,i):
# 	return OR(GT(x,g,i), ET(x,g,i))
# def LTET(x,g,i):
# 	return OR(LT(x,g,i), ET(x,g,i))
# def SUB(x,g,i):
# 	return I(x,i) - I(g,i)
# def ADD(x,g,i):
# 	return I(x,i) + I(g,i)
# def MLT(x,g,i):
# 	return I(x,i) * I(g,i)
# def DIV(x,g,i):
# 	return I(x,i) * I(g,i)
# def POW(x,g,i):
# 	return I(x,i) ** I(g,i)

# operatorlist = {
# 	'in':IN,
# 	'index':INDEX
# 	'and':AND,
# 	'or':OR,
# 	'is':IS,
# 	'gt':GT,
# 	'lt':LT,
# 	'gtet':GTET,
# 	'ltet':LTET,
# 	'sub':SUB,
# 	'add':ADD,
# 	'mult':MLT,
# 	'div':DIV,
# 	'pow':POW
# }