from Objects import *

def parse(statement):
	w = ''
	s = []
	state = None
	for i in range(len(statement)):
		if state == None:
			s.append('START')

		state = s[len(s)-1]
		if statement[i] == '(':
			s.append('CALL')
			s.append(w)
			s.append('INPUT')
			w = ''
		elif statement[i] == ',':
			s.append(w)
			s.append('INPUT')
			w = ''
		elif statement[i] == ')':
			if w != '':
				s.append(w)

			s.append('END')
			w = ''
		elif statement[i] == ';':
			s.append('STOP') 
			w = ''
		elif statement[i] != ' ':
			w += statement[i]
	return s

def merge(m, i):
	for j in range(len(m[i]['X'])):
		if m[i]['X'][j] == 'CALL':
			m[i]['X'][j] = merge(m, i+1)
	return m[i]

def convert(s):
	state = None
	model = []
	t = []
	v = []
	for i in range(len(s)):
		if s[i] == 'START':
			state = -1
		elif s[i] == 'CALL':
			model.append(Model(s[i+1]))
			state += 1
		elif s[i] == 'END':
			state -= 1
		elif s[i] == 'STOP':
			state = None
		elif s[i] == 'INPUT':
			model[len(model)-1]['X'].append(s[i+1])
	merge(model, 0)
	return model[0]

def call(system, model):
	inputs = []
	for i in range(len(model['X'])):
		x = model['X'][i]
		if isobject(x): x = call(system, x)
		inputs.append(x)
	return system['F'][model['F']](system, inputs)
