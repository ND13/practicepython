user_num = int(input("Please eneter a number: "))
a = range(1, user_num)
b = []

for num in a:
	if user_num % num == 0:
		b.append(num)
print(b)
