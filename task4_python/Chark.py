import abc
from Player import Player 
from Axe import Axe
from Wand import Wand

class Chark(Player):
	def __init__(self,posx,posy,index,game):
		super(Chark,self).__init__(100,4,posx,posy,index,game)

		self.myString = "C" + str(index)
		self.Symbol = "C"
		if index == (self.game.n/2) - 1:
			self.equipment = Wand(self)
		else:
			self.equipment = Axe(self)

	def teleport(self):
		super(Chark,self).teleport()
		self.equipment.enhance()

	def askForMove(self):
		

		if type(self.equipment) is Axe:
			print"You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)" % (self.index , self.equipment.ranges,self.equipment.effect)
		
		elif type(self.equipment)is Wand:
			print"You are a Chark (C%d) using Wand. (Range: %d, Heal: %d)" % (self.index , self.equipment.ranges,self.equipment.effect)

		super(Chark,self).askForMove()