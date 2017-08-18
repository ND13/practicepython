def beg_end_list(some_list):
	new_list = [some_list[0], some_list[-1]]
	return new_list

a = [5, 10, 15, 20, 25]

print(beg_end_list(a))

