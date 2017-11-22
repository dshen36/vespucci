class Robot:

	def __init__(self, name):
		# Instantiating initial values
		# IMPORTANT: this assumes that you are starting from the bottome left corner of the room
		self.canvas = [[]]
		self.xCord = 0
		self.yCord = 0

	def draw(self):

	def updateMap(self, direction, isObstacle, isGoal):

		mapHeight = len(self.canvas)-1
		mapWidth = len(self.canvas[0])-1
		if ((direction == UP && yCord == mapHeight) ||
			(direction == RIGHT && xCord = mapWidth)):
			expandMap()

		# If it's not an obstacle, then assume that the robot moved, otherwise the robot was stationary during that action
		if (!isObstacle):
			recordStep(self, direction)

		self.canvas[self.yCord][self.xCord] = Step(isObstacle,getOppositeDirection(direction), isGoal)
		
	def expandMap(self):
		# something along this line
		for i in len(data):
		  myList = [] + myList
		  for k in len(data):
		    if (true conditional):
		      myList[i].append(k)

	def recordStep(self, direction):
		if (direction == UP):
			self.yCord += 1
		if (direction == DOWN):
			self.yCord -= 1
		if (direction == RIGHT):
			self.xCord += 1
		if (direction == LEFT):
			self.xCord -= 1

	def getOppositeDirection(self, direction):
		if (direction == UP):
			return DOWN
		if (direction == DOWN):
			return UP
		if (direction == RIGHT):
			return LEFT
		if (direction == LEFT):
			return RIGHT

class Step:
	def __init__(self, isObstacle, backTrack, isGoal):
		self.isObstacle = isObstacle
		self.backTrack = backTrack
		self.isGoal = isGoal