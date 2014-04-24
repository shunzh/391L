import random

class Data:
	"""
		A sequence of numbers
	"""
	def __init__(self, length):
		self.nums = range(length)
		random.shuffle(self.nums)
	
	@staticmethod
	def degreeSorted(d):
		"""
			Return how sorted this data is.
			each i < j and d[i] < d[j] contributes 1 to this degree
		"""
		r = range(len(d))
		return sum([1 for i in r for j in r if i < j and d[i] < d[j]])
