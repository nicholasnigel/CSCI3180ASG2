import abc
from Player import Player
from Rifle import Rifle

class Human(Player):

	def __init__(self,posx,posy,index,game):
		super(Human,self).__init__(80,2,posx,posy,index,game)

		self.myString = 'H' + str(index)
		self.symbol = "H"
		self.equipment = Rifle(self)

	def teleport(self):
		super(Human,self).teleport()
		self.equipment.enhance()

	def askForMove(self):
		print"You are a human (H%d) using Rifle.(Range %d, Ammo #: %d, Damage per shot: %d)" %(self.index,self.equipment.ranges, self.equipment.ammo,self.equipment.effect)

		super(Human , self).askForMove()
