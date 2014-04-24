
def evaluate(elems, pool):
	"""
		Evaluate the fitness of elems and pool
	"""
	for sample in pool:
		thisSample = sample[:]
		for elem in elems:
			sort(elem, thisSample)

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
