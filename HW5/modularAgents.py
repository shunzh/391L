from qlearningAgents import ApproximateQAgent
from game import Actions
import util

import math

class ModularAgent(ApproximateQAgent):
	def __init__(self, **args):
		ApproximateQAgent.__init__(self, **args)

		self.qTable = util.Counter()
 
	def getQValue(self, state, action):
		"""
			Get Q value by consulting each module
			If idx indicated, then only return qvalue for that qFunc
		"""
		"""
		qValues = []
		for qFunc in self.qFuncs:
			qValues.append(qFunc(state, action))

		return 0.6 * qValues[0] + 0.4 * qValues[1]
		"""
		return self.qTable[(state, action)]
	
	def setQFuncs(self, qFuncs):
		"""
			Must set QFuncs here. getQValue will use this.
		"""
		self.qFuncs = qFuncs
	
	def getPolicy(self, state):
		"""
			Can toggle between using QValue directly (traditional way)
			or by proportion of exp(QValue)
		"""
		#return ApproximateQAgent.getPolicy(self, state)
		return self.getGibbsPolicy(state)
	
	def getGibbsPolicy(self, state):
		"""
			Rather than using QValue, use proportion of exp(QValue)
		"""
		actions = self.getLegalActions(state)
		if actions: 
			vMat = []
			for idx in range(len(self.qFuncs)):
				qFunc = lambda action: self.qFuncs[idx](state, action)
				# list of exp^q
				exps = [math.exp(qFunc(action)) for action in actions]
				# Normalize
				sumExps = sum(exps)
				vMat.append([exp / sumExps for exp in exps])

			values = [(vMat[0][j] + vMat[1][j]) for j in range(len(actions))]
			for i in range(len(actions)):
				self.qTable[(state, actions[i])] = values[i]

			return actions[values.index(max(values))]
		else:
			return None


def getObsAvoidFuncs(mdp):
	"""
		Return Q functiosn for modular mdp for obstacle avoidance behavior

		the environment is passed by mdp
	"""
	obstacle = {'bias': -0.20931133310480204, 'dis': 0.06742681562641269}
	sidewalk = {'x': 0.06250000371801567}

	def getNext(state, action):
		x, y = state
		dx, dy = Actions.directionToVector(action)
		next_x, next_y = int(x + dx), int(y + dy)
		if next_x < 0 or next_x >= mdp.grid.width:
			next_x = x
		if next_y < 0 or next_y >= mdp.grid.height:
			next_y = y

		return [next_x, next_y]

	def qWalk(state, action):
		"""
			QValue of forward walking
		"""
		next_x, next_y = getNext(state, action)
		return sidewalk['x'] * next_x

	def qObstacle(state, action):
		"""
			QValue of obstacle avoiding
		"""
		x, y = state
		next_x, next_y = getNext(state, action)

		# find the distance to the nearest obstacle
		minDist = mdp.grid.width * mdp.grid.height
		for xt in range(mdp.grid.width):
			for yt in range(mdp.grid.height):
				cell = mdp.grid[xt][yt] 
				if (type(cell) == int or type(cell) == float) and cell < 0:
					# it's an obstacle!
					dist = math.sqrt((xt - next_x) ** 2 + (yt - next_y) ** 2)
					if (dist < minDist): minDist = dist
		return minDist * obstacle['dis'] + 1 * obstacle['bias']

	return [qWalk, qObstacle]
