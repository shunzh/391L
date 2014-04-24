import random

class SortNet:
	"""
		Contain multiple sorting elements
	"""
	CO_RATE = 0.5
	MU_RATE = 0.001

	def __init__(self, maxrange, num):
		self.elems = [SortElem(maxrange) for _ in xrange(num)]
		self.maxrange = maxrange
		self.length = num
		
	def __getitem__(self,index):
		return self.elems[index]

	def __len__(self):
		return self.length

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
	
	@staticmethod
	def crossover(net1, net2):
		"""
			Exchange CO_RATE of their elements
		"""
		# Their lengths should be equal. Just make sure.
		num = min(len(net1), len(net2))
		co_num = int(num * SortNet.CO_RATE)

		for _ in xrange(num):
			idx = random.randInt(0, num)

			# swap them
			net1[idx], net2[idx] = net2[idx], net1[idx]

	def mutate(self):
		"""
			Randomly change one element with prob. of MU_RATE
		"""
		for i in range(self.length):
			for j in range(2):
				# with this probability
				if random.random() < SortNet.MU_RATE:
					# the i-th element
					# j \in [0, 1], which is the first or second index
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
