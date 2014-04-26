import random
import ga

class Data(ga.Individual):
	"""
		A sequence of numbers
	"""
	def __init__(self, args):
		self.length = args['length']

		self.elems = [random.randint(0, 10000) for _ in xrange(self.length)]
	
	def mutate(self):
		"""
			Randomly swap two numbers
		"""
		i = random.randint(0, self.length-1)
		j = random.randint(0, self.length-1)

		self[i], self[j] = self[j], self[i]
