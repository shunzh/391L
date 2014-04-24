class Individual:
	"""
		Each individual is a list.
	"""
	def __getitem__(self,index):
		return self.elems[index]

	def __len__(self):
		return self.length

	def mutate(self):
		abstract


class Population:
	def select(self, fitness):
		"""
			Evaluate all the individuals.
			The fitness is given.
		"""
	
	def crossover(self, ind1, ind2):
		"""
			Exchange CO_RATE of their elements.
		"""
		# Their lengths should be equal. Just make sure.
		num = min(len(ind1), len(ind2))
		co_num = int(num * Population.CO_RATE)

		for _ in xrange(num):
			idx = random.randInt(0, num)

			# swap them
			ind1[idx], ind2[idx] = ind2[idx], ind1[idx]

	def mutate(self, ind):
		"""
			Randomly change one element with prob of MU_RATE.
		"""
		if random.random() < SortNet.MU_RATE:
			ind.mutate()


def main():
	# length of numbers to sort
	length = 10
	# 
	elemnum = 30
	sortnets = [SortNet(length, elemnum) for _ in xrange(
