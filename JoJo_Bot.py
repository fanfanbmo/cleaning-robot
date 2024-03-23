from Bot import *

class Bot961333(Bot):
	def __init__(self, settings):
		super().__init__(settings)
		self.setName('JoJo')
		self.is_on_track = True
		
	def nextMove(self, currentCell, currentEnergy, vision, remainingStainCells):
		#move down if there is a stain
		if vision[2][1] == "@" and self.is_on_track:
			self.is_on_track= False
			return DOWN
		#move back up after cleaned the stain
		elif currentCell[0]%3 == 0 and self.is_on_track == False:
			self.is_on_track = True
			return UP
		#move up if there is a stain
		elif vision[0][1] == "@":
			return UP
		#default move if there are no stains
		elif currentCell[0]%3 == 2 and currentCell[0]%2 == 0 and currentCell[1] < self.nrCols-2:
			return RIGHT
		elif currentCell[0]%3 == 2 and currentCell[0]%2 == 1 and currentCell[1] > 1:
			return LEFT
		#move to the left on the last row if the last row is not scanned
		elif vision[2][1] == "x" and currentCell[0]%2 == 0:
			return LEFT
		#move to the right on the last row if the last row is not scanned
		elif vision[2][1] == "x" and  currentCell[0]%2 == 1:
			return RIGHT
		#skip 2 rows or going back to track after cleaning 
		else:
			return DOWN
