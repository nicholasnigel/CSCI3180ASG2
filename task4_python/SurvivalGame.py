""""
		    /*
		    * CSCI3180 Principles of Programming Languages
		    *
		    * --- Declaration ---
		    *
		    * I declare that the assignment here submitted is original except for source
		    * material explicitly acknowledged. I also acknowledge that I am aware of
		    * University policy and regulations on honesty in academic work, and of the
		    * disciplinary guidelines and procedures applicable to breaches of such policy
		    * and regulations, as contained in the website
		    * http://www.cuhk.edu.hk/policy/academichonesty/
		    *
		    * Assignment 2
		    * Name : Nigel Nicholas
		    * Student ID : 1155088791
		    * Email Addr : nigel7@cse.cuhk.edu.hk
		    */

"""

import random
import sys
from Player import Player
from Weapon import Weapon
from Obstacle import Obstacle
from Pos import Pos
from Human import Human
from Chark import Chark
from Rifle import Rifle
from Axe import Axe


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
			self.teleportObjects[i] = Human(0,0,i,self)
			self.teleportObjects[i + SurvivalGame.n/2]= Chark(0,0,i,self)

		for i in range(SurvivalGame.Obstacle):
			self.teleportObjects[i+SurvivalGame.n] = Obstacle(0,0,i,self)

	
	def printBoard(self):
		#initialize to spaces
		printObject = [["  "for x in range(SurvivalGame.Dimension)] for y in range(SurvivalGame.Dimension)]

		#getting player:
		 

		for i in range(SurvivalGame.n):
			pos = self.teleportObjects[i].pos
			printObject[pos.x][pos.y]= self.teleportObjects[i].myString

		for i in range(SurvivalGame.n , SurvivalGame.n + SurvivalGame.Obstacle):
			pos = self.teleportObjects[i].pos
			printObject[pos.x][pos.y]= "O" + str(i - SurvivalGame.n)

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
				if pos.x == randx and pos.y == randy:
					return True
			else:
				pos = obj.pos
				if pos.x == randx and pos.y == randy:
					return True
		return False


	def getPlayer(self,randx,randy):#return Player:
		for obj in self.teleportObjects:
			if isinstance(obj,Player):
				pos = obj.pos
				if pos.x == randx and pos.y == randy:
					return obj

		return None

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
			t = self.teleportObjects[turn]
			if t.health > 0:
				t.askForMove()
				print(" ")
			turn = (turn + 1) % SurvivalGame.n

			numOfAlivePlayers = 0

			for i in range(SurvivalGame.n):
				if self.teleportObjects[i].health > 0:
					numOfAlivePlayers+=1
		print"Game over."
		self.printBoard()
			








game=SurvivalGame()
game.gameStart()


