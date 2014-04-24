import random
import ga

class Data(ga.Individual):
	"""
		A sequence of numbers
	"""
	def __init__(self, args):
		self.length = args['length']

		self.elems = range(self.length)
		random.shuffle(self.elems)
	
	def mutate(self):
		"""
			Randomly swap two numbers
		"""
		i = random.randint(0, self.length-1)
		j = random.randint(0, self.length-1)

		self[i], self[j] = self[j], self[i]
