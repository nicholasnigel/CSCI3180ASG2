import abc
from Player import Player 
from Axe import Axe

class Chark(Player):
	def __init__(self,posx,posy,index,game):
		super(Chark,self).__init__(100,4,posx,posy,index,game)
		self.Symbol = "C"
		self.myString = "C" + str(index)
		self.equipment = Axe(self)

	def teleport(self):
		super(Chark,self).teleport()
		self.equipment.enhance()

	def askForMove(self):
		print"You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)" % (self.index , self.equipment.ranges,self.equipment.effect)
		super(Chark,self).askForMove()