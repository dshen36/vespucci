# from enum import ENUM
class Robot:

	def __init__(self):
		# Instantiating initial values
		# IMPORTANT: this assumes that you are starting from the bottome left corner of the room
		self.canvas = [[None]]
		self.xCord = 0
		self.yCord = 0

	# def draw(self):

	def updateMap(self, direction, isObstacle, isGoal):

		mapHeight = len(self.canvas)-1
		mapWidth = len(self.canvas[0])-1
		if ((direction == Directions.DOWN and self.yCord == mapHeight) or
			(direction == Directions.RIGHT and self.xCord == mapWidth)):
			self.expandMap(direction)

		# If it's not an obstacle, then assume that the robot moved, otherwise the robot was stationary during that action
		if (not isObstacle):
			self.recordStep(direction)

		self.canvas[self.yCord][self.xCord] = Step(isObstacle, self.getOppositeDirection(direction), isGoal)
		print(self.canvas)

	def expandMap(self, direction):
		
		if (direction == Directions.DOWN):
			rowSize = len(self.canvas[0])
			newRow = rowSize * [None]
			self.canvas.append(newRow)

		if (direction == Directions.RIGHT):
			for i in range(len(self.canvas)):
				self.canvas[i].append(None);
		      
		print("expanding!")

    # up and down are reversed since we're respecting that the 2d array mimics the 4th quadrant
	def recordStep(self, direction):
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

class Step:
	def __init__(self, isObstacle, backTrack, isGoal):
		self.isObstacle = isObstacle
		self.backTrack = backTrack
		self.isGoal = isGoal

class Directions():
	UP = "UP"
	DOWN = "DOWN"
	LEFT = "LEFT"
	RIGHT = "RIGHT"



def main():
	r = Robot()
	r.updateMap("DOWN", False, False)
	r.updateMap("RIGHT", False, False)
	r.updateMap("UP", False, False)
	r.updateMap("RIGHT", False, False)


	print("hi!")



if __name__ == '__main__':
    main()