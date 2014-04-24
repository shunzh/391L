import random

class Data(ga.Individual):
	"""
		A sequence of numbers
	"""
	def __init__(self, length):
		self.elems = range(length)
		random.shuffle(self.nums)
	
	def mutate(self):
		"""
			Randomly swap two numbers
		"""


def degreeSorted(d):
	"""
		Return how sorted this data is.
		each i < j and d[i] < d[j] contributes 1 to this degree
	"""
	r = range(len(d))
	return sum([1 for i in r for j in r if i < j and d[i] < d[j]])

