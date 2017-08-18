def reverse_string(string):
	new_string = string.split()
	return " ".join(new_string[::-1])

user_string = input("Please enter a sentance to be reversed: ")

print(reverse_string(user_string))
