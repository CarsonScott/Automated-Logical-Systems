from Object import *
from Functions import *
from Operators import *
from Interpreter import *

class System(Interpreter):

	def __init__(self, operators):
		super().__init__(operators)
		self['statements'] = []

	def add_statement(self, statement):
		self['statements'].append(statement)

	def run(self):
		y = []
		for i in range(len(self['statements'])):
			y.append(self.call(self['statements'][i]))
		return y