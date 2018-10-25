
import abc
import random
from Pos import Pos


class Player(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self, healthCap, mob,posx,posy,index,game):
		self.MOBILITY = mob
		self.health = healthCap
		self.pos = Pos(posx,posy)
		self.index = index
		self.game = game

	@abc.abstractmethod
	def teleport(self):

		randx = random.randint(0, self.game.Dimension - 1)
		randy = random.randint(0, self.game.Dimension - 1)

		while(self.game.positionOccupied(randx,randy)):
			randx = random.randint(0, self.game.Dimension - 1)
			randy = random.randint(0, self.game.Dimension - 1)


		self.pos.setPos(randx,randy)


	def increaseHealth(self,h):
		self.health += h

	def decreaseHealth(self, h):	# BACK HERE
		self.health -= h
		if(self.health <= 0):
			self.myString = "C"+ self.myString[0]

	@abc.abstractmethod
	def askForMove(self):
		print "Yor health is %d. Your position is (%d,%d). Your mobility is %d."%(self.health, self.pos.x, self.pos.y, self.MOBILITY)

		print"You now have the following options: "
		print"1. Move"
		print"2. Attack"
		print"3. End the turn"

		a = input()

		if a==1:
			print"Specify your target position ( Input 'x y')."
			row,col = raw_input().split()
			row = int(row)
			col = int(col)

			if self.pos.distance1(row,col) > self.MOBILITY :
				print "Beyond your reach. Staying still."
			elif self.game.positionOccupied(row,col):
				print "Position occupied. Cannot move there."
			else:
				self.pos.setPos(row,col)
				self.game.printBoard()
				print"You can now\n1.attacj\n2.End the turn"
				a = input()
				if a ==1 :
					print"Input position to attack. (Input 'x y')"
					attx,atty = raw_input().split()
					attx = int(attx)
					atty = int(atty)
					self.equipment.action(attx,atty)
		elif a==2:
			print"Input position to attack. (Input 'x y')"
			attx,atty = raw_input().split()
			attx = int(attx)
			atty = int(atty)
			self.equipment.action(attx,atty)

		elif a==3:
			return



