import os

board = ["-","-","-",
		"-","-","-",
		"-","-","-"]
gameStillGoing = True
currentPlayer = "X"
position = None
winner = "Nobody"

def displayBoard():
	print("")
	print("")
	print(board[0]+" | "+board[1]+" | "+board[2] + "     1 | 2 | 3") 
	print(board[3]+" | "+board[4]+" | "+board[5] + "     4 | 5 | 6") 
	print(board[6]+" | "+board[7]+" | "+board[8] + "     7 | 8 | 9") 



def handleTurn():
	global position
	print("")
	print(currentPlayer+"'s turn")
	print("")
	position = input("Enter Position from 1 to 9 ")
	validate()	
	position = int(position)-1
	while board[position] != "-":
		validate()
	board[position] = currentPlayer

def fipPlayer():
	global currentPlayer
	if (currentPlayer=="X"):
		currentPlayer="O"
	elif(currentPlayer=="O"):
		currentPlayer = "X"

def validate():
	global position
	while position not in ["1","2","3","4","5","6","7","8","9"]:
		position = input("Enter Position from 1 to 9 ")
		position = int(position) - 1
		return position
	
def checkWin():
	global gameStillGoing
	global winner

	row1 = board[0] == board[1] == board[2] != "-" 
	row2 = board[3] == board[4] == board[5] != "-"
	row3 = board[6] == board[7] == board[8] != "-"

	col1 = board[0] == board[3] == board[6] != "-"
	col2 = board[1] == board[4] == board[7] != "-"
	col3 = board[2] == board[5] == board[8] != "-" 

	diag1 = board[0] == board[4] == board[7] != "-"
	diag2 = board[2] == board[4] == board[6] != "-"

	if(row1 or row2 or row3):
		gameStillGoing = False
		if row1: 
			winner = board[0]
		elif row2: 
			winner = board[3]
		elif row3:
			winner = board[6]

	elif(col1 or col2 or col3):
		gameStillGoing = False
		if col1: 
			winner = board[0]
		elif col2: 
			winner = board[1]
		elif col3:
			winner = board[2]

	elif(diag1 or diag2):
		gameStillGoing = False
		if diag1: 
			winner = board[0]
		elif diag2: 
			winner = board[2]

def playgame():
	while gameStillGoing:
		os.system('cls')
		displayBoard()
		handleTurn()
		fipPlayer()
		checkWin()
		os.system('cls')
		displayBoard()
		
		print("Game Over " + winner + " Won")
k = None
playgame()
print("")
print("")
print("")
k = input("press enter key to exit")

