# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  explored = set()
  frontier = util.Stack()
  frontier.push(Node(problem.getStartState()))
  while True:
  	if frontier.isEmpty():
  		return False
  	current = frontier.pop()
  	if problem.isGoalState(current.state):
  		return current.actions
  	if current.state not in explored:
  		explored.add(current.state)
  		expanded = expansion(problem, current)
  		for node in expanded:
  			frontier.push(node)
  #print "Start: ", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  #print "Start's successors:", problem.getSuccessors(problem.getStartState())

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  if problem.isGoalState(problem.getStartState()):
  	return Node(problem.getStartState()).actions
  explored = set()
  frontier = util.PriorityQueue()
  root = Node(problem.getStartState())
  frontier.push(root, len(root.actions))
  while True:
  	if frontier.isEmpty():
  		return False
  	current = frontier.pop()
  	if problem.isGoalState(current.state):
  		return current.actions
  	if current.state not in explored:
  		explored.add(current.state)
  		expanded = expansion(problem, current)
  		for node in expanded:
  			frontier.push(node, len(node.actions))
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  if problem.isGoalState(problem.getStartState()):
  	return Node(problem.getStartState()).actions
  explored = set()
  frontier = util.PriorityQueue()
  root = Node(problem.getStartState())
  frontier.push(root, root.cost)
  while True:
  	if frontier.isEmpty():
  		return False
  	current = frontier.pop()
  	if problem.isGoalState(current.state):
  		return current.actions
  	if current.state not in explored:
  		explored.add(current.state)
  		expanded = expansion(problem, current)
  		for node in expanded:
  			frontier.push(node, node.cost)

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  if problem.isGoalState(problem.getStartState()):
  	return Node(problem.getStartState()).actions
  explored = set()
  frontier = util.PriorityQueue()
  root = Node(problem.getStartState())
  frontier.push(root, root.cost+heuristic(root.state, problem))
  while True:
  	if frontier.isEmpty():
  		return False
  	current = frontier.pop()
  	if problem.isGoalState(current.state):
  		return current.actions
  	if current.state not in explored:
  		explored.add(current.state)
  		expanded = expansion(problem, current)
  		for node in expanded:
  			frontier.push(node, node.cost+heuristic(node.state, problem))

# Custom stuff #
def expansion(problem, parent):
	"""
	Expands a Node.
	Parameters:
		problem: an instance of SearchProblem
		parent: the Node instance of the parent node
	Returns:
		children: a list of Node instances of the children nodes
	"""
	children = []
	successors = problem.getSuccessors(parent.state)
	for successor in successors:
		child = Node(successor[0])
		child.setActions(parent.actions+[successor[1]])
		child.setCost(parent.cost+successor[2])
		children.append(child)
	return children

class Node:
	"""
	A node in the game tree
	"""
	def __init__(self, state, actions=[], cost=0):
		self.actions = actions
		self.state = state
		self.cost = 0

	def setActions(self, actions):
		self.actions = actions[:]

	def setCost(self, cost):
		self.cost = cost

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
