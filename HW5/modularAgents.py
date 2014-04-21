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
				cell = self.grid[xt][yt] 
				if (type(cell) == int or type(cell) == float) and cell < 0:
					# it's an obstacle!
					dist = math.sqrt((xt - next_x) ** 2 + (yt - next_y) ** 2)
					if (dist < minDist): minDist = dist
		qObstacle = minDist * obstacle['dis'] + 1 * obstacle['bias']

		return [qWalk, qObstacle]

	return qValues
