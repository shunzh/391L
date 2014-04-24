import random
import ga

class SortNet(ga.Individual):
	"""
		Contain multiple sorting elements
	"""
	def __init__(self, maxrange, num):
		self.elems = [SortElem(maxrange) for _ in xrange(num)]
		self.maxrange = maxrange
		self.length = num
		
	def sort(self, l):
		"""
			Sort l using this sortnet
			l will be sorted (passed with reference)
		"""
		for elem in self.elems:
			i = elem[0]
			j = elem[1]

			assert len(l) > max(i, j)

			if (l[i] > l[j]):
				l[i], l[j] = l[j], l[i]
	
	def mutate(self):
		"""
			the i-th element
			j \in [0, 1], which is the first or second index
		"""
		i = random.randInt(0, self.length)
		j = random.randInt(0, 2)

		self[i][j] = random.randInt(0, self.maxrange)


class SortElem:
	"""
		One sorting element.
		Contain i and j, which are the indices that might be swapped.
	"""
	def __init__(self, maxrange):
		self.indices = [random.randint(0, maxrang), random.randint(0, maxrang)]

	def __getitem__(self,index):
		return self.indices[index]
