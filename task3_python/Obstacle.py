import random
import abc
from Pos import Pos

class Obstacle(object):

	def __init__(self,posx,posy,index,game):
		self.pos = Pos(posx, posy)
		self.index = index
		self.game = game

	def teleport(self):
		randx = random.randint(0, self.game.Dimension -1)
		randy = self.game.Dimension - randx - 1

		while self.game.positionOccupied(randx, randy):
			randx = random.randint(0, self.game.Dimension -1)
			randy = self.game.Dimension - randx - 1

		self.pos.setPos(randx,randy)