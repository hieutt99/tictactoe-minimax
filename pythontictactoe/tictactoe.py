import board
import gameplay

Player_Letter, Computer_Letter = gameplay.getPlayerLetter()
play_field = board.field
gameplay.printBoard(play_field)

game_status = gameplay.checkBoardFull(play_field)

while game_status == False :
	move = gameplay.getPlayerMove(play_field)
	print('letter above is players move')
	gameplay.fillTheBoard(play_field, move, Player_Letter)
	gameplay.printBoard(play_field)

	game_status=gameplay.checkPlayerWin(play_field,Player_Letter)
	if game_status == True:
		print('Player Won')
		break
	game_status = gameplay.checkBoardFull(play_field)
	if game_status == True :
		print('The game has end with the tie')
		break

	computer_move = gameplay.getComputerMove(play_field,move)
	print('letter above is computer move')
	gameplay.fillTheBoard(play_field, computer_move, Computer_Letter)
	gameplay.printBoard(play_field)

	game_status=gameplay.checkComputerWin(play_field,Computer_Letter)
	if game_status == True:
		print('Computer Won')
		break
	game_status = gameplay.checkBoardFull(play_field)
	if game_status == True:
		print('The game has end with the tie')
		break
else :
	print('The game has end with the tie')






















