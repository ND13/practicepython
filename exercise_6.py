#converting to all lower case, in case of capitalized user input
a = input("Please enter a word: ").lower()

#if statement compares a to a[working through entire string backwards]
if a == a[::-1]:
	print('This is a palindrome')
else:
	print('This is not a palindrome')
