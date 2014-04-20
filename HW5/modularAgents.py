from qlearningAgents import ApproximateQAgent 

class ModularAgent(ApproximateQAgent):
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    self.weights = util.Counter()
 
  def getQValue(self, state, action):
