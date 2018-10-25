import random
import sys

	


#Class player:

class Player(object):
	


	def __init__(self, healthCap, mob, posx, posy, index, game):
		self.mobility=mob
		self.health=healthCap
		self.pos = # create object pos
		self.index=index
		self.game = game

	#def getpos should just be replaced with accessing the atttributes directly

	def teleport(self):
		#java rand.nexint is from 0 to the parameter (exclusively)
		randx = rand.randint(0,SurvivalGame.Dimension-1)#-1 because you 
		randy = rand.randint(0,SurvivalGame.Dimension-1)









#Class Survival Game:

class SurvivalGame(object):
	#initialize as class attribute
	n=0 
	Dimension=10
	Obstacle=2

	def __init__(self):
		print "Welcome to Kafustrok. Light blesses you."
		SurvivalGame.n = input("Input number of players: (an even number) ")

		self.teleportObjects= [0 for x in range(SurvivalGame.n + SurvivalGame.Obstacle)]
		

		#should create n/2 humans

		for i in range(SurvivalGame.n /2):
			self.teleportObjects[i] = Human(0,0,i,game)
			self.teleportObjects[i + n/2]= Chark(0,0,i,game)

		for i in range(SurvivalGame.Obstacle):
			self.teleportObjects[i+SurvivalGame.n] = Obstacle(0,0,i,game)

	
	def printBoard(self):
		#initialize to spaces
		printObject = [[" " for x in SurvivalGame.Dimension] for y in SurvivalGame.Dimension]

		for i in range(SurvivalGame.n):
			pos = self.teleportObjects[i].pos
			printObject[pos.X][pos.Y]= "O" + str(i - SurvivalGame.n)

		sys.stdout.write(" ")
		for i in range(SurvivalGame.Dimension):
			sys.stdout.write("| %d  " % i)
		sys.stdout.write("|")
		sys.stdout.flush()
		print(" ")

		print "-"*55

		for row in range(SurvivalGame.Dimension):
			sys.stdout.write("%d" % row)
			for col in range(SurvivalGame.Dimension):
				sys.stdout.write("| %s "%printObject[row][col])
			sys.stdout.write("|")
			sys.stdout.flush()
			print(" ")
			print"-"*55

	def positionOccupied(self,randx,randy):

		for obj in self.teleportObjects:
			if isinstance(obj,Player):
				pos = obj.pos
				if pos.X == randx and pos.Y == randy:
					return True
			else:
				pos = obj.pos
				if pos.X == randx and pos.Y == randy:
					return True
		return False


	def getPlayer(self):#return Player:


	def gameStart(self):
		turn=0
		numOfAlivePlayers = SurvivalGame.n
		while numOfAlivePlayers > 1:
			if turn == 0:
				for obj in self.teleportObjects:
					if isinstance(obj,Human):
						obj.teleport()
					elif isinstance(obj, Chark):
						obj.teleport()
					elif isinstance(obj, Obstacle):
						obj.teleport()
				print("Everything gets teleported..")
			self.printBoard()
			t = 
			








game=SurvivalGame()


