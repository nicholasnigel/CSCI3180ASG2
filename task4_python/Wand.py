from Weapon import Weapon

class Wand(Weapon):
	WAND_RANGE = 5
	WAND_INIT_HEAL = 10

	def __init__(self,owner):
		super(Wand, self).__init__(Wand.WAND_RANGE, Wand.WAND_INIT_HEAL, owner)

	def enhance(self):
		self.effect +=5

	def action(self, posx, posy):
		print"You are using wand healing %d %d." %(posx,posy)

		if self.owner.pos.distance1(posx,posy)<= self.ranges:
			player = self.owner.game.getPlayer(posx,posy)
			
			if player != None :
		
				
				if type(player)is type(self.owner):
					
					player.increaseHealth(self.effect)
					print "You have healed %s for %d" %(player.myString , self.effect)
				else:
					print"The target you're healing is not of the same race"
				
		else:
			print"Out of reach."

