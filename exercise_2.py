number = int(input('Please enter a number: '))

if number % 2 == 0: 
	print('This number is even!')
elif number % 4 == 0: # solution to extra challenge part 1
	print('This number is a multiple of 4!')
else:
	print('This number odd!')

# separate section for extra challenge part 2
num = int(input('Please enter a number: '))
check = int(input('Please enter a second number: '))

if num % check == 0:
	print('These numbers will divide evenly into each other.')
else:
	print('These numbers will no divide evenly into each other.')
