import abc
from Weapon import Weapon
import subprocess
import time

class Rifle(Weapon):
	RIFLE_RANGE = 4
	RIFLE_INIT_DAMAGE = 10
	AMMO_LIMIT = 6

	AMMO_RECHARGE = 3

	def __init__(self, owner):
		super(Rifle,self).__init__(Rifle.RIFLE_RANGE,Rifle.RIFLE_INIT_DAMAGE,owner)
		self.ammo=Rifle.AMMO_LIMIT

	def enhance(self):
		self.ammo = min(Rifle.AMMO_LIMIT, self.ammo + Rifle.AMMO_RECHARGE)


	def action(self,posx,posy):
		print"You are using rifle attacking %d %d." %(posx,posy)

		ammoToUse = input("Type how many ammos you want to use. ")

		if(ammoToUse > self.ammo):
			print"You don't have that ammos"
			return

		if(self.owner.pos.distance1(posx,posy)<= self.ranges):
			player = self.owner.game.getPlayer(posx,posy)
			if player != None :

				if type(player) is type(self.owner):
					print "DONT KILL HIM PLEASE, HE'S YOUR OWN BROTHER"

				else: 
					subprocess.call(["afplay","gunshot.wav"])
					player.decreaseHealth(self.effect * ammoToUse)
					for i in range(ammoToUse):
						self.ammo-= ammoToUse
					

		else:
				print"Out of reach."


