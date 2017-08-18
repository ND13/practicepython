import random

number = random.randint(1,9)
num_of_guess = 0
guess = 0

while guess != exit and number:
	
	guess = input('Enter a number as your guess or type "exit" to quit: ')

	if guess == 'exit':
		exit()

	guess = int(guess)
	num_of_guess +=1

	if guess == number:
		print('Great job, you are correct!')
		print('This is how many time you had to guess to get the right answer: ' + str(num_of_guess))
		num_of_guess = 0
	elif guess < number:
		print('That is too low')
	elif guess > number:
		print('That is too high')
	else:
		print("That isn't valid input!")

'''Take note of where the variables are implemented, how they are converted, and how both of those factors
play a role in how the program works and makes decisions. Also line 20 is important for resetting the number
of guess variable back to 0 when a new round of guess starts. Without doing this the number of guesses will 
carry over from the previous session.'''
		

