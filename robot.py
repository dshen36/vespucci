# from enum import ENUM
class Robot:

	def __init__(self):
		# Instantiating initial values
		# IMPORTANT: this assumes that you are starting from the bottome left corner of the room
		self.canvas = [[None]]
		self.xCord = 0
		self.yCord = 0

	def updateMap(self, direction, isObstacle, isGoal):
		# Readability
		mapHeight = len(self.canvas)-1
		mapWidth = len(self.canvas[0])-1

		# Checking if you're venturing into unknown terrain
		if ((direction == Directions.DOWN and self.yCord == mapHeight) or
			(direction == Directions.RIGHT and self.xCord == mapWidth)):
			self.expandMap(direction)

		# If it's not an obstacle, then assume that the robot moved, otherwise the robot was stationary during that action
		if (not isObstacle):
			self.recordStep(direction, isGoal)
		else:
			self.recordObstacle(direction)

		self.prettyPrintCanvas()

		if (isGoal):
			self.comeBackHomeBaby()

	def expandMap(self, direction):
		if (direction == Directions.DOWN):
			rowSize = len(self.canvas[0])
			newRow = rowSize * [None]
			self.canvas.append(newRow)

		if (direction == Directions.RIGHT):
			for i in range(len(self.canvas)):
				self.canvas[i].append(None);

	def comeBackHomeBaby(self):
		print("surprise mofo")
		print("(%d,%d)" % (self.xCord, self.yCord))

		while not(self.xCord == 0 and self.yCord == 0):

			step = self.canvas[self.yCord][self.xCord]
			print(step.backTrack)
			self.updateStep(step.backTrack)
			print("(%d,%d)" % (self.xCord, self.yCord))

	def recordObstacle(self, direction):
		self.updateStep(direction)
		self.canvas[self.yCord][self.xCord] = Step(True, None, False)

		#really jank way of doing this but i'm too lazy to make it cleaner. woops
		self.updateStep(self.getOppositeDirection(direction))

	def recordStep(self, direction, isGoal):
		self.updateStep(direction)
		self.canvas[self.yCord][self.xCord] = Step(False, self.getOppositeDirection(direction), isGoal)

    # up and down are reversed since we're respecting that the 2d array mimics the 4th quadrant
	def updateStep(self, direction):
		if (direction == Directions.UP):
			self.yCord -= 1
		if (direction == Directions.DOWN):
			self.yCord += 1
		if (direction == Directions.RIGHT):
			self.xCord += 1
		if (direction == Directions.LEFT):
			self.xCord -= 1

	def getOppositeDirection(self, direction):
		if (direction == Directions.UP):
			return Directions.DOWN
		if (direction == Directions.DOWN):
			return Directions.UP
		if (direction == Directions.RIGHT):
			return Directions.LEFT
		if (direction == Directions.LEFT):
			return Directions.RIGHT


	def prettyPrintCanvas(self):
		print("\n~~~~~~~~~~~~~~~~~~~TBH this is pretty ugly~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		for row in range(len(self.canvas)):
			print #new line
			for col in range(len(self.canvas[0])):
				step = self.canvas[row][col]
				if (step is not None):
					if (step.backTrack == Directions.UP):
						print("^"),
					elif (step.backTrack == Directions.DOWN):
						print("v"),
					elif (step.backTrack == Directions.RIGHT):
						print(">"),
					elif (step.backTrack == Directions.LEFT):
						print("<"),
					else: 
						print("x"),
				else:
					print("*"),
				

class Step:
	def __init__(self, isObstacle, backTrack, isGoal):
		self.isObstacle = isObstacle
		self.backTrack = backTrack
		self.isGoal = isGoal

#TODO: make into enum
class Directions():
	UP = "UP"
	DOWN = "DOWN"
	LEFT = "LEFT"
	RIGHT = "RIGHT"

def main():
	r = Robot()
	r.updateMap("DOWN", False, False)
	r.updateMap("RIGHT", False, False)
	r.updateMap("RIGHT", True, False)
	r.updateMap("UP", False, False)
	r.updateMap("RIGHT", False, True)

if __name__ == '__main__':
    main()