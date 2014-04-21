from qlearningAgents import ApproximateQAgent 
from game import Actions

import math

class ModularAgent(ApproximateQAgent):
	def __init__(self, **args):
		ApproximateQAgent.__init__(self, **args)
 
	def getQValue(self, state, action):
		"""
			Get Q value by consulting each module
		"""
		qValues = self.qFuncs(state, action)

		return 0.6 * qValues[0] + 0.4 * qValues[1]
	
	def setQFuncs(self, qFuncs):
		"""
			Must set QFuncs here. getQValue will use this.
		"""
		self.qFuncs = qFuncs

def getObsAvoidFuncs(mdp):
	"""
		Return Q functiosn for modular mdp for obstacle avoidance behavior

		the environment is passed by mdp
	"""
	obstacle = {'bias': -0.20931133310480204, 'dis': 0.06742681562641269}
	sidewalk = {'x': 0.06250000371801567}

	def qValues(state, action):
		x, y = state
		dx, dy = Actions.directionToVector(action)
		next_x, next_y = int(x + dx), int(y + dy)

		# forward walking
		qWalk = sidewalk['x'] * next_x

		# obstacle avoiding
		# find the distance to the nearest obstacle
		minDist = mdp.grid.width * mdp.grid.height
		for xt in range(mdp.grid.width):
			for yt in range(mdp.grid.height):
				cell = mdp.grid[xt][yt] 
				if (type(cell) == int or type(cell) == float) and cell < 0:
					# it's an obstacle!
					dist = math.sqrt((xt - next_x) ** 2 + (yt - next_y) ** 2)
					if (dist < minDist): minDist = dist
		qObstacle = minDist * obstacle['dis'] + 1 * obstacle['bias']

		return [qWalk, qObstacle]

	return qValues
