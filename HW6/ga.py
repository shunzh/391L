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
	"""
		Population contains multiple of individuals
	"""
	CO_RATE = 0.5
	MU_RATE = 0.001

	def select(self, fitness):
		"""
			Evaluate all the individuals.
			The fitness is given.
		"""
	
	def crossover(self):
		"""
			Exchange CO_RATE of their elements.
		"""
		num = int(self.length * CO_RATE)
		for _ in xrange(num):
			i = random.randInt(0, self.length)
			j = random.randInt(0, self.length)
			self.crossoverInd(
		
	def mutate(self):
		"""
			Randomly change one element with prob of MU_RATE.
		"""
		for i in xrange(self.length):
			if random.random() < Population.MU_RATE:
				self.mutate(self.elems[i])

	def crossoverInd(self, ind1, ind2):
		# Their lengths should be equal. Just make sure.
		num = min(len(ind1), len(ind2))
		co_num = int(num / 2)

		for _ in xrange(num):
			idx = random.randInt(0, num)

			# swap them
			ind1[idx], ind2[idx] = ind2[idx], ind1[idx]

	def mutateInd(self, ind):
		"""
			Randomly change one element with prob of MU_RATE.
		"""
		ind.mutate()


def main():
	# length of numbers to sort
	length = 10
	# n 
	elemnum = 30

	for _ in xrange(iterations):
		results = evaluate(sortnets, inputs)

		sortnets.select(results)
		inputs.select(results)

		sortnets.crossover()
		inputs.crossover()

		sortnets.mutate()
		inputs.mutate()

