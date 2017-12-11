from Functions import *

class Interpreter(Object):
	def __init__(self, operators):
		super().__init__('interpreter')
		self['F'] = operators

	def run(self, statement):
		model = convert(parse(statement))
		return call(self, model)