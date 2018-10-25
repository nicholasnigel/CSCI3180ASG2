
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
		self.healthCap = healthCap

	@abc.abstractmethod
	def teleport(self):

		randx = random.randint(0, self.game.Dimension - 1)
		randy = random.randint(0, self.game.Dimension - 1)

		while(self.game.positionOccupied(randx,randy)):
			randx = random.randint(0, self.game.Dimension - 1)
			randy = random.randint(0, self.game.Dimension - 1)


		self.pos.setPos(randx,randy)


	def increaseHealth(self,h):
		previousHealth = self.health
		self.health += h
		if self.health > self.healthCap :
			self.health = self.healthCap
		if self.health > 0 :
			self.myString = self.Symbol + str(self.index)
		print self.myString +"'s Health increased from", previousHealth, "to", self.health
		if previousHealth<=0 and self.health>0:
			print"REVIVED"



	def decreaseHealth(self, h):	# BACK HERE
		previousHealth = self.health
		self.health -= h
		if(self.health <= 0):
			self.myString = "C"+ self.myString[0]
		print self.myString +"'s Health is reduced from", previousHealth ,"to",self.health

	@abc.abstractmethod
	def askForMove(self):
		print "Yor health is %d. Your position is (%d,%d). Your mobility is %d."%(self.health, self.pos.x, self.pos.y, self.MOBILITY)

		print"You now have the following options: "
		print"1. Move"
		if self.index == (self.game.n/2)-1:
			print"2. Heal"
		else:
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
				

				if self.index == (self.game.n/2)-1:
					print"You can now\n1.heal\n2.End the turn"
				else: 
					print"You can now\n1.attack\n2.End the turn"
				a = input()
				if a ==1 :
					if self.index == (self.game.n/2)-1:
						print "Input position to heal. (Input 'x y')"
					else:
						print"Input position to attack. (Input 'x y')"
					attx,atty = raw_input().split()
					attx = int(attx)
					atty = int(atty)
					self.equipment.action(attx,atty)
		elif a==2:
			if self.index == (self.game.n/2)-1:
				print "Input position to heal. (Input 'x y')"

			else: 
				print"Input position to attack. (Input 'x y')"
			attx,atty = raw_input().split()
			attx = int(attx)
			atty = int(atty)
			self.equipment.action(attx,atty)

		elif a==3:
			return



