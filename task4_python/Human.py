import abc
from Player import Player
from Rifle import Rifle
from Wand import Wand

class Human(Player):

	def __init__(self,posx,posy,index,game):
		super(Human,self).__init__(80,2,posx,posy,index,game)

		self.myString = 'H' + str(index)
		self.Symbol = "H"
		if index == (self.game.n/2) - 1:
			self.equipment = Wand(self)
		else:
			self.equipment = Rifle(self)

	def teleport(self):
		super(Human,self).teleport()
		self.equipment.enhance()

	def askForMove(self):
		

		if type(self.equipment) is  Rifle:
			print"You are a human (H%d) using Rifle.(Range %d, Ammo #: %d, Damage per shot: %d)" %(self.index,self.equipment.ranges, self.equipment.ammo,self.equipment.effect)
		if type(self.equipment) is Wand:
		 	print"You are a human (H%d) using Wand. (Range: %d, heal: %d)" % (self.index , self.equipment.ranges,self.equipment.effect)
		super(Human , self).askForMove()
