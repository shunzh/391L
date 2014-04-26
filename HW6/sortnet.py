import random
import ga

class SortNet(ga.Individual):
	"""
		Contain multiple sorting elements
	"""
	def __init__(self, args):
		"""
			maxindex is the largest index in data
			elemsNum is a FUNCTION that returns the number of elems in this
			network. call once.
		"""
		self.maxindex = args['length']

		num = args['elemsNum']
		self.length = num()

		self.elems = [SortElem(self.maxindex) for _ in xrange(self.length)]

	def display(self):
		return [elem.indices for elem in self.elems]

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
		def randomChange():
			# change one number in sortnet randomly
			i = random.randint(0, self.length-1)
			j = random.randint(0, 1)

			self[i][j] = random.randint(0, self.maxindex-1)

		def randomAppend():
			# add three random pairs to sortnet
			self.length += 3

			for _ in xrange(3):
				self.elems.append(SortElem(self.maxindex))

		if random.random() < 0.5:
			randomChange()
		else:
			pass
			#randomAppend()


class SortElem:
	"""
		One sorting element.
		Contain i and j, which are the indices that might be swapped.
	"""
	def __init__(self, maxindex):
		self.indices = [random.randint(0, maxindex-1), random.randint(0, maxindex-1)]

	def __getitem__(self, index):
		return self.indices[index]

	def __setitem__(self, index, value):
		self.indices[index] = value
