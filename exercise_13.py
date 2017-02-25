def get_int():
	user_int = int(input('Enter a number: '))
	return user_int

def fibbonaci(num_range):
	num_1 = 0
	num_2 = 1
	sum = 0

	for i in range(num_range):
		sum = num_1 + num_2
		print(sum)
		num_1 = num_2
		num_2 = sum

fibbonaci(get_int())
