# Maze for modular RL
class Maze():
	"""
		A general maze with sizes and positions of obstacles specified
	"""
	def __init__(self, grids):
		assert grids != None
		assert len(grids) > 1
		assert len(grids[0]) > 1

		self.grids = grids
		self.height = len(grids)
		self.width = len(grids[0])
	
	def getState(self, state):
		"""
			Identical mapping from state in the environment to the state
			for the learning agent by default
		"""
		return state
	
	def getNextState(self, state, action):
		"""
			Return the effect of taking an action
		"""

class ObstacleMaze(Maze):
	"""
		Maze for training obstacle avoiding behavior
	"""
	def __init__(self):
		grids = [[0, 0, 0, 0, 0],
		         [0, 0, 0, 0, 0],
		         [0, 0, -1, 0, 0],
		         [0, 0, 0, 0, 0],
		         [0, 0, 0, 0, 0]]
		Maze.__init__(self, grids)
	
	def getState(self, state):
		return (state[1] - 2, state[2] - 2)

class SideWayMaze(Maze):
	"""
		Maze for training reaching destinations
	"""
	def __init__(self, m, n):
		"""
			Maze has the size of m x n
		"""
		grids = [[0 for x in xrange(n)] for x in xrange(m)] 

		for i in xrange(m):
			# reward of reaching the goal
			grids[i][n - 1] = 1

		Maze.__init__(self, grids)
	
	def getState(self, state):
		return state[2]
