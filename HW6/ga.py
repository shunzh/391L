import copy

class Individual:
	"""
		Each individual is a list.
	"""
	def __init__(self, num):
		self.length = num

	def __getitem__(self,index):
		return self.elems[index]

	def __len__(self):
		return self.length

	def copy(self):
		return copy.deepcopy(self)

	def mutate(self):
		abstract


class Population:
	"""
		Population contains multiple of individuals
	"""
	CO_RATE = 0.5
	MU_RATE = 0.001

	def __init__(self, num, cate):
		"""
			num: number of individuals
			cate: class of individuals
		"""
		self.inds = [cate() for _ in xrange(num)]
		self.num = num

	def select(self, fitness):
		"""
			Evaluate all the individuals.
			The fitness is given.
		"""
		assert len(fitness) == self.num

		# normalize first if necessary
		if sum(fitness) != 1:
			fit_sum = sum(fitness)
			fitness = [fit / fit_sum for fit in fitness]

		# cumulative prob func
		cum_fitness = [fitness[0]]
		for i in range(1, self.num):
			cum_fitness[i] = cum_fitness[i - 1] + fitness[i]

		# regenerate the population
		new_inds = []
		for _ in xrange(self.num):
			rand = random.random()
			j = 0
			while j < self.num:
				if rand > cum_fitness[j]:
					j += 1
				else:
					break

			new_ind.append(self.inds[j].copy())

		# replace the current individuals
		self.inds = new_inds
	
	def crossover(self):
		"""
			Exchange CO_RATE of their elements.
		"""
		num = int(self.num * CO_RATE)
		for _ in xrange(num):
			i = random.randInt(0, self.num)
			j = random.randInt(0, self.num)
			self.crossoverInd(self.ind[i], self.ind[j])
		
	def mutate(self):
		"""
			Randomly change one element with prob of MU_RATE.
		"""
		for i in xrange(self.length):
			if random.random() < Population.MU_RATE:
				self.mutate(self.ind[i])

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

