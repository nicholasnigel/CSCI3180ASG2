import abc
from Weapon import Weapon

class Axe(Weapon):
	AXE_RANGE = 1
	AXE_INIT_DAMAGE = 40

	def __init__(self,owner):
		super(Axe,self).__init__(Axe.AXE_RANGE,Axe.AXE_INIT_DAMAGE,owner)

	def enhance(self):
		self.effect += 10

	def action(self, posx, posy):
		print"You are using axe attacking %d %d." %(posx,posy)

		if self.owner.pos.distance1(posx,posy)<= self.ranges:
			player = self.owner.game.getPlayer(posx,posy)
			if player != None :
				player.decreaseHealth(self.effect)
				
		else:
			print"Out of reach."