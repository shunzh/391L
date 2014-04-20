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

def getQFuncs():
	obstacle = {'bias': -0.20931133310480204, 'dis': 0.06742681562641269}
	sidewalk = {'x': 0.06250000371801567}
