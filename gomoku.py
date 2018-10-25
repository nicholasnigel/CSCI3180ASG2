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
import sys
import abc 
import random



class Gomoku(object):

	#initializing self
	def __init__(self):
		#initalize instance variables: gameboard,players,and turn
		self.gameBoard= [[0 for x in range(9)] for y in range(9)]
		#just for initialization purpose
		self.player1=1
		self.player2=2

		#turn changes between 1 or -1, 1 for player 1, -1 for player 2
		self.turn=1
		#rowCheck and colCheck is for check win and check draw purpose
		self.rowCheck=0
		self.colCheck=0



	#creating object depending on num and return the object
	def createPlayer(self,symbol,playerNum):
		#print"successful creation"
		#if player num 1 : create object human
		#if player num 2 : create cobjet computer
		if playerNum==1:
			playerTemp = Human(symbol,self.gameBoard)

		elif playerNum==2:
			playerTemp= Computer(symbol,self.gameBoard)

		return playerTemp	
	
	def startGame(self):
		#create players
		self.playerPrompt()
		#initial look
		self.printGameBoard()
		
		#after players have been created, then start the game

		#game goes on until either win or draw
		

		while self.checkWin()==False and self.checkTie()==False:
			#if turn=1, playerO move , if -1, player X
			if self.turn==1:
				coordinate=self.player1.nextMove()
				#coordinate should be a list where 0 = row, 1 = col
				self.gameBoard[coordinate[0]-1][coordinate[1]-1]='O'
				self.printGameBoard()
				self.turn=self.turn* -1
				self.rowCheck=coordinate[0]-1
				self.colCheck=coordinate[1]-1
				

			elif self.turn==-1:
				coordinate=self.player2.nextMove()
				#coordinate should be a list where 0 = row, 1 = col
				self.gameBoard[coordinate[0]-1][coordinate[1]-1]='X'
				self.printGameBoard()
				self.turn = self.turn * (-1)
				self.rowCheck=coordinate[0]-1
				self.colCheck=coordinate[1]-1
				
		




	def printGameBoard(self):
		#header:
		print" | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
		print"--------------------------------------"
		#loop for 1 to 9 row including its content

		for i in range(9):
			sys.stdout.write("%d"%(i+1))
			sys.stdout.write("|")
			for j in range(9):
				if self.gameBoard[i][j] == 0:
					self.gameBoard[i][j] = ' '
				sys.stdout.write(" %s |"%self.gameBoard[i][j])	
			sys.stdout.write("\n")
			sys.stdout.flush()
			print "-"*36	
					

	def checkWin(self):
		#win condition: for a certain symbol, they have 5 in a row
		#horiontally,vertically,or diagonally
		""""
		Algorithm:
			For every row that is recently put, check all directions
			whether it makes 5 in a row.
			return for each direction true/false
		"""
		if(self.checkHorizontal()==True):
			print("horizontal win!")
			if self.turn==1:
				print("Game ends. Player X wins")
			else:
				print("Game ends. Player O wins")
			return True
		if(self.checkVertical()==True):
			print("Vertical win!")
			if self.turn==1:
				print("Game ends. Player X wins")
			else:
				print("Game ends. Player O wins")
			return True
		if(self.checkDiagonal()==True):
			print("Diagonal win!")
			if self.turn==1:
				print("Game ends. Player X wins")
			else:
				print("Game ends. Player O wins")
			return True	
		
		return False


	def checkHorizontal(self):
		row=self.rowCheck
		col=self.colCheck
		sym=self.gameBoard[row][col]
		
		if sym!='O' and sym!='X':
			return False

		
		#same row different col
		#from col-4 to col
		for i in range(col-4,col+1):
			count=0
			if i<0:
				pass

			elif not self.gameBoard[row][i] == sym:
				pass

			
				
			else:
				for j in range(4):
					if i+j+1>8:
						break
					elif not self.gameBoard[row][i+j+1]==sym:
						break
					elif self.gameBoard[row][i+j+1]==sym:
						count+=1

				if count==4:
					print("5 in a row")
					return True		
			





		return False			
				



	def checkVertical(self):
		row=self.rowCheck
		col=self.colCheck
		sym=self.gameBoard[row][col]
		if sym!='O' and sym!='X':
			return False
		#same col different row
		for i in range(row-4,row+1):
			count=0
			if i<0:
				pass

			elif not self.gameBoard[i][col] == sym:
				pass

			
				
			else:
				for j in range(4):
					if i+j+1>8:
						break
					elif not self.gameBoard[i+j+1][col]==sym:
						break
					elif self.gameBoard[i+j+1][col]==sym:
						count+=1

				if count==4:
					return True		
			

		return False


	def checkDiagonal(self):
		row=self.rowCheck
		col=self.colCheck
		sym=self.gameBoard[row][col]
		if sym!='O' and sym!='X':
			return False
		#upright,downright,downleft,upleft
		# \ orientation
		i=row-4
		j=col-4
		while i<=row and j<=col:
			count=0

			if i<0 or j<0:
				pass

			elif not self.gameBoard[i][j] == sym:
				pass

			else:
				for k in range(4):
					if i+k+1>8 or j+k+1>8:
						break
					elif not self.gameBoard[i+k+1][j+k+1]==sym:
						break
					elif self.gameBoard[i+k+1][j+k+1]==sym:
						count+=1
			if count==4:
				
				return True
			i+=1
			j+=1
		
		i=row+4
		j=col-4

		while i>=row and j<=col:
			count=0

			if i>8 or j<0:
				pass

			elif not self.gameBoard[i][j] == sym:
				pass 


			else:
				for k in range(4):
					if i-k-1<0 or j+k+1>8:
						break
					elif not self.gameBoard[i-k-1][j+k+1]==sym:
						break
					elif self.gameBoard[i-k-1][j+k+1]==sym:
						count+=1
			if count==4:
				
				return True

			i-=1
			j+=1
		
		return False						




	

	def checkTie(self):
		#tie condition: if the table is filled and no result of winning:
		for i in range(9):
			for j in range(9):
				if(self.gameBoard[i][j]== " "):
					return False

		if self.checkWin()==False:
			print("Tie Game!")
			return True
		return False

	

	#function to prompt user and setting up player
	def playerPrompt(self):
		#print"player prompt"
		map = { 1: 'Human', 2: 'Computer'}

		print("Please choose player 1 (O) :")
		print("1. Human")
		print("2. Computer Player")

		playerOnum = input("Your choice is: ")

		print"Player O is",map[playerOnum],".", '\n'
		
		self.player1 = self.createPlayer('O',playerOnum)

		print("Please choose player 1 (X) :")
		print("1. Human")
		print("2. Computer Player")

		playerXnum = input("Your choice is: ")
		print "Player X is", map[playerXnum],".", '\n'
		self.player2 = self.createPlayer('X',playerXnum)






