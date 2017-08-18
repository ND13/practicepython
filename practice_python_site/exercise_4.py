#don't forget to convert user_num to int here
user_num = int(input("Please eneter a number: "))
#new technique for creating lists here.
a = list(range(1, user_num + 1))
#empty list to hold divisor values
b = []

#printing list here to make sure it populates correctly
print(a)

#loop through list a, check if user_num divides evenly, populate list b
for num in a:
	if user_num % num == 0:
		b.append(num)
#print list b for verification
print(b)
