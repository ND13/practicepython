#gets input from user and converts to integer for easy use
def get_integer():
	return int(input('Please enter an integer: '))

#checks and tells prime status of numbers from user
def check_prime(user_num):
	#boolean value for checking prime values
	is_prime = True
	#checks prime status and sets booleans accordingly
	if user_num == 1:
		is_prime = False
	elif user_num == 2:
		is_prime = True
	else:
		for i in range(2, user_num):
			if user_num % i == 0:
				is_prime = False

	if is_prime == True:
		print('This number is prime')
	else:
		print('This is not a prime number')

		
#calls functions then repeats program based on user input
while True:
	check_prime(get_integer())
	print()
	
	exit_program = input('To exit the program type "exit". To check another number type "check": ').lower().strip()

	if exit_program == 'exit':
		exit()
	elif exit_program == 'check':
		continue
	else:
		print('That is not valid input, program exiting now.')
		exit()
