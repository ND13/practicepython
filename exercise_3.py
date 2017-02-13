a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for loop goes through each number in our list, numbers in our list < 5 get printed
for num in a:
	if num < 5: 
		print(num) 

		

''' Extra Challenge Part 1 '''
# empty list to hold our new values
b = []

#for and if statement are same as above, b.append(num) adds our numbers less than 5 to our new list
for num in a:
	if num < 5:  
		b.append(num)
print(b)



''' Extra Challenge Part 2 '''
#Found this a bit tricky, had to study list comprehensions.
b_2 = [num for num in a if num < 5]
print(b_2)



''' Extra Challenge Part 3 '''
b_3 = []

user_num = int(input('Please enter a number: '))

#Same as the other loops just changing the 5 to the user_num variable in the if
for num in a:
	if num < user_num:
		b_3.append(num)
print(b_3)