class Player(object):
	__metaclass__= abc.ABCMeta
	def __init__(self,symbol,gameboard):
		self.playerSymbol=symbol
		self.gameboard=gameboard
	
	@abc.abstractmethod
	def nextMove(self):
		return




"""""
	 Classes to categorize type of player
"""
class Human(Player):
	def __init__(self, symbol, gameboard):
		print"created human object"
		super(Human,self).__init__(symbol,gameboard)

	def nextMove(self):
		#show which player's turn
		print("Player %s's turn!" % self.playerSymbol)
		#prompt user and ask for 2 inputs
		row,col=raw_input("Type the row and col to put the disc:   ").split()
		#convert to int
		row=int(row)
		col=int(col)

		while(not self.gameboard[row-1][col-1]== ' '):
			print("Invalid input!")
			print("Player %s's turn!" % self.playerSymbol)
			row,col=raw_input("Type the row and col to put the disc:   ").split()
			row=int(row)
			col=int(col)

		return row,col

class Computer(Player):
	def __init__(self,symbol,gameboard):
		print"created computer object"
		super(Computer,self).__init__(symbol,gameboard)		

	def nextMove(self):
		print("Player %s's turn!" % self.playerSymbol)

		row=random.randint(1,9)
		col=random.randint(1,9)

		while(not self.gameboard[row-1][col-1]== ' '):
			row=random.randint(1,9)
			col=random.randint(1,9)
		print("computer chooses cell: %d %d"%(row,col))
		return row,col


""""sys.stdout.write('abc')
sys.stdout.write('def')
sys.stdout.flush()"""

game = Gomoku()
game.startGame()
#prompt:


