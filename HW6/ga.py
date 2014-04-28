import copy
import random
import math

class Individual(object):
	"""
		Each individual is a list.
	"""
	def __getitem__(self, index):
		return self.elems[index]

	def __setitem__(self, index, value):
		self.elems[index] = value

	def __len__(self):
		return self.length

	def updateLength(self):
		self.length = len(self.elems)

	def copy(self):
		return copy.deepcopy(self)

	def mutate(self):
		abstract


class Population:
	"""
		Population contains multiple of individuals
	"""
	CO_RATE = 0.4
	MU_RATE = 0.01

	def __init__(self, num, cate, args):
		"""
			num: number of individuals
			cate: class of individuals
		"""
		self.inds = [cate(args) for _ in xrange(num)]
		self.num = num

	def __getitem__(self, index):
		return self.inds[index]

	def __setitem__(self, index, value):
		self.inds[index] = value

	def __len__(self):
		return self.num

	def select(self, fitness, exp=False):
		"""
			Evaluate all the individuals.
			The fitness is given.
		"""
		# An option: raise fitness to power of e
		if (exp):
			fitness = [math.exp(fit) for fit in fitness]

		fit_sum = sum(fitness)

		assert fit_sum != 0

		fitness = [fit / fit_sum for fit in fitness]

		# cumulative prob func
		cum_fitness = [0 for _ in xrange(self.num)]
		cum_fitness[0] = fitness[0]
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

			new_inds.append(self.inds[j].copy())

		# replace the current generation
		self.inds = new_inds
	
	def crossover(self):
		"""
			Exchange CO_RATE of their elements.
		"""
		num = int(self.num * Population.CO_RATE)
		for _ in xrange(num):
			i = random.randint(0, self.num-1)
			j = random.randint(0, self.num-1)
			self.crossoverInd(self.inds[i], self.inds[j])

			self.inds[i].updateLength()
			self.inds[j].updateLength()
		
	def mutate(self):
		"""
			Randomly change one element with prob of MU_RATE.
		"""
		for i in xrange(self.num):
			if random.random() < Population.MU_RATE:
				self.mutateInd(self.inds[i])

	"""
		Operation on individuals
	"""
	def crossoverInd(self, ind1, ind2):
		# Their lengths should be equal. Just make sure.
		half_1 = len(ind1) / 2
		half_2 = len(ind2) / 2

		# Exchange the first half
		ind1[ : half_1], ind2[ : half_2] = ind2[ : half_2], ind1[ : half_1] 

	def mutateInd(self, ind):
		"""
			Randomly change one element with prob of MU_RATE.
		"""
		ind.mutate()


def evaluate(sortnets, datas):
	"""
		Evalute the performance of each sortnet on each datum
		It creates a dictionary, with (sortnet_id, data_id) as key, its
		fitness as value.
		Return fitness for sortnet and datas as a tuple.
	"""
	def fitness(d):
		"""
			Return how sorted this data is, range in [0, 1]
			each i < j and d[i] < d[j] contributes 1 to this degree
		"""
		r = range(len(d))
		possiSum = len(d) * (len(d) - 1) / 2
		return 1.0 * sum([1 for i in r for j in r if i < j and d[i] <= d[j]]) / possiSum

	def getSortnetFit():
		"""
			Get fitness for Sortnet
		"""
		result_sort = []
		alist = []
		llist = []

		for i in range(len(sortnets)):
			a = avg([results[(i, j)] for j in range(len(datas))])
			l = len(sortnets[i])

			# compromise between accuracy and length
			result_sort.append(a + 1.0/l)

			# stats
			alist.append(a)
			llist.append(len(sortnets[i]))

		# for print
		opt_a = max(alist)
		ind_opt = alist.index(opt_a)
		opt_l = llist[ind_opt]
		sort = sortnets[ind_opt]

		print opt_a, opt_l
		print sort.display()

		return result_sort

	def getDataFit():
		"""
			Get fitness for Data
		"""
		result_data = []
		for j in range(len(datas)):
			o = avg([1 - results[(i, j)] for i in range(len(sortnets))])
			result_data.append(o)
		return result_data

	results = {}

	for i in range(len(sortnets)):
		for j in range(len(datas)):
			datum = datas[j].copy()
			sortnets[i].sort(datum)

			results[(i, j)] = fitness(datum)
	
	return [getSortnetFit(), getDataFit()]


# utility
def avg(l):
	return 1.0 * sum(l) / len(l)


def main():
	# length of numbers to sort
	length = 16
	# elements in a sortnet
	elemsNum = lambda : random.randint(length * (length / 2), length ** 2)
	#elemsNum = lambda : length ** 2

	# number of iterations for GA
	iterations = 200

	# init population
	import sortnet, data
	sort_args = {'length': length, 'elemsNum': elemsNum}
	sortnets = Population(500, sortnet.SortNet, sort_args)

	data_args = {'length': length}
	datas = Population(200, data.Data, data_args)

	for _ in xrange(iterations):
		result_sort, result_data = evaluate(sortnets, datas)

		sortnets.select(result_sort)
		datas.select(result_data)

		sortnets.crossover()
		datas.crossover()

		sortnets.mutate()
		datas.mutate()


if __name__ == '__main__':
	main()
