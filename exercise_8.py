#using getpass to hide user input
import getpass

def play_game():
	player_1 = getpass.getpass('Player 1, choose rock, paper, or scissors: ').lower()
	player_2 = getpass.getpass('Player 2, choose rock, paper, or scissors: ').lower()
	print('')
	print('Player 1 chose: ' + player_1)
	print('Player 2 chose: ' + player_2)
	print('')

	if player_1 == 'rock' and player_2 == 'scissors':
		print('Player 1 wins!')
	elif player_1 == 'paper' and player_2 == 'rock':
		print('Player 1 wins')
	elif player_1 == 'scissors' and player_2 == 'paper':
		print('Player 1 wins')
	elif player_2 == 'rock' and player_1 == 'scissors':
		print('Player 2 wins!')
	elif player_2 == 'paper' and player_1 == 'rock':
		print('Player 2 wins')
	elif player_2 == 'scissors' and player_1 == 'paper':
		print('Player 2 wins')
	elif player_1 == player_2:
		print('Tie game!')
	else:
		print("Oops! Invalid input! Start over.")
	print('')

def keep_playing():
	while True:
		play_again = input('To play rock, paper, scissors, type a or type q to quit: ').lower()

		if play_again == 'a':
			play_game()
		elif play_again == 'q':
			break
		else:
			print('Oops invalid input!')

keep_playing()
