#code by minari
#October 2019

import copy
import board

#========================================================================
#==================PLAY FIELD============================================
def printBoard(play_field):
		print(play_field[1] + '|' + play_field[2] + '|' + play_field[3])
		print('-+-+-')
		print(play_field[4] + '|' + play_field[5] + '|' + play_field[6])
		print('-+-+-')
		print(play_field[7] + '|' + play_field[8] + '|' + play_field[9])
def fillTheBoard(play_field, the_move, letter) :
	for key in play_field.keys():
		if key == the_move:
			play_field[the_move] = letter
def checkBoardFull(play_field):
	for i in range(1,9):
		if play_field[i] ==' ' :
			return False 
	return True
def checkMoveInBoard(play_field,move):
	for key, value in play_field.items():
		if key == move and value == ' ':
			return False
		elif key == move and value != ' ':
			return True
def getBoardCopy(play_field):
	board = copy.copy(play_field)
	return board
#==================CHECK WIN=============================================
def checkPlayerWin(play_field,letter):
	temp = letter
	return ((play_field[7]==temp and play_field[8]==temp and play_field[9]==temp) or 
	        (play_field[4]==temp and play_field[5]==temp and play_field[6]==temp) or 
	        (play_field[1]==temp and play_field[2]==temp and play_field[3]==temp) or 
	        (play_field[7]==temp and play_field[4]==temp and play_field[1]==temp) or
            (play_field[8]==temp and play_field[5]==temp and play_field[2]==temp) or
	        (play_field[9]==temp and play_field[6]==temp and play_field[3]==temp) or
	        (play_field[7]==temp and play_field[5]==temp and play_field[3]==temp) or
	        (play_field[9]==temp and play_field[5]==temp and play_field[1]==temp))
def checkComputerWin(play_field,letter):
	temp = letter
	return ((play_field[7]==temp and play_field[8]==temp and play_field[9]==temp) or 
	        (play_field[4]==temp and play_field[5]==temp and play_field[6]==temp) or 
	        (play_field[1]==temp and play_field[2]==temp and play_field[3]==temp) or 
	        (play_field[7]==temp and play_field[4]==temp and play_field[1]==temp) or
	        (play_field[8]==temp and play_field[5]==temp and play_field[2]==temp) or
	        (play_field[9]==temp and play_field[6]==temp and play_field[3]==temp) or
	        (play_field[7]==temp and play_field[5]==temp and play_field[3]==temp) or
	        (play_field[9]==temp and play_field[5]==temp and play_field[1]==temp))
#==================GET LETTER============================================
def getPlayerLetter():
	letter = ''
	print('Choose your letter : X or O ?')
	letter = input().upper()
	if letter == 'X' :
		print('You are X and Computer is O')
		return['X','O']
	elif letter == 'O' :
		print('You are O and Computer is X')
		return['O','X']
	else : 
		print('You have not choose the letter')
		getPlayerLetter()
#==================PLAYER MOVE===========================================
def checkPlayerMove(play_field,move):
	if move in range(1,10):
		return True
	else:
		return False
	if checkMoveInBoard(play_field,move) == True :
		return False
	else :
		return True
def getPlayerMove(play_field):
	move = int(input())
	while checkPlayerMove(play_field,move) == False :
		move = int(input())
		checkPlayerMove(play_field,move)
	else : 
		return move

#============================TEMP========================================
def checkEndGame(play_field,Player_Letter,Computer_Letter):
	if checkPlayerWin(play_field,Player_Letter) == True or checkComputerWin(play_field,Computer_Letter) == True:
		return True
	elif checkBoardFull(play_field) == True :
		return True
	else :
		return False
#========================================================================
class Tree(object):
	def __init__(self, move = None,depth = -1, grade = 0):
		self.children = []
		self.move = move
		self.grade = grade
		self.depth = depth 
	def checkGrade(self,Player_Letter,Computer_Letter):
		if checkComputerWin(self.move,Computer_Letter) == True :
			return -1
		elif checkPlayerWin(self.move,Player_Letter) == True :
			return 1
		else :
			return 0
	def setGrade(self,Player_Letter,Computer_Letter):
		if checkComputerWin(self.move,Computer_Letter) == True :
			self.grade = 1
		elif checkPlayerWin(self.move,Player_Letter) == True :
			self.grade = -1
		else :
			self.grade = 0
	
	def add(self,node):
		assert isinstance(node,Tree)
		self.children.append(node)
class Tree2(object):
	def __init__(self, move = None,depth = -1, grade = 0):
		self.children = []
		self.move = move
		self.grade = grade
		self.depth = depth 
	def checkGrade(self,Player_Letter,Computer_Letter):
		if checkComputerWin(self.move,Computer_Letter) == True :
			return -1
		elif checkPlayerWin(self.move,Player_Letter) == True :
			return 1
		else :
			return 0
	def setGrade(self,Player_Letter,Computer_Letter):
		if checkComputerWin(self.move,Computer_Letter) == True :
			self.grade = -1
		elif checkPlayerWin(self.move,Player_Letter) == True :
			self.grade = 1
		else :
			self.grade = 0
	
	def add(self,node):
		assert isinstance(node,Tree2)
		self.children.append(node)
#========================================================================
#traverse
def printTree_pre(tree):
	if tree == None : 
		print("Tree is empty")
		return
	else :
		printBoard(tree.move)
		print(tree.grade)

		print("============")
		for i in range(len(tree.children)):
			printTree_pre(tree.children[i])
