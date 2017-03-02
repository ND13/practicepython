def reverse_string(string):
	new_string = string[::-1]
	return new_string

user_string = input("Please enter a string to be reversed: ")

print(reverse_string(user_string))
