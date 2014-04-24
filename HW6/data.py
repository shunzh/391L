import random
import ga

class Data(ga.Individual):
	"""
		A sequence of numbers
	"""
	def __init__(self, args):
		self.length = args['length']

		self.elems = range(self.length)
		random.shuffle(self.nums)
	
	def mutate(self):
		"""
			Randomly swap two numbers
		"""
		i = random.randInt(0, self.length)
		j = random.randInt(0, self.length)

		self[i], self[j] = self[j], self[i]
