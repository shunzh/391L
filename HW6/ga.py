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


def evaluate(sortnets, data):
	"""
		Evalute the performance of each sortnet on each datum
		Return fitness for sortnet and data, respectively
	"""
	for i in range(len(sortnest)):
		for j in range(len(data)):
			thisDatum = data[j].copy()
			sortnet[i].sort(thisDatum)

			results[(i, j)] = fitness(thisDatum)
	
	result_sort = []
	for i in range(len(sortnest)):
		result_sort.append(avg([result(i, j) for j in range(len(data))]))

	result_data = []
	for j in range(len(data)):
		result_data.append(avg([1 - result(i, j) for i in range(len(sortnest))]))

	return [result_sort, result_data]


def fitness(d):
	"""
		Return how sorted this data is, range in [0, 1]
		each i < j and d[i] < d[j] contributes 1 to this degree
	"""
	r = range(len(d))
	possiSum = len(d) * (len(d) - 1) / 2
	return 1.0 * sum([1 for i in r for j in r if i < j and d[i] <= d[j]]) / possiSum


# utility
def avg(l):
	return 1.0 * sum(l) / len(l)


def main():
	# length of numbers to sort
	length = 10
	# elements in a sortnet
	elemsNum = 50
	# population size 
	size = 100

	# init population
	import sortnet, data
	sort_args = {'length': length, 'elemsNum': elemsNum}
	sortnets = Population(size, sortnet.SortNet, sort_args)

	data_args = {'length': length}
	datas = Population(size, data.Data, data_args)

	for _ in xrange(iterations):
		result_sort, result_data = evaluate(sortnets, datas)

		sortnets.select(results_sort)
		datas.select(results_data)

		sortnets.crossover()
		datas.crossover()

		sortnets.mutate()
		datas.mutate()


if __name__ == '__main__':
	main()
