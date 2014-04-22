import util

def sort(elem, l):
	"""
		Basic sort function, sort two elements in l.
		elem gives the indices.
	"""
	i = elem[0]
	j = elem[1]

	assert len(l) > max(i, j)

	if (l[i] > l[j]):
		l[i], l[j] = l[j], l[i]

def evaluate(elems, pool):
	"""
		Evaluate the fitness of elems and pool
	"""
	for sample in pool:
		for elem in elems:
			sort(elem, sample)


def fitness(elems, pool):
	"""
		Fitness of given elements on the pool of inputs
	"""
	def length():
		"""
			Shorter length has more fitness
		"""
		return 1 / len(elems)
	
	testLog = evaluate(elems, pool)