#========================================================================
chosen = getBoardCopy(board.field)
def minimax(position,depth,maximizing,Player_Letter,Computer_Letter):
	eval = position.grade
	if depth == 0 or checkEndGame(position.move,Player_Letter,Computer_Letter) == True : 
		# print("gia tri cua minimax : "+str(eval))
		return eval
	if maximizing == True:
		maxEval = -10000
		for child in position.children:
			eval = minimax(child,depth-1,False,Player_Letter,Computer_Letter)
			maxEval = max(maxEval,eval)
			position.grade = maxEval
		return position.grade
	elif maximizing == False:
		minEval = 10000
		for child in position.children:
			eval = minimax(child,depth-1,True,Player_Letter,Computer_Letter)
			minEval = min(minEval,eval)
			position.grade = minEval
		return position.grade

#==================COMPUTER MOVE=========================================
def availableMoves(play_field,letter):
	available = []
	for i in range(1,10):
		if checkMoveInBoard(play_field,i) != True : 
			temp = getBoardCopy(play_field)
			fillTheBoard(temp,i,letter)
			available.append(temp)
	if(len(available) == 0):
		return None
	return available

def test(play_field,Player_Letter,Computer_Letter):
	print("=================================")
	print("DAY LA HAM TEST")
	d = 4
	t = Tree(move = play_field, depth = d)
	stack = []
	stack.append(t)
	top = 0
	
	letter = [Computer_Letter,Player_Letter]
	
	while top != -1 :
		temp = stack.pop(top)
		top = top - 1

		d = temp.depth
		# print("o day depth bang : "+str(d))
		index = d%2 - 1
		# print("index : " + str(index) + "   depth : "+str(d))
		
		if availableMoves(temp.move,letter[index]) != None and checkEndGame(temp.move,letter[1],letter[0])==False: 
			d -= 1
			# print("o day nay depth bang : "+str(d))
			for child in availableMoves(temp.move,letter[index]):
				temp.add(Tree(move = child, depth = d))
			for i in temp.children:
				stack.append(i)
			top = top + len(temp.children)
		else :
			temp.setGrade(Player_Letter,Computer_Letter)
		print("==========================")
		print("in ra stack : ")
		for i in range(len(stack)):
			printBoard(stack[i].move)
			print("---------------")
		print("==========================")
		print(top)
		print(len(stack))
	print("nhap xog vao tree")
	print("test nuoc di : ")

	d = 7
	move = minimax(t,d,True,Player_Letter,Computer_Letter)
	printTree_pre(t)
	for i in t.children :
		if(i.grade == t.grade):
			chosen = getBoardCopy(i.move)
	return chosen

	# print(t.children[0].checkGrade(Player_Letter,Computer_Letter))
	# print(t.children[1].children[1].checkGrade(Player_Letter,Computer_Letter))
	# print(t.children[2].checkGrade(Player_Letter,Computer_Letter))

	
# def getComputerMove(play_field):
# 	print("=================================")
# 	print("cac nuoc available cho computer : ")
# 	available = availableMoves(play_field)
# 	for aval in available:
# 		printBoard(aval)
# 		print("====================")
# 	print("chon nuoc di phu hop cho computer : ")
# 	computer_move = getPlayerMove(play_field)
# 	return computer_move

#======================VARIABLES=========================================
# Player_Letter, Computer_Letter = gameplay.getPlayerLetter()
Player_Letter, Computer_Letter = ['X','O']
play_field = board.field5
game_status = checkBoardFull(play_field)
game_status = False



#=========================================================================
print("===========================TEST MOVE=========================")
while game_status == False :
	# move = getComputerMove(play_field)
	# print('letter above is Computer move')
	# fillTheBoard(play_field, move, Computer_Letter)
	# printBoard(play_field)
	chosen = test(play_field,Computer_Letter,Player_Letter)
	printBoard(chosen)
	# stack = []
	# t = Tree(play_field)
	# for i in range(10):
	# 	stack.append(t)
	# for i in range(10):
	# 	printBoard(stack[i].move)
	# print(checkEndGame(board.field2,Player_Letter,Computer_Letter))
	game_status = True
	if game_status == True:
		print('End test')
		print("=================================================")

#======================MAIN===============================================
# while game_status == False :
# 	move = test2(play_field,Computer_Letter,Player_Letter)
# 	print('letter above is Computer2 move')
# 	play_field = getBoardCopy(move)
# 	printBoard(play_field)

# 	game_status=checkPlayerWin(play_field,Player_Letter)
# 	if game_status == True:
# 		print('Computer 2 Won')
# 		break
# 	game_status = checkBoardFull(play_field)
# 	if game_status == True :
# 		print('The game has end with the tie')
# 		break

# 	move = test(play_field,Player_Letter,Computer_Letter)
# 	print('letter above is Computer move')
# 	play_field = getBoardCopy(move)
# 	printBoard(play_field)

# 	game_status=checkComputerWin(play_field,Computer_Letter)
# 	if game_status == True:
# 		print('Computer  Won')
# 		break
# 	game_status = checkBoardFull(play_field)
# 	if game_status == True:
# 		print('The game has end with the tie')
# 		break
# else :
# 	print('The game has end with the tie')
#===========================================================================
