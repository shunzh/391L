from qlearningAgents import ApproximateQAgent 

class ModularAgent(ApproximateQAgent):
	def __init__(self, **args):
		ApproximateQAgent.__init__(self, **args)

		# a set of q functions
		self.qFuncs = args['qfunc']
 
	def getQValue(self, state, action):
		"""
			Get Q value by consulting each module
		"""
		qValues = []
		for qFunc in self.qFuncs:
			qValues.append(qFunc(state, action))

		# FIXME
		return sum(qValues)
